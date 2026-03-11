# Source: https://tyk.io/docs/tyk-stack/tyk-developer-portal/enterprise-developer-portal/api-access/configuring-custom-rate-limit-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Custom Rate Limit Keys in Developer Portal

> How to configure custom rate limit keys in Tyk Developer Portal

## Introduction

The Tyk Enterprise Developer Portal supports custom rate limiting patterns that allow you to apply rate limits based on entities other than just credentials, such as per application, per developer, or per organization. This is particularly useful for B2B scenarios where API quotas need to be shared across multiple developers and applications within an organization.

For detailed information about custom rate limiting concepts and configuration, see the [Custom Rate Limiting](/api-management/rate-limit#custom-rate-limiting) section in the main Rate Limiting documentation.

**Prerequisites**

This capability works with [Tyk 5.3.0](/developer-support/release-notes/dashboard#530-release-notes) or higher.

## Configuring Custom Rate Limit Keys in the Portal

<Note>
  If you are using Tyk Developer Portal version 1.13.0 or later, you can configure the custom rate limit keys directly from the Developer Portal in the Advanced settings (optional) collapsible section of the Plan's view (by Credentials metadata).

  <img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-plan-advanced-settings.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=8f0bc85c1a91bd0f51d731195c6fa115" alt="Add Plan Advanced Settings" width="3456" height="1978" data-path="img/dashboard/portal-management/enterprise-portal/portal-plan-advanced-settings.png" />
</Note>

For general configuration of custom rate limit keys in policies, refer to the [Custom Rate Limiting](/api-management/rate-limit#custom-rate-limiting) documentation.

## Using Custom Rate Limit Keys with the Portal

The Tyk Enterprise Developer Portal facilitates the configuration of various rate limiting options based on a business model for API Products published in the portal.

To achieve this, the portal, by default, populates the following attributes in the credential metadata, which can be used as part of a custom rate limit key:

* **ApplicationID**: The ID of the application to which the credential belongs.
* **DeveloperID**: The ID of the developer who created the credential.
* **OrganisationID**: The ID of the organization to which the developer belongs.

Additionally, it's possible to attach [custom attribute values](/portal/customization/user-model#add-custom-attributes-to-the-user-model) defined in a developer profile as metadata fields to credentials.

When a credential is provisioned by the portal, all the fields described above are added as metadata values to the credential, making them valid options for configuring the rate limit key:

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/credential-metadata.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=256cf22ed7744c29cf1dfd848b72927d" alt="Credential's metadata" width="2878" height="1374" data-path="img/dashboard/portal-management/enterprise-portal/credential-metadata.png" />

This approach allows the portal to seamlessly apply rate limits based on any combination of the aforementioned fields and other custom metadata objects defined in policies used for plans or products. This is in addition to credentials.

***

<Note>
  **Tyk Enterprise Developer Portal**

  If you are interested in getting access contact us at [support@tyk.io](<mailto:support@tyk.io?subject=Tyk Enterprise Portal Beta>)
</Note>

Built with [Mintlify](https://mintlify.com).
