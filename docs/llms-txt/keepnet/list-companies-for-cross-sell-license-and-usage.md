# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/list-companies-for-cross-sell-license-and-usage.md

# List companies for cross-sell by license and usage

As a Reseller you list or export companies with license details (license type, license limit, user count, renewal date, tags) to identify cross-sell or upsell opportunities. Use a credential with Client Role = **Reseller**. Use the same company search endpoint; filter or sort by license type, usage, or renewal date to find candidates. Request body: see Endpoints → **Company** for filter and sort options.

***

## POST /api/companies/search

Returns a paginated list of companies with license details. Use **`filter`** to narrow by license type, renewal date, or other fields if the API supports them. Use **`orderBy`** (e.g. `RenewalDate`, `CreateTime`, or license-related fields) and **`ascending`** to sort. Each item includes license limit, user count, renewal date, and related fields for cross-sell analysis.

> Retrieves a list of all companies with license details. Use filter and orderBy to identify cross-sell candidates by license type, usage, or renewal date.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

Exports the same list to CSV or Excel for analysis in a spreadsheet or BI tool. Use the same filter and sort as in search so the export matches your cross-sell criteria.

> Exports the list of companies to CSV or Excel. Apply the same filter and sort as in search for cross-sell reporting.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body or filter. Include `pageNumber`, `pageSize`, `orderBy`, `ascending`; check Endpoints → **Company** for supported filter fields and orderBy values.

**Related:** [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
