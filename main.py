import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

## Заголовок сайта
st.title("Мой тренировочный сайт") # заголовок сайта
st.write("""
#### <-- Если загрузишь свой csv-файл, ниже появится твой график
""")

## Работа с библиотекой yfinance для получения информации о котировках APPLE
tickerSymbol = 'AAPL' # для каждой компании существует свой тикер, по Yahoo Finance, например
tickerData = yf.Ticker(tickerSymbol) # создаем объект Ticker для акции APPLE
tickerDF = tickerData.history(start='2023-01-01', end='2025-01-01') # Загрузка исторических данных в виде DataFrame за указанный период

# Создание графика котировок APPLE

# fig, ax = plt.subplots()
# sns.lineplot(data=tickerDF, x=tickerDF.index, y='Close', c='red')
# plt.title('Котировки APPLE')
# plt.xticks(rotation=90)
st.line_chart(data=tickerDF, y='Close')

# Создание графика по tips.csv

## Загрузка CSV файла, если файл загружен


uploaded_file = st.sidebar.file_uploader('Загрузи свой CSV файл', type='csv')
if uploaded_file is not None: # условие, чтобы сайт streamlit не ругался в моменте, когда файла еще нет
    df = pd.read_csv(uploaded_file) #сформировали DataFrame из загруженного csv-файла (read_csv автомат формирует DF)

    st.write(""" #### Здесь твой график
                        """)

    choice_x = st.sidebar.selectbox('Выбери, что будет по оси x', options=df.columns)
    choice_y = st.sidebar.selectbox('Выбери, что будет по оси y', options=df.columns)
    
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x=choice_x, y=choice_y)
    st.pyplot(fig)

    
    # нужно сохранить созданный график в байтовом формате:
    buffer = io.BytesIO()  # создаем буфер в памяти
    plt.savefig(buffer, format='png') # сохранили наш график в буфер в формате PNG
    image_bytes = buffer.getvalue() # получили байтовое содержимое буфера
    
    download_but = st.sidebar.download_button('Скачать готовый график', 
                                              data=image_bytes,
                                              file_name='final.png')

else:
    st.stop()


