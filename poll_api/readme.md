# Django REST API for Polls

This is a Django REST API project that allows CRUD operations on the `Poll` model. The `Poll` model has fields such as age, height, sex, and favorite color.

## Getting Started

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.x
- Django
- Django REST framework

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/poll-api.git
   cd poll-api
   ```

2. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Running the Development Server
    ```bash
    python manage.py runserver
    ```

### Endpoints
- **GET**  /api/polls/: List all polls.
- **POST** /api/polls/: Create a new poll.
- **GET** /api/polls/{poll_id}/: Retrieve details of a specific poll.
- **PUT** /api/polls/{poll_id}/: Update all fields of a specific poll.
- **PATCH** /api/polls/{poll_id}/: Update specific fields of a specific poll.
- **DELETE** /api/polls/{poll_id}/: Delete a specific poll.


### Endpoints
- List all polls
     ```bash
       curl http://127.0.0.1:8000/api/polls/
- Create a new poll
     ```bash
      curl -X POST -H "Content-Type: application/json" -d '{"age": 25, "height": 175, "sex": "Male", "favorite_color": "Blue"}' http://127.0.0.1:8000/api/polls/
- Update a poll
-  ```bash 
    curl -X PUT -H "Content-Type: application/json" -d '{"age": 30}' http://127.0.0.1:8000/api/polls/1/
- Delete a poll
  ```bash
   curl -X DELETE http://127.0.0.1:8000/api/polls/1/

### License

Feel free to copy and use this template for your project's README.


