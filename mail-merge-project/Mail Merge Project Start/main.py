#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

names = []

with open("./Input/Names/invited_names.txt", "r") as file:
    my_list = file.readlines()
    for n in my_list:
        name = n.strip("\n")
        names.append(name)

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    first_line = letter.readlines(1)
    next_lines = letter.readlines()

    for name in names:
        first_line_x = first_line[0].replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
            invite.write(first_line_x)
            for line in range(0, len(next_lines)):
                invite.write(next_lines[line])

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp