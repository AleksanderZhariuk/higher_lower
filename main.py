from art import logo, vs
from game_data import data
import random
import os


END_GAME = False
user_count = 0


def random_question(data_with_info, questions):
	global END_GAME
	if len(questions) == len(data):
		END_GAME = True
		return END_GAME
	random_question_from_data = random.choice(data_with_info)
	while random_question_from_data['name'] in questions:
		random_question_from_data = random.choice(data_with_info)
	name = random_question_from_data['name']
	description = random_question_from_data['description']
	country = random_question_from_data['country']
	result = random_question_from_data['follower_count']
	questions.append(random_question_from_data['name'])
	return result, name, description, country


def compares_counts(first_count, second_count, user_answer):
	global user_count
	if first_count > second_count and user_answer == 'A':
		user_count += 1
		print(f"You're right! Correct score: {user_count}")
		END_GAME = False
		return END_GAME
	elif first_count < second_count and user_answer == 'B':
		user_count += 1
		print(f"You're right! Correct score: {user_count}")
		END_GAME = False
		return END_GAME
	else:
		print(f'You lose! Your final score: {user_count}')
		END_GAME = True
		return END_GAME


def higher_lower():
	print(logo)
	questions_that_already_been = []
	first_data = random_question(data, questions_that_already_been)
	global END_GAME
	while END_GAME == False:
		second_data  = random_question(data, questions_that_already_been)
		if second_data == True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'{logo}\nYOU WON THE GAME! YOUR FINAL SCORE: {user_count}')
			continue
		print(f'Compare A: {first_data[1]}, a {first_data[2]}, from {first_data[3]}.')
		print(vs)
		print(f'Against B: {second_data[1]}, a {second_data[2]}, from {second_data[3]}.')
		answer = input('Who has more followers? Type "A" or "B": ').capitalize()
		os.system('cls' if os.name == 'nt' else 'clear')
		print(logo)
		END_GAME = compares_counts(first_data[0], second_data[0], answer)
		if first_data[0] > second_data[0]:
			pass
		else:
			first_data = second_data


os.system('cls' if os.name == 'nt' else 'clear')
higher_lower()
