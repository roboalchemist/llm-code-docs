# Source: https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report.md

# View customer's campaign list and report

As a Reseller you can list a customer’s phishing, smishing, or quishing campaigns and get reports for a specific campaign or campaign job. Get the customer’s Company ID, then call the campaign search and campaign-job-report endpoints with **`X-KEEPNET-Company-Id`** so results are scoped to that company. Use a credential with Client Role = **Reseller**. The same pattern applies to **phishing**, **smishing**, and **quishing** simulators — only the base path changes.

***

## POST /api/companies/search

Get the customer’s Company ID. Use the `resourceId` of the desired company in the next steps.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company (e.g. by `name`) and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use `xC5kfGz7w2Nz` as Company ID in the campaign and report requests below.

***

## POST /api/phishing-simulator/phishing-campaign/search

Send the Company ID in the **`X-KEEPNET-Company-Id`** header so the list is scoped to the chosen company. Returns a paginated list of phishing campaigns for that customer. Response includes campaign `resourceId`, name, status, and other fields.

> Returns a list of the phishing campaigns. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. Request body: optional `filter`, `pageNumber`, `pageSize`, `orderBy`, `ascending`. **Test it:** Endpoints → **PhishingCampaign** → **Returns a list of the phishing campaigns** — use dummy data (H8d) and set the header to a Company ID from companies/search. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. Request body: optional `filter`, `pageNumber`, `pageSize`, `orderBy`, `ascending`. **Test it:** Endpoints → **PhishingCampaign** → **Returns a list of the phishing campaigns** — use dummy data (H8d) and set the header to a Company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Campaigns or enrollments with **Mark as Test** (`excludeFromReports: true`) are excluded from dashboard and report statistics in the platform UI; they may still appear in API list responses. When aggregating metrics for reporting, filter or ignore items where `excludeFromReports` is `true`.

Example request headers:

```http
Authorization: Bearer <your_access_token>
Content-Type: application/json
X-KEEPNET-Company-Id: xC5kfGz7w2Nz
```

Example body (dummy data — first page):

```json
{
  "pageNumber": 1,
  "pageSize": 20
}
```

### Smishing and quishing

Same flow with a different base path and same header:

* **Smishing:** `POST /api/smishing-simulator/smishing-campaign/search`
* **Quishing:** `POST /api/quishing-simulator/quishing-campaign/search`

***

## POST /api/phishing-simulator/phishing-campaign-job-report/search

Campaign **jobs** are run instances of a campaign. To get job-level reports (summary, clicked users, export), use this endpoint — it returns jobs with `resourceId` and `instanceGroup` that you need for the summary and export endpoints. Send **`X-KEEPNET-Company-Id`**. From the response, note `resourceId` and `instanceGroup` for the job you want to report on.

> Retrieves campaign job's list. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. Request body: see Endpoints → **PhishingCampaignJobReport** for the search request schema.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign-job-report/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

## GET /api/phishing-simulator/phishing-campaign-job-report/summary/{resourceId}/{instanceGroup}

Returns the summary report for one campaign job (sent, opened, clicked, etc.). Send **`X-KEEPNET-Company-Id`**.

> Returns campaign job summary. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign-job-report/summary/{resourceId}/{instanceGroup}" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example: `GET /api/phishing-simulator/phishing-campaign-job-report/summary/pJb2kL9mNq/1` with header `X-KEEPNET-Company-Id: xC5kfGz7w2Nz`.

### Export campaign or job report list

* **Export campaign list:** `POST /api/phishing-simulator/phishing-campaign/search/export` — same Company ID header and body shape as search (see Endpoints → **PhishingCampaign**).
* **Export campaign job report list:** `POST /api/phishing-simulator/phishing-campaign-job-report/search/export` — same header, request body per Endpoints → **PhishingCampaignJobReport**.

Smishing and quishing have equivalent paths under `smishing-simulator` and `quishing-simulator` (e.g. `.../smishing-campaign/search`, `.../smishing-campaign-job-report/search`, `.../summary/{resourceId}/{instanceGroup}`, `.../search/export`).

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID or campaign/job ID. Verify Company ID from `POST /api/companies/search` and job `resourceId`/`instanceGroup` from the campaign-job-report search; ensure you send `X-KEEPNET-Company-Id` for the customer that owns the campaign.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). Endpoint details: see **Endpoints** → **PhishingCampaign**, **PhishingCampaignJobReport** (and equivalent paths under smishing-simulator, quishing-simulator).
