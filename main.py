from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ListProperty, StringProperty, OptionProperty
from kivy.graphics import Color, Ellipse, Line

import slider2
import ValveIndicator
import analogInputs


# The widget looks for the kv file of the same name, so if you call your app PlotterApp, make sure the kv file is named
# plotter
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

    def on_valve_open(self):
        if analogInputs.calculatedVar1 < 250:
            self._valve_open()
        else:
            self._valve_closed()

    def _valve_open(self):
        pass

    def _valve_close(self):
        pass


class MainView(Widget):
    scale = ListProperty([100, 100])

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.slider.bind(value1=self.on_slider_changed, value2=self.on_slider_changed)

    def on_slider_changed(self, obj, value):
        self.scale[0] = self.slider.value1
        self.scale[1] = self.slider.value2


class SliderApp(App):
    def build(self):
        self.view = MainView()
        return self.view


if __name__ == '__main__':
    SliderApp().run()
