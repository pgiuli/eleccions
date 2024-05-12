import requests
import json

def get_data():
    url = 'https://dinamics.ccma.cat/public/eleccions/20240512_parlament/2024/escrutini-ordre-escons/09000000000.json'
    response = requests.get(url)
    return response.text



def get_escons():
    try:
        request = get_data()
        data = json.loads(request)

        # Extract values of id and mnumitems
        id_mnumitems_dict = {}
        for item in data['datos']['geo']['opcions']['item']:
            id_mnumitems_dict[item['id']] = item['mnumitems']


        diccionari = id_mnumitems_dict
        return diccionari
    except:
        return 'Error'
        



    

if __name__ == '__main__':
    get_escons()