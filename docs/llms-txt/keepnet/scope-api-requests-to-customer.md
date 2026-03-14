# Source: https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer.md

# Scope API requests to a customer

As a Reseller you manage multiple customer companies. Most list/report endpoints return data for **all** companies you manage. To get or change data for **one specific customer**, send that customer’s Company ID in the request. This page explains how Reseller scope works and where to pass Company ID.

***

## POST /api/companies/search

Get the customer's Company ID. Use the `resourceId` of the desired company as `X-KEEPNET-Company-Id` in scoped requests.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Use that value as `X-KEEPNET-Company-Id` or `companyId` in the endpoints listed under "Where to use Company ID" below.

***

## How Reseller scope works

* **Without Company ID:** Endpoints such as `POST /api/companies/search` and `GET /api/companies/my` return data for every company you (the Reseller) manage.
* **With Company ID:** To limit results or actions to a single customer (e.g. training report, phishing campaigns, target users), send the customer’s Company ID so the API scopes the response or operation to that company.

***

## How to send Company ID

Use one of these:

* **Header (recommended):** `X-KEEPNET-Company-Id: <companyResourceId>`
* **Query:** `?companyId=<companyResourceId>`
* **Path:** Some endpoints use `{companyId}` or `{resourceId}` in the path (e.g. `GET /api/companies/{resourceId}`).

Obtain customer Company IDs from [List companies with license details →](https://doc.keepnetlabs.com/api-reference/reseller/companies/list-companies-with-license-details) (`POST /api/companies/search`). The response includes `resourceId` per company — use that as `X-KEEPNET-Company-Id` or `companyId`. Use dummy/placeholder IDs in examples (H8d).

***

## Where to use Company ID

* **Reports:** Training, phishing, gamification, executive summaries, audit logs — pass Company ID to get that customer’s data. [View customer's enrollment list and report →](https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-list-and-report), [View customer's enrollment sending, certificates, and notifications →](https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-sending-certificates-notifications), [View customer's campaign list and report →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report), [Pull executive report data for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/reports/pull-executive-report-data-for-customer). Endpoint details: see **Endpoints** in the API Reference sidebar (TrainingReport, PhishingCampaign, ExecutiveReport, etc.).
* **Company & Users:** Add target users, target groups, enroll users in training, manage system users, set up SCIM — use Company ID to scope the operation to one customer. [Add target users for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/add-target-users-for-customer), [List or export target users for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/list-or-export-target-users-for-customer), [List and create target groups for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/list-and-create-target-groups-for-customer), [Set up SCIM for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/set-up-scim-for-customer), [Add system user for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/users-and-groups/add-system-user-for-customer). To create a new company (onboard): [Create a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/onboard-new-customer). To get, update, or delete a company: [Get a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/get-a-company), [Update a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/update-a-company), [Delete a company →](https://doc.keepnetlabs.com/api-reference/reseller/companies/delete-a-company).
* **Phishing simulation:** List scenarios and create/start campaigns for a customer. [List phishing scenarios for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/list-phishing-scenarios-for-customer), [Create and start phishing campaign for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/create-and-start-phishing-campaign-for-customer).

{% hint style="info" %}
**Quickstart:** Company ID usage is summarized in the [Quickstart →](https://doc.keepnetlabs.com/api-reference/quickstart) under “Reseller: scope by Company ID”.
{% endhint %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** — Invalid or unknown Company ID. Verify from `POST /api/companies/search`.
