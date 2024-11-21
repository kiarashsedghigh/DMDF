import random 

prompt_starters = [
	"Generate text based on the: ",
	"Continue the following text: ",
	"What is your idea about this text: ",
	"Expand more of the idea of: ",
	"Write your opinion about: "
]

def create_prompt(input_ctx):
	return random.choice(prompt_starters) + input_ctx



	