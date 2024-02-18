# Simple Note-Taking Application API

This is a simple Django application that provides a RESTful API for a note-taking application. Users can register, login, create, read, update, and share notes.

## Requirements

- Python (3.6+)
- Django
- Django REST Framework
- Postman (optional, for testing API endpoints)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/note-taking-app.git
    cd note-taking-app
    ```

2. Install the Python dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

By default, the application uses SQLite as the database backend. You can change the database settings in `settings.py` if needed.

Run the database migrations to create the necessary tables:

```bash
python manage.py migrate
```

 # Running the Server

To start the Django development server, run the following command in your terminal:

```bash
python manage.py runserver
```

The API will be accessible at http://localhost:8000/.

## API Endpoints

- User Registration: `POST /signup`
- User Login: `POST /login`
- Create New Note: `POST /note/create`
- Get a Note: `GET /note/{id}`
- Update a Note: `PUT /note/{id}`

To interact with the API endpoints in this project using Postman, you'll need to send various HTTP request methods. Here are the methods you can use:

- **User Registration:**
  - Method: POST
  - Endpoint: /signup

- **User Login:**
  - Method: POST
  - Endpoint: /login

- **Create New Note:**
  - Method: POST
  - Endpoint: /note/create

- **Get a Note:**
  - Method: GET
  - Endpoint: /note/{id}

- **Update a Note:**
  - Method: PUT
  - Endpoint: /notes/{id}

These methods correspond to the actions you can perform with the API endpoints using Postman. Make sure to set the appropriate request method and endpoint URL in Postman when testing each functionality.
