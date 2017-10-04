# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program calculates the height of an object dropped from 100 m above the ground after the number of 
# seconds the user inputs

import ui

def calculate_button_touch_up_inside(sender):
    # This calculates the height of an object in meters after being dropped n seconds from 100 m
    
    # constants
    GRAVITY = 9.81
    
    # input
    seconds = float(view['input_seconds_textbox'].text)
    
    # process
    height = 100 - 0.5 * GRAVITY * (seconds ** 2)
    
    # output
    view['height_answer_label'].text = "The height of the object above ground is: " + str(height) + " m"

view = ui.load_view()
view.present('full_screen')
