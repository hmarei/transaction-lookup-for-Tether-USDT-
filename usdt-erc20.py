import requests

def get_tether_transactions(address, api_key):
    # Etherscan API endpoint for Tether transactions
    url = f"https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}"
    
    # Sending a GET request to the Etherscan API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        
        # Checking if the API returned the expected data
        if data['status'] == "1":
            # Extracting and returning the Tether transactions
            return data['result']
        else:
            print("Error: Unable to retrieve Tether transactions.")
    else:
        print("Error: Unable to connect to the Etherscan API.")

# Example usage:
address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # Sample Tether address (ERC-20)
api_key = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key

transactions = get_tether_transactions(address, api_key)

if transactions:
    print("Tether Transactions:")
    for tx in transactions:
        print("Transaction Hash:", tx['hash'])
        print("From:", tx['from'])
        print("To:", tx['to'])
        print("Value (USDT):", tx['value'])
        print("Timestamp:", tx['timeStamp'])
        print("-------------------------")
else:
    print("No Tether transactions found for the specified address.")
