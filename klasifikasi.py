# -*- coding: utf-8 -*-
"""klasifikasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/108yV-jhyhpEkvP1H9eybRhN1ppBaP3qT
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

"""# Gabung seluruh data"""

main_path = 'data'
files = os.listdir(main_path)

df = pd.read_csv(os.path.join(main_path, files[0]))
for i in files[1:]:

    temp = pd.read_csv(os.path.join(main_path, i))
    df = pd.concat([df, temp], ignore_index=True)

df.head()

"""# Data cleaning

## Menggantikan nilai yang mencerminkan ketiadaan data menjadi Null
"""

for i in df.columns[1:]:

    df[i] = df[i].replace({"---":None})
    df[i] = df[i].replace({'NaN':None})
    df[i] = df[i].replace({'TIDAK ADA DATA':None})

"""## Mengganti tipe data dan mengganti Nol menjadi Null"""

for i in [i for i in df.columns[3:8]] + ['pm25']:

    df[i] = df[i].astype(float)
    df[i] = df[i].replace({0:None})
    df[i] = df[i].astype(float)

df.info()

"""## Menghilangkan beberapa kolom dan menghilangkan data kosong"""

df = df[['stasiun', 'pm25'] + [i for i in df.columns[3:8]] + ['categori']]

"""# Exploratory data analysis

## Menghilangkan missing value dan outliers
"""

df.head()

df.dropna(inplace=True)

for i in df.columns[1:-1]:

    df.plot.box(y=i)

q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3 - q1
df = df[~((df < (q1 - 1.5 * iqr)) | (df > (q3 + 1.5 * iqr))).any(axis=1)]

"""### Info data setelah dibersihkan"""

df.info()

"""### Deskripsi data"""

df.describe()

"""## Univariative data analysis"""

for feature in ['stasiun', 'categori']:

    count = df[feature].value_counts()
    percent = 100 * df[feature].value_counts(normalize=True)

    data = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
    print(data)
    data.plot(y='jumlah sampel',
              kind='bar',
              title=feature)

df[1:-1].hist(bins=50, figsize=(20,15))
plt.show()

"""## Multivariative data analysis"""

agg = dict(zip([i for i in df.columns[1:-1]], ['mean' for i in range(6)]))
data = df.groupby('categori').agg(agg)
print(data)

for i in data.columns:
    data.plot.bar(y=i,
                  color=['g','y','r'])

agg = dict(zip([i for i in df.columns[1:-1]], ['mean' for i in range(6)]))
data = df.groupby('stasiun').agg(agg)

for i in data.columns:
    data.plot.bar(y=i,
                  color=['r', 'b', 'g', 'y', 'c'])

"""# Data Preparation

## Menghilangkan kolom stasiun
"""

df = df[df.columns[1:]]

"""## Mengganti data kategori menjadi numerik"""

replacement = dict(zip(df['categori'].drop_duplicates(), [i for i in range(3)]))
df['categori'] = df['categori'].replace(replacement)

"""## Normalisasi data numerik (bukan label)"""

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(df[df.columns[:-1]])
df[df.columns[:-1]] = scaler.transform(df.loc[:, df.columns[:-1]])

"""## Membagi data menjadi data latih dan data uji"""

from sklearn.model_selection import train_test_split as tts

x, y = df.drop(columns=['categori']), df['categori']
x_train, x_test, y_train, y_test = tts(x, y,
                                       random_state=20,
                                       test_size=0.2)

"""# Model development

## Menguji dan memilih ketiga model
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

"""## Mengimpor library metrik pengukuran"""

from sklearn.metrics import accuracy_score, precision_score, recall_score

models = [KNeighborsClassifier(),
          DecisionTreeClassifier(),
          RandomForestClassifier(),
          GaussianNB()]

hasil = {'model':[],
         'accuracy':[],
         'precision':[],
         'recall':[]}

for model in models:
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')

    hasil['model'].append(str(model))
    hasil['accuracy'].append(acc)
    hasil['precision'].append(prec)
    hasil['recall'].append(rec)

    print(str(model), acc)

"""# Evaluasi model"""

hasil = pd.DataFrame(hasil).sort_values(['accuracy', 'precision', 'recall'], ascending=False)
print(hasil)
hasil.plot.bar(x='model', color=['b', 'gold', 'r'], rot=0, figsize=(9,5))

"""# Model development part 2

## Melakukan upgrade yaitu hyperparameter tuning menggunakan randomized search cv
"""

from sklearn.model_selection import RandomizedSearchCV

n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
min_samples_split = [2, 5, 10]
min_samples_leaf = [1, 2, 4]
bootstrap = [True, False]

random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

clf = RandomForestClassifier()
clf_random = RandomizedSearchCV(estimator=clf,
                               param_distributions=random_grid,
                               n_iter=100,
                               cv=3,
                               verbose=2,
                               random_state=42,
                               n_jobs=-1)

clf_random.fit(x_train, y_train)
clf_random.best_params_

"""# Evaluasi model part 2

## Menguji ulang model dengan parameter yang sudah diupgrade
"""

args = clf_random.best_params_
clf = RandomForestClassifier(**args)
clf.fit(x_train, y_train)
clf.score(x_test, y_test)

"""## Menyimpan model"""

from pickle import dump

# dump(clf, open('classifier.pkl', 'wb'))