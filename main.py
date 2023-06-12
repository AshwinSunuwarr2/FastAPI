from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from db import Base, SessionLocal, engine
from model import Users
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserSchema(BaseModel):
    f_name: str
    m_name: Optional[str] = None
    l_name: str
    user_label: str
    
    class Config:
        orm_mode = True


@app.get("/", response_model=List[UserSchema])
def get_images(db: Session = Depends(get_db)):
    return db.query(Users).all()


@app.post("/add-image", response_model=UserSchema)
def add_image(users: UserSchema, db: Session = Depends(get_db)):
    u = Users(f_name=users.f_name, m_name=users.m_name, l_name=users.l_name, user_label=users.user_label)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

@app.put("/update-image/{u_id}", response_model = UserSchema)
def update_image(u_id: int, user: UserSchema, db: Session = Depends(get_db)):
    try:
        i = db.query(Users).filter(Users.id == u_id).first()
        i.f_name = user.f_name
        i.m_name = user.m_name
        i.l_name = user.l_name
        i.user_label = user.user_label
        db.add(i)
        db.commit()
        return i
    except:
        raise HTTPException(status_code = 404, details = "Image ID not found.")
    
@app.delete("/delete-user/{u_id}", response_class = JSONResponse)
def delete_img(u_id: int, db: Session = Depends(get_db)):
    try:
        i = db.query(Users).filter(Users.id == u_id).first()
        db.delete(i)
        db.commit()
        return {f"Image of id {u_id} has been deleted.": True}
    except:
        raise HTTPException(status_code = 404, details = "ID not found.")
