# World parameters
''' Layout '''
# Layout section
""" 
X, Y, Z Info
X = ->
Y = up
Z = <-
"""
''' Overworld '''
Overworld_buildLimitX = int(7600000000) # 7.6 billion is the default for X
Overworld_buildLimitY = int(65536) # 65,536 is the default for Y
Overworld_buildLimitZ = int(7600000000) # 7.6 billion is the default for Z
Overworld_void1 = int(-1) # the starting point of the void
Overworld_voidBottom = int(-256) # the bottom of the void
Overworld_defChunk = int(16) # The size of a chunk in the overworld in blocks (first number, first number, first number, first number)
Overworld_chunk = int(Overworld_defChunk * 4) # the perimeter of a chunk in the Overworld (DO NOT CHANGE THE 4 VALUE)
''' Nether '''
Nether_buildLimitX = int(7600000000) # 7.6 billion is the default for X
Nether_buildLimitY = int(65536) # 65,536 is the default for Y
Nether_buildLimitZ = int(7600000000) # 7.6 billion is the default for Z
Nether_void1 = int(-1) # the starting point of the void
Nether_voidBottom = int(-256) # the bottom of the void
Nether_defChunk = int(16) # The size of a chunk in the nether in blocks (first number, first number, first number, first number)
Nether_chunk = int(Nether_defChunk * 4) # the perimeter of a chunk in the Nether (DO NOT CHANGE THE 4 VALUE)
''' End '''
End_buildLimitX = int(7600000000) # 7.6 billion is the default for X
End_buildLimitY = int(65536) # 65,536 is the default for Y
End_buildLimitZ = int(7600000000) # 7.6 billion is the default for Z
End_void1 = int(-1) # the starting point of the void
End_voidBottom = int(-256) # the bottom of the void
End_defChunk = int(16) # The size of a chunk in the end in blocks (first number, first number, first number, first number)
End_chunk = int(End_defChunk * 4) # the perimeter of a chunk in the end (DO NOT CHANGE THE 4 VALUE)
"""
The original Minecraft Java edition has "endless" worlds in it. These worlds are not that big compared to this versions limit
Minecraft Java editions limit is {X: 30,000,000 Y: 256 Z: 30,000,000}
This is the same for bedrock (C) edition
Users can also change this value to whatever they want, but it might not work with certain values
"""
''' Other '''
# Other section
''' Overworld '''
# coming soon
''' nether '''
# coming soon
''' End '''
# coming soon
''' end of parameters '''
# End
