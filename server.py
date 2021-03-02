from flask_cors import CORS
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

pygame.mixer.pre_init(4400, -16, 1, 512)
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Stars.wav")

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
cors = CORS(app)

ip_address = "10.0.1.11"

@app.route("/")
def hello():
    return render_template("index.html", ip=ip_address)
    
@app.route("/on")
def on():
    GPIO.output(7, True)
    return "The light is on"

@app.route("/off")
def off():
    GPIO.output(7, False)
    return "The light is off"

@app.route("/blink")
def blink():
    for i in range(10):
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        time.sleep(1)
    return "The light is blinking"

@app.route("/BlinkRapidly")
def BlinkRapidly():
    for i in range(100):
        GPIO.output(7, True)
        time.sleep(.1)
        GPIO.output(7, False)
        time.sleep(.1)
    return "The light is rapdily blinking"

@app.route("/Alarm")
def Alarm():
    pygame.mixer.music.play()
    for i in range(63):
        GPIO.output(7, True)
        time.sleep(.1)
        GPIO.output(7, False)
        time.sleep(.1)
    while pygame.mixer.music.get_busy():
            continue
        
    return "Alarm is done"
        
@app.route("/timer", methods=['POST'])
def timer():
    delay = request.form["delay"]
    delay = int(delay)
    
    time.sleep(delay)
    pygame.mixer.music.play()
    for i in range(63):
        GPIO.output(7, True)
        time.sleep(.1)
        GPIO.output(7, False)
        time.sleep(.1)
    #.... do whatever you  need to do here
    
    return "Timer done."
 
if __name__ == "__main__":
    app.run(host=ip_address, port=80, debug=True)
