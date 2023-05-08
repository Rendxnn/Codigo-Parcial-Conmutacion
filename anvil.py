from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import time

class Form1(Form1Template):
  def _init_(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    while True:
      if anvil.server.call('leer_boton') == 1:
          anvil.server.call('led')
          while True:
              if anvil.server.call('leer_boton') == 1:
                  anvil.server.call('apagar_motor')
                  anvil.server.call('led')
                  break
              anvil.server.call('activar_motor')
              temp = anvil.server.call('leer_potenciometro') / 2000
              self.label_1.text = f'La temperatura actual es: {temp}'
