# Source: https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/create-and-start-phishing-campaign-for-customer.md

# Create and start phishing campaign for a customer

As a Reseller you can create a phishing campaign for a customer and start a campaign job (run) so that the campaign sends emails to the customer's target users. Get the customer's Company ID, create the campaign with **`X-KEEPNET-Company-Id`**, then start a job using the campaign `resourceId`. Use a credential with Client Role = **Reseller**. You need a phishing scenario and target group or target users for that customer (see related use-cases).

***

## POST /api/companies/search

Get the customer's Company ID. Use the `resourceId` of the desired company in the next steps.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Use it as `X-KEEPNET-Company-Id` when creating the campaign and starting the job.

***

## GET /api/phishing-simulator/phishing-campaign/form-details

Optional. Returns dropdown and reference data (scenarios, target groups, email settings, etc.) needed to build the campaign create request. Send **`X-KEEPNET-Company-Id`** so options are scoped to that customer.

> **Test it:** Authorize, set header to the customer's Company ID, then Send.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign/form-details" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/phishing-simulator/phishing-campaign

Creates a new phishing campaign for that customer. Send **`X-KEEPNET-Company-Id`**. Request body includes scenario, target group or users, schedule, and other options — see Endpoints → **PhishingCampaign** → **Creates a new phishing campaign for a company** for the full schema.

> Creates a new phishing campaign for a company. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. **Test it:** Endpoints → **PhishingCampaign** — use dummy data (H8d) and set the header to a Company ID from companies/search.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, note the campaign `resourceId`. Use it in the start-job endpoint below.

***

## POST /api/phishing-simulator/phishing-campaign-job/start/{resourceId}

Starts a new campaign job (run) for the given campaign. Replace `{resourceId}` with the campaign `resourceId` from the create response. Send **`X-KEEPNET-Company-Id`**.

> Start new phishing campaign job with phishing campaign resource id. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign-job/start/{resourceId}" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example: `POST /api/phishing-simulator/phishing-campaign-job/start/pJb2kL9mNq` with header `X-KEEPNET-Company-Id: xC5kfGz7w2Nz`. To start a specific instance group, use **POST /api/phishing-simulator/phishing-campaign-job/start/{resourceId}/{instanceGroup}** (see Endpoints → **PhishingCampaignJob**).

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID or campaign ID; or invalid request body (e.g. missing scenario, target group). Verify Company ID from `POST /api/companies/search`, get scenario from [List phishing scenarios for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/list-phishing-scenarios-for-customer), target group from [List and create target groups for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/list-and-create-target-groups-for-customer); check Endpoints → **PhishingCampaign** for the create body schema.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [View customer's campaign list and report →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report) (list campaigns and job reports). [List phishing scenarios for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/list-phishing-scenarios-for-customer).
