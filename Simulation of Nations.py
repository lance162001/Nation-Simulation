#to do list:
	# -Fix the player deletion system
	# -create production
	# -create different resource types
	# -revamp values for turn by turn things
	# -+create random events for characters based on type and civility

import random
import sys
from os import path

turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("r"))
stuff = turnsdoc.read()
stuff = stuff.split("\n")
overview=open(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\overview',("r"))
overviewData=overview.read()
overviewData=overviewData.split("\n")
print(stuff)
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
	if country == "M":
		currentR = 15
		currentM = 20
		currentC = 15
		currentI = 50
	if country == "D":
		currentR = 20
		currentM = 15
		currentC = 50
		currentI = 15
	if country == "U":
		currentR = 50
		currentM = 15
		currentC = 20
		currentI = 15
	pop = 100
	if country == "Utopia":
		if input("This is none of your concern, mortal") == "Genius without education is like silver in the mine":
			print("this isn't at all fair")
			currentR = 1000
			currentM = 1000
			currentC = 1000
			currentI = 1000
			pop = 10000
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("a"))
	turnsdoc.write('\n')
	turnsdoc.write (name)
	stats(name,country,currentR,currentM,currentC,currentI,pop)
	info(name,country,currentR,currentM,currentC,currentI,pop)

def info(name,type,resources,military,civility,money,pop):
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
		"The",type2,"Nation of",name,": \n Population:",pop,title,
		"\n Resources:",resources,"\n Military: ",military,
		"\n Civility: ",civility, "\n Money: ",money)
		

def stats(name,type,R,M,C,I,pop):
	pat = path.join(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\players', name)
	save = open(pat,"w")
	
	for i in R,M,C,I,pop:
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
	this=input("Would you like to access the *logs* or the status of *turns* for the players? : ")
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
	if this != "turns" and this != "logs" and this!= "clearlog":
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
		type = d["type"]
		resources = int(float(d["resources"]))
		military = int(float(d["military"]))
		civility = int(float(d["civility"]))
		money = int(float(d["money"]))
		population = int(float(d["population"]))

		option=input("Would you like your country's *info* or to *execute* an action? : ")
		if option == "info": 
			info(name,type,resources,military,civility,money,population)
			sys.exit()
		if option == "execute":
			if (name + " done") in stuff:
				print("Please wait until everyone else has had a chance to do their turn.")
				sys.exit()
			execute = input("War - Trade - Production - Pass: ")

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
					print("Your Enemy's Information is Below \n")
					info(c["name"],c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
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
								c["military"] -= int(float(military))
								c["military"] = neut(c["military"])
								logData = "war"
							try: 
								stats(name2,c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
							except OverflowError:
								print("that's not good")
								sys.exit()
					else:
						print("ok nevermind then")
						sys.exit()
			if execute == "trade":
				print("	Your Resources: ",resources,"\n	Your Money: ", money)
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
					print("	His/Her/Attack Helicopter's Resources: ",c["resources"],"\n	His/Her/Attack Helicopter's Money: ",c["money"])
					what = input("Are you giving *resources* or *money*? : ")
					if what == "resources":
						howmuch = int(input("How many resources? : "))
						payment = int(input("How many dollar bills are you going to be handed for your goodies? : "))
						if howmuch > resources or payment > c["resources"]:
							print("One of you does not have enough to give...")
							sys.exit()
						else:
							resources -= howmuch
							c["resources"] += howmuch
							money += payment
							c["money"] -= payment
							print("Charlie is happy with you giving resources to",c["name"],"!")
					if what == "money":
						howmuch = int(input("How much money? : "))
						payment = int(input("How much are you recieving? : "))
						if howmuch > money or payment > c["money"]:
							print("One of you doesn't have enough to give...")
							sys.exit()
						else:
							money -= howmuch
							resources += payment
							c["money"] += howmuch
							c["resources"] -= payment	
							print("Congratulations, your money has been removed and given to",c["name"],"!")
					if what != "money" and what != "resources":
						print("but he refused")
						sys.exit()
					logData="trade"
					try: 
						stats(c["name"],c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
					except NameError:
						print("what even happened here")
						sys.exit()
			
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
				stats(name,type,resources,military,civility,money,population)
			except NameError:
				print("something went wrong")
				sys.exit()
		if option == "execute by hanging": print("~~~~hell yeah~~~~~")
		if option != "execute" and option != "info" and option != "execute by hanging":
			print("you dissapoint me")
			sys.exit()
if selection != "load" and selection != "new":
	print("it was a simple question my child")
	sys.exit()


try:
	name
except NameError:
	print("you are doing dev stuff or you broke it")
else:
		try:
			line_number=stuff.index(name)
		except ValueError:
			print("didn't work")
		else:
			x=0
			turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("w"))
		if name not in stuff:
			stuff.append(name)
		for things in stuff:
			turnsdoc.write(things)
			if things == name:
				turnsdoc.write(" done")
			if x < (len(stuff)-1): turnsdoc.write('\n')
			x+=1
			
try:
	logData
except NameError:
	print("if you are getting this message something wrong happened")
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
		if what == "resources":
			logFile.write(" dollars")
		else:
			logFile.write(" resources")
		
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
		
turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("r"))
stuff = turnsdoc.read()
stuff = stuff.split("\n")
	
if all('done' in i for i in stuff):
	turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("w"))
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
			pass
		else:
			nameE = who[0]
			typeE = who[1]
			resourcesE = int(float(who[2]))
			militaryE= int(float(who[3]))
			civilityE = int(float(who[4]))
			moneyE = int(float(who[5]))
			populationE = int(float(who[6]))
			populationE = int(float(populationE*1.05))
			if typeE == "D":
				civilityE = civilityE + 2
				if random.randint(1,10) == 5:
					civilityE = civilityE - 10
					print("uprising for",nameE,", and he loses 10 civility!")
			if typeE == "M":
				moneyE = int(float(moneyE*1.02 + 1))
				if random.randint(1,20) == 10:
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
			stats(nameE,typeE,resourcesE,militaryE,civilityE,moneyE,populationE)
				if random.randint(1,10) == 5 and civilityE < 8:
					print("The people from",nameE,"stage a revolt and fail, but cause chaos nonetheless")
					militaryE -= 15
					populationE -= 30

	overviewData[1]=int(overviewData[1])
	overviewData[1]+=1

	x=0
	overview=open(r'C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\overview',("w"))
	for i in overviewData:
		overview.write(str(i))
		if x < len(overviewData)-1:
			overview.write("\n")
			x+=1
	
	
	
	