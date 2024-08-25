import requests

def searsh_by_name(name):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "operationName": "GetERC1155TokensList",
        "variables": {
            "from": 0,
            "auctionType": "All",
            "size": 50,
            "sort": "PriceAsc",
            "rangeCriteria": [],
            "tokenAddress": "0xcc451977a4be9adee892f7e610fe3e3b3927b5a1",
            "name": name
        },
        "query": """
        query GetERC1155TokensList($tokenAddress: String, $slug: String, $criteria: [SearchCriteria!], $from: Int!, $size: Int!, $sort: SortBy, $auctionType: AuctionType, $name: String, $rangeCriteria: [RangeSearchCriteria!]) {
          erc1155Tokens(
            tokenAddress: $tokenAddress
            slug: $slug
            criteria: $criteria
            from: $from
            size: $size
            sort: $sort
            auctionType: $auctionType
            name: $name
            rangeCriteria: $rangeCriteria
          ) {
            total
            results {
              ...Erc1155TokenBrief
              __typename
            }
            __typename
          }
        }

        fragment Erc1155TokenBrief on Erc1155 {
          tokenAddress
          tokenId
          slug
          name
          image
          cdnImage
          video
          minPrice
          totalItems
          collectionMetadata
          isLocked
          __typename
        }
        """
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error in function searsh_by_name: {response.status_code}, {response.text}")
        return f"Error in function searsh_by_name: {response.status_code}, {response.text}"