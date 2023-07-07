# Quiz_App

The Quiz App is a RESTful API that allows users to create quizzes, add questions to quizzes, and participate in quizzes to get scores. The API provides various endpoints to perform these operations.

<br />Installation
<br />1. Clone the repository:

```bash
   git clone https://github.com/hacky-tosh/Quiz_App.git
```
2. Install the required dependencies:
<br />
    ```bash
    cd QuizApp
    pip install -r requirements.txt
   ```
<br />3. Apply the database migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate

<br />4. Run the development server:
```bash
   python manage.py runserver
```

<br />The application will be accessible at http://localhost:8000/.
<br />#The application can also be aacessible at http://167.71.220.189/ server

<br />##API Endpoints
<br />#Create a Quiz: Allows an admin user to create a quiz.

<br />Endpoint: /api/quizzes/
<br />Method: POST
<br />Headers: Authorization: Token <token>
<br />Request Body:
```bash
  {
          "title": "General Knowledge Quiz"
  }
```

<br />#Retrieve a Quiz: Retrieves details of a specific quiz.

<br />Endpoint: /api/quizzes/<quiz_id>/
<br />Method: GET
<br />Headers: Authorization: Token <token>
<br />Example Response:
```bash
         {
            "id": 1,
            "title": "General Knowledge Quiz",
            "creator": 1,
            "url": "http://localhost:8000/api/quizzes/1/"
        }
```
<br />#List Participants: Retrieves a list of participants for a specific quiz.

<br />Endpoint: /api/participants/
<br />Method: GET
<br />Headers: Authorization: Token <token>
<br />Example Response:
```bash
    [
    {
        "user": 1,
        "quiz": 1,
        "score": 85
    },
    {
        "user": 2,
        "quiz": 1,
        "score": 92
    }
    ] 
```

<br />#Create a Question: Allows an admin user to add a question to a quiz.

<br />Endpoint: /api/questions/
<br />Method: POST
<br />Headers: Authorization: Token <token>
<br />Request Body:
```bash
        {
            "quiz_id": 1,
            "text": "What is the capital of France?",
            "creator_id": 1
        }
 ```
<br />#Create Answers: Allows an admin user to add answers to a question.

<br />Endpoint: /api/answers/
<br />Method: POST
<br />Headers: Authorization: Token <token>
<br />Request Body:
```bash
        {
            "question_id": 1,
            "answers": [
                {
                    "text": "Paris",
                    "is_correct": true
                },
                {
                    "text": "London",
                    "is_correct": false
                },
                {
                    "text": "Berlin",
                    "is_correct": false
                }
            ]
        }
```

<br />#Attempt a Quiz: Allows a user to attempt a quiz and submit answers.

<br />Endpoint: /api/quizzes/<quiz_id>/attempt/
<br />Method: POST
<br />Headers: Authorization: Token <token>
<br />Request Body:
```bash
        {
            "user": 1,
            "answers": [
                {
                    "question": 1,
                    "selected_answer": 1
                },
                {
                    "question": 2,
                    "selected_answer": 3
                }
            ]
        }
```

<br />#Get Quiz Scores: Retrieves the scores of participants for a specific quiz.

<br />Endpoint: /api/quizzes/<quiz_id>/scores/
<br />Method: GET
<br />Headers: Authorization: Token <token>
<br />Example Response:
```bash
    [
        {
            "participant": 1,
            "user": 1,
            "score": 75
        },
        {
            "participant": 2,
            "user": 2,
            "score": 85
        }
    ]
```

<br />#Authentication Tokens
<br />Use the following authentication tokens to make requests as different users:

<br />User: admin

<br />Token: 4f2d27e2d24e8f713fbac4f55f83e09fd5a34e4b

<br />User: normal_user

<br />Token: df40a7a960d47f2ad4b10bf493c09f21b43d47e6

```bash
Please replace `<token>` with the actual token values for the respective users.
Let me know if you need any further assistance!
```


<br />#To generate tokens for additional users
```bash
python manage.py drf_create_token
```


