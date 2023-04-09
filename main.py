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

print("Hello World") # Say hello world to terminal so you know it's running


import extra_funcs as ef # Extra functions to keep things neat
from time import sleep # import sleep for delay at end of program

fixed_names = ef.get_files() # Get files to test

# Continue to do this until we get some output
while True:
    print("What file would you like to run?")
    for i in range(len(fixed_names)):
        print(f'{i}) {fixed_names[i]}')
    
    print(f'{len(fixed_names)}) (Q)uit')
    
    print(">")
    user_input = input()
    
    if ef.run_file(fixed_names, user_input):
        continue
    else:
        break

sleep(1) # This way user(Me) can see output no matter how they(I) run it

ef.clean_output()