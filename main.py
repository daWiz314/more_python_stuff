###
# TODO:
#   The objective of this script is to use it as a location to learn
#   I will probably just stick each thing I learn into a separate file and just include it into here
#   Tomorrow I will work on updating this to work with anything I add to it
#   The ideal layout, would grab everything in this folder, list it all, allowing the user (myself) to choose one and run it
#       ---Everything Will actually be in this same dir because other wise it gets touchy
#   Should be easy enough, and well with-in my abilities.
#   After I finish that, I would like to add the ability to save input data, whatever we do to it, and output data with an easy comparison.
###


# This way we can import custom files
import os
import importlib

file_names_with_ending = [name for name in os.listdir() if name.endswith(".py")]
fixed_names = []

for name in file_names_with_ending:
    if name == 'main.py':
        continue
    print(name)
    fixed_names.append(name[0:-3])

from time import sleep # import sleep for delay at end of program
print("Hello World") # Say hello world to terminal

# Continue to do this until we get some output
while True:
    print("What file would you like to run?")
    for i in range(len(fixed_names)):
        print(f'{i}) {fixed_names[i]}')
    
    print(f'{len(fixed_names)}) Quit')
    
    print(">")
    user_input = input()

    # Is a try block to get rid of error output
    try:
        cs = importlib.import_module(fixed_names[int(user_input)]) #cs = custom file
        cs.main()
        sleep(2)
        print("\n\n\n")
    except IndexError:
        print("\n\n\n")
        print("GoodBye!")
        break
    except ValueError:
        print("\n\n\n")
        print("Not valid input! Try again!")
        sleep(1)
    except Exception as inst:
        print("----ERROR----")
        print(type(inst))
        print(inst)
        print("----ERROR----")
        break

sleep(1) # This way user(Me) can see output no matter how they(I) run it

for i in range(20): # Clear screen when done, we don't want any ugly clutter
    print()
      