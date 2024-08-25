import requests

def get_collection_metadata(token_address):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "operationName": "GetTokenMetadata",
        "variables": {
            "tokenAddress": token_address
        },
        "query": """
        query GetTokenMetadata($tokenAddress: String!) {
            tokenMetadata(tokenAddress: $tokenAddress) {
                ...TokenMetadataBrief
                __typename
            }
        }

        fragment TokenMetadataBrief on TokenMetadata {
            erc
            attributes {
                key
                displayType
                maxValue
                minValue
                values {
                    value
                    count
                    __typename
                }
                __typename
            }
            __typename
        }
        """
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
