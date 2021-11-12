import time
import yaml

class Instance(yaml.YAMLObject):
    yaml_tag: str = u'!Instance'
    name: str
    file: str
    pin: int

    def __init__(self, **entries) -> None:
        self.__dict__.update(entries)

class Config(yaml.YAMLObject):
    yaml_tag: str = u'!Config'
    emulate: bool
    instances: list[Instance]

    def __init__(self, **entries) -> None:
        self.__dict__.update(entries)

def play_track(file: str):
    print("Playing " + file)
    # TODO: implement!

def main() -> None:
    with open('config.yaml', 'r') as file:
        loader = yaml.Loader
        config: Config = yaml.load(file, loader)

    if(config.emulate):
        from GPIOEmulator.EmulatorGUI import GPIO
    else:
        import RPi.GPIO as GPIO  # requires RPi OS

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for instance in config.instances:
        GPIO.setup(instance.pin, GPIO.IN)

    while(True):
        for instance in config.instances:
            if (GPIO.input(instance.pin)):
                play_track(instance.file)
                time.sleep(0.1)

if __name__ == "__main__":
    main()
