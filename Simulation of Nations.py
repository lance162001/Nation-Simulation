import sys
from os import path
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
	save = open(pat,'r')
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
"")


selection = input("New, Load, Help, Options, or Quit? : ")
if selection == "quit": 
	print("Well that was a short lived encounter...")
	#sys.exit()

elif selection == "options":
	print("non existant")
	
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

elif selection == "new": 
	name=input("your name? : ")
	start=newPlayer(name)
	selection == "load"
elif selection == "load": 
	name=input("Name of Player? : ")
	try:
		data=fetchPlayer(name)
	except IOError:
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

		option=input("Would you like your country's info or an action to be executed? : ")
		if option == "info": 
			info(name,type,resources,military,civility,money,population)
			#sys.exit()
		if option == "execute":
			execute = input("War - Trade - Production - Pass : ")

			if execute == "war":			
				print("Your military force is currently",military,"strong, who would you like to attack?")
				name2 = input(": ")
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
					confirm = input("Are you sure you want to attack? : ")
					if confirm == "yes":
						try:
							troops=int(input("With how many of your troops? : "))
						except ValueError:
							print("That is not a valid amount of troops")
							sys.exit()
						else:
							if troops > military:
								print("You can't just make troops out of thin air, I apologize for the inconvenience")
							if troops < military:
								result = war(troops,c["military"],c["civility"],type)
								if result < 0 or result == 0:
									print("Your army may or may not have just all died")
									military = military - troops
									if type == "A":
										civility = civility - 10
									else:
										civility = civility - 5
								
								if result > 0:
									print("A crushing victory that I am sure high schoolers will write essays about for hundreds of years to come \n What is left of your army: ",result)
									military=result
									if type == "A":
										civility = civility + 15
									else:
										civility = civility + 5
								c["military"] -= int(float(military))
								c["military"] = neut(c["military"])
							try: 
								stats(aggro,c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
							except NameError:
								print("that's not good")
								sys.exit()

			if execute == "trade":
				print("	Your Resources: ",resources,"\n	Your Money: ", money)
				name2 = input("With Who? : ")
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
					what = input("Are you giving resources or money? : ")
					if what == "resources":
						howmuch = int(input("How many resources? : "))
						payment = int(input("How many dollar bills are you going to be handed for your goodies? : "))
						resources -= howmuch
						c["resources"] += howmuch
						money += payment
						c["money"] -= payment
						print("Charlie is happy with you giving resources to",c["name"],"!")
					if what == "money":
						howmuch = int(input("How much money? : "))
						payment = int(input("How much are you recieving? (prob not a lot like come on man you are not a barter master): "))
						money -= howmuch
						resources += payment
						c["money"] += howmuch
						c["resources"] -= payment
						print("Congratulations, your money has been removed and given to",c["name"],"!")
					else:
						print("but he refused")
						sys.exit()
					try: 
						stats(c["name"],c["type"],c["resources"],c["military"],c["civility"],c["money"],c["population"])
					except NameError:
						print("what even happened here")
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
else:
	print("it was a simple question my child")
	sys.exit()



turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("r"))
stuff = turnsdoc.read()
stuff = stuff.split("\n")
if name in stuff:
	try:
		line_number=stuff.index(name)
	except ValueError:
		print("didn't work")
	else:
		turnsdoc=open(r"C:\Users\User\Desktop\program crap\Simulation of Nations and stuff\specifics\players",("r"))
		turnsdoc.write("\n \n \n test"
else: 
	print("error")