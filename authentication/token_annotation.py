from functools import wraps
from flask_restful import request, abort
import jwt
from constants import SECRET_KEY
import time
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        header = request.headers.get("Authorization")
        if header != None:
            token = header.split(" ")[1]
            try:
                encoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])         
            except:
                abort(401)
        else:
            abort(401)
        return f(*args, **kwargs)    
        
    return decorated_function