import json

def read():
    with open ('3rd\data\og.json','r') as f:
        data=json.load(f)
    f.close()
    return data
    
def write():

    with open("3rd\data\og.json","r") as f:
        ex5=json.load(f)

        for x in ex5:
            if x['name'] == 'Old Fashioned' and x['type'] == 'donut':
                z=x['batters']['batter']

                z.append({'id': '1003', 'type': 'Coffee'})

    with open("3rd\data\og_out.json","w") as out:
        json.dump(ex5,out,indent=4)

def show_the_write():
    write()
    with open ("3rd\data\og_out.json","r")as f:
        data=json.load(f)
    f.close()
    return data    
