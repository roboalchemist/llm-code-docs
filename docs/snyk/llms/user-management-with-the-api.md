# Source: https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api.md

# User management with the API

{% hint style="info" %}
**Feature availability**

The Snyk API is available only with Enterprise plans. For more information, see [plans and pricing](https://snyk.io/plans/).
{% endhint %}

You can manage users through the Snyk Web UI and Snyk API. You can also [manage service accounts](https://docs.snyk.io/implementation-and-setup/enterprise-setup/service-accounts/manage-service-accounts-using-the-snyk-api) using the API.

* You can use the [provisioning endpoints ](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/provision-users-to-organizations-using-the-api)to organize and grant permissions under a specified role for SSO users before initial log-on.
* You must use the API to [update member roles](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/update-member-roles-using-the-api).
* You can [remove users from Groups and Organizations](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/remove-members-from-groups-and-orgs-using-the-api) programmatically using the member endpoints.
* You can retrieve [audit logs](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/retrieve-audit-logs-of-user-initiated-activity-by-api-for-an-org-or-group) for the past 90 days using the Group-level audit logs endpoint to monitor user activity.
