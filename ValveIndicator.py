from kivy.uix.widget import Widget
from kivy.properties import OptionProperty, BooleanProperty, StringProperty, ListProperty

import analogInputs
import slider2


class ValveIndicator(Widget):
    valve_closed = StringProperty('/home/ken/Pictures/Kivy_AC_Controls_Images/red_circle.png')
    valve_open = StringProperty('/home/ken/Pictures/Kivy_AC_Controls_Images/green_circle.png')
    border = ListProperty([16, 16, 16, 16])

    state = OptionProperty('open', options=('close', 'open'))

    def __init__(self, **kwargs):

        super(ValveIndicator, self).__init__(**kwargs)
        self.__state_event = None

    def _valve_open(self):
        self.state = 'open'

    def _valve_close(self, *args):
        self.state = 'close'


