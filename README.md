# ToDo Project

A simple ToDo application built using Django and Django REST Framework.

## Features

- Create, read, update, and delete ToDos
- RESTful API endpoints for ToDos

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST Framework

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bonmvsk/todo_project.git
    cd todo_project
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    
3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
    
4. **Run migrations**:

    ```bash
    python manage.py makemigrations todo
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **ToDos**:
  - List and create ToDos: `GET /api/todos/`, `POST /api/todos/`
  - Retrieve, update, and delete a specific ToDo: `GET /api/todos/<id>/`, `PUT /api/todos/<id>/`, `DELETE /api/todos/<id>/`

## Project Structure

todo_project/  
├── manage.py  
├── todo_project/  
│ ├── init.py  
│ ├── asgi.py  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
└── todo/  
├── init.py  
├── admin.py  
├── apps.py  
├── models.py  
├── serializers.py  
├── tests.py  
├── urls.py  
└── views/  
├── init.py  
├── todo_views.py  
└── subtodo_views.py  
  
## Usage

- **Access the API**: Navigate to `http://127.0.0.1:8000/api/` to access the API endpoints.
- **Admin Panel**: Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials to manage ToDos through the Django admin interface.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
