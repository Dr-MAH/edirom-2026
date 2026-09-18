# Write a program that prints the words "Hello Edirom" to the console.
# Run it with `python exercises/ex1.py` in the terminal, or with the "|>" button in the top-right.
# Your solution must contain at least one function.

family:list = ["Martin", "Else", "note"]

def print_sentence(name: str):

    if name == "Martin" or name == "Else":
        print(f"{name}")    
    else:
        print(f"<{name} />")

for name in family:
    print_sentence(name)


print_sentence("note")   
print_sentence("measure") 
print_sentence("xyz")  
  