""" Start of script """
# Block list
# View the blocks in the game and their ID
# There is going to be over 10000 blocks when ready
''' Dirt ''' # Category 1
block_dirtID = int(1)
block_coarseDirtID = int(2)
block_podzolID = int(3)
block_myceliumID = int(4)
block_grassPathID = int(5)
block_fertileDirtID = int(6)
block_wetFertileDirtID = int(7)
block_swampGrassDirtID = int(8)
block_grassBlockID = int(9)
block_deadGrassBlockID = int(10)
block_witherGrassBlockID = int(11)
block_netherGrassBlockID = int(12)
block_endGrassBlockID = int(13)
block_yellowGrassBlockID = int(14)
block_jungleGrassBlockID = int(15)
''' Stone ''' # Category 2
block_caveStoneID = float(1.1)
block_cobbleStoneID = float(1.2)
block_mossyCobbleStoneID = float(1.3)
block_smoothStoneID = float(1.4)
block_obsidianID = float(1.5)
block_bedrockID = float(1.6)
block_blueStoneID = float(1.7)
block_brimstoneID = float(1.8)
block_infestedCobblestoneID = float(1.9)
block_infestedMossyCobblestoneID = float(1.10)
block_blueCobblestoneID = float(1.11)
block_mossyBlueCobblestoneID = float(1.12)
block_infestedBlueCobblestoneID = float(1.13)
block_infestedMossyBlueCobblestoneID = float(1.14)
block_limeCobblestoneID = float(1.15)
block_mossyLimeCobblestoneID = float(1.16)
block_infestedLimeCobblestoneID = float(1.17)
block_infestedMossyLimeCobblestoneID = float(1.18)
block_greenCobblestoneID = float(1.19)
block_mossyGreenCobblestoneID = float(1.20)
block_infestedGreenCobblestoneID = float(1.21)
block_infestedMossyGreenCobblestoneID = float(1.22)
block_silverStoneID = float(1.23)
block_foolsGoldBlockID = float(1.24)
block_micaBlockID = float(1.25)
block_smoothMicaBlockID = float(1.26)
block_whiteMarbleBlockID = float(1.27)
block_smoothWhiteMarbleBlockID = float(1.28)
block_blackMarbleBlockID = float(1.29)
block_smoothBlackMarbleBlockID = float(1.30)
block_linoleumBlockID = float(1.31)
''' Slabs ''' # Category 3
block_dirtSlabID = float(2.1)
block_coarseDirtSlabID = float(2.2)
block_podzolSlabID = float(2.3)
block_myceliumSlabID = float(2.4)
block_grassPathSlabID = float(2.5)
block_caveStoneSlabID = float(2.6)
block_mossyCobbleStoneSlabID = float(2.7)
block_smoothStoneSlabID = float(2.8)
block_obsidianSlabID = float(2.9)
block_bedrockSlabID = float(2.10)
block_gravelSlabID = float(2.11)
block_goldSlabID = float(2.12)
block_purpurSlabID = float(2.13)
block_OakWoodPlankSlabID = float(2.14)
block_darkOakWoodPlankSlabID = float(2.15)
block_acaciaWoodPlankSlabID = float(2.16)
block_birchWoodPlankSlabID = float(2.17)
block_spruceWoodPlankSlabID = float(2.18)
block_jungleWoodPlankSlabID = float(2.19)
block_cherryWoodPlankSlabID = float(2.20)
block_locustWoodPlankSlabID = float(2.21)
block_appleWoodPlankSlabID = float(2.22)
block_ashWoodPlankSlabID = float(2.23)
block_diamondSlabID = float(2.24)
block_OakWoodLogSlabID = float(2.25)
block_darkOakWoodLogSlabID = float(2.26)
block_acaciaWoodLogSlabID = float(2.27)
block_birchWoodLogSlabID = float(2.28)
block_spruceWoodLogSlabID = float(2.29)
block_jungleWoodLogSlabID = float(2.30)
block_cherryWoodLogSlabID = float(2.31)
block_locustWoodLogSlabID = float(2.32)
block_appleWoodLogSlabID = float(2.33)
block_ashWoodLogSlabID = float(2.34)
block_ironSlabID = float(2.35)
block_graniteSlabID = float(2.36)
block_polishedGraniteSlabID = float(2.37)
block_andesiteSlabID = float(2.38)
block_polishedAndesiteSlabID = float(2.39)
block_dioriteSlabID = float(2.40)
block_polishedDioriteSlabID = float(2.41)
block_chocolateSlabID = float(2.42)
block_tinSlabID = float(2.43)
block_steelSlabID = float(2.44)
block_aluminumSlabID = float(2.45)
block_silverSlabID = float(2.46)
block_bronzeSlabID = float(2.47)
block_titaniumSlabID = float(2.48)
block_pineWoodPlanksSlabID = float(2.49)
block_palmWoodPlanksSlabID = float(2.50)
block_acornWoodPlanksSlabID = float(2.51)
block_sycamoreWoodPlanksSlabID = float(2.52)
block_chestnutWoodPlanksSlabID = float(2.53)
block_pineWoodLogSlabID = float(2.54)
block_palmWoodLogSlabID = float(2.55)
block_acornWoodLogSlabID = float(2.56)
block_sycamoreWoodLogSlabID = float(2.57)
block_chestnutWoodLogSlabID = float(2.58)
block_strippedpineWoodPlanksSlabID = float(2.59)
block_strippedpalmWoodPlanksSlabID = float(2.60)
block_strippedacornWoodPlanksSlabID = float(2.61)
block_strippedsycamoreWoodPlanksSlabID = float(2.62)
block_strippedchestnutWoodPlanksSlabID = float(2.63)
block_strippedpineWoodLogSlabID = float(2.64)
block_strippedpalmWoodLogSlabID = float(2.65)
block_strippedacornWoodLogSlabID = float(2.66)
block_strippedsycamoreWoodLogSlabID = float(2.67)
block_strippedchestnutWoodLogSlabID = float(2.68)
block_brimStoneSlabID = float(2.69)
block_infestedCobblestoneSlabID = float(2.70)
block_infestedMossyCobblestoneSlabID = float(2.71)
block_blueCobblestoneSlabID = float(2.71)
block_mossyBlueCobblestoneSlabID = float(2.72)
block_infestedBlueCobblestoneSlabID = float(2.73)
block_infestedMossyBlueCobblestoneSlabID = float(2.74)
block_limeCobblestoneSlabID = float(2.75)
block_mossyLimeCobblestoneSlabID = float(2.76)
block_infestedLimeCobblestoneSlabID = float(2.77)
block_infestedMossyLimeCobblestoneSlabID = float(2.78)
block_greenCobblestoneSlabID = float(2.79)
block_mossyGreenCobblestoneSlabID = float(2.80)
block_infestedGreenCobblestoneSlabID = float(2.81)
block_infestedMossyGreenCobblestoneSlabID = float(2.82)
block_whiteMarbleSlabID = float(2.83)
block_smoothWhiteMarbleSlabID = float(2.84)
block_blackMarbleSlabID = float(2.85)
block_smoothBlackMarbleSlabID = float(2.86)
block_linoleumSlabID = float(2.87)
block_yellowGrassSlabID = float(2.88)
block_endGrassSlabID = float(2.89)
block_netherGrassSlabID = float(2.90)
''' Stairs ''' # Category 4
block_dirtStairsID = float(3.1)
block_coarseDirtStairsID = float(3.2)
block_podzolStairsID = float(3.3)
block_obsidianStairsID = float(3.4)
block_yellowSandStairsID = float(3.5)
block_bedrockStairsID = float(3.6)
block_gravelStairsID = float(3.7)
block_myceliumStairsID = float(3.8)
block_grassPathStairsID = float(3.9)
block_mossyCobbleStoneStairsID = float(3.10)
block_cobblestoneStairsID = float(3.11)
block_smoothStoneStairsID = float(3.12)
block_goldStairsID = float(3.13)
block_purpurStairsID = float(3.14)
block_diamondStairsID = float(3.15)
block_sapphireStairsID = float(3.16)
block_titaniumStairsID = float(3.17)
block_oakWoodPlankStairsID = float(3.18)
block_oakWoodLogStairsID = float(3.19)
block_strippedoakWoodPlankStairsID = float(3.20)
block_strippedoakWoodLogStairsID = float(3.21)
block_ironStairsID = float(3.22)
block_graniteStairsID = float(3.23)
block_polishedGraniteStairsID = float(3.24)
block_andesiteStairsID = float(3.25)
block_polishedAndesiteStairsID = float(3.26)
block_dioriteStairsID = float(3.27)
block_polishedDioriteStairsID = float(3.28)
block_chocolateStairsID = float(3.29)
block_strippedOakWoodPlankStairsID = float(3.30)
block_strippedOakWoodLogStairsID = float(3.31)
block_darkOakWoodPlankStairsID = float(3.32)
block_darkOakWoodLogStairsID = float(3.33)
block_strippedDarkOakWoodPlankStairsID = float(3.34)
block_strippedDarkOakWoodLogStairsID = float(3.35)
block_acaciaWoodPlankStairsID = float(3.36)
block_acaciaWoodLogStairsID = float(3.37)
block_strippedAcaciaWoodPlankStairsID = float(3.38)
block_strippedAcaciaWoodLogStairsID = float(3.39)
block_birchWoodPlankStairsID = float(3.40)
block_birchWoodLogStairsID = float(3.41)
block_strippedBirchWoodPlankStairsID = float(3.42)
block_strippedBirchWoodLogStairsID = float(3.43)
block_spruceWoodPlankStairsID = float(3.44)
block_spruceWoodLogStairsID = float(3.45)
block_strippedSpruceWoodPlankStairsID = float(3.46)
block_strippedSpruceWoodLogStairsID = float(3.47)
block_jungleWoodPlankStairsID = float(3.48)
block_jungleWoodLogStairsID = float(3.49)
block_strippedJungleWoodPlankStairsID = float(3.50)
block_strippedJungleWoodLogStairsID = float(3.51)
block_cherryWoodPlankStairsID = float(3.52)
block_cherryWoodLogStairsID = float(3.53)
block_strippedCherryWoodPlankStairsID = float(3.54)
block_strippedCherryWoodLogStairsID = float(3.55)
block_locustWoodPlankStairsID = float(3.56)
block_locustWoodLogStairsID = float(3.57)
block_strippedLocustWoodPlankStairsID = float(3.58)
block_strippedLocustWoodLogStairsID = float(3.59)
block_appleWoodPlankStairsID = float(3.60)
block_appleWoodLogStairsID = float(3.61)
block_strippedAppleWoodPlankStairsID = float(3.62)
block_strippedAppleWoodLogStairsID = float(3.63)
block_ashWoodPlankStairsID = float(3.64)
block_ashWoodLogStairsID = float(3.65)
block_strippedAshWoodPlankStairsID = float(3.66)
block_strippedAshWoodLogStairsID = float(3.67)
block_pineWoodPlankStairsID = float(3.68)
block_pineWoodLogStairsID = float(3.69)
block_strippedPineWoodPlankStairsID = float(3.70)
block_strippedPineWoodLogStairsID = float(3.71)
block_palmWoodPlankStairsID = float(3.72)
block_palmWoodLogStairsID = float(3.73)
block_strippedPalmWoodPlankStairsID = float(3.74)
block_strippedPalmWoodLogStairsID = float(3.75)
block_sycamoreWoodPlankStairsID = float(3.76)
block_sycamoreWoodLogStairsID = float(3.77)
block_strippedSycamoreWoodPlankStairsID = float(3.78)
block_strippedSycamoreWoodLogStairsID = float(3.79)
block_acornWoodPlankStairsID = float(3.80)
block_acornWoodLogStairsID = float(3.81)
block_strippedAcornWoodPlankStairsID = float(3.82)
block_strippedAcornWoodLogStairsID = float(3.83)
block_chestnutWoodPlankStairsID = float(3.84)
block_chestnutWoodLogStairsID = float(3.85)
block_strippedChestnutWoodPlankStairsID = float(3.86)
block_strippedChestnutWoodLogStairsID = float(3.87)
block_brimstoneStairsID = float(3.88)
block_iceStairsID = float(3.89)
block_packedIceStairsID = float(3.90)
block_blueIceStairsID = float(3.91)
block_snowStairsID = float(3.92)
block_glowstoneStairsID = float(3.93)
block_plywoodStairsID = float(3.94)
block_TNTStairsID = float(3.95)
block_steelStairsID = float(3.96)
block_tinStairsID = float(3.97)
block_aluminumStairsID = float(3.98)
block_silverStairsID = float(3.99)
block_bronzeStairsID = float(3.100)
block_glassStairsID = float(3.101)
block_blackStainedGlassStairsID = float(3.102)
block_whiteStainedGlassStairsID = float(3.103)
block_rubyStairsID = float(3.104)
''' Ores ''' # Category 5
block_coalOreID = float(4.1)
block_ironOreID = float(4.2)
block_goldOreID = float(4.3)
block_redstoneOreID = float(4.4)
block_emeraldOreID = float(4.5)
block_diamondOreID = float(4.6)
block_lapisLazuliOreID = float(4.7)
block_netherQuartzOreID = float(4.8)
block_bronzeOreID = float(4.9)
block_silverOreID = float(4.10)
block_rubyOreID = float(4.11)
block_sapphireOreID = float(4.12)
block_titaniumOreID = float(4.13)
block_steelOreID = float(4.14)
block_netherriteOreID = float(4.15)
''' Saplings ''' # Category 6
block_oakSaplingID = float(5.1)
block_darkOakTreeSaplingID = float(5.2)
block_acaciaTreeSaplingID = float(5.3)
block_birchTreeSaplingID = float(5.4)
block_spruceTreeSaplingID = float(5.5)
block_jungleTreeSaplingID = float(5.6)
block_cherryTreeSaplingID = float(5.7)
block_locustTreeSaplingID = float(5.8)
block_appleTreeSaplingID = float(5.9)
block_ashTreeSaplingID = float(5.10)
block_chestnutTreeSaplingID = float(5.11)
block_pineTreeSaplingID = float(5.12)
block_palmTreeSaplingID = float(5.13)
block_acornTreeSaplingID = float(5.14)
block_sycamoreTreeSaplingID = float(5.15)
block_mapleTreeSaplingID = float(5.16)
''' Beds ''' # Category 7
block_redBasicBedID = float(6.1)
block_blueBasicBedID = float(6.2)
block_greenBasicBedID = float(6.3)
block_cyanBasicBedID = float(6.4)
block_magentaBasicBedID = float(6.5)
block_whiteBasicBedID = float(6.6)
block_blackBasicBedID = float(6.7)
''' Wood ''' # Category 8
block_oakWoodPlankID = float(7.1)
block_darkOakWoodPlankID = float(7.2)
block_acaciaWoodPlankID = float(7.3)
block_birchWoodPlankID = float(7.4)
block_spruceWoodPlankID = float(7.5)
block_jungleWoodPlankID = float(7.6)
block_cherryWoodPlankID = float(7.7)
block_locustWoodPlankID = float(7.8)
block_appleWoodPlankID = float(7.9)
block_ashWoodPlankID = float(7.10)
block_oakWoodLogID = float(7.11)
block_darkOakWoodLogID = float(7.12)
block_acaciaWoodLogID = float(7.13)
block_birchWoodLogID = float(7.14)
block_spruceWoodLogID = float(7.15)
block_jungleWoodLogID = float(7.16)
block_cherryWoodLogID = float(7.17)
block_locustWoodLogID = float(7.18)
block_appleWoodLogID = float(7.19)
block_ashWoodLogID = float(7.20)
block_OldOakWoodLogID = float(7.21) # Old logs have rings in the middle. There can be a maximum of 8 rings. A ring automatically is created after 365 in-game days worth of time.
block_OldDarkOakWoodLogID = float(7.22)
block_OldAcaciaWoodLogID = float(7.23)
block_OldBirchWoodLogID = float(7.24)
block_OldSpruceWoodLogID = float(7.25)
block_OldJungleWoodLogID = float(7.26)
block_OldCherryWoodLogID = float(7.27)
block_OldLocustWoodLogID = float(7.28)
block_OldAppleWoodLogID = float(7.29)
block_OldAshWoodLogID = float(7.30)
block_strippedoakWoodPlankID = float(7.31)
block_strippeddarkOakWoodPlankID = float(7.32)
block_strippedacaciaWoodPlankID = float(7.33)
block_strippedbirchWoodPlankID = float(7.34)
block_strippedspruceWoodPlankID = float(7.35)
block_strippedjungleWoodPlankID = float(7.36)
block_strippedcherryWoodPlankID = float(7.37)
block_strippedlocustWoodPlankID = float(7.38)
block_strippedappleWoodPlankID = float(7.39)
block_strippedashWoodPlankID = float(7.40)
block_strippedoakWoodLogID = float(7.41)
block_strippeddarkOakWoodLogID = float(7.42)
block_strippedacaciaWoodLogID = float(7.43)
block_strippedbirchWoodLogID = float(7.44)
block_strippedspruceWoodLogID = float(7.45)
block_strippedjungleWoodLogID = float(7.46)
block_strippedcherryWoodLogID = float(7.47)
block_strippedlocustWoodLogID = float(7.48)
block_strippedappleWoodLogID = float(7.49)
block_strippedashWoodLogID = float(7.50)
block_chestNutWoodPlanksID = float(7.51)
block_pineWoodPlanksID = float(7.52)
block_sycamoreWoodPlanksID = float(7.53)
block_acornWoodPlanksID = float(7.54)
block_PalmWoodPlanksID = float(7.55)
block_chestNutWoodLogID = float(7.56)
block_pineWoodLogID = float(7.57)
block_sycamoreWoodLogID = float(7.58)
block_acornWoodLogID = float(7.59)
block_PalmWoodLogID = float(7.60)
block_strippedchestNutWoodPlanksID = float(7.61)
block_strippedpineWoodPlanksID = float(7.62)
block_strippedsycamoreWoodPlanksID = float(7.63)
block_strippedacornWoodPlanksID = float(7.64)
block_strippedPalmWoodPlanksID = float(7.65)
block_strippedchestNutWoodLogID = float(7.66)
block_strippedpineWoodLogID = float(7.67)
block_strippedsycamoreWoodLogID = float(7.68)
block_strippedacornWoodLogID = float(7.69)
block_strippedPalmWoodLogID = float(7.70)
block_OldChestnutWoodLogID = float(7.71) # Old logs have rings in the middle. There can be a maximum of 8 rings. A ring automatically is created after 365 in-game days worth of time.
block_OldPineWoodLogID = float(7.72)
block_OldSycamoreWoodLogID = float(7.73)
block_OldPalmWoodLogID = float(7.74)
block_OldAcornWoodLogID = float(7.75)
block_slimyOakWoodLogID = float(7.76)
block_slimyOakWoodPlanksID = float(7.77)
block_slimyStrippedOakWoodLogID = float(7.78)
block_slimyStrippedOakWoodPlanksID = float(7.79)
block_slimyDarkOakWoodLogID = float(7.76)
block_slimyDarkOakWoodPlanksID = float(7.77)
block_slimyStrippedDarkOakWoodLogID = float(7.78)
block_slimyStrippedDarkOakWoodPlanksID = float(7.79)
block_slimySpruceWoodLogID = float(7.80)
block_slimySpruceWoodPlanksID = float(7.81)
block_slimyStrippedSpruceWoodLogID = float(7.82)
block_slimyStrippedSpruceWoodPlanksID = float(7.83)
block_slimyBirchWoodLogID = float(7.84)
block_slimyBirchWoodPlanksID = float(7.85)
block_slimyStrippedBirchWoodLogID = float(7.86)
block_slimyStrippedBirchWoodPlanksID = float(7.87)
block_slimyJungleWoodLogID = float(7.88)
block_slimyJungleWoodPlanksID = float(7.89)
block_slimyStrippedJungleWoodLogID = float(7.90)
block_slimyStrippedJungleWoodPlanksID = float(7.91)
block_slimyAcaciaWoodLogID = float(7.92)
block_slimyAcaciaWoodPlanksID = float(7.93)
block_slimyStrippedAcaciaWoodLogID = float(7.94)
block_slimyStrippedAcaciaWoodPlanksID = float(7.95)
block_slimyCherryWoodLogID = float(7.96)
block_slimyCherryWoodPlanksID = float(7.97)
block_slimyStrippedCherryWoodLogID = float(7.98)
block_slimyStrippedCherryWoodPlanksID = float(7.99)
block_slimyLocustWoodLogID = float(7.100)
block_slimyLocustWoodPlanksID = float(7.101)
block_slimyStrippedLocustWoodLogID = float(7.102)
block_slimyStrippedLocustWoodPlanksID = float(7.103)
block_slimyPineWoodLogID = float(7.104)
block_slimyPineWoodPlanksID = float(7.105)
block_slimyStrippedPineWoodLogID = float(7.106)
block_slimyStrippedPineWoodPlanksID = float(7.107)
block_slimyPineWoodLogID = float(7.108)
block_slimyPineWoodPlanksID = float(7.109)
block_slimyStrippedPineWoodLogID = float(7.110)
block_slimyStrippedPineWoodPlanksID = float(7.111)
block_slimyAppleWoodLogID = float(7.112)
block_slimyAppleWoodPlanksID = float(7.113)
block_slimyStrippedAppleWoodLogID = float(7.114)
block_slimyStrippedAppleWoodPlanksID = float(7.115)
block_slimyAshWoodLogID = float(7.116)
block_slimyAshWoodPlanksID = float(7.117)
block_slimyStrippedAshWoodLogID = float(7.118)
block_slimyStrippedAshWoodPlanksID = float(7.119)
block_slimyAcornWoodLogID = float(7.120)
block_slimyAcornWoodPlanksID = float(7.121)
block_slimyStrippedAcornWoodLogID = float(7.122)
block_slimyStrippedAcornWoodPlanksID = float(7.123)
block_slimySycamoreWoodLogID = float(7.124)
block_slimySycamoreWoodPlanksID = float(7.125)
block_slimyStrippedSycamoreWoodLogID = float(7.126)
block_slimyStrippedSycamoreWoodPlanksID = float(7.127)
block_slimySycamoreWoodLogID = float(7.128)
block_slimySycamoreWoodPlanksID = float(7.129)
block_slimyStrippedSycamoreWoodLogID = float(7.130)
block_slimyStrippedSycamoreWoodPlanksID = float(7.131)
block_petrifiedOakWoodLogID = float(7.132)
block_petrifiedOakWoodPlanksID = float(7.133)
block_petrifiedStrippedOakWoodPlanksID = float(7.134)
block_petrifiedStrippedOakWoodLogID = float(7.135)
block_burntOakWoodLogID = float(7.136)
block_burntOakWoodPlanksID = float(7.137)
block_burntStrippedOakWoodLogID = float(7.138)
block_burntStrippedOakWoodPlanksID = float(7.139)
block_petrifiedDarkOakWoodLogID = float(7.140)
block_petrifiedDarkOakWoodPlanksID = float(7.141)
block_petrifiedStrippedDarkOakWoodPlanksID = float(7.142)
block_petrifiedStrippedDarkOakWoodLogID = float(7.143)
block_burntDarkOakWoodLogID = float(7.144)
block_burntDarkOakWoodPlanksID = float(7.145)
block_burntStrippedDarkOakWoodLogID = float(7.146)
block_burntStrippedDarkOakWoodPlanksID = float(7.147)
block_petrifiedSpruceWoodLogID = float(7.148)
block_petrifiedSpruceWoodPlanksID = float(7.149)
block_petrifiedStrippedSpruceWoodPlanksID = float(7.150)
block_petrifiedStrippedSpruceWoodLogID = float(7.151)
block_burntSpruceWoodLogID = float(7.152)
block_burntSpruceWoodPlanksID = float(7.153)
block_burntStrippedSpruceWoodLogID = float(7.154)
block_burntStrippedSpruceWoodPlanksID = float(7.155)
block_petrifiedBirchWoodLogID = float(7.156)
block_petrifiedBirchWoodPlanksID = float(7.157)
block_petrifiedStrippedBirchWoodPlanksID = float(7.158)
block_petrifiedStrippedBirchWoodLogID = float(7.159)
block_burntBirchWoodLogID = float(7.160)
block_burntBirchWoodPlanksID = float(7.161)
block_burntStrippedBirchWoodLogID = float(7.162)
block_burntStrippedBirchWoodPlanksID = float(7.163)
block_petrifiedAcaciaWoodLogID = float(7.164)
block_petrifiedAcaciaWoodPlanksID = float(7.165)
block_petrifiedStrippedAcaciaWoodPlanksID = float(7.166)
block_petrifiedStrippedAcaciaWoodLogID = float(7.167)
block_burntAcaciaWoodLogID = float(7.168)
block_burntAcaciaWoodPlanksID = float(7.169)
block_burntStrippedAcaciaWoodLogID = float(7.170)
block_burntStrippedAcaciaWoodPlanksID = float(7.171)
block_petrifiedJungleWoodLogID = float(7.172)
block_petrifiedJungleWoodPlanksID = float(7.173)
block_petrifiedStrippedJungleWoodPlanksID = float(7.174)
block_petrifiedStrippedJungleWoodLogID = float(7.175)
block_burntJungleWoodLogID = float(7.176)
block_burntJungleWoodPlanksID = float(7.177)
block_burntStrippedJungleWoodLogID = float(7.178)
block_burntStrippedJungleWoodPlanksID = float(7.179)
block_petrifiedPineWoodLogID = float(7.180)
block_petrifiedPineWoodPlanksID = float(7.181)
block_petrifiedStrippedPineWoodPlanksID = float(7.182)
block_petrifiedStrippedPineWoodLogID = float(7.183)
block_burntPineWoodLogID = float(7.184)
block_burntPineWoodPlanksID = float(7.185)
block_burntStrippedPineWoodLogID = float(7.186)
block_burntStrippedPineWoodPlanksID = float(7.187)
block_petrifiedPalmWoodLogID = float(7.188)
block_petrifiedPalmWoodPlanksID = float(7.189)
block_petrifiedStrippedPalmWoodPlanksID = float(7.190)
block_petrifiedStrippedPalmWoodLogID = float(7.191)
block_burntPalmWoodLogID = float(7.192)
block_burntPalmWoodPlanksID = float(7.193)
block_burntStrippedPalmWoodLogID = float(7.194)
block_burntStrippedPalmWoodPlanksID = float(7.195)
block_petrifiedSycamoreWoodLogID = float(7.196)
block_petrifiedSycamoreWoodPlanksID = float(7.197)
block_petrifiedStrippedSycamoreWoodPlanksID = float(7.198)
block_petrifiedStrippedSycamoreWoodLogID = float(7.199)
block_burntSycamoreWoodLogID = float(7.200)
block_burntSycamoreWoodPlanksID = float(7.201)
block_burntStrippedSycamoreWoodLogID = float(7.202)
block_burntStrippedSycamoreWoodPlanksID = float(7.203)
block_petrifiedChestWoodLogID = float(7.204)
block_petrifiedChestWoodPlanksID = float(7.205)
block_petrifiedStrippedChestWoodPlanksID = float(7.206)
block_petrifiedStrippedChestWoodLogID = float(7.207)
block_burntChestWoodLogID = float(7.208)
block_burntChestWoodPlanksID = float(7.209)
block_burntStrippedChestWoodLogID = float(7.210)
block_burntStrippedChestWoodPlanksID = float(7.211)
block_petrifiedAppleWoodLogID = float(7.212)
block_petrifiedAppleWoodPlanksID = float(7.213)
block_petrifiedStrippedAppleWoodPlanksID = float(7.214)
block_petrifiedStrippedAppleWoodLogID = float(7.215)
block_burntAppleWoodLogID = float(7.216)
block_burntAppleWoodPlanksID = float(7.217)
block_burntStrippedAppleWoodLogID = float(7.218)
block_burntStrippedAppleWoodPlanksID = float(7.219)
block_petrifiedAshWoodLogID = float(7.220)
block_petrifiedAshWoodPlanksID = float(7.221)
block_petrifiedStrippedAshWoodPlanksID = float(7.222)
block_petrifiedStrippedAshWoodLogID = float(7.223)
block_burntAshWoodLogID = float(7.224)
block_burntAshWoodPlanksID = float(7.225)
block_burntStrippedAshWoodLogID = float(7.226)
block_burntStrippedAshWoodPlanksID = float(7.227)
block_petrifiedLocustWoodLogID = float(7.228)
block_petrifiedLocustWoodPlanksID = float(7.229)
block_petrifiedStrippedLocustWoodPlanksID = float(7.230)
block_petrifiedStrippedLocustWoodLogID = float(7.231)
block_burntLocustWoodLogID = float(7.232)
block_burntLocustWoodPlanksID = float(7.233)
block_burntStrippedLocustWoodLogID = float(7.234)
block_burntStrippedLocustWoodPlanksID = float(7.235)
block_icyOakWoodLogID = float(7.236)
block_icyOakWoodPlanksID = float(7.237)
block_icyStrippedOakWoodLogID = float(7.238)
block_icyStrippedOakWoodPlanksID = float(7.239)
''' Nether ''' # Category 9
block_magmaBlockID = float(8.1)
block_netherrackID = float(8.2)
block_soulSandID = float(8.3)
block_glowStoneID = float(8.4)
block_netherBrickBlockID = float(8.5)
block_redNetherBrickBlockID = float(8.6)
block_netherriteBlockID = float(8.7)
''' Glass ''' # Category 10
block_glassID = float(9.1)
block_glassPaneID = float(9.2)
block_whiteStainedGlassID = float(9.3)
block_whiteStainedGlassPaneID = float(9.4)
''' Appliances ''' # Category 11
block_furnaceID = float(10.1)
block_enderChestID = float(10.2)
block_OakWoodCraftingTableID = float(10.3)
block_ironCauldronID = float(10.4)
block_ironSpawnerCageID = float(10.5)
block_jukeBoxID = float(10.6)
block_oakWoodNoteblockID = float(10.7)
block_darkOakWoodNoteblockID = float(10.8)
block_acaciaWoodNoteblockID = float(10.9)
block_birchWoodNoteBlockID = float(10.10)
block_spruceWoodNoteBlockID = float(10.11)
block_jungleWoodNoteBlockID = float(10.12)
block_cherryWoodNoteBlockID = float(10.13)
block_locustWoodNoteBlockID = float(10.14)
block_appleWoodNoteBlockID = float(10.15)
block_ashWoodNoteBlockID = float(10.16)
block_DarkOakWoodCraftingTableID = float(10.17)
block_acaciaWoodCraftingTableID = float(10.18)
block_birchWoodCraftingTableID = float(10.19)
block_spruceWoodCraftingTableID = float(10.20)
block_jungleWoodCraftingTableID = float(10.21)
block_cherryWoodCraftingTableID = float(10.22)
block_locustWoodCraftingTableID = float(10.23)
block_appleWoodCraftingTableID = float(10.24)
block_ashWoodCraftingTableID = float(10.25)
block_chestID = float(10.26)
block_barrelID = float(10.27)
block_ironAnvilID = float(10.28)
block_slightlyDamagedIronAnvilID = float(10.29)
block_heavilyDamagedIronAnvilID = float(10.30)
block_steelAnvilID = float(10.31)
block_slightlyDamagedsteelAnvilID = float(10.32)
block_heavilyDamagedsteelAnvilID = float(10.33)
block_diamondAnvilID = float(10.34)
block_slightlyDamagedDiamondAnvilID = float(10.35)
block_heavilyDamagedDiamondAnvilID = float(10.36)
block_blastFurnaceID = float(10.37)
block_enderDispenserID = float(10.38)
block_dispenserID = float(10.39)
block_bookshelfID = float(10.40)
block_lecternID = float(10.41)
block_loomID = float(10.42)
block_netherReactorCoreID = float(10.43)
block_airConditionerBlockID = float(10.44)
block_jackintheboxBlockID = float(10.45)
block_goldAnvilID = float(10.46)
block_slightlyDamagedGoldAnvilID = float(10.47)
block_heavilyDamagedGoldAnvilID = float(10.48)
block_redstoneAnvilID = float(10.49)
block_slightlyDamagedRedstoneAnvilID = float(10.50)
block_heavilyDamagedRedstoneAnvilID = float(10.51)
block_caveStoneAnvilID = float(10.52)
block_slightlyDamagedCaveStoneAnvilID = float(10.53)
block_heavilyDamagedCaveStoneAnvilID = float(10.54)
block_tinAnvilID = float(10.55)
block_slightlyDamagedTinAnvilID = float(10.56)
block_heavilyDamagedTinAnvilID = float(10.57)
block_silverAnvilID = float(10.55)
block_slightlyDamagedSilverAnvilID = float(10.56)
block_heavilyDamagedSilverAnvilID = float(10.57)
block_bronzeAnvilID = float(10.58)
block_slightlyDamagedBronzeAnvilID = float(10.59)
block_heavilyDamagedBronzeAnvilID = float(10.60)
block_rubyAnvilID = float(10.61)
block_slightlyDamagedRubyAnvilID = float(10.62)
block_heavilyDamagedRubyAnvilID = float(10.63)
block_sapphireAnvilID = float(10.64)
block_slightlyDamagedSapphireAnvilID = float(10.65)
block_heavilyDamagedSapphireAnvilID = float(10.66)
block_cartographyTableID = float(10.67)
block_ironToiletID = float(10.68)
block_steelToiletID = float(10.69)
block_tinToiletID = float(10.70)
block_aluminumToiletID = float(10.71)
block_silverToiletID = float(10.72)
block_bronzeToiletID = float(10.73)
block_titaniumToiletID = float(10.74)
block_goldToiletID = float(10.75)
block_diamondToiletID = float(10.76)
block_lapizLazuliToiletID = float(10.77)
block_emeraldToiletID = float(10.78)
block_obsidianToiletID = float(10.79)
block_cobblestoneToiletID = float(10.80)
block_ironSinkID = float(10.81)
block_steelSinkID = float(10.82)
block_tinSinkID = float(10.83)
block_aluminumSinkID = float(10.84)
block_silverSinkID = float(10.85)
block_bronzeSinkID = float(10.86)
block_titaniumSinkID = float(10.87)
block_goldSinkID = float(10.88)
block_diamondSinkID = float(10.89)
block_lapizLazuliSinkID = float(10.90)
block_emeraldSinkID = float(10.91)
block_obsidianSinkID = float(10.92)
block_cobblestoneSinkID = float(10.93)
block_itemMagnetID = float(10.94) # Sucks items into it within a set radius of 5 to 50 blocks
block_birdMagnetID = float(10.95) # Sucks birds into it within a set radius of 5 to 50 blocks
block_mobMagnetID = float(10.96)
block_smokerID = float(10.97)
block_meatSmokerID = float(10.98)
block_CartographyTableID = float(10.99)
block_workbenchID = float(10.100)
block_smithingTableID = float(10.101)
block_toasterID = float(10.102)
block_fletchingTableID = float(10.103)
''' Doors ''' # Category 12
block_ironDoorID = float(11.1)
block_steelDoorID = float(11.2)
block_oakWoodDoorID = float(11.3)
block_darkOakWoodDoorID = float(11.4)
block_acaciaWoodDoorID = float(11.5)
block_birchWoodDoorID = float(11.6)
block_spruceWoodDoorID = float(11.7)
block_jungleWoodDoorID = float(11.8)
block_cherryWoodDoorID = float(11.9)
block_locustWoodDoorID = float(11.10)
block_appleWoodDoorID = float(11.11)
block_ashWoodDoorID = float(11.12)
block_obsidianDoorID = float(11.13)
block_caveStoneDoorID = float(11.14)
block_goldDoorID = float(11.15)
block_diamondDoorID = float(11.16)
block_aluminumDoorID = float(11.17)
block_tinDoorID = float(11.18)
block_diamondDoorID = float(11.19)
block_emeraldDoorID = float(11.20)
block_ironTrapDoorID = float(11.21)
block_steeTraplDoorID = float(11.22)
block_oakWoodTrapDoorID = float(11.23)
block_darkOakWoodTrapDoorID = float(11.24)
block_acaciaWoodTrapDoorID = float(11.25)
block_birchWoodTrapDoorID = float(11.26)
block_spruceWoodTrapDoorID = float(11.27)
block_jungleWoodTrapDoorID = float(11.28)
block_cherryWoodTrapDoorID = float(11.29)
block_locustWoodTrapDoorID = float(11.30)
block_appleWoodTrapDoorID = float(11.31)
block_ashWoodTrapDoorID = float(11.32)
block_obsidianTrapDoorID = float(11.33)
block_caveStoneTrapDoorID = float(11.34)
block_goldTrapDoorID = float(11.35)
block_diamondTrapDoorID = float(11.36)
block_aluminumTrapDoorID = float(11.37)
block_tinTrapDoorID = float(11.38)
block_diamondTrapDoorID = float(11.39)
block_emeraldTrapDoorID = float(11.40)
block_blueWoolDoorID = float(11.41)
block_cyanWoolDoorID = float(11.42)
block_turquioseWoolDoorID = float(11.43)
block_darkBlueWoolDoorID = float(11.44)
block_greenWoolDoorID = float(11.45)
block_magentaWoolDoorID = float(11.46)
block_brownWoolDoorID = float(11.47)
block_pinkWoolDoorID = float(11.48)
block_whiteWoolDoorID = float(11.49)
block_blackWoolDoorID = float(11.50)
block_orangeWoolDoorID = float(11.51)
block_yellowWoolDoorID = float(11.52)
block_greyWoolDoorID = float(11.53)
block_darkGreyWoolDoorID = float(11.54)
block_limeWoolDoorID = float(11.55)
block_purpleWoolDoorID = float(11.56)
block_blueWoolTrapDoorID = float(11.57)
block_cyanWoolTrapDoorID = float(11.58)
block_turquioseWoolTrapDoorID = float(11.59)
block_darkBlueWoolTrapDoorID = float(11.60)
block_greenWoolTrapDoorID = float(11.61)
block_magentaWoolTrapDoorID = float(11.62)
block_brownWoolTrapDoorID = float(11.63)
block_pinkWoolTrapDoorID = float(11.64)
block_whiteWoolTrapDoorID = float(11.65)
block_blackWoolTrapDoorID = float(11.66)
block_orangeWoolTrapDoorID = float(11.67)
block_yellowWoolTrapDoorID = float(11.68)
block_greyWoolTrapDoorID = float(11.69)
block_darkGreyWoolTrapDoorID = float(11.70)
block_limeWoolTrapDoorID = float(11.71)
block_purpleWoolTrapDoorID = float(11.72)
''' End ''' # Category 13
block_purpleEndCrystalID = float(12.1)
block_endStoneID = float(12.2)
block_enderDragonEggID = float(12.3)
block_endPortalID = float(12.4)
block_purpurBlockID = float(12.5)
block_purpurPillarBlockID = float(12.6)
block_endRodID = float(12.7)
''' Clay ''' # Category 14
block_clayID = float(13.1)
block_whiteClayID = float(13.2)
block_blackClayID = float(13.3)
block_limeClayID = float(13.4)
block_greenClayID = float(13.5)
block_cyanClayID = float(13.6)
block_turquioseClayID = float(13.7)
block_yellowClayID = float(13.8)
block_lightBlueClayID = float(13.9)
block_darkBlueClayID = float(13.10)
block_lightGreyClayID = float(13.11)
block_darkGreyClayID = float(13.12)
block_redClayID = float(13.13)
block_pinkClayID = float(13.14)
block_purpleClayID = float(13.15)
block_brownClayID = float(13.16)
block_orangeClayID = float(13.17)
block_hardenedwhiteClayID = float(13.18)
block_hardenedblackClayID = float(13.19)
block_hardenedlimeClayID = float(13.20)
block_hardenedgreenClayID = float(13.21)
block_hardenedcyanClayID = float(13.22)
block_hardenedturquioseClayID = float(13.23)
block_hardenedyellowClayID = float(13.24)
block_hardenedlightBlueClayID = float(13.25)
block_hardeneddarkBlueClayID = float(13.26)
block_hardenedlightGreyClayID = float(13.27)
block_hardeneddarkGreyClayID = float(13.28)
block_hardenedredClayID = float(13.29)
block_hardenedpinkClayID = float(13.30)
block_hardenedpurpleClayID = float(13.31)
block_hardenedbrownClayID = float(13.32)
block_hardenedorangeClayID = float(13.33)
''' Terracotta ''' # Category 15
block_whiteArrowTerracottaID = float(14.1)
''' Concrete ''' # Category 16
block_whiteConcretePowderID = float(15.1)
block_whiteConcreteID = float(15.2)
block_blackConcretePowderID = float(15.3)
block_blackConcreteID = float(15.4)
block_lightGreyConcretePowderID = float(15.5)
block_lightGreyConcreteID = float(15.6)
block_darkGreyConcretePowderID = float(15.7)
block_darkGreyConcreteID = float(15.8)
''' Carpet ''' # Category 17
block_whiteCarpetID = float(16.1)
''' Wool ''' # Category 18
block_whiteWoolID = float(17.1)
block_blackWoolID = float(17.2)
block_lightGreyWoolID = float(17.3)
block_darkGreyWoolID = float(17.4)
block_yellowWoolID = float(17.5)
block_redWoolID = float(17.6)
block_cyanWoolID = float(17.7)
block_turquioseWoolID = float(17.8)
block_blueWoolID = float(17.9)
block_darkBlueWoolID = float(17.10)
block_purpleWoolID = float(17.11)
block_brownWoolID = float(17.12)
block_pinkWoolID = float(17.13)
block_greenWoolID = float(17.14)
block_limeWoolID = float(17.15)
block_orangeWoolID = float(17.16)
block_magentaWoolID = float(17.17)
''' Redstone ''' # Category 19
block_redstoneBlockID = float(18.1)
block_redstoneTorchID = float(18.2)
block_goldenPressurePlateID = float(18.3)
block_CaveStoneLeverID = float(18.4)
block_cobbleStoneButtonID = float(18.5)
block_caveStoneButtonID = float(18.6)
block_pistonID = float(18.7)
block_stickyPistonID = float(18.8)
block_oakWoodPressurePlateID = float(18.9)
block_darkOakWoodPressurePlateID = float(18.10)
block_acaciaWoodPressurePlateID = float(18.11)
block_birchWoodPressurePlateID = float(18.12)
block_spruceWoodPressurePlateID = float(18.13)
block_jungleWoodPressurePlateID = float(18.14)
block_cherryWoodPressurePlateID = float(18.15)
block_locustWoodPressurePlateID = float(18.16)
block_appleWoodPressurePlateID = float(18.17)
block_ashWoodPressurePlateID = float(18.18)
block_pythonCommandBlockID = float(18.19)
block_NormalcommandBlockID = float(18.20)
block_redstoneRepeaterID = float(18.21)
block_redstoneComparterID = float(18.22)
block_daylightSensorID = float(18.23)
block_hopperID = float(18.24)
block_dropperID = float(18.25)
block_ironCashRegisterID = float(18.26)
block_redstoneLampBlockID = float(18.27)
block_redstoneID = float(18.28)
block_tripwireHookID = float(18.29)
block_smokeMachineID = float(18.30)
block_placedStringID = float(18.31)
block_doublePistonID = float(18.32)
block_doubleStickyPistonID = float(18.33)
block_triplePistonID = float(18.34)
block_tripleStickyPistonID = float(18.35)
block_quadruplePistonID = float(18.36)
block_quadrupleStickyPistonID = float(18.37)
block_quintuplePistonID = float(18.38)
block_quintupleStickyPistonID = float(18.39)
block_upsideDownDaylightSensorID = float(18.40)
block_wallMountDaylightsensorID = float(18.41)
block_curvedRedstoneRepeaterID = float(18.42)
''' On the wall ''' # Category 20
block_painting1ID = float(19.1) # OG MC painting A
block_torchID = float(19.2)
block_steveHeadID = float(19.3)
block_alexHeadID = float(19.4)
block_herobrineHeadID = float(19.5)
block_notchHeadID = float(19.6)
block_skeletonSkullID = float(19.7)
block_witherSkeletonSkullID = float(19.8)
block_creeperHeadID = float(19.9)
block_enderDragonHeadID = float(19.10)
block_endermanHeadID = float(19.11)
block_zombieHeadID = float(19.12)
block_villagerZombieHeadID = float(19.13)
block_chickenHeadID = float(19.14)
block_pigHeadID = float(19.15)
block_villagerHeadID = float(19.16)
block_itemFrameID = float(19.17)
block_burntOutRedStoneTorchID = float(19.18)
block_burntOutTorchID = float(19.19)
block_painting2ID = float(19.20) # OG MC painting B
block_painting3ID = float(19.21) # OG MC painting C
block_painting4ID = float(19.22) # OG MC painting D
block_painting5ID = float(19.23) # OG MC painting E
block_painting6ID = float(19.24) # OG MC painting F
block_painting7ID = float(19.25) # OG MC painting G
block_painting8ID = float(19.26) # OG MC painting H
block_painting9ID = float(19.27) # OG MC painting I
block_painting10ID = float(19.28) # OG MC painting J
block_painting11ID = float(19.29) # OG MC painting K
block_painting12ID = float(19.30) # OG MC painting L
block_painting13ID = float(19.31) # OG MC painting M
block_painting14ID = float(19.32) # OG MC painting N
block_painting15ID = float(19.33) # OG MC painting O
block_painting16ID = float(19.34) # OG MC painting P
block_painting17ID = float(19.35) # OG MC painting Q
block_painting18ID = float(19.36) # OG MC painting R
block_painting19ID = float(19.37) # OG MC painting S
block_painting20ID = float(19.38) # OG MC painting T
block_painting21ID = float(19.39) # OG MC painting U
block_painting22ID = float(19.40) # OG MC painting V
block_painting23ID = float(19.41) # OG MC painting W
block_painting24ID = float(19.42) # OG MC painting X
block_painting25ID = float(19.43) # OG MC painting Y
block_painting26ID = float(19.44) # OG MC painting Z
block_painting27ID = float(19.45) # A painting of a troll face, 1x1
block_painting28ID = float(19.46) # A painting of a troll face, 2x2
block_painting29ID = float(19.47) # A painting of the python logo, 1x1
block_painting30ID = float(19.48) # A painting of the old Python logo, 1x2
block_painting31ID = float(19.49) # A painting of the python logo, 2x2
block_painting32ID = float(19.50) # A painting of the old Python logo, 2x3
block_painting33ID = float(19.51) # A painting of the mona lisa, 2x2
block_painting34ID = float(19.52) # A painting of starry night, 2x2
block_painting35ID = float(19.53) # A painting of the scream, 2x2
block_painting36ID = float(19.54) # A painting of the old Mozilla Firefox icon, 1x1
block_painting37ID = float(19.55) # A painting of Tux, 1x1
block_painting38ID = float(19.56) # A painting of Tux, 2x2
block_painting39ID = float(19.57) # A painting of Tux, 3x3
block_painting40ID = float(19.58) # A painting of Tux, 4x4
block_painting41ID = float(19.59) # A painting of Tux, 5x5
block_painting42ID = float(19.60) # A painting of a python terminal hello world script light mode, 1x1
block_painting43ID = float(19.61) # A painting of a python terminal hello world script dark mode, 1x1
block_painting44ID = float(19.62) # A painting of a blue screen of death (1995 version) 1x1)
block_painting45ID = float(19.63) # A painting of a blue screen of death (2000 version) 1x1)
block_painting46ID = float(19.64) # A painting of a creeper in a TNT biome (1x1)
block_painting47ID = float(19.65) # A painting of a math equation on a blackboard (2+2=4) (1x1)
block_painting48ID = float(19.66) # A painting of the white house (3x2)
block_painting49ID = float(19.67) # A painting of George Washington (1x2)
block_painting50ID = float(19.68) # A painting of the leaning tower of pisa (1x3)
block_painting51ID = float(19.69) # A painting of the Taj Mahal (3x3)
block_painting52ID = float(19.70) # A painting of the pyramid of Giza (5x5)
block_painting53ID = float(19.71) # A painting of stonehenge (3x3)
block_painting54ID = float(19.72) # A painting of a sunset (1x1)
block_painting55ID = float(19.73) # A painting of the Eiffel Tower (2x4)
block_painting56ID = float(19.74) # A painting of the grand canyon (3x3)
block_painting57ID = float(19.75) # A painting of a Wi-Fi signal (1x1)
block_painting58ID = float(19.76) # A painting of the great wall of china (3x3)3
block_chargedEnderDragonHeadID = float(19.77) # An enderdragon head that when you get close to it, it will spray out purple fire.
''' Frozen ''' # Category 21
block_snowBlockID = float(20.1)
block_snowID = float(20.2)
block_iceBlockID = float(20.3)
block_packedIceBlockID = float(20.4)
block_blueIceBlockID = float(20.5)
block_greenIceBlockID = float(20.6)
block_crackedIceBlockID = float(20.7)
block_crackedPackedIceBlockID = float(20.8)
block_crackedBlueIceBlockID = float(20.9)
block_crackedGreenIceBlockID = float(20.10)
block_packedSnowBlockID = float(20.11)
''' Fence-like ''' # Category 22
block_ironBarsID = float(21.1)
block_steelBarsID = float(21.2)
block_diamondBarsID = float(21.3)
block_oakWoodPlankFenceID = float(21.4)
block_oakWoodPlankWallID = float(21.5)
block_darkOakWoodPlankFenceID = float(21.6)
block_darkOakWoodPlankWallID = float(21.7)
block_acaciaWoodPlankFenceID = float(21.8)
block_acaciaWoodPlankWallID = float(21.9)
block_birchWoodPlankFenceID = float(21.10)
block_spruceWoodPlankFenceID = float(21.11)
block_jungleWoodPlankFenceID = float(21.12)
block_cherryWoodPlankFenceID = float(21.13)
block_locustWoodPlankFenceID = float(21.14)
block_appleWoodPlankFenceID = float(21.15)
block_ashWoodPlankFenceID = float(21.16)
block_birchWoodPlankWallID = float(21.17)
block_spruceWoodPlankWallID = float(21.18)
block_jungleWoodPlankWallID = float(21.19)
block_cherryWoodPlankWallID = float(21.20)
block_locustWoodPlankWallID = float(21.21)
block_appleWoodPlankWallID = float(21.22)
block_ashWoodPlankWallID = float(21.23)
block_pineWoodPlankWallID = float(21.24)
block_pineWoodPlankFenceID = float(21.25)
block_acornWoodPlankFenceID = float(21.26)
block_chestnutWoodPlankFenceID = float(21.27)
block_sycamoreWoodPlankFenceID = float(21.28)
block_acornWoodPlankWallID = float(21.29)
block_chestnutWoodPlankWallID = float(21.30)
block_sycamoreWoodPlankWallID = float(21.31)
block_palmWoodPlankFenceID = float(21.32)
block_palmWoodPlankWallID = float(21.33)
block_strippedoakWoodPlankFenceID = float(21.34)
block_strippedoakWoodPlankWallID = float(21.35)
block_strippeddarkOakWoodPlankFenceID = float(21.36)
block_strippeddarkOakWoodPlankWallID = float(21.37)
block_strippedacaciaWoodPlankFenceID = float(21.38)
block_strippedacaciaWoodPlankWallID = float(21.39)
block_strippedbirchWoodPlankFenceID = float(21.40)
block_strippedspruceWoodPlankFenceID = float(21.41)
block_strippedjungleWoodPlankFenceID = float(21.42)
block_strippedcherryWoodPlankFenceID = float(21.43)
block_strippedlocustWoodPlankFenceID = float(21.44)
block_strippedappleWoodPlankFenceID = float(21.45)
block_strippedashWoodPlankFenceID = float(21.46)
block_strippedbirchWoodPlankWallID = float(21.47)
block_strippedspruceWoodPlankWallID = float(21.48)
block_strippedjungleWoodPlankWallID = float(21.49)
block_strippedcherryWoodPlankWallID = float(21.50)
block_strippedlocustWoodPlankWallID = float(21.51)
block_strippedappleWoodPlankWallID = float(21.52)
block_strippedashWoodPlankWallID = float(21.53)
block_strippedpineWoodPlankWallID = float(21.54)
block_strippedpineWoodPlankFenceID = float(21.55)
block_strippedacornWoodPlankFenceID = float(21.56)
block_strippedchestnutWoodPlankFenceID = float(21.57)
block_strippedsycamoreWoodPlankFenceID = float(21.58)
block_strippedacornWoodPlankWallID = float(21.59)
block_strippedchestnutWoodPlankWallID = float(21.60)
block_strippedsycamoreWoodPlankWallID = float(21.61)
block_strippedpalmWoodPlankFenceID = float(21.62)
block_strippedpalmWoodPlankWallID = float(21.63)
block_oakWoodLogFenceID = float(21.64)
block_oakWoodLogWallID = float(21.65)
block_darkOakWoodLogFenceID = float(21.66)
block_darkOakWoodLogWallID = float(21.67)
block_acaciaWoodLogFenceID = float(21.68)
block_acaciaWoodLogWallID = float(21.69)
block_birchWoodLogFenceID = float(21.70)
block_spruceWoodLogFenceID = float(21.71)
block_jungleWoodLogFenceID = float(21.72)
block_cherryWoodLogFenceID = float(21.73)
block_locustWoodLogFenceID = float(21.74)
block_appleWoodLogFenceID = float(21.75)
block_ashWoodLogFenceID = float(21.76)
block_birchWoodLogWallID = float(21.77)
block_spruceWoodLogWallID = float(21.78)
block_jungleWoodLogWallID = float(21.79)
block_cherryWoodLogWallID = float(21.80)
block_locustWoodLogWallID = float(21.81)
block_appleWoodLogWallID = float(21.82)
block_ashWoodLogWallID = float(21.83)
block_pineWoodLogWallID = float(21.84)
block_pineWoodLogFenceID = float(21.85)
block_acornWoodLogFenceID = float(21.86)
block_chestnutWoodLogFenceID = float(21.87)
block_sycamoreWoodLogFenceID = float(21.88)
block_acornWoodLogWallID = float(21.89)
block_chestnutWoodLogWallID = float(21.90)
block_sycamoreWoodLogWallID = float(21.91)
block_palmWoodLogFenceID = float(21.92)
block_palmWoodLogWallID = float(21.93)
block_strippedoakWoodLogFenceID = float(21.94)
block_strippedoakWoodLogWallID = float(21.95)
block_strippeddarkOakWoodLogFenceID = float(21.96)
block_strippeddarkOakWoodLogWallID = float(21.97)
block_strippedacaciaWoodLogFenceID = float(21.98)
block_strippedacaciaWoodLogWallID = float(21.99)
block_strippedbirchWoodLogFenceID = float(21.100)
block_strippedspruceWoodLogFenceID = float(21.101)
block_strippedjungleWoodLogFenceID = float(21.102)
block_strippedcherryWoodLogFenceID = float(21.103)
block_strippedlocustWoodLogFenceID = float(21.104)
block_strippedappleWoodLogFenceID = float(21.105)
block_strippedashWoodLogFenceID = float(21.106)
block_strippedbirchWoodLogWallID = float(21.107)
block_strippedspruceWoodLogWallID = float(21.108)
block_strippedjungleWoodLogWallID = float(21.109)
block_strippedcherryWoodLogWallID = float(21.110)
block_strippedlocustWoodLogWallID = float(21.111)
block_strippedappleWoodLogWallID = float(21.112)
block_strippedashWoodLogWallID = float(21.113)
block_strippedpineWoodLogWallID = float(21.114)
block_strippedpineWoodLogFenceID = float(21.115)
block_strippedacornWoodLogFenceID = float(21.116)
block_strippedchestnutWoodLogFenceID = float(21.117)
block_strippedsycamoreWoodLogFenceID = float(21.118)
block_strippedacornWoodLogWallID = float(21.119)
block_strippedchestnutWoodLogWallID = float(21.120)
block_strippedsycamoreWoodLogWallID = float(21.121)
block_strippedpalmWoodLogFenceID = float(21.122)
block_strippedpalmWoodLogWallID = float(21.123)
block_ironFenceID = float(21.124)
block_ironWallID = float(21.125)
block_steelFenceID = float(21.126)
block_steelWallID = float(21.127)
blcok_tinFenceID = float(21.128)
block_tinWallID = float(21.129)
block_aluminumFenceID = float(21.130)
block_aluminumWallID = float(21.131)
block_silverFenceID = float(21.132)
block_silverWallID = float(21.133)
block_bronzeFenceID = float(21.134)
block_bronzeWallID = float(21.135)
block_rubyFenceID = float(21.136)
block_rubyWallID = float(21.137)
block_sapphireFenceID = float(21.138)
block_sapphireWallID = float(21.139)
block_obsidianFenceID = float(21.140)
block_obsidianWallID = float(21.141)
block_netherBrickFenceID = float(21.142)
block_netherBrickWallFenceID = float(21.143)
block_redNetherBrickFenceID = float(21.144)
block_redNetherBrickWallFenceID = float(21.145)
block_netherrackFenceID = float(21.146)
block_netherrackWallID = float(21.147)
block_dirtFenceID = float(21.148)
block_dirtWallID = float(21.149)
block_cobblestoneFenceID = float(21.150)
block_cobblestoneWallID = float(21.151)
block_mossyCobblestoneFenceID = float(21.152)
block_mossyCobblestoneWallID = float(21.153)
block_infestedCobblestoneFenceID = float(21.154)
block_infestedCobblestoneWallID = float(21.155)
block_infestedMossyCobblestoneFenceID = float(21.156)
block_infestedMossyCobblestoneWallID = float(21.157)
block_yellowSandstoneFenceID = float(21.158)
block_yellowSandstoneWallID = float(21.159)
block_redSandstoneFenceID = float(21.160)
block_redSandstoneWallID = float(21.161)
block_iceFenceID = float(21.162)
block_iceWallID = float(21.163)
block_packedIceFenceID = float(21.164)
block_packedIceWallID = float(21.165)
block_blueIceFenceID = float(21.166)
block_blueIceWallID = float(21.167)
block_snowFenceID = float(21.168)
block_snowWallID = float(21.169)
block_smoothStoneFenceID = float(21.170)
block_smoothStoneWallID = float(21.171)
block_caveStoneFenceID = float(21.172)
block_caveStoneWallID = float(21.173)
block_caveStoneFenceGateID = float(21.174)
block_ironFenceGateID = float(21.175)
block_tinFenceGateID = float(21.176)
block_aluminumFenceGateID = float(21.177)
block_rubyFenceGateID = float(21.178)
block_sapphireFenceGateID = float(21.179)
block_goldFenceGateID = float(21.180)
block_diamondFenceGateID = float(21.181)
block_emeraldFenceGateID = float(21.182)
block_redstoneFenceGateID = float(21.183)
block_lapisLazuliFenceGateID = float(21.184)
block_obsidianFenceGateID = float(21.185)
block_steelFenceGateID = float(21.186)
block_silverFenceGateID = float(21.187)
block_bronzeFenceGateID = float(21.188)
block_netherBrickFenceGateID = float(21.189)
block_redNetherBrickFenceGateID = float(21.190)
block_iceFencegateID = float(21.191)
block_blueIceFencegateID = float(21.192)
block_packedIceFenceGateID = float(21.193)
block_snowFenceGateID = float(21.194)
block_dirtFenceGateID = float(21.195)
block_cobblestoneFenceGateID = float(21.196)
block_mossyCobblestoneFenceGateID = float(21.197)
block_caveStoneFenceGateID = float(21.198)
block_smoothStoneFenceGateID = float(21.199)
block_yellowSandstoneFencegateID = float(21.200)
block_redSandstoneFencegateID = float(21.201)
block_oakWoodPlankFenceGateID = float(21.202)
block_prismarineElectricFenceID = float(21.203)
block_prismarineElectricFencegateID = float(21.204)
block_prismarineElectricWallID = float(21.205)
block_darkprismarineElectricFenceID = float(21.206)
block_darkprismarineElectricFencegateID = float(21.207)
block_darkprismarineElectricWallID = float(21.208)
block_steelElectricFenceID = float(21.209)
block_steelElectricFencegateID = float(21.210)
block_steelElectricWallID = float(21.211)
# finish the rest of this tomorrow:
'''
Fencegates: all wood types, planks, logs, stripped
'''
''' Ocean Monument ''' # Category 23
block_prismarineBlockID = float(22.1)
block_prismarineBrickBlockID = float(22.2)
block_seaLanternBlockID = float(22.3)
''' Solid Ores ''' # Category 24
block_steelBlockID = float(23.1)
block_diamondBlockID = float(23.2)
block_ironBlockID = float(23.3)
block_goldBlockID = float(23.4)
block_emeraldBlockID = float(23.5)
block_BronzeBlockID = float(23.6)
block_silverBlockID = float(23.7)
block_rubyBlockID = float(23.8)
block_lapisLazuliBlockID = float(23.9)
block_coalBlockID = float(23.10)
block_aluminumOreBlockID = float(23.11)
block_tinOreBlockID = float(23.12)
block_titaniumBlockID = float(23.13)
block_sapphireBlockID = float(23.14)
''' Liquid ''' # Category 25
block_waterBlockID = float(24.1)
block_coldWaterBlockID = float(24.2)
block_soulWaterBlockID = float(24.3)
block_magmaWaterBlockID = float(24.4)
block_redLavaBlockID = float(24.5)
block_orangeLavaBlockID = float(24.6)
block_plainMilkBlockID = float(24.7)
block_chocolateMilkBlockID = float(24.8)
block_strawberryMilkBlockID = float(24.9)
block_greenAcidBlockID = float(24.10)
block_urineBlockID = float(24.11)
block_oilBlockID = float(24.12)
block_tarBlockID = float(24.13)
block_gasolineBlockID = float(24.14)
block_petroleumBlockID = float(24.15)
block_steamingWaterBlockID = float(24.16)
block_javaID = float(24.17)
block_moltenChocolateBlockID = float(24.18)
block_coconutMilkBlockID = float(24.19)
block_peanutButterID = float(24.20)
block_honeyID = float(24.21)
block_slowRisingWaterID = float(24.22) # Rises at 1 block every 8 ticks
block_fastRisingWaterID = float(24.23) # Rises at 1 block every 2 ticks
block_slowRisingLavaID = float(24.24) # rises at 1 block every 64 ticks
block_fastRisingLavaID = float(24.25) # rises at 1 block every 8 ticks
block_extremelyFastRisingLavaID = float(24.26) # rises at 1 block every 2 ticks
block_fastestRisingLavaID = float(24.27) # rises at 8 blocks every 1 tick
block_ketchupBlockID = float(24.28)
block_slowRisingKetchupID = float(24.29) # Rises at 1 block every 16 ticks
block_fastRisingKetchupID = float(24.30) # Rises at 1 block every 4 ticks
block_extremelyFastRisingKetchupID = float(24.31) # Rises at 1 block every 1 tick
block_fastestRisingKetchupID = float(24.32) # Rises at 8 blocks every 1 tick
''' Bones ''' # Category 26
block_ribcageBlockID = float(25.1)
block_skullBlockID = float(25.2)
''' Helpful ''' # Category 27
block_spongeID = float(26.1)
block_wetSpongeID = float(26.2)
block_lavaSpongeID = float(26.3)
block_wetLavaSpongeID = float(26.4)
block_superSpongeID = float(26.5)
''' Transportation ''' # Category 28
block_poweredRailID = float(27.1)
block_normalRailID = float(27.2)
block_activatorRailID = float(27.3)
block_wallRailID = float(27.4)
block_ceilingRailID = float(27.5)
block_oakWoodLadderID = float(27.6)
block_darkOakWoodLadderID = float(27.7)
block_acaciaWoodLadderID = float(27.8)
block_birchWoodLadderID = float(27.9)
block_spruceWoodLadderID = float(27.10)
block_JungleWoodLadderID = float(27.11)
block_cherryWoodLadderID = float(27.12)
block_locustWoodLadderID = float(27.13)
block_appleWoodLadderID = float(27.14)
block_ashWoodLadderID = float(27.15)
block_vineID = float(27.16)
block_policeCarID = float(27.17)
block_firetruckID = float(27.18)
block_ambulanceID = float(27.19)
block_steelRowingBoatID = float(27.20)
block_diamondRowingBoatID = float(27.21)
block_oakWoodRowingBoatID = float(27.22)
block_darkOakWoodRowingBoatID = float(27.23)
block_acaciaWoodRowingBoatID = float(27.24)
block_birchWoodRowingBoatID = float(27.25)
block_spruceWoodRowingBoatID = float(27.26)
block_jungleWoodRowingBoatID = float(27.27)
block_cherryWoodRowingBoatID = float(27.28)
block_locustWoodRowingBoatID = float(27.29)
block_appleWoodRowingBoatID = float(27.30)
block_ashWoodRowingBoatID = float(27.31)
block_aluminumRowingBoatID = float(27.32)
block_ironRowingBoatID = float(27.33)
block_obsidianRowingBoatID = float(27.34)
block_tinRowingBoatID = float(27.35)
block_goldRowingBoatID = float(27.36)
block_emeraldRowingBoatID = float(27.37)
block_diamondRowingBoatID = float(27.38)
block_ironMinecartID = float(27.39)
block_ironMinecartWithEnderChestID = float(27.40)
block_ironMinecartWithChestID = float(27.41)
block_ironMinecartWithTNTID = float(27.42)
block_ironMinecartWithDynamiteID = float(27.43)
block_ironMinecartWithFurnaceID = float(27.44)
block_ironMinecartWithBlastFurnaceID = float(27.45)
block_ironMinecartWithHopperID = float(27.46)
''' Desert caves ''' # Category 29
block_yellowSandBlockID = float(28.1)
block_redSandBlockID = float(28.2)
block_blueSandBlockID = float(28.3)
block_greenSandBlockID = float(28.4)
block_blackSandBlockID = float(28.4)
block_orangeSandBlockID = float(28.6)
block_yellowSandStoneBlockID = float(28.7)
block_smoothYellowSandStoneBlockID = float(28.8)
block_carvedYellowSandStoneBlockID = float(28.9)
block_redSandStoneBlockID = float(28.10)
block_smoothRedSandStoneBlockID = float(28.11)
block_carvedRedSandStoneBlockID = float(28.12)
block_blueSandStoneBlockID = float(28.13)
block_smoothBlueSandStoneBlockID = float(28.14)
block_carvedBlueSandStoneBlockID = float(28.15)
block_greenSandStoneBlockID = float(28.16)
block_smoothGreenSandStoneBlockID = float(28.17)
block_carvedGreenSandStoneBlockID = float(28.18)
block_blackSandStoneBlockID = float(28.19)
block_smoothBlackSandStoneBlockID = float(28.20)
block_carvedBlackSandStoneBlockID = float(28.21)
block_orangeSandStoneBlockID = float(28.22)
block_smoothOrangeSandStoneBlockID = float(28.23)
block_carvedOrangeSandStoneBlockID = float(28.24)
block_gravelBlockID = float(28.25)
block_cactusID = float(28.26)
block_cobwebID = float(28.27)
block_yellowQuicksandBlockID = float(28.28)
block_redQuicksandBlockID = float(28.29)
block_blueQuicksandBlockID = float(28.30)
block_greenQuicksandBlockID = float(28.31)
block_blackQuicksandBlockID = float(28.32)
block_orangeQuicksandBlockID = float(28.33)
''' Classic explosives ''' # Category 30
block_TNTBlockID = float(29.1)
block_dynamiteBlockID = float(29.2)
block_netherRedBedID = float(29.3) # Use this bed to make explosions in all biomes, even in the overworld. Does not let you sleep in the nether.
''' Quartz and urban blocks ''' # Category 31
block_quartzBlockID = float(30.1)
block_beaconID = float(30.2)
block_quartzPillarBlockID = float(30.3)
block_smoothQuartzBlockID = float(30.4)
block_chiseledQuartzBlockID = float(30.5)
block_dioriteBlockID = float(30.6)
block_polishedDioriteBlockID = float(30.7)
block_andesiteBlockID = float(30.8)
block_polishedAndesiteBlockID = float(30.9)
block_graniteBlockID = float(30.10)
block_polishedGraniteBlockID = float(30.11)
block_solidBrownCardboardBlockID = float(30.12)
block_brownCardboardBlockID = float(30.13)
block_wetBrownCardboardBlockID = float(30.14)
block_packedBrownCardboardBlockID = float(30.15)
block_brownCardboardDoorID = float(30.16)
block_brownCardboardTrapdoorID = float(30.17)
block_brownCardboardWallID = float(30.18)
block_brownCardboardFenceID = float(30.19)
block_solidBrownCardboardSlabID = float(30.20)
block_wetBrownCardboardSlabID = float(30.21)
block_packedBrownCardboardSlabID = float(30.22)
block_solidBrownCardboardStaircaseID = float(30.23)
block_wetBrownCardboardStaircaseID = float(30.24)
block_packedBrownCardboardStaircaseID = float(30.25)
block_solidwhiteCardboardBlockID = float(30.26)
block_whiteCardboardBlockID = float(30.27)
block_wetwhiteCardboardBlockID = float(30.28)
block_packedwhiteCardboardBlockID = float(30.29)
block_whiteCardboardDoorID = float(30.30)
block_whiteCardboardTrapdoorID = float(30.31)
block_whiteCardboardWallID = float(30.32)
block_whiteCardboardFenceID = float(30.33)
block_solidwhiteCardboardSlabID = float(30.34)
block_wetwhiteCardboardSlabID = float(30.35)
block_packedwhiteCardboardSlabID = float(30.36)
block_solidwhiteCardboardStaircaseID = float(30.37)
block_wetwhiteCardboardStaircaseID = float(30.38)
block_packedwhiteCardboardStaircaseID = float(30.39)
block_solidlightGreyCardboardBlockID = float(30.40)
block_lightGreyCardboardBlockID = float(30.41)
block_wetlightGreyCardboardBlockID = float(30.42)
block_packedlightGreyCardboardBlockID = float(30.43)
block_lightGreyCardboardDoorID = float(30.44)
block_lightGreyCardboardTrapdoorID = float(30.45)
block_lightGreyCardboardWallID = float(30.46)
block_lightGreyCardboardFenceID = float(30.47)
block_solidlightGreyCardboardSlabID = float(30.48)
block_wetlightGreyCardboardSlabID = float(30.49)
block_packedlightGreyCardboardSlabID = float(30.50)
block_solidlightGreyCardboardStaircaseID = float(30.51)
block_wetlightGreyCardboardStaircaseID = float(30.52)
block_packedlightGreyCardboardStaircaseID = float(30.53)
block_soliddarkGreyCardboardBlockID = float(30.54)
block_darkGreyCardboardBlockID = float(30.55)
block_wetdarkGreyCardboardBlockID = float(30.56)
block_packeddarkGreyCardboardBlockID = float(30.57)
block_darkGreyCardboardDoorID = float(30.58)
block_darkGreyCardboardTrapdoorID = float(30.59)
block_darkGreyCardboardWallID = float(30.60)
block_darkGreyCardboardFenceID = float(30.61)
block_soliddarkGreyCardboardSlabID = float(30.62)
block_wetdarkGreyCardboardSlabID = float(30.63)
block_packeddarkGreyCardboardSlabID = float(30.64)
block_soliddarkGreyCardboardStaircaseID = float(30.65)
block_wetdarkGreyCardboardStaircaseID = float(30.66)
block_packeddarkGreyCardboardStaircaseID = float(30.67)
block_solidblackCardboardBlockID = float(30.68)
block_blackCardboardBlockID = float(30.69)
block_wetblackCardboardBlockID = float(30.70)
block_packedblackCardboardBlockID = float(30.71)
block_blackCardboardDoorID = float(30.72)
block_blackCardboardTrapdoorID = float(30.73)
block_blackCardboardWallID = float(30.74)
block_blackCardboardFenceID = float(30.75)
block_solidblackCardboardSlabID = float(30.76)
block_wetblackCardboardSlabID = float(30.77)
block_packedblackCardboardSlabID = float(30.78)
block_solidblackCardboardStaircaseID = float(30.79)
block_wetblackCardboardStaircaseID = float(30.80)
block_packedblackCardboardStaircaseID = float(30.81)
block_solidyellowCardboardBlockID = float(30.82)
block_yellowCardboardBlockID = float(30.83)
block_wetyellowCardboardBlockID = float(30.84)
block_packedyellowCardboardBlockID = float(30.85)
block_yellowCardboardDoorID = float(30.86)
block_yellowCardboardTrapdoorID = float(30.87)
block_yellowCardboardWallID = float(30.88)
block_yellowCardboardFenceID = float(30.89)
block_solidyellowCardboardSlabID = float(30.90)
block_wetyellowCardboardSlabID = float(30.91)
block_packedyellowCardboardSlabID = float(30.92)
block_solidyellowCardboardStaircaseID = float(30.93)
block_wetyellowCardboardStaircaseID = float(30.94)
block_packedyellowCardboardStaircaseID = float(30.95)
block_solidcyanCardboardBlockID = float(30.96)
block_cyanCardboardBlockID = float(30.97)
block_wetcyanCardboardBlockID = float(30.98)
block_packedcyanCardboardBlockID = float(30.99)
block_cyanCardboardDoorID = float(30.100)
block_cyanCardboardTrapdoorID = float(30.101)
block_cyanCardboardWallID = float(30.102)
block_cyanCardboardFenceID = float(30.103)
block_solidcyanCardboardSlabID = float(30.104)
block_wetcyanCardboardSlabID = float(30.105)
block_packedcyanCardboardSlabID = float(30.106)
block_solidcyanCardboardStaircaseID = float(30.107)
block_wetcyanCardboardStaircaseID = float(30.108)
block_packedcyanCardboardStaircaseID = float(30.109)
block_solidturquioseCardboardBlockID = float(30.110)
block_turquioseCardboardBlockID = float(30.111)
block_wetturquioseCardboardBlockID = float(30.112)
block_packedturquioseCardboardBlockID = float(30.113)
block_turquioseCardboardDoorID = float(30.114)
block_turquioseCardboardTrapdoorID = float(30.115)
block_turquioseCardboardWallID = float(30.116)
block_turquioseCardboardFenceID = float(30.117)
block_solidturquioseCardboardSlabID = float(30.118)
block_wetturquioseCardboardSlabID = float(30.119)
block_packedturquioseCardboardSlabID = float(30.120)
block_solidturquioseCardboardStaircaseID = float(30.121)
block_wetturquioseCardboardStaircaseID = float(30.122)
block_packedturquioseCardboardStaircaseID = float(30.123)
block_solidlightBlueCardboardBlockID = float(30.124)
block_lightBlueCardboardBlockID = float(30.125)
block_wetlightBlueCardboardBlockID = float(30.126)
block_packedlightBlueCardboardBlockID = float(30.127)
block_lightBlueCardboardDoorID = float(30.128)
block_lightBlueCardboardTrapdoorID = float(30.129)
block_lightBlueCardboardWallID = float(30.130)
block_lightBlueCardboardFenceID = float(30.131)
block_solidlightBlueCardboardSlabID = float(30.132)
block_wetlightBlueCardboardSlabID = float(30.133)
block_packedlightBlueCardboardSlabID = float(30.134)
block_solidlightBlueCardboardStaircaseID = float(30.135)
block_wetlightBlueCardboardStaircaseID = float(30.136)
block_packedlightBlueCardboardStaircaseID = float(30.137)
block_soliddarkBlueCardboardBlockID = float(30.138)
block_darkBlueCardboardBlockID = float(30.139)
block_wetdarkBlueCardboardBlockID = float(30.140)
block_packeddarkBlueCardboardBlockID = float(30.141)
block_darkBlueCardboardDoorID = float(30.142)
block_darkBlueCardboardTrapdoorID = float(30.143)
block_darkBlueCardboardWallID = float(30.144)
block_darkBlueCardboardFenceID = float(30.145)
block_soliddarkBlueCardboardSlabID = float(30.146)
block_wetdarkBlueCardboardSlabID = float(30.147)
block_packeddarkBlueCardboardSlabID = float(30.148)
block_soliddarkBlueCardboardStaircaseID = float(30.149)
block_wetdarkBlueCardboardStaircaseID = float(30.150)
block_packeddarkBlueCardboardStaircaseID = float(30.151)
block_solidpinkCardboardBlockID = float(30.152)
block_pinkCardboardBlockID = float(30.153)
block_wetpinkCardboardBlockID = float(30.154)
block_packedpinkCardboardBlockID = float(30.155)
block_pinkCardboardDoorID = float(30.156)
block_pinkCardboardTrapdoorID = float(30.157)
block_pinkCardboardWallID = float(30.158)
block_pinkCardboardFenceID = float(30.159)
block_solidpinkCardboardSlabID = float(30.160)
block_wetpinkCardboardSlabID = float(30.161)
block_packedpinkCardboardSlabID = float(30.162)
block_solidpinkCardboardStaircaseID = float(30.163)
block_wetpinkCardboardStaircaseID = float(30.164)
block_packedpinkCardboardStaircaseID = float(30.165)
block_solidmagentaCardboardBlockID = float(30.166)
block_magentaCardboardBlockID = float(30.167)
block_wetmagentaCardboardBlockID = float(30.168)
block_packedmagentaCardboardBlockID = float(30.169)
block_magentaCardboardDoorID = float(30.170)
block_magentaCardboardTrapdoorID = float(30.171)
block_magentaCardboardWallID = float(30.172)
block_magentaCardboardFenceID = float(30.173)
block_solidmagentaCardboardSlabID = float(30.174)
block_wetmagentaCardboardSlabID = float(30.175)
block_packedmagentaCardboardSlabID = float(30.176)
block_solidmagentaCardboardStaircaseID = float(30.177)
block_wetmagentaCardboardStaircaseID = float(30.178)
block_packedmagentaCardboardStaircaseID = float(30.179)
block_solidmagentaCardboardBlockID = float(30.180)
block_magentaCardboardBlockID = float(30.181)
block_wetmagentaCardboardBlockID = float(30.182)
block_packedmagentaCardboardBlockID = float(30.183)
block_magentaCardboardDoorID = float(30.184)
block_magentaCardboardTrapdoorID = float(30.185)
block_magentaCardboardWallID = float(30.186)
block_magentaCardboardFenceID = float(30.187)
block_solidmagentaCardboardSlabID = float(30.188)
block_wetmagentaCardboardSlabID = float(30.189)
block_packedmagentaCardboardSlabID = float(30.190)
block_solidmagentaCardboardStaircaseID = float(30.191)
block_wetmagentaCardboardStaircaseID = float(30.192)
block_packedmagentaCardboardStaircaseID = float(30.193)
block_solidredCardboardBlockID = float(30.194)
block_redCardboardBlockID = float(30.195)
block_wetredCardboardBlockID = float(30.196)
block_packedredCardboardBlockID = float(30.197)
block_redCardboardDoorID = float(30.198)
block_redCardboardTrapdoorID = float(30.199)
block_redCardboardWallID = float(30.200)
block_redCardboardFenceID = float(30.201)
block_solidredCardboardSlabID = float(30.202)
block_wetredCardboardSlabID = float(30.203)
block_packedredCardboardSlabID = float(30.204)
block_solidredCardboardStaircaseID = float(30.205)
block_wetredCardboardStaircaseID = float(30.206)
block_packedredCardboardStaircaseID = float(30.207)
block_solidorangeCardboardBlockID = float(30.208)
block_orangeCardboardBlockID = float(30.209)
block_wetorangeCardboardBlockID = float(30.210)
block_packedorangeCardboardBlockID = float(30.211)
block_orangeCardboardDoorID = float(30.212)
block_orangeCardboardTrapdoorID = float(30.213)
block_orangeCardboardWallID = float(30.214)
block_orangeCardboardFenceID = float(30.215)
block_solidorangeCardboardSlabID = float(30.216)
block_wetorangeCardboardSlabID = float(30.217)
block_packedorangeCardboardSlabID = float(30.218)
block_solidorangeCardboardStaircaseID = float(30.219)
block_wetorangeCardboardStaircaseID = float(30.220)
block_packedorangeCardboardStaircaseID = float(30.221)
block_solidgreenCardboardBlockID = float(30.222)
block_greenCardboardBlockID = float(30.223)
block_wetgreenCardboardBlockID = float(30.224)
block_packedgreenCardboardBlockID = float(30.225)
block_greenCardboardDoorID = float(30.226)
block_greenCardboardTrapdoorID = float(30.227)
block_greenCardboardWallID = float(30.228)
block_greenCardboardFenceID = float(30.229)
block_solidgreenCardboardSlabID = float(30.230)
block_wetgreenCardboardSlabID = float(30.231)
block_packedgreenCardboardSlabID = float(30.232)
block_solidgreenCardboardStaircaseID = float(30.233)
block_wetgreenCardboardStaircaseID = float(30.234)
block_packedgreenCardboardStaircaseID = float(30.235)
block_solidlimeCardboardBlockID = float(30.236)
block_limeCardboardBlockID = float(30.237)
block_wetlimeCardboardBlockID = float(30.238)
block_packedlimeCardboardBlockID = float(30.239)
block_limeCardboardDoorID = float(30.240)
block_limeCardboardTrapdoorID = float(30.241)
block_limeCardboardWallID = float(30.242)
block_limeCardboardFenceID = float(30.243)
block_solidlimeCardboardSlabID = float(30.244)
block_wetlimeCardboardSlabID = float(30.245)
block_packedlimeCardboardSlabID = float(30.246)
block_solidlimeCardboardStaircaseID = float(30.247)
block_wetlimeCardboardStaircaseID = float(30.248)
block_packedlimeCardboardStaircaseID = float(30.249)
block_deadPurpleShulkerBlockID = float(30.250) # Dead shulkers don't shoot, they can be used for storage and building
block_activePurpleShulkerBlockID = float(30.251) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadPinkShulkerBlockID = float(30.252) # Dead shulkers don't shoot, they can be used for storage and building
block_activePinkShulkerBlockID = float(30.253) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadCyanShulkerBlockID = float(30.254) # Dead shulkers don't shoot, they can be used for storage and building
block_activeCyanShulkerBlockID = float(30.255) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadTurquioseShulkerBlockID = float(30.256) # Dead shulkers don't shoot, they can be used for storage and building
block_activeTurquioseShulkerBlockID = float(30.257) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadLightBlueShulkerBlockID = float(30.258) # Dead shulkers don't shoot, they can be used for storage and building
block_activeLightBlueShulkerBlockID = float(30.259) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadDarkBlueShulkerBlockID = float(30.260) # Dead shulkers don't shoot, they can be used for storage and building
block_activeDarkBlueShulkerBlockID = float(30.261) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadRedShulkerBlockID = float(30.262) # Dead shulkers don't shoot, they can be used for storage and building
block_activeRedShulkerBlockID = float(30.263) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadMagentaShulkerBlockID = float(30.264) # Dead shulkers don't shoot, they can be used for storage and building
block_activeMagentaShulkerBlockID = float(30.265) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadLightGreyShulkerBlockID = float(30.266) # Dead shulkers don't shoot, they can be used for storage and building
block_activeLightGreyShulkerBlockID = float(30.267) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadDarkGreyShulkerBlockID = float(30.268) # Dead shulkers don't shoot, they can be used for storage and building
block_activeDarkGreyShulkerBlockID = float(30.269) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadBlackShulkerBlockID = float(30.270) # Dead shulkers don't shoot, they can be used for storage and building
block_activeBlackShulkerBlockID = float(30.271) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadOrangeShulkerBlockID = float(30.272) # Dead shulkers don't shoot, they can be used for storage and building
block_activeOrangeShulkerBlockID = float(30.273) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadGreenShulkerBlockID = float(30.274) # Dead shulkers don't shoot, they can be used for storage and building
block_activeGreenShulkerBlockID = float(30.275) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
block_deadLimeShulkerBlockID = float(30.276) # Dead shulkers don't shoot, they can be used for storage and building
block_activeLimeShulkerBlockID = float(30.277) # Active shulkers shoot orbs that give you the levitation effect. They can also be used for storage and building. They only activate in difficulties above peaceful
''' The great outdoors ''' # Category 32
block_campfireID = float(31.1)
block_sleepingBagID = float(31.2)
block_ironSpitID = float(31.3)
block_steelSpitID = float(31.4)
block_titaniumSpitID = float(31.5)
block_tinSpitID = float(31.6)
block_goldSpitID = float(31.7)
block_diamondSpitID = float(31.8)
block_tentPostID = float(31.9)
block_hornCoralBlockID = float(31.10) # Coral block works underwater, dies on land
block_fireCoralBlockID = float(31.11) # Coral block works underwater, dies on land
block_tubeCoralBlockID = float(31.12) # Coral block works underwater, dies on land
block_bubbleCoralBlockID = float(31.13) # Coral block works underwater, dies on land
block_brainCoralBlockID = float(31.14) # Coral block works underwater, dies on land
block_deadHornCoralBlockID = float(31.15) # Dead coral block. Revives in water
block_deadFireCoralBlockID = float(31.16) # Dead coral block. Revives in water
block_deadTubeCoralBlockID = float(31.17) # Dead coral block. Revives in water
block_deadBubbleCoralBlockID = float(31.18) # Dead coral block. Revives in water
block_deadBrainCoralBlockID = float(31.19) # Dead coral block. Revives in water
block_imitatorHornCoralBlockID = float(31.20) # Coral block that works on land, and dies in water
block_imitatorFireCoralBlockID = float(31.21) # Coral block that works on land, and dies in water
block_imitatorTubeCoralBlockID = float(31.22) # Coral block that works on land, and dies in water
block_imitatorBubbleCoralBlockID = float(31.23) # Coral block that works on land, and dies in water
block_imitatorBrainCoralBlockID = float(31.24) # Coral block that works on land, and dies in water
block_sunCoreBlockID = float(31.25) # The brightest block in the game, and the biggest fire hazard. Unless you contain it, keep it at least 1000 blocks away from other flammable blocks. Containment is in the crafting recipe file
block_sunReactorBlockID = float(31.26)
''' In the sky and outer space ''' # Category 33
block_cloudBlockID = float(32.1)
block_stormCloudBlockID = float(32.2)
block_moonStoneBlockID = float(32.3)
block_lightningRodID = float(32.4)
''' Food ''' # Category 34
block_chocolateBlockID = float(33.1)
block_watermelonBlockID = float(33.2)
block_whiteBreadBlockID = float(33.3)
block_breadLoafBlockID = float(33.4)
block_whiteCheeseBlockID = float(33.5)
''' More Plants ''' # Category 35
block_lilyPadID = float(34.1)
block_cattailPlantID = float(34.2)
block_kelpPlantID = float(34.3)
block_poppyPlantID = float(34.4)
block_roseBushID = float(34.5)
block_redMushroomID = float(34.6)
block_brownMushroomID = float(34.7)
block_whiteDottedRedMushroomBlockID = float(34.9)
block_dandelionID = float(34.10)
block_blueOrchidID = float(34.11)
block_seaWeedPlantID = float(34.12)
block_pumpkinBlockID = float(34.13)
block_carvedPumpkinBlockID = float(34.14)
block_jackolanternID = float(34.15)
block_chorusPlantID = float(34.16)
''' Leaves and shrubs ''' # Category 36
block_oakWoodLeavesID = float(35.1)
block_darkOakWoodLeavesID = float(35.2)
block_acaciaWoodLeavesID = float(35.3)
block_spruceWoodLeavesID = float(35.4)
block_jungleWoodLeavesID = float(35.5)
block_birchWoodLeavesID = float(35.6)
block_cherryWoodLeavesID = float(35.7)
block_locustWoodLeavesID = float(35.8)
block_ashWoodLeavesID = float(35.9)
block_appleWoodLeavesID = float(35.10)
block_sycamoreWoodLeavesID = float(35.11)
block_pineWoodLeavesID = float(35.12)
block_chestnutWoodLeavesID = float(35.13)
block_palmWoodLeavesID = float(35.14)
block_acornWoodLeavesID = float(35.15)
block_greenShrubID = float(35.16)
block_burntShrubID = float(35.17)
''' Plastic ''' # Category 37
""" For plastic blocks """
block_whitePlasticBlockID = float(36.1)
block_blackPlasticBlockID = float(36.2)
block_lightGreyPlasticBlockID = float(36.3)
block_darkGreyPlasticBlockID = float(36.4)
block_cyanPlasticBlockID = float(36.5)
block_yellowPlasticBlockID = float(36.6)
block_turquiosePlasticBlockID = float(36.7)
block_bluePlasticBlockID = float(36.8)
block_darkBluePlasticBlockID = float(36.9)
block_redPlasticBlockID = float(36.10)
block_bluePlasticBlockID = float(36.11)
block_purplePlasticBlockID = float(36.12)
block_pinkPlasticBlockID = float(36.13)
block_brownPlasticBlockID = float(36.14)
''' Banners and flags ''' # Category 38
""" For banner and flag blocks """
block_illagerBannerID = float(37.1)
block_whiteBannerID = float(37.2)
block_blackBannerID = float(37.3)
block_lightGreyBannerID = float(37.4)
block_darkGreyBannerID = float(37.5)
block_brownBannerID = float(37.6)
block_orangeBannerID = float(37.7)
block_pinkBannerID = float(37.8)
block_purpleBannerID = float(37.9)
block_magentaBannerID = float(37.10)
block_redBannerID = float(37.11)
block_yellowBannerID = float(37.12)
block_greenBannerID = float(37.13)
block_limeBannerID = float(37.14)
block_lightBlueBannerID = float(37.15)
block_darkBlueBannerID = float(37.16)
block_cyanBannerID = float(37.17)
block_turquioseBannerID = float(37.18)
block_villagerBannerID = float(37.19)
block_creeperBannerID = float(37.20)
block_endermanBannerID = float(37.21)
block_zombieBannerID = float(37.22)
block_witherSkeletonBannerID = float(37.23)
block_skeletonBannerID = float(37.24)
block_blazeBannerID = float(37.25)
block_pigBannerID = float(37.26)
block_chickenBannerID = float(37.27)
block_cowBannerID = float(37.28)
block_mooshroomBannerID = float(37.29)
block_japaneseFlagID = float(37.30)
block_russianFlagID = float(37.31)
block_USSRFlagID = float(37.32)
block_germanFlagID = float(37.33)
block_completeAmericanFlagID = float(37.34)
block_italianFlagID = float(37.35)
block_norwegianFlagID = float(37.36)
block_indiaFlagID = float(37.37)
block_southKoreanFlagID = float(37.38)
block_northKoreanFlagID = float(37.39)
block_swedishFlagID = float(37.40)
block_UKFlagID = float(37.41)
block_EUFlagID = float(37.42)
block_naziGermanyFlagID = float(37.43)
block_hungarianFlagID = float(37.44)
block_polishFlagID = float(37.45)
block_turkishFlagID = float(37.46)
block_whiteFlagID = float(37.47)
block_blackFlagID = float(37.48)
block_lightGreyFlagID = float(37.49)
block_darkGreyFlagID = float(37.50)
block_brownFlagID = float(37.51)
block_blackAndWhiteCheckeredFlagID = float(37.52)
block_orangeFlagID = float(37.53)
block_pinkFlagID = float(37.54)
block_purpleFlagID = float(37.55)
block_magentaFlagID = float(37.56)
block_redFlagID = float(37.57)
block_yellowFlagID = float(37.58)
block_greenFlagID = float(37.59)
block_limeFlagID = float(37.60)
block_lightBlueFlagID = float(37.61)
block_darkBlueFlagID = float(37.62)
block_cyanFlagID = float(37.63)
block_turquioseFlagID = float(37.64)
block_canadianFlagID = float(37.65)
block_communistChinaFlagID = float(37.66)
block_ww2JapaneseFlagID = float(37.67)
block_australianFlagID = float(37.68)
block_austrianFlagID = float(37.69)
block_belgiumFlagID = float(37.70)
block_brazilFlagID = float(37.71)
block_cambodiaFlagID = float(37.72)
block_vietnamFlagID = float(37.73)
block_chileFlagID = float(37.74)
block_CzechRepublicFlagID = float(37.75)
block_denmarkFlagID = float(37.76)
block_egyptFlagID = float(37.77)
block_finlandFlagID = float(37.78)
block_georgiaFlagID = float(37.79)
block_greeceFlagID = float(37.80)
block_irelandFlagID = float(37.81)
block_indonesiaFlagID = float(37.82)
block_iranFlagID = float(37.83)
block_iraqFlagID = float(37.84)
block_israelFlagID = float(37.85)
block_mexicoFlagID = float(37.86)
block_nepalFlagID = float(37.87)
block_norwayFlagID = float(37.88)
block_panamaFlagID = float(37.89)
block_romaniaFlagID = float(37.90)
block_serbiaFlagID = float(37.91)
block_spainFlagID = float(37.92)
block_ukrainFlagID = float(37.93)
''' Infested blocks ''' # Category 39
""" For monster infested blocks """
block_infestedCaveStoneBlockID = float(38.1) # Spanws silverfish
block_infestedCobblestoneBlockID = float(38.2) # Spawns silverfish
block_infestedMossyCobblestoneBlockID = float(38.3) # Spawns silverfish
block_infestedStoneBricksBlockID = float(38.4) # Spanws silverfish
block_infestedEndStoneBlockID = float(38.5) # Spawns endermite
block_infestedPurPurBlockID = float(38.6) # Spawns endermite
block_infestedPurPurPillarBlockID = float(38.7) # Spawns endermite
block_infestedObsidianBlockID = float(38.8) # Spawns endermite
block_infestedBrownCardboardBlockID = float(38.9) # Spawns mice
block_infestedOakWoodLogID = float(38.10) # Spawns termites
block_infestedOakWoodPlanksID = float(38.11) # Spawns termites
block_infestedDirtBlockID = float(38.12) # Spawns silverfish
block_infestedCoarseDirtBlockID = float(38.13) # Spawns silverfish
block_infestedBedrockBlockID = float(38.14) # Spawns endermite # This is one of the only ways to obtain bedrock in survival mode. This bedrock can be mined with a pickaxe with efficiency X or higher, and drops bedrock. The bedrock you receive is not infested, unless you use silk touch, and can easily be mined by the miner when misplaced
block_infestedSmoothStoneBlockID = float(38.15) # Spawns silverfish
''' Slopes ''' # Category 40
""" For triangle slopes and curved slope blocks """
block_grassCurvedSlopeBlockID = float(39.1) # A curved grassy slope
block_grassStraightSlopeBlockID = float(39.2) # A normal grass slope
block_dirtCurvedSlopeBlockID = float(39.3) # A curved dirt slope
block_dirtStraightSlopeBlockID = float(39.4) # A normal dirt slope
block_caveStoneCurvedSlopeBlockID = float(39.5) # A curved cave stone slope
block_caveStoneStraightSlopeBlockID = float(39.6) # A normal cave stone slope
block_obsidianCurvedSlopeBlockID = float(39.7) # A curved obsidian slope
block_obsidianStraightSlopeBlockID = float(39.8) # A normal obsidian slope
block_waterCurvedSlopeBlockID = float(39.9) # A curved water slope
block_waterStraightSlopeBlockID = float(39.10) # A normal water slope
block_flowingWaterCurvedSlopeBlockID = float(39.11) # A curved flowing water slope
block_flowingWaterStraightSlopeBlockID = float(39.12) # A normal flowing water slope
block_lavaCurvedSlopeBlockID = float(39.13) # A curved lava slope
block_lavaStraightSlopeBlockID = float(39.14) # A normal lava slope
block_flowingLavaCurvedSlopeBlockID = float(39.15) # A curved flowing lava slope
block_flowingLavaStraightSlopeBlockID = float(39.16) # A normal flowing lava slope
block_goldBlockCurvedSlopeBlockID = float(39.17) # A curved gold block slope
block_goldBlockStraightSlopeBlockID = float(39.18) # A normal gold block slope
block_ironBlockCurvedSlopeBlockID = float(39.19) # A curved iron block slope
block_ironBlockStraightSlopeBlockID = float(39.20) # A normal iron block slope
block_iceBlockCurvedSlopeBlockID = float(39.21) # A curved ice block slope
block_iceBlockStraightSlopeBlockID = float(39.22) # A normal ice block slope
block_packedIceBlockCurvedSlopeBlockID = float(39.23) # A curved packed ice block slope
block_packedIceBlockStraightSlopeBlockID = float(39.24) # A normal packed ice block slope
block_blueIceBlockCurvedSlopeBlockID = float(39.25) # A curved blue ice block slope
block_blueIceBlockStraightSlopeBlockID = float(39.26) # A normal blue ice block slope
block_endStoneBlockCurvedSlopeBlockID = float(39.27) # A curved end stone block slope
block_endStoneBlockStraightSlopeBlockID = float(39.28) # A normal end stone block slope
block_endBrickBlockCurvedSlopeBlockID = float(39.29) # A curved end brick block slope
block_endBrickBlockStraightSlopeBlockID = float(39.30) # A normal end brick block slope
block_gravelBlockCurvedSlopeBlockID = float(39.31) # A curved gravel block slope
block_gravelBlockStraightSlopeBlockID = float(39.32) # A normal gravel block slope
block_podzolBlockCurvedSlopeBlockID = float(39.33) # A curved podzol block slope
block_podzolBlockStraightSlopeBlockID = float(39.34) # A normal podzol block slope
block_myceliumBlockCurvedSlopeBlockID = float(39.35) # A curved mycelium block slope
block_myceliumBlockStraightSlopeBlockID = float(39.36) # A normal mycelium block slope
block_clayBlockCurvedSlopeBlockID = float(39.37) # A curved clay block slope
block_claylBlockStraightSlopeBlockID = float(39.38) # A normal clay block slope
block_yellowSandBlockCurvedSlopeBlockID = float(39.39) # A curved yellow sand block slope
block_yellowSandlBlockStraightSlopeBlockID = float(39.40) # A normal yellow sand block slope
block_redSandBlockCurvedSlopeBlockID = float(39.41) # A curved red sand block slope
block_redSandlBlockStraightSlopeBlockID = float(39.42) # A normal red sand block slope
block_snowBlockCurvedSlopeBlockID = float(39.43) # A curved snow block slope
block_snowBlockStraightSlopeBlockID = float(39.44) # A normal snow block slope
block_packedSnowBlockCurvedSlopeBlockID = float(39.45) # A curved packed snow block slope
block_packedSnowBlockStraightSlopeBlockID = float(39.46) # A normal packed snow block slope
block_magmaBlockCurvedSlopeBlockID = float(39.47) # A curved magma block slope
block_magmaBlockStraightSlopeBlockID = float(39.48) # A normal magma block slope
block_coalBlockCurvedSlopeBlockID = float(39.49) # A curved coal block slope
block_coalBlockStraightSlopeBlockID = float(39.50) # A normal coal block slope
block_steelBlockCurvedSlopeBlockID = float(39.51) # A curved steel block slope
block_steelBlockStraightSlopeBlockID = float(39.52) # A normal steel block slope
block_tinBlockCurvedSlopeBlockID = float(39.53) # A curved tin block slope
block_tinBlockStraightSlopeBlockID = float(39.54) # A normal tin block slope
block_aluminumBlockCurvedSlopeBlockID = float(39.55) # A curved aluminum block slope
block_aluminumBlockStraightSlopeBlockID = float(39.56) # A normal aluminum block slope
block_bronzeBlockCurvedSlopeBlockID = float(39.57) # A curved bronze block slope
block_bronzeBlockStraightSlopeBlockID = float(39.58) # A normal bronze block slope
block_titaniumBlockCurvedSlopeBlockID = float(39.59) # A curved titanium block slope
block_titaniumBlockStraightSlopeBlockID = float(39.60) # A normal titanium block slope
block_redBrickBlockCurvedSlopeBlockID = float(39.61) # A curved red brick block slope
block_redBrickBlockStraightSlopeBlockID = float(39.62) # A normal red brick block slope
block_oakWoodPlankBlockCurvedSlopeBlockID = float(39.63) # A curved oak wood plank block slope
block_oakWoodPlankBlockStraightSlopeBlockID = float(39.64) # A normal oak wood plank block slope
block_oakWoodLogBlockCurvedSlopeBlockID = float(39.65) # A curved oak wood log block slope
block_oakWoodLogBlockStraightSlopeBlockID = float(39.66) # A normal oak wood log block slope
block_strippedOakWoodPlankBlockCurvedSlopeBlockID = float(39.67) # A curved stripped oak wood plank block slope
block_strippedOakWoodPlankBlockStraightSlopeBlockID = float(39.68) # A normal stripped oak wood plank block slope
block_strippedOakWoodLogBlockCurvedSlopeBlockID = float(39.69) # A curved stripped oak wood log block slope
block_strippedOakWoodLogBlockStraightSlopeBlockID = float(39.70) # A normal stripped oak wood log block slope
block_darkOakWoodPlankBlockCurvedSlopeBlockID = float(39.71) # A curved dark oak wood plank block slope
block_darkOakWoodPlankBlockStraightSlopeBlockID = float(39.72) # A normal dark oak wood plank block slope
block_darkOakWoodLogBlockCurvedSlopeBlockID = float(39.73) # A curved dark oak wood log block slope
block_darkOakWoodLogBlockStraightSlopeBlockID = float(39.74) # A normal dark oak wood log block slope
block_strippedDarkOakWoodPlankBlockCurvedSlopeBlockID = float(39.75) # A curved stripped  dark oak wood plank block slope
block_strippedDarkOakWoodPlankBlockStraightSlopeBlockID = float(39.76) # A normal stripped dark oak wood plank block slope
block_strippedDarkOakWoodLogBlockCurvedSlopeBlockID = float(39.77) # A curved stripped dark oak wood log block slope
block_strippedDarkOakWoodLogBlockStraightSlopeBlockID = float(39.78) # A normal stripped dark oak wood log block slope
block_birchWoodPlankBlockCurvedSlopeBlockID = float(39.79) # A curved birch wood plank block slope
block_birchWoodPlankBlockStraightSlopeBlockID = float(39.80) # A normal birch wood plank block slope
block_birchWoodLogBlockCurvedSlopeBlockID = float(39.81) # A curved birch wood log block slope
block_birchWoodLogBlockStraightSlopeBlockID = float(39.82) # A normal birch wood log block slope
block_strippedBirchWoodPlankBlockCurvedSlopeBlockID = float(39.83) # A curved stripped birch wood plank block slope
block_strippedBirchWoodPlankBlockStraightSlopeBlockID = float(39.84) # A normal stripped birch wood plank block slope
block_strippedBirchWoodLogBlockCurvedSlopeBlockID = float(39.85) # A curved stripped birch wood log block slope
block_strippedBirchWoodLogBlockStraightSlopeBlockID = float(39.86) # A normal stripped birch wood log block slope
block_acaciaWoodPlankBlockCurvedSlopeBlockID = float(39.87) # A curved acacia wood plank block slope
block_acaciaWoodPlankBlockStraightSlopeBlockID = float(39.88) # A normal acacia wood plank block slope
block_acaciaWoodLogBlockCurvedSlopeBlockID = float(39.89) # A curved acacia wood log block slope
block_acaciaWoodLogBlockStraightSlopeBlockID = float(39.90) # A normal acacia wood log block slope
block_strippedAcaciaWoodPlankBlockCurvedSlopeBlockID = float(39.91) # A curved stripped acacia wood plank block slope
block_strippedAcaciaWoodPlankBlockStraightSlopeBlockID = float(39.92) # A normal stripped acacia wood plank block slope
block_strippedAcaciaWoodLogBlockCurvedSlopeBlockID = float(39.93) # A curved stripped acacia wood log block slope
block_strippedAcaciaWoodLogBlockStraightSlopeBlockID = float(39.94) # A normal stripped acacia wood log block slope
block_jungleWoodPlankBlockCurvedSlopeBlockID = float(39.95) # A curved acacia wood plank block slope
block_jungleWoodPlankBlockStraightSlopeBlockID = float(39.96) # A normal jungle wood plank block slope
block_jungleWoodLogBlockCurvedSlopeBlockID = float(39.97) # A curved jungle wood log block slope
block_jungleWoodLogBlockStraightSlopeBlockID = float(39.98) # A normal jungle wood log block slope
block_strippedJungleWoodPlankBlockCurvedSlopeBlockID = float(39.99) # A curved stripped jungle wood plank block slope
block_strippedJungleWoodPlankBlockStraightSlopeBlockID = float(39.100) # A normal stripped jungle wood plank block slope
block_strippedJungleWoodLogBlockCurvedSlopeBlockID = float(39.101) # A curved stripped jungle wood log block slope
block_strippedJungleWoodLogBlockStraightSlopeBlockID = float(39.102) # A normal stripped jungle wood log block slope
block_spruceWoodPlankBlockCurvedSlopeBlockID = float(39.103) # A curved spruce wood plank block slope
block_spruceWoodPlankBlockStraightSlopeBlockID = float(39.104) # A normal spruce wood plank block slope
block_spruceWoodLogBlockCurvedSlopeBlockID = float(39.105) # A curved spruce wood log block slope
block_spruceWoodLogBlockStraightSlopeBlockID = float(39.106) # A normal spruce wood log block slope
block_strippedSpruceWoodPlankBlockCurvedSlopeBlockID = float(39.107) # A curved stripped spruce wood plank block slope
block_strippedSpruceWoodPlankBlockStraightSlopeBlockID = float(39.108) # A normal stripped spruce wood plank block slope
block_strippedSpruceWoodLogBlockCurvedSlopeBlockID = float(39.109) # A curved stripped spruce wood log block slope
block_strippedSpruceWoodLogBlockStraightSlopeBlockID = float(39.110) # A normal stripped spruce wood log block slope
block_cherryWoodPlankBlockCurvedSlopeBlockID = float(39.111) # A curved cherry wood plank block slope
block_cherryWoodPlankBlockStraightSlopeBlockID = float(39.112) # A normal cherry wood plank block slope
block_cherryWoodLogBlockCurvedSlopeBlockID = float(39.113) # A curved cherry wood log block slope
block_cherryWoodLogBlockStraightSlopeBlockID = float(39.114) # A normal cherry wood log block slope
block_strippedCherryWoodPlankBlockCurvedSlopeBlockID = float(39.115) # A curved stripped cherry wood plank block slope
block_strippedCherryWoodPlankBlockStraightSlopeBlockID = float(39.116) # A normal stripped cherry wood plank block slope
block_strippedCherryWoodLogBlockCurvedSlopeBlockID = float(39.117) # A curved stripped cherry wood log block slope
block_strippedCherryWoodLogBlockStraightSlopeBlockID = float(39.118) # A normal stripped cherry wood log block slope
block_ashWoodPlankBlockCurvedSlopeBlockID = float(39.119) # A curved ash wood plank block slope
block_ashWoodPlankBlockStraightSlopeBlockID = float(39.120) # A normal ash wood plank block slope
block_ashWoodLogBlockCurvedSlopeBlockID = float(39.121) # A curved ash wood log block slope
block_ashWoodLogBlockStraightSlopeBlockID = float(39.122) # A normal ash wood log block slope
block_strippedAshWoodPlankBlockCurvedSlopeBlockID = float(39.123) # A curved stripped ash wood plank block slope
block_strippedAshWoodPlankBlockStraightSlopeBlockID = float(39.124) # A normal stripped ash wood plank block slope
block_strippedAshWoodLogBlockCurvedSlopeBlockID = float(39.125) # A curved stripped ash wood log block slope
block_strippedAshWoodLogBlockStraightSlopeBlockID = float(39.126) # A normal stripped ash wood log block slope
block_locustWoodPlankBlockCurvedSlopeBlockID = float(39.127) # A curved locust wood plank block slope
block_locustWoodPlankBlockStraightSlopeBlockID = float(39.128) # A normal locust wood plank block slope
block_locustWoodLogBlockCurvedSlopeBlockID = float(39.129) # A curved locust wood log block slope
block_locustWoodLogBlockStraightSlopeBlockID = float(39.130) # A normal locust wood log block slope
block_strippedLocustWoodPlankBlockCurvedSlopeBlockID = float(39.131) # A curved stripped locust wood plank block slope
block_strippedLocustWoodPlankBlockStraightSlopeBlockID = float(39.132) # A normal stripped locust wood plank block slope
block_strippedLocustWoodLogBlockCurvedSlopeBlockID = float(39.133) # A curved stripped locust wood log block slope
block_strippedLocustWoodLogBlockStraightSlopeBlockID = float(39.134) # A normal stripped locust wood log block slope
block_appleWoodPlankBlockCurvedSlopeBlockID = float(39.135) # A curved apple wood plank block slope
block_appleWoodPlankBlockStraightSlopeBlockID = float(39.136) # A normal apple wood plank block slope
block_appleWoodLogBlockCurvedSlopeBlockID = float(39.137) # A curved apple wood log block slope
block_appleWoodLogBlockStraightSlopeBlockID = float(39.138) # A normal apple wood log block slope
block_strippedAppleWoodPlankBlockCurvedSlopeBlockID = float(39.139) # A curved stripped apple wood plank block slope
block_strippedAppleWoodPlankBlockStraightSlopeBlockID = float(39.140) # A normal stripped apple wood plank block slope
block_strippedAppleWoodLogBlockCurvedSlopeBlockID = float(39.141) # A curved stripped apple wood log block slope
block_strippedAppleWoodLogBlockStraightSlopeBlockID = float(39.142) # A normal stripped apple wood log block slope
block_pineWoodPlankBlockCurvedSlopeBlockID = float(39.143) # A curved pine wood plank block slope
block_pineWoodPlankBlockStraightSlopeBlockID = float(39.144) # A normal pine wood plank block slope
block_pineWoodLogBlockCurvedSlopeBlockID = float(39.145) # A curved pine wood log block slope
block_pineWoodLogBlockStraightSlopeBlockID = float(39.146) # A normal pine wood log block slope
block_strippedPineWoodPlankBlockCurvedSlopeBlockID = float(39.147) # A curved stripped pine wood plank block slope
block_strippedPineWoodPlankBlockStraightSlopeBlockID = float(39.148) # A normal stripped pine wood plank block slope
block_strippedPineWoodLogBlockCurvedSlopeBlockID = float(39.149) # A curved stripped pine wood log block slope
block_strippedPineWoodLogBlockStraightSlopeBlockID = float(39.150) # A normal stripped pine wood log block slope
block_palmWoodPlankBlockCurvedSlopeBlockID = float(39.151) # A curved palm wood plank block slope
block_palmWoodPlankBlockStraightSlopeBlockID = float(39.152) # A normal palm wood plank block slope
block_palmWoodLogBlockCurvedSlopeBlockID = float(39.153) # A curved palm wood log block slope
block_palmWoodLogBlockStraightSlopeBlockID = float(39.154) # A normal palm wood log block slope
block_strippedPalmWoodPlankBlockCurvedSlopeBlockID = float(39.155) # A curved stripped palm wood plank block slope
block_strippedPalmWoodPlankBlockStraightSlopeBlockID = float(39.156) # A normal stripped palm wood plank block slope
block_strippedPalmWoodLogBlockCurvedSlopeBlockID = float(39.157) # A curved stripped palm wood log block slope
block_strippedPalmWoodLogBlockStraightSlopeBlockID = float(39.158) # A normal stripped palm wood log block slope
block_sycamoreWoodPlankBlockCurvedSlopeBlockID = float(39.159) # A curved sycamore wood plank block slope
block_sycamoreWoodPlankBlockStraightSlopeBlockID = float(39.160) # A normal sycamore wood plank block slope
block_sycamoreWoodLogBlockCurvedSlopeBlockID = float(39.161) # A curved sycamore wood log block slope
block_sycamoreWoodLogBlockStraightSlopeBlockID = float(39.162) # A normal sycamore wood log block slope
block_strippedSycamoreWoodPlankBlockCurvedSlopeBlockID = float(39.163) # A curved stripped sycamore wood plank block slope
block_strippedSycamoreWoodPlankBlockStraightSlopeBlockID = float(39.164) # A normal stripped sycamore wood plank block slope
block_strippedSycamoreWoodLogBlockCurvedSlopeBlockID = float(39.165) # A curved stripped sycamore wood log block slope
block_strippedSycamoreWoodLogBlockStraightSlopeBlockID = float(39.166) # A normal stripped sycamore wood log block slope
block_acornWoodPlankBlockCurvedSlopeBlockID = float(39.165) # A curved acorn wood plank block slope
block_acornWoodPlankBlockStraightSlopeBlockID = float(39.166) # A normal acorn wood plank block slope
block_acornWoodLogBlockCurvedSlopeBlockID = float(39.167) # A curved acorn wood log block slope
block_acornWoodLogBlockStraightSlopeBlockID = float(39.168) # A normal acorn wood log block slope
block_strippedAcornWoodPlankBlockCurvedSlopeBlockID = float(39.169) # A curved stripped acorn wood plank block slope
block_strippedAcornWoodPlankBlockStraightSlopeBlockID = float(39.170) # A normal stripped acorn wood plank block slope
block_strippedAcornWoodLogBlockCurvedSlopeBlockID = float(39.171) # A curved stripped acorn wood log block slope
block_strippedAcornWoodLogBlockStraightSlopeBlockID = float(39.172) # A normal stripped acorn wood log block slope
block_boneBlockCurvedSlopeID = float(39.173) # A normal curved bone block slope
block_boneBlockStraightSlopeID = float(39.174) # A normal bone block slope
# Custom wood types: Cherry, Ash, Locust, Apple, Pine, Palm, Acorn, Sycamore
''' Strong ''' # Category 41
""" For reinforced and compact blocks """
block_reinforcedGlassBlockID = float(40.1) # Stronger glass block. 9x harder to break than a normal glass block
block_compactGlassBlockID = float(40.2) # Very strong glass block. 9x harder to break than a reinforced glass block. It is as strong as normal obsidian, and is explosion proof
block_reinforcedObsidianBlockID = float(40.3) # Stronger obsidian block. 9x harder to break than a normal obsidian block. Requires diamond pickaxe with efficiency 9 to break at the same speed of a normal obsidian block
block_compactObsidianBlockID = float(40.4) # Very strong obsidian block. 9x harder to break than a reinforced obsidian block. Wither proof, along with all mob proof. Takes over an hour to mine with your first.
block_reinforcedIronBlockID = float(40.5) # Stronger iron block. 9x harder to break than a normal iron block
block_compactIronBlockID = float(40.6) # Very strong iron block. 9x harder to break than a reinforced iron block. Explosion proof.
block_reinforcedSteelBlockID = float(40.7) # Stronger steel block. 9x harder to break than a normal steel block
block_compactSteelBlockID = float(40.8) # Very strong steel block. 9x harder to break than a reinforced steel block. Explosion proof.
block_reinforcedTitaniumBlockID = float(40.9) # Stronger titanium block. 9x harder to break than a normal titanium block
block_compactTitaniumBlockID = float(40.10) # Very strong titanium block. 9x harder to break than a reinforced titanium block. Explosion proof.
block_reinforcedGoldBlockID = float(40.11)
block_compactGoldBlockID = float(40.12)
block_reinforcedBronzeBlockID = float(40.13)
block_compactBronzeBlockID = float(40.14)
block_reinforcedSoulSandBlockID = float(40.15)
block_compactSoulSandBlockID = float(40.16)
block_reinforcedNetherrackBlockID = float(40.17) # Stronger netherrack that now has the durability of normal cave stone. 9x harder to break than normal netherrack
block_compactNetherrackBlockID = float(40.18) # Very strong nethttack block. Now has half the durability of obsidian. 9x harder to break than reinforced netherrack
block_reinforcedMagmaBlockID = float(40.19)
block_compactMagmaBlockID = float(40.20)
block_reinforcedDirtBlockID = float(40.21)
block_compactDirtBlockID = float(40.22)
block_reinforcedLapisLazuliBlockID = float(40.23)
block_compactLapisLazuliBlockID = float(40.24)
block_reinforcedEmeraldBlockID = float(40.25)
block_compactEmeraldBlockID = float(40.26)
block_reinforcedRedstoneBlockID = float(40.27)
block_compactRedstoneBlockID = float(40.28)
block_reinforcedEndStoneBlockID = float(40.29)
block_compactEndStoneBlockID = float(40.30)
block_reinforcedCaveStoneBlockID = float(40.31)
block_compactCaveStoneBlockID = float(40.32)
block_reinforcedDiamondBlockID = float(40.33)
block_compactDiamondBlockID = float(40.34)
block_reinforcedTinBlockID = float(40.35)
block_compactTinBlockID = float(40.36)
block_reinforcedYellowSandstoneBlockID = float(40.37)
block_compactYellowSandstoneBlockID = float(40.38)
block_reinforcedRedSandstoneBlockID = float(40.39)
block_compactRedSandstoneBlockID = float(40.40)
block_reinforcedQuartzBlockID = float(40.41)
block_compactQuartzBlockID = float(40.42)
block_reinforcedRubyBlockID = float(40.43)
block_compactRubyBlockID = float(40.44)
block_reinforcedSapphireBlockID = float(40.45)
block_compactSapphireBlockID = float(40.46)
block_reinforcedBoneBlockID = float(40.47)
block_compactBoneBlockID = float(40.48)
block_reinforcedStoneBrickBlockID = float(40.49)
block_compactStoneBrickBlockID = float(40.50)
block_reinforcedPurPurBlockID = float(40.51)
block_compactPurPurBlockID = float(40.52)
''' Industrial ''' # Category 42
block_blackRubberBlockID = float(41.1)
block_whiteRubberBlockID = float(41.2)
block_greyRubberBlockID = float(41.3)
block_lightGreyRubberBlockID = float(41.4)
block_darkGreyRubberBlockID = float(41.5)
''' More Nature ''' # Category 43 (needs to be added to DB)
block_honeyCombBlockID = float(42.1)
block_honeyBlockID = float(42.2)
block_beehiveBlockID = float(42.3)
block_beehiveWithHoneyBlockID = float(42.4)
block_beenestBlockID = float(42.5)
''' Others ''' # Category xx
block_hayBaleBlockID = float(100.1)
block_slimeBlockID = float(100.2)
block_untexturedBlockID = float(100.3) # Untextured blocks have the black and purple checkers texture. If a graphics driver were to crash in this game, a message would show up upon realization of the error, or loading the world. These items can be crafted with a concrete block/slab/staircase/wooden door, purple dye, black dye, and an eye of ender
block_untexturedStaircaseID = float(100.4)
block_untexturedSlabID = float(100.5)
block_untexturedDoorID = float(100.6)
block_redbarrierID = float(100.7) # blocks all
block_blueBarrierID = float(100.8) # semisolid
block_greenBarrierID = float(100.9) # arrows, tridents, etc pass through, players and mobs don't
block_yellowBarrierID = float(100.10) # only mobs can get through
block_orangeBarrierID = float(100.11) # blocks all, but can fall right through it, timer included to activate the drop
block_redstoneBarrierID = float(100.12) # becomes transparent when activated by redstone, goes solid when no redstone signal is available, and blocks all Can be moved my pistons.
''' Block count '''
# Category 1:
cat1Count = int(14)
# Category 2:
cat2Count = int(31)
# Category 3:
cat3Count = int(90)
# Category 4:
cat4Count = int(104)
# Category 5:
cat5Count = int(14)
# Category 6:
cat6Count = int(16)
# Category 7:
cat7Count = int(7)
# Category 8:
cat8Count = int(75)
# Category 9:
cat9Count = int(6)
# Category 10:
cat10Count = int(4)
# Category 11:
cat11Count = int(103)
# Category 12:
cat12Count = int(72)
# Category 13:
cat13Count = int(7)
# Category 14:
cat14Count = int(33)
# Category 15:
cat15Count = int(1)
# Category 16:
cat16Count = int(8)
# Category 17:
cat17Count = int(1)
# Category 18:
cat18Count = int(17)
# Category 19:
cat19Count = int(42)
# Category 20:
cat20Count = int(75)
# Category 21:
cat21Count = int(11)
# Category 22:
cat22Count = int(212)
# Category 23:
cat23Count = int(3)
# Category 24:
cat24Count = int(14)
# Category 25:
cat25Count = int(32)
# Category 26:
cat26Count = int(2)
# Category 27:
cat27Count = int(5)
# Category 28:
cat28Count = int(46)
# Category 29:
cat29Count = int(33)
# Category 30:
cat30Count = int(3)
# Category 31:
cat31Count = int(277)
# Category 32:
cat32Count = int(9)
# Category 33:
cat33Count = int(4)
# Category 34:
cat34Count = int(5)
# Category 35:
cat35Count = int(16)
# Category 36
cat36Count = int(17)
# Category 37
cat37Count = int(14)
# Category 38
cat38Count = int(93)
# Category 39
cat39Count = int(15)
# Cateogyr 40
cat40Count = int(174)
# Category 41
cat41Count = int(52)
# Category 42
cat42Count = int(5)
# Category 43
cat43Count = int(0)
# Category 44
cat44Count = int(0)
# Category 45
cat45Count = int(0)
# Category 46
cat46Count = int(0)
# Category 47
cat47Count = int(0)
# Category 48
cat48Count = int(0)
# Category 49
cat49Count = int(0)
# Category 50
cat50Count = int(0)
# Category 51
cat51Count = int(0)
# Category 52
cat52Count = int(0)
# Category 53
cat53Count = int(0)
# Category 54
cat54Count = int(0)
# Category 55
cat55Count = int(0)
# Category 56
cat56Count = int(0)
# Category 57
cat57Count = int(0)
# Category 58
cat58Count = int(0)
# Category 59
cat59Count = int(0)
# Category 60
cat60Count = int(0)
# Category 61
cat61Count = int(0)
# Category 62
cat62Count = int(0)
# Category 63
cat63Count = int(0)
# Category 64
cat64Count = int(0)
# Category 65
cat65Count = int(0)
# Category 66
cat66Count = int(0)
# Category 67
cat67Count = int(0)
# Category 68
cat68Count = int(0)
# Category 69
cat69Count = int(0)
# Category 70
cat70Count = int(0)
# Category 71
cat71Count = int(0)
# Category 72
cat72Count = int(0)
# Category 73
cat73Count = int(0)
# Category 74
cat74Count = int(0)
# Category 75
cat75Count = int(0)
# Category 76
cat76Count = int(0)
# Category 77
cat77Count = int(0)
# Category 78
cat78Count = int(0)
# Category 79
cat79Count = int(0)
# Category 80
cat80Count = int(0)
# Category 81
cat81Count = int(0)
# Category 82
cat82Count = int(0)
# Category 83
cat83Count = int(0)
# Category 84
cat84Count = int(0)
# Category 85
cat85Count = int(0)
# Category 86
cat86Count = int(0)
# Category 87
cat87Count = int(0)
# Category 88
cat88Count = int(0)
# Category 89
cat89Count = int(0)
# Category 90
cat90Count = int(0)
# Category 91
cat91Count = int(0)
# Category 92
cat92Count = int(0)
# Category 93
cat93Count = int(0)
# Category 94
cat94Count = int(0)
# Category 95
cat95Count = int(0)
# Category 96
cat96Count = int(0)
# Category 97
cat97Count = int(0)
# Category 98
cat98Count = int(0)
# Category 99
cat99Count = int(0)
# Category 100
cat100Count = int(0)
# Category Z:
catZCount = int(12)
''' Total block count '''
blockCount = int(cat1Count + cat2Count + cat3Count + cat4Count + cat5Count + cat6Count + cat7Count + cat8Count + cat9Count + cat10Count + cat11Count + cat12Count + cat13Count + cat14Count + cat15Count + cat16Count + cat17Count + cat18Count + cat19Count + cat20Count + cat21Count + cat22Count + cat23Count + cat24Count + cat25Count + cat26Count + cat27Count + cat28Count + cat29Count + cat30Count + cat31Count + cat32Count + cat33Count + cat34Count + cat35Count + cat36Count + cat37Count + cat38Count + cat39Count + cat40Count + cat41Count + catZCount)
# Current total: 01,.742 blocks
''' File info '''
print ("This is a ID resource file for block IDs. Modifying this file can cause the game to stop working properly if not properly configured")
print ("This is an important game resource file. Be careful when using it.")
print ("There is a total number of " + str(blockCount) + " blocks in this list")
catInfo = str(input("Type in the letter b to view the block listing in categories"))
catInfo = catInfo.upper() # Makes the input an uppercase letter
if (catInfo == "B"): # Even if you type it lowercase, it will still count with the upper() method
	print ("Category 1") # Category 1 blocks
	print ("Category name: dirt")
	print ("Block count: " + str(cat1Count))
	moreInfo1 = input("Press [ENTER] key to see category 1 block listing")
	print ("Block listing: ")
	print ("Dirt block | ID: block_dirtID | Number ID: integer (1) ")
	print ("Coarse Dirt | ID: block_coarseDirtID | Number ID: integer (2) ")
	print ("Podzol | ID: block_podzolID | Number ID: integer (3) ")
	print ("Mycelium | ID: block_myceliumID | Number ID: integer (4) ")
	print ("Grasspath | ID: block_grassPathID | Number ID: integer (5) ")
	more2 = input("View 5 more? [ENTER]")
	print ("Fertile dirt | ID: block_fertileDirtID | Number ID: integer (6) ")
	print ("Wet Fertile dirt | ID: block_wetFertileDirtID | Number ID: integer (7) ")
	print ("Swamp Grass Dirt | ID: block_swampGrassDirtID | Number ID: integer (8) ")
	print ("Grass Block | ID: block_grassBlockID | Number ID: integer (9) ")
	print ("Dead Grass Block | ID: block_deadGrassBlockID | Number ID: integer (10) ")
	more2 = input("View 5 more? [ENTER]")
	print ("Wither grass | ID: block_witherGrassBlockID | Number ID: integer (11) ")
	print ("List is complete")
	moreInfo1 = input("Press [ENTER] key to view category 2")
	print ("Category 2") # Category 2 Blocks
	print ("Block count: " + str(cat2Count))
	moreInfo1 = input("Press [ENTER] key to see category 2 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 3")
	print ("Category 3") # Category 3 Blocks
	print ("Block count: " + str(cat3Count))
	moreInfo1 = input("Press [ENTER] key to see category 3 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 4")
	print ("Category 4") # Category 4 Blocks
	print ("Category name: stairs")
	print ("Block count: " + str(cat4Count))
	moreInfo1 = input("Press [ENTER] key to see category 4 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 4")
	print ("Category 5") # Category 5 Blocks
	print ("Block count: " + str(cat5Count))
	moreInfo1 = input("Press [ENTER] key to see category 5 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 6")
	print ("Category 6") # Category 6 Blocks
	print ("Block count: " + str(cat6Count))
	moreInfo1 = input("Press [ENTER] key to see category 6 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 7")
	print ("Category 7") # Category 7 Blocks
	print ("Block count: " + str(cat7Count))
	moreInfo1 = input("Press [ENTER] key to see category 7 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 8")
	print ("Category 8") # Category 8 Blocks
	print ("Block count: " + str(cat8Count))
	moreInfo1 = input("Press [ENTER] key to see category 8 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 9")
	print ("Category 9") # Category 9 Blocks
	print ("Block count: " + str(cat9Count))
	moreInfo1 = input("Press [ENTER] key to see category 9 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 10")
	print ("Category 10") # Category 10 Blocks
	print ("Block count: " + str(cat10Count))
	moreInfo1 = input("Press [ENTER] key to see category 10 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 11")
	print ("Category 11") # Category 11 Blocks
	print ("Block count: " + str(cat11Count))
	moreInfo1 = input("Press [ENTER] key to see category 11 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 12")
	print ("Category 12") # Category 12 Blocks
	print ("Block count: " + str(cat12Count))
	moreInfo1 = input("Press [ENTER] key to see category 12 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 13")
	print ("Category 13") # Category 13 Blocks
	print ("Block count: " + str(cat13Count))
	moreInfo1 = input("Press [ENTER] key to see category 13 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 14")
	print ("Category 14") # Category 14 Blocks
	print ("Block count: " + str(cat14Count))
	moreInfo1 = input("Press [ENTER] key to see category 14 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 15")
	print ("Category 15") # Category 15 Blocks
	print ("Block count: " + str(cat15Count))
	moreInfo1 = input("Press [ENTER] key to see category 15 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 16")
	print ("Category 16") # Category 16 Blocks
	print ("Block count: " + str(cat16Count))
	moreInfo1 = input("Press [ENTER] key to see category 16 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 17")
	print ("Category 17") # Category 17 Blocks
	print ("Block count: " + str(cat17Count))
	moreInfo1 = input("Press [ENTER] key to see category 17 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 18")
	print ("Category 18") # Category 18 Blocks
	print ("Block count: " + str(cat18Count))
	moreInfo1 = input("Press [ENTER] key to see category 18 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 19")
	print ("Category 19") # Category 19 Blocks
	print ("Block count: " + str(cat19Count))
	moreInfo1 = input("Press [ENTER] key to see category 19 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 20")
	print ("Category 20") # Category 20 Blocks
	print ("Block count: " + str(cat20Count))
	moreInfo1 = input("Press [ENTER] key to see category 20 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 21")
	print ("Category 21") # Category 21 Blocks
	print ("Block count: " + str(cat21Count))
	moreInfo1 = input("Press [ENTER] key to see category 21 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 22")
	print ("Category 22") # Category 22 Blocks
	print ("Block count: " + str(cat22Count))
	moreInfo1 = input("Press [ENTER] key to see category 22 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 3")
	print ("Category 23") # Category 23 Blocks
	print ("Block count: " + str(cat23Count))
	moreInfo1 = input("Press [ENTER] key to see category 23 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 24")
	print ("Category 24") # Category 24 Blocks
	print ("Block count: " + str(cat24Count))
	moreInfo1 = input("Press [ENTER] key to see category 24 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 25")
	print ("Category 25") # Category 25 Blocks
	print ("Block count: " + str(cat25Count))
	moreInfo1 = input("Press [ENTER] key to see category 25 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 26")
	print ("Category 26") # Category 26 Blocks
	print ("Block count: " + str(cat26Count))
	moreInfo1 = input("Press [ENTER] key to see category 26 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 27")
	print ("Category 27") # Category 27 Blocks
	print ("Block count: " + str(cat27Count))
	moreInfo1 = input("Press [ENTER] key to see category 27 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 28")
	print ("Category 28") # Category 28 Blocks
	endOfMoreInfoBlockList = input("You have reached the end of this files info. The rest of this file is for the game to handle. Please run the game to see what this file does")
	print ("Block count: " + str(cat28Count))
	moreInfo1 = input("Press [ENTER] key to see category 28 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 29")
	print ("Category 29") # Category 29 Blocks
	print ("Block count: " + str(cat29Count))
	moreInfo1 = input("Press [ENTER] key to see category 30 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 30")
	print ("Category 30") # Category 30 Blocks
	print ("Block count: " + str(cat30Count))
	moreInfo1 = input("Press [ENTER] key to see category 30 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 31")
	print ("Category 31") # Category 31 Blocks
	print ("Block count: " + str(cat31Count))
	moreInfo1 = input("Press [ENTER] key to see category 31 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 32")
	print ("Category 32") # Category 32 Blocks
	print ("Block count: " + str(cat32Count))
	moreInfo1 = input("Press [ENTER] key to see category 32 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 33")
	print ("Category 33") # Category 33 Blocks
	print ("Block count: " + str(cat33Count))
	moreInfo1 = input("Press [ENTER] key to see category 33 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 34")
	print ("Category 34") # Category 34 Blocks
	print ("Block count: " + str(cat34Count))
	moreInfo1 = input("Press [ENTER] key to see category 34 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 35")
	print ("Category 35") # Category 35 Blocks
	print ("Block count: " + str(cat35Count))
	moreInfo1 = input("Press [ENTER] key to see category 35 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 36")
	print ("Category 36") # Category 36 Blocks
	print ("Block count: " + str(cat36Count))
	moreInfo1 = input("Press [ENTER] key to see category 36 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to view category 37")
	print ("Category 37") # Category 37 Blocks
	print ("Block count: " + str(cat37Count))
	moreInfo1 = input("Press [ENTER] key to see category 37 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 38")
	print ("Category 38") # Category 38 Blocks
	print ("Block count: " + str(cat38Count))
	moreInfo1 = input("Press [ENTER] key to see category 38 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 39")
	print ("Category 39") # Category 39 Blocks
	print ("Block count: " + str(cat39Count))
	moreInfo1 = input("Press [ENTER] key to see category 39 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 40")
	# Category 40 insert here
	print ("Category 40") # Category 40 Blocks
	print ("Block count: " + str(cat40Count))
	moreInfo1 = input("Press [ENTER] key to see category 40 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 41")
	# Category 41 insert here
	print ("Category 41") # Category 41 Blocks
	print ("Block count: " + str(cat41Count))
	moreInfo1 = input("Press [ENTER] key to see category 41 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 42")
	# Category 42 insert here
	'''
	print ("Category 42") # Category 42 Blocks
	print ("Block count: " + str(cat42Count))
	moreInfo1 = input("Press [ENTER] key to see category 42 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 43")
	'''
	# Category 43 insert here
	'''
	print ("Category 43") # Category 43 Blocks
	print ("Block count: " + str(cat43Count))
	moreInfo1 = input("Press [ENTER] key to see category 43 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 44")
	'''
	# Category 44 insert here
	'''
	print ("Category 44") # Category 44 Blocks
	print ("Block count: " + str(cat44Count))
	moreInfo1 = input("Press [ENTER] key to see category 44 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 45")
	'''
	# Category 45 insert here
	'''
	print ("Category 45") # Category 45 Blocks
	print ("Block count: " + str(cat45Count))
	moreInfo1 = input("Press [ENTER] key to see category 45 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 46")
	'''
	# Category 46 insert here
	'''
	print ("Category 46") # Category 46 Blocks
	print ("Block count: " + str(cat46Count))
	moreInfo1 = input("Press [ENTER] key to see category 46 block listing")
	print ("Block listing: ")
	print ("Unavailable"(
	moreInfo1 = input("Press [ENTER] key to see category 47")
	'''
	# Category 47 insert here
	'''
	print ("Category 47") # Category 47 Blocks
	print ("Block count: " + str(cat47Count))
	moreInfo1 = input("Press [ENTER] key to see category 47 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 48")
	'''
	# Category 48 insert here
	'''
	print ("Category 48") # Category 48 Blocks
	print ("Block count: " + str(cat48Count))
	moreInfo1 = input("Press [ENTER] key to see category 48 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 49")
	'''
	# Category 49 insert here
	'''
	print ("Category 49") # Category 49 Blocks
	print ("Block count: " + str(cat49Count))
	moreInfo1 = input("Press [ENTER] key to see category 49 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 50")
	'''
	# Category 50 insert here
	'''
	print ("Category 50") # Category 50 Blocks
	print ("Block count: " + str(cat50Count))
	moreInfo1 = input("Press [ENTER] key to see category 50 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 51")
	'''
	# Category 51 insert here
	'''
	print ("Category 51") # Category 51 Blocks
	print ("Block count: " + str(cat51Count))
	moreInfo1 = input("Press [ENTER] key to see category 51 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 52")
	'''
	# Category 52 insert here
	'''
	print ("Category 52") # Category 52 Blocks
	print ("Block count: " + str(cat52Count))
	moreInfo1 = input("Press [ENTER] key to see category 52 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 53")
	'''
	# Category 53 insert here
	'''
	print ("Category 53") # Category 53 Blocks
	print ("Block count: " + str(cat53Count))
	moreInfo1 = input("Press [ENTER] key to see category 53 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 54")
	'''
	# Category 54 insert here
	'''
	print ("Category 54") # Category 54 Blocks
	print ("Block count: " + str(cat54Count))
	moreInfo1 = input("Press [ENTER] key to see category 54 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 55")
	'''
	# Category 55 insert here
	'''
	print ("Category 55") # Category 55 Blocks
	print ("Block count: " + str(cat55Count))
	moreInfo1 = input("Press [ENTER] key to see category 55 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 56")
	'''
	# Category 56 insert here
	'''
	print ("Category 56") # Category 56 Blocks
	print ("Block count: " + str(cat56Count))
	moreInfo1 = input("Press [ENTER] key to see category 56 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 57")
	'''
	# Category 57 insert here
	'''
	print ("Category 57") # Category 57 Blocks
	print ("Block count: " + str(cat57Count))
	moreInfo1 = input("Press [ENTER] key to see category 57 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 58")
	'''
	# Category 58 insert here
	'''
	print ("Category 58") # Category 58 Blocks
	print ("Block count: " + str(cat58Count))
	moreInfo1 = input("Press [ENTER] key to see category 58 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 59")
	'''
	# Category 59 insert here
	'''
	print ("Category 59") # Category 59 Blocks
	print ("Block count: " + str(cat59Count))
	moreInfo1 = input("Press [ENTER] key to see category 59 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 60")
	'''
	# Category 60 insert here
	'''
	print ("Category 60") # Category 60 Blocks
	print ("Block count: " + str(cat60Count))
	moreInfo1 = input("Press [ENTER] key to see category 60 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 61")
	'''
	# Category 61 insert here
	'''
	print ("Category 61") # Category 61 Blocks
	print ("Block count: " + str(cat61Count))
	moreInfo1 = input("Press [ENTER] key to see category 61 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 62")
	'''
	# Category 62 insert here
	'''
	print ("Category 62") # Category 62 Blocks
	print ("Block count: " + str(cat62Count))
	moreInfo1 = input("Press [ENTER] key to see category 62 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 63")
	'''
	# Category 63 insert here
	'''
	print ("Category 63") # Category 63 Blocks
	print ("Block count: " + str(cat63Count))
	moreInfo1 = input("Press [ENTER] key to see category 63 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 64")
	'''
	# Category 64 insert here
	'''
	print ("Category 64") # Category 64 Blocks
	print ("Block count: " + str(cat64Count))
	moreInfo1 = input("Press [ENTER] key to see category 64 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 65")
	'''
	# Category 65 insert here
	'''
	print ("Category 65") # Category 65 Blocks
	print ("Block count: " + str(cat65Count))
	moreInfo1 = input("Press [ENTER] key to see category 65 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 66")
	'''
	# Category 66 insert here
	'''
	print ("Category 66") # Category 66 Blocks
	print ("Block count: " + str(cat66Count))
	moreInfo1 = input("Press [ENTER] key to see category 66 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 67")
	'''
	# Category 67 insert here
	'''
	print ("Category 67") # Category 67 Blocks
	print ("Block count: " + str(cat67Count))
	moreInfo1 = input("Press [ENTER] key to see category 67 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 68")
	'''
	# Category 68 insert here
	'''
	print ("Category 68") # Category 68 Blocks
	print ("Block count: " + str(cat68Count))
	moreInfo1 = input("Press [ENTER] key to see category 68 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 69")
	'''
	# Category 69 insert here
	'''
	print ("Category 69") # Category 69 Blocks
	print ("Block count: " + str(cat69Count))
	moreInfo1 = input("Press [ENTER] key to see category 69 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 70")
	'''
	# Category 70 insert here
	'''
	print ("Category 70") # Category 70 Blocks
	print ("Block count: " + str(cat70Count))
	moreInfo1 = input("Press [ENTER] key to see category 70 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 71")
	'''
	# Category 71 insert here
	'''
	print ("Category 71") # Category 71 Blocks
	print ("Block count: " + str(cat71Count))
	moreInfo1 = input("Press [ENTER] key to see category 71 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 72")
	'''
	# Category 72 insert here
	'''
	print ("Category 72") # Category 72 Blocks
	print ("Block count: " + str(cat72Count))
	moreInfo1 = input("Press [ENTER] key to see category 72 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 72")
	'''
	# Category 73 insert here
	'''
	print ("Category 73") # Category 73 Blocks
	print ("Block count: " + str(cat73Count))
	moreInfo1 = input("Press [ENTER] key to see category 73 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 74")
	'''
	# Category 74 insert here
	'''
	print ("Category 74") # Category 74 Blocks
	print ("Block count: " + str(cat74Count))
	moreInfo1 = input("Press [ENTER] key to see category 74 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 75")
	'''
	# Category 75 insert here
	'''
	print ("Category 75") # Category 75 Blocks
	print ("Block count: " + str(cat75Count))
	moreInfo1 = input("Press [ENTER] key to see category 75 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 76")
	'''
	# Category 76 insert here
	'''
	print ("Category 76") # Category 76 Blocks
	print ("Block count: " + str(cat76Count))
	moreInfo1 = input("Press [ENTER] key to see category 76 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 77")
	'''
	# Category 77 insert here
	'''
	print ("Category 77") # Category 77 Blocks
	print ("Block count: " + str(cat77Count))
	moreInfo1 = input("Press [ENTER] key to see category 77 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 78")
	'''
	# Category 78 insert here
	'''
	print ("Category 78") # Category 78 Blocks
	print ("Block count: " + str(cat78Count))
	moreInfo1 = input("Press [ENTER] key to see category 78 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 79")
	'''
	# Category 79 insert here
	'''
	print ("Category 79") # Category 79 Blocks
	print ("Block count: " + str(cat79Count))
	moreInfo1 = input("Press [ENTER] key to see category 79 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 80")
	'''
	# Category 80 insert here
	'''
	print ("Category 80") # Category 80 Blocks
	print ("Block count: " + str(cat80Count))
	moreInfo1 = input("Press [ENTER] key to see category 80 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 81")
	'''
	# Category 81 insert here
	'''
	print ("Category 81") # Category 81 Blocks
	print ("Block count: " + str(cat81Count))
	moreInfo1 = input("Press [ENTER] key to see category 81 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 82")
	'''
	# Category 82 insert here
	'''
	print ("Category 82") # Category 82 Blocks
	print ("Block count: " + str(cat82Count))
	moreInfo1 = input("Press [ENTER] key to see category 82 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 83")
	'''
	# Category 83 insert here
	'''
	print ("Category 83") # Category 83 Blocks
	print ("Block count: " + str(cat83Count))
	moreInfo1 = input("Press [ENTER] key to see category 83 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 84")
	'''
	# Category 84 insert here
	'''
	print ("Category 84") # Category 84 Blocks
	print ("Block count: " + str(cat84Count))
	moreInfo1 = input("Press [ENTER] key to see category 84 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 84")
	'''
	# Category 85 insert here
	'''
	print ("Category 85") # Category 85 Blocks
	print ("Block count: " + str(cat85Count))
	moreInfo1 = input("Press [ENTER] key to see category 85 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 86")
	'''
	# Category 86 insert here
	'''
	print ("Category 86") # Category 86 Blocks
	print ("Block count: " + str(cat86Count))
	moreInfo1 = input("Press [ENTER] key to see category 86 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 87")
	'''
	# Category 87 insert here
	'''
	print ("Category 87") # Category 87 Blocks
	print ("Block count: " + str(cat87Count))
	moreInfo1 = input("Press [ENTER] key to see category 87 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 88")
	'''
	# Category 88 insert here
	'''
	print ("Category 88") # Category 88 Blocks
	print ("Block count: " + str(cat88 Count))
	moreInfo1 = input("Press [ENTER] key to see category 88 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 89")
	'''
	# Category 89 insert here
	'''
	print ("Category 89") # Category 89 Blocks
	print ("Block count: " + str(cat89Count))
	moreInfo1 = input("Press [ENTER] key to see category 89 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 90")
	'''
	# Category 90 insert here
	'''
	print ("Category 90") # Category 90 Blocks
	print ("Block count: " + str(cat90Count))
	moreInfo1 = input("Press [ENTER] key to see category 90 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 91")
	'''
	# Category 91 insert here
	'''
	print ("Category 91") # Category 91 Blocks
	print ("Block count: " + str(cat91Count))
	moreInfo1 = input("Press [ENTER] key to see category 91 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 92")
	'''
	# Category 92 insert here
	'''
	print ("Category 92") # Category 92 Blocks
	print ("Block count: " + str(cat92Count))
	moreInfo1 = input("Press [ENTER] key to see category 92 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 93")
	'''
	# Category 93 insert here
	'''
	print ("Category 93") # Category 93 Blocks
	print ("Block count: " + str(cat93Count))
	moreInfo1 = input("Press [ENTER] key to see category 93 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 94")
	'''
	# Category 94 insert here
	'''
	print ("Category 94") # Category 94 Blocks
	print ("Block count: " + str(cat94Count))
	moreInfo1 = input("Press [ENTER] key to see category 94 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 95")
	'''
	# Category 95 insert here
	'''
	print ("Category 95") # Category 95 Blocks
	print ("Block count: " + str(cat95Count))
	moreInfo1 = input("Press [ENTER] key to see category 95 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 96")
	'''
	# Category 96 insert here
	'''
	print ("Category 96") # Category 96 Blocks
	print ("Block count: " + str(cat96Count))
	moreInfo1 = input("Press [ENTER] key to see category 96 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 97")
	'''
	# Category 97 insert here
	'''
	print ("Category 97") # Category 97 Blocks
	print ("Block count: " + str(cat97Count))
	moreInfo1 = input("Press [ENTER] key to see category 97 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 98")
	'''
	# Category 98 insert here
	'''
	print ("Category 98") # Category 98 Blocks
	print ("Block count: " + str(cat98Count))
	moreInfo1 = input("Press [ENTER] key to see category 98 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 99")
	'''
	# Category 99 insert here
	'''
	print ("Category 99") # Category 99 Blocks
	print ("Block count: " + str(cat99Count))
	moreInfo1 = input("Press [ENTER] key to see category 99 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category 100")
	'''
	# Category 100 insert here
	'''
	print ("Category 100") # Category 100 Blocks
	print ("Block count: " + str(cat100Count))
	moreInfo1 = input("Press [ENTER] key to see category 100 block listing")
	print ("Block listing: ")
	print ("Unavailable")
	moreInfo1 = input("Press [ENTER] key to see category Z")
	'''
	# Category Z
	moreInfo1 = input("Press [ENTER] key to view category Z")
	print ("Category Z") # Category Z Blocks
	print ("Category name: other")
	print ("Block count: " + str(catZCount))
	moreInfo1 = input("Press [ENTER] key to see category Z block listing")
	print ("Block listing: ")
	print ("Unavailable")
	endOfMoreInfoBlockList = input("You have reached the end of this files info. The rest of this file is for the game to handle. Please run the game to see what this file does")
noMore = input("Press [ENTER] key to exit this file")
print ("File exited")
print (">>> end")
''' File info '''
# Version: 20
# Language: Python 3.7.1 (Compatible with Python 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1)(not yet tested with Python 3.8/3.9)
# Size: 0,.122,.246 bytes (0,.122,.24 Kilobytes (base 10)) -base 2 calculation not available- (0,.122 Megabytes (base 10)) -base 2 calculation not available-
# Lines: 02,.059
# Unicode characters used: None
# Written with: notepad++ (7.5.9 (64 bit))
# Software group: FOSS (Free Open Source Software)
# Last modified: September 16th 2019
# Sharing status: share with anyone, don't claim as your own, don't sell for a profit
# Encoding: UNIX (LF) - Windows (CR) (LF) prior to version 20
''' End of file info '''
''' Move '''
# Section "items" moved to separate file on 7.22.2019
# Section "mobs" moved to separate file on 7.22.2019
''' ToDo '''
# make slabs and stairs of every block type
# Separate the files
# Get all 10 wood types of most items written in
""" End of script """
