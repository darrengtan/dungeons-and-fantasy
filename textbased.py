#!/usr/bin/env python

import sys
import common as com
import modes

###
# main entry point for game, first draft
#  handles loading, etc. - will likely change if this gets bigger
#  TODO - implement gui
###

#considerations -
# xml, json, csv files to store various resources
# decide how we want to format files
# simple save file - just save the character data, make each game a new run
#  thru a new dungeon/quest
# make a json reader/appender to simplify json creation


def options():
  #TODO - any glob flags that need to be set, do it here
  # things like difficulty, map size, etc.
  # just write out settings to options.txt or something
  print "this is where options go"

def runGame():
  #load basic game prompts
  g_prompt = com.parseData("game_prompts.json")['text']

  main_menu = g_prompt['main']['prompt']

  #main game loop
  while True:
    game_mode = com.cli(main_menu)
    #switchcase equiv
    if   '1' in game_mode:
      print "good choice! you chose New Game!"
      modes.newChar()
    elif '2' in game_mode:
      print "You chose Load Game!"
      modes.loadChar()
    elif '3' in game_mode:
      print "You chose Options!"
      options()
    elif '4' in game_mode:
      sys.exit(0)
    else:
      print "not a valid option\n"


runGame()
