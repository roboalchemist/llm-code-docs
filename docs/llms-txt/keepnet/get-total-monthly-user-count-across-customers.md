# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/get-total-monthly-user-count-across-customers.md

# Get total monthly user count across customers

As a Reseller you get the total monthly user count across all companies you manage for billing or capacity reporting. Use a credential with Client Role = **Reseller**. Call company search (with a month parameter if the API supports it for Monthly Users), then sum the **monthly user** value from each company in the response. Paginate through all pages to include every company, or export to CSV/Excel and sum the monthly user column client-side.

***

## POST /api/companies/search

Returns a paginated list of companies; each item includes a **monthly user** count for the selected period. Request body: see Endpoints → **Company** (e.g. month selector or date range if available for Monthly Users). To get the total monthly user count: call search with a large `pageSize` or loop through all pages and sum the monthly user field from each company. The response total count and items give you the full set to aggregate.

> Retrieves a list of all companies with license details, including monthly user count per company. Sum the monthly user values across all pages to get the total for billing.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

Exports the company list to CSV or Excel including the monthly user column. Sum that column in your spreadsheet or script to get the total monthly user count for billing. Use the same request parameters as in the UI month selector if the API supports a month or date range for Monthly Users.

> Exports the list of companies to CSV or Excel. Use the monthly user column to compute the total monthly user count for billing.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body. Include `pageNumber`, `pageSize`, `orderBy`, `ascending`; add any month or date parameter required for Monthly Users per Endpoints → **Company**.

**Related:** [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
