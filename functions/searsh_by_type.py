import requests

def searsh_by_type(token_address, 
                   from_index=0, 
                   size=50, 
                   sort="PriceAsc", 
                   auction_type="All", 
                   criteria=list):
    
    url = "https://marketplace-graphql.skymavis.com/graphql"

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "operationName": "GetERC1155TokensList",
        "variables": {
            "from": from_index,
            "auctionType": auction_type,
            "size": size,
            "sort": sort,
            "criteria": criteria if criteria else [],
            "rangeCriteria": [],
            "tokenAddress": token_address
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
        return f"Error en la función searsh_by_type: {response.status_code}, {response.text}"
