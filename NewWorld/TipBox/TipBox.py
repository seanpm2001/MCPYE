# Start of script
''' TIPS '''
# Title
print ("\tMinecraft Python Edition") # Title text
print ("\t\t Tips\n\n") # Centered heading text
# Randomization
import random
ranTip = int(41) # only adjust this value to change the range of tips. It does not work with 0, or negative numbers
# Written tips section
tip1 = str("Welcome to Minecraft Python Edition")
tip2 = str("To be able to mine stone blocks, you need a pickaxe. Start with a wooden one")
tip3 = str("To be safe, try sleeping at night.")
tip4 = str("When mining, make sure to bring plenty of light sources, such as torches")
tip5 = str("Sleeping in a bed sets a spawn point, so when you die, you come back to a certain point")
tip6 = str("When you cut down a tree, items like saplings, apples, and sticks will fall. Make sure to collect everything before moving on")
tip7 = str("You can instantly grow any plant with bonemeal. Kill skeletons to get some")
tip8 = str("To swim faster in the water, start sprinting. You can also go within 1 block areas when swimming")
tip9 = str("You can modify the game files to customize your experience. Just make sure you know what you are doing")
tip10 = str("You can't mine stone or ores with an axe, hoe, or sword")
tip11 = str("When holding a sword, you can't break any blocks.")
tip12 = str("You can change settings to make it so when you die, you don't drop any items")
tip13 = str("Want to see more of the game at a time? Change your render distance! This can also make the game go faster, or slower")
tip14 = str("Ice is slippery, be careful")
tip15 = str("When walking in soul sand, you will move a lot slower")
tip16 = str("Water can't easily be placed in the nether")
tip17 = str("You can use lava around soul sand to grow plants in the nether faster")
tip18 = str("You don't have to kill a sheep to get wool. You can also use shears")
tip19 = str("Use a silk touch enchantment book to get blocks that you can't normally get with normal tools")
tip20 = str("Watch out for creepers! They will explode")
tip21 = str("Don't look an enderman in the eye")
tip22 = str("Iron golems spawn around villages. They defend villagers from hostile mobs.")
tip23 = str("If you fall from 4 blocks or more onto hard blocks without any protection, you will take damage.")
tip24 = str("With a feather falling enchantment book, you can take less fall damage from high distances")
tip25 = str("Never dig straight down, unless you want to die")
tip26 = str("When digging up, place a torch at your feet for any possible gravel or sand that may fall. The torch will break these. Also be prepared for falling water")
tip27 = str("At the bottom of the world is bedrock. Breaking this layer will send you to the void. You can't build in the void, you will just die, even in creative mode")
tip28 = str("TNT can be set off with a redstone torch, redstone, flint and steel, lava, fire charge, and more")
tip29 = str("You can fall on beds to prevent some fall damage and also bounce")
tip30 = str("Minecraft Python Edition can be played both offline and online")
tip31 = str("To sneak, press shift. When sneaking, you can place certain blocks on other blocks, and also not fall off the edge of a high or dangerous place")
tip32 = str("Minecraft Python Edition is written mostly in Python, except for some converters")
tip33 = str("You can ride over lava in an obsidian boat")
tip34 = str("You can get a grass path block by right clicking/tapping a grass block with a shovel")
tip35 = str("You can't mine titanium ore with an iron pickaxe, you will either need a titanium, diamond, or obsidian pickaxe to mine it")
tip36 = str("Magma and soul sand bubbles let you breath underwater when you swim into them")
tip37 = str("Watch out for underwater magma blocks! The bubbles will suck you in, and the magma will burn you up")
tip38 = str("Campfires are still dangerous, don't walk on them")
tip39 = str("Poison potions only take you down to half a heart, they aren't a guaranteed death sentence")
tip40 = str("Use milk to remove potion effects")
tip41 = str("Soul sand bubbles quickly take you up to the surface")
tip42 = str("Silverfish live in infested stone blocks. Make sure you build with the right kind, or you could be swarmed in silverfish")
tip43 = str("A level 2 invisibility potion not only makes your body invisible, but everything on you, armor, and the items you are holding")
tip44 = str("Sneak to place blocks on certain appliances")
tip45 = str("You can't mine bedrock unfortunately")
tip46 = str("Cobwebs slow you down when you walk into them. Use a sword to quickly break them apart")
tip47 = str("Soul sand makes you slow, but it typically isn't dangerous")
tip48 = str("You can write your own music discs and play them within the game!")
tip49 = str("Falling into the void in the nether is guaranteed death, even in creative mode")
tip50 = str("Falling into the void in the end is also guaranteed death, even in creative mode")
tip51 = str("Never sleep in the nether")
tip52 = str("Never sleep in the end")
tip53 = str("Endermen can't pick up obsidian")
tip54 = str("Be careful with the Wither boss. It can destroy any block, except for obsidian")
tip55 = str("Steel, ruby, sapphire, and titanium items and blocks were inspired by an old Minecraft mod known as \"railcraft\"")
tip56 = str("Netherrack is the weakest type of common stone")
tip57 = str("Sand falls, sandstone doesn't")
tip58 = str("Ocelots show creepers who's boss") # copied from MC-PE
tip59 = str("Only you can prevent forest fires")
tip60 = str("Don't use wood in the nether without commands")
tip61 = str("Zombies that drown underwater turn into drowned")
tip62 = str("Husk zombies not only deal damage, but they increase your hunger")
tip63 = str("Witches are skilled with potions. It takes a little strategy to defeat them without taking any damage to yourself or your armor")
tip64 = str("TNT cannot break obsidian or bedrock")
''' Custom tips section '''
tip10000 = str("") # Unknown range
tip10001 = str("") # Unknown range
tip10002 = str("") # Unknown range
# Tip randomizer
tipNum = int(random.randint(1, ranTip))
# Tip printing (prints them to the screen)
if (tipNum == 1):
	print (str(tip1))
