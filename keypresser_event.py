# -*- coding=utf-8 -*-
# Python2.7
# @Burak Büyükyüksel
# @Eren Durgunlu

'''
pip2 install python3-xlib
pip2 install pyautogui
sudo apt-get install -y scrot
sudo apt-get install -y python3-tk
sudo apt-get install -y python3-dev
'''

'''
___________________________
Directions
___________________________
    U   : Forward
    UL  : Forward & Left
    UR  : Forward & Right

    D   : Backward
    DL  : Backward & Left
    DR  : Backward & Right

'''

import pyautogui
import threading
import logging
from time import sleep

class KEYPRESS_EVENT:
    @classmethod
    def keys_help():
        print(pyautogui.KEYBOARD_KEYS)

    @classmethod
    def setQ(cls):
       pyautogui.press('q')

    @classmethod
    def forward(cls, event, logger):
        logger.info("Forward") 
        pyautogui.keyDown("up")
        event.wait()
        pyautogui.keyUp("up")

    @classmethod
    def LTF(cls, time, event, logger):
        logger.info("LTF")
        pyautogui.keyDown('left')
        sleep(time)
        cls.forward(event)
        pyautogui.keyUp('left')

    @classmethod
    def RTF(cls, time, event, logger):
        logger.info("RTF")
        pyautogui.keyDown('right')
        sleep(time)
        cls.forward(event)
        pyautogui.keyUp('right')


    @classmethod
    def backward(cls, event, logger):
        logger.info("Backward")
        cls.setQ() # Geri vitese al
        pyautogui.keyDown("up")
        event.wait()
        pyautogui.keyUp("up")
        cls.setQ() # Geri vitesten çek 
    
    @classmethod
    def forward_left(cls, event, logger):
        logger.info("Forward - Left")
        pyautogui.keyDown("up")
        pyautogui.keyDown("left")
        event.wait()
        pyautogui.keyUp("up")
        pyautogui.keyUp("left")
    
    @classmethod
    def forward_right(cls, event, logger):
        logger.info("Forward - Right")
        pyautogui.keyDown('up')
        pyautogui.keyDown("right")
        event.wait()
        pyautogui.keyUp("up")
        pyautogui.keyUp("right")

    @classmethod
    def backward_left(cls, event, logger):
        logger.info("Backward - Left")
        cls.setQ() # Geri Vitese Al 
        pyautogui.keyDown("up")
        pyautogui.keyDown("left")
        event.wait()
        pyautogui.keyUp("up")
        pyautogui.keyUp("left")
        cls.setQ() # Geri Vitesten Çık 
    @classmethod
    def backward_right(cls, event, logger):
        logger.info("Backward - Right")
        cls.setQ() # Geri Vitese Al
        pyautogui.keyDown("up")
        pyautogui.keyDown("right")
        event.wait()
        pyautogui.keyUp("up")
        pyautogui.keyUp("right")
        cls.setQ() # Geri Vitesten Çek
    
    @classmethod
    def test(cls, event, logger):
        logger.info("Test")
        pyautogui.keyDown('q')
        event.wait()
        pyautogui.keyUp('q')

    @classmethod
    def stop(cls, event, logger):
        logger.info("Stop")
        pyautogui.keyDown('s')
        event.wait()
        pyautogui.keyUp('s')
        
    @classmethod
    def reset(cls):
        keys = ['q', 'up', 'right', 'left','s']
        for _keys in keys:
            pyautogui.keyUp(_keys)

    @classmethod
    def run(cls, cmd, event):
        
        formatter = "%(asctime)s - %(name)s (%(threadName)-10s) - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=formatter)
        logger = logging.getLogger(__name__)
        
        time = '0'
        args = cmd.split(',')
        if len(args) == 1: 
	    direction = cmd.split(',')[0] 
        else:
            direction, time= cmd.split(',') 
            time = float(time)
        
        print('Running..')
        time = float(time)
        print('Direction', direction)
        print('time', time)
        
        if direction == 'U':
            #cls.forward(event)
            t = threading.Thread(target=cls.forward, args=(event, logger)).start()
        elif direction == 'UL':
            #cls.forward_left(event)
            t = threading.Thread(target=cls.forward_left, args=(event, logger)).start()
        elif direction == 'UR':
            #cls.forward_right(event)
            t = threading.Thread(target=cls.forward_right, args=(event, logger)).start()
        elif direction == 'D':
            #cls.backward(event)
            t = threading.Thread(target=cls.backward, args=(event, logger)).start()
        elif direction == 'DL':
            #cls.backward_left(event)
            t = threading.Thread(target=cls.backward_left, args=(event, logger)).start()
        elif direction == 'DR':
            #cls.backward_right(event)
            t = threading.Thread(target=cls.backward_right, args=(event, logger)).start()
        elif direction == 'S':
            #cls.stop(event)
            t = threading.Thread(target=cls.stop, args=(event, logger)).start()
        elif direction == 'LTF':
            #cls.LTF(time, event)
            t = threading.Thread(target=cls.LTF, args=(time, event, logger)).start()
        elif direction == 'RTF':
            #cls.RTF(time, event)
            t = threading.Thread(target=cls.RTF, args=(time, event, logger)).start()
        elif direction == 'test':
            t = threading.Thread(target=cls.test, args=(event, logger)).start()
        event.clear()

def main(cmd=None):
    #while True:
    KEYPRESS.run(cmd=cmd, sleep_before_run=2)

#if __name__ == '__main__':
#    main()
