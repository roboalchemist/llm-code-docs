# Source: https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/list-phishing-scenarios-for-customer.md

# List phishing scenarios for a customer

As a Reseller you can list a customer's phishing scenarios (templates used to run campaigns) scoped to that company. Get the customer's Company ID, then call the phishing-scenario search endpoint with **`X-KEEPNET-Company-Id`**. Use a credential with Client Role = **Reseller**. Use the scenario `resourceId` when creating or managing phishing campaigns for that customer.

***

## POST /api/companies/search

Get the customer's Company ID. Use the `resourceId` of the desired company in the next steps.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use as `X-KEEPNET-Company-Id` in the scenario requests below.

***

## POST /api/phishing-simulator/phishing-scenario/search

Returns a paginated list of phishing scenarios for that customer. Send **`X-KEEPNET-Company-Id`**. Response includes scenario `resourceId`, name, and other fields — use a scenario ID when creating a phishing campaign.

> Returns a list of the phishing scenarios. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. Request body: optional `filter`, `pageNumber`, `pageSize`, `orderBy`, `ascending`. **Test it:** Endpoints → **PhishingScenario** — use dummy data (H8d) and set the header to a Company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-scenario/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

To export the scenario list: **POST /api/phishing-simulator/phishing-scenario/search/export** — same header and body shape; see Endpoints → **PhishingScenario**.

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID. Verify Company ID from `POST /api/companies/search` and ensure you send `X-KEEPNET-Company-Id` for the customer.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [View customer's campaign list and report →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report) (campaigns and job reports). [Create and start phishing campaign for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/create-and-start-phishing-campaign-for-customer).
