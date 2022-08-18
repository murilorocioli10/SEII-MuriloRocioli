from flask import Flask, render_template, Response, request # módulos necessários
#from serial import Serial
import serial # conectar com arduino
import time

serialcom = serial.Serial('/dev/ttyACM0') # porta do arduino
serialcom.timeout = 1

app = Flask(__name__)


def ledOn():
    serialcom.write(str('on').encode())
    
def ledOff():
	serialcom.write(str('off').encode())

def disconnect():
	serialcom.close()

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if 'on' in request.form.to_dict():
			ledOn()
		if 'off' in request.form.to_dict():
			ledOff()
		if 'dis' in request.form.to_dict():
			disconnect()

	return render_template('index.html') # página HTML

if __name__ == "__main__":
    app.run(debug=True)
