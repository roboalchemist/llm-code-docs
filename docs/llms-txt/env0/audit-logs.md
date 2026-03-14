# Source: https://docs.envzero.com/guides/admin-guide/audit-logs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View Audit Logs

> Track user activity and organizational events with enterprise audit logs in env zero

The audit log lists user activity-triggered events in your organization. The audit logs contain information about who performed the activity, when the action was performed, the activity's description, and additional data. Only an Admin user can access the audit logs.

<Info>
  **Feature Availability**

  Audit logs are only available to Enterprise level customers. Click [here for more details](https://www.env0.com/pricing)
</Info>

The audit log shows events related to changes in your:

* Organization
* Projects
* Templates
* Environments
* Teams
* Users
* Roles
* Modules
* Git Tokens
* Cloud credentials
* API keys
* SSH keys
* Variables
* Agent configurations

## Accessing the audit logs

#### Through the env zero UI

1. Go to the Organization's **Settings** page.
2. Click the **Audit Logs** tab.
3. The audit details are listed in a table.
4. Click the row's **+** sign to reveal additional activity details.
5. Click the **Show more** button at the bottom of the page to see more rows.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/e55f3be-screen_shot_2022-11-08_at_13.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=b082329af28287dd70b9af8265d85cad" alt="" width="2870" height="1236" data-path="images/guides/admin-guide/e55f3be-screen_shot_2022-11-08_at_13.png" />

#### Through the env zero API

Use this [API](/api-reference/audit-events/fetch-audit-logs) to retrieve your organization's audit logs programmatically.

Built with [Mintlify](https://mintlify.com).
