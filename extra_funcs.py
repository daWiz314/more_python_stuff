# Import these in the entire thing we so we can keep using it everytime the function is called 
from time import sleep
import importlib 

def clean_output():
    for i in range(20): # Clear screen when done, we don't want any ugly clutter
        print()

def pause():
    print("Press enter to continue")
    input()
    return

def get_files():
    import os # Import this once so we can get rid of it afterwards
    file_names_with_ending = [name for name in os.listdir() if name.endswith(".py")]
    fixed_names = [] # fixed names = Names of files without extension so we can import them
    for name in file_names_with_ending:
        if name == 'main.py' or name == 'extra_funcs.py': # Skip our files that are CRITICAL to base function of script
            continue
        fixed_names.append(name[0:-3])
    return fixed_names

def run_file(fixed_names, user_input):
    # Rules for returns of in this function
    # True = run again
    # False = Quit program
    if user_input[0].lower() == 'q':
        quit = True
    else:
        quit = False
    try:
        if quit:
            raise IndexError
        cs = importlib.import_module(fixed_names[int(user_input)]) #cs = custom file
        cs.main() # Every file will have a 'main()'
        pause()
        print("\n\n\n")
        return True
    except IndexError: # Typed a number outside of range, treat as quit
        print("\n\n\n")
        print("GoodBye!")
        return False 
    except ValueError: # Typed literally anything besides a number or q
        print("\n\n\n")
        print("Not valid input! Try again!")
        sleep(1)
        return True
    except Exception as inst: # Take any uncaught error (they should be caught in their respective file) and output it
        print("----ERROR----")
        print(type(inst))
        print(inst)
        print("----ERROR----")
        return False