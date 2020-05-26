''' start of script '''
# Mob list
# View the mobs in the game and their ID
# There is going to be over 1000 mobs when ready
''' divider '''
# Start of list
''' Farm animals ''' # Category 1
mob_pigID = int(1)
mob_chickenID = int(2)
mob_cowID = int(3)
mob_mooshroomID = int(4)
mob_duckID = int(5)
mob_horseID = int(6)
mob_donkeyID = int(7)
mob_goatID = int(8)
mob_turkeyID = int(9)
mob_whiteSheepID = int(10)
mob_blackSheepID = int(11)
mob_lightGreySheepID = int(12)
mob_darkGreySheepID = int(13)
mob_redSheepID = int(14)
mob_yellowSheepID = int(15)
mob_brownSheepID = int(16)
mob_lightBlueSheepID = int(17)
mob_darkBlueSheepID = int(18)
mob_cyanSheepID = int(19)
mob_turquioseSheepID = int(20)
mob_silverSheepID = int(21)
mob_orangeSheepID = int(22)
mob_purpleSheepID = int(23)
mob_pinkSheepID = int(24)
mob_greenSheepID = int(25)
mob_rainbowSheepID = int(26)
mob_babywhiteSheepID = int(27)
mob_babyblackSheepID = int(28)
mob_babylightGreySheepID = int(29)
mob_babydarkGreySheepID = int(30)
mob_babyredSheepID = int(31)
mob_babyyellowSheepID = int(32)
mob_babybrownSheepID = int(33)
mob_babylightBlueSheepID = int(34)
mob_babydarkBlueSheepID = int(35)
mob_babycyanSheepID = int(36)
mob_babyturquioseSheepID = int(37)
mob_babysilverSheepID = int(38)
mob_babyorangeSheepID = int(39)
mob_babypurpleSheepID = int(40)
mob_babypinkSheepID = int(41)
mob_babygreenSheepID = int(42)
mob_babyrainbowSheepID = int(43)
mob_babyMuleID = int(44)
mob_muleID = int(45)
''' Apocalypse ''' # Category 2
mob_normalZombieID = float(1.1)
mob_villagerZombieID = float(1.2)
mob_babyNormalZombieID = float(1.3)
mob_babyVillagerZombieID = float(1.4)
mob_giantNormalZombieID = float(1.5)
mob_giantVillagerZombieID = float(1.6)
mob_babyDrownedID = float(1.7)
mob_drownedID = float(1.8)
mob_babyChickenJockey = float(1.9)
''' Skeletons ''' # Category 3
mob_unarmedSkeletonID = float(2.1)
mob_armedSkeletonID = float(2.2)
mob_babyUnarmedSkeletonID = float(2.3)
mob_babyArmedSkeletonID = float(2.4)
mob_witherSkeletonID = float(2.5)
mob_babyWitherSkeletonID = float(2.6)
mob_skeletonHorseID = float(2.7)
mob_babySkeletonHorseID = float(2.8)
''' Magical ''' # Category 4
mob_witchID = float(3.1)
mob_babyWitchID = float(3.2)
''' In the end ''' # Category 5
mob_enderDragonID = float(4.1)
mob_endermanID = float(4.2)
''' Nether ''' # Category 6
mob_blazeID = float(5.1)
mob_babyBlazeID = float(5.2)
mob_magmaCubeSmallID = float(5.3)
mob_magmaCubeMediumID = float(5.4)
mob_magmaCubeLargeID = float(5.5)
mob_magmaCubeXLargeID = float(5.6)
mob_magmaCubeMassiveID = float(5.7)
mob_zombiePigmanID = float(5.8)
mob_babyZombiePigmanID = float(5.9)
mob_ghastID = float(5.10)
mob_babyGhastID = float(5.11)
mob_witherID = float(5.12)
''' Villagers ''' # Category 7
mob_testificateID = float(6.1)
mob_classicVillager1ID = float(6.2)
mob_classicVillager2ID = float(6.3)
mob_classicVillager3ID = float(6.4)
mob_classicVillager4ID = float(6.5)
mob_classicVillager5ID = float(6.6)
mob_librarianVillagerID = float(6.7)
mob_clericVillagerID = float(6.8)
mob_butcherVillagerID = float(6.9)
mob_farmerVillagerID = float(6.10)
mob_blackSmithVillagerID = float(6.11)
''' More birds ''' # Category 8
mob_blueParrotID = float(7.1)
mob_redParrotID = float(7.2)
mob_peacockID = float(7.3)
mob_hummingBirdID = float(7.4)
''' On the beach ''' # Category 9
mob_turtleID = float(8.1)
mob_babyTurtleID = float(8.2)
mob_redTurtleID = float(8.3)
mob_greenTurtleID = float(8.4)
''' The pillager army ''' # Category 10
mob_vindicatorID = float(9.1)
mob_ravagerID = float(9.2)
mob_pillagerID = float(9.3)
mob_evokerID = float(9.4)
''' Bears ''' # Category 11
mob_brownBearID = float(10.1)
mob_pandaID = float(10.2)
mob_GrizzlyBearID = float(10.3)
mob_polarBearID = float(10.4)
''' Under the sea ''' # Category 12
mob_salmonID = float(11.1)
mob_guardianID = float(11.2)
mob_pufferFishID = float(11.3)
mob_goldFishID = float(11.4)
mob_dolphinID = float(11.5)
mob_babyDolphinID = float(11.6)
mob_starfishID = float(11.7)
''' Defenders of the village ''' # Category 13
mob_ironGolemID = float(12.1)
mob_babyIronGolemID = float(12.2)
mob_ironGolemiteID = float(12.3)
mob_steelGolemID = float(12.4)
mob_babySteelGolemID = float(12.5)
mob_steelGolemiteID = float(12.6)
mob_goldGolemID = float(12.7)
mob_babyGoldGolemID = float(12.8)
mob_goldGolemiteID = float(12.9)
mob_emeraldGolemID = float(12.10)
mob_babyEmeraldGolemID = float(12.11)
mob_emeraldGolemiteID = float(12.12)
mob_diamondGolemID = float(12.13)
mob_babyDiamondGolemID = float(12.14)
mob_diamonddGolemiteID = float(12.15)
''' Companions ''' # Category 14
mob_wolfID = float(13.1)
mob_babyWolfID = float(13.2)
mob_ocelotID = float(13.3)
mob_babyOcelotID = float(13.4)
mob_foxID = float(13.5)
mob_babyFoxID = float(13.6)
mob_kittenID = float(13.7)
mob_catID = float(13.8)
mob_firefoxID = float(13.9)
mob_babyFirefoxID = float(13.10)
mob_firefoxQuantumID = float(13.11)
mob_babyFirefoxQuantumID = float(13.12)
mob_waterfoxID = float(13.13)
mob_babyWaterfoxID = float(13.14)
mob_iceFoxID = float(13.15)
mob_babyIceFoxID = float(13.16)
mob_GNU_IcecatID = float(13.17)
''' Creepy crawlies, lizards and bombers ''' # Category 15
mob_caveSpiderID = float(14.1)
mob_spiderID = float(14.2)
mob_skeletonJockeyID = float(14.3)
mob_babyCreeperID = float(14.4)
mob_creeperID = float(14.5)
mob_giantCreeperID = float(14.6)
mob_bluePythonID = float(14.7)
mob_yellowPythonID = float(14.8)
mob_blueAndYellowPythonID = float(14.9)
mob_chameleonID = float(14.10)
mob_babyChameleonID = float(14.11)
mob_cobraID = float(14.12)
mob_babyCobraID = float(14.13)
mob_greenGeckoID = float(14.14)
mob_babyGreenGeckoID = float(14.15)
''' Hidden enemies ''' # Category 16
mob_silverfishID = float(15.1)
mob_enderMiteID = float(15.2)
mob_babySilverfishID = float(15.3)
mob_babyEndermiteID = float(15.4)
''' Swamp dwellers ''' # Category 17
mob_slimeSmallID = float(16.1)
mob_slimeMediumID = float(16.2)
mob_slimeLargeID = float(16.3)
mob_slimeXLargeID = float(16.4)
mob_silimeMassiveID = float(16.5)
mob_ogreID = float(16.6)
mob_babyOgreID = float(16.7)
mob_greenTreeFrogID = float(16.8)
mob_GreenTreeFrogTadpoleID = float(16.9)
mob_giantOgreID = float(16.10)
''' Rodents ''' # Category 18
mob_babyMouseID = float(17.1)
mob_mouseID = float(17.2)
mob_babyRatID = float(17.3)
mob_ratID = float(17.4)
mob_babyFerretID = float(17.5)
mob_ferretID = float(17.6)
mob_babyGopherID = float(17.7)
mob_gopherID = float(17.8)
mob_babyGroundHogID = float(17.7)
mob_groundHogID = float(17.10)
mob_babyMoleID = float(17.11)
mob_moleID = float(17.12)
''' Mob count '''
# Category 1:
cat1Count = int(45)
# Category 2:
cat2Count = int(9)
# Category 3:
cat3Count = int(8)
# Category 4:
cat4Count = int(2)
# Category 5:
cat5Count = int(2)
# Category 6:
cat6Count = int(12)
# Category 7:
cat7Count = int(11)
# Category 8:
cat8Count = int(4)
# Category 9:
cat9Count = int(4)
# Category 10:
cat10Count = int(4)
# Category 11:
cat11Count = int(4)
# Category 12:
cat12Count = int(7)
# Category 13:
cat13Count = int(15)
# Category 14:
cat14Count = int(17)
# Category 15:
cat15Count = int(15)
# Category 16:
cat16Count = int(4)
# Category 17:
cat17Count = int(10)
# Category 18:
cat18Count = int(12)
''' Total mob count '''
mobCount = int(cat1Count + cat2Count + cat3Count + cat4Count + cat5Count + cat6Count + cat7Count + cat8Count + cat9Count + cat10Count + cat11Count + cat12Count + cat13Count + cat14Count + cat15Count + cat16Count + cat17Count + cat18Count)
# Current total: 185 mobs
''' File info '''
print ("This is a ID resource file for mob IDs. Modifying this file can cause the game to stop working properly if not properly configured")
print ("This is an important game resource file. Be careful when using it.")
print ("There is a total number of " + str(mobCount) + " mobs in this list")
catInfo = str(input("Type in the letter m to view the mob listing in categories"))
catInfo = catInfo.upper() # Makes the input an uppercase letter
if (catInfo == "M"): # Even if you type it lowercase, it will still count with the upper() method
	print ("Category 1") # Category 1 mobs
	print ("Mob count: " + str(cat1Count))
	moreInfo1 = input("Press [ENTER] key to see category 1 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 2")
	print ("Category 2") # Category 2 mobs
	print ("Mob count: "  + str(cat2Count))
	moreInfo1 = input("Press [ENTER] key to see category 2 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 3")
	print ("Category 3") # Category 3 mobs
	print ("Mob count: " + str(cat3Count))
	moreInfo1 = input("Press [ENTER] key to see category 3 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 4")
	print ("Category 4") # Category 4 mobs
	print ("Mob count: " + str(cat4Count))
	moreInfo1 = input("Press [ENTER] key to see category 4 mob listing")
	print ("Mob listing: ")
	print ("| Witch")
	print ("| Baby witch")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 5")
	print ("Category 5") # Category 5 mobs
	print ("Mob count: " + str(cat5Count))
	moreInfo1 = input("Press [ENTER] key to see category 5 mob listing")
	print ("Mob listing: ")
	print ("| Ender dragon")
	print ("| Enderman")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 6")
	print ("Category 6") # Category 6 mobs
	print ("Mob count: " + str(cat6Count))
	moreInfo1 = input("Press [ENTER] key to see category 6 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 7")
	print ("Category 7") # Category 7 mobs
	print ("Mob count: " + str(cat7Count))
	moreInfo1 = input("Press [ENTER] key to see category 7 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 8")
	print ("Category 8") # Category 8 mobs
	print ("Mob count: " + str(cat8Count))
	moreInfo1 = input("Press [ENTER] key to see category 8 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 9")
	print ("Category 9") # Category 9 mobs
	print ("Mob count: " + str(cat9Count))
	moreInfo1 = input("Press [ENTER] key to see category 9 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 10")
	print ("Category 10") # Category 10 mobs
	print ("Mob count: " + str(cat10Count))
	moreInfo1 = input("Press [ENTER] key to see category 10 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 11")
	print ("Category 11") # Category 11 mobs
	print ("Mob count: " + str(cat11Count))
	moreInfo1 = input("Press [ENTER] key to see category 11 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 12")
	print ("Category 12") # Category 12 mobs
	print ("Mob count: " + str(cat12Count))
	moreInfo1 = input("Press [ENTER] key to see category 12 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 13")
	print ("Category 13") # Category 13 mobs
	print ("Mob count: " + str(cat13Count))
	moreInfo1 = input("Press [ENTER] key to see category 13 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 14")
	print ("Category 14") # Category 14 mobs
	print ("Mob count: " + str(cat14Count))
	moreInfo1 = input("Press [ENTER] key to see category 14 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 15")
	print ("Category 15") # Category 15 mobs
	print ("Mob count: " + str(cat15Count))
	moreInfo1 = input("Press [ENTER] key to see category 15 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 16")
	print ("Category 16") # Category 16 mobs
	print ("Mob count: " + str(cat16Count))
	moreInfo1 = input("Press [ENTER] key to see category 16 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 17")
	print ("Category 17") # Category 17 mobs
	print ("Mob count: " + str(cat17Count))
	moreInfo1 = input("Press [ENTER] key to see category 17 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 18")
	print ("Category 18") # Category 18 mobs
	print ("Mob count: " + str(cat18Count))
	moreInfo1 = input("Press [ENTER] key to see category 18 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 19")
	print ("Category 19")
	print ("Not yet created")
	endOfMoreInfoMobList = input("You have reached the end of this files info. The rest of this file is for the game to handle. Please run the game to see what this file does")
noMore = input("Press [ENTER] key to exit this file")
print ("File exited")
print (">>> end")
''' File info '''
# Version: 4
# Language: Python 3.7.1 (Compatible with Python 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1)(not yet tested with Python 3.8/3.9)
# Size: 13,.604 bytes (13,.60 Kilobytes)
# Lines: 0,.377
# Unicode characters used: None
# Written with: notepad++ (7.5.9 (64 bit))
# Software group: FOSS (Free Open Source Software)
# Sharing status: share with anyone, don't claim as your own, don't sell for a profit
''' End of file info '''
# End of list
''' end of script '''