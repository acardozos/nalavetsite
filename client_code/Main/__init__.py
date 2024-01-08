from ._anvil_designer import MainTemplate
from anvil import *
from ..Home import Home

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # self.aviso_flow_panel.visible = False
    # self.aviso_spacer.visible = False
    # self.aviso_image.visible = False
    self.content_panel.add_component(Home(), full_width_row=True)
