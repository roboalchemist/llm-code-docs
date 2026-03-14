# Source: https://plivo.com/docs/voice/migrate/sdk/active-sdk/active-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade from SDK v4 to v4.8.0 or Latest Version

> Upgrade your Plivo SDK within the v4.x line — breaking changes guide

<Tabs>
  <Tab title="Node">
    # Upgrade from Node SDK v4 to v4.8.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      <strong>Deprecation notice:</strong> Plivo Node SDK versions lower than 4.8.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently.  Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    Use the command **npm install plivo\@4.8.0** to upgrade to the active version of the SDK, or **npm install plivo\@latest** to upgrade to the latest version.
  </Tab>

  <Tab title="Ruby">
    # Upgrade from Ruby SDK v4 to v4.9.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      **Deprecation notice:** Plivo Ruby SDK versions lower than 4.9.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    Use the command **gem install plivo -v 4.9.0** to upgrade to the active version of the SDK, or **gem update plivo** to upgrade to the latest version.
  </Tab>

  <Tab title="Python">
    # Upgrade from Python SDK v4 to v4.9.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      **Deprecation notice:** Plivo Python SDK versions lower than 4.9.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    Use the command **pip install --upgrade plivo==4.9.0** to upgrade to the active version of the SDK, or **pip install --upgrade plivo** to upgrade to the latest version.
  </Tab>

  <Tab title="PHP">
    # Upgrade from PHP SDK v4 to v4.25.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      **Deprecation notice:** Plivo PHP SDK versions lower than 4.25.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    Use the command **composer require plivo/plivo-php:4.25.0** to upgrade to the active version of the SDK, or **composer require plivo/plivo-php** to upgrade to the latest version.
  </Tab>

  <Tab title=".NET">
    # Upgrade from .NET SDK v4 to v4.10.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      **Deprecation notice:** Plivo .NET SDK versions lower than 4.10.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    You can upgrade to the active SDK version without making any changes to your implementation if you’re not using any of the features or APIs mentioned in the breaking changes section below. Use the command **Update-Package Plivo -Version 4.10.0** to upgrade to the active version of the SDK, or **Update-Package Plivo** to upgrade to the latest version.

    ## Breaking changes

    If you are upgrading to versions higher than [v4.17.1](https://github.com/plivo/plivo-dotnet/releases/tag/v4.17.1), be aware of a breaking change with those versions:

    [v5.0.0](https://github.com/plivo/plivo-dotnet/releases/tag/v5.0.0)

    * **BREAKING:** Removed the total\_count parameter in metadata for list MDR response
  </Tab>

  <Tab title="Java">
    # Upgrade from Java SDK v4 to v4.8.0 or Latest Version

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
  </Tab>

  <Tab title="Go">
    # Upgrade from Go SDK v4 to v4.8.0 or Latest Version

    ## Introduction

    This is a minor application update. Plivo recommends you always use the latest or an active version of our SDKs for guaranteed security, stability, and uptime. The active SDK versions are designed to handle intermittent and regional failures of API requests. In addition, they offer a host of security features, such as protection against DoS attacks and bot detection for suspicious user agents.

    <Warning>
      **Deprecation notice:** Plivo Go SDK versions lower than v4.8.0 are being deprecated on January 31, 2022. If you use a deprecated version of our SDK after that date, your API requests and voice calls may fail intermittently. Plivo will no longer provide bug fixes to these versions, and our support team may ask you to upgrade before debugging issues.
    </Warning>

    ## Update the SDK

    You can upgrade to the active SDK version without making any changes to your implementation if you’re not using any of the features or APIs mentioned in the breaking changes section below. Use the command go get github.com/plivo/plivo-go/v7\@v4.8.0 to upgrade to the active version of the SDK, or go get github.com/plivo/plivo-go/v7\@latest to upgrade to the latest version.

    ## Breaking changes

    If you are upgrading to a version higher than [v4.9.1](https://github.com/plivo/plivo-go/releases/tag/v4.9.1), be aware of some breaking changes with those versions:

    [v5.0.0](https://github.com/plivo/plivo-go/releases/tag/v5.0.0)

    * **BREAKING:** Rename MultiPartyCall struct to PhloMultiPartyCall

    [v6.0.0](https://github.com/plivo/plivo-go/releases/tag/v6.0.0)

    * **BREAKING:** Update AddSpeak method signature: remove optional parameters
    * Add methods to set SpeakElement attributes

    [v7.0.0](https://github.com/plivo/plivo-go/releases/tag/v7.0.0)

    * Remove the total\_count parameter in metadata for list MDR response
  </Tab>
</Tabs>
