from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .clustering import predict, train

# Connecting to the database and create the tables if they do not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Coordinates(BaseModel):
    x: float
    y: float


@app.get("/")
async def root():
    # Test Function
    return {"message": "Hello World"}


@app.post("/post", status_code=status.HTTP_201_CREATED)
async def store_data(new_data: Coordinates, db: Session = Depends(get_db)):
    # Post data to be classified and stored in the database
    new_data = new_data.dict()
    clusterID = predict([new_data['x'],new_data['y']])
    new_entry = models.clicks(x=new_data['x'], y=new_data['y'], cluster_id=int(clusterID))
    db.add(new_entry)
    db.commit()
    train(db)
    return {"message": "successfully added"}



@app.post("/classify")
async def root(new_data: Coordinates):
    # Classify input data
    new_data = new_data.dict()
    buff_id = predict([new_data['x'], new_data['y']])
    return {"class": str(buff_id)}


@app.get("/all_data")
async def get_all_data(db: Session = Depends(get_db)):
    # Return all data
    allData = db.query(models.clicks).all()
    # print(allData)
    return allData
    # return {"message": allData}