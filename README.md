# :computer: Serverless REST API :computer:

![](https://socialify.git.ci/palrohitg/icompass-python-task/image?forks=1&language=1&owner=1&pulls=1&stargazers=1&theme=Dark)
Its a **REST API (Serverless) with AWS Services** which allow you to perform  **CRUD** operations.
## :rotating_light: Pre-requisites 


[![node-current](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]() [![GitHub top language](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)]()[![GitHub top language](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]()[![GitHub top language](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()



## :dart: Tech stack : 
* AWS Services
* Python 
* Flask 
* Linux  
* DynamoDB
   

 
## :pencil2: REST API: 

The REST API for User. 

### Get list of users

#### Request 
  `GET /users`

    curl -X GET "https://cv8o6nhjxe.execute-api.us-west-2.amazonaws.com/Prod/users"

#### Reponse

    [
      {
        "password": "user2pass",
        "last_name": "user2lastname",
        "id": "2",
        "email": "user2@gmail.com",
        "first_name": "user2firstname"
      }, 
      {
        "password": "password",
        "last_name": "pal",
        "id": "1",
        "email": "user1@gmail.com",
        "first_name": "vikas"
      }, 
      {
      "password": "testuser1pass",
      "last_name": "testuserlastname",
      "id": "3",
      "email": "testuser@gmail.com",
      "first_name": "testuserupdateduserfirstname"
      }
    ]

### Creat a User

#### Request 
  `POST /users`

    curl -d "id=10&email=user9@gmail.com&first_name=user9firstname&last_name=user9lastname&password=userpass9" -H "Content-Type: application/x-www-form-urlencoded" -X POST "https://cv8o6nhjxe.execute-api.us-west-2.amazonaws.com/Prod/users"

#### Reponse

    {
     "message": "users entry created"
    }

### Get Users by Id

#### Request 
  `GET /users/1`

    curl -X GET "https://cv8o6nhjxe.execute-api.us-west-2.amazonaws.com/Prod/users/9"

#### Reponse

    {
      "password": "password",
      "last_name": "pal",
      "id": "1",
      "email": "user1@gmail.com",
      "first_name": "vikas"
    }

### Update a User by Id

#### Request 
  `PATCH /users/10`

     curl -d "first_name=user9updatefirstname" -H "Content-Type: application/x-www-form-urlencoded" -X PATCH "https://cv8o6nhjxe.execute-api.us-west-2.amazonaws.com/Prod/users/10"

#### Reponse

    {
      "message": "users entry updated"
    }

### Delete a User By Id 

#### Request 
  `DELETE /users/10`

    curl -X DELETE "https://cv8o6nhjxe.execute-api.us-west-2.amazonaws.com/Prod/users/10"


## 📜 Thank You
