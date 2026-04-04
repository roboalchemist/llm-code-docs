# Source: https://docs.infrahub.app/guides/managing-api-tokens.md

# Managing API tokens

API tokens can be used as an authentication mechanism for Infrahub's REST- and GraphQL API, the Python SDK and infrahubctl.

* Via the Web Interface
* Via the GraphQL Interface

1. Login to Infrahub's web interface as an administrator.
2. Click on the user in the left side menu.
3. Navigate to the **Account settings**.
4. In the user Profile page, click on **Tokens** tab. ![Profile Tokens](/assets/images/profile_tokens-b6ffd0794847c56959af9a2b1a51c4af.png)
5. Click **+ Add Account Token**. ![Creating an API Token](/assets/images/profile_tokens_create-7407c11fb07c99f72b504000421e3a63.png)
6. Fill in the details and click **Save**.
7. Copy the generated token and store in a safe location. ![Copy API Token](/assets/images/profile_tokens_copy-99004d3c7729a274ddd9eb04df6390bc.png)
8. Deleting a token can be achieved by selecting the trash icon on the token table item.

## Creating a new API Token[​](#creating-a-new-api-token "Direct link to Creating a new API Token")

In the GraphQL sandbox, execute the following mutation, replace the name of the token in the mutation with a value that is appropriate for your use case:

```
mutation {
  InfrahubAccountTokenCreate(data: {name: "token name"}) {
    object {
      token {
        value
      }
    }
  }
}
```

The result of the query will show you the value of the token that was generated for the token. Store the token in a secure location, as there will be no way to retrieve the token from Infrahub at a later stage.

## Listing existing API Tokens for a user[​](#listing-existing-api-tokens-for-a-user "Direct link to Listing existing API Tokens for a user")

In the GraphQL sandbox, execute the following query:

```
query {
  InfrahubAccountToken {
    edges {
      node {
        name
        expiration
        id
      }
    }
  }
}
```

## Deleting an API token for a user[​](#deleting-an-api-token-for-a-user "Direct link to Deleting an API token for a user")

In the GraphQL sandbox, execute the following mutation, replace the id of the token in the mutation with the id of the token that you want to delete:

```
mutation {
  InfrahubAccountTokenDelete(data: {id: "17d8cde3-d36b-a0a3-370e-c51707234f19"}) {
    ok
  }
}
```

## Using API tokens[​](#using-api-tokens "Direct link to Using API tokens")

info

While using the API, the authentication token must be provided in the header:

```
X-INFRAHUB-KEY: 06438eb2-8019-4776-878c-0941b1f1d1ec
```
