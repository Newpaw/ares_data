import requests

def get_company_data(ico:str):
    url = f'https://ares.novopacky.com/company/{ico}'
    response = requests.get(url, headers={'accept': 'application/json'})
    return response.json()

def main():
    data_company = get_company_data("02423243")
    print(data_company)
if __name__=="__main__":
    main()