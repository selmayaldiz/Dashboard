import streamlit as st
import pandas as pd

# Örnek veriler
data = {
    'Kredi Türü': ['Otomotiv', 'Poliçe Prim Kredisi', 'Perakende', 'Otomotiv - Filo', 'Otomotiv - Ticari', 'Otomotiv - Stok', 'Ticari Finansman - İhtiyaç Kredisi', 'Poliçe Prim Kredisi'],
    'Adet': [2, 0, 0, 1, 10, 5, 0, 0],
    'Tutar': [423500, 0, 0, 3200000, 8428665, 3766907, 0, 0],
    'Yaşayan Adet': [1013, 0, 2, 30, 967, 1299, 5, 29],
    'Yaşayan Tutar': [306789117, 0, 50000, 704280962, 748787544, 1156029660, 5603202, 1215793],
    'Toplam Adet': [1757, 25, 10, 97, 2066, 3787, 12, 78],
    'Toplam Tutar': [534205997, 171978, 292592, 1133455298, 1580282614, 2969905815, 10046127, 6006428],
    'Yaşayan Toplam Adet': [1309, 1, 9, 75, 1648, 286, 10, 36],
    'Yaşayan Toplam Tutar': [363550960, 3961, 173816, 922372282, 1082106103, 282960255, 6553948, 989139]
}

df = pd.DataFrame(data)

# Dashboard başlığı
st.title('Finansman Şirketi Dashboard')

# Genel Bakış
st.header('Genel Bakış')
total_credit = df['Toplam Tutar'].sum()
total_collections = df['Yaşayan Toplam Tutar'].sum()
st.metric(label='Toplam Kredi Hacmi', value=f'{total_credit:,} TL')
st.metric(label='Toplam Tahsilat', value=f'{total_collections:,} TL')
st.metric(label='Yeni Kredi Başvuruları', value='50')  # Bu veriyi manuel olarak girdim. Güncellenebilir.

#Operasyon Gunluk Basvuru Adet 
import streamlit as st
import pandas as pd

# Örnek veriler, dosyanızdaki verilere göre güncellenmiştir.
data = {
    'Başvuru Türü': ['Bireysel', 'Kurumsal', 'Stok/Filo', 'Ticari'],
    'Başvuru Adedi': [217, 37, 8, 29],
    'Başvuru Toplam Tutar': [104116952, 41714070, 7889570, 33824500],
    'Onaylanan Toplam Tutar': [21183200, 11097570, 7889570, 3208000],
    'Manuel Onay Oranı': ['39%', '26%', '-', '26%'],
    'Otomatik Onay Oranı': ['39%', '6%', '4%', '24%'],
    'Otomatik Ret Oranı': ['29%', '4%', '6%', '34%']
}

df = pd.DataFrame(data)

# Dashboard başlığı
st.title('Günlük Başvuru Raporu Dashboard')

# Genel Bakış
st.header('Genel Bakış')
total_applications = df['Başvuru Adedi'].sum()
total_amount = df['Başvuru Toplam Tutar'].sum()
total_approved_amount = df['Onaylanan Toplam Tutar'].sum()

st.metric(label='Toplam Başvuru Adedi', value=total_applications)
st.metric(label='Toplam Başvuru Tutarı', value=f'{total_amount:,} TL')
st.metric(label='Toplam Onaylanan Tutar', value=f'{total_approved_amount:,} TL')

# Başvuru Türüne Göre Detaylar
st.header('Başvuru Türüne Göre Detaylar')
st.table(df)

# Detaylı Grafikler
st.header('Başvuru ve Onay Oranları')
st.bar_chart(df.set_index('Başvuru Türü')[['Başvuru Adedi', 'Onaylanan Toplam Tutar']])

st.header('Onay ve Ret Oranları')
st.line_chart(df.set_index('Başvuru Türü')[['Manuel Onay Oranı', 'Otomatik Onay Oranı', 'Otomatik Ret Oranı']])

st.header('Başvuru Türlerine Göre Dağılım')
st.bar_chart(df.set_index('Başvuru Türü')['Başvuru Toplam Tutar'])


# Bireysel ve Kurumsal Krediler
st.header('Krediler')
st.table(df)

# Tahsilatlar
st.header('Tahsilatlar')
daily_collection = 50000  # Günlük tahsilat örnek verisi
overdue_collections = 3  # Gecikmiş tahsilatlar örnek verisi
st.metric(label='Günlük Tahsilat', value=f'{daily_collection:,} TL')
st.metric(label='Gecikmiş Tahsilatlar', value=overdue_collections)

# Finansal Veriler
st.header('Finansal Veriler')
st.line_chart(df[['Tutar', 'Yaşayan Tutar', 'Toplam Tutar', 'Yaşayan Toplam Tutar']])

# Satış Verileri
st.header('Satış Verileri')
st.bar_chart(df[['Adet', 'Yaşayan Adet', 'Toplam Adet', 'Yaşayan Toplam Adet']])
