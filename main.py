import random
import os
import wikipedia
good_responses = open('good_response.txt','w')
bad_responses = open('bad_response.txt','w')

def respond_rand():
	#this is just a random reposnse for now
	lines = open('chatbotdata.txt').read().splitlines()
	myline = random.choice(lines)
	print(myline)
	try:
		response = int(input('what do you rate this reponse? (1-100)'+ '\n'))
		if response >= 50:
			with open('good_response.txt', 'a') as the_file:
				the_file.write(myline)
				the_file.close
		else:
			with open('bad_reposnse.txt', 'a') as the_file:
				the_file.write(myline)
				the_file.close()
	except ValueError:
		print('Sorry only numbers 1-5 please.')
		pass
#this will run if nothing is known to respond with



#this is the first thing that will run
print("Hi, what would you like to talk about?")
user_response = input()
respond_rand()
#a def for a response will be put in a loop here
#if user_response == 'bye bye' end
def be_better():
	#this should be someway to respond with something that is correct
	"""uses the rating system to choose the best response and 
	sets that to a varible which will be printed by another function """










"""i dont want it to ever have to use these, i would prefer if it just
 got better with the nerual network"""
unknownq_resp = [
	'Im sorry, what is the proper response here?',
	'Huh?',
	'hmm, I guess im not smart enough to respond to that.',
	'wat'
	]




def response():
	while True:
		if user_response =='bye bye':
			print("Bye friend :)")
			exit()
		else:
			respond()
	
#im gonna change the order of thesee so it will run
#i think i need to design how to choose a response
def respond():



