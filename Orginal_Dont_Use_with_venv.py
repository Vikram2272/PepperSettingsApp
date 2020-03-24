from flask import Flask, render_template
from naoqi import ALProxy
from naoqi import ALModule

app = Flask(__name__)

ip = "192.168.1.35"
port = 9559

############################## Class for Events ##########################

class ReactingToEventsModule(ALModule):
  def __init__(self):
    bat = ALProxy("ALBattery", ip, port)
    
    global memory
    memory = ALProxy("ALMemory", ip, port)
    memory.subscribeToEvent("BatteryPowerPluggedChanged", "ReactingToEventsModule", "isPower")

  def isPower(self):
    val = memory.getData("BatteryPowerPluggedChanged")
    return val

############################### FLASK APP ################################

@app.route("/")
def hello():
  return render_template("index.html",data=chargeLevel)

@app.route("/battery")
def battery():
  return render_template('battery.html',data=chargeLevel)

@app.route('/isCharge')
def isCharge():
    eve = ReactingToEventsModule()
    datas = eve.isPower()
    if datas == True:
      return "1"
    else:
      return "0"

@app.route('/chargeLevel')
def chargeLevel():
    bat = ALProxy("ALBattery", ip,port)
    data = bat.getBatteryCharge();
    return str(data)




if __name__ == '__main__':
  app.run(host="192.168.1.35")



