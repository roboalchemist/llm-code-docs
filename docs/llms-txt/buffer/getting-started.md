# Source: https://developers.buffer.com/guides/getting-started.md

Buffer's API is built using GraphQL. If you are new to GraphQL, its worth checking out the [official GraphQL documentation](https://graphql.org/learn/) and [tutorial offered by Apollo's](https://www.apollographql.com/tutorials/) to learn the foundations for building for our API.

## Register for API Access

To access our API you'll need a Buffer Account and an API token. If you don't have an account yet, you can sign up for one [here](https://buffer.com/signup).

Once you have an Account, you can create an API Key in the [API settings](https://publish.buffer.com/settings/api) of your account.

## What the API supports

Your API Key can be used to perform actions against **your own Buffer account**. Through this we currently support the following operations:

- Post Creation
- Post Retrieval
- Idea Creations
- Account Retrieval
- Organizations Retrieval
- Channels Retrieval

## Endpoint

Our GraphQL API can be accessed via the following endpoint:

```
https://api.buffer.com
```

If you are looking to make GraphQL calls using postman or any other HTTP request tool, you direct requests to the above endpoint and follow [this](https://learning.postman.com/docs/sending-requests/graphql/graphql-overview/) guide.

## Authorization

Requests must be authenticated via the `Authorization` header. You will need to provide your API token with the correct permissions using the `Bearer` formatting.

<!-- AUTH_CODE_EXAMPLES -->

## Making your first request

To make your first request, you can use the following example query to fetch your account and Organization:

<!-- FIRST_REQUEST_CODE_EXAMPLES -->

Once you have your organizations, you can use the desired organization ID to make further requests to fetch profiles, posts, and other data associated with your organization.