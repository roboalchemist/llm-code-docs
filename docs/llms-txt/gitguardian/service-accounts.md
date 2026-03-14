# Source: https://docs.gitguardian.com/api-docs/service-accounts.md

# Service accounts

> How to create and manage service accounts, non-human API keys for automated scenarios like CI pipeline scanning, on the Business plan.

## Prelude

A **Service account** is a special type of API key intended to represent a non-human user that needs to authenticate and be authorized for scenarios such as secrets scanning in CI pipelines or batch processing open incidents.

> Please note that service accounts are **only available for workspaces under our Business plan**.

## Creating a service account

> **Only workspace Managers** are allowed to manage service accounts.

1. Go to the [Service accounts page](https://dashboard.gitguardian.com/api/service-accounts) in the API section of your workspace. Click on `Create service account`.
2. Name your service account according to its use-case (for example `<Service Name>-<Environment>`)
3. Set an expiry date for your token (in 1 week, 1 month, 3 months, 6 months, 1 year, or never). If an expiry date is set, all the Managers of the workspace will receive an email notification 5 days before expiration.
4. Choose one or several scopes for your service account.
5. Click on `Create service account`

Make sure you copy the service account, it will no longer be visible to you in the future.

![Service accounts modal](/img/api/service_accounts_modal.png)

The service accounts of your workspace are visible and can be managed [here](https://dashboard.gitguardian.com/api/service-accounts) by workspace Managers of workspaces under our Business plan.

![Service accounts table](/img/api/service_accounts_table.png)
