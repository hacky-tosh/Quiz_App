# Quiz_App

The Quiz App is a RESTful API that allows users to create quizzes, add questions to quizzes, and participate in quizzes to get scores. The API provides various endpoints to perform these operations.

Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/hacky-tosh/Quiz_App.git

2. Install the required dependencies:

    ```bash
    cd QuizApp
    pip install -r requirements.txt

3. Apply the database migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate

4. Run the development server:
   ```bash
   python manage.py runserver

The application will be accessible at http://localhost:8000/.
#The application can also be aacessible at http://167.71.220.189/ server

##API Endpoints
#Create a Quiz: Allows an admin user to create a quiz.

Endpoint: /api/quizzes/
Method: POST
Headers: Authorization: Token <token>
Request Body:
  ```bash
  {
          "title": "General Knowledge Quiz"
  }
```

#Retrieve a Quiz: Retrieves details of a specific quiz.

Endpoint: /api/quizzes/<quiz_id>/
Method: GET
Headers: Authorization: Token <token>
Example Response:
  ```bash
         {
            "id": 1,
            "title": "General Knowledge Quiz",
            "creator": 1,
            "url": "http://localhost:8000/api/quizzes/1/"
        }
```
#List Participants: Retrieves a list of participants for a specific quiz.

Endpoint: /api/participants/
Method: GET
Headers: Authorization: Token <token>
Example Response:
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

#Create a Question: Allows an admin user to add a question to a quiz.

Endpoint: /api/questions/
Method: POST
Headers: Authorization: Token <token>
Request Body:
    ```bash
        {
            "quiz_id": 1,
            "text": "What is the capital of France?",
            "creator_id": 1
        }
        ```
#Create Answers: Allows an admin user to add answers to a question.

Endpoint: /api/answers/
Method: POST
Headers: Authorization: Token <token>
Request Body:
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

#Attempt a Quiz: Allows a user to attempt a quiz and submit answers.

Endpoint: /api/quizzes/<quiz_id>/attempt/
Method: POST
Headers: Authorization: Token <token>
Request Body:
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

#Get Quiz Scores: Retrieves the scores of participants for a specific quiz.

Endpoint: /api/quizzes/<quiz_id>/scores/
Method: GET
Headers: Authorization: Token <token>
Example Response:
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

#Authentication Tokens
Use the following authentication tokens to make requests as different users:

User: admin

Token: 4f2d27e2d24e8f713fbac4f55f83e09fd5a34e4b

User: normal_user

Token: df40a7a960d47f2ad4b10bf493c09f21b43d47e6

```bash
Please replace `<token>` with the actual token values for the respective users.
Let me know if you need any further assistance!
```


#To generate tokens for additional users
```bash
python manage.py drf_create_token
```


