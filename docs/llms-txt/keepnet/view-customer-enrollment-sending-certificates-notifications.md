# Source: https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-sending-certificates-notifications.md

# View customer's enrollment sending, certificates, and notifications

As a Reseller you can view a customer's training enrollment **sending report** (emails sent, delivery status), **certificates**, **reminder mails**, and **notification activity logs** for a specific enrollment. Get the customer's Company ID and the enrollment ID from the enrollment list, then call the training-report and enrollment endpoints with **`X-KEEPNET-Company-Id`** so results are scoped to that customer. Use a credential with Client Role = **Reseller**.

***

## POST /api/companies/search

Get the customer's Company ID. Use the `resourceId` of the desired company in the next steps.

> Retrieves a paginated list of all companies you manage with license details. Each item includes `resourceId` — use it as the Company ID for scoped requests. **Test it:** Authorize with Client ID/Secret, then Send — request body is pre-filled.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/companies/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

From the response, pick the company and note its `resourceId`. Example: `"resourceId": "xC5kfGz7w2Nz"` → use as `X-KEEPNET-Company-Id` in all following requests.

***

## POST /api/enrollments/search

Get the customer's enrollment list so you can choose an enrollment to inspect. Send **`X-KEEPNET-Company-Id`**. From the response, take the `resourceId` of the enrollment you want (e.g. `"resourceId": "eNrl9Ab3k2Qp"`) — that is the `enrollmentId` for the sending, certificates, reminder, and notification endpoints below.

> Returns a list of enrollments. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**. Request body: `filter` (required — use the structure with `Condition`, `SearchInputTextValue`, `FilterGroups`; see [View customer's enrollment list and report](https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-list-and-report) for a full example), optional `pageNumber`, `pageSize`, `orderBy`, `ascending`, `enrollmentType`.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/enrollments/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/training-reports/{enrollmentId}/sending-report/search

Returns the **sending report** for that enrollment: emails sent, delivery status, and related data. Send **`X-KEEPNET-Company-Id`**. Replace `{enrollmentId}` with the enrollment `resourceId` from the enrollment list.

> Returns sending report training report for an enrollment. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/training-reports/{enrollmentId}/sending-report/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

To export: **POST /api/training-reports/{enrollmentId}/sending-report/search/export** — same header and body shape; see Endpoints → **TrainingReport**.

***

## POST /api/enrollments/{enrollmentId}/certificates/search

Search **certificates** issued for that enrollment. Send **`X-KEEPNET-Company-Id`**. Replace `{enrollmentId}` with the enrollment `resourceId`.

> Search enrollment certificates. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/enrollments/{enrollmentId}/certificates/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/training-reports/{enrollmentId}/reminder-mails/search

Returns **reminder mails** sent for that enrollment (e.g. training reminders). Send **`X-KEEPNET-Company-Id`**. Replace `{enrollmentId}` with the enrollment `resourceId`.

> Returns reminder mails for enrollment mails. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/training-reports/{enrollmentId}/reminder-mails/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## POST /api/notifications/{enrollmentId}/search

Search **notification activity logs** for that enrollment (e.g. email/Teams notifications). Send **`X-KEEPNET-Company-Id`**. Replace `{enrollmentId}` with the enrollment `resourceId`.

> Search notification activity logs with filtering and pagination. As a Reseller, send **`X-KEEPNET-Company-Id: <companyResourceId>`**.

{% openapi src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media>" path="/api/notifications/{enrollmentId}/search" method="post" expanded="true" %}
[keepnet-api-spec.json](https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2Fgit-blob-4014607a1a6ee7dd6b419e39e769b8d46d3d7d73%2Fkeepnet-api-spec.json?alt=media)
{% endopenapi %}

***

## Common errors

* **403 Forbidden** — Credential is not Reseller, or the Company ID is not one you manage. Set Client Role = **Reseller**. [Roles and permissions →](https://doc.keepnetlabs.com/next-generation-product/platform/company/system-users/user-roles)
* **401 Unauthorized** — Missing or invalid token. Request a new token via `POST /connect/token`.
* **404 Not Found** / **400 Bad Request** — Invalid Company ID or enrollment ID. Verify Company ID from `POST /api/companies/search` and enrollment ID from `POST /api/enrollments/search`; ensure you send `X-KEEPNET-Company-Id` for the customer that owns the enrollment.

**Related:** [Scope API requests to a customer →](https://doc.keepnetlabs.com/api-reference/reseller/companies/scope-api-requests-to-customer). [View customer's enrollment list and report →](https://doc.keepnetlabs.com/api-reference/reseller/training/view-customer-enrollment-list-and-report) (list enrollments and summary). For enrollment and training endpoints: see **Endpoints** → **Enrollment**, **TrainingReport** in the API Reference.
