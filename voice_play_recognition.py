#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospeex_core
import rospy
import re
import wave
import sys
import time

from rospeex_if import ROSpeexInterface
from rospeex_msgs.msg import SpeechRecognitionResponse 

def callback(msg):
    print(msg)

def subscriber_callback(msg):
    str = msg.message
    f = open('recognized_text.txt','w')
    f.write(str)
    f.close()

rospy.init_node("hoge")
rospy.Subscriber('/sr_res', SpeechRecognitionResponse, subscriber_callback)

interface = ROSpeexInterface()
interface.init()
interface.register_sr_response(callback)
interface.register_ss_response(callback)
#language = "en"
language = 'ja'
#voice_font = "nict(ja)"
text_data = 'recognized_text.txt'

interface.set_spi_config(language=language, engine='nict')

def recognize_speak(filename):

    w = open(filename)
    voice_data = w.read()
    print("recognize")    
    interface.recognize(voice_data, language=language, engine='nict')  
    w.close()
    
    time.sleep(1)   

    f = open(text_data)
    voice_data = f.read()
    print("speak")
    f.close()
    interface.say(voice_data, language=language, engine='nict')
    
    rospy.spin()

        
if __name__ == '__main__':
    try:
        argv = sys.argv
        if len(argv) == 1:
            print "no input files."
            sys.exit()
        filename = argv[1]
        
        interface.play_sound(filename)
        recognize_speak(filename)

        #print('check')
        #interface.say(u'てすと watashi wa robotto desu yo', language, 'nict')

        sys.exit()
    except:
        pass

