# Source: https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/start-phishing-simulation-for-customer.md

# Start phishing simulation for a customer

As a Reseller you can create a phishing campaign for a customer and immediately start it so the simulation emails go out to target users. The flow: get the customer's Company ID, pick a scenario and target group, create the campaign, then start the campaign job. Use a credential with Client Role = **Reseller**. Send **`X-KEEPNET-Company-Id`** with every request.

***

## POST /api/companies/search

> Get the customer's Company ID first. Use the `resourceId` from the response as **`X-KEEPNET-Company-Id`** in all subsequent requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/phishing-simulator/phishing-scenario/search

> List phishing scenarios available for the customer. Send **`X-KEEPNET-Company-Id`**. Pick a scenario and note its `resourceId` — use it as `phishingScenarioResourceIds` in the campaign body.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-scenario/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/target-groups/search/current-company

> List target groups for the customer. Send **`X-KEEPNET-Company-Id`**. Use one or more `resourceId` values as `targetGroupResourceIds` in the campaign body.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/target-groups/search/current-company" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## GET /api/phishing-simulator/phishing-campaign/form-details

> Returns dropdown and reference data (email delivery settings, schedule types, etc.) needed to build the campaign. Send **`X-KEEPNET-Company-Id`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign/form-details" method="get" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/phishing-simulator/phishing-campaign

> Creates a new phishing campaign for the customer. Send **`X-KEEPNET-Company-Id`**. Body: `name` (required), `scheduleTypeId` (required), `phishingScenarioResourceIds`, `targetGroupResourceIds`, duration, distribution, and email delivery settings. See Endpoints → **PhishingCampaign** for the full schema.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example body (minimal — send immediately):

```json
{
  "name": "Q1 Phishing Simulation",
  "scheduleTypeId": 1,
  "phishingScenarioResourceIds": ["<scenarioResourceId>"],
  "targetGroupResourceIds": ["<targetGroupResourceId>"],
  "duration": 7,
  "distributionTypeId": 1,
  "distributionDelayEvery": 0,
  "distributionDelayTimeTypeId": 1,
  "sendingLimit": 0,
  "emailDeliverySettingType": 1,
  "excludeFromReports": false,
  "sendOnlyActiveUsers": true
}
```

From the response, note the campaign `resourceId`. Use it in the next step.

***

## POST /api/phishing-simulator/phishing-campaign-job/start/{resourceId}

> Starts the campaign — emails go out to target users. Replace `{resourceId}` with the campaign ID from the create response. Send **`X-KEEPNET-Company-Id`**. Body: `scheduleTypeId`, `targetGroupResourceIds`, and optional distribution config.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/phishing-simulator/phishing-campaign-job/start/{resourceId}" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

Example body (start immediately):

```json
{
  "scheduleTypeId": 1,
  "targetGroupResourceIds": ["<targetGroupResourceId>"],
  "excludeFromReports": false,
  "sendingLimit": 0,
  "distributionDelayEvery": 0,
  "distributionDelayTimeTypeId": 1,
  "useTargetUserTimeZone": false
}
```

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **400 Bad Request** — Invalid request body (missing scenario, target group, or schedule). Verify IDs from the search endpoints above; check Endpoints → **PhishingCampaign** for the full schema.
* **404 Not Found** — Invalid Company ID, scenario ID, or campaign ID.

{% hint style="info" %}
**Platform UI:** Create phishing campaigns under **Phishing Simulator → Campaign Manager**. [Campaign Manager →](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager)
{% endhint %}

**Related:** [Create and start phishing campaign for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/create-and-start-phishing-campaign-for-customer) (compact version). [List phishing scenarios for a customer →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/list-phishing-scenarios-for-customer). [View customer's campaign list and report →](https://doc.keepnetlabs.com/api-reference/reseller/phishing-simulation/view-customer-simulation-campaign-list-and-report). [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer).
