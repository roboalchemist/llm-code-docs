<!-- Source: https://docs.verda.com/inference/authorization.md -->

# Authorization

## Overview

Our API uses bearer token authentication for securing access and ensuring that only authorized users can perform certain operations. This authentication method is particularly implemented for all our inference endpoint APIs, making the bearer token universally applicable across these services. This approach simplifies the authentication process for our REST API by avoiding session-based authentication and providing stateless communication.

## Obtaining a Bearer Token

To use our Inference API you will first need to obtain a bearer token. Bearer tokens are unique identifiers that ensure secure access to our API endpoints.

### Steps to Generate a Bearer Token

1. Go to **Keys -> Inference API Keys**
2. Click on **Create** button.
3. Once generated, your API key will serve as your bearer token and is valid for all inference endpoint APIs.

## Using the Bearer Token

After obtaining your bearer token, you can use it to authenticate your requests to any of the inference endpoint APIs. Each request to our API should include the bearer token in the `Authorization` header.

## Security Notes

* Keep your bearer token secure and never expose it in client-side code.
* If you suspect that your token has been compromised, regenerate a new token immediately.
