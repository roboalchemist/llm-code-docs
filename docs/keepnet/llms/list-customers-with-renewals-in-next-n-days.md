# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/list-customers-with-renewals-in-next-n-days.md

# List customers with renewals in the next N days

As a Reseller you list or export companies whose license renewal date falls within the next N days (e.g. 90 days) for renewal forecasting and sales follow-up. Use a credential with Client Role = **Reseller**. Call company search with a **`filter`** on renewal date (e.g. renewal date between today and today + N days) if the API supports it; otherwise export the full list and filter by the renewal date column client-side. Request body: see Endpoints → **Company** for filter structure and supported fields.

***

## POST /api/companies/search

Returns a paginated list of companies. Use **`filter`** to restrict results to companies whose **renewal date** is within the next N days (e.g. next 90 days). If the API supports a renewal-date filter, set the filter accordingly; otherwise use **`orderBy: "RenewalDate"`** and **`ascending: true`** and paginate to get upcoming renewals first, then filter client-side by date range.

> Retrieves a list of all companies. Use filter on renewal date (or orderBy RenewalDate) to list customers with renewals in the next N days.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

Exports the company list to CSV or Excel. Apply the same filter (or orderBy) as in search so the file contains only companies with renewals in the target window, or export all and filter by the renewal date column in your spreadsheet.

> Exports the list of companies to CSV or Excel. Use the same filter or orderBy as in search to export only customers with upcoming renewals.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body or filter. Include `pageNumber`, `pageSize`, `orderBy`, `ascending`; check Endpoints → **Company** for renewal-date filter syntax.

**Related:** [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [List customers with expired licenses →](https://doc.keepnetlabs.com/api-reference/reseller/billing/list-customers-with-expired-licenses). [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
