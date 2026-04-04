# Source: https://docs.pentaho.com/pdc-api-docs/get-started-with-pdc-api-v2/troubleshooting-guide.md

# Source: https://docs.pentaho.com/pdc-api-docs/v1/get-started-with-pdc-api-v1/troubleshooting-guide.md

# Troubleshooting guide

This section provides guidance for diagnosing and resolving common issues when working with the Pentaho Data Catalog (PDC) API. Use it as a quick reference when requests fail or when you encounter unexpected responses.

***

### Authentication issues

#### 401 Unauthorized

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: Missing, expired, or invalid bearer token.</summary>

<mark style="color:$success;">**Fix**</mark>:

1. Confirm that the `Authorization` header is included in the request:

   ```
   Authorization: Bearer <accessToken>
   ```
2. Verify that the token has not expired. Tokens are short-lived and must be refreshed by calling `POST /api/public/v1/auth`.
3. If you are using Swagger UI, ensure you pasted only the token value (without the `Bearer` prefix) into the **Authorize** dialog.

</details>

#### 403 Forbidden

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: Your token is valid, but your user role does not have permission for the requested operation.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Contact your PDC administrator to confirm that your account has the correct role (for example, *Administrator*, *Data Steward*, or *Analyst*).
* Review endpoint requirements in the API reference; some operations are restricted to specific roles.

</details>

***

### Endpoint and base URL issues

#### Wrong base URL in "Try it" panel

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: GitBook may display a placeholder server (for example, <code>https://open-2v.gitbook.com</code>) instead of your actual PDC server.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Replace the placeholder with your server:

  ```
  https://<your-domain>/api/public
  ```
* Ensure your OpenAPI spec defines a `servers:` block with your hostname or IP.

</details>

#### 404 Not Found

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: The requested resource does not exist, or the path is incorrect.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Confirm the endpoint path matches the documentation.
* Check whether the resource ID you are querying actually exists in your catalog.
* Remember that Health is unversioned (`/api/public/health`) while other endpoints are versioned (`/api/public/v1/...`).

</details>

***

### Request and payload issues

#### 400 Bad Request

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: Missing or invalid request parameters.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Validate JSON syntax in the request body.
* Check required fields and ensure they use the correct data type.
* For search and filter endpoints, verify the syntax of filter expressions.

</details>

#### 415 Unsupported Media Type

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: Incorrect <code>Content-Type</code> header.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Use `Content-Type: application/json` for JSON requests.
* Use `application/x-www-form-urlencoded` for the Auth endpoint.

</details>

***

### Service availability issues

#### 500 Internal Server Error

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: An unexpected error occurred while processing the request.</summary>

**Fix**:

* Retry the request after a short delay.
* If the error persists, capture the `status`, `message`, and `requestId` from the error response and contact your administrator.

</details>

#### 503 Service Unavailable

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: The API service is temporarily unavailable or refusing connections.</summary>

<mark style="color:$success;">**Fix**</mark>:

* Check the system health with `GET /api/public/health`.
* Verify network connectivity and firewall rules for port 443.
* Try again later if the service is under maintenance.

</details>

***

### CORS and browser issues

#### CORS error in Swagger UI or browser

<details>

<summary><mark style="color:$danger;"><strong>Cause</strong></mark>: Your browser blocks cross-origin requests when trying to call your PDC server from PDC doc site (Gitbook).</summary>

<mark style="color:$success;">**Fix**</mark>:

* Use `curl` or Postman instead of the Swagger “Try it” panel.
* Ask your administrator to configure CORS headers on the API server if browser-based calls are required.

</details>

***

### Best practices for troubleshooting

Follow these best practices to diagnose and resolve issues efficiently when working with the PDC API:

* **Log critical details**\
  Capture the **endpoint path**, **HTTP method**, **status code**, **`requestId`**, and the full **error body** for every failing request. These details are essential for debugging and for escalation to support teams.
* **Use the Errors catalog**\
  Refer to the Errors page to interpret error codes and messages. The catalog explains common causes and provides guidance for corrective action.
* **Validate with `curl` or Postman**\
  Reproduce the request outside of GitBook’s “Try it” panel to rule out browser extensions, CORS restrictions, or GitBook UI quirks. This ensures you are testing against the raw API.
* **Implement retries for transient errors**\
  Add retry logic for temporary failures such as `500 Internal Server Error` and `503 Service Unavailable`. Use **exponential backoff with jitter** to avoid overwhelming the server.
* **Escalate with context**\
  If errors persist after validating your request, contact your PDC administrator or support team. Provide logs with **timestamps, request IDs, and sample payloads** so the issue can be diagnosed quickly.

***
