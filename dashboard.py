import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='My Dashboard',layout='wide')
st.title("Perilaku Konsumsi Makanan di Area Urban di Indonesia")

data = pd.read_excel('data/indo food consumption.xlsx')


#------------ Sidebar --------------
st.sidebar.subheader("Pengaturan Visualisasi")
selection_degree = st.sidebar.selectbox('Education Level:',list(data['Education Level'].unique()))
warna = st.sidebar.color_picker("Pilih Warna","#0000FF")

_,baris_col,_ = st.columns(3)
baris_col.metric('Total Responden', len(data))

#------------ Baris 1 --------------
baris1_col1,baris1_col2,baris1_col3 = st.columns((2,2,1))

## -- Plot 1 --
fig1,ax1 = plt.subplots()

data.groupby('City').mean()['% Monthly Food Expense'].sort_values(ascending=False).plot(kind='bar',ax=ax1, color=warna)

ax1.set_xlabel('Kota') #Set keterangan sumbu x
ax1.set_ylabel('% Pengeluaran Makanan terhadap Total Pengeluaran')

baris1_col1.write('Rata-Rata % Pengeluaran Makanan Tiap Kota')
baris1_col1.pyplot(fig1)
## -- end Plot 1 --


## --Plot 2
selection_class = baris1_col3.radio('Social Class',['Lower Class','Middle Class','Upper Class'])
fig2,ax2 = plt.subplots()

socialclass_dat = data[data['Social Class']==selection_class] 
group_class = socialclass_dat['Price Factor'].value_counts()
group_class.plot(kind='pie',ax=ax2)

baris1_col2.write('Price Food dan {}'.format(selection_class))
baris1_col2.pyplot(fig2)
## --end Plot 2

#-------------- Baris 2 -------------
fig3, ax3 = plt.subplots(figsize=(18,5))
st.write('Pengaruh Level Pendidikan terhadap Faktor Kesehatan dalam Pemilihan Makanan')
data[data['Education Level']==selection_degree]['Health Factor'].value_counts().sort_values(ascending=False).plot(kind='bar', label=selection_degree, color = warna)
ax3.legend()
st.pyplot(fig3)