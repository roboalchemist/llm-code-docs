# Source: https://docs.carv.io/carv-ecosystem/carv-play/carv-intro/api-verified-quest-graphql.md

# API-Verified Quest (GraphQL)

## Introduction

GraphQL verification takes a single wallet address or email as input and outputs 0(false)/1(true) to indicate whether the wallet address is eligible. It requires 3 fields to be filled in: **GraphQL Endpoint (HTTPs)**, **Query** and **Expression**.

## Sequence Diagram

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2F6DyBO2kWzy7gudpots69%2Fimage.png?alt=media&#x26;token=e06e8f8e-81ba-40c6-97b3-25ebafb4e250" alt=""><figcaption></figcaption></figure>

## GraphQL Endpoint (HTTPs)

It's the HTTPs endpoint where Subgraph queries go to, see the example below.&#x20;

{% hint style="warning" %}
NOTE: If you saw an error when testing the API, check if the endpoint is a valid GraphQL API endpoint. Common misconfigurations include:

* &#x20;Incorrectly used a GraphQL *playground* url, that usually ends with `/graph`
* &#x20;The GraphQL endpoint does now allow CORS from carv.io.
  {% endhint %}

## Query

The GraphQL query requires a single wallet address as input. In the dashboard, once you finish your query, fill in a test address and click 'Run' button to check if the query's return is good.

## Expression

A JavaScript (ES6) function with this type signature: `(object) => int`. The function must be anonymous, which means that the first line of the expression should be like `function(data) {`, instead of `let expression = (data) => {`.

The function should return either number 1 or 0, representing if the address has completed the quest. Behind the scenes, first, we send the query with the user's address to the GraphQL endpoint, and then we will apply the function against the 'data' field of the response. If the returned value is 1, then user is considered to have completed this quest, otherwise not.

Once the query's output is good, click 'Run' button to check if expression processes the query's output correctly.

## Subgraph Examples

**Endpoint**

```
https://api.thegraph.com/subgraphs/name/carv-protocol/carvachievementsonbnb
```

**Query**

```graphql
query info($address: String!) {
  # write you query here 
    erc1155Balances(
    first: 1
    where: {token_: {identifier: "1"}, account_: {id: $address}}
  ) {
    account {
      id
    }
    token {
      id
      identifier
    }
  }
}

# test address: 0x357A5eE000B5cA0935Aad7bb4Cb96E8AcAf46727
```

**Query Output**

```json
{
  "erc1155Balances": [
    {
      "account": {
        "id": "0x357a5ee000b5ca0935aad7bb4cb96e8acaf46727"
      },
      "token": {
        "id": "0xc2f24ffe96a69e381a747dc73fcd51492e29a0a4/0x1",
        "identifier": "1"
      }
    }
  ]
}
```

**Expression**

```javascript
function verify(data){
    if (data.erc1155Balances.length > 0){
        return true
    } else {
        return false
    }
}
```

**Expression Output**

```
true
```
