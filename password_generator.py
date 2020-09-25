import string
import random

def eassy(length):
	letters = string.ascii_letters
	print("Your Password is: ", end="")
	for i in range(length):
		password = random.choice(letters)
		print(password, end="")

def medium(length):
	ascii_letters = string.ascii_letters
	digits = string.digits
	letters = ascii_letters + digits
	print("Your Password is: ", end="")
	for i in range(length):
		password = random.choice(letters)
		print(password, end="")

def hard(length):
	ascii_letters = string.ascii_letters
	digits = string.digits
	punctuations = string.punctuation
	letters = ascii_letters + digits + punctuations
	print("Your Password is: ", end="")
	for i in range(length):
		password = random.choice(letters)
		print(password, end="")




if __name__ == "__main__":
	try:
		while(True):
			try:
				print('''
					      Password Generator
					____________________________
					
					1. Eassy
					2. Medium
					3. Hard
					4. Exit

					''')

				choice = int(input("Your choice: "))

				if choice == 1:
					length = int(input("Password Length: "))
					eassy(length)

				elif choice == 2:
					length = int(input("Password Length: "))
					medium(length)

				elif choice == 3:
					length = int(input("Password Length: "))
					hard(length)

				elif choice == 4:
					break

				else:
					print("Input Out Of Range.")
			except Exception as e:
				print(e)

	except ValueError:
		print("\nValueError")
	except KeyboardInterrupt:
		print("\nKeyboardInterrupt")
	except Exception as e: 
		print(e)