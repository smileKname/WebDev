# Використовуємо офіційний образ Python
FROM python:3.10-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл з залежностями та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі інші файли проекту (включаючи app.py та index.html)
COPY . .

# Відкриваємо порт 5000
EXPOSE 5000

# Команда для запуску сервера
CMD ["python", "app.py"]