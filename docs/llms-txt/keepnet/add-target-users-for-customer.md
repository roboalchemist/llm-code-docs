# Source: https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/add-target-users-for-customer.md

# Add target users for a customer

As a Reseller you can add target users for a customer by getting their Company ID from the companies list and sending it in the request. The flow: list companies, pick the customer, then call the target-users endpoint with **`X-KEEPNET-Company-Id`**. Use a credential with Client Role = **Reseller**.

***

## POST /api/companies/search

Get the customer’s Company ID by calling this endpoint; use the `resourceId` of the desired company in the next step.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company (e.g. by `name`) and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use `xC5kfGz7w2Nz` as Company ID when calling `POST /api/target-users`.

***

## POST /api/target-users

Add target users for that company by sending the Company ID in the **`X-KEEPNET-Company-Id`** header. Without it, the user may be created in the wrong context or the request may fail.

> Creates a new target user. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`** with the customer’s Company ID from the companies search response. Body: `email`, `firstName`, `lastName`, and optional fields (e.g. `department`). **Test it:** Endpoints → **TargetUser** → **Creates a new target user** — use dummy data (H8d) and set the header to a Company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/target-users" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example request headers:

```http
Authorization: Bearer <your_access_token>
Content-Type: application/json
X-KEEPNET-Company-Id: xC5kfGz7w2Nz
```

Example body (dummy data):

```json
{
  "email": "user@example.com",
  "firstName": "Jane",
  "lastName": "Doe"
}
```

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID or missing required body fields. Verify Company ID from `POST /api/companies/search` and check Endpoints → **TargetUser** for the request body schema.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer) for how Company ID is used across endpoints. [Add system user for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/add-system-user-for-customer) for the same flow with system users.
