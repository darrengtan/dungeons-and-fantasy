import common as com
import json

pts_lvlup = 2

class CS: #class sheet - rename
  Name = ""
  job = "" #keep it simple
  skills = []
  items = []
  equip = []
  S = dict(STR = 5,
  AGI = 5,
  INT = 5,
  END = 5)
  LVL = 0
  EXP = 0
  HP = {'curr':100, 'max':100}
  MP = {'curr':100, 'max':100}  # could simplify by storing curr health only in battle

  def __init__(self, name, dct = {}):
    self.Name = name
    if dct:
      self.S = dct['S']
      self.LVL = dct['LVL']
      self.HP, self.MP = dct['HP'].copy(), dct['MP'].copy()

  def useItem():  #TODO
    print 'another stub'

  def assignEquip(): #TODO
    print 'yay!'

  def assignSkills():
    if   classname == 'Warrior':
      self.skills.append('')
    elif classname == "Mage":
      self.skills.append('')
    elif classname == "Rogue":
      self.skills.append('')
    else:
      self.skills.append('')

  def assignClass(self, classname):
    if   classname == 'Warrior':
      self.job = "Warrior"
    elif classname == "Mage":
      self.job = "Mage"
    elif classname == "Rogue":
      self.job = "Rogue"
    else:
      self.job = "Villager"

  def allocPts(self, free_pts):  #this is gross, need to clean up
    inc = 0
    while free_pts > 0:
      print "You have", free_pts, "points to spend"
      for i, stat in enumerate(dict.iteritems(self.S)):
        print str(i+1)+'.', stat[0], '=', stat[1]
      inc = com.cli()
      for i, stat in enumerate(dict.iteritems(self.S)):
        if any(word in str(i+1)+'. '+ stat[0] for word in inc):
          self.S[stat[0]] += 1
          free_pts -= 1

    print "Current stats are:"
    for stat in dict.iteritems(self.S):
      print stat[0], '=', stat[1]
    print self.HP['max'], self.MP['max']

  def expUp(self, exp_gain):
    self.EXP += exp_gain
    print self.Name, 'has earned', exp_gain, "EXP points!"
    #arbitrary lvl up
    if self.EXP > ((10 * self.LVL) ** 2):
      self.lvlUp()

  def updateEnergies(self):
    self.HP['max'] = self.S['END'] * self.LVL + 100
    self.MP['max'] = self.S['INT'] * self.LVL + 100
    self.HP['curr'] = self.HP['max']
    self.MP['curr'] = self.MP['max']

  def lvlUp(self):
    self.LVL += 1
    self.updateEnergies()
    self.allocPts(pts_lvlup)

