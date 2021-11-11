import time
import yaml

try:
    import RPi.GPIO as GPIO
except:
    from GPIOEmulator.EmulatorGUI import GPIO

def load_config():
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as err:
        print(err)

def play_track(file):
    print("Playing " + file)
    # TODO

def main():
    config = load_config()
    instances = config['instances']

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for instance in instances:
        GPIO.setup(instance['pin'], GPIO.IN)

    while(True):
        for instance in instances:
            if (GPIO.input(instance['pin'])):
                play_track(instance['file'])
                time.sleep(0.1)

if __name__ == "__main__":
    main()
