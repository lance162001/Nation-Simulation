import random
import sys
from os import path
import os

turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("r"))
stuff = turnsdoc.read()
stuff = stuff.split("\n")

overview=open(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\overview',("r"))
overviewData=overview.read()
overviewData=overviewData.split("\n")

def newPlayer(name):
	country=input("Authoritarian,Mercantile,Democratic, or Utilitarian type government? (A,M,D,U): ")
	pat = path.join(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\players', name)
	save = open(pat,"w+")
	save.write(name)
	save.write("\n")
	save.write(country)
	if country == "A":
		currentR = 15
		currentM = 50
		currentC = 15
		currentI = 20
		currentW = 0
	if country == "M":
		currentR = 15
		currentM = 20
		currentC = 15
		currentI = 50
		currentW = 25
	if country == "D":
		currentR = 20
		currentM = 15
		currentC = 50
		currentI = 15
		currentW = 15
	if country == "U":
		currentR = 50
		currentM = 15
		currentC = 20
		currentI = 15
		currentW = 5
	pop = 100
	if country == "Utopia":
		if input("This is none of your concern, mortal") == "Genius without education is like silver in the mine":
			print("this isn't at all fair")
			currentR = 1000
			currentM = 1000
			currentC = 1000
			currentI = 1000
			currentW = 1000
			pop = 10000
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("a"))
	turnsdoc.write('\n')
	turnsdoc.write (name)
	stats(name,country,currentR,currentM,currentC,currentI,pop)
	info(name,country,currentR,currentM,currentC,currentI,pop)

def info(name,type,resources,military,civility,money,pop,weapons):
		if type == 'D': 
			type2 = "Democratic"
			title = "Suburban protesters"
		if type == 'A': 
			type2 = "Authoritaric"
			title = "Grunt Soldiers"
		if type == 'M': 
			type2 = "Mercantilistic"
			title = "Greedy Businessmen"
		if type == 'U': 
			type2 = "Utilitaristic"
			title = "Coal Miners"
		if type == "Utopia":
			type2 = "Utopian"
			title = "Gods"
		print(
		"\nThe",type2,"Nation of",name,": \n Population:",pop,title,
		"\n Resources:",resources,"\n Military: ",military,
		"\n Civility: ",civility, "\n Money: ",money,"\n Weapons: ",weapons)
		

def stats(name,type,R,M,C,I,pop,W):
	pat = path.join(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\players', name)
	save = open(pat,"w")
	
	for i in R,M,C,I,pop,W:
		i=neut(i)
		i=int(float(i))
	
	save.write(name)
	save.write("\n")
	save.write(type)
	save.write('\n')
	save.write(str(R))
	save.write("\n")
	save.write(str(M))
	save.write("\n")
	save.write(str(C))
	save.write("\n")
	save.write(str(I))
	save.write("\n")
	save.write(str(pop))
	save.write("\n")
	save.write(str(W))

def fetchPlayer(name):
	pat = path.join(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\players', name)
	try:
		save = open(pat,'r')
	except FileNotFoundError:
		print("you just don't exist")
		sys.exit()
	else:
		data=save.read()
		data=data.split("\n")
		return (data)

def war(offense,defense,civildefense,type):
	if type == "A":
		offense = int(1.2*float(offense))
	civildefense=int(civildefense)
	offense=int(offense)
	defense=int(defense)
	if civildefense > 10 and defense > 5:
		defensepower = (civildefense*2 / defense) + defense
	else: 
		defensepower = defense 
	return (offense - defensepower)

def neut(number):
	if number < 0:
		number = 0
	if number > 2000:
		number = 2000
	return(number)

def delete(name):
	pat = path.join(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\players', name)
	os.remove(pat)
	try:
		stuff.remove(name+" done")
	except ValueError:
		stuff.remove(name)
	x=0
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("w"))
	for things in stuff:
		turnsdoc.write(things)
		if x < (len(stuff)-1):
			turnsdoc.write("\n")
			x+=1

print("_______________________________________________________________\n"
"Programming by Lance Gruber, Concept by Alex Flynn,\n"
"and Comedic Relief / Moral Support by Charlie Kennedy\n"
"_______________________________________________________________\n"
"Copyright 2017 Unproductive Productions. All Rights Not Reserved.\n"
"Unproductive Productions is not a registered trademark of \n"
"anything, and neither is this game calculator.\n"
"_______________________________________________________________\n"
"Welcome to the Simulation of Nations and Stuff Offical Program!\n"
"_______________________________________________________________\n"
"\n		Turn:",overviewData[1],"\n")


selection = input("New, Load, Help, Options, or Quit? : ")
if selection == "quit": 
	print("Well that was a short lived encounter...")
	sys.exit()

elif selection == "options":
	this=input("Would you like to access the *logs*,the status of *turns*, or *delete* a character? : ")
	if this == "logs":
		logs=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\log",("r"))
		log=logs.read()
		log=log.split("\n")
		print("_______________________________________________________________\nNote:\n Goes from top to bottom chronologically\n")
		for each in log:
			print(each)
	if this == "turns":
		print("_______________________________________________________________\nNote:\n If there is a *done* to the right of a name, that player has done their turn\n")
		print("\n Turn Data ------------------------------------")
		for stuffs in stuff:
			print("  ",stuffs)
	if this == "clearlog":
		password=input("password? : ")
		if password == "Geronimo":
			logFile=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\log",("w"))
			logFile.write("Log Data ------------------------------------")
			sys.exit()
	if this == "delete":
		iput=input("Who? and don't be that guy who deletes someone else's acc without permission : ")
		sure=input("but like are you sure because this is irreversible : ")
		if sure == "yes":
			try:
				delete(iput)
			except FileNotFoundError:
				print("deleting something that doesn't exist? impressive.")
			else:
				print("deleted!")
	if this != "turns" and this != "logs" and this!= "clearlog" and this!="delete":
		print("that isn't an option for the options")
	sys.exit()
elif selection == "help":
	print(
	"\nGeneral Tips --------------------------------------------------------- \n \n"
	"	1. Respond to applicable questions with lowercase answers.(except names) \n"
	"	2. Make sure not to misspell any name or else you will have to restart. \n"
	"	3. Make your name weird so people won't be able to guess it. \n \n"
	"Different Types of Countries ----------------------------------------- \n \n"
	"	Authoritarian - A war machine that gains bonuses to military statically\n"
	"	and civility when winning. Extra lost when a war is lost. \n \n"
	"	Democratic - A slow moving long term \n"
	"	country that passively gains civility. \n \n"
	"	Utilitarian - A mining or farming country that depends\n"
	"	on producing natural resources for income. \n \n"
	"	Mercantile - The money grubbing oppurtunists who \n" 
	"	depend on cash for happiness and success. \n")
	sys.exit()
elif selection == "new": 
	name=input("your name? : ")
	start=newPlayer(name)
	logData="new"
if selection == "load": 
	name=input("Name of Player? : ")
	
	try:
		data=fetchPlayer(name)
	except IOError or UnboundLocalError:
		print(name,"I am so sorry but it seems to me you don't exist")
		sys.exit()
	else:
		d = {}
		d["name"] = data[0]
		d["type"] = data[1]
		d["resources"] = data[2]
		d["military"] = data[3]
		d["civility"] = data[4]
		d["money"] = data[5]
		d["population"] = data[6]
		d["weapons"] = data[7]
		type = d["type"]
		resources = int(float(d["resources"]))
		military = int(float(d["military"]))
		civility = int(float(d["civility"]))
		money = int(float(d["money"]))
		population = int(float(d["population"]))
		weapons = int(float(d["weapons"]))

		option=input("Would you like your country's *info* or to *execute* an action? : ")
		if option == "info": 
			info(name,type,resources,military,civility,money,population,weapons)
			sys.exit()
		if option == "execute":
			if (name + " done") in stuff:
				print("Please wait until everyone else has had a chance to do their turn.")
				sys.exit()
			execute = input("War - Trade - Production - Pass: ")
#war
			if execute == "war":			
				print("Your military force is currently",military,"strong, who would you like to attack?")
				name2 = input(": ")
				while name2 == name:
					name2=input("how about you try not to go to war with yourself.. : ")
				try:
					who=fetchPlayer(name2)
				except FileNotFoundError:
					print("Try attacking the sky another day")
					sys.exit()
				else:
					c = {}
					c["name"] = who[0]
					c["type"] = who[1]
					c["resources"] = int(float(who[2]))
					c["military"] = int(float(who[3]))
					c["civility"] = int(float(who[4]))
					c["money"] = int(float(who[5]))
					c["population"] = int(float(who[6]))
					c["weapons"] = int(float(who[7]))
					print("Your Enemy's Information is Below \n")
					info(c["name"],c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"],c["weapons"])
					confirm = input("Are you sure you want to attack? yes/no : ")
					if confirm == "yes":
						try:
							troops=int(input("With how many of your troops? : "))
						except ValueError:
							print("That is not a valid amount of troops")
							sys.exit()
						else:
							if troops > military:
								print("You can't just make troops out of thin air, I apologize for the inconvenience")
							if troops < military or troops == military:
								result = war(troops,c["military"],c["civility"],type)
								if result < 0 or result == 0:
									warResults="l"
									print("Your army may or may not have just all died")
									military = military - troops
									if type == "A":
										civility = civility - 10
									else:
										civility = civility - 5
								
								if result > 0:
									warResults="w"
									print("A crushing victory that I am sure high schoolers will write essays about for hundreds of years to come \n What is left of your army: ",result)
									if type == "A":
										civility = civility + 15
										military = military-troops+int(float(result/1.2))
									else:
										civility = civility + 5
										military=military-troops+result
									weapons = c["weapons"]/2
									c["weapons"] -= int(float(c["weapons"]/2))
								c["military"] -= int(float(military))
								c["military"] = neut(c["military"])
								logData = "war"
							try: 
								stats(name2,c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"],c["weapons"])
							except OverflowError:
								print("that's not good")
								sys.exit()
					else:
						print("ok nevermind then")
						sys.exit()
#trade
			if execute == "trade":
				print("	Your Resources: ",resources,"\n	Your Money: ", money,"\n Your Weapons: ",weapons)
				name2 = input("With Who? : ")
				while name2 == name:
					name2=input("how about you try not to trade with yourself... : ")
				try:
					who=fetchPlayer(name2)
				except FileNotFoundError:
					print("trading with imaginary friends is not productive")
					sys.exit()
				else:
					c = {}
					c["name"] = who[0]
					c["type"] = who[1]
					c["resources"] = int(float(who[2]))
					c["military"] = int(float(who[3]))
					c["civility"] = int(float(who[4]))
					c["money"] = int(float(who[5]))
					c["population"] = int(float(who[6]))
					c["weapons"] = int(float(who[7]))
					print("	His/Her/Attack Helicopter's Resources: ",c["resources"],"\n	His/Her/Attack Helicopter's Money: ",c["money"],"\n His/Her/Attack Helicopter's Weapons: ",c["weapons"])
					what = input("Are you giving *resources*, *money*, or *weapons*? : ")
					
					howmuch = int(input("How much? : "))
					trials = 0
					while howmuch > resources:
						trials += 1
						howmuch = int(input("How many that you actually have? : "))
						if trials == 5:
							print("ok that is enough")
							sys.exit()
					if what == "resources":
						paymentType = input("are you recieving weapons or money?")
					if what == "weapons":
						paymentType = input("are you recieving resources or money?")
					if what == "money":
						paymentType = input("are you recieving resources or weapons?")
					
					if paymentType == "money":
						payment = int(input("How many dollar bills are you going to be handed for your goodies? : "))
					if paymentType == "weapons":
						payment = int(input("How many machine guns in briefcases are going to mysteriously appear on your doorstep? : "))
					if paymentType == "resources":
						payment = int(input("How many boxes of oil will you be putting in your attic?"))
				
					if payment > c[paymentType]:
							print("You are asking for what they don't have...\n")
							trials = 0
							while payment > c[paymentType]:
								int(input("So how much are they actually going to be paying? : "))
								trials+=1
								if trials == 5:
									print("bro calm down and take a break")
									sys.exit()
					
					else:
						what -= howmuch
						c[paymentType] += howmuch
						paymentType += payment
						c[what] -= payment
						print("Charlie is happy with you giving goodies to",c["name"],"!")
					
				if what != "money" and what != "resources" and what != "weapons":
					print("but he refused")
					sys.exit()
				logData="trade"
				try: 
					stats(c["name"],c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
				except NameError:
					print("what even happened here")
					sys.exit()
#production
			if execute == "production":
				what=input("What are we making? guns/soldiers/gold-mines : ")
				if what == "guns":
					print("\n  You need 2 resources to produce weapons \n  And the max amount you can make per turn are 10, or 30 if Mercantile")
					print("  Weapons: ",weapons,"\n  Resources: ",resources)
					howMany=int(input("So how many weapons do you want to make? : "))
					if type == "M":
						max = 30
					else:
						max = 10
					x=0
					while howMany > max and x!=5:
						int(input("Try that again : "))
						x+=1
					if x == 5:
						print("You are outta ear")
						sys.exit()
					
					x=0
					while resources - howMany*2 < 0 and x != 5:
						howMany=int(input("Not Enough Resources, Try Again : "))
						x+=1
					if x == 5:
						print("Ok no more tries")
						sys.exit()
					resources -= howMany*2
					weapons+=howMany
					print("  Resources Left: ",resources,"\n\n  New Weapon Value: ",weapons)
					logData = "production"
				
				if what == "soldiers":
					print("\n  You need 1 person and 1 weapon to produce a soldier, and if you are\n  not Authoritarian, your soldiers can't outnumber your population")
					print("  Weapons: ",weapons,"\n  Population: ",population)
					howMany=int(input("How many soldiers would you like to train? : "))	
					while type != "A" and howMany > int(float(population/2)):
						howMany=int(input("I just told you the rule about over half of population being soldiers!"))
					while howMany > population or howMany > weapons:
						howMany=int(input("You don't have enough weapons or people! Try again : "))
					weapons-=howMany
					population-=howMany
					military+=howMany
					print("  Population Left: ",population,"\n  Weapons Left: ",weapons,"\n\nNew Military Value: ",military)
					logData="production"
#pass
					if execute == "pass":
						ok=input("are you sure you don't want to do anything during your turn? yes/no : ")
						if ok == "yes": 
							print("ok your turn is over")
							logData="pass"
						else: 
							print("that is probably a good choice")
							sys.exit()
				
			if execute != "trade" and execute != "war" and execute != "production" and execute != "pass":
				print("I would hope that this is a typo")
				sys.exit()
			try:		
				stats(name,type,resources,military,civility,money,population,weapons)
			except NameError:
				print("something went wrong")
				sys.exit()
		if option == "execute by hanging": print("~~~~hell yeah~~~~~")
		if option != "execute" and option != "info" and option != "execute by hanging":
			print("you dissapoint me")
			sys.exit()
if selection != "load" and selection != "new" and selection != "options" and selection != "help" and selection !="quit":
	print("it was a simple question my child")
	sys.exit()

#Turn Updating
try:
	name
except NameError:
	print("no Name applicable")
else:
	if name not in stuff: stuff.append(name)
	line_number=stuff.index(name)
	x=0
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("w"))
	for things in stuff:
		turnsdoc.write(things)
		if things == name:
			turnsdoc.write(" done")
		if x < (len(stuff)-1): turnsdoc.write('\n')
		x+=1

#Log Creation		
try:
	logData
except NameError:
	print("no logData applicable")
else:
	logFile=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\log",("a"))
	logFile.write("\n")
	logFile.write(name)
	if logData == "new":
		logFile.write(" enters the carnage ")
	if logData == "trade":
		logFile.write(" traded ")
		logFile.write(str(howmuch))
		logFile.write(" ")
		if what == "money":
			logFile.write("dollars")
		else:
			logFile.write(what)
		logFile.write(" to ")
		logFile.write(name2)
		logFile.write(" for ")
		logFile.write(str(payment))
		if what == "money":
			logFile.write(" dollars")
		else:
			logFile.write(paymentType)
		
	if logData == "war":
		logFile.write(" started a battle with ")
		logFile.write(name2)
		logFile.write(" and ")
		if warResults == "l":
			logFile.write("lost horribly")
		else:
			logFile.write("destroyed the enemy")
	if logData == "pass":
		logFile.write(" just sort of sat there")
	if logData == "production":
		logFile.write(" created ")
		logFile.write(str(howMany))
		logFile.write(" glorious ")
		logFile.write(what)
turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("r"))
stuff = turnsdoc.read()
stuff = stuff.split("\n")
	
#End of turn actions	
if all('done' in i for i in stuff):
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\turns",("w"))
	print("turn over!\n\n\n\n 		Thank god you finally did your turn everyone was waiting...")
	i = 0

	while i < len(stuff):
		if "done" in stuff[i]:
			stuff[i]=stuff[i].replace(" done", "")
		i += 1
	x=0
	for things in stuff:
		turnsdoc.write(things)
		
		if x < (len(stuff)-1):
			turnsdoc.write("\n")
			x+=1
		
	
	for thing in stuff:
		try:
			who=fetchPlayer(thing)
		except FileNotFoundError:
			print("issue with",who,"!")
		else:
			nameE = who[0]
			typeE = who[1]
			resourcesE = int(float(who[2]))
			militaryE= int(float(who[3]))
			civilityE = int(float(who[4]))
			moneyE = int(float(who[5]))
			populationE = int(float(who[6]))
			populationE = int(float(populationE*1.02))
			weaponsE = int(float(who[7]))
			if typeE == "D":
				civilityE = civilityE + 2
				if random.randint(1,10) == 5:
					civilityE = civilityE - 10
					print("protesting against",nameE,", and 10 civility is lost!")
			if typeE == "M":
				moneyE = int(float(moneyE*1.02 + 1))
				if random.randint(1,20) == 10 and civilityE < 25:
					print("Looks like",nameE,"'s Economy just went into a short depression and lost 20 money and half his/her civility!")
					moneyE = moneyE - 20
					civilityE = civilityE/2
			if typeE == "U":
				resourcesE = int(float(resourcesE + (civilityE*populationE)/1000))
				if random.randint(1,5) == 3:
					print("A massive drought just wrecked the farms of",nameE,", losing him/her 5 resources!")
					resourcesE = resourcesE - 5
			if typeE == "A":
				civilityE -= 1
				weaponsE += 1
				if random.randint(1,10) == 5 and civilityE < 8:
					print("The people from",nameE,"stage a revolt and fail, but cause chaos nonetheless!")
					militaryE -= 15
					populationE -= 30
			stats(nameE,typeE,resourcesE,militaryE,civilityE,moneyE,populationE,weaponsE)
	overviewData[1]=int(overviewData[1])
	overviewData[1]+=1

	x=0
	overview=open(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\overview',("w"))
	for i in overviewData:
		overview.write(str(i))
		if x < len(overviewData)-1:
			overview.write("\n")
			x+=1
	
	
	
	