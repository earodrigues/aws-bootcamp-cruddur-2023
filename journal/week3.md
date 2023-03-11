# Week 3 — Decentralized Authentication

## Required Homework

### Cognito user pool

I was able to follow the instructions setting up the cognito user pool, solving problems with the follow up videos and implementing custom pages for authentication process.

![cognito](https://user-images.githubusercontent.com/124768576/224487281-7ab621c5-427d-45f2-bfae-a789c73cb5bc.png)
![cognito-user](https://user-images.githubusercontent.com/124768576/224487634-dda7f49b-43f2-4553-8ae2-c7bce726d355.png)

#### Cruddur app with UI improvements and user logged in
![cruddur-user](https://user-images.githubusercontent.com/124768576/224488162-a60c9a90-d7e9-4e35-955d-9c88699a0c9b.png)


## Homework Challenges

### Decouple JWT verification into a middleware
I've implemented the JWT verification in what I think is a middleware. I did it using the same library that we wrote in the bootcamp (cognito_jwt_token.py) and I managed to make it work. Idealy, we can put this together with the library outside our application.

[auth_middleware.py](https://github.com/earodrigues/aws-bootcamp-cruddur-2023/blob/main/backend-flask/middleware/auth_middleware.py)
