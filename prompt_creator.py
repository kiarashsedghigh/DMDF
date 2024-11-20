import random 

prompt_starters = [
	"Generate text based on the: ",
	"Continute the following text: ",
]

def create_prompt(input_ctx):
	return random.choice(prompt_starters) + input_ctx



	