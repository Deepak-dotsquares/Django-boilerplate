# Django REST Panel

## Project Overview

This project is a Django-based web application that provides a comprehensive site management panel with user authentication, email notifications, and various site-related tasks. It's designed to offer a robust and scalable solution for web applications and rest application requiring user management and site administration capabilities.

## Features

- **User Authentication** (Signup, Login, Forgot Password, Reset Password)
- **Site Management Panel** for handling site-related tasks and user management
- **Email Notifications** for user actions and system updates
- **RESTful API** built using Django Rest Framework
- **Cross-Origin Resource Sharing (CORS)** support for API requests across different domains
- **Environment-based configuration** using `django-environ`
- **Flexible filtering system** for easy data querying and management
- **Swagger API Documentation** for easier testing and exploring of API endpoints
- **Common Message Handling Approach** for centralized response messages across the app

## Project Structure

```
├── commonConf/
│   ├── EnumFile.py
│   ├── authentication.py
│   ├── choices.py
│   ├── messages.py
│   ├── request.py
│   ├── response_handler.py
│   ├── send_email.py
│   └── validator.py
├── configurations/
│   ├── asgi.py
│   ├── routing.py
│   ├── settings.py
│   ├── swagger.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   └── user.png
├── sitepanel/
│   ├── authentications/
│   │   ├── forgotpassword/
│   │   ├── login/
│   │   ├── resetpassword/
│   │   └── signup/
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── models.py
│   ├── notifications.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│ 
├── templates/
├── venv/
├── manage.py
└── requirements.txt
```

## Prerequisites

- Python 3.12
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add necessary environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`, etc.).

5. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the admin panel at `http://localhost:8000/admin/` using the superuser credentials.
2. Use the site panel for various management tasks.
3. Implement front-end applications to interact with the API endpoints.

## API Endpoints

(List and describe your main API endpoints here)

For example:
- **POST** `/api/signup/` - Register a new user
- **POST** `/api/login/` - User login
- **GET** `/api/users/` - List all users

## Configuration

The project uses `django-environ` for environment-based configuration. Key settings can be found in `configurations/settings.py`.

- `SECRET_KEY` - The secret key for signing cookies and session data
- `DATABASE_URL` - URL for the PostgreSQL database connection
- `CORS_ORIGIN_ALLOW_ALL` - CORS settings

## Swagger API Documentation

The project implements Swagger API documentation for testing and exploring API endpoints. Access it at:

```
http://localhost:8000/swagger/
```

## Common Message Handling Approach

This project follows a **common message handling approach** for managing response messages across the app. The messages are centralized in `commonConf/messages.py`, making it easy to update and maintain response messages across multiple views and APIs.

Example:

```python
# commonConf/messages.py
USER_CREATED_SUCCESSFULLY = "User was successfully created."
USER_AUTHENTICATED = "User authenticated successfully."
INVALID_CREDENTIALS = "Invalid username or password."
```

The response handler then uses these centralized messages to provide consistent feedback to users throughout the application.

## Testing

Run the test suite using:
```bash
python manage.py test
```

## Deployment

(Add instructions for deploying your Django application to production environments, such as setting up a production database, configuring settings for production, and deploying to platforms like Heroku or AWS.)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

(Specify the license under which this project is released)

## Contact

(Add your contact information or ways for users to reach out with questions or feedback)

## Acknowledgements

- Django
- Django Rest Framework
- django-cors-headers
- django-environ
- django-filter
- drf-yasg (for Swagger API Docs)
```

This version includes the Swagger documentation setup and the common message approach that you wanted to highlight. Let me know if you'd like to add or modify anything else!