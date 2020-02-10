# -*- coding: utf-8 -*-
import threading
import time
import logging
from keypresser_event import KEYPRESS_EVENT as KE
import os

    
if __name__ == '__main__':
    start_event = threading.Event()
    print("\033[01;31m Started \033[00m")

    #t_one = threading.Thread(target=thread_one, args=(start_event,)).start()
    #t_two = threading.Thread(target=thread_two, args=(start_event,)).start()
    cmd_list = ['U','UL','UR','D','DL','DR','S']
    for cmd in cmd_list: 
        KE.run(cmd, start_event)
        #Process    
        for i in range(3):
            print("\033[01;32m{}\033[00m".format(i))
            time.sleep(1)
        #End
        start_event.set()
    


