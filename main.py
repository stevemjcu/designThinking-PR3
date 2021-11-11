import time

try:
    import RPi.GPIO as GPIO
except:
    from GPIOEmulator.EmulatorGUI import GPIO

# TODO: Read from config.yaml
config = {
    'pins': {
        24: {
            'name': 'Bachman\'s Warbler',
            'file': 'data/1.wav'
        },
        26: {
            'name': 'Passenger Pigeon',
            'file': 'data/2.wav'
        }
    }
}

def main():
    '''
    Enter main loop
    '''
    pins = config['pins']

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in pins.keys():
        GPIO.setup(pin, GPIO.IN)

    while(True):
        for pin, info in pins.items():
            if (GPIO.input(pin)):
                print(info['name'])
                time.sleep(0.5)

if __name__ == "__main__":
    main()
