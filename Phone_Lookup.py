# phone_lookup.py
import requests
import sys

API_KEY = 'YOUR_NUMVERIFY_API_KEY'
API_URL = 'http://apilayer.net/api/validate'

def lookup_phone_number(phone_number):
    params = {
        'access_key': API_KEY,
        'number': phone_number
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if data['valid']:
        print(f"Phone Number: {data['number']}")
        print(f"Local Format: {data['local_format']}")
        print(f"International Format: {data['international_format']}")
        print(f"Country: {data['country_name']}")
        print(f"Location: {data['location']}")
        print(f"Carrier: {data['carrier']}")
        print(f"Line Type: {data['line_type']}")
    else:
        print("Invalid phone number.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python phone_lookup.py <phone_number>")
        sys.exit(1)

    phone_number = sys.argv[1]
    lookup_phone_number(phone_number)

if __name__ == '__main__':
    main()