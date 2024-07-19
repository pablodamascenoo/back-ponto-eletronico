from fastapi import FastAPI, HTTPException
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# Define o pino GPIO onde o sensor PIR está conectado
pir_sensor_pin = 37

Configuração inicial do GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor_pin, GPIO.IN)

app = FastAPI()

@app.get("/read_data")
async def readTag():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        return {"id": id, "text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error reading data")
    finally:
        GPIO.cleanup()

@app.post("/write_data")
async def writeTag(data: str):
    reader = SimpleMFRC522()
    try:
        reader.write(data)
        return {"message": "Data written successfully"};
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error writing data")
    finally:
        GPIO.cleanup()

@app.get("/")
async def root():
    return {"message": "Hello World"}