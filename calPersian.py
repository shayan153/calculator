#Developed by Shayan
#calculator
#nokte: in mashin hesab faghat ta 2 adad suport mikonad
import os
import sys
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
import ConfigParser
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
def clearScr():
    os.system('clear')
clearScr()
def hesab():
    l=input(color_random[9]+'''
khob hala mikhay che amaliaty angam bedy??
baray jam bezan----{'+'}
baray tafrigh bezan-----{'-'}
baray zarb bezan---{'*'}
baray taghsim bezan----------{'/'}
== ''')
    number1=float(input('Enter Number ='))
    number2=float(input('Enter Number ='))
    if l=='+':
        print(number1+number2)
    elif l=='-':
        print(number1-number2)
    elif l=='*':
        print(number1*number2)
    elif l=='/':
        print(number1/number2)
    else:
        print(color_random[5]+'''
lotfan az gozine ha entekhab kon
gozineha:
zarb:+
taghsim:/
jam:+
tafrigh:- ''')
        
    again()
        
def again():
    m=input(color_random[4]+'''
aya dost darid baz hesab konid
age are bezan 'Y'
age na bezan 'N'
== ''')
    if m.upper()=='Y':
        hesab()
    elif m.upper()=='N':
        print('mamnoon az entekhabeton va beomiddidar :)')
    else:
        again()
hesab()
