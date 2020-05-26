# Start of script
''' Definition section '''
def javaRead():
	print ("JavaRead unavailable")
def pythonRead():
	print ("PythonRead unavailable")
def cRead():
	print ("CRead unavailable")
def launchStart():
	print ("The launcher was unable to start")
''' End of definition section '''
print ("Minecraft Python Edition launcher")
launcherLang1 = str("C")
launcherLang2 = str("Python")
launcherLang3 = str("Java")
print ("Launcher types")
print ("L1 " + str(launcherLang1) + " ID: 1")
print ("L2 " + str(launcherLang2) + " ID: 2")
print ("L3 " + str(launcherLang3) + " ID: 3")
launchSwitch2 = str(input("Select a launcher type: "))
if (launchSwitch2 == "1"):
	print ("Starting bedrock launcher")
	print ("Reading .c files")
	# Read C files
	print ("Select a platform")
	print ("Minecraft Pocket Edition ID: 1")
	print ("Minecraft Windows 10 edition ID: 2")
	platformCIn = str(input("Select a platform: "))
	if (platformCIn == "1"):
		print ("Minecraft Pocket Edition mode")
		print ("Select a version")
		print ("1.12.0 ID: 100")
		mcpe_verIn = str(input("Enter in an ID for a version: "))
		if (mcpe_verIn == "1"):
			print ("Loading PE1")
if (launchSwitch2 == "2"):
	print ("Starting Python launcher")
	print ("Reading .py files")
	# Read PY files
	print ("Select a platform")
	print ("MCPYE PC ID: 1")
	print ("MCPYE Mobile ID: 2")
	platformPIn = str(input("Select a platform: "))
	if (platformPIn == "1"):
		print ("MCPYE PC edition")
		print ("Select a version")
		print ("0.0.1 ID: 1]")
		pyedpc_verIn = str(input("Enter in an ID for a version: "))
		if (pyedpc_verIn == "1"):
			print ("Loading MCPYE 0.0.1")
if (launchSwitch2 == "3"):
	print ("Starting Java launcher")
	print ("Reading .java files")
	# Read JAVA files
	print ("Select a platform")
	print ("Java edition PC ID: 1")
	platformJIn = str(input("Select a platform: "))
	if (platformJIn == "1"):
		print ("Java PC edition versions")
		print ("Select a version")
		print ("0.0.1 ID: 1]")
		print ("Beta 1.0 [ID: ?]")
		print ("Beta ? [ID: ?]")
		print ("1.2 [ID: ?]")
		print ("1.3 [ID: ?]")
		print ("1.4 [ID: ?]")
		print ("1.5 [ID: ?]")
		print ("1.5.1 [ID: ?]")
		print ("1.6 [ID: ?]")
		print ("1.7 [ID: ?]")
		print ("1.7.1 [ID: ?]")
		print ("1.7.2 [ID: ?]")
		print ("1.8 [ID: ?]")
		print ("1.8.1 [ID: ?]")
		print ("1.8.2 [ID: ?]")
		print ("1.9 [ID: ?]")
		print ("1.10 [ID: ?]")
		print ("1.11 [ID: ?]")
		print ("1.12 [ID: ?]")
		print ("1.13 [ID: ?]")
		print ("1.14 [ID: ?]")
		print ("1.14.1 [ID: ?]")
		print ("1.14.2 [ID: ?]")
		print ("1.14.3 [ID: ?]")
		print ("1.15 [ID: ?]")
		''' add in snapshots as well '''
		japc_verIn = str(input("Enter in an ID for a version: "))
		if (japc_verIn == "1"):
			print ("Loading Java Edition First version")
print(launchStart())
noMore = input("Press [ENTER] key to quit")
# End of script
