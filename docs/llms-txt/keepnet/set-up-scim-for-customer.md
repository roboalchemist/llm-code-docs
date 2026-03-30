# Source: https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/set-up-scim-for-customer.md

# Set up SCIM for a customer

As a Reseller you can create a SCIM integration for a **customer (sub-company)** so that customer can sync target users from their identity provider (Entra ID, Okta, OneLogin, JumpCloud, etc.) into Keepnet. The SCIM integration is created in the **customer’s** context, not your Reseller company. Get the customer’s Company ID, then call the SCIM endpoints with **`X-KEEPNET-Company-Id`**. Use a credential with Client Role = **Reseller**. After creation, share the returned **SCIM token** and endpoint URL with the customer so they can configure their IdP.

***

## POST /api/companies/search

Get the customer’s Company ID. Use the `resourceId` of the desired company in the next steps.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use `xC5kfGz7w2Nz` as Company ID when creating the SCIM integration.

***

## GET /api/scim/fields

Returns available SCIM fields for mapping (e.g. IdP attributes to Keepnet custom fields). Send **`X-KEEPNET-Company-Id`** for the customer.

> Returns all available scim fields. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim/fields" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

**Target group:** To sync users into a specific target group, get the customer's target groups via the target-groups API with the same header. Pass `groupResourceId` in the create-SCIM request; if omitted, synced users appear under **Target Users > People**.

***

## POST /api/scim

Creates a new SCIM integration **for that customer**. Send the Company ID in the **`X-KEEPNET-Company-Id`** header. The request body requires **`name`** (e.g. `"Entra ID Sync"`). Optional: **`groupResourceId`** (target group to sync users into), **`groupBySCIMFieldResourceId`** (e.g. group by department), **`fieldMappings`** (array of SCIM attribute → custom field mapping), **`syncPlatformGroup`** (boolean). The response includes the **SCIM token** and endpoint URL — the customer uses these in their identity provider to complete the SCIM setup.

> Creates a new scim integration. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`** so the integration is created for the chosen customer. **Test it:** Endpoints → **SCIM** → **Creates a new scim integration** — use dummy data (H8d) and set the header to a Company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example request headers:

```http
Authorization: Bearer <your_access_token>
Content-Type: application/json
X-KEEPNET-Company-Id: xC5kfGz7w2Nz
```

Example body (dummy data — minimal; syncs users to no specific group):

```json
{
  "name": "Acme Entra ID Sync"
}
```

With an optional target group (use a valid `groupResourceId` for that customer):

```json
{
  "name": "Acme Entra ID Sync",
  "groupResourceId": "gR4pL2mK9xYz"
}
```

After creation, provide the customer with the **SCIM token** and the Keepnet SCIM base URL from the response so they can configure their IdP (e.g. [SCIM Setup in Entra ID](https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-entra-id), [Okta](https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-okta), etc.).

***

## POST /api/scim/search

List SCIM integrations for that customer. Send **`X-KEEPNET-Company-Id`**.

> Returns a list of the scim integrations. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## GET /api/scim/{resourceId}

Get SCIM integration details. Replace `{resourceId}` with the SCIM integration ID from the search response. Send **`X-KEEPNET-Company-Id`**.

> Retrieves the details of an existing scim setting. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim/{resourceId}" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## PUT /api/scim/{resourceId}

Update the SCIM integration (e.g. name, field mappings). Replace `{resourceId}` with the SCIM integration ID. Send **`X-KEEPNET-Company-Id`**.

> Updates an existing scim integration. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim/{resourceId}" method="put" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/scim/{resourceId}/revoke

Revoke the current token and generate a new one (e.g. if the token was exposed). Replace `{resourceId}` with the SCIM integration ID. Send **`X-KEEPNET-Company-Id`**.

> Revokes the current token of the scim integration and generates a new token. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/scim/{resourceId}/revoke" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID or invalid `groupResourceId` (must be a target group belonging to that customer). Verify Company ID from `POST /api/companies/search` and ensure you send `X-KEEPNET-Company-Id` for the customer.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [List or export target users for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/list-or-export-target-users-for-customer). For SCIM setup in the UI and IdP-specific guides: [Getting Started with SCIM](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/getting-started-with-scim).
