# Web Frameworks Assignment

This project demonstrates the implementation of two web applications using Flask and Django frameworks, with Docker containerization for easy deployment and testing.

## Project Overview

This assignment consists of three main parts:

1. **Flask Application**: A simple web app with a homepage and a form handling functionality
2. **Django Application**: A basic item management system with database integration and admin panel
3. **Docker Compose Setup**: Containerization of both applications to run simultaneously

## Project Structure

```
web-frameworks-assignment/
├── flask_app/              # Flask application
│   ├── app.py              # Main Flask application code
│   ├── templates/          # HTML templates
│   ├── Dockerfile          # Flask container configuration
│   └── requirements.txt    # Flask dependencies
├── django_app/             # Django application
│   ├── manage.py           # Django management script
│   ├── project/            # Project settings directory
│   ├── item_manager/       # Django app for item management
│   ├── Dockerfile          # Django container configuration
│   └── requirements.txt    # Django dependencies
├── docker-compose.yml      # Docker Compose configuration
└── README.md               # Documentation (this file)
```

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (optional, for cloning the repository)

## Running the Applications

### Option 1: Using Docker Compose (Recommended)

1. Clone or download this repository to your local machine
2. Open a terminal and navigate to the project root directory
3. Build and start the containers:

```bash
docker-compose up --build
```

4. Access the applications in your web browser:
   - Flask application: http://localhost:5000
   - Django application: http://localhost:8000
   - Django admin panel: http://localhost:8000/admin (username: admin, password: adminpass)

5. To stop the applications:
   - Press `Ctrl+C` in the terminal
   - Or run `docker-compose down` in another terminal

### Option 2: Running Applications Separately (for Development)

#### Flask Application

1. Navigate to the flask_app directory
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Flask application:
```bash
python app.py
```
5. Access the application at http://localhost:5000

#### Django Application

1. Navigate to the django_app directory
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```
6. Run the Django development server:
```bash
python manage.py runserver
```
7. Access the application at http://localhost:8000

## Features

### Flask Application

- Homepage: Displays a "Hello, World!" message
- Form page: Accepts user's name and age inputs
- Error handling: Validates inputs and displays appropriate error messages

### Django Application

- Homepage: Displays a list of items from the database
- Form: Allows adding new items directly from the homepage
- Admin panel: Provides full CRUD functionality for items

### Docker Setup

- Individual Dockerfiles for each application
- Docker Compose configuration for orchestrating both containers
- Port mapping to access applications from the host machine

## Troubleshooting

- If ports 5000 or 8000 are already in use on your system, you can modify the port mappings in the docker-compose.yml file
- For Django admin access issues, you can create a new superuser by running:
```bash
docker-compose exec django python manage.py createsuperuser
```

## License

This project is created for educational purposes.