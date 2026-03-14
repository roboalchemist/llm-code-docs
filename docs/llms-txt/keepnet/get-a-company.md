# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies/get-a-company.md

# Get a company

As a Reseller you can retrieve a single company you manage by its ID to view full details (license, settings, etc.). Get the company `resourceId` from the companies list, then call **GET /api/companies/{resourceId}**. Use a credential with Client Role = **Reseller**.

***

## POST /api/companies/search

Get the company's `resourceId` by calling this endpoint; use it in the next step as `{resourceId}`.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company (e.g. by `name`) and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use in `GET /api/companies/xC5kfGz7w2Nz`.

***

## GET /api/companies/{resourceId}

Returns full details for that company (license, settings, etc.). Replace `{resourceId}` with the company ID from the search response. No request body.

> Retrieves a single company by ID. **Test it:** Authorize, then set path parameter to a company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/{resourceId}" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or company is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** — Invalid or unknown company ID. Verify from `POST /api/companies/search`.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Update a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/update-a-company).
