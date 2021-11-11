import time
import yaml

try:
    import RPi.GPIO as GPIO
except:
    from GPIOEmulator.EmulatorGUI import GPIO

def load_config():
    '''
    Load config from YAML
    '''
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as err:
        print(err)

def play_soundbite(file):
    '''
    Play .wav file (TODO)
    '''
    print("Playing " + file + "...")

def main():
    '''
    Enter main loop
    '''
    config = load_config()
    pins = config['pins']

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in pins.keys():
        GPIO.setup(pin, GPIO.IN)

    while(True):
        for pin, info in pins.items():
            if (GPIO.input(pin)):
                play_soundbite(info['file'])
                time.sleep(0.1)

if __name__ == "__main__":
    main()
