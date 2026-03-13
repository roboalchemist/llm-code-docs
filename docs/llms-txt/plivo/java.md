# Source: https://plivo.com/docs/voice/migrate/sdk/legacy-to-active-sdk/java.md

# Source: https://plivo.com/docs/voice/migrate/sdk/active-sdk/java.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade from Java SDK v4 to v4.8.0 or Latest Version

> Upgrade your Java SDK to v4.8.0+ — steps and breaking changes

## Introduction

This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

<Warning>
  **Deprecation notice:** Plivo Java SDK versions lower than 4.8.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
</Warning>

## Update the SDK

You can upgrade to the active SDK version without making any changes to your implementation if you’re not using any of the features or APIs mentioned in the breaking changes section below. Update the dependency in your project to compile **'com.plivo:plivo-java:4.8.0'** to upgrade to the active version of the SDK.

You can upgrade to the active SDK version without making any changes to your implementation if you’re not using any of the features or APIs mentioned in the breaking changes section below. Use the command **Update-Package Plivo -Version 4.10.0** to upgrade to the active version of the SDK, or upgrade to the latest version.

## Breaking Changes

If you are upgrading to versions higher than [v4.15.3](https://github.com/plivo/plivo-java/releases/tag/v4.15.3), be aware of a breaking change with those versions:

[v5.0.0](https://github.com/plivo/plivo-java/releases/tag/v5.0.0)

* **BREAKING:** Remove getTotalCount() method for list MDR
