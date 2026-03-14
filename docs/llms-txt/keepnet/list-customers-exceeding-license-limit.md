# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/list-customers-exceeding-license-limit.md

# List customers exceeding license limit

As a Reseller you list or export companies that currently exceed their license limit (more users than the licensed maximum) for billing review, true-up, or compliance. Use a credential with Client Role = **Reseller**. Send **`isTargetUserCountExceededLimit: true`** in the request body so only overage customers are returned.

***

## POST /api/companies/search

Returns a paginated list of companies that exceed their license limit. Include **`isTargetUserCountExceededLimit: true`** in the request body. Use `pageNumber`, `pageSize`, `orderBy` (e.g. `CreateTime`), and `ascending` as needed. Request body: see Endpoints → **Company** → Company search; add `isTargetUserCountExceededLimit: true`.

> Retrieves a list of companies. For billing overage, set **`isTargetUserCountExceededLimit: true`** so only companies over their license limit are returned.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

Exports the same overage list to CSV or Excel. Include **`isTargetUserCountExceededLimit: true`** in the request body. Use `exportType: "Csv"` or `"Excel"`. Request body: see Endpoints → **Company** → Company search export.

> Exports the list of companies to CSV or Excel. Set **`isTargetUserCountExceededLimit: true`** to export only customers exceeding their license limit.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body. Include `pageNumber`, `pageSize`, `orderBy`, `ascending`, and `isTargetUserCountExceededLimit: true`; use `filter: null` if you do not need date or other filters.

{% hint style="info" %}
**Platform UI:** In **Company → Companies**, use the **FILTER EXCEEDING LIMIT** toggle to see the same overage list. [Companies →](https://doc.keepnetlabs.com/next-generation-product/platform/company/companies)
{% endhint %}

**Related:** [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
