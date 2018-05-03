# Name:Murie Queen Fiona
# Section: 2
# Date:3/5/2018
# rps.py

##### Template for Homework 1, exercises 1.2-1.4 ######

print ("********** Exercise 2.1 **********")
options =("rock","paper","scissors")
player1=input("Player 1? ")
while player1 not in options:
	print("This is not a valid object selection")
	player1=input("Player 1? ")
player2=input("Player 2? ")
while player2 not in options:
	print("This is not a valid object selection")
	player2=input("Player 2? ")

if player1 == "rock" and player2 == "rock":
	print("Tie.")
elif player1 == "rock" and player2 == "paper":
	print("Player 2 wins.")
elif player1 == "rock" and player2 == "scissors":
	print("Player 1 wins.")
elif player1 == "paper" and player2 == "rock":
	print("Player 1 wins.")
elif player1 == "paper" and player2 == "scissors":
	print("Player 2 wins.")
elif player1 == "paper" and players2 == "paper":
	print("Tie.")
elif player1 == "scissors" and player2 == "scissors":
	print ("Tie.")
elif player1 == "scissors" and player2 == "rock":
	print("Player 2 wins.")
elif player1 == "scissors" and player2 == "paper":
	print("Player 1 wins.")


