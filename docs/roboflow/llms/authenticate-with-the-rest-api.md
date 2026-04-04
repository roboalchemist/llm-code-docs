# Source: https://docs.roboflow.com/developer/rest-api/authenticate-with-the-rest-api.md

# Authenticate with the REST API

Most Roboflow API endpoints require an API key. You can authenticate your request through the `api_key` parameter in the body and the query, via an authentication header, or with a query parameter.

### Authentication Header

We recommend you authenticate with the REST API by sending your API key as a bearer authentication header.

Here is an example of the header structure:

```
Authorization: Bearer abcdefghijklmnopqrstuvwxyz
```

### Body Parameter

You can send your API key as a parameter within a JSON request body of POST endpoints.

Here is an example of using an API key in the body of a request:

```json
{
    "api_key":"abcdefghijklmnopqrstuvwxyz"
}
```

### Query Parameter

You can also send your API key through a query parameter in the URL of your request.

We recommend against this method of authentication for production applications for security reasons. We instead recommend sending authentication headers.

Here is an example of an API key sent in a query parameter:

```
https://api.roboflow.com?api_key=abcdefghijklmnopqrstuvwxyz
```
