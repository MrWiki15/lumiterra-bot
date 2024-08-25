import requests

def get_erc1155_transfer_history( token_address, token_id ):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
      "Content-Type": "application/json",
    }
    
    payload = {
        "operationName": "GetERC1155TransferHistory",
        "variables": {
            "tokenId": token_id,
            "tokenAddress": token_address,
            "from": 0,
            "size": 10
        },
        "query": """
        query GetERC1155TransferHistory($tokenAddress: String, $slug: String, $tokenId: BigDecimal!, $from: Int!, $size: Int!) {
          erc1155Token(tokenAddress: $tokenAddress, slug: $slug, tokenId: $tokenId) {
            transferHistory(from: $from, size: $size) {
              total
              results {
                ...TransferRecordBrief
                __typename
              }
              __typename
            }
            __typename
          }
        }

        fragment TransferRecordBrief on TransferRecord {
          tokenId
          from
          to
          fromProfile {
            ...PublicProfileBrief
            __typename
          }
          toProfile {
            ...PublicProfileBrief
            __typename
          }
          timestamp
          txHash
          withPrice
          quantity
          paymentToken
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
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"