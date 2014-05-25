#/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

difficulty = {'easy':random.randint(1,10),'medium':random.randint(1,100),'hard':random.randint(1,1000),'very hard':random.randint(1,10000)}
print("Hello and welcome to Roman Menzel's Guess My Number Game")
print("1.) Easy")
print("2.) Medium")
print("3.) Hard")
print("4.) Very Hard")
print("Your choice: ")
choice = input()

if choice == "1":
	tries = 0
	while True:
		print("Enter your guess: ")
		g = input()
		guess = int(g)
		if guess == difficulty['easy']:
			print("The number {0} is right :)".format(guess))
			tries = tries + 1
			if tries > 1:
				print("You've nedded {0} tries".format(tries))
			else:
				print("You've nedded {0} try".format(tries))
			exit()

		if guess > difficulty['easy']:
			print("The number {0} is too big".format(guess))
			tries = tries + 1

		if guess < difficulty['easy']:
			print("The number {0} is too small".format(guess))
			tries = tries + 1

if choice == "2":
	tries = 0
	while True:
		print("Enter your guess: ")
		g = input()
		guess = int(g)
		if guess == difficulty['medium']:
			print("The number {0} is right :)".format(guess))
			tries = tries + 1
			if tries > 1:
				print("You've nedded {0} tries".format(tries))
			else:
				print("You've nedded {0} try".format(tries))
			exit()

		if guess > difficulty['medium']:
			print("The number {0} is too big".format(guess))
			tries = tries + 1

		if guess < difficulty['medium']:
			print("The number {0} is too small".format(guess))
			tries = tries + 1

if choice == "3":
	tries = 0
	while True:
		print("Enter your guess: ")
		g = input()
		guess = int(g)
		if guess == difficulty['hard']:
			print("The number {0} is right :)".format(guess))
			tries = tries + 1
			if tries > 1:
				print("You've nedded {0} tries".format(tries))
			else:
				print("You've nedded {0} try".format(tries))
			exit()

		if guess > difficulty['hard']:
			print("The number {0} is too big".format(guess))
			tries = tries + 1

		if guess < difficulty['hard']:
			print("The number {0} is too small".format(guess))
			tries = tries + 1

if choice == "4":
	tries = 0
	while True:
		print("Enter your guess: ")
		g = input()
		guess = int(g)
		if guess == difficulty['very hard']:
			print("The number {0} is right :)".format(guess))
			tries = tries + 1
			if tries > 1:
				print("You've nedded {0} tries".format(tries))
			else:
				print("You've nedded {0} try".format(tries))
			exit()

		if guess > difficulty['very hard']:
			print("The number {0} is too big".format(guess))
			tries = tries + 1

		if guess < difficulty['very hard']:
			print("The number {0} is too small".format(guess))
			tries = tries + 1



		


