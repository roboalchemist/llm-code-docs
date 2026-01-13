# Source: https://docs.datadoghq.com/account_management/org_settings/service_accounts.md

---
title: Service Accounts
description: >-
  Create and manage non-interactive service accounts for automated scripts and
  shared application keys across teams with secure access controls.
breadcrumbs: Docs > Account Management > Service Accounts
source_url: https://docs.datadoghq.com/org_settings/service_accounts/index.html
---

# Service Accounts

## Overview{% #overview %}

Service accounts are non-interactive accounts you can use to own application keys and other resources that are shared across your teams. Service account application keys can only be viewed once by the individual who created the key.

Suppose an employee at your company sets up an automated script to send requests to the Datadog API, using their personal application key. When that employee leaves the company, you deactivate their Datadog account, and their application key stops working. The automated script also stops working, until someone updates it with a valid application key. Using a service account application key instead of a personal application key for automated requests to the Datadog API avoids this problem.

## Navigation{% #navigation %}

Service accounts exist in [Organization Settings](https://docs.datadoghq.com/account_management/org_settings/).

To access service accounts in the UI:

1. Navigate to **Organization Settings** from your account menu.
1. Under **Accounts**, select **Service Accounts**.

The [Service Accounts page](https://app.datadoghq.com/organization-settings/service-accounts) contains a list of all service accounts in your organization. Users with the Service Account Write permission, including users with the Datadog Admin Role, may create service accounts. Users without the Service Account Write permission see a read-only view.

### View service accounts{% #view-service-accounts %}

By default, the Service Accounts page shows only active service accounts. To include disabled service accounts in the list below, select **Disabled**.

Use the search box at the top of the page to filter service accounts. The filter searches name, email, and role fields.

Click on an account to access a detailed side panel view with the following information:

- Status (active or disabled)
- Created and last modified dates
- Roles
- Application keys
- Permissions

### Create service account{% #create-service-account %}

To create a service account, perform the following steps:

1. Click **New Service Account**. A dialog box appears.
1. Enter a name and email address for your service account.
1. Use the **Assign Roles** dropdown menu to choose one or more roles for your service account.
1. To save, click **Create Service Account**.

Unlike the email addresses for Datadog users, service account email addresses do not need to be unique across an organization.

### Edit service account{% #edit-service-account %}

To modify a service account, click on one in the service accounts list.

1. In the side panel, click **Edit** next to the service account name. A dialog box appears.
1. Update any fields you would like to change. You can edit the name, email address, status, and roles.
1. Click **Save**.

To disable a service account, the user must have the User Manage Access permission in addition to Service Account Write.

To disable a service account, follow the previous procedure to edit the service account and set the status to **Disabled**.

### Create or revoke application keys{% #create-or-revoke-application-keys %}

To create or revoke service account application keys, select an account from the service account list. The service account's side panel appears.

To create a new application key, follow the steps below:

- Click **New Key**. A dialog box appears.
- Give the key a descriptive name.
- Click **Create Key**.

The dialog box refreshes, showing you the key. Copy and paste the key into your desired location. After you close the dialog box, you cannot retrieve the value of the key.

{% callout %}
# Important note for users on the following Datadog sites: ap2.datadoghq.com, app.ddog-gov.com

{% alert level="danger" %}
Service account application keys are one-time read only. Make sure to securely store your application key immediately after creation, as the key secret cannot be retrieved later.
{% /alert %}

{% /callout %}

To revoke an application key, find the key in the service account detailed view side panel and hover over it. Pencil and trash can icons appear on the right. Click the trash can to revoke the key. After the key is revoked, click **Confirm**.

### API{% #api %}

See the [Service accounts API reference](https://docs.datadoghq.com/api/latest/service-accounts/) to use service accounts through the Datadog API.

## Service account application keys{% #service-account-application-keys %}

You can view a service account applications key exactly once, immediately after you create it. Limiting the access to the application key prevents any problems that may occur when another user accesses the key. If you lose or forget a service account key, revoke it and create a new one.

## Permissions{% #permissions %}

By creating a service account, you create an actor that interacts with Datadog on your behalf. Your capabilities on the Service Accounts page vary depending on your Datadog roles and permissions.

Creating a service account requires the Service Account Write permission. The Datadog Admin role includes Service Account Write, so anyone with the Datadog Admin role can create service accounts.

When creating a service account, you can give it any subset of the roles and permissions that you have. The exception is if you have the User Access Manage permission, which effectively gives you administrator access to do anything in Datadog. Datadog accounts with the User Access Manage permission have no restrictions on the roles and permissions they can assign to service accounts.

## Notifications{% #notifications %}

Datadog sends a notification to the email address associated with the service account when the following actions occur:

- Create an application key
- Revoke an application key
- Disable the service account

## Further reading{% #further-reading %}

- [Service accounts API reference](https://docs.datadoghq.com/api/latest/service-accounts/)
