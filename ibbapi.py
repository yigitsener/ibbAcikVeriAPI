# Kütüphaneler
import urllib # dataya erişim
import json # data formatının dönüşümü
import pandas as pd # analizler için

# IBB data kaynağındaki API adresi
# web sitesi https://data.ibb.gov.tr/dataset/ilce-bazinda-yillara-gore-dogalgaz-tuketim-miktari/resource/d5fe41b0-3848-4548-9ac7-6e4756c3027b
url = "https://data.ibb.gov.tr/datastore/odata3.0/d5fe41b0-3848-4548-9ac7-6e4756c3027b?$format=json"

def ibbVeriToDataframe(urladresi):
    # API bağlantısı
    sorgu = urllib.request.urlopen(urladresi)
    # Veriyi python-json dosya biçimine dönüştürme
    data = json.loads(sorgu.read().decode())
    # Sadece datanın olduğu bölümün alınması
    data = data.get("value")
    # Verinin dataframe formatına dönüştürülmesi
    return pd.DataFrame(data)

# fonksiyonun çalıştırılması
df = ibbVeriToDataframe(url)
# Data analiz için hazır
print(df.columns) # Kolon isimleri
df = df.drop(columns="_id") # ID kolonunun çıkarılması

# ilk 5 satır
df.head()

# Genel Bakış
print(df.info())

# Betimleyici istatistikler
print(df.describe())
