# Source: https://docs.pentaho.com/pdc-api-docs/get-started-with-pdc-api-v2/authentication.md

# Source: https://docs.pentaho.com/pdc-api-docs/v1/get-started-with-pdc-api-v1/authentication.md

# Authentication

The Data Catalog API is protected using **JWT bearer tokens**. You must obtain a token from the [Auth](https://docs.pentaho.com/pdc-api-docs/v1/pdc-api-ref-v1/auth#post-api-public-v1-auth) endpoint and include it in the `Authorization` header of your requests to call protected APIs.

### Auth endpoint

**URL**

```
POST /api/public/v1/auth
```

**Description**\
Generates a JWT bearer token when provided with valid credentials.

### Request

**Headers**

| Header         | Value                               |
| -------------- | ----------------------------------- |
| `Content-Type` | `application/x-www-form-urlencoded` |
| `Accept`       | `application/json`                  |

**Body parameters**

<table><thead><tr><th width="130">Field</th><th width="107">Type</th><th width="102">Required</th><th>Example value</th><th>Description</th></tr></thead><tbody><tr><td><code>username</code></td><td>string</td><td>Yes</td><td><code>data_steward@hv.com</code></td><td>PDC login username.</td></tr><tr><td><code>password</code></td><td>string</td><td>Yes</td><td><code>password</code></td><td>PDC login password.</td></tr><tr><td><code>client_id</code></td><td>string</td><td>Yes</td><td><code>pdc-client</code></td><td>Client identifier for API authentication.</td></tr><tr><td><code>grant_type</code></td><td>string</td><td>Yes</td><td><code>password</code></td><td>Grant type used for authentication.</td></tr><tr><td><code>scope</code></td><td>string</td><td>Yes</td><td><code>openid profile email</code></td><td>Scope of the token request.</td></tr></tbody></table>

### Example request

```bash
curl -X POST "https://<your-domain>/api/public/v1/auth" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=data_steward@hv.com&password=Welcome123!&client_id=pdc-client&grant_type=password&scope=openid%20profile%20email"
```

***

### Responses

#### **200 — OK**

Returns a JWT bearer token.

**Example response**

```json
{
  "message": "OK",
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

#### **400 — Bad Request**

Returned when required parameters are missing or invalid.

**Example response**

```json
{
  "status": 400,
  "message": "Invalid Request Parameters"
}
```

#### **401 — Unauthorized**

Returned when credentials are incorrect or a bearer token is missing in a protected call.

**Example response**

```json
{
  "status": 401,
  "message": "Unauthorized"
}
```

#### **500 — Internal Server Error**

Returned when the server fails to process the request.

**Example response**

```json
{
  "status": 500,
  "message": "Internal Server Error"
}
```

#### **503 — Service Unavailable**

Returned when the authentication service is unavailable or the connection is refused.

**Example response**

```json
{
  "status": 503,
  "message": "Service unavailable – connection refused"
}
```

***

### Using the token

Include the token in the `Authorization` header for subsequent requests:

```bash
curl -X GET "https://<your-domain>/api/public/v1/notifications" \
  -H "accept: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR..."
```

***

### Authorize in Swagger UI

Perform the following steps to authorize in Swagger UI:

1. Open Swagger UI:

   ```
   https://<your-domain>/api/public/v1/swagger/
   ```
2. Click the **Authorize** button.
3. Paste your bearer token (without the `Bearer` prefix).
4. Click **Authorize**.

Swagger UI will automatically include the token in all subsequent requests.

***

### Token behavior

When you authenticate through the **Auth** endpoint, PDC issues a **JWT (JSON Web Token)** that grants access to protected API endpoints. Understanding how these tokens behave will help you manage sessions and build reliable integrations.

* **Token type**: The token is a **JWT** (JSON Web Token). It is a signed token that contains encoded claims about the authenticated user, such as identity and assigned roles. You must present this token in the `Authorization` header when calling secured endpoints.
* **Lifetime**: Tokens are **short-lived** to reduce security risks. The exact validity period (for example, 15 minutes, 1 hour, or longer) depends on how your PDC instance is configured by the administrator. After the token expires, all API calls will return `401 Unauthorized` until you obtain a new token.
* **Refresh**: PDC does **not** issue refresh tokens. This means that once your access token expires, you must re-authenticate using your username and password to generate a new token. Automations or scripts should include logic to handle re-authentication.
* **Scopes and roles**: The level of access provided by the token depends on the **role assigned to the user** in PDC. Roles such as *Administrator*, *Data Steward*, or *Analyst* determine what actions you can perform with the API. For example, an Analyst may be able to search and retrieve data assets, while an Administrator can also manage data sources and jobs.
