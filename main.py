import requests

def get_country_info(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}?fullText=true")
    response.raise_for_status()

    country_data = response.json()

    return {
        "name": country_data[0]['name']['common'],
        "capital": country_data[0]['capital'][0],
        "region": country_data[0]['region'],
        "population": country_data[0]['population'],
        "area": country_data[0]['area'],
        "languages": list(country_data[0]['languages'].values())
    }

def main():
    country_name = input("Enter a country name: ")
    country_info = get_country_info(country_name)

    print(f"Country: {country_info['name']}")
    print(f"Capital: {country_info['capital']}")
    print(f"Region: {country_info['region']}")
    print(f"Population: {country_info['population']}")
    print(f"Area: {country_info['area']} square kilometers")
    print(f"Languages: {', '.join(country_info['languages'])}")

if __name__ == "__main__":
    main()
