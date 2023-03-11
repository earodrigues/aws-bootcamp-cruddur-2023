from functools import wraps
from flask import request, abort
from flask import current_app
import os

from lib.cognito_jwt_token import CognitoJwtToken, extract_access_token, TokenVerifyError

cognito_jwt_token = CognitoJwtToken(
  user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"), 
  user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
  region=os.getenv("AWS_DEFAULT_REGION")
)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = extract_access_token(request.headers)
        if token is None or token == 'null':
            # return {
            #    "message": "Authentication Token is missing!",
            #    "data": None,
            #    "error": "Unauthorized"
            #}, 401
            # Return null for the current_user so the endpoint can return data when no token provided
            return f(None, *args, **kwargs)
        try:
            data=cognito_jwt_token.verify(token)
            current_user=data['username']
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
