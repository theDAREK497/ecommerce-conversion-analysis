# Анализ данных конверсии сайтов  

## Описание  
Проект демонстрирует анализ метрик конверсии сайтов:  
- Время загрузки страниц  
- Конверсия по типу устройств  
- Визуализация данных через Streamlit  

## Технологии  
- Python (Pandas, Matplotlib, Streamlit)  
- Jupyter Notebook  
- CSV-данные  

## Установка  
1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/yourusername/ecommerce-conversion-analysis.git
   ```  
2. Установите зависимости:  
   ```bash
   pip install -r requirements.txt
   ```  

## Запуск  
### 1. Анализ данных (Jupyter)  
```bash
cd notebooks/
jupyter notebook
```  

### 2. Дашборд (Streamlit)  
```bash
streamlit run app/dashboard.py
```  

## Структура проекта  
```
├── data/               # Исходные данные  
├── notebooks/          # Jupyter-анализ  
├── src/                # Скрипты обработки данных  
├── app/dashboard.py    # Streamlit-интерфейс  
└── requirements.txt    # Зависимости  
```  

## Примеры  
### Метрики:  
- Среднее время загрузки: `2.5 сек`  
- Конверсия: `40%`  

### Графики:  
- Конверсия по устройствам (desktop/mobile)  
- Время загрузки vs Bounce Rate  

## Лицензия  
Apache License

