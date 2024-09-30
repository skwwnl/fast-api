from fastapi import APIRouter, HTTPException, status
from app.models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)
users = {}


@user_router.post("/signup")
async def sign_up_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists",
        )
    users[data.email] = data
    print(type(data))
    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully."}
