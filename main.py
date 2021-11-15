from config import config
import pygame
import time

if(config.emulate):
    from GPIOEmulator.EmulatorGUI import GPIO
else:
    import RPi.GPIO as GPIO

def play_soundbite(path: str, channel: int, loops: int = 0):
    sound = pygame.mixer.Sound(path)
    pygame.mixer.Channel(channel).play(sound, loops)

def stop_soundbite(channel: int):
    pygame.mixer.Channel(channel).stop()

def main():
    pygame.init()
    playing = {}
    # load
    print("Loading...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in config.instances:
        GPIO.setup(i.pin, GPIO.IN)
        playing[i.name] = False
    print("...Done!")
    # run
    try:
        while(True):
            for i in config.instances:
                if (GPIO.input(i.pin)):
                    if(not playing[i.name]):
                        print(i.name)
                        play_soundbite(i.file, i.channel, -1)
                        playing[i.name] = True
                    else:
                        stop_soundbite(i.channel)
                        playing[i.name] = False
                    time.sleep(0.25)
    finally:
        GPIO.cleanup()
        pygame.quit()

if __name__ == "__main__":
    main()
