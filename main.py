import config
import pygame
import time

if(config.config.emulate):
    from GPIOEmulator.EmulatorGUI import GPIO
else:
    import RPi.GPIO as GPIO

def play_soundbite(path: str, channel: int):
    sound = pygame.mixer.Sound(path)
    pygame.mixer.Channel(channel).play(sound)

def main():
    # load
    print("Loading...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for instance in config.config.instances:
        GPIO.setup(instance.pin, GPIO.IN)
    pygame.init()
    print("...Done!")
    # run
    try:
        while(True):
            for i in config.config.instances:
                if (GPIO.input(i.pin)):
                    print("Playing: " + i.name)
                    play_soundbite(i.file, i.channel)
                    time.sleep(0.25)
    finally:
        GPIO.cleanup()
        pygame.quit()

if __name__ == "__main__":
    main()
