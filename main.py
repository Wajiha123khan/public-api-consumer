import requests
BASEURL = "https://restcountries.com/v3.1/name/" 

def get_country_data(country_name):
    try:
        response = requests.get(BASEURL + country_name, timeout=5)

        if response.status_code == 404:
            print("Error: Country not found.")
            return
        elif response.status_code != 200:
            print("Error: API request failed.")
            return 
        
        data = response.json()
        if not data:
            print("Error: No data found for the specified country.")
            return
        country = data[0]
        name = country.get("name",{}).get("common", "N/A")
        capital = country.get("capital", ["N/A"])[0]
        population = country.get("population", "N/A")
        region = country.get("region", "N/A")
        currencies = country.get("currencies", {})
        currency_names = ",".join(
            [currencies[c]["name"] for c in currencies]
        ) if currencies else "N/A"

        languages = country.get("languages", {})
        language_names = ", ".join(
            languages.values()
        ) if languages else "N/A"

        flag = country.get("flags", {}).get("png", "N/A")

        print("\nCountry Information")
        print("-------------------")
        print(f"Name: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        print(f"Region: {region}")
        print(f"Currencies: {currency_names}")
        print(f"Languages: {language_names}")
        print(f"Flag URL: {flag}")

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
def main():
    country_name = input("Enter country name: ").strip()

    # Handle bad user input
    if not country_name:
        print("Error: Country name cannot be empty.")
        return

    get_country_data(country_name)


if __name__ == "__main__":
    main()