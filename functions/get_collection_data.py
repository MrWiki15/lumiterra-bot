import requests

def get_collection_data(token_address):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "operationName": "GetTokenData",
        "variables": {
            "tokenAddress": token_address
        },
        "query": """
        query GetTokenData($tokenAddress: String, $slug: String) {
            tokenData(tokenAddress: $tokenAddress, slug: $slug) {
                ...TokenData
                allowedPaymentTokens
                __typename
            }
        }
        
        fragment TokenData on TokenData {
            tokenAddress
            slug
            collectionMetadata
            volumeAllTime
            totalOwners
            totalItems
            totalListing
            minPrice
            erc
            groupTraits
            content
            __typename
        }
        """
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")