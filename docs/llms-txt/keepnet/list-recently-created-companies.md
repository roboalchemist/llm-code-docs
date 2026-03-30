# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/list-recently-created-companies.md

# List recently created companies

As a Reseller you list or count companies created in a recent period for billing, onboarding reports, or growth metrics. Use a credential with Client Role = **Reseller**. Call company search with **`orderBy: "CreateTime"`** and **`ascending: false`** to get newest first; use **`filter`** with a date range on creation date if the API supports it. Total count is in the response or sum across pages.

***

## POST /api/companies/search

Returns a paginated list of companies. Set **`orderBy: "CreateTime"`** and **`ascending: false`** to list newest companies first. Optionally use **`filter`** to restrict by creation date range (see Endpoints → **Company** for supported filter fields). The response total count gives the number of companies matching the criteria; paginate through all pages if you need a full list or count for a period.

> Retrieves a list of all companies. Use orderBy CreateTime and ascending false to list recently created companies first; use filter for a date range if supported.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

Exports the company list to CSV or Excel with the same order and filter. Use this to get all recently created companies in one file and compute counts or dates client-side.

> Exports the list of companies to CSV or Excel. Use the same orderBy and filter as in search to export recently created companies.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body. Include `pageNumber`, `pageSize`, `orderBy: "CreateTime"`, `ascending: false`; use `filter: null` or a valid filter structure.

**Related:** [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
