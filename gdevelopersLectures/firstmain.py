import argparse

#defining a repeat function
def repeat(s,exclaim):
	#result = s+s+s
	result = s*3
	if exclaim:
		result = result+ '!!!'
	return result

# define a main() function
def main():
	print('Hello from main')
	parser = argparse.ArgumentParser()
	parser.add_argument("a")
	args = parser.parse_args()
	print('Args '+args.a)
	res = repeat(args.a,True)
	print('Result = ', res)

# this is standard boiler plate code
if __name__ == '__main__':
	main()

# the if statement is true, if you are running the program. 
# but there is another way in which you can refer to a python program as a library or in python terms a "module". In that way you still want to load the program, but dont want to run it, just have the declared definitions ready. Then this above boiler plate if statment will be false, & would avoid running the program.