if (tipNum == 2):
	print (str(tip2))
if (tipNum == 3):
	print (str(tip3))
if (tipNum == 4):
	print (str(tip4))
if (tipNum == 5):
	print (str(tip5))
if (tipNum == 6):
	print (str(tip6))
if (tipNum == 7):
	print (str(tip7))
if (tipNum == 8):
	print (str(tip8))
if (tipNum == 9):
	print (str(tip9))
if (tipNum == 10):
	print (str(tip10))
if (tipNum == 11):
	print (str(tip11))
if (tipNum == 12):
	print (str(tip12))
if (tipNum == 13):
	print (str(tip13))
if (tipNum == 14):
	print (str(tip14))
if (tipNum == 15):
	print (str(tip15))
if (tipNum == 16):
	print (str(tip16))
if (tipNum == 17):
	print (str(tip17))
if (tipNum == 18):
	print (str(tip18))
if (tipNum == 19):
	print (str(tip19))
if (tipNum == 20):
	print (str(tip20))
if (tipNum == 21):
	print (str(tip21))
if (tipNum == 22):
	print (str(tip22))
if (tipNum == 23):
	print (str(tip23))
if (tipNum == 24):
	print (str(tip24))
if (tipNum == 25):
	print (str(tip25))
if (tipNum == 26):
	print (str(tip26))
if (tipNum == 27):
	print (str(tip27))
if (tipNum == 28):
	print (str(tip28))
if (tipNum == 29):
	print (str(tip29))
if (tipNum == 30):
	print (str(tip30))
if (tipNum == 31):
	print (str(tip31))
if (tipNum == 32):
	print (str(tip32))
''' ADDED IN V2 '''
if (tipNum == 33):
	print (str(tip33))
if (tipNum == 34):
	print (str(tip34))
if (tipNum == 35):
	print (str(tip35))
if (tipNum == 36):
	print (str(tip36))
if (tipNum == 37):
	print (str(tip37))
if (tipNum == 38):
	print (str(tip38))
if (tipNum == 39):
	print (str(tip39))
if (tipNum == 40):
	print (str(tip40))
if (tipNum == 41):
	print (str(tip41))
if (tipNum == 42):
	print (str(tip42))
if (tipNum == 43):
	print (str(tip43))
if (tipNum == 44):
	print (str(tip44))
if (tipNum == 45):
	print (str(tip45))
if (tipNum == 46):
	print (str(tip46))
if (tipNum == 47):
	print (str(tip47))
if (tipNum == 48):
	print (str(tip48))
if (tipNum == 49):
	print (str(tip49))
if (tipNum == 50):
	print (str(tip50))
if (tipNum == 51):
	print (str(tip51))
if (tipNum == 52):
	print (str(tip52))
if (tipNum == 53):
	print (str(tip53))
if (tipNum == 54):
	print (str(tip54))
if (tipNum == 55):
	print (str(tip55))
if (tipNum == 56):
	print (str(tip56))
if (tipNum == 57):
	print (str(tip57))
if (tipNum == 58):
	print (str(tip58))
if (tipNum == 59):
	print (str(tip59))
if (tipNum == 60):
	print (str(tip60))
if (tipNum == 61):
	print (str(tip64))
if (tipNum == 62):
	print (str(tip64))
if (tipNum == 63):
	print (str(tip64))
if (tipNum == 64):
	print (str(tip64))
# end of program, enter to eiit
noMore = input("Press [ENTER] key to quit")
# End of script
