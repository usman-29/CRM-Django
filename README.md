# Django CRM with MySQL

Welcome to Django CRM with MySQL! This project is a Customer Relationship Management (CRM) system built using Django, where users can manage their information records effectively with MySQL as the database backend.

## Features

- **User Authentication**: Secure user authentication system allowing users to register, log in, and log out.
- **Record Management**: Users can add, delete, update, and view their information records conveniently.
- **Customizable**: Easily customizable for specific business needs or additional features.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone https://github.com/username/CRM-Django.git
   ```

2. **Install the required dependencies:**
   ```
   pip install django
   pip install mysqlclient
   ```

3. **Configure Django settings:**
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_mysql_host',
        'PORT': '3306', # Default MySQL port
    }
}
   ```

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the Django development server:**
   ```
   python manage.py runserver
   ```

6. **Access the application at** `http://localhost:8000` **in your web browser.**

## Usage

1. Register for a new account or log in if you already have one.
2. Once logged in, you can start adding, deleting, updating, and viewing your information records.
3. Explore the features and functionalities of Django CRM to manage your records efficiently.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.
