import json
from prompt_creator import *

def make_prompt_real_prompt(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()  # Read all lines from the file

        # Move the file pointer to the beginning of the file
        file.seek(0)
        file.truncate()  # Clear the file content

        for line in lines:
            try:
                # Parse the JSON record
                record = json.loads(line.strip())
                
                # Remove the 'textwm' field if it exists
                # if 'textwm' in record:
                #     del record['textwm']

                record['prompt'] = create_prompt(record['prompt'])  # You can replace this with any text
               
               
                # Write the modified record back to the file
                json.dump(record, file)
                file.write("\n")  # To ensure each JSON record is on a new line
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")


# Function to modify the file in place by removing the 'textwm' field
def remove_textwm_inplace(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()  # Read all lines from the file
        
        # Move the file pointer to the beginning of the file
        file.seek(0)
        file.truncate()  # Clear the file content
        
        for line in lines:
            try:
                # Parse the JSON record
                record = json.loads(line.strip())
                
                # Remove the 'textwm' field if it exists
                if 'textwm' in record:
                    del record['textwm']


                # Write the modified record back to the file
                json.dump(record, file)
                file.write("\n")  # To ensure each JSON record is on a new line
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")


# Function to modify the file in place by removing the 'textwm' field
def add_textwm_inplace(file_path, data):
    with open(file_path, 'r+') as file:
        lines = file.readlines()  # Read all lines from the file
        
        # Move the file pointer to the beginning of the file
        file.seek(0)
        file.truncate()  # Clear the file content
        
        for line in lines:
            try:
                # Parse the JSON record
                record = json.loads(line.strip())
                
                # Remove the 'textwm' field if it exists
                # if 'textwm' in record:
                #     del record['textwm']

                record['textwm'] = data  # You can replace this with any text

                # Write the modified record back to the file
                json.dump(record, file)
                file.write("\n")  # To ensure each JSON record is on a new line
                
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

