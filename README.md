# Phone Number Lookup Tool

## Introduction
A simple phone number lookup tool built with Python using the `numverify` API. It validates phone numbers and retrieves information such as carrier, location, and line type.

## Features
- Validate phone numbers
- Retrieve carrier information
- Retrieve location information (country, city)
- Command-line interface

## Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/GloryWasHere/Phone-Lookup
    ```
2. Navigate to the project directory:
    ```sh
    cd phone-number-lookup
    ```
3. Create and activate a virtual environment:
    ```sh
    python3 -m venv phone_lookup_env
    source phone_lookup_env/bin/activate
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the phone lookup tool:
```sh
python phone_lookup.py <phone_number>
