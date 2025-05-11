import streamlit as st
import sys
import os

# Добавьте путь к папке src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.data_processing import load_data, calculate_metrics
from src.visualization import plot_conversion_by_device

st.title("SEO & Conversion Dashboard")

# Загрузка данных
df = load_data('data/sample_data.csv')

# Отображение метрик
metrics = calculate_metrics(df)
st.metric("Среднее время загрузки страницы", f"{metrics['avg_page_load']:.2f} секунд")
st.metric("Конверсия", f"{metrics['conversion_rate']:.2f}%")

# График конверсии по устройствам
st.subheader("Конверсия по типу устройства")
plot_conversion_by_device(df)
st.image('docs/images/conversion_by_device.png')

# Отображение данных
st.subheader("Исходные данные")
st.write(df)