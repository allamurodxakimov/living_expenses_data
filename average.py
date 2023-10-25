import json
def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    file_path=open("data.json").read()
    ls=json.loads(file_path)
    s=0.0
    l=0
    for i in ls:
        s+=ls[i]
        l+=1
    return (s/l)
# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
