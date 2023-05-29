from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.plot_1.data = [
      go.Scatter(
        x = [],
        y = [],
        marker = dict(
          color= 'rgb(16, 32, 77)'
        )
      ),
      go.Bar(
        x = [],
        y = [],
        name = 'Temperaturas registradas'
      )
    ]
    self.label_1.text = 'La temperatura actual es: '
    self.temperaturas = []
    self.numeros = []
    # Any code you write here will run before the form opens.

  def update_plot(self):
    self.plot_1.data = [
      go.Scatter(
        x = self.numeros,
        y = self.temperaturas,
        marker = dict(
          color= 'rgb(16, 32, 77)'
        )
      ),
      go.Bar(
        x = self.numeros,
        y = self.temperaturas,
        name = 'Temperaturas registradas'
      )
    ]
  
  def button_1_click(self, **event_args):
    contador = 1
    while True:
      if anvil.server.call('leer_boton') == 1:
          anvil.server.call('led')
          while True:
              if anvil.server.call('leer_boton') == 1:
                  anvil.server.call('apagar_motor')
                  anvil.server.call('led')
                  anvil.server.call('pito')
                  
                  break
              anvil.server.call('activar_motor')
              temp = anvil.server.call('leer_potenciometro') / 2000
              self.label_1.text = f'La temperatura actual es: {temp}'
              self.temperaturas.append(temp)
              self.numeros.append(contador)
              contador += 1
              self.update_plot()
            



