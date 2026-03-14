# Source: https://developers.make.com/custom-apps-documentation/app-components/connections/oauth2.md

# OAuth 2.0

Before you start configuring your OAuth 2.0 connection, create an app on a third-party service.

When creating an app, use:

* `https://www.make.com/oauth/cb/app` as a callback URL together with the `oauth.makeRedirectUri` variable, or:
* `https://www.make.com/oauth/cb/app` as a callback URL together with the `oauth.localRedirectUri` variable, if you are going to request approval of your app, or:
* `https://www.integromat.com/oauth/cb/app` as an old callback URL together with the `oauth.redirectUri` variable. This option is not suggested for new apps.

## OAuth 2.0 authentication process

OAuth 2.0 authentication processes consist of multiple steps that need to be defined in the Connection communication. The communication should be a collection with the keys below. You can use the keys the particular flow requires and disregard those that are unnecessary.

<table><thead><tr><th width="172" valign="top">Key</th><th width="201.33333333333331" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>preauthorize</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that should be executed prior to the <code>authorize</code> directive.</td></tr><tr><td valign="top"><code>authorize</code></td><td valign="top">Request specification</td><td valign="top">Describes the authorization process.</td></tr><tr><td valign="top"><code>token</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that exchanges credentials for tokens.</td></tr><tr><td valign="top"><code>info</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that validates a connection. The most common way to validate the connection is to call an API’s method to get a user’s information. Most of the APIs have such a method. The <code>info</code> directive can be used to store account's metadata.</td></tr><tr><td valign="top"><code>refresh</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that refreshes an access token.</td></tr><tr><td valign="top"><code>invalidate</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that invalidates acquired access token.</td></tr></tbody></table>

Each section is responsible for executing its part in the OAuth 2.0 flow.

You can describe the initial OAuth 2.0 flow as follows:

```
preauthorize => authorize => token => info
```

with `preauthorize` and `info` sections being optional, and `refresh` and `invalidate` not being a part of the initial OAuth 2.0 flow.

{% hint style="info" %}
If the `authorize` directive isn't used, the `condition` in the`token` directive has to be set to `true.` Otherwise, the token directive will not be successfully triggered.
{% endhint %}

## Components

### Communication

For more information, see the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api) documentation.

* `aws` directive is not available
* `pagination` directive is not available
* `response.limit` is not available
* `response.iterate` directive is not available
* `response.output` is not available
* `response` is extended with `data`
* `response` is extended with `expires`

#### response.data

The `data` directive saves data to the connection so that it can be later accessed from a module through the `connection` variable. It functions similarly to the `temp` directive, except that `data` is persisted to the connection.

{% tabs %}
{% tab title="Code example" %}

```json
{
    "response": {
        "data": {
            "accessToken": "{{body.token}}"
        }
    }
}
```

{% endtab %}

{% tab title="Code example used to access later" %}

```json
{
    "url": "http://example.com",
    "qs": {
        "token": "{{connection.accessToken}}"
    }
}
```

{% hint style="info" %}
This `accessToken` can be later accessed in any module that uses this connection or in the app base.
{% endhint %}
{% endtab %}
{% endtabs %}

#### response.expires

The `expires` directive indicates the expiration datetime for tokens.

It's generally used only in the `token` and `refresh` blocks of the connection communication and there are two variations:

* `response.data.expires` is used to trigger the token refresh request.
* `response.expires` is used to prompt the user to manually reauthorize the connection. This is necessary when the access token can no longer be automatically refreshed, such as when a refresh token expires. This is generally defined by the `refresh_expires_in` value in the response from the access token request, or specified in the documentation.

When the date is reached, the connection needs to be reauthorized manually, either from a scenario or the Connections tab.

{% tabs %}
{% tab title="Connection" %}

```json
"token": {
    ...
    "response": {
        "data": {
          "expires": "{{addSeconds(now, body.expires_in)}}" // the access token expiration datetime
        }
        "expires": "{{addSeconds(now, body.refresh_expires_in)}}" // the refresh token expiration datetime
    }
}
```

