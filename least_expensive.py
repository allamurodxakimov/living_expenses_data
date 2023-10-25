import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    file_path=open("data.json").read()
    ls=json.loads(file_path)
    mi=ls["rent"]
    for i in ls:
        if mi>ls[i]:
            mi=ls[i]
    return mi
# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
