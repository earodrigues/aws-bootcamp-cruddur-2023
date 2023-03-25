# Week 5 — DynamoDB and Serverless Caching

## Required homework

I managed to get through the errors and implement all the access patterns.
I spent several hours in one specific error with boto3 client, it was keeping me saying "Unable to locate credentials" so I had to pass the security_access_key, secret_key and region in the params when instantiate the client.

### DynamoDB table with Stream on and Lambda trigger

![dynamoDB-table](https://user-images.githubusercontent.com/124768576/227722178-64ae6c9d-f18c-42c6-a4f3-1d13e2e57a50.png)

### Creating messages for existing groups and new group

![message_groups](https://user-images.githubusercontent.com/124768576/227724111-c8baa551-a95f-4c98-a2b2-98aaf350b3ef.png)
