x=0
import json

# Open and load the JSON file
with open('Jikan.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
""" print(data) """

## Print all anime that stopped airing before 2015

""" for anime in data['data']:
    try:
        if anime['aired']['prop']['to']['year'] < 2015:
            print(data['data'][x]['title'])
            x=x+1
    except:
        continue """
    
    

##Print all anime whose synopsis has more than 80 characters

""" for anime in data['data']:
    if len(data['data'][x]['synopsis']) > 80:
        print(data['data'][x]['title'])
    x= x+1 """
            

