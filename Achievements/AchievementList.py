''' start of script '''
# Achievement list
# View the achievements in the game, and their ID
# There is going to be over 1000 achievements when ready
''' divider ''' 
# Start of list
''' Overworld ''' # Category 1
quest_firstDayID = float(0.1)
quest_firstDayStr = str("First day\nSurvive the first night")
quest_gettingDirtyID = float(0.2)
quest_gettingDirtyStr = str("Getting dirty\nDig 256 dirt blocks without any tools")
''' Nether ''' # Category 2
quest_intoTheUnderworldID = float(1.1)
quest_intoTheUnderworldStr = str("Into the underworld\nVisit the Nether for the first time")
quest_eternalSadnessID = float(1.2)
quest_eternalSadnessStr = str("Eternal sadness\nKill a ghast")
quest_firefoxquantumID = float(1.3)
quest_firefoxquantumStr = str("Firefox Quantum\nLight a Firefox on fire")
quest_bedtimeqmarkID = float(1.5)
quest_bedtimeqmarkStr = str("Bedtime?\nDetonate a bed when trying to sleep in the nether")
quest_ghastHouseID = float(1.6)
quest_ghastHouseStr = str("Ghast house\nKill 25 ghast in a row in a nether haunted mansion")
quest_acquireQuartzID = float(1.7)
quest_acquireQuartzStr = str("Acquire quartz\nMine quartz in the nether")
quest_sandOfSoulsID = float(1.8)
quest_sandOfSoulsStr = str("Sand of soulds\nCollect 4 soul sand in the nether")
quest_bayOfPigsID = float(1.9)
quest_bayOfPigsStr = str("Bay of pigs\nAggrevate 50 zombie pigmen with 1 punch")
''' Mining ''' # Category 3
quest_coalMinerID = float(2.1)
quest_coalMinerStr = str("Coal miner\nGather 3 coal while mining")
quest_stoneAgeID = float(2.2)
quest_stoneAgeStr = str("Stone age\nMine a piece of stone with a wooden pickaxe")
quest_ironAgeID = float(2.3)
quest_ironAgeStr = str("Iron age\nSmelt iron in a furnace")
quest_gettingAnUpgradeID = float(2.4)
quest_gettingAnUpgradeStr = str("Getting an upgrade\nCraft a stone pickaxe")
''' End ''' # Category 4
quest_dragonSlayerID = float(3.1)
quest_dragonSlayerStr = str("Dragon slayer\nDefeat the ender dragon")
''' Items ''' # Category 5
quest_masterCraftsmanID = float(4.1)
quest_masterCraftsmanStr = str("Master craftsman\nUse a crafting table to craft every item in the game")
''' Exploring ''' # Category 6
quest_adventureTimeID = float(5.1)
quest_adventureTimeStr = str("Adventure time\nExplore every biome")
''' Combat ''' # Category 7
quest_theShiningID = float(6.1)
quest_theShiningStr = str("The shining\nSpawn a vindicator named Johnny in hard mode")
quest_heresJohnnyID = float(6.2)
quest_heresJohnnyStr = str("Here's Johnny!!!\nHave a vindicator chop down your door")
quest_creeperAwManID = float(6.3)
quest_creeperAwManStr = str("Creeper... Aw man\nEncounter a creeper")
quest_safeFromSlendermanID = float(6.4)
quest_safeFromSlendermanStr = str("Safe from slenderman\nEscape an enderman by going into water, or a 2 block high area.")
quest_notTodayThankYouID = float(6.5)
quest_notTodayThankYouStr = str("Not today, thank you\nDeflect a skeletons arrow with a shield")
quest_monsterHunterID = float(6.6)
quest_monsterHunterStr = str("Monster hunter\nKill an enemy")
''' Quest count '''
# Category 1
cat1Count = int(2)
# Category 2
cat2Count = int(9)
# Category 3
cat3Count = int(4)
# Category 4
cat4Count = int(1)
# Category 5
cat5Count = int(1)
# Category 6
cat6Count = int(1)
# Category 7
cat7Count = int(6)
# Achievement counter
achievementCountInt = int(cat1Count + cat2Count + cat3Count + cat4Count + cat5Count + cat6Count + cat7Count)
# Achievement count: 24 (last updated: August 21st 2019)
'''
User opens the file section
'''
print ("This is a resource file for the list of achievements. Be careful modifying this file.")
print ("Total amount of achievements: " + str(achievementCountInt))
noMore = input("Press [ENTER] key to exit this file")
'''
File info
Lines of code: 0,.093
Character count: 003,.962
Written in: Python
Last modified: August 21st 2019
File version: 2
'''
# End of list
''' end of script '''
