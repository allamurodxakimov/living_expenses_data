import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    file_path=open("data.json").read()
    ls=json.loads(file_path)
    sum=0
    for i in ls:
        sum+=ls[i]
    return sum

# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
