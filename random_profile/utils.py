import random

def load_txt_file(file_name: str) -> list:
    """ function to load txt file into list
    
    args:
        file_name (str): file name to load
    
    returns:
        list: list of data from file
    """
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data

def ipv4_gen() -> str:
    return f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

