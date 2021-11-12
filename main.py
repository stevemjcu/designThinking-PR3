import pygame
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
            self.channel: int
            self.__dict__.update(entries)

def play_soundbite(path: str, channel: int):
    sound = pygame.mixer.Sound(path)
    pygame.mixer.Channel(channel).play(sound)

def main():
    with open('config.yaml', 'r') as file:
        loader = yaml.Loader
        config: Config = yaml.load(file, loader)

    if(config.emulate):
        from GPIOEmulator.EmulatorGUI import GPIO
    else:
        import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for instance in config.instances:
        GPIO.setup(instance.pin, GPIO.IN)
    pygame.init()

    try:
        while(True):
            for instance in config.instances:
                if (GPIO.input(instance.pin)):
                    print("Playing " + instance.name + "...")
                    play_soundbite(instance.file, instance.channel)
                    time.sleep(0.1)
    finally:
        GPIO.cleanup()
        pygame.quit()

if __name__ == "__main__":
    main()
