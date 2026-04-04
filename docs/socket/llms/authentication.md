# Source: https://docs.socket.dev/reference/authentication.md

# Authentication

This page will explain how Socket API authentication works

Socket's API uses organization tokens for authenticating requests.

Organization tokens can be created in your Socket organization settings and are scoped to the organization that you create them in.

Authenticating requests to the Socket API can be done by passing the API token as a Bearer token in the `Authorization` header, or as the username field of an HTTP Basic authentication header.

To authenticate using a Bearer token, pass the API token in the Authorization header after the work "Bearer":

```
curl --request GET \
     --url 'https://api.socket.dev/v0/orgs/org_slug/full-scans' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer your_api_key'
```

To authenticate a request, provide your API token through HTTP Basic authentication in the request. The API token is used as the `username` and the `password` is left blank (ie. `your_api_key:` encoded in Base64).

An example is shown below:

```shell cURL
curl https://api.socket.dev/v0/quota -X GET -u "your_api_key:"
```