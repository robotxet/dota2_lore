#!/usr/bin/python
import codecs
import os.path
from lxml import html
import requests
import urllib

heroes = [
'Abaddon',
'Alchemist',
'Ancient_Apparition',
'Anti-Mage',
'Arc_Warden',
'Axe',
'Bane',
'Batrider',
'Beastmaster',
'Bloodseeker',
'Bounty_Hunter',
'Brewmaster',
'Bristleback',
'Broodmother',
'Centaur_Warrunner',
'Chaos_Knight',
'Chen',
'Clinkz',
'Clockwerk',
'Crystal_Maiden',
'Dark_Seer',
'Dazzle',
'Death_Prophet',
'Disruptor',
'Doom',
'Dragon_Knight',
'Drow_Ranger',
'Earth_Spirit',
'Earthshaker',
'Elder_Titan',
'Ember_Spirit',
'Enchantress',
'Enigma',
'Faceless_Void',
'Gyrocopter',
'Huskar',
'Invoker',
'Io',
'Jakiro',
'Juggernaut',
'Keeper_of_the_Light',
'Kunkka',
'Legion_Commander',
'Leshrac',
'Lich',
'Lifestealer',
'Lina',
'Lion',
'Lone_Druid',
'Luna',
'Lycan',
'Magnus',
'Medusa',
'Meepo',
'Mirana',
'Morphling',
'Monkey_King',
'Naga_Siren',
'Natures_Prophet',
'Necrophos',
'Night_Stalker',
'Nyx_Assassin',
'Ogre_Magi',
'Omniknight',
'Oracle',
'Outworld_Devourer',
'Phantom_Assassin',
'Phantom_Lancer',
'Phoenix',
'Puck',
'Pudge',
'Pugna',
'Queen_of_Pain',
'Razor',
'Riki',
'Rubick',
'Sand_King',
'Shadow_Demon',
'Shadow_Fiend',
'Shadow_Shaman',
'Silencer',
'Skywrath_Mage',
'Slardar',
'Slark',
'Sniper',
'Spectre',
'Spirit_Breaker',
'Storm_Spirit',
'Sven',
'Techies',
'Templar_Assassin',
'Terrorblade',
'Tidehunter',
'Timbersaw',
'Tinker',
'Tiny',
'Treant_Protector',
'Troll_Warlord',
'Tusk',
'Underlord',
'Undying',
'Ursa',
'Vengeful_Spirit',
'Venomancer',
'Viper',
'Visage',
'Warlock',
'Weaver',
'Windranger',
'Winter_Wyvern',
'Witch_Doctor',
'Wraith_King',
'Zeus'
]

languages = [
'english',
'russian',
# 'brazilian',
# 'bulgarian',	
# 'czech',
# 'danish',
# 'dutch',
# 'finnish',
# 'french',
# 'german',
# 'greek',
# 'hungarian',
# 'italian',
# 'japanese',
# 'koreana',
# 'norwegian',
# 'polish',
# 'portuguese',
# 'romanian',
# 'schinese',
# 'spanish',
# 'swedish',
# 'tchinese',
# 'thai',
# 'turkish'
]

DIR = "Lore"
if not os.path.exists(DIR):
  os.mkdir(DIR)

for hero in heroes:
	print "Downloading " + hero + " info"
	herodir = os.path.join(DIR, hero)
	if not os.path.exists(herodir):
		os.mkdir(herodir)
	for language in languages:
		while True:
			try:
				page = requests.get("http://www.dota2.com/hero/" + hero + "/?l=" + language)
				tree = html.fromstring(page.content)
				history = tree.xpath('//div[@id="bioInner"]/text()')
				data = history[0]
				break
			except:
				pass
		with codecs.open(os.path.join(herodir, "history_" + language + ".txt"), 'w', 'utf-8') as hist_file:
			hist_file.write(data)

		if not os.path.isfile(os.path.join(herodir, "avatar.png")):
			imglink = tree.xpath('//img[@id="heroTopPortraitIMG"]/@src')
			urllib.urlretrieve(imglink[0], os.path.join(herodir, "avatar.png"))