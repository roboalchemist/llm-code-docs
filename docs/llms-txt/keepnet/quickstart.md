# Source: https://doc.keepnetlabs.com/api-reference/quickstart.md

# Quickstart

The Keepnet API lets you automate platform operations: pull reports, manage users, onboard customers, and integrate with SIEM, SOAR, or identity systems.

You can use the Keepnet API to:

* Pull campaign reports (phishing, smishing, quishing, vishing, callback)
* Export training reports, gamification data, and executive summaries
* Add target users and enroll them in training
* List and manage companies (Reseller)
* Export audit logs to SIEM

…and more, all via REST calls with OAuth 2.0 Client Credentials.

Use the API from AI assistants (Cursor, Claude, ChatGPT, etc.) via MCP: [Use the API with AI assistants (MCP) →](https://doc.keepnetlabs.com/api-reference/use-the-api-with-ai-assistants-mcp)

***

{% stepper %}
{% step %}
**Getting started**

You need a Keepnet platform account with API access. Generate **Client ID** and **Client Secret** from **Company → Company Settings → REST API** before making any API calls.

{% hint style="info" %}
**Platform UI:** Go to **Company → Company Settings → REST API** and click **+ NEW**. [REST API Settings →](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api)
{% endhint %}

| Field              | Description                                                                 |
| ------------------ | --------------------------------------------------------------------------- |
| **Name**           | A label for this credential set (e.g. `prod-integration`, `siem-connector`) |
| **Client Role**    | `Company Admin` for full access, or a custom role with limited privileges   |
| **IP Restriction** | Optionally restrict access to specific IP addresses                         |
| **Status**         | Set to `Active`                                                             |

{% hint style="warning" %}
**The Client Secret is shown only once.** Copy and store it securely immediately after you generate it — it cannot be retrieved later.
{% endhint %}
{% endstep %}

{% step %}
**Request an access token**

Keepnet API uses **OAuth 2.0 Client Credentials**. Every request requires a Bearer token in the `Authorization` header.

**Endpoint:** `POST /connect/token`

{% tabs %}
{% tab title="HTTP" %}
Send a POST request with form-encoded body:

```bash
curl -X POST https://api.keepnetlabs.com/connect/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "scope=api1"
```

Response:

```json
{
  "access_token": "eyJ...",
  "expires_in": 3600,
  "token_type": "Bearer",
  "scope": "api1",
  "permissions": ["tags/search|POST", "companies/search|POST", "..."]
}
```

Include `access_token` in every API request as `Authorization: Bearer <token>`. The optional `permissions` array lists endpoints your credential can call (e.g. `companies/search|POST`).
{% endtab %}

{% tab title="JavaScript" %}

```javascript
const response = await fetch('https://api.keepnetlabs.com/connect/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'client_credentials',
    client_id: process.env.CLIENT_ID,
    client_secret: process.env.CLIENT_SECRET,
    scope: 'api1',
  }),
});

const { access_token } = await response.json();
// Use: Authorization: Bearer ${access_token}
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Integration tools (Zapier, Make, n8n, Postman, etc.)**\
The token endpoint accepts **only** `application/x-www-form-urlencoded`. Do **not** send a JSON body or use "Raw" with `Content-Type: application/json` — that returns a **500 Internal Server Error**. In your tool, choose **Form** (or form-urlencoded) as the body type and send the fields: `grant_type`, `client_id`, `client_secret`, `scope`.
{% endhint %}

{% hint style="success" %}
**Test it — step by step**

**Authorize** is not on this page; it is in the **Endpoints** section. Open **Endpoints** in the left sidebar → pick an endpoint (e.g. **Company** → **Retrieves a list of all companies**) → in the right panel click the lock icon **Authorize** → enter **Client ID** and **Client Secret** → click **Authorize**. The token is fetched and applied to all requests. Then click **Send** in the same panel to send the request.

* **GET /api/companies/my:** Endpoints → **Company** → **Retrieves the companies which can be simulated by user** → **Send**. No body.
* **POST /api/companies/search:** Endpoints → **Company** → **Retrieves a list of all companies** → Body is pre-filled → **Send**. Reseller credential required.

Alternatively, get a token from the **POST /connect/token** block on this page, copy `access_token` from the response, and paste it into the Bearer field in Endpoints instead of using Authorize.
{% endhint %}
{% endstep %}

{% step %}
**Make your first API call**

Verify your token and company access with `GET /api/companies/my` — returns your company (Company Admin) or companies you manage (Reseller). No request body, no extra parameters.

```bash
curl -X GET "https://api.keepnetlabs.com/api/companies/my" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

If successful, you'll get a `data` array with your company details (id, name, etc.). This confirms:

* Token is valid
* Credentials have API access
* You can fetch your own company data
  {% endstep %}
  {% endstepper %}

***

## Test it — quick checklist

The **Authorize** button is not on the Quickstart page; it appears in the right panel when you open an endpoint under **Endpoints** (left sidebar). Order:

| Step | Action                                                                                                                                                   | Result                                                                  |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1    | **Endpoints** → open any endpoint (e.g. Company → Retrieves a list…) → **Authorize** (lock icon) → enter Client ID + Client Secret → click **Authorize** | Token is fetched and applied to all requests                            |
| 2    | **GET /api/companies/my** (Company) → Send                                                                                                               | Returns your company (Company Admin) or companies you manage (Reseller) |
| 3    | **POST /api/companies/search** (Company) → Body pre-filled → Send                                                                                        | Company list with license details (Reseller credential required)        |

{% hint style="info" %}
With a **Company Admin** credential, step 3 returns `403 Forbidden`. This is expected — `companies/search` is for Reseller only.
{% endhint %}

***

## Base URL and response format

**Base URL:** `https://api.keepnetlabs.com`

All API responses include an `isSuccess` field. When `isSuccess` is `false`, check the `messages` array for error details.

| Field       | Type    | Description                              |
| ----------- | ------- | ---------------------------------------- |
| `isSuccess` | boolean | Indicates whether the request succeeded  |
| `data`      | object  | Response payload when successful         |
| `messages`  | array   | Error or validation messages when failed |

***

## Common conventions

| Convention              | Description                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pagination**          | Search endpoints use `pageNumber`, `pageSize`, `orderBy`, `ascending`, `filter` in the request body                                                                                                                                                                    |
| **Search request body** | **Do not send an empty body** for search endpoints. Always include at least `pageNumber`, `pageSize`, `orderBy`, `ascending`, and `filter` (or the structure shown in the endpoint). Empty or missing body can cause errors or unreliable results in automation tools. |
| **Filter**              | Use `filter: null` for no filtering, or a filter object with operators (`eq`, `neq`, `contains`, `gt`, `lt`, etc.)                                                                                                                                                     |
| **Sorting**             | `orderBy` is often required — use `CreateTime` for chronological ordering                                                                                                                                                                                              |
| **Company scope**       | Most endpoints require a company context. Company Admin: automatic. Reseller: include Company ID (header/path/query)                                                                                                                                                   |

***

## Integration and automation

When calling the API from automation platforms (Zapier, Make, n8n, custom scripts, etc.), follow these rules to avoid common errors:

| Topic                                                    | Requirement                                                                                                                                                             | If you don't                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Token (`POST /connect/token`)**                        | Body must be **form-encoded** (`application/x-www-form-urlencoded`). Use the **Form** body type in your tool; send `grant_type`, `client_id`, `client_secret`, `scope`. | Sending JSON or Raw with `Content-Type: application/json` returns **500 Internal Server Error**. |
| **Search endpoints** (e.g. `POST /api/companies/search`) | Send a **non-empty request body** with at least `pageNumber`, `pageSize`, `orderBy`, `ascending`, `filter`. Use the example in each endpoint's docs.                    | Empty body can cause **500** or unreliable/empty results.                                        |

***

## What the token contains

The access token is a **JWT**. Decode it to read company context, role, and other values — useful when endpoints require Company ID in the path, header, or query.

**To decode:** Paste the token at [jwt.io](https://jwt.io) (signature verification optional) or Base64URL-decode the middle part (between the two dots).

### Company context

| Claim                                   | Description                                                                                          | Example                                       |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `user_company_resourceid`               | **Company ID** — use in `X-KEEPNET-Company-Id`, path `/api/.../companies/{id}/...`, or `?companyId=` | `xC5kfGz7w2Nz`                                |
| `user_company_name`                     | Company name                                                                                         | `ACME LLC`                                    |
| `user_company_id`                       | Numeric company ID                                                                                   | `1`                                           |
| `user_company_logopath`                 | Company logo URL                                                                                     | `https://api.keepnetlabs.com/companylogo/...` |
| `user_company_industry_name`            | Industry (e.g. Technology)                                                                           | `Technology`                                  |
| `user_company_parentcompany_resourceid` | Parent/MSSP company ID — **Reseller only**, empty for Company Admin                                  | `xC5kfGz7w2Nz` (Reseller) or empty            |
| `user_company_parentcompany_name`       | Parent company name — **Reseller only**                                                              | `ACME Corp`                                   |

### Role and access

| Claim                  | Description                   | Company Admin   | Reseller   |
| ---------------------- | ----------------------------- | --------------- | ---------- |
| `role`                 | User role                     | `Company Admin` | `Reseller` |
| `company_admin_access` | Can manage own company        | `true`          | `true`     |
| `reseller_access`      | Can manage multiple companies | `false`         | `true`     |
| `root_access`          | Platform root/admin           | `false`         | `false`    |
| `scope`                | API scope                     | `["api1"]`      | `["api1"]` |

### Token metadata

| Claim       | Description                        | Example            |
| ----------- | ---------------------------------- | ------------------ |
| `exp`       | Expiry (Unix timestamp)            | `1772935488`       |
| `iat`       | Issued at (Unix timestamp)         | `1772931888`       |
| `client_id` | Client ID used to obtain the token | `xxxxxxxxxxxxxxxx` |

{% hint style="info" %}
**Company Admin**

* `user_company_resourceid` = your Company ID — use when an endpoint requires a company context (e.g. `GET /api/companies/{resourceId}`)
* `user_company_parentcompany_*` = empty
  {% endhint %}

{% hint style="info" %}
**Reseller**

* `user_company_resourceid` = your Reseller company
* `user_company_parentcompany_resourceid` = parent/MSSP company
* Managed company IDs → `POST /api/companies/search` — use those IDs in `X-KEEPNET-Company-Id` for company-scoped requests
  {% endhint %}

***

## Who can use the API

| Role              | Access                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| **Company Admin** | Full access to your company's data — no Company ID needed                                               |
| **Reseller**      | Cross-company management — list companies, onboard customers, pull reports per company using Company ID |
| **Custom role**   | Scoped to specific products or actions based on role definition                                         |

***

## Token expiry and errors

Tokens expire after **1 hour**. No refresh token — request a new one when the current token expires.

| HTTP status                            | Cause                                              | Action                                                                                                             |
| -------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `400 Bad Request` — `invalid_client`   | Wrong or placeholder credentials                   | Use real credentials from **Company → Company Settings → REST API**                                                |
| `401 Unauthorized`                     | Missing or invalid token                           | Re-authenticate and retry                                                                                          |
| `403 Forbidden`                        | Insufficient role permissions                      | Check the Client Role in platform settings                                                                         |
| `500 Internal Server Error` (on token) | Token request sent with JSON or wrong Content-Type | Use **form-encoded** body only: `Content-Type: application/x-www-form-urlencoded` and Form body type in your tool. |
| `429 Too Many Requests`                | Rate limit exceeded                                | Back off and retry after a delay                                                                                   |

***

## Reseller: scope by Company ID

If your credential has the **Reseller** role, include Company ID when calling company-scoped endpoints:

* **Header:** `X-KEEPNET-Company-Id: {companyId}` (when supported)
* **Path:** `/api/.../companies/{companyId}/...`
* **Query:** `?companyId={companyId}`

Company IDs are returned by `POST /api/companies/search`. For a full explanation and usage in report and user endpoints, see [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). For the list: [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details).

***

## Keep credentials secure

{% hint style="success" %}
**Do:** Store credentials in environment variables or a secrets manager. Enable IP Restriction if your integration runs from a fixed IP. Use a custom role scoped to only the endpoints you need.
{% endhint %}

{% hint style="danger" %}
**Don't:** Hard-code `client_id` or `client_secret` in source code. Don't commit credentials to version control.
{% endhint %}

***

## Explore the API

| What you want to do                  | Use case                                                                                                                                                               |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List companies (Reseller)            | [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details)                              |
| Scope requests to a customer         | [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer)                                      |
| Export customer list for billing     | [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing)                                      |
| View customer's training enrollments | [View customer's enrollment list and report →](https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-list-and-report)                   |
| View customer's simulation campaigns | [View customer's campaign list and report →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report) |
