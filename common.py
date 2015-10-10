## include any shared functions in here, if needed
import json

###
# basic wrapper for raw input
#  currently converts raw to list obj
###
def cli(text=''):
  if text != '': 
    print text
  return raw_input('==> ').split()
"""  alternate wrap if we're just gonna use int responses - convs raw to int
  while 1:
    num = raw_input('==> ')
    try:
      return int(num.strip()[0])
    except:
      print "Please enter a numeric option"
      pass
"""


###
# attempt at a 2-word parser
#  check input str against dictionary/ies
###
def parser():
  print 'will get around to this too'

def parseData(filename):
  data = open(filename, 'r')
  return json.load(data)
