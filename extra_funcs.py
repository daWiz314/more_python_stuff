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