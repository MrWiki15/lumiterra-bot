import requests

def get_erc1155_detail_token(token_id, token_address):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "operationName": "GetERC1155TokenDetail",
        "variables": {
            "tokenId": token_id,
            "tokenAddress": token_address
        },
        "query": """
        query GetERC1155TokenDetail($tokenAddress: String, $slug: String, $tokenId: BigDecimal!) {
          erc1155Token(tokenAddress: $tokenAddress, slug: $slug, tokenId: $tokenId) {
            ...Erc1155Token
            __typename
          }
        }
        
        fragment Erc1155Token on Erc1155 {
          totalListing
          totalItemsListing
          totalItems
          totalOwners
          tokenId
          tokenAddress
          slug
          name
          attributes
          image
          cdnImage
          video
          animationUrl
          minPrice
          transferHistory(from: 0, size: 1) {
            total
            results {
              ...TransferRecordBrief
              __typename
            }
            __typename
          }
          traitDistribution {
            ...TokenTrait
            __typename
          }
          collectionMetadata
          isLocked
          metadataLastUpdated
          description
          __typename
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
        
        fragment TokenTrait on TokenTrait {
          key
          value
          count
          percentage
          displayType
          maxValue
          __typename
        }
        """
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}