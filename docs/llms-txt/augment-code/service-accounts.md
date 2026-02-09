# Source: https://docs.augmentcode.com/cli/automation/service-accounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Service Accounts

## About

Service Accounts provide non-human identities for automation use cases to make API requests to the Augment backend through Auggie CLI. They decouple automation tasks from using individual user accounts and enable per-automation task token lifecycle management.

## Managing Service Accounts

Service Accounts can be managed by navigating to [app.augmentcode.com/settings/service-accounts](https://app.augmentcode.com/settings/service-accounts) and logging in. Service accounts are only available to [Enterprise plan](https://augmentcode.com/pricing) customers. Service accounts can only be managed by the Administrator of the Enterprise Plan.

### Creating a Service Account

To create a new service account, click the "New Service Account" button. You will be prompted to enter a name and an optional description for the service account. The account name must be unique within your organization.

### Creating API tokens

Once you've created a service account, you can create API tokens for it by clicking the "Add API token" button next to the service account name in the list of service accounts. You will be prompted to enter a name for the API token which must be unique amongst the tokens for this service account. Once you've created a token, you will be given a one time opportunity to retrieve the token value by either:

* Copying the token value directly or using the "Copy token" button **OR**
* Downloading a `session.json` file that is ready to use with Auggie CLI.

API tokens for service accounts don't have an expiration date and need to be manually revoked if they are no longer needed.

### Deleting Service Accounts and API tokens

API tokens can be revoked by selecting "Revoke" from the triple dot menu next to the token name in the service account list. Note that revoking a token is a permanent action and cannot be undone. Any existing Auggie CLI automation sessions using the token will be disrupted.

Service accounts can be deleted by clicking "Manage" next to the service account name in the service account list, and then clicking "Delete Account" from the dialog that appears. Note that deleting a service account will also delete all the associated API tokens.

## Using API tokens with Auggie CLI

In order to use a service account API token with Auggie CLI, you need to edit the `session.json` file stored under `~/.augment`. If you've downloaded a `session.json` file after creating the API token, you can simply replace the existing `session.json` file with the new one. If you've only copied the token value, you need to edit the `session.json` file with the following content and replace the `accessToken` value with the new token value.

```
{
  "accessToken": "<TOKEN VALUE>",
  "tenantURL": "<TENANT URL>",
  "scopes": [
    "read",
    "write"
  ]
}
```

The correct `tenantURL` value for your organization is displayed on top of the service account list in the management UI.

## Best Practices

* Use a separate service account per automation task. This will allow you to manage token lifecycle and monitor credit usage per automation task.
* Use the ability to create multiple tokens under a service account to rotate tokens when needed. Create a new API token, update the automation tasks to use the new token, and revoke the old token once all automation tasks have been updated.