{% hint style="info" %}
If `refresh_expires_in` is not included in the reply but the API documentation mentions refresh tokens expire after a certain time, you should use that value. For example, for a year: `"{{addYears(now, 1)}}"`
{% endhint %}
{% endtab %}
{% endtabs %}

### Parameters​ <a href="#parameters" id="parameters"></a>

[Parameters](https://developers.make.com/custom-apps-documentation/block-elements/parameters) the user needs to provide when setting up a new connection.

### Default scope

[Default scope](https://developers.make.com/custom-apps-documentation/component-blocks/scope) for every new connection.

### Scope list

Collection of available [scopes](https://developers.make.com/custom-apps-documentation/component-blocks/scopes).

### ​Common data​ <a href="#common-data" id="common-data"></a>

[Non-user-specific sensitive values](https://developers.make.com/custom-apps-documentation/app-components/connections) like secrets.

## Available IML variables

These IML variables are available for you to use everywhere in this module:

<table><thead><tr><th width="233.4444580078125" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>temp</code></td><td valign="top">Contains custom variables created via <code>temp</code> directive.</td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">Contains the connection’s input parameters.</td></tr><tr><td valign="top"><code>common</code></td><td valign="top">Contains the connection’s common data collection.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">Contains the connection’s data collection.</td></tr><tr><td valign="top"><code>oauth.scope</code></td><td valign="top">Contains an array of scope required to be passed to the OAuth 2.0 authorization process.</td></tr><tr><td valign="top"><code>oauth.redirectUri</code></td><td valign="top">Contains the redirect URL for the OAuth 2.0 authorization process in this format: <code>https://www.integromat.com/oauth/cb/app</code></td></tr><tr><td valign="top"><code>oauth.localRedirectUri</code></td><td valign="top">Contains the redirect URL for the OAuth 2.0 authorization process in this format: <code>https://www.make.com/oauth/cb/app</code> or this format:<br><code>https://www.private-instance.com/oauth/cb/app</code></td></tr><tr><td valign="top"><code>oauth.makeRedirectUri</code></td><td valign="top">Contains the redirect URL for the OAuth 2.0 authorization process in this format: <code>https://www.make.com/oauth/cb/app</code></td></tr></tbody></table>

## Code grant example

{% tabs %}
{% tab title="Common data" %}

```json
{
    "clientId": "3j2h5g234iuy75467k3g457kj34bl",
    "clientSecret": "m034f8756y0cw3k8t7hkxl0esybv"
}
```

{% endtab %}

{% tab title="Default scope" %}

```json
[ "user.read", "offline_access" ]
```

{% endtab %}

{% tab title="Parameters" %}

```json
[
    {
        "name": "clientId",
        "type": "text",
        "label": "Client ID",
        "advanced": true,
        "editable": true
    },
    {
        "name": "clientSecret",
        "type": "password",
        "label": "Client secret",
        "advanced": true,
        "editable": true
    },
    {
        "name": "scopes",
        "label": "Additional scopes",
        "type": "array",
        "labels": {
            "add": "Add scope"
        },
        "spec": {
            "type": "text",
            "label": "Scope"
        },
        "help": "Use this to get access to extra scopes.",
        "advanced": true,
        "editable": true
    }
]
```

{% endtab %}

{% tab title="Communication" %}

```json
{
    "authorize": {
        "url": "https://example.com/authorize",
        "qs": {
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.scopes, emptyarray))), ' ')}}",
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "redirect_uri": "{{oauth.localRedirectUri}}",
            "response_type": "code"
            // You generally don't need to specify the 'state' value, Make handles that for you.
        },

        "response": {
            "temp": {
                "code": "{{query.code}}"
            }
        }
    },
    
    "token": {
        "url": "https://example.com/token",
        "method": "POST",
        "body": {
            "code": "{{temp.code}}",
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "grant_type": "authorization_code",
            "redirect_uri": "{{oauth.localRedirectUri}}",
            "client_secret": "{{ifempty(parameters.clientSecret, common.clientSecret)}}"
        },
        "type": "urlencoded",

        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}",
                "refreshToken": "{{body.refresh_token}}"
            },
            "expires": "{{addSeconds(now, body.refresh_expires_in)}}" // refresh token expiration. The connection needs manual reauthorization once this date is reached.
        },
        
        "log": {
            "sanitize": [
                "request.body.code",
                "request.body.client_secret",
                "response.body.access_token",
                "response.body.refresh_token"
            ]
        }
    },
    
    "refresh": {
        "condition": "{{data.expires < addMinutes(now, 15)}}",
        "url": "https://example.com/token",
        "method": "POST",
        "body": {
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "grant_type": "refresh_token",
            "client_secret": "{{ifempty(parameters.clientSecret, common.clientSecret)}}",
            "refresh_token": "{{data.refreshToken}}"
        },
        "type": "urlencoded",
        
        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}",
                "refreshToken": "{{body.refresh_token}}"
            }
        },
        
        "log": {
            "sanitize": [
                "request.body.client_secret",
                "request.body.refresh_token",
                "response.body.access_token",
                "response.body.refresh_token"
            ]
        }
    },
    
    "info": {
        "url": "https://example.com/me",
        "headers": {
            "authorization": "Bearer {{connection.accessToken}}"
        },
        
        "response": {
            "metadata": { // This is added under the connection name in the UI to make it easier for the user to identify it.
                "type": "text",
                "value": "{{body.data.name}} ({{body.data.email}})"
            },
            "uid": "{{body.data.id}}" // This is only needed if your app uses Shared webhooks. The ID allows Make to match the payloads del;ivered to the shared webhook to the correct recipients.
        },
        
        "log": {
            "sanitize": [ "request.headers.authorization" ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## OAuth 2.0 code grant example with PCKE

{% tabs %}
{% tab title="Common data" %}

```json
{
    "clientId": "3j2h5g234iuy75467k3g457kj34bl",
    "clientSecret": "m034f8756y0cw3k8t7hkxl0esybv"
}
```

{% endtab %}

{% tab title="Default scope" %}

```json
[ "user.read", "offline_access" ]
```

{% endtab %}

{% tab title="Parameters" %}

```json
[
    {
        "name": "clientId",
        "type": "text",
        "label": "Client ID",
        "advanced": true,
        "editable": true
    },
    {
        "name": "clientSecret",
        "type": "password",
        "label": "Client secret",
        "advanced": true,
        "editable": true
    },
    {
        "name": "scopes",
        "label": "Additional scopes",
        "type": "array",
        "labels": {
            "add": "Add scope"
        },
        "spec": {
            "type": "text",
            "label": "Scope"
        },
        "help": "Use this to get access to extra scopes.",
        "advanced": true,
        "editable": true
    }
]
```

{% endtab %}

{% tab title="Communication" %}

```json
{
    "authorize": {
        "temp": {
            "code_verifier": "{{uuid}}"
        },
        "qs": {
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.scopes, emptyarray))), ' ')}}",
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "code_challenge": "{{base64url(sha256(temp.code_verifier, 'base64'))}}",
            "code_challenge_method": "S256",
            "redirect_uri": "{{oauth.redirectUri}}",
            "response_type": "code"
        },
        "url": "https://example.com/authorize",

        "response": {
            "temp": {
                "code": "{{query.code}}"
            }
        }
    },

    "token": {
        "url": "https://example.com/token",
        "body": {
            "code": "{{temp.code}}",
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "grant_type": "authorization_code",
            "redirect_uri": "{{oauth.redirectUri}}",
            "code_verifier": "{{temp.code_verifier}}"
        },
        "type": "urlencoded",
        "method": "POST",

        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}",
                "refreshToken": "{{body.refresh_token}}"
            },
            "expires": "{{addSeconds(now, body.refresh_expires_in)}}" // refresh token expiration. The connection needs manual reauthorization once this date is reached.
        },

        "log": {
            "sanitize": [
                "request.body.code",
                "response.body.access_token",
                "response.body.refresh_token"
            ]
        }
    },

    "refresh": {
        "condition": "{{data.expires < addMinutes(now, 15)}}",
        "url": "https://example.com/token",
        "method": "POST",
        "body": {
            "grant_type": "refresh_token",
            "client_id": "{{ifempty(parameters.clientId, common.clientId)}}",
            "refresh_token": "{{data.refreshToken}}"
        },
        "type": "urlencoded",

        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}",
                "refreshToken": "{{body.refresh_token}}"
            }
        },

        "log": {
            "sanitize": [
                "request.body.refresh_token",
                "response.body.access_token",
                "response.body.refresh_token"
            ]
        }
    },
    "info": {
        "url": "https://example.com/v1/info",
        "headers": {
            "authorization": "Bearer {{connection.accessToken}}"
        },

        "response": {
            "error": {
                "message": "[{{statusCode}}] {{body.error}}"
            },
            "metadata": { // This is added under the connection name in the UI to make it easier for the user to identify it.
                "type": "text",
                "value": "{{body.user.fullName}} ({{body.user.email}})"
            },
            "data": {
                "userId": "{{body.user.id}}"
            },
            "uid": "{{body.user.id}}" // This is only needed if your app uses Shared webhooks. The ID allows Make to match the payloads del;ivered to the shared webhook to the correct recipients.
        },

        "log": {
            "sanitize": [
                "request.headers.authorization"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Client credentials example

{% tabs %}
{% tab title="Common data" %}
{% hint style="info" %}
In the client credentials flow, the user must provide the Client ID and secret, so no common data is defined.
{% endhint %}
{% endtab %}

{% tab title="Default scope" %}

```json
[ "user.read", "offline_access" ]
```

{% endtab %}

{% tab title="Parameters" %}

```json
[
    {
        "name": "clientId",
        "type": "text",
        "label": "Client ID",
        "required": true,
        "editable": true
    },
    {
        "name": "clientSecret",
        "type": "password",
        "label": "Client secret",
        "required": true,
        "editable": true
    },
    {
        "name": "scopes",
        "label": "Additional scopes",
        "type": "array",
        "labels": {
            "add": "Add scope"
        },
        "spec": {
            "type": "text",
            "label": "Scope"
        },
        "help": "Use this to get access to extra scopes.",
        "advanced": true,
        "editable": true
    }
]
```

{% endtab %}

{% tab title="Communication" %}

```json
{
    "token": {
        "url": "https://example.com/token",
        "body": {
            "grant_type": "client_credentials",
            "client_id": "{{parameters.clientId}}",
            "client_secret": "{{parameters.clientSecret}}",
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.scopes, emptyarray))), ' ')}}"
        },
        "type": "urlencoded",
        "method": "POST",

        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}"
            }
        },

        "log": {
            "sanitize": [
                "response.body.access_token"
            ]
        }
    },
    "refresh": {
        "condition": "{{data.expires < addMinutes(now, 15)}}"

        "url": "https://example.com/token",
        "body": {
            "grant_type": "client_credentials",
            "client_id": "{{connection.clientId}}",
            "client_secret": "{{connection.clientSecret}}",
            "scope": "{{join(distinct(merge(oauth.scope, ifempty(parameters.scopes, emptyarray))), ' ')}}"
        },
        "type": "urlencoded",
        "method": "POST",

        "response": {
            "data": {
                "expires": "{{addSeconds(now, body.expires_in)}}", // access token expiration. This is used in the condition to trigger the "refresh" request.
                "accessToken": "{{body.access_token}}"
            }
        },

        "log": {
            "sanitize": [
                "response.body.access_token"
            ]
        }
    },
    "info": {
        "url": "https://example.com/v1/info",
        "headers": {
            "authorization": "Bearer {{connection.accessToken}}"
        },

        "response": {
            "error": {
                "message": "[{{statusCode}}] {{body.error}}"
            },
            "metadata": { // This is added under the connection name in the UI to make it easier for the user to identify it.
                "type": "text",
                "value": "{{body.user.fullName}} ({{body.user.email}})"
            },
            "uid": "{{body.user.id}}" // This is only needed if your app uses Shared webhooks. The ID allows Make to match the payloads del;ivered to the shared webhook to the correct recipients.
        },
        
        "log": {
            "sanitize": [
                "request.headers.authorization"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}
