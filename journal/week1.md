# Week 1 — App Containerization

## Required Homework
I had two problems following the instructions about containerizing the application:
- one, not showing any information in ports tab, solved by closing workspace and opening it again
- two, frontend wasn't running with command docker compose up, solved by executing npm i before docker command

I was able to complete all the checklist and follow instructions about writing frontend and backend notifications feature without any problem

## Homework Challenges
### Run dockerfile CMD as an external script
I was able to run the dockerfile CMD as an external script but I had to change its permissions to make it executable

[Dockerfile](https://github.com/earodrigues/aws-bootcamp-cruddur-2023/blob/main/backend-flask/Dockerfile)

[External script](https://github.com/earodrigues/aws-bootcamp-cruddur-2023/blob/main/backend-flask/external-script.sh)

### Push and tag an image to DockerHub
I build a new image for the backend in my repo and I was able to push it and tag it

[My DockerHub repo](https://hub.docker.com/repository/docker/earodrigues/backend-flask/general)
![dockerhub](https://user-images.githubusercontent.com/124768576/220429338-1a5a9609-0572-47c0-b47f-515444587721.png)

### Install Docker on your local machine and get the same containers running outside of Gitpod / Codespaces
I have Windows so I've installed Docker Desktop and I managed to run the same containers! I've also changed my env vars:
- FRONTEND_URL: "http://localhost:3000"
- BACKEND_URL: "http://localhost:4567" 
![docker-desktop](https://user-images.githubusercontent.com/124768576/221120649-b7475e37-50eb-4565-a61f-01c0c94d7ee2.png)
