import config
import pygame
import time

if(config.config.emulate):
    from GPIOEmulator.EmulatorGUI import GPIO
else:
    import RPi.GPIO as GPIO

def play_soundbite(path: str, channel: int, loops: int = 0):
    sound = pygame.mixer.Sound(path)
    pygame.mixer.Channel(channel).play(sound, loops)

def stop_soundbite(channel: int):
    pygame.mixer.Channel(channel).stop()

def main():
    playing = {}
    # load
    print("Loading...")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for i in config.config.instances:
        playing[i.name] = False
        GPIO.setup(i.pin, GPIO.IN)
    pygame.init()
    print("...Done!")
    # run
    try:
        while(True):
            for i in config.config.instances:
                if (GPIO.input(i.pin)):
                    if(not playing[i.name]):
                        playing[i.name] = True
                        print("Playing: " + i.name)
                        play_soundbite(i.file, i.channel, -1)
                        time.sleep(0.25)
                    else:
                        playing[i.name] = False
                        print("Stopping: " + i.name)
                        stop_soundbite(i.channel)
                        time.sleep(0.25)
    finally:
        GPIO.cleanup()
        pygame.quit()

if __name__ == "__main__":
    main()
