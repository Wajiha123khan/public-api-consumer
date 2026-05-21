import requests
BASEURL = "https://restcountries.com/v3.1/name/" 



def fetch_country(country_name):
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
            return None

        return data[0]

    except requests.exceptions.RequestException:
        return None

def get_country_data(country_name):

    try:
        country = fetch_country(country_name)

        if not country:
            print("Error: Country not found or API issue.")
            return
       
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


def compare_countries(country1, country2):
    data1 = fetch_country(country1)
    data2 = fetch_country(country2)

    if not data1 or not data2:
        print("Error: One or both countries not found.")
        return

    name1 = data1.get("name", {}).get("common", "N/A")
    name2 = data2.get("name", {}).get("common", "N/A")

    pop1 = data1.get("population", 0)
    pop2 = data2.get("population", 0)

    region1 = data1.get("region", "N/A")
    region2 = data2.get("region", "N/A")

    print("\n Country Comparison")
    print("=" * 40)

    print(f"{name1} Population: {pop1}")
    print(f"{name2} Population: {pop2}")

    if pop1 > pop2:
        print(f"{name1} has larger population")
    elif pop2 > pop1:
        print(f"{name2} has larger population")
    else:
        print("Both have equal population")

    print("\nRegion Comparison")
    print(f"{name1}: {region1}")
    print(f"{name2}: {region2}")

def main():
    print("\n=== Country Info Tool ===")
    print("1. Single country info")
    print("2. Compare two countries")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        country_name = input("Enter country name: ").strip()

        if not country_name:
            print("Error: Country name cannot be empty.")
            return

        get_country_data(country_name)

    elif choice == "2":
        country1 = input("Enter first country: ").strip()
        country2 = input("Enter second country: ").strip()

        if not country1 or not country2:
            print("Error: Both country names are required.")
            return

        compare_countries(country1, country2)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()