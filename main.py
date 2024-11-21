from c4_utils import *

# First distill the c4_dataset files by removing their "textwm" json field
for i in range(0,40):
	file_path = f"./c4_dataset/{i}.jsonl"
	print(file_path)
	
	## Adding the prompt to the previous C4 texts
	make_prompt_real_prompt(file_path)

	## Removing the textwm field of the json record
	remove_textwm_inplace(file_path)