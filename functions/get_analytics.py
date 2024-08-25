import requests
import json

def get_analytics(token_address):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    headers = {
        "Content-Type": "application/json",
    }

    # Payload con la variable tokenAddress
    payload = {
        "operationName": "GetCollectionAnalytics",
        "variables": {
            "tokenAddress": token_address
        },
        "query": """
        query GetCollectionAnalytics($tokenAddress: String!) {
          collectionAnalytics(tokenAddress: $tokenAddress) {
            ...CollectionAnalytic
            __typename
          }
        }

        fragment CollectionAnalytic on CollectionAnalytic {
          changesPct
          extraStats
          floorDepth
          mkpValueCharts
          tokenAddress
          totalSupply
          topOwners {
            ...TopOwner
            __typename
          }
          __typename
        }

        fragment TopOwner on TopOwner {
          owner
          ownerProfile {
            ...PublicProfileBrief
            __typename
          }
          quantity
          __typename
        }

        fragment PublicProfileBrief on PublicProfile {
          accountId
          addresses {
            ...Addresses
            __typename
          }
          activated
          name
          __typename
        }

        fragment Addresses on NetAddresses {
          ethereum
          ronin
          __typename
        }
        """
    }

    # Haciendo la solicitud POST
    response = requests.post(url, headers=headers, json=payload)

    # Comprobando si la solicitud fue exitosa
    if response.status_code == 200:
        # Procesando la respuesta JSON
        data = response.json()
        return data
    else:
        # Si ocurre un error, muestra el código de estado
        print(f"Error: {response.status_code}")
        return None
