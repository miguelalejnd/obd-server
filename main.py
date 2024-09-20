from flask import Flask, render_template, url_for
from elm import Elm
import obd
import threading

app = Flask(__name__)

# Ejecutar el emulador ELM327-emulator en modo demonio
emulator = Elm(batch_mode=True)

# Obtener el puerto en que se ejecuta
pty = emulator.get_pty()

def run_emulator():
    """
        Start the ELM327-emulator
        
        This function must be executed in a different
        thread so that it does not obstruct the execution flow
    """
    emulator.run()

# Instanciar un hilo para ejecutar el emulador en él
thread = threading.Thread(target=run_emulator)

# Iniciar la ejecución del hilo
thread.start()

# Establcer la concexión de la biblioteca OBD-Python con el emulador ELM327-emulator
connection = obd.OBD(pty)



@app.route('/')
def index():
    """
        Serves the index file of the website.
    """
    return render_template('index.html')



@app.route("/api")
def get_data():
    """
        Endpoint

        Processes the data obtained from the vehicle and 
        responds with a JSON object that contains it.
    """

    elm_version = connection.query(obd.commands.ELM_VERSION)

    coolant_temp = connection.query(obd.commands.COOLANT_TEMP)
    barometric_pressure = connection.query(obd.commands.BAROMETRIC_PRESSURE)
    throttle_position = connection.query(obd.commands.THROTTLE_POS)
    speed = connection.query(obd.commands.SPEED)
    engine_rpm = connection.query(obd.commands.RPM)
    engine_load = connection.query(obd.commands.ENGINE_LOAD)
    engine_runtime = connection.query(obd.commands.RUN_TIME)
    control_module_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
    
    maf = connection.query(obd.commands.MAF)
    intake_temp = connection.query(obd.commands.INTAKE_TEMP)
    distance_traveled_w_mil = connection.query(obd.commands.DISTANCE_W_MIL)
    fuel_type = connection.query(obd.commands.FUEL_TYPE)
    intake_pressure = connection.query(obd.commands.INTAKE_PRESSURE)
    
    
    information = {
        'elm_version': str(elm_version.value),
		'coolant_temperature': str(coolant_temp.value),
		'barometric_pressure': str(barometric_pressure.value),
		'throttle_position': str(throttle_position.value),
		'vehicle_speed': str(speed.value),
		'engine_rpm': str(engine_rpm.value),
		'engine_load': str(engine_load.value),
		'engine_runtime': str(engine_runtime.value),
		'control_module_voltage': str(control_module_voltage.value),
		'maf': str(maf.value),
		'intake_temperature': str(intake_temp.value),
		'distance_traveled_w_mil': str(distance_traveled_w_mil.value),
		'fuel_type': str(fuel_type.value),
		'intake_pressure': str(intake_pressure.value)
    }
    
    return information



@app.route('/api/dtc')
def dtc():
    """
        Endpoint 

        Responds with a JSON object containing all
        diagnostic trouble codes from the vehicle (DTC).
    """
    DTC = connection.query(obd.commands.GET_DTC)

    return DTC.value

if __name__ == "__main__":
    app.run(host='0.0.0.0')
