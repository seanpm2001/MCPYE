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
mob_babyPigID = int(46)
mob_babyChickenID = int(47)
mob_babyCowID = int(48)
mob_babyMooshroomID = int(49)
mob_babyDuckID = int(50)
mob_babyHorseID = int(51)
mob_babyDonkeyID = int(52)
mob_babyTurkeyID = int(53)
mob_babyGoatID = int(54)
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
mob_blueParrotID = float(7.1) # Spawns in jungle biomes in treetops
'''
# Has 4 health
# Does not deal damage
# Imitates sounds from nearby mobs, will repeat things you say in chat to people who visit you
# Drops 1 blue dye, 4 feathers, and 1 bone when killed
'''
mob_redParrotID = float(7.2)
'''
# Has 4 health
# Does not deal damage
# Imitates sounds from nearby mobs, will repeat things you say in chat to people who visit you
# Drops 1 red dye, 4 feathers, and 1 bone when killed
'''
mob_peacockID = float(7.3) # Spawns in jungles around water
'''
# Has 12 health
# Does not deal damage
# Drops 6 different dyes when killed (never black, white, or grey dyes)
'''
mob_hummingBirdID = float(7.4) # Spawns in any grassy biome
'''
# Has 2 health
# Does not deal damage
# Has efficiency M (1000) by default
# Drinks sweet items
# Can fly up to 40 blocks up from the ground
# Drops 1 sugar and 1 feather when killed
'''
mob_seagullID = float(7.5) # Spawns around composters, and water
'''
# Has 8 health
# Does not deal damage
# Drops 6 feathers when killed, plus any items it picked up (capacity: 6 inventory slots)
# Steals junk items and food that are on the ground, such as dirt, apples, sand, and more
# Can fly up to 100 blocks up from the ground
# Can steal from composters
'''
mob_babyBlueParrotID = float(7.6)
mob_babyRedParrotID = float(7.7)
mob_babyPeacockID = float(7.8)
mob_babyHummingBirdID = float(7.9)
mob_babySeagullID = float(7.10)
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
mob_pufferFishID = float(11.3) # Effects the player with Poison II for 10 seconds when touched
mob_goldFishID = float(11.4)
mob_dolphinID = float(11.5)
mob_babyDolphinID = float(11.6)
mob_starfishID = float(11.7)
mob_squidID = float(11.8)
mob_babySquidID = float(11.9)
mob_spermWhaleID = float(11.10)
mob_babySpermWhaleID = float(11.11)
mob_babySharkID = float(11.12)
mob_sharkID = float(11.13)
mob_babySalmonID = float(11.14)
mob_babyGuardianID = float(11.15)
mob_babyPufferfishID = float(11.16) # Effects the player with Poison I for 10 seconds when touched
mob_babyGoldFishID = float(11.17)
mob_babyStarfishID = float(11.18)
mob_codID = float(11.19)
mob_babyCodID = float(11.20)
mob_belugaWhaleID = float(11.21)
mob_babyBelugaWhaleID = float(11.22)
mob_blueWhaleID = float(11.23)
mob_babyBlueWhaleID = float(11.24)
mob_clownfishID = float(11.25)
mob_babyClownfishID = float(11.26)
mob_squidmanID = float(11.27)
mob_babySquidmanID = float(11.28)
mob_fatalPufferfishID = float(11.29) # Effects the player with fatal poison II for 10 seconds when touched
mob_babyFatalPufferfishID = float(11.30) # Effects the player with fatal poison I for 10 seconds when touched
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
mob_chargedCreeperID = float(14.16) # To get a charged creeper, it has to be within 5 blocks of a lightning strike. Charged creeper explosions are 2x bigger than regular explosions
mob_superchargedCreeperID = float(14.17) # To get a super charged creeper, it has to be struck directly by lightning. Super charged creeper explosions are 5x bigger than charged creeper explosions, 10x bigger than normal creeper explosions. 
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
''' Insects ''' # Category 19
mob_maggotID = float(18.1)
mob_flyID = float(18.2)
mob_mosquitoID = float(18.3)
mob_poisonousMosquitoID = float(18.4)
mob_antID = float(18.5)
mob_queenAntID = float(18.6)
mob_kingAntID = float(18.7)
mob_rollyPollyID = float(18.8)
mob_giantRollyPollyID = float(18.9)
mob_honeyBeeID = float(18.10)
mob_redLadyBugID = float(18.11)
mob_blueLadyBugID = float(18.12)
mob_greenLadyBugID = float(18.13)
mob_orangeLadyBugID = float(18.14)
mob_waterSkipperID = float(18.15)
mob_syntaxErrorBugID = float(18.16) # This bug causes a syntax error on all command blocks within a 5 block radius. It only does this while editing command blocks
mob_termiteID = float(18.17) # This mob spawns when you injure but not kill other bugs near a wooden block that is either infected, or in water. Termites have only 1 health, but deal damage when there are swarms of them (1 heart for every 20 hits)
''' Wild cats ''' # Category 20
mob_babyLionID = float(19.1)
mob_lionFlagID = float(19.2)
mob_babyPumaID = float(19.3)
mob_pumaID = float(19.4)
mob_babyTigerID = float(19.5)
mob_tigerID = float(19.6)
mob_babyLeopardID = float(19.7)
mob_leopardID = float(19.8)
mob_babyPantherID = float(19.9)
mob_pantherID = float(19.10)
''' Ancient attackers ''' # Category 21
mob_babyVikingID = float(20.1) # This mob carries 2 giant iron swords, and does massive damage. It also attacks at a speed of 0.5 seconds between hits. It has heavy armor and has 100 health points
mob_vikingID = float(20.2) # This mob carries 2 giant iron swords, and does massive damage. It also attacks at a speed of 0.5 seconds between hits. It has heavy armor and has 200 health points
mob_babyCavemanID = float(20.3) # This mob commonly hides in open caves. It doesn't spawn deep in caves (more than 50 blocks in)
mob_cavemanID = float(20.4) # This mob commonly hides in open caves. It doesn't spawn deep in caves (more than 50 blocks in)
mob_babyKnightID = float(20.5) # This mob carries an iron sword, and has heavy iron armor. 
mob_knightID = float(20.6) # This mob carries an iron sword, and has heavy iron armor. 
mob_babyStarmanID = float(20.7) # this mob carries a morning star, a swinging ball of spikes. It wears leather warmor
nob_starmanID = float(20.8) # this mob carries a morning star, a swinging ball of spikes. It wears leather warmor
mob_babyArcherID = float(20.9) # This mob is skilled with a bow, unlike skeletons, the archers aim is near perfect, and it fires at 1 time every 3 seconds. It wears dyed leather armor
mob_ArcherID = float(20.10) # This mob is skilled with a bow, unlike skeletons, the archers aim is near perfect, and it fires at 1 time every 3 seconds. It wears dyed leather armor
mob_babyBarbarianID = float(20.11) # This mob goes around and kills everything. It carries an iron sword, and has moderate health. It wears leather armor. Health: 50. It hits 4 times per second, or once every 0.25 seconds
mob_BarbarianID = float(20.12) # This mob goes around and kills everything. It carries an iron sword, and has moderate health. It wears leather armor. Health: 90. It hits 4 times per second, or once every 0.25 seconds
mob_babyPirateID = float(20.13) # This mob drops gold nuggets, it has low health (10) and it can operate levers.
mob_pirateID = float(20.14) # This mob drops gold nuggets, it has low health (12) and it can operate levers.
mob_pirateCaptainID = float(20.15) # This mob is the leader of pirates. When you have a green parrot on your shoulder, it will recognize you as a pirate, and it will begin to attack you. It is a boss, and has 300 health. It attacks with cannons, and can sink boats. It will light wooden objects on fire, and will not stop until it sinks a ship.
mob_babyMummyID = float(20.16) # spawn in pyramids, 10 health, 
''' 
Easy: 0.5 damage per hit (0.25 hearts)
Medium: 1 damage per hit (0.5 hearts)
Hard: 2 damage per hit (1 heart)
Drops:
Paper, gold nuggets
'''
mob_mummyID = float(20.17) # Spawns in pyramids, 15 health
''' 
Easy: 1 damage per hit (0.5 hearts)
Medium: 2 damage per hit (1 hearts)
Hard: 4 damage per hit (2 heart)
Drops:
Paper, gold ingots
'''
mob_babyPharaohID - float(20.18) # Spawns in deserts, 50 health
'''
Baby pharaohs cannot take power from light sources to regenerate. They also don't do damage
'''
mob_pharaohID = float(20.19) # Spawns in deserts, 100 health
'''
Pharaoh - takes power from light sources to regenerate. 50 health, damage
Easy: 4 damage (2 hearts) per hit
Medium: 6 damage (3 hearts) per hit
Hard: 8 damage (4 hearts) per hit
Drops: golden power wand
'''
mob_bladesID = float(20.20) # Carries 2 metal swords, and can use both of them at once. Minimum: Iron, max: Titanium
mob_weakBladesID = float(20.21) # Carries 2 weaker swords (wood, stone, plastic) and can use them both at once
''' bosses ''' # Category 22
mob_herobrineID = float(21.1) # The true final boss of the game, and one of the hardest bosses to fight
''' Assistants ''' # Category 23
mob_friendlyLumberjackID - float(22.1) # Spawns an assistant that cuts down trees for you, just assign one to him by hitting it once
mob_digmanID = float(22.2) # Spawns an assistant that digs for you, just punch 2 blocks, and it will go and dig out an area between them. Punch the second block twice for Y=1 digging
mob_friendlyMinerID = float(22.3) # Spawns in an assistant that mines blocks for you. You can choose to make it go get all of a type of block in a set area. Just punch one side, and the other side, and the second block twice for Y=1 digging
mob_fatiguedFriendlyMinerID = float(22.4) # Spawns in an assistant miner with Mining Fatigue I. Over time, every 25 blocks that are broke, the fatigue increases by 1. It eventually maxes out at 1000. It can be cured with a slowness potion
'''
Can spawn lightning
Will strike all pigs and creepers, and make them come after you (zombie pigmen and supercharged creepers)
Has 1000000000 health
His lightning stick has knockback 500
Kills chickens and destroys their remains, along with cows, mooshrooms, vindicators, endermen, zombies, skeletons, wither skeletons, pandas, polar bears, 
His lightning stick has sharpness 80
His lightning stick gives you the wither and fatal poison effects
Does not take damage from fire, explosions, drowning, lava, poison, wither, and fall damage
DO NOT FIGHT UNTIL YOU ARE 100% READY
'''
''' Ender ''' # Category 24
mob_shulkerID = float(23.1) # A normal purple shulker
mob_pinkShulkerID = float(23.2) # A pink shulker
mob_redShulkerID = float(23.3) # A red shulker
mob_blueShulkerID = float(23.4) # A blue shulker
mob_cyanShulkerID = float(23.5) # A cyan shulker
mob_turquioseShulkerID = float(23.6) # A turquiose shulker
mob_brownShulkerID = float(23.7) # A brown shulker
mob_blackShulkerID = float(23.8) # A black shulker
mob_whiteShulkerID = float(23.0) # A white shulker
mob_greyShulkerID = float(23.10) # A Grey shulker
mob_lightGreyShulkerID = float(23.11) # A light Grey shulker
mob_darkGreyShulkerID = float(23.12) # A dark Grey shulker
mob_yellowShulkerID = float(23.13) # A yellow shulker
mob_orangeShulkerID = float(23.14) # A orange shulker
mob_limeShulkerID = float(23.15) # A lime shulker
mob_magentaShulkerID = float(23.16) # A magenta shulker
mob_stickyShulkerID = float(23.17) # A normal purple shulker (this shulker is sticky, it does not teleport)
mob_stickyPinkShulkerID = float(23.18) # A pink shulker (this shulker is sticky, it does not teleport)
mob_stickyRedShulkerID = float(23.19) # A red shulker (this shulker is sticky, it does not teleport)
mob_stickyBlueShulkerID = float(23.20) # A blue shulker (this shulker is sticky, it does not teleport)
mob_stickyCyanShulkerID = float(23.21) # A cyan shulker (this shulker is sticky, it does not teleport)
mob_stickyTurquioseShulkerID = float(23.22) # A turquiose shulker (this shulker is sticky, it does not teleport)
mob_stickyBrownShulkerID = float(23.23) # A brown shulker (this shulker is sticky, it does not teleport)
mob_stickyBlackShulkerID = float(23.24) # A black shulker (this shulker is sticky, it does not teleport)
mob_stickyWhiteShulkerID = float(23.25) # A white shulker (this shulker is sticky, it does not teleport)
mob_stickyGreyShulkerID = float(23.26) # A Grey shulker (this shulker is sticky, it does not teleport)
mob_stickyLightGreyShulkerID = float(23.27) # A light Grey shulker (this shulker is sticky, it does not teleport)
mob_stickyDarkGreyShulkerID = float(23.28) # A dark Grey shulker (this shulker is sticky, it does not teleport)
mob_stickyYellowShulkerID = float(23.29) # A yellow shulker (this shulker is sticky, it does not teleport)
mob_stickyOrangeShulkerID = float(23.30) # A orange shulker (this shulker is sticky, it does not teleport)
mob_stickyLimeShulkerID = float(23.31) # A lime shulker (this shulker is sticky, it does not teleport)
mob_stickyMagentaShulkerID = float(23.32) # A magenta shulker (this shulker is sticky, it does not teleport)
''' Mob count '''
# Category 1:
cat1Count = int(54)
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
cat8Count = int(10)
# Category 9:
cat9Count = int(4)
# Category 10:
cat10Count = int(4)
# Category 11:
cat11Count = int(4)
# Category 12:
cat12Count = int(30)
# Category 13:
cat13Count = int(15)
# Category 14:
cat14Count = int(17)
# Category 15:
cat15Count = int(17)
# Category 16:
cat16Count = int(4)
# Category 17:
cat17Count = int(10)
# Category 18:
cat18Count = int(12)
# Category 19:
cat19Count = int(17)
# Category 20:
cat20Count = int(10)
# Category 21:
cat21Count = int(21)
# Category 22:
cat22Count = int(1)
# Category 23
cat23Count = int(4)
# Category 24
cat24Count = int(32)
''' Total mob count '''
mobCount = int(cat1Count + cat2Count + cat3Count + cat4Count + cat5Count + cat6Count + cat7Count + cat8Count + cat9Count + cat10Count + cat11Count + cat12Count + cat13Count + cat14Count + cat15Count + cat16Count + cat17Count + cat18Count + cat19Count + cat20Count + cat21Count + cat22Count + cat23Count + cat24Count)
# Current total: 257 mobs
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
	print ("Category 19") # Category 19 mobs
	print ("Mob count: " + str(cat19Count))
	moreInfo1 = input("Press [ENTER] key to see category 19 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 20")
	print ("Category 20") # Category 20 mobs
	print ("Mob count: " + str(cat20Count))
	moreInfo1 = input("Press [ENTER] key to see category 20 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 21")
	print ("Category 21") # Category 21 mobs
	print ("Mob count: " + str(cat21Count))
	moreInfo1 = input("Press [ENTER] key to see category 21 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 22")
	print ("Category 22") # Category 22 mobs
	print ("Mob count: " + str(cat22Count))
	moreInfo1 = input("Press [ENTER] key to see category 22 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 23")
	print ("Category 23") # Category 23 mobs
	print ("Mob count: " + str(cat23Count))
	moreInfo1 = input("Press [ENTER] key to see category 23 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 24")
	print ("Category 24") # Category 24 mobs
	print ("Mob count: " + str(cat24Count))
	moreInfo1 = input("Press [ENTER] key to see category 24 mob listing")
	print ("Mob listing: ")
	print ("Unavailable")
	print ("End of mob listing")
	moreInfo1 = input("Press [ENTER] key to view category 25")
	print ("Category 25")
	print ("Not yet created")
	endOfMoreInfoMobList = input("You have reached the end of this files info. The rest of this file is for the game to handle. Please run the game to see what this file does")
noMore = input("Press [ENTER] key to exit this file")
print ("File exited")
print (">>> end")
''' File info '''
# Version: 9
# Language: Python 3.7.1 (Compatible with Python 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1)(not yet tested with Python 3.8/3.9)
# Size: 020,.265 bytes (020,.26 Kilobytes base 10) (when this file reaches 100.4 kilobytes in size, a megabyte conversion section will be added here) -base 2 conversion unavailable-
# Lines: 0,.503
# Unicode characters used: None
# Encoding: UTF-8
# Written with: notepad++ (7.5.9 (64 bit))
# Software group: FOSS (Free Open Source Software)
# Last modified: August 14th 2019
# Sharing status: share with anyone, don't claim as your own, don't sell for a profit
''' End of file info '''
# End of list
''' end of script '''
