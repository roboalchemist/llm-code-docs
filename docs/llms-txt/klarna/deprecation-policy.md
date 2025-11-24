# Source: https://docs.klarna.com/resources/legal-and-compliance/policies-and-term-of-service/deprecation-policy.md

# Deprecation policy

As a Klarna connected merchant, you have the right to use Klarna’s web service, SDKs and modules in order to handle your transactions with Klarna. This policy explains to what extent Klarna develops and supports them. The table below will explain the different statuses we use:


![Services status](089e7796-989f-4629-949c-bd062bc6bfd4_FOOTER_deprecation-policy.jpeg)
*Services status*

## API

Deprecation within Klarna’s API’s can be split into two different types; API versions and API calls. An API version is determined by breaking changes within the API and API Calls is determined by functionalities for communication towards Klarna.

### Deprecation of API versions

Full support is always given to the latest API version. If a new API version is released by Klarna, the previous version with full support will be legacy. The old legacy version will be deprecated. A Deprecated version will be removed from Klarna’s system within a timeframe set by Klarna, minimum of 6 months. Affected users will be informed.

### Deprecation of API calls

Klarna can from time to time deprecate specific calls from existing API versions and may replace them with newer and better API calls. When a call has been set as Legacy, the new call replacing is hereinafter treated as Full Support and shall be used with all new integrations towards Klarna. A Deprecated call will be removed from Klarna’s system within a timeframe set by Klarna, minimum of 6 months. Affected users will be informed.

## SDKs

Full support is always given to the most recent version and the programming language version that the SDK is developed for. If a new minor version is released by Klarna, the previous version with full support will be legacy. The old legacy version will be dropped down to deprecated. A Deprecated library will be supported, during a limited timeframe set by Klarna, minimum of 6 months. Affected users will be informed. We follow semantic versioning as detailed by [semver.org](http://semver.org/).

## Modules

Full support is always given to the most recent official Klarna module version and platform versions that the particular module is developed for. If a new platform version makes it impossible for the module to support the new and the old version, a new module with Full support will be developed. The old Legacy version will be dropped down to Deprecated. A Deprecated module will be supported, according to table 1, during a limited timeframe set by Klarna, minimum of 6 months. Affected users will be informed.

### Example of support status

| Klarna module version | Supported platform version | Klarna module status |
|-----------------------|----------------------------|----------------------|
| 4.2.x                 | 1.7.0.2                    | Full support         |
| 4.1.x                 | 1.7.0.1, 1.6.0, 1.6.2      | Legacy               |
| 4.0.x                 | 1.6.2, 1.6.0, 1.5          | Deprecated           |