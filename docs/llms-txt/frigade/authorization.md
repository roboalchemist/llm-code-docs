# Source: https://docs.frigade.com/api-reference/authorization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Authorization

The Frigade API is secured using authorization tokens.
These api keys are used to authenticate your requests to the API. You can create and manage your api keys in the [Frigade Dashboard](https://app.frigade.com/developer).

Frigade provides two scopes of API keys: public and private. Below, we describe the differences between the two.

## Public API keys

This key can be exposed publicly (i.e. in your frontend code) and is used to access the public API endpoints.
These endpoints are prefixed with the `public` namespace in the API url (e.g. `https://api.frigade.com/v1/public/flows`).

## Private API keys

This key should be kept secret and is used to access the private API endpoints. It can be used to both access public and private API endpoints.

## Sample API request

The key should be passed in the `Authorization: Bearer <key>` header.
For example, to access the list of available flows in your account, you would make the following request:

```bash  theme={"system"}
curl -i -X GET \
   -H "Authorization:Bearer api_public_J3FNG3dJASDKLW98SN4KLOJHNTYUFGNVSK" \
 'https://api.frigade.com/v1/public/flows'
```
