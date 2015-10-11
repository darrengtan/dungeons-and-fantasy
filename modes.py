import random
import common as com
import ai_scripts as ai
from class_sheet import CS
#import interact as act

#globals for character
pts_new   = 10

battle_menu = com.parseData("game_prompts.json")['text']['battle']['prompt']
monster = com.parseData("monsters.json")

def createDungeon(): #should create a Dungeon class obj
  #TODO
  print "this is where dungeons are created"
  #create Dungeon()
  #rng populate dungeon, based off of tileset -> create tilesets
  #check if dungeon goal is reachable (st_tile has path to end_tile)
  #state purpose of dungeon crawl - find treasure, kill enemy, etc.
  #return dungeon obj

#how should we battle? i guess this is the crux of the gameplay
# 1v1, 1vX?
# TODO actually develop some sort of dmg equations
def battleMode(pc):
  print 'this is battle!!!!!'

  #test gen an enemy - one at a time
  mon = random.choice(monster["monsters"].items())
  enemy = CS(mon[0], mon[1])
  print 'You are fighting a', enemy.Name
  initiative = random.randint(0,9) % 2

  player_hp = pc.HP['curr']
  mon_hp = enemy.HP['curr']

  while player_hp > 0 and mon_hp > 0:

    if initiative == 0:  # your turn
      action = com.cli(battle_menu)
      if 'attack' in action:
        dmg = pc.S['STR']
        mon_hp -= dmg
        print "You dealt", dmg, 'damage'
      elif 'skills' in action:
        print 'need to implement skillz! you just wasted a turn'
      elif 'items' in action:
        print 'need to implement items!'
      elif 'flee' in action:
        print 'You bravely ran away!'
        return

    else:  #enemy turn
      action = ai.ai_mook()
      if 'attack' in action:
        dmg = enemy.S['STR']
        player_hp -= dmg
        print enemy.Name, "has dealt", dmg, "damage to you"

    initiative = (initiative + 1) % 2

  if not player_hp > 0:
    print "You have died!"
    # do dead things
  else:
    print "You have defeated the", enemy.Name
    pc.expUp(enemy.LVL * 10)

def enterDungeon(pc, prompt):
  #load rng dungeon
  #dungeon = createDungeon()

  #run dungeon
  while True:
    action = " ".join(com.cli("How will you proceed?"))
    #dungeon.validate(action)  #what do? check against dungeon state
    #  need to place pc at start of dungeon
    #if dungeon goal is achieved, end quest/break loop

    ###test lines to implement lvlup, battle sys
    if 'lvlup' in action:
      pc.lvlUp()

    if 'battle' in action:
      battleMode(pc)

    if 'exit' in action:
      break

def newChar(prompt):
  name = com.cli(prompt["name"])
  char = CS(" ".join(name))
  print "Your name is", char.Name, '\n'

  job  = com.cli(prompt["job"])
  if '1' in job:
    char.assignClass("Warrior")
  elif '2' in job:
    char.assignClass("Mage")
  elif '3' in job:
    char.assignClass("Rogue")
  else:
    print "Learn to read."
    char.assignClass("Villager")

  print "Your profession is", char.job

  #char.assignSkills()

  print "Allocate your stat points"
  char.allocPts(pts_new)

  enterDungeon(char, prompt)

def saveChar(pc):
  import os.path
  subdir = 'saves'
  try:
    os.mkdir(subdir)
  except:
    pass

  f = open(os.path.join(subdir, pc.Name.strip().replace(' ', '_') + '.sav'), 'w')
  # write Name:{job, skills, items, equip, S, LVL, EXP, HP, MP }
  f.write('{'+pc.Name+':')
  f.write('\"job\":' + pc.job + ',')
  f.write('\"skills\":[' + ','.join(pc.skills) + '],')
  f.write('\"items\":[' + ','.join(pc.items) + '],')
  f.write('\"equip\":[' + ','.join(pc.equip) + '],')
  f.write('\"S\":{')
  for key, val in pc.S.items():    #fix
    f.write()
  #}
  f.write(',')
  f.write('\"LVL\":' + pc.LVL + ',')
  f.write('\"EXP\":' + pc.EXP + ',')
  f.write('\"HP\":' + pc.HP + ',')  #fix
  f.write('\"MP\":' + pc.MP + ',')  #fix
  f.write('}')

  f.close()

def loadChar():
  print "save game system not implemented"
  #TODO - decide if one char per or multiple
  # if no save files found, make note

  #else

funcs = {
  "loadChar": loadChar,
  "saveChar": saveChar,
  "newChar": newChar,
  "enterDungeon": enterDungeon,
  "battleMode": battleMode,
  "createDungeon": createDungeon
}
