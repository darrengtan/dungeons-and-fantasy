## include any shared functions in here, if needed
import json
import sys
import os

###
# basic wrapper for raw input
#  DEPRECATED --- currently converts raw to list obj
#  currently handles responses utilizing game_prompts.json fields
###
def cli(prompt):
    print prompt["prompt"]
    while 1:
        if not prompt["response"]:
            return raw_input('==> ')
        else:
            for item in prompt["response"]:
                print item
            try:
                num = int(raw_input('==> ').strip()[0])
            except KeyboardInterrupt:
                os.system("./clean")
                exit()
            except:
                print "Please enter a number"
                continue
            print num
            if num - 1 < len(prompt["response"]) and num > 0:
                return prompt["action"][num - 1]

###
# attempt at a 2-word parser
#  check input str against dictionary/ies
###
def parser():
  print 'will get around to this too'

def parseData(filename):
  data = open(filename, 'r')
  return json.load(data)

def exit(var = 0):
    print "\nExiting..."
    sys.exit(var)
