# transaction lookup for Tether (USDT)

Make sure to replace 'YOUR_ETHERSCAN_API_KEY' with your actual Etherscan API key, which you can obtain by registering on the Etherscan website. Additionally, replace the address variable with the Tether address you want to look up transactions for.

This code sends a GET request to the Etherscan API's tokentx endpoint, specifying the Tether contract address and the user's address. It retrieves Tether transactions associated with the specified address and prints transaction details such as hash, sender, recipient, value (in USDT), and timestamp.

Please note that this code specifically targets Tether transactions on the Ethereum blockchain (ERC-20 tokens). If you're looking to retrieve Tether transactions on a different blockchain, you'll need to use an appropriate blockchain explorer API for that blockchain. Additionally, ensure compliance with the API provider's usage policies and rate limits.
