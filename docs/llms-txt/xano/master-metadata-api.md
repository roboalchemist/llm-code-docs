# Source: https://docs.xano.com/xano-features/metadata-api/master-metadata-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Master Metadata API

The master Metadata API allows you to browse and retrieve Instances of an account associated with a Personal Access Token. It is especially useful for displaying an account's different Instances in a UI.

The master Metadata API Swagger documentation can be accessed by the following URL:

<Info>
  **[https://app.xano.com/api:meta](https://app.xano.com/api:meta)**
</Info>

### Instance

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d85ac08b-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=363afd34523486abe39e84b67485bca5" width="1457" height="179" data-path="images/d85ac08b-image.jpeg" />
</Frame>

#### GET /instance/\{name} - Get Single Instance

The GET request will provide details of a specific instance when provided the instance name

### get instance

get

[https://app.xano.com/api:meta/instance/\{name](https://app.xano.com/api:meta/instance/\{name)}

get instance Authentication: required

Authorizations

Path parameters

namestringRequired

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

get

/instance/\{name}

HTTP

```swift  theme={null}
GET /api:meta/instance/{name} HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```json  theme={null}
{
  "name": "x1234-4567-8901",
  "display": "My Instance",
  "xano_domain": "x1234-4567-8901.n7.xano.com",
  "custom_domain": "text",
  "meta_api": "https://x1234-4567-8901.n7.xano.com/api:meta",
  "meta_swagger": "https://x1234-4567-8901.n7.xano.com/apispec:meta?type=json"
}
```

#### GET /instance - Browse Instances

The GET request will provide a list of Instances associated with an account.

### browse instances

get

[https://app.xano.com/api:meta/instance](https://app.xano.com/api:meta/instance)

browse instances Authentication: required

Authorizations

Responses

200

Success!

application/json

Responseobject\[]

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

get

/instance

HTTP

```bash  theme={null}
GET /api:meta/instance HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```json  theme={null}
[
  {
    "name": "x1234-4567-8901",
    "display": "My Instance",
    "xano_domain": "x1234-4567-8901.n7.xano.com",
    "custom_domain": "text",
    "meta_api": "https://x1234-4567-8901.n7.xano.com/api:meta",
    "meta_swagger": "https://x1234-4567-8901.n7.xano.com/apispec:meta?type=json"
  }
]
```

* The response provides both the Xano domain and the custom domain (if applicable).

* The meta\_api value will provide access to the Metadata API for the given Instance.

* The JSON of the Metadata API Swagger for the Instance is also provided.

### Snippet / Token

These endpoints provide functionality for managing private snippet access tokens.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/771a4d76-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=3ee57e6f8a264e3838fcde54a2668516" width="1458" height="288" data-path="images/771a4d76-image.jpeg" />
</Frame>

For reference, the \*\*canonical ID \*\*of your snippet is found at the end of the URL.

```ruby  theme={null}
https://www.xano.com/snippet/abC123Zx/
```

In this example URL, **abC123Zx** is our canonical.

#### POST /snippet/\{canonical}/token/\{token]

Use this endpoint to update a token's allowed number of installations.

### updates a snippet token

post

[https://app.xano.com/api:meta/snippet/\{canonical}/token/\{token](https://app.xano.com/api:meta/snippet/\{canonical}/token/\{token)}

updates a snippet token Authentication: required

Authorizations

Path parameters

canonicalstringRequired

tokenstringRequired

Body

application/json

max\_installsinteger · int64Required

current\_installsinteger · int64Required

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/snippet/\{canonical}/token/\{token}

HTTP

```bash  theme={null}
POST /api:meta/snippet/{canonical}/token/{token} HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 39

{
  "max_installs": 1,
  "current_installs": 1
}
```

application/json

Test it

200

Success!

```json  theme={null}
{
  "created_at": "2023-05-09 21:31:20+0000",
  "updated_at": "2023-05-09 21:31:20+0000",
  "token": "OL3T4JYM",
  "max_installs": 23,
  "current_installs": 1
}
```

#### DELETE /snippet/\{canonical}/token/\{token}

Use this endpoint to delete an access token from a snippet.

### deletes a snippet token

delete

[https://app.xano.com/api:meta/snippet/\{canonical}/token/\{token](https://app.xano.com/api:meta/snippet/\{canonical}/token/\{token)}

deletes a snippet token Authentication: required

Authorizations

Path parameters

canonicalstringRequired

tokenstringRequired

Responses

200

Success!

application/json

Responseobject

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

delete

/snippet/\{canonical}/token/\{token}

HTTP

```swift  theme={null}
DELETE /api:meta/snippet/{canonical}/token/{token} HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```
{}
```

#### GET /snippet/\{canonical}/token

Use this endpoint to get a list of tokens for a snippet.

### returns a list of tokens for a snippet

get

[https://app.xano.com/api:meta/snippet/\{canonical}/token](https://app.xano.com/api:meta/snippet/\{canonical}/token)

returns a list of tokens for a snippet Authentication: required

Authorizations

Path parameters

canonicalstringRequired

Responses

200

Success!

application/json

Responseobject\[]

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

get

/snippet/\{canonical}/token

HTTP

```bash  theme={null}
GET /api:meta/snippet/{canonical}/token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```json  theme={null}
[
  {
    "created_at": "2023-05-09 21:31:20+0000",
    "updated_at": "2023-05-09 21:31:20+0000",
    "token": "OL3T4JYM",
    "max_installs": 23,
    "current_installs": 1
  }
]
```

#### POST /snippet/\{canonical}/token

Use this endpoint to create a new token for a snippet.

### creates a new install token on the snippet

post

[https://app.xano.com/api:meta/snippet/\{canonical}/token](https://app.xano.com/api:meta/snippet/\{canonical}/token)

creates a new install token on the snippet Authentication: required

Authorizations

Path parameters

canonicalstringRequired

Body

application/json

max\_installsinteger · int64Required

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/snippet/\{canonical}/token

HTTP

```bash  theme={null}
POST /api:meta/snippet/{canonical}/token HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 18

{
  "max_installs": 1
}
```

application/json

Test it

200

Success!

```json  theme={null}
{
  "created_at": "2023-05-09 21:31:20+0000",
  "updated_at": "2023-05-09 21:31:20+0000",
  "token": "OL3T4JYM",
  "max_installs": 23,
  "current_installs": 1
}
```

### Snippets

#### GET /snippet/\{canonical}

Retrieve a specific snippet by its canonical ID

### get a specific snippet by ID

get

[https://app.xano.com/api:meta/snippet/\{canonical](https://app.xano.com/api:meta/snippet/\{canonical)}

get a specific snippet by ID Authentication: required

Authorizations

Path parameters

canonicalstringRequired

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

get

/snippet/\{canonical}

HTTP

```swift  theme={null}
GET /api:meta/snippet/{canonical} HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```json  theme={null}
{
  "canonical": "kRG3t_-i",
  "created_at": "2023-03-23 23:32:56+0000",
  "updated_at": "2023-03-27 17:58:48+0000",
  "name": "Token Share Test",
  "review": "pending",
  "review_exception": "text",
  "install_access": "public",
  "install_access_description": "text",
  "featured": true,
  "verified": true
}
```

#### POST /snippet/\{canonical}

Update settings on the snippet, such as the access method and access description.

### update settings on the snippet

post

[https://app.xano.com/api:meta/snippet/\{canonical](https://app.xano.com/api:meta/snippet/\{canonical)}

update settings on the snippet Authentication: required

Authorizations

Path parameters

canonicalstringRequired

Body

application/json

install\_accessstring · enumRequiredPossible values: `public``link``token`

install\_access\_descriptionstringRequired

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/snippet/\{canonical}

HTTP

```bash  theme={null}
POST /api:meta/snippet/{canonical} HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 63

{
  "install_access": "public",
  "install_access_description": "text"
}
```

application/json

Test it

200

Success!

```json  theme={null}
{
  "canonical": "kRG3t_-i",
  "created_at": "2023-03-23 23:32:56+0000",
  "updated_at": "2023-03-27 17:58:48+0000",
  "name": "Token Share Test",
  "review": "pending",
  "review_exception": "text",
  "install_access": "public",
  "install_access_description": "text",
  "featured": true,
  "verified": true
}
```

#### GET /snippet

List all snippets owned by the authenticated user.

### list snippets owned by the authenticated user

get

[https://app.xano.com/api:meta/snippet](https://app.xano.com/api:meta/snippet)

list snippets owned by the authenticated user Authentication: required

Authorizations

Query parameters

pageinteger · int64Optional

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

get

/snippet

HTTP

```bash  theme={null}
GET /api:meta/snippet HTTP/1.1
Host: app.xano.com
Authorization: Bearer JWT
Accept: */*
```

Test it

200

Success!

```json  theme={null}
{
  "curPage": 1,
  "nextPage": 1,
  "prevPage": 1,
  "items": [
    {
      "canonical": "kRG3t_-i",
      "created_at": "2023-03-23 23:32:56+0000",
      "updated_at": "2023-03-27 17:58:48+0000",
      "name": "Token Share Test",
      "review": "pending",
      "review_exception": "text",
      "install_access": "public",
      "install_access_description": "text",
      "featured": true,
      "verified": true
    }
  ]
}
```


Built with [Mintlify](https://mintlify.com).