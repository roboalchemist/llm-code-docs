# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details.md

# List companies with license details

As a Reseller you can retrieve all companies you manage with license information: License Type, Target Users, Monthly Users, License Limit, Renewal Date. Use this list to get Company IDs for scoped API calls and for export to CSV/Excel. Use a credential with Client Role = **Reseller**.

***

## POST /api/companies/search

> Retrieves a paginated, filterable, sortable list of all companies with license details. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled (`pageNumber: 1`, `pageSize: 10`, `orderBy: CreateTime`).

{% hint style="warning" %}
**Automation tools (Zapier, Make, scripts):** This endpoint **requires a non-empty request body**. Do not send an empty body or `{}`. Include at least `pageNumber`, `pageSize`, `orderBy`, `ascending`, and `filter` (use the example in the schema below, or `filter: { "Condition": "AND", "SearchInputTextValue": "" }`). Empty body can cause 500 errors or unreliable results. See [Quickstart → Integration and automation](https://github.com/ucarozan/keepnet-docs/blob/main/api-reference/use-cases/quickstart.md#integration-and-automation) for general rules.
{% endhint %}

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/companies/search/export

> Exports the same list to CSV or Excel for reporting or billing. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled (minimal pagination + `exportType: Csv`).

{% hint style="info" %}
**Request body:** Send a non-empty body (e.g. `pageNumber`, `pageSize`, `orderBy`, `ascending`, `filter`, `exportType`). Empty body can cause errors in automation tools. Use the schema example below.
{% endhint %}

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**.
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body (e.g. missing `orderBy`). Include `pageNumber`, `pageSize`, `orderBy`, `ascending`, `filter`.

{% hint style="info" %}
**Platform UI:** View and manage companies in **Company → Companies**. For billing export, see [Export customer list for billing →](https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing). [Companies →](https://doc.keepnetlabs.com/next-generation-product/platform/company/companies)
{% endhint %}
