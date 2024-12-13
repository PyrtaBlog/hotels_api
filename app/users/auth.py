import datetime
import bcrypt
import jwt


from app.config import settings


def get_hashed_password(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

def verify_hash_password(hashed_password, provided_password):
    hashed_password_bytes = hashed_password
    provided_password_bytes = provided_password.encode('utf-8')
    return bcrypt.checkpw(provided_password_bytes, hashed_password_bytes)
    
def create_access_token (data: dict) -> str:
    encode_data = data.copy()
    print(type(encode_data))
    # Добавляем время в секундах
    expire = datetime.datetime.now() + datetime.timedelta(minutes=30)
    encode_data.update({'expire': expire.isoformat()})
    encode_jwt = jwt.encode(
        encode_data,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encode_jwt

