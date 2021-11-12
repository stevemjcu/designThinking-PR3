import time
import yaml

class Config(yaml.YAMLObject):
    yaml_tag = u'!Config'

    def __init__(self, **entries):
        self.emulate: bool
        self.instances: list[self.Instance]
        self.__dict__.update(entries)

    class Instance(yaml.YAMLObject):
        yaml_tag = u'!Instance'
        
        def __init__(self, **entries):
            self.name: str
            self.file: str
            self.pin: int
            self.__dict__.update(entries)

def play_soundbite(file: str):
    print("Playing " + file)
    # TODO: implement!

def main():
    with open('config.yaml', 'r') as file:
        config: Config = yaml.load(file, yaml.Loader)

    if(config.emulate):
        from GPIOEmulator.EmulatorGUI import GPIO
    else:
        import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for instance in config.instances:
        GPIO.setup(instance.pin, GPIO.IN)

    while(True):
        for instance in config.instances:
            if (GPIO.input(instance.pin)):
                play_soundbite(instance.file)
                time.sleep(0.1)

if __name__ == "__main__":
    main()
