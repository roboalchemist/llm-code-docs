# Source: https://docs.firehydrant.com/reference/firehydrant-api.md

# FireHydrant API

The FireHydrant API is based around REST. It uses Bearer token authentication and returns JSON responses. You can use the FireHydrant API to configure integrations, define incidents, and set up webhooks--anything you can do on the FireHydrant UI.

* [View your API keys](https://app.firehydrant.io/settings/api_keys)

## Base API endpoint

`https://api.firehydrant.io/v1`

Read only requests:

`https://api-read.firehydrant.io/v1`

Note that the read-only endpoint has a much longer timeout for retrieving more complex data, but may lag behind the primary endpoint by as much as 30s.  Any attempt to send POST, PATCH, PUT, or DELETE methods will result in an error.

## Current version

`v1`

## Authentication

All requests to the FireHydrant API require an `Authorization` header with the value set to `Bearer {token}`. FireHydrant supports API keys to act on behalf of a computer instead of a user's account. This prevents integrations from breaking when people leave your organization or their token is revoked. See the API keys section (below) for more information on this.

An example of a header to authenticate against FireHydrant would look like:

```
Authorization: Bearer fhb-thisismykey
```

## API Keys

To access the FireHydrant API, you must authenticate with an API key (requires **Owner** permissions in your organization to manage). API keys allow you to interact with the FireHydrant API by using token-based authentication. To create keys, log in to your organization and refer to the [API keys page](https://app.firehydrant.io/settings/api_keys).

Every API request/endpoint is authenticated unless specified otherwise.

### Rate Limiting

Currently, requests made with API keys are rate limited on a per-account level. If your account has multiple API keys then the rate limit is shared across all of them. As of February 7th, 2023, the rate limit is 50 requests per account every 10 seconds, or 300 requests per minute.

Rate limited responses will be served with a `429` status code and a JSON body of:

```json
{"error": "rate limit exceeded"}
```

and headers of:

```
"RateLimit-Limit" -> the maximum number of requests in the rate limit pool
"Retry-After" -> the number of seconds to wait before trying again
```

## How lists are returned

API lists are returned as arrays. A paginated entity in FireHydrant will return two top-level keys in the response object: a data key and a pagination key.

### Paginated requests

The `data` key is returned as an array. Each item in the array includes all of the entity data specified in the API endpoint. (The per-page default for the array is 20 items.)

Pagination is the second key (`pagination`) returned in the overall response body. It includes medtadata around the current page, total count of items, and options to go to the next and previous page. All of the specifications returned in the pagination object are available as URL parameters. So if you want to specify, for example, going to the second page of a response, you can send a request to the same endpoint but pass the URL parameter **page=2**.

For example, you might request **[https://api.firehydrant.io/v1/environments/](https://api.firehydrant.io/v1/environments/)** to retrieve environments data. The JSON returned contains the above-mentioned data section and pagination section. The data section includes various details about an incident, such as the environment name, description, and when it was created.

```json
{
  "data": [
    {
      "id": "f8125cf4-b3a7-4f88-b5ab-57a60b9ed89b",
      "name": "Production - GCP",
      "description": "",
      "created_at": "2021-02-17T20:02:10.679Z"
    },
    {
      "id": "a69f1f58-af77-4708-802d-7e73c0bf261c",
      "name": "Staging",
      "description": "",
      "created_at": "2021-04-16T13:41:59.418Z"
    }
  ],
  "pagination": {
    "count": 2,
    "page": 1,
    "items": 2,
    "pages": 1,
    "last": 1,
    "prev": null,
    "next": null
  }
}
```

To request the second page, you'd request the same endpoint with the additional query parameter of `page` in the URL:

```
GET https://api.firehydrant.io/v1/environments?page=2
```

If you need to modify the number of records coming back from FireHydrant, you can use the `per_page` parameter (max is 200):

```
GET https://api.firehydrant.io/v1/environments?per_page=50
```