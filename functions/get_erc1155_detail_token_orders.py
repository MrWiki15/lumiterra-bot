import requests

def get_erc1155_detail_token_orders(token_address, token_id, from_index=0, size=5, show_invalid=False, sort="PriceAsc"):
    url = "https://marketplace-graphql.skymavis.com/graphql"
    
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "es-ES,es;q=0.9",
        "Authorization": "",  # Agrega tu token de autorización si es necesario
        "Content-Type": "application/json",
        "Origin": "https://marketplace.skymavis.com",
        "Referer": "https://marketplace.skymavis.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"
    }
    
    payload = {
        "operationName": "GetErc1155Orders",
        "variables": {
            "tokenAddress": token_address,
            "tokenId": token_id,
            "from": from_index,
            "size": size,
            "showInvalid": show_invalid,
            "sort": sort
        },
        "query": """
        query GetErc1155Orders($tokenAddress: String, $slug: String, $tokenId: BigDecimal!, $from: Int!, $size: Int!, $maker: String, $showInvalid: Boolean!, $sort: Erc1155SortBy!) {
          erc1155Token(tokenAddress: $tokenAddress, slug: $slug, tokenId: $tokenId) {
            orders(
              maker: $maker
              from: $from
              size: $size
              showInvalid: $showInvalid
              sort: $sort
            ) {
              ...OrderInfo
              __typename
            }
            __typename
          }
        }

        fragment OrderInfo on Order {
          id
          maker
          kind
          assets {
            ...AssetInfo
            __typename
          }
          expiredAt
          paymentToken
          startedAt
          basePrice
          expectedState
          nonce
          marketFeePercentage
          signature
          hash
          duration
          timeLeft
          currentPrice
          suggestedPrice
          makerProfile {
            ...PublicProfileBrief
            __typename
          }
          orderStatus
          orderQuantity {
            orderId
            quantity
            remainingQuantity
            availableQuantity
            __typename
          }
          __typename
        }

        fragment AssetInfo on Asset {
          erc
          address
          id
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
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
