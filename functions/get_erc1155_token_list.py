import requests

def get_erc1155_token_list(token_address, from_index=0, size=50, sort="PriceAsc", auction_type="All"):
    url = "https://marketplace-graphql.skymavis.com/graphql"

    # Cabeceras de la solicitud
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
    }

    # Payload de la solicitud
    payload = {
        "operationName": "GetERC1155TokensList",
        "variables": {
            "from": from_index,
            "auctionType": auction_type,
            "size": size,
            "sort": sort,
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

    # Hacer la solicitud POST
    response = requests.post(url, json=payload, headers=headers)

    # Procesar la respuesta
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}, {response.text}"