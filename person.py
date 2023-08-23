#Write a function called get_age that asks the user for their age, and returns it as an int
def get_age():
    age = int(input('Enter your age: '))
    return age


#Write another function called get_name, which does the same but for the users name.
def get_name():
    name = input('Enter your name: ')
    return name

#Call both these functions and tell the user what you know about them!
Age = get_age()
print('You are ' + str(Age) + ' years old.')


Name = get_name()
print('Your name is ' + Name)  





