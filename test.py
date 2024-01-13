conda env list
conda list
conda env export > enviroment.yaml

#tupras için yeni ortam oluşturma
conda create -n tupras_env

#şimdi bu yeni oluşan tupras env'ını aktive etmek gerekiyor.
conda activate tupras_env

#base'i orjin kabul ediyorsun .yaml dosyamı tupras_env için kullanıyorum.
conda env create -f enviroment.yaml

#hangi paketler var tekrar listeliyorum
conda list

#tüm paketleri güncelliyorum
conda upgrade -all

import numpy as np
import pandas as pd



df = pd.read_excel('C:/Users/Administrator/Desktop/tupras/shopping_trends_updated.xlsx', sheet_name = 'shopping_trends_updated')

#ilk 5 satırı consolda çıkarır.
df.head()

#sayısal değişkenler için ayrı bir tanımlama yapıyorsun
num_var= [col for col in df.columns if df[col].dtype != 'object']
num_var

#temel descritive(tamamlayıcı) fonksiyonlarını list'liyorsun
desc_agg = ['sum', 'mean', 'std', 'var','min','max']
desc_agg

#bu fonksiyonları sayısal değerlere uyguluyorum
desc_agg_dict = {col : desc_agg for col in df}
desc_agg_dict


import seaborn as sns

df.shape
#3900,18 kaç satır kaç kod görebiliyorsun.
df.info()

#Customer ID,Age,Gender,Item Purchased,Category,Purchase Amount (USD),Location,Size,Color,Season,Review Rating,Subscription Status,Shipping Type,Discount Applied,Promo Code Used,Previous Purchases,Payment Method,Frequency of Purchases  3900 non-null   object
df.columns

#missing value için extra kontrol yapılıyor false or true / false verdi
df.isnull().values.any()

#Her bir değişkene ait descriptive analytics değerleri bir tabloya yeniden yazdırıyorum
desc_summv2 = df.describe().T
print(desc_summv2)
df.info()

ortalama_age = df['Age'].mean()
print(f"Age sütununun ortalaması: {ortalama_age}") #44

df[df.Age > df.Age.mean()].Age.count() #1930  DataFrame'deki Age sütunundaki değerlerin ortalamasını aşan örneklerin sayısını bulmaktadır.
df[df.Age < df.Age.mean()].Age.count() #1970   Altında kalanları anlatıyor.

df.loc[df.Age > df.Age.mean(),'Purchase Amount (USD)'].head() #aynı şeyi purchase amount için yap edim ilk 5 satırı ver headle dedim

#sensor data
sensor = df.iloc[:, 1:18]
sensor #custom ıd almadı,
sensor.columns


import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#değişkenlerin grafiklerini çıkarma
sns.boxplot(x = sensor['Purchase Amount (USD)'])
plt.show()

def num_summary(sensor, numerical_col, plot=True):
    quantiles = [0.01, 0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95,0.99]#çeyreklikler
    print(sensor[numerical_col].describe(quantiles).T)

    if plot:
        sensor[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block= True)

num_summary(sensor,'Purchase Amount (USD)', plot=True)
num_summary(sensor,'Age',plot=True)
num_summary(sensor,numerical_col='Previous Purchases', plot=True)


# Gender'ın  dağılımı
sns.countplot(x='Gender', data=df)
plt.title('Cinsiyet Dağılımı')
plt.show()

# Category'nin dağılımı
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=df)
plt.title('Kategori Dağılımı')
plt.xticks(rotation=45)
plt.show()



#birbiri ile analizi
# 'Gender' değişkenine göre satın alma miktarının analizi
sns.barplot(x='Gender', y='Purchase Amount (USD)', data=df)
plt.title('Cinsiyet e Göre Satın Alma Miktarı')
plt.show()


# 'Category' değişkenine göre satın alma miktarının analizi
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Purchase Amount (USD)', data=df)
plt.title('Kategoriye Göre Satın Alma Miktarı')
plt.xticks(rotation=45)
plt.show()


# Yaşa göre satın alma miktarının scatter plot ile analizi
sns.scatterplot(x='Age', y='Purchase Amount (USD)', data=df)
plt.title('Yaşa Göre Satın Alma Miktarı Analizi')
plt.show()

# Yaşları grupla ve yaşa göre satın alma barplot
df['Age Group'] = pd.cut(df['Age'], bins=range(20, 90, 10), right=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='Purchase Amount (USD)', data=df)
plt.title('Yaşa Göre Satın Alma Miktarı')
plt.xlabel('Yaş Grubu')
plt.ylabel('Satın Alma Miktarı (USD)')
plt.show()



#gendera göre kategori
plt.figure(figsize=(8, 6))
sns.countplot(x='Category', hue='Gender', data=df)
plt.title('Gendera Göre Kategori Sayısı')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# 'Subscription Status' değişkenine göre satın alma miktarının analizi
plt.figure(figsize=(8, 5))
sns.barplot(x='Subscription Status', y='Purchase Amount (USD)', data=df)
plt.title('Abonelik Durumuna Göre Satın Alma Miktarı')
plt.show()


df['Age Group'] = pd.cut(df['Age'], bins=range(20, 90, 10), right=False)
plt.figure(figsize=(10, 6))
sns.countplot(x='Age Group', hue='Category', data=df)
plt.title('Yaş Gruplarına Göre Kategori Sayısı')
plt.xlabel('Yaş Grubu')
plt.ylabel('Sayı')
plt.legend(title='Kategori')
plt.show()














