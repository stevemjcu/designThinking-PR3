import time
import yaml

class Instance():
    name: str
    file: str
    pin: int

    def __init__(self, **entries):
        self.__dict__.update(entries)

def play_track(file):
    print("Playing " + file)
    # TODO: implement!

def main():
    with open('config.yaml', 'r') as file:
        data_map = yaml.safe_load(file)
        use_emulator = bool(data_map['use_emulator'])
        instances = [Instance(**i) for i in data_map['instances']]

    if(use_emulator):
        from GPIOEmulator.EmulatorGUI import GPIO
    else:
        import RPi.GPIO as GPIO  # requires RPi OS

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for instance in instances:
        GPIO.setup(instance.pin, GPIO.IN)

    while(True):
        for instance in instances:
            if (GPIO.input(instance.pin)):
                play_track(instance.file)
                time.sleep(0.1)

if __name__ == "__main__":
    main()
