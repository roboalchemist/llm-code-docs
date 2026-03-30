# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/introduction/authentication.mdx

***

## stoplight-id: z0gjtl5assxz7

# Authentication

The Cash App Afterpay Online API uses two different authentication options, which are discussed below. With the exception of [Ping](/cash-app-afterpay/api-reference/reference/service-status/ping), all Online API endpoints require that one of these forms of authentication are used. Failure to correctly authenticate an API request will result in a `401 Unauthorized` response.

## Basic auth

The first authentication method is [Basic HTTP Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), a simple authentication scheme built into the HTTP protocol, as specified by [RFC 7617](https://tools.ietf.org/html/rfc7617).

### Example request

<Tabs>
  <Tab title="HTTP" language="http">
    ```http
    GET /v2/configuration HTTP/1.1
    Host: global-api-sandbox.afterpay.com
    Authorization: Basic MzI6YWJjZGVmZ2g=
    ```
  </Tab>

  <Tab title="cURL" language="curl">
    ```bash
    curl "https://global-api-sandbox.afterpay.com/v2/configuration" \
      -H 'Authorization: Basic MzI6YWJjZGVmZ2g='
    ```
  </Tab>

  <Tab title="Node.js" language="javascript">
    ```javascript
    var request = require("request");

    var options = {
      url: 'https://global-api-sandbox.afterpay.com/v2/configuration',
      headers: {
        Authorization: 'Basic MzI6YWJjZGVmZ2g='
      }
    };

    request(options, function (error, response, body) {
      if (error) throw new Error(error);

      console.log(body);
    });
    ```
  </Tab>

  <Tab title="Ruby" language="ruby">
    ```ruby
    require 'uri'
    require 'net/http'

    url = URI("https://global-api-sandbox.afterpay.com/v2/configuration")

    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Basic MzI6YWJjZGVmZ2g='

    response = http.request(request)
    puts response.read_body
    ```
  </Tab>

  <Tab title="Python" language="python">
    ```python
    import requests

    url = "https://global-api-sandbox.afterpay.com/v2/configuration"

    headers = {
        'Authorization': "Basic MzI6YWJjZGVmZ2g="
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    ```
  </Tab>
</Tabs>

Consider the following example:

| Merchant ID | Secret Key |
| ----------- | ---------- |
| 32          | abcdefgh   |

<Info>
  In conventional HTTP terms, "Merchant ID" is the **username** and "Secret Key" is the **password**.
  Afterpay provides merchant accounts per region, and each merchant account has unique API credentials.
</Info>

The credentials are joined by a colon character (without any spaces), then base64-encoded.

| Plain Text  | Base64 Encoded   |
| ----------- | ---------------- |
| 32:abcdefgh | MzI6YWJjZGVmZ2g= |

The `Authorization` header can then be formed by including the word `Basic`, followed by a single space character, followed by the base64-encoded credential pair.

|              |                                         |   |
| ------------ | --------------------------------------- | - |
| Final Header | `Authorization: Basic MzI6YWJjZGVmZ2g=` |   |

<Info title="Security Notice">
  The base64-encoding of the Authorization header is unrelated to security. All HTTP headers and bodies (for both requests and responses) between the Merchant and Afterpay are encrypted with TLS. The reason for base64-encoding is solely to comply with the [RFC 7617](https://www.rfc-editor.org/rfc/rfc7617.txt) standard, which allows non-HTTP characters and multibyte strings to be used for [Basic HTTP Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication).
</Info>

## Bearer tokens

The Client Credentials Authentication method is another authentication method available to merchants. It is a secure mechanism used to obtain access tokens which is defined in [RFC 6749](https://datatracker.ietf.org/doc/rfc6749/).

When using this method, a client application uses its unique credentials to fetch an access token, which enables it to access Cash App Afterpay's online APIs.

### Token URLs

Tokens are generated using separate URLs from those described in the [API environments](/cash-app-afterpay/api-reference/reference/introduction)

<Tabs>
  <Tab title="OAuth Endpoint Production">
    |             |                                                      |
    | ----------- | ---------------------------------------------------- |
    | Locations   | AU, NZ, US, CA, and UK                               |
    | Environment | `https://merchant-auth.afterpay.com/v2/oauth2/token` |
  </Tab>

  <Tab title="OAuth Endpoint Sandbox">
    |             |                                                              |
    | ----------- | ------------------------------------------------------------ |
    | Locations   | AU, NZ, US, CA, and UK                                       |
    | Environment | `https://merchant-auth-sandbox.afterpay.com/v2/oauth2/token` |
  </Tab>
</Tabs>

### Example request

The following examples use the same credentials as the [Basic Auth](#basic-auth) section.

<Note>
  The `scopes` field mentioned below is `merchant_api_v2`, but `merchant_api_v1` may be used to access the first version of the merchant APIs.
</Note>

#### Access token request

```http
POST /v2/oauth2/token HTTP/1.1
Host: https://merchant-auth-sandbox.afterpay.com
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=32
&client_secret=abcdefgh
&scope=merchant_api_v2
```

```cURL
curl -X POST "https://merchant-auth-sandbox.afterpay.com/v2/oauth2/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "grant_type=client_credentials&client_id=32&client_secret=abcdefgh&scope=merchant_api_v2"
```

```javascript
const request = require('request');

const options = {
  url: 'https://merchant-auth-sandbox.afterpay.com/v2/oauth2/token',
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  form: {
    grant_type: 'client_credentials',
    client_id: '32',
    client_secret: 'abcdefgh',
    scope: 'merchant_api_v2'
  }
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

```ruby
require 'uri'
require 'net/http'

uri = URI.parse('https://merchant-auth-sandbox.afterpay.com/v2/oauth2/token')

http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

request = Net::HTTP::Post.new(uri.path, { 'Content-Type' => 'application/x-www-form-urlencoded' })

request.set_form_data({
  'grant_type' => 'client_credentials',
  'client_id' => '32',
  'client_secret' => 'abcdefgh',
  'scope' => 'merchant_api_v2'
})

response = http.request(request)

puts response.body
```

```python
import requests

data = {
    'grant_type': 'client_credentials',
    'client_id': '32',
    'client_secret': 'abcdefgh',
    'scope': 'merchant_api_v2'
}

response = requests.post('https://merchant-auth-sandbox.afterpay.com/v2/oauth2/token', data=data)
print(response.json())
```

### Access token response

The response to a successful authentication request includes the full JWT `access_token`. In the example below, the token is shortened for brevity.

```json
{
  "access_token": "eyJraWQiOiIwMzllNDBlMy0wYjM5LTQ3MTktOGFjNS05ZmE0OWRiMjQ3MWMiLCJhbGciOiJSUzI1NiJ9.eyJzd…",
  "scope": "merchant_api_v2/read merchant_api_v2/reverse merchant_api_v2/void merchant_api_v2/deferred_capture merchant_api_v2/capture merchant_api_v2/manage merchant_api_v2/initiate merchant_api_v2/cancel_subscription merchant_api_v2/direct_capture merchant_api_v2/refund merchant_api_v2/auth",
  "token_type": "Bearer",
  "expires_in": 86399
} 
```

<Note>
  The field `expires_in` is the time (in seconds) that the token is valid from when its generated. The token is not usable after this time elapses.
</Note>

### API requests with token

See the following example where the `access_token` field is provided in the `Authorization` header of the request to access a secure API:

```http request
GET /v2/configuration HTTP/1.1
Host: global-api-sandbox.afterpay.com
Authorization: Bearer eyJraWQiOiIwMzllNDBlMy0wYjM5LTQ3MTktOGFjNS05ZmE0OWRiMjQ3MWMiLCJhbGciOiJSUzI1NiJ9.eyJzd…
```

<Info>
  Instead of the Authorization header using a prefix of 

  `Basic`

  , the token authentication method uses 

  `Bearer`

  . Omitting this value or setting it to something else will return an HTTP status code of 

  `401 Unauthorized`
</Info>

<Info>
  Other Cash App Afterpay APIs are accessible by using the same authentication scheme as the previous example.
</Info>
