# Source: https://docs.pentaho.com/pdc-api-docs/get-started-with-pdc-api-v2/errors.md

# Source: https://docs.pentaho.com/pdc-api-docs/v1/get-started-with-pdc-api-v1/errors.md

# Errors

The PDC API uses standard HTTP status codes to indicate success or failure. This page catalogs the common error responses that appear across endpoints and explains how to diagnose and fix them.

* **Format:** JSON
* **Typical shape:** an object with `status` (number) and `message` (string/array/object).
* **Where returned:** Most endpoints define `400`, `401`, `500`, and `503` responses.

{% hint style="warning" %}
Always capture the **HTTP status**, **request path**, and the full **error body** when troubleshooting. If the error occurs in automation, log the last request payload and headers (excluding secrets).
{% endhint %}

### Standard error object

Most error responses follow this structure:

```json
{
  "status": 400,
  "message": "Invalid Request Parameters"
}
```

* `status` (number): HTTP status code.
* `message` (string | array | object): Human-readable message or structured details.
  * In many endpoints, `message` may be a string (e.g., `"Unauthorized"`), an array of issues, or an object (e.g., `{ "error": "Invalid data format" }`).

***

### Error catalog

| Status                          | When it happens                                                                     | What to check                                                                                                      | Example response                                                                |
| ------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **400 – Bad Request**           | The request is malformed or missing required parameters/fields.                     | Validate payload types, required fields, query params, and JSON format.                                            | `json { "status": 400, "message": "Invalid Request Parameters" }`               |
| **401 – Unauthorized**          | Missing/invalid/expired bearer token or wrong credentials when authenticating.      | For protected endpoints, include `Authorization: Bearer <token>`. If calling `/v1/auth`, verify username/password. | `json { "status": 401, "message": "Unauthorized" }`                             |
| **500 – Internal Server Error** | An unexpected error occurred while processing the request.                          | Retry if transient; if persistent, collect the request + response and contact an admin.                            | `json { "status": 500, "message": "Internal Server Error" }`                    |
| **503 – Service Unavailable**   | The service is unavailable or refusing connections (maintenance, startup, network). | Check service health (`/api/public/health`), base URL, network/firewall, and try again later.                      | `json { "status": 503, "message": "Service unavailable — connection refused" }` |

{% hint style="info" %}
In PDC API, these errors are defined consistently across operations with the same descriptions and example payloads. Some endpoints may also include structured `message` bodies (array/object) when returning validation details.
{% endhint %}
