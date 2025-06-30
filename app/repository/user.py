from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.models import User
from app.schemas import UserCreate

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def create_user(user: UserCreate, db: Session):
    db_user = User(**user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Ya existe un usuario con ese correo electrónico."
        )
def update_user(user: User, data: UserCreate, db: Session):
    for key, value in data.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user: User, db: Session):
    db.delete(user)
    db.commit()
