# Todo Project

A simple Todo application built with Django, allowing users to manage tasks with features to create, edit, delete, and prioritize tasks.

## Project Structure

db.sqlite3 # SQLite Database manage.py # Django management script static/ # Static files (CSS, JS, Images) bootstrap/ # Bootstrap framework files css/ # Custom stylesheets js/ # JavaScript files images/ # Image assets tasks/ # Main task management app migrations/ # Database migrations models.py # Task models views.py # Task views (handling requests) forms.py # Task forms urls.py # Task app URL routes templates/ # HTML templates for the task app tests.py # Unit tests for the task app todo_project/ # Main project folder settings.py # Project settings urls.py # Main URL routing wsgi.py # WSGI config for production asgi.py # ASGI config for async support

bash
Copy code

## Setup

### 1. Clone the repository:
`git clone <repository-url>
cd todo_project`
### 2. Create and activate a virtual environment:
`python -m venv venv`
`source venv/bin/activate ` # On Windows use 'venv\Scripts\activate' 
### 3. Install dependencies:
`pip install -r requirements.txt`
### 4. Apply database migrations:
`python manage.py migrate`
### 5. Run the development server:
`python manage.py runserver`
### 6. Access the application:
Open your browser and go to `http://127.0.0.1:8000/.`

## Features
### Task Management: 
Add, edit, and delete tasks.
### Task Prioritization: 
Set priorities for tasks.
### Due Dates: 
Assign due dates to tasks.
### Authentication: 
User authentication for personalized task management.

## Project Details
### Settings
The project settings are located in todo_project/settings.py. Key configurations include:

### Database: 
SQLite is used by default for simplicity.
### Static Files: 
Configured to serve static files from the static directory.
### Templates: 
The application renders HTML from the templates directory.
## URL Configuration
The URL patterns are defined in todo_project/urls.py and tasks/urls.py. Key routes include:

### Admin interface: 
/admin/
### Task management: 
/ (Home page)
### Authentication:
/accounts/
## Applications
The primary application is tasks, which handles the core functionality of the Todo app:

### Models: 
Defined in tasks/models.py, it represents tasks in the database.
### Views: 
Defined in tasks/views.py, responsible for rendering and processing task-related pages.
### Forms: 
Defined in tasks/forms.py to create and update tasks.
### Templates: 
Located in tasks/templates/, the HTML files for task-related pages.
## Static Files
The static/ directory includes:

### Bootstrap:
Located in static/bootstrap/, used for styling.
### CSS: 
Custom stylesheets in static/css/.
### JavaScript: 
Scripts in static/js/.
### Images: 
Image assets in static/images/.
## Templates
HTML templates are in the templates/ directory. The base layout is in base_generic.html, and there are authentication templates in templates/registration/.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
