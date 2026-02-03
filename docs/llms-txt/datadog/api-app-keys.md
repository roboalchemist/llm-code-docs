# Source: https://docs.datadoghq.com/account_management/api-app-keys.md

---
title: API and Application Keys
description: >-
  Manage API keys, application keys, and client tokens for browser applications
  with security features.
breadcrumbs: Docs > Account Management > API and Application Keys
---

# API and Application Keys

## API keys{% #api-keys %}

API keys are unique to your organization. An [API key](https://app.datadoghq.com/organization-settings/api-keys) is required by the Datadog Agent to submit metrics and events to Datadog.

## Application keys{% #application-keys %}

[Application keys](https://app.datadoghq.com/organization-settings/application-keys), in conjunction with your organization's API key, give users access to Datadog's programmatic API. Application keys are associated with the user account that created them and by default have the permissions of the user who created them.

### One-Time Read mode{% #one-time-read-mode %}

One-Time Read (OTR) mode is a security feature that limits the visibility of application key secrets to creation time only. When OTR mode is enabled, application key secrets are only displayed once during creation and cannot be retrieved later for security purposes.

#### For new organizations{% #for-new-organizations %}

All application keys for new parent organizations (and their child organizations) created after August 20th, 2025 have OTR mode enabled by default. This setting is permanent and cannot be changed.

#### For existing organizations{% #for-existing-organizations %}

Organization administrators can enable or disable OTR mode from [**Organization Settings** > **Application Keys**](https://app.datadoghq.com/organization-settings/application-keys). After enabling OTR mode:

- Application key secrets are visible only once, at the time of creation
- They are no longer retrievable through the UI or API
- The setting can be toggled on or off by organization administrators for 3 months after enabling
- After 3 months of being continuously enabled, OTR mode becomes permanent and the toggle is removed

**Permissions**: Users must have both the `org_app_keys_write` and `org_management` permissions to enable or disable OTR mode for their organization.

### Scopes{% #scopes %}

To better protect and secure your applications, you can specify authorization scopes for your application keys to define more granular permissions and minimize the access that applications have to your Datadog data. This gives you fine-grained access control over your applications and minimizes security vulnerabilities by limiting extraneous access. For example, an application that only reads dashboards does not need admin rights to manage users or delete any of your organization's data.

The recommended best practice for scoping application keys is to grant your keys the minimal privileges and least permissions necessary for an application to function as intended. Scoped application keys are granted only the scopes specified by the user, and no other additional permissions. While you can modify the authorization scopes of your application keys anytime, consider how those changes may impact the existing functionality or access of your application.

**Notes:**

- Users or service accounts with [permissions](https://docs.datadoghq.com/account_management/rbac/permissions) to create or edit application keys can scope application keys. A user must have the `user_app_keys` permission to scope their own application keys, or the `org_app_keys_write` permission to scope application keys owned by any user in their organization. A user must have the `service_account_write` permission to scope application keys for service accounts.
- Application owners cannot authorize an application if they are missing any required permissions, even if they scope an application key with authorization scopes that they do not have.
- Errors due to missing permissions when writing application keys or authorizing applications display a `403 Forbidden` error. More information about various error responses can be found in the [Datadog API](https://docs.datadoghq.com/api/latest/key-management/) documentation.
- If a user's role or permissions change, authorization scopes specified for their application keys remain unchanged.

### Actions API access{% #actions-api-access %}

Action APIs include:

- [App Builder](https://docs.datadoghq.com/api/latest/app-builder/)
- [Actions Connections](https://docs.datadoghq.com/api/latest/action-connection/)
- [Workflow Automation](https://docs.datadoghq.com/api/latest/workflow-automation/)

In order to use application keys with these APIs, you must enable Actions API access on the application key. This can be done [through the UI](https://app.datadoghq.com/organization-settings/application-keys) or [API](https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key). By default, application keys cannot be used with these APIs.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/click-enable-actions-api-access.ce8aca33ad7331b7e5af3cf0517b0957.png?auto=format"
   alt="Click Enable for Actions API Access" /%}

**Note**: The **Last used** section only shows if [Audit Trail is enabled](https://docs.datadoghq.com/account_management/audit_trail/#setup) in the account and you have [`Audit Trail Read`](https://docs.datadoghq.com/account_management/rbac/permissions/#compliance) permission.

## Client tokens{% #client-tokens %}

For security reasons, API keys cannot be used to send data from a browser, mobile, or TV app, as they would be exposed client-side. Instead, end user facing applications use client tokens to send data to Datadog.

Several types of clients submit data that requires a client token, including the following examples:

- The log collectors for [web browser](https://docs.datadoghq.com/logs/log_collection/javascript/), [Android](https://docs.datadoghq.com/logs/log_collection/android/), [iOS](https://docs.datadoghq.com/logs/log_collection/ios/), [React Native](https://docs.datadoghq.com/logs/log_collection/reactnative/), [Flutter](https://docs.datadoghq.com/logs/log_collection/flutter/), and [Roku](https://docs.datadoghq.com/logs/log_collection/roku/) submit logs.
- [Real User Monitoring](https://docs.datadoghq.com/real_user_monitoring/) applications submit events and logs.

Client tokens are unique to your organization. To manage your client tokens, go to **Organization Settings**, then click the **Client Tokens** tab.

**Note**: When a user who created a client token is deactivated, the client token remains active.

## Add an API key or client token{% #add-an-api-key-or-client-token %}

To add a Datadog API key or client token:

1. Navigate to Organization settings, then click the [**API keys**](https://app.datadoghq.com/organization-settings/api-keys) or [**Client Tokens**](https://app.datadoghq.com/organization-settings/client-tokens) tab.
1. Click the **New Key** or **New Client Token** button, depending on which you're creating.
1. Enter a name for your key or token.
1. Click **Create API key** or **Create Client Token**.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/api-key.60abd3d42408607da509794034239f28.png?auto=format"
   alt="Navigate to the API Keys page for your organization in Datadog" /%}

**Notes:**

- Your org must have at least one API key and at most 50 API keys.
- Key names must be unique across your organization.

## Remove API keys or client tokens{% #remove-api-keys-or-client-tokens %}

To remove a Datadog API key or client token, navigate to the list of keys or tokens, and click the **Delete**  icon next to the key or token you want to remove.

## Add application keys{% #add-application-keys %}

To add a Datadog application key, navigate to [**Organization Settings** > **Application Keys**](https://app.datadoghq.com/organization-settings/application-keys). If you have the [permission](https://docs.datadoghq.com/account_management/rbac/permissions) to create application keys, click **New Key**.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/app-key.539846c4c574bf013a47dc86ccfc0f52.png?auto=format"
   alt="Navigate to the Application Keys page for your organization in Datadog" /%}

{% callout %}
# Important note for users on the following Datadog sites: ap2.datadoghq.com, app.ddog-gov.com

{% alert level="danger" %}
Make sure to securely store your application key immediately after creation, as the key secret cannot be retrieved later.
{% /alert %}

{% /callout %}

{% alert level="info" %}
If your organization has One-Time Read (OTR) mode enabled, make sure to securely store your application key immediately after creation, as the key secret cannot be retrieved later.
{% /alert %}

**Notes:**

- Application key names cannot be blank.

## Remove application keys{% #remove-application-keys %}

To remove a Datadog application key, navigate to [**Organization Settings** > **Application Keys**](https://app.datadoghq.com/organization-settings/application-keys). If you have the [permission](https://docs.datadoghq.com/account_management/rbac/permissions) to create and manage application keys, you can see your own keys and click **Revoke** next to the key you want to revoke. If you have the permission to manage all org application keys, you can search for the key you want to revoke and click **Revoke** next to it.

## Key propagation delay and eventual consistency{% #key-propagation-delay-and-eventual-consistency %}

Datadog's API and application keys follow an eventual consistency model. Due to the distributed nature of Datadog's systems, updates to keys, such as creation and revocation, may take a few seconds to fully propagate.

As a result:

- Do not use new API or application keys immediately in critical workflows. Allow a brief period (a few seconds) for propagation. You can implement a retry strategy with short exponential backoff to handle transient errors during the propagation window.
- To validate whether an API key is active and usable, call the [/api/v1/validate](https://docs.datadoghq.com/api/latest/authentication/#validate-api-key) endpoint.
- To verify that an application key is active, use the `/api/v2/validate_keys` endpoint with the appropriate key pair.

Attempting to use a newly created key before it is fully propagated may result in temporary authentication errors such as 403 Forbidden or 401 Unauthorized.

## Scope application keys{% #scope-application-keys %}

To specify authorization scopes for application keys, [make a request to the Datadog API](https://docs.datadoghq.com/api/latest/key-management/) or the UI to create or edit an application key. Scopes can be specified for application keys owned by [the current user](https://docs.datadoghq.com/api/latest/key-management/#create-an-application-key-for-current-user) or a [service account](https://docs.datadoghq.com/api/latest/service-accounts/). If this field is unspecified, application keys by default have all the same scopes and permissions as the user who created them.

**Notes:**

- Scope names are case-sensitive.

## Using multiple API keys{% #using-multiple-api-keys %}

Consider setting up multiple API keys for your organization. For example, use different API keys for each of your various deployment methods: one for deploying an Agent on Kubernetes in AWS, one for deploying it on prem with Chef, one for Terraform scripts that automate your dashboards or monitors, and one for developers deploying locally.

Using multiple API keys lets you rotate keys as part of your security practice, or revoke a specific key if it's inadvertently exposed or if you want to stop using the service it's associated with.

If your organization needs more than the built-in limit of 50 API keys, contact [Support](https://docs.datadoghq.com/help/) to ask about increasing your limit.

## Disabling a user account{% #disabling-a-user-account %}

If a user's account is disabled, any application keys that the user created are revoked. Any API keys that were created by the disabled account are not deleted, and are still valid.

## Transferring keys{% #transferring-keys %}

Due to security reasons, Datadog does not transfer application keys from one user to another. If you need to share an application key, use a [service account](https://docs.datadoghq.com/account_management/org_settings/service_accounts/).

## What to do if an API or Application key was exposed{% #what-to-do-if-an-api-or-application-key-was-exposed %}

If a private key has been compromised or publicly exposed, steps should be taken as quickly as possible to ensure the security of your account. Removing the file containing the key from a public site such as GitHub **does not** guarantee it was not already accessed by another party.

Follow these steps to help safeguard your account:

**Note:** Revoking an active key may cause an impact to your services. If the scope of usage is large or undetermined, consider steps 2-5 **before** revoking the affected key.

1. Revoke the affected key.
1. Remove code containing the private key from any publicly accessible files:
   - Publish the sanitized file to your public repository.
   - Remove the sensitive data from your commit history.
1. Create a new key.
1. Update affected services with the new key.
1. Review your account for any unapproved access:
   - Users that have been recently added
   - New resources
   - Roles or permission changes

If any unusual activity is identified, or you need additional help securing your account, contact [Datadog support](https://docs.datadoghq.com/help/).

## Troubleshooting{% #troubleshooting %}

Need help? Contact [Datadog support](https://docs.datadoghq.com/help/).
