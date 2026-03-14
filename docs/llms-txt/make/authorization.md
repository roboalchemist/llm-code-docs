# Source: https://developers.make.com/custom-apps-documentation/app-components/base/authorization.md

# Authorization

The Base section is used to set up authorization. Most services require the authorization key be sent either in `headers` or in the `qs` (query string). If you set the authorization in the base, all modules and Remote Procedure Calls (RPCs) will inherit it.

## Common methods of authorization

### API key in headers

```json
{
    "headers": {
        "x-api-key": "{{connection.apiKey}}"
    }
}
```

### API key in query string

```json
{
    "qs": {
        "apikey": "{{connection.apiKey}}"
    }
}
```

### OAuth 2 access token in headers

```json
{
    "headers": {
        "authorization": "Bearer {{connection.accessToken}}"
    }
}
```
