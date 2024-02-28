print('WELCOME TO YOUR TASK MANAGER!')

filename = input('What would you like your filename to be: \n(Please type \'.txt\' at the end of the name)');

tasks = []
with open(filename, 'w+') as f:
	prompt = 'Please enter what you need to do: \n(separated by commas and a space. Ex: laundry, clean) \n When you are done puting in tasks please press enter and type \'exit\' '
	user_input = f.write(input(prompt).strip())

while (user_input != 'exit'):
    tasks.append(user_input)
    user_input = input(prompt).strip()
    f.write(user_input)

tasks.sort()

print('\nAlphabetical order:')
for task in tasks:
    print(task)
