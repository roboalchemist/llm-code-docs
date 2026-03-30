# Source: https://developers.make.com/custom-apps-documentation/best-practices/base/authorization-and-sanitization.md

# Authorization and sanitization

The Base section should also have [authorization](https://developers.make.com/custom-apps-documentation/app-components/base/authorization) and [sanitization](https://developers.make.com/custom-apps-documentation/app-components/base/sanitization) that is common for all modules. The authorization should use the API key, access token, or username and password entered in the connection. The sanitization should hide all these sensitive parameters.

{% tabs %}
{% tab title="API Key" %}

```javascript
{
...
    "headers": {
        "Authorization": "Token {{connection.apiKey}}"
    },
    "log": {
        "sanitize": [
            "request.headers.authorization"
        ]
    }
...
}
```

{% endtab %}

{% tab title="Access Token" %}

```javascript
{
...
    "qs": {
        "access_token": "{{connection.accessToken}}"
    },
    "log": {
        "sanitize": [
            "request.qs.access_token"
        ]
    }
...
}
```

{% endtab %}

{% tab title="Basic auth" %}

```javascript
{
...
    "headers": {
        "authorization": "Basic {{base64(connection.username + ':' + connection.password)}}"
    },
    "log": {
        "sanitize": [
            "request.headers.authorization"
        ]
    }
...    
}
```

{% endtab %}

{% tab title="Secret in request body" %}

```javascript
{
...
    "body": "There is something {{parameters.secret}} hidden here.",
    "type": "raw",
    "log": {
        "sanitize": [
            "request.body<parameters.secret>"
        ]
    }
...
}
```

{% endtab %}
{% endtabs %}
