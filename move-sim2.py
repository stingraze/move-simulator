#Move Function Simulator
import random
def move(input_num1, input_num2):
	random_number1 = random.randint(1, 5)
	random_number2 = random.randint(1, 5)
	if(random_number1 == 1):
		input_num1 = input_num1 + 1
	if(random_number1 == 2):
		input_num1 = input_num1 + 2
	if(random_number1 == 3):
		input_num1 = input_num1 + 3
	if(random_number1 == 4):
		input_num1 = input_num1 + 4
	if(random_number1 == 5):
		input_num1 = input_num1 + 5
	if(random_number2 == 1):
		input_num2 = input_num2 + 1
	if(random_number2 == 2):
		input_num2 = input_num2 + 2
	if(random_number2 == 3):
		input_num2 = input_num2 + 3
	if(random_number2 == 4):
		input_num2 = input_num2 + 4
	if(random_number2 == 5):
		input_num2 = input_num2 + 5

	numbers = [input_num1, input_num2]
	return(numbers)

#Test 3 moves
print(move(1,5))
print(move(2,2))
print(move(3,2))
#Loop for 100 moves
x = 0

while(x < 100):
	random_number_loop1 = random.randint(1,5)
	random_number_loop2 = random.randint(1,5)
	print(move(random_number_loop1,random_number_loop2))
	x = x + 1
