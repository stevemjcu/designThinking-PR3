import adafruit_mpr121
import board
import busio
from config import config
import pygame
import time

def play_soundbite(path: str, channel: int, loops: int = 0):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(path), loops)

def stop_soundbite(channel: int):
    pygame.mixer.Channel(channel).stop()

def main():
    pygame.init()
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
    is_playing = {}
    for i in config.instances:
        is_playing[i.name] = False
    while(True):
        for i in config.instances:
            if (mpr121[i.input].value):
                if(not is_playing[i.name]):
                    print('Playing ' + i.name)
                    play_soundbite(i.file, i.output, -1)
                    is_playing[i.name] = True
                else:
                    print('Stopping ' + i.name)
                    stop_soundbite(i.output)
                    is_playing[i.name] = False
                time.sleep(0.25)

if __name__ == "__main__":
    main()