import anvil.pico
import uasyncio as a
from machine import Pin, ADC, PWM
import time


UPLINK_KEY = "server_UTNEKVEQD253TFF3B7ODWCNZ-2UHY4HPVWF6UUX2R"


led = Pin("LED", Pin.OUT, value=1)
pot = ADC(Pin(28))
motor = PWM(Pin(27))
boton = Pin(16, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(17, Pin.OUT, value=1)
pito1 = Pin(19, Pin.OUT, value=0)
motor.freq(1000)


@anvil.pico.callable_async
async def leer_potenciometro():
    return int(pot.read_u16())


@anvil.pico.callable_async
async def activar_motor():
    duty = int(pot.read_u16())
    motor.duty_u16(duty)
    

@anvil.pico.callable_async
async def apagar_motor():
    motor.duty_u16(0)
    

@anvil.pico.callable_async
async def leer_boton():
    return boton.value()


@anvil.pico.callable_async
async def led():
    led1.toggle()
    
    
@anvil.pico.callable_async
async def pito():
    pito1.on()
    time.sleep(1000)
    pito1.off()


anvil.pico.connect(UPLINK_KEY)

  