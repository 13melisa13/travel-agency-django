# Используем базовый образ Python
FROM python:3.10

# Устанавливаем переменную окружения для отключения вывода сообщений Python
ENV PYTHONUNBUFFERED 1

# Создаем и переходим в рабочую директорию /app
WORKDIR /app

# Копируем файлы зависимостей (requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости через pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY app/ /app/

# Запускаем Django приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]