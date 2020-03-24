from flask import Flask, render_template, jsonify
#from naoqi import ALProxy
#from naoqi import ALModule

app = Flask(__name__)

ip = "192.168.1.35"
port = 9559

############################## Class for Events ##########################

class ReactingToEventsModule():
  def __init__(self):
    #bat = ALProxy("ALBattery", ip, port)
    
    global memory
   # memory = ALProxy("ALMemory", ip, port)
    #memory.subscribeToEvent("BatteryPowerPluggedChanged", "ReactingToEventsModule", "isPower")

  def isPower(self):
    #val = memory.getData("BatteryPowerPluggedChanged")
    return ""

############################### FLASK APP ################################

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/network")
def network():
  return render_template('network.html')

@app.route("/audio")
def audio():
  return render_template('audio.html')

@app.route("/display")
def display():
  return render_template('display.html')

@app.route("/asr")
def asr():
  return render_template('asr.html')

@app.route("/reset")
def reset():
  return render_template('reset.html')

####################################  Battery Functions  ###################################
@app.route("/battery")
def battery():
  return render_template('battery.html', data=chargeLevel)

@app.route('/isCharge')
def isCharge():
    eve = ""#ReactingToEventsModule()
    #datas = eve.isPower()
    datas = {
          "isCharge": "True"
        }
    return jsonify(datas)

@app.route('/chargeLevel')
def chargeLevel():
    #bat = ALProxy("ALBattery", ip,port)
    #data = bat.getBatteryCharge();
    data = 78
    return str(data)

@app.route('/batterysaver')
def batterysaver():
  return str(22)

if __name__ == '__main__':
  app.run(debug=True)



