# Flower Delivery Project

Проект представляет собой веб-приложение для заказа доставки цветов с интеграцией Telegram-бота для уведомлений о новых заказах.

## Описание проекта

Цель проекта — создать удобный сервис для заказа цветов с функционалом:
- Регистрация и авторизация пользователей.
- Просмотр каталога товаров (цветов).
- Добавление товаров в корзину и оформление заказа.
- Уведомления о новых заказах через Telegram-бота.

## Технологии

- **Backend**: Django 5.1.6
- **База данных**: SQLite (по умолчанию)
- **Telegram API**: python-telegram-bot
- **Frontend**: HTML, CSS (без JavaScript)

## Структура проекта
FlowerDelivery/
├── FlowerDelivery/ # Настройки проекта
│ ├── settings.py # Конфигурация Django
│ ├── urls.py # Основные маршруты
│ └── ...
├── products/ # Приложение для товаров
│ ├── models.py # Модели товаров
│ ├── views.py # Представления для каталога
│ └── templates/products/ # Шаблоны товаров
├── orders/ # Приложение для заказов
│ ├── models.py # Модели заказов
│ ├── views.py # Представления для корзины и оформления заказа
│ ├── forms.py # Формы для оформления заказа
│ ├── bot.py # Логика Telegram-бота
│ └── templates/orders/ # Шаблоны заказов
├── users/ # Приложение для пользователей
│ ├── models.py # Расширенная модель пользователя
│ ├── views.py # Регистрация и авторизация
│ └── templates/users/ # Шаблоны пользователей
├── static/ # Статические файлы (CSS, JS, изображения)
├── media/ # Медиафайлы (изображения товаров)
└── manage.py # Управление проектом


## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-repo/flower-delivery.git
cd flower-delivery

### 2. Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows

### 3. Установка зависимостей

pip install -r requirements.txt

### 4. Настройка переменных окружения

SECRET_KEY=your_django_secret_key
DEBUG=True
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

### 5. Применение миграций

python manage.py makemigrations
python manage.py migrate

### 6. Запуск сервера

python manage.py runserver

### 7. Запуск Telegram-бота

python run_bot.py

### Использование

Использование
Регистрация и авторизация :
Перейдите на страницу /register/ для регистрации.
Авторизуйтесь на главной странице.
Просмотр каталога :
Перейдите на страницу /products/, чтобы увидеть доступные товары.
Добавление в корзину :
Нажмите "Add to Cart" для добавления товара в корзину.
Оформление заказа :
Перейдите на страницу /orders/cart/, чтобы увидеть содержимое корзины.
Нажмите "Оформить заказ" и заполните форму.
Уведомления :
После оформления заказа вы получите уведомление в Telegram.

### Команды для разработки
python manage.py startapp app_name

### Лицензия
Этот проект распространяется под лицензией MIT. Подробности см. в файле LICENSE .

### Вклад
Если вы хотите внести свой вклад в проект, создайте pull request или откройте issue.


---

Этот `README.md` полностью готов к использованию. Вы можете скопировать его и вставить в ваш проект. Не забудьте заменить плейсхолдеры (например, `your-repo`, `your_django_secret_key`, `your_telegram_bot_token`, `your_telegram_chat_id`) на реальные значения.

