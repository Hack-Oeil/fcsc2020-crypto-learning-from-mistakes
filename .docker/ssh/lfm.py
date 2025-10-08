import ast
from Crypto.Random.random import getrandbits

e =  32
n =  64
q = 128

def randomize_secret(n):
	return [ getrandbits(q) for _ in range(n) ]

def dot(a, b):
	return sum(x * y for x, y in zip(a, b))

def LWE(s):
	a = [ getrandbits(q) for _ in range(n)]
	return (a, dot(a, s) + getrandbits(e))

def menu():
	print("Commands are:")
	print("|-> s: Sample the oracle")
	print("|-> f: Get flag")
	print("|-> q: Quit")

if __name__ == "__main__":

	s = randomize_secret(n)
	req = 0
	while req <= 3 * n:
		try:
			menu()
			cmd = input(">>> ")

			if len(cmd) == 0 or cmd not in ['s', 'f', 'q']:
				continue

			if cmd == 'q':
				break

			if cmd == 's':
				a, c = LWE(s)
				print(a)
				print(c)
				req += 1

			elif cmd == 'f':
				ss = ast.literal_eval(input("Enter the server secret: "))
				if s == ss:
					flag = open("flag.txt").read().strip()
					print(f"Congrats!! Here is the flag: {flag}")
				else:
					print("Nope, bye bye.")

				break

		except:
			print("Error: check your input.")
			continue
