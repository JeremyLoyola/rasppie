import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
led_pins = {'led-1': 3, 'led-2': 5, 'led-3': 7}  # Replace pin numbers with your GPIO pin numbers
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)

print('''
Using the robot.txt file:
#1 - Create a program, where you ask the
     user for a variable user_robot_name
#2 - Check to see if the name is in the file
#3 - If it's found, print the line, if not
     print "Robot Not Found"
#4 - split out all the parts of the line.
HINT: See that the line can be split into a list by commas ','

i.e: 'robot3,rgb-led,green,2022-05-03,08:08:52pm'

#5 - Using the list you created from step #4,
     create 5 variables and pull their values by
     indexing the list
    - robot_name
    - robot_feature
    - robot_action
    - robot_date
    - robot_time
#6 - Print the 5 variables
#7 - Print a formatted line that looks like:

The User requested to have <robot_name> turn on
the <robot_feature> and have it be <robot_action>

# Put your code here:
------------------------------------------
''')

# Function to control LEDs
def robotLED(device, action):
    print('LED on/off Function')
    print('The robot device is', device, 'the robot action is', action)

    # GPIO control code to turn on/off the LEDs
    pin = led_pins.get(device)
    if pin is not None:
        if action == 'on':
            print('Turning on', device)
            GPIO.output(pin, GPIO.HIGH)  # Turn on LED
        elif action == 'off':
            print('Turning off', device)
            GPIO.output(pin, GPIO.LOW)  # Turn off LED
        else:
            print('Warning: Invalid action - should not see this message')
    else:
        print('Warning: Invalid device - should not see this message')
        
# Function to control LEDs


# Put your code here:
user_robot_name = input("Please enter the robot name: ")

# Open the file and check if the robot name is present
with open("robot.txt", "r") as file:
    for line in file:
        if user_robot_name in line:
            parts = line.strip().split(',')
            robot_name = parts[0]
            robot_feature = parts[4]
            robot_action = parts[5]
            robot_date = parts[1]
            robot_time = parts[2]
            robot_API = parts[3]
            print("robot_name:", robot_name)
            print("robot_API:" , robot_API)
            print("robot_feature:", robot_feature)
            print("robot_action:", robot_action)
            print("robot_date:", robot_date)
            print("robot_time:", robot_time)
            print("\nThe User requested to have {} turn on the {} and have it be {}.".format(robot_name, robot_feature, robot_action))
            #break
            if(robot_feature == "led-1"):
               #after you figure pout if its led-1
                robotLED(robot_feature, robot_action)
                sleep(1)
    else:
        print("Robot Not Found")
    


# Call the LED control function
#robotLED(robot_feature, robot_action)

# Clean up GPIO
#GPIO.cleanup()
