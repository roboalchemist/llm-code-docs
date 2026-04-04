# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/collecting-cookies.md

# Collecting Cookies

## get\_cookies Functions

Websites may set cookies for a variety of purposes, from identifying returning users to storing user preference information.

Capturing and saving the cookies a website sends is easily done with Page Interactions using the `get_cookies` function. `get_cookies` accepts a timeout parameter to set how long to listen for new cookies, as demonstrated below:&#x20;

<table><thead><tr><th width="156">Parameter</th><th width="162">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>timeout</code></td><td>Optional<br>Default = <code>1000</code></td><td>Integer | Controls how long to wait for new cookies before storing all collected cookie data in ms.</td></tr></tbody></table>

### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "render_flow": [{
        "get_cookies": {
                "timeout": 1000
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}

### Example Response

`get_cookies` returns an array of cookies with a variety of relevant metadata, as shown in the example below:

<pre class="language-json"><code class="lang-json">...
<strong>"render_flow": {
</strong>        "success": true,
        "results": [
            {
                "name": "get_cookies",
                "status": "done",
                "duration": 2,
                "result": [
                    {
                        "name": "AEC",
                        "value": "AQTF6HyAslt2IuPBg9jwM2zCXxNUpsNKGgNwuplQWREeFgCJ5xXjYer98As",
                        "domain": ".google.com",
                        "path": "/",
                        "expires": 1733227086.667467,
                        "size": 62,
                        "httpOnly": true,
                        "secure": true,
                        "session": false,
                        "sameSite": "Lax",
                        "priority": "Medium",
                        "sameParty": false,
                        "sourceScheme": "Secure",
                        "sourcePort": 443
                    },
                    {
                        "name": "receive-cookie-deprecation",
                        "value": "1",
                        "domain": "www.google.com",
                        "path": "/",
                        "expires": 1733227086.667547,
                        "size": 27,
                        "httpOnly": true,
                        "secure": true,
                        "session": false,
                        "sameSite": "None",
                        "priority": "Medium",
                        "sameParty": false,
                        "sourceScheme": "Secure",
                        "sourcePort": 443,
                        "partitionKey": "https://google.com"
                    },
                    {
                        "name": "NID",
                        "value": "514=lxnGqrzAmosD7_7PmQUW-pU4qmlkut0tglTMPm3_T98VEVTulM6PgQWJW8RA4ayo0GKh3pIEP4cOET0JOn56PR2-rPD9nSrNzD_uKid8WQ3s_-WNjXpGs68BFpqHCRRnwG9OZBMi3NeGUYe2gE7pmIL1mkV_ryQDDcgcicdlthU",
                        "domain": ".google.com",
                        "path": "/",
                        "expires": 1733486286.667576,
                        "size": 178,
                        "httpOnly": true,
                        "secure": true,
                        "session": false,
                        "sameSite": "None",
                        "priority": "Medium",
                        "sameParty": false,
                        "sourceScheme": "Secure",
                        "sourcePort": 443
                    }
                ]
            }
        ]
    }
</code></pre>
