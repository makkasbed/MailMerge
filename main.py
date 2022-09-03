# Read letter and store in a variable
with open("Input/Letters/starting_letter.txt") as f:
    letter = f.readlines()
    letter = " ".join(letter)
    print(letter)

# Read invited guests names
with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()
    for name in names:
        invited = name.strip()
        # replace template name with name
        invited_letter = letter.replace("[name]", invited)
        # create and write to file
        filename = "Output/ReadyToSend/"+invited+"_letter.txt"
        with open(filename, mode="w") as file:
            file.write(invited_letter)

