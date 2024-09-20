const sidenav = document.getElementById('sidenav-open')
const closenav = document.getElementById('sidenav-close')
const opennav = document.getElementById('sidenav-button')

const barometric_pressure = document.getElementById('barometric_pressure')
const control_module_voltage = document.getElementById('control_module_voltage')
const coolant_temperature = document.getElementById('coolant_temperature')
const distance_traveled_w_mil = document.getElementById('distance_traveled_w_mil')
const elm_version = document.getElementById('elm_version')
const engine_load = document.getElementById('engine_load')
const engine_rpm = document.getElementById('engine_rpm')
const engine_runtime = document.getElementById('engine_runtime')
const fuel_type = document.getElementById('fuel_type')
const intake_pressure = document.getElementById('intake_pressure')
const intake_temperature = document.getElementById('intake_temperature')
const throttle_position = document.getElementById('throttle_position')
const vehicle_speed = document.getElementById('vehicle_speed')
const maf = document.getElementById('maf')

/**
  * set focus to our open/close buttons after animation
  */
  
opennav.addEventListener('click', e => {
    sidenav.classList.add('sidenav__open')
    closenav.focus()
})

// sidenav.addEventListener('transitionend', e => closenav.focus())

closenav.addEventListener('click', e => sidenav.classList.remove('sidenav__open'))

/**
  * close our menu when esc is pressed. this is optional but good for accesibility.
  */
sidenav.addEventListener('keyup', e => {
  if (e.code === 'Escape')
      sidenav.classList.remove('sidenav__open')
})

const getData = () => {
    fetch(`${window.location.origin}/api`)
        .then(response => response.ok ? Promise.resolve(response): Promise.reject(response))
        .then(response => response.json())
        .then(response => {
            // clean the list.
            barometric_pressure.textContent = response.barometric_pressure
            control_module_voltage.textContent = response.control_module_voltage
            coolant_temperature.textContent = response.coolant_temperature
            distance_traveled_w_mil.textContent = response.distance_traveled_w_mil
            elm_version.textContent = response.elm_version
            engine_load.textContent = response.engine_load
            engine_rpm.textContent = response.engine_rpm
            engine_runtime.textContent = response.engine_runtime
            fuel_type.textContent = response.fuel_type
            intake_pressure.textContent = response.intake_pressure
            intake_temperature.textContent = response.intake_temperature
            throttle_position.textContent = response.throttle_position
            vehicle_speed.textContent = response.vehicle_speed
            maf.textContent = response.maf
            

        })
        .catch();
}

document.getElementById('btn').addEventListener('click', getData)

window.addEventListener('load', getData)
