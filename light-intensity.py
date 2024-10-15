import tkinter as tk
from gpiozero import PWMLED

# Define LEDs connected to GPIO pins with PWM control for brightness
led1 = PWMLED(26)  # LED 1 on GPIO 26
led2 = PWMLED(3)   # LED 2 on GPIO 3
led3 = PWMLED(2)   # LED 3 on GPIO 2

# Function to turn off all the LEDs
def reset_led():
    led1.value = 0
    led2.value = 0
    led3.value = 0

# Initialize LEDs
reset_led()

# Function to adjust the brightness of the selected LED based on slider value
def adjust_brightness(value):
    selected_led = led_var.get()
    brightness = float(value) / 100  # Convert slider value to 0-1 for PWM
    if selected_led == 1:
        led1.value = brightness
    elif selected_led == 2:
        led2.value = brightness
    elif selected_led == 3:
        led3.value = brightness

# Function to turn on the selected LED and turn off the others
def turn_on_led(led):
    reset_led()
    brightness = brightness_slider.get() / 100  # Set initial brightness based on slider
    if led == 1:
        led1.value = brightness
    elif led == 2:
        led2.value = brightness
    elif led == 3:
        led3.value = brightness

# Function to handle radio button selection
def led_select():
    selected_led = led_var.get()
    turn_on_led(selected_led)

# Function to quit the application
def quit_app():
    reset_led()
    root.quit()

# Create the GUI window
root = tk.Tk()
root.title("LED Control")

# Variable to store the radio button selection
led_var = tk.IntVar()

# Create a heading
heading = tk.Label(root, text="Toggle lights and adjust brightness", font=("Helvetica", 24))
heading.pack()

# Create radio buttons to select the LED
radio1 = tk.Radiobutton(root, text="LED 1", variable=led_var, value=1, command=led_select)
radio2 = tk.Radiobutton(root, text="LED 2", variable=led_var, value=2, command=led_select)
radio3 = tk.Radiobutton(root, text="LED 3", variable=led_var, value=3, command=led_select)

# Pack the radio buttons
radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
radio3.pack(anchor=tk.W)

# Create a slider to adjust brightness (0-100)
brightness_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Brightness", command=adjust_brightness)
brightness_slider.set(50)  # Set initial brightness to 50%
brightness_slider.pack()

# Reset button to turn off all LEDs
reset_button = tk.Button(root, text="Reset", command=reset_led)
reset_button.pack()

# Exit button to quit the program
exit_button = tk.Button(root, text="Exit", command=quit_app)
exit_button.pack()

# Run the GUI event loop
root.mainloop()
