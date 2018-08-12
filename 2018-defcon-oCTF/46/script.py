import socket

import base64
import re

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

MORSE = {MORSE_CODE_DICT[k]:k for k in MORSE_CODE_DICT}

def start():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('172.31.2.59', 51966))
  print s.recv(1024)
  return s

debug = True

def sink(label):
  def wrapper(f):
    def wrapped(res):
      try:
        out = f(res)
        if debug:
          print '{}: {}'.format(label, out)
        return out
      except:
        return
    return wrapped
  return wrapper

@sink('b64')
def b64(res):
  return base64.b64decode(res)

@sink('morse')
def morse(res):
  return ''.join([MORSE[x] for x in res.strip().split(' ')])

@sink('binary')
def binary(res):
  return ''.join([chr(int(res[i*8:i*8+8], 2)) for i in xrange(0, len(res)/8)])

@sink('chars')
def chars(res):
  return ''.join([chr(int(x, 16)) for x in res.split(' ')])

def unknown(res):
  print 'Failed: ' + res
  raise Exception("Failed")

s = start()
while True:
  ch = s.recv(1024)
  print 'Challenge:\n{}'.format(ch)
  res = ch.split('\n')[0]
  answer = morse(res) or binary(res) or chars(res) or b64(res) or unknown(res)
  print 'Sending: ' + answer
  print
  s.send(answer + '\n')
