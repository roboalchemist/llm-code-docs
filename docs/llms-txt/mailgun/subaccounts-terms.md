# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/subaccounts/subaccounts-terms.md

# Terminology

| Term | Definition |
|  --- | --- |
| **Primary Account** | The top-level organizational Mailgun account where subaccounts originate. |
| **Subaccount** | The separate-but-linked entities used to organize various use-cases, customers, etc. |
| **RBAC Permissions** | Primary account admin users and developers can create/manage subaccounts. Primary account RBAC user types with access to reporting and logs can view subaccount data. |


### Name and Status

Additionally primary account admins can edit name and status of subaccounts:

| Subaccount Status | Description |
|  --- | --- |
| Enabled | Default, subaccount has all available access via API and UI. |
| Disabled | API access suspended, UI access limited to read-only state. |
| Closed | Subaccount is deleted all data specific to that subaccount including API keys users and sending domains and sending history/stats are removed and cannot be recovered. |


### Use Cases

As subaccounts are designed for full segmentation of account assets, they can be used to support a number of business cases. The most common would be the need to give a separate business unit, project, or even a customer separate access to Mailgun including the separate of sending assets and data/reporting.

Other potential use cases include:

- You are a marketing platform that needs to segment your end-users into their own separate subaccounts.
- A cross-functional team also needs email capabilities but you need to ensure their sending assets and data is separate from your own.
- You have a specific mail stream or project that needs separate assets and reporting.