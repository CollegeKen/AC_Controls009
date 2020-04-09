# AC_Controls009
9th Version of AC Controls
This batch of files is used to controls outputs based on the analog inputs from an Arduino. A RPi4 and Arduino Mega were used,
but the code should be good for RPi3 and Arduino Uno.

The main.py file is used to create the screen, and the ValveIndicator and slider files are used for widgets. The analog input 
file is taking the inputs from the Arduino for reading, and the kv file is used to order the widget on the screen. Discrete 
outputs to the Arduino still need to be implemented. Potential problems are with the sliders and the Waveshare touchscreen that 
is being used. 
