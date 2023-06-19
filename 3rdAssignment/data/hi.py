import json
import os

directory = os.path.dirname(__file__)

def read():
    with open(os.path.join(directory, 'exno5.json'), 'r') as file:
        data = json.load(file)
    return data


def write():
    ex5 = read()

    for i in ex5:
        if i['name'] == 'Old Fashioned' and i['type'] == 'donut':
            x = i['batters']['batter']

            max_id = 0
            for id in x:
                cur_id = int(id["id"])
                if cur_id > max_id:
                    max_id = cur_id
            last_id = str(max_id + 1)
            z = {"id": last_id, "type": "Coffee"}
            x.append(z)

    with open(os.path.join(directory, 'output.json'), 'w') as f:
        json.dump(ex5, f, indent=4)


def outputEx5():
    write()
    with open(os.path.join(directory, 'output.json'), 'r') as f:
        data = json.load(f)
    return data
