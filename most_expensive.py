import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    file_path=open("data.json").read()
    ls=json.loads(file_path)
    ma=ls["rent"]
    for i in ls:
        if ma<ls[i]:
            ma=ls[i]
    return ma

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)