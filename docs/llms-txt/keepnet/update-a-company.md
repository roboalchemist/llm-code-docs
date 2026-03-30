# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies/update-a-company.md

# Update a company

As a Reseller you can update a customer company's details, license (type, target user limit, expiry), or other settings. Get the company's `resourceId` from the companies list, then call **PUT /api/companies/{resourceId}** with the fields you want to change. Use a credential with Client Role = **Reseller**.

***

## POST /api/companies/search

Get the company's `resourceId` by calling this endpoint; use it in the next step as `{resourceId}`.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use in `PUT /api/companies/xC5kfGz7w2Nz`.

***

## PUT /api/companies/{resourceId}

Updates company details, license (type, target user limit, expiry), or other settings. Replace `{resourceId}` with the company ID. Request body depends on what you change — see Endpoints → **Company** → **Updates a company** for the full schema.

> Updates an existing company. **Test it:** Endpoints → **Company** → **Updates a company** — use dummy/placeholder values (H8d).

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/{resourceId}" method="put" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or company is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid company ID or invalid request body. Verify company ID from `POST /api/companies/search` and check Endpoints → **Company** for the request schema.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [Get a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/get-a-company). To add or update the company in a group: [List and manage company groups →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-and-manage-company-groups) (PUT participants).
