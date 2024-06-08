# Credit Card Service

## Overview

Credit Card Service is a Django application that allows users to manage loans, calculate credit scores, and handle billing cycles. It leverages Celery for asynchronous task processing and Redis as the message broker.

## Features

- User management with unique identifiers.
- Loan management including different loan types, amounts, and terms.
- Asynchronous tasks for calculating credit scores and running billing cycles.
- Integration with external CSV data for credit score calculations.

## Requirements

- Python 3.8+
- Django 3.2+
- Celery 5.0+
- Redis
- PostgreSQL (or any other database supported by Django)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/credit_card_service.git
    cd credit_card_service
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASES` setting in `CreditService/settings.py` to point to your database.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2. **Start the Redis server:**

    Ensure Redis is running on `localhost:6379`.

3. **Start the Celery worker:**

    ```bash
    celery -A CreditService worker --loglevel=info
    ```

## Usage

### Calculate Credit Score

You can calculate the credit score for a user using the following custom management command:

```bash
python manage.py calculate_credit_score <aadhar_id>
