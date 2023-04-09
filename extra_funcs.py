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
    import os
    file_names_with_ending = [name for name in os.listdir() if name.endswith(".py")]
    fixed_names = []
    for name in file_names_with_ending:
        if name == 'main.py' or name == 'extra_funcs.py':
            continue
        fixed_names.append(name[0:-3])
    return fixed_names

def run_file(fixed_names, user_input):
    if user_input[0].lower() == 'q':
        quit = True
    else:
        quit = False
    try:
        if quit:
            raise IndexError
        cs = importlib.import_module(fixed_names[int(user_input)]) #cs = custom file
        cs.main()
        pause()
        print("\n\n\n")
        return True
    except IndexError:
        print("\n\n\n")
        print("GoodBye!")
        return False
    except ValueError:
        print("\n\n\n")
        print("Not valid input! Try again!")
        sleep(1)
        return True
    except Exception as inst:
        print("----ERROR----")
        print(type(inst))
        print(inst)
        print("----ERROR----")
        return False