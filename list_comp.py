# Example of list comp

def main():
    colors = ['black', 'white']
    sizes = ['xs','s','m','l','xl']
    shirts = [(size, color) for size in sizes for color in colors]

    print(shirts)
    return shirts # In case we want to save data
