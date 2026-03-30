# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies/onboard-new-customer.md

# Create a company

As a Reseller you can create a new company (customer) via the API — this is the programmatic way to onboard a new customer. No Company ID is needed for creation; the new company is created under your Reseller account. Use a credential with Client Role = **Reseller**. After creation, use the returned company `resourceId` for license configuration, company groups, and scoped API calls (e.g. `X-KEEPNET-Company-Id`).

***

## POST /api/companies

Creates a new company. The request uses **multipart/form-data**. Required form fields include: `Name`, `CountryResourceId`, `DateFormat`, `IndustryResourceId`, `LicensePeriodTypeResourceId`, `LicenseTypeResourceId`, `NumberOfUsers`, `TimeFormat`, `TimeZoneId`. Optional: `Description`, `Address`, `WebsiteUrl`, `LicenseModuleResourceIdArray`, `LicenseStartDate`, `LicenseEndDate`, `CompanyGroupResourceIdArray`, and others. Reference IDs (country, industry, license type, etc.) are platform-specific — use valid values from your environment or see Endpoints → **Company** for the full schema.

> **Test it:** Endpoints → **Company** → **Creates a new company**. Use dummy data (H8d): e.g. name `"Acme Corp"`, placeholder resource IDs for country, industry, license type, etc.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example (conceptual — actual request is multipart/form-data): **Name** `Acme Corp`, **NumberOfUsers** `100`, and valid **CountryResourceId**, **IndustryResourceId**, **LicenseTypeResourceId**, **LicensePeriodTypeResourceId**, **DateFormat**, **TimeFormat**, **TimeZoneId** from your platform. Response includes the new company's `resourceId` — use it as Company ID in subsequent API calls and in the optional steps below.

***

## PUT /api/companies/{resourceId}

> Update the new company's details or license (type, user limit, expiry). Replace `{resourceId}` with the company ID from the create response.

[keepnet-api-spec.json](https://github.com/ucarozan/keepnet-docs/blob/main/openapi/keepnet-api-spec.json)

***

## PUT /api/company-groups/{resourceId}/participants

Optional. Add the new company to a group. Replace the first `{resourceId}` with the **group** ID; send in the body the list of company resource IDs (including the new company). See [List and manage company groups →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-and-manage-company-groups).

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/company-groups/{resourceId}/participants" method="put" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller. Set Client Role = **Reseller** in **Company → Company Settings → REST API**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid or missing required form fields. Check Endpoints → **Company** for the full request schema (multipart/form-data).

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details) to see the new company after creation.

{% hint style="info" %}
**Platform UI:** Create companies and manage REST API credentials in **Company → Company Settings → REST API**. [REST API Settings →](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api)
{% endhint %}
