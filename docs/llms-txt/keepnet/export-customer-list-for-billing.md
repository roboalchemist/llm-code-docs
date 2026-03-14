# Source: https://doc.keepnetlabs.com/api-reference/reseller/billing/export-customer-list-for-billing.md

# Export customer list for billing

As a Reseller you can export the list of companies you manage to CSV or Excel for billing, MSSP reporting, license reconciliation, or partner dashboards. Use a credential with Client Role = **Reseller**. Same endpoint as the export in [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details); this page focuses on billing and export use cases.

***

## POST /api/companies/search/export

> Exports the list of companies (with license details) to CSV or Excel. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled (minimal pagination + `exportType: Csv`). Use `exportType: "Excel"` for Excel output.

{% hint style="info" %}
**Automation tools:** Send a non-empty request body (`pageNumber`, `pageSize`, `orderBy`, `ascending`, `filter`, `exportType`). Empty body can cause errors. See [Quickstart → Integration and automation](https://github.com/ucarozan/keepnet-docs/blob/main/api-reference/use-cases/quickstart.md#integration-and-automation) and [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details).
{% endhint %}

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search/export" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body. Use minimal body: `pageNumber`, `pageSize`, `orderBy`, `ascending`, `exportType` (e.g. `Csv`).

**Related:** Paginated list without file download: [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
