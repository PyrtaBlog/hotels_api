from fastapi import APIRouter, HTTPException, Response, status

from app.users import auth
from app.users.schemas import SUsersAuth
from app.users.dao import UsersDao

router = APIRouter(
    prefix='/auth',
    tags=['Регистрация и Аутентификация'],
)

@router.post('/register')
async def register(user_data: SUsersAuth):
    exiting_user = await UsersDao.find_one_or_none(email=user_data.email)
    if exiting_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    hash_password = auth.get_hashed_password(user_data.password)
    await UsersDao.add(email=user_data.email, hashed_password=hash_password)
    
@router.post('/login')
async def login(res: Response, user_data: SUsersAuth):
    user = await UsersDao.find_one_or_none(email=user_data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователь не найден')
    password = auth.verify_hash_password(user.hashed_password, user_data.password)
    if not password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Неверный пароль')
    token = auth.create_access_token({'sub': str(user.id)})
    res.set_cookie('token', token, httponly=True)
    return {'token': token}

@router.post('/logout')
def logout(res: Response):
    res.delete_cookie('token')
    return {'message': 'Вы успешно вышли из системы'}

