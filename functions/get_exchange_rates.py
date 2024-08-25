#Used to view prices of each NFT in Sky Mavis
import requests

def get_exchange_rates():
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    # Create the POST request payload
    payload = {
        "query": """
        {
            exchangeRate {
                eth {
                    usd
                    __typename
                }
                slp {
                    usd
                    __typename
                }
                ron {
                    usd
                    __typename
                }
                axs {
                    usd
                    __typename
                }
                usd {
                    usd
                    __typename
                }
                __typename
            }
        }
        """
    }

    # Make POST request
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
