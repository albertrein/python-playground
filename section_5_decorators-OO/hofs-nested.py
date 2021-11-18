def teste(outra_funcao):
    outra_funcao()

def impressao():
    print("Hello gatis")


def zero_function():
	def first_function():
		print("Hello")

	def second_function():
		print("You!")

	first_function()
	second_function()

if __name__ == "__main__":
    teste(impressao)
    zero_function
