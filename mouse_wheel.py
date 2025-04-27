###Mouse wheel replacer###
#Sends mouse wheel up and down inputs when pressing the chosen keys

##Imports
try:
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",datefmt="%H:%M:%S")
    import time
    import keyboard
    import mouse
except ModuleNotFoundError:
    logging.critical ("Module not found, please make sure all required modules are installed")
    print("Press enter to Quit")
    input("")
    exit()

##Code
logging.info("Simulating mouse wheel")

print("Choose mouse wheel up key:")
wheel_up = keyboard.read_key()
print(wheel_up)
time.sleep(0.5)

print("Choose mouse wheel down key:")
wheel_down = keyboard.read_key()
print(wheel_down)

logging.info("Close window when done")

while True:
    
    key = keyboard.read_key()
    if key == wheel_up:
        mouse.wheel(1)
    if key == wheel_down:
        mouse.wheel(-1)
    time.sleep(0.1)