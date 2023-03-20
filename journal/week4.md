# Week 4 — Postgres and RDS

## Required homework

I was able to create an RDS postgres instance, connect gitpod to RDS, create cognito trigger to insert user into db, create a lambda function and create new activities with insert commands. I runned into a few problems:
- For the lambda function I was getting an error executing the insert when I pass de *params (function takes at most 2 arguments (5 given) insert) so I've changed to cur.execute(sql,(user_display_name,user_email,user_handle,user_cognito_id))
- For creating new activities with a db insert, I was getting an error returning null uuid so I realized through logging that I had to change the user_handle in the app.py data_activities(): user_handle = 'erodrigues'


### RDS Postgres Instance
![rds-instance](https://user-images.githubusercontent.com/124768576/226403572-d6416538-2910-4adb-aeea-7aa5b56f4095.png)


### Congito trigger and Lambda function
![cognito-trigger](https://user-images.githubusercontent.com/124768576/226404436-c1212d8f-97f8-4390-8e5d-a6f61d3e6e5e.png)
![lambda](https://user-images.githubusercontent.com/124768576/226403843-ddfed942-93ad-4203-a83d-a5be41d8d103.png)


### New activities with a database insert
![cruddur-tweets](https://user-images.githubusercontent.com/124768576/226403979-9e5ce6f5-1967-41c8-9c3b-dca7d076da87.png)
