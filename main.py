import anvil.pico
import uasyncio as a
from machine import Pin, ADC, PWM
import time


UPLINK_KEY = "<UPLINK_KEY>"


led = Pin("LED", Pin.OUT, value=1)
pot = ADC(Pin(28))
motor = PWM(Pin(27))
boton = Pin(16, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(17, Pin.OUT, value=1)
motor.freq(1000)


@anvil.pico.callable(is_async=True)
async def leer_potenciometro():
    return pot.read_u16()


@anvil.pico.callable(is_async=True)
async def activar_motor():
    duty = leer_potenciometro()
    motor.duty_u16(duty)
    

@anvil.pico.callable(is_async=True)
async def apagar_motor():
    motor.duty_u16(0)
    

@anvil.pico.callable(is_async=True)
async def leer_boton():
    return boton.value()


@anvil.pico.callable(is_async=True)
async def led():
    led1.toggle()


anvil.pico.connect(UPLINK_KEY)

  
