# Source: https://plivo.com/docs/voice/migrate/sdk/legacy-to-active-sdk/php.md

# Source: https://plivo.com/docs/voice/migrate/sdk/active-sdk/php.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade from PHP SDK v4 to v4.25.0 or Latest Version

> Upgrade your PHP SDK to v4.25.0+ — steps and breaking changes

## Introduction

This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

<Warning>
  **Deprecation notice:** Plivo PHP SDK versions lower than 4.25.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
</Warning>

## Update the SDK

Use the command **composer require plivo/plivo-php:4.25.0** to upgrade to the active version of the SDK, or **composer require plivo/plivo-php** to upgrade to the latest version.
