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

def ss_callback(msg):

    return

def callback(msg):
    print(msg)
    print('inside callback')
#    cbstr = msg.message
    cbstr = msg
    f = open('recognized_text.txt','w')
    f.write(cbstr)
    f.close()
    sys.stdout.write('cbstr: ')
    print(cbstr)
    f = open(text_data,'r')
    voice_data = f.read()
    voice_data = voice_data.decode('utf-8')
    sys.stdout.write('voice text:')
    print(voice_data)
    f.close()
    interface.say(voice_data, language=language, engine='nict')
    endflg = 1

rospy.init_node("hoge")
interface = ROSpeexInterface()
interface.init()

interface.register_sr_response(callback)
interface.register_ss_response(ss_callback)
#language = "en"
language = 'ja'
#voice_font = "nict(ja)"
text_data = 'recognized_text.txt'

interface.set_spi_config(language=language, engine='nict')

endflg = 0

def recognize_speak(filename):
    #speak original sound
    interface.play_sound(filename)

    w = open(filename)
    voice_data = w.read()
    print("before recognize")
    interface.recognize(voice_data, language=language, engine='nict')
    w.close()

    rospy.spin()


if __name__ == '__main__':
    try:
        argv = sys.argv
        if len(argv) == 1:
            print "no input files."
            sys.exit()
        filename = argv[1]
        recognize_speak(filename)

        #print('check')
        #interface.say(u'てすと watashi wa robotto desu yo', language, 'nict')

        sys.exit()
    except:
        pass
