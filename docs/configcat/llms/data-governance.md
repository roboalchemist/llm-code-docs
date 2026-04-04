# Source: https://configcat.com/docs/advanced/data-governance.md

# Data Governance - CDN

Copy page

ConfigCat's Data Governance feature gives you control over how and where your config JSONs are published and served from. This helps you comply with regional data handling requirements such as GDPR.

## CDN - Data Centers[​](#cdn---data-centers "Direct link to CDN - Data Centers")

To ensure high availability and low response times worldwide, ConfigCat provides multiple global data centers, each with multiple CDN nodes for built-in redundancy and failover.

### ConfigCat Data Center locations[​](#configcat-data-center-locations "Direct link to ConfigCat Data Center locations")

ConfigCat uses Cloudflare Edge Cache Network to deliver the configuration JSONs to the SDKs. Read more about Cloudflare data centers [here](https://www.cloudflare.com/network/).

## How to govern the data?[​](#how-to-govern-the-data "Direct link to How to govern the data?")

Currently available geographical areas:

### Global \[Default][​](#global-default "Direct link to Global \[Default]")

Provides geo-location based load balancing on all nodes around the globe to ensure the lowest response times.

### EU Only[​](#eu-only "Direct link to EU Only")

Compliant with GDPR. This way your data will never leave the EU.

## Set preferences on the Dashboard[​](#set-preferences-on-the-dashboard "Direct link to Set preferences on the Dashboard")

Open [Data Governance page](https://app.configcat.com/organization/data-governance) and follow the steps to set preferences.

> Only team members with Organization Admin role can access Data Governance preferences.

## Set up the ConfigCat SDK in your application code[​](#set-up-the-configcat-sdk-in-your-application-code "Direct link to Set up the ConfigCat SDK in your application code")

Make sure the `dataGovernance` option is specified when initializing the ConfigCat SDK in your application code.

> The `dataGovernance` option's value must be in sync with the selected option on the Dashboard.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

#### What if I forget to specify the `dataGovernance` option?[​](#what-if-i-forget-to-specify-the-datagovernance-option "Direct link to what-if-i-forget-to-specify-the-datagovernance-option")

By default, the ConfigCat SDK contacts the ConfigCat Global CDN. However, if you switch to the EU CDN on the Dashboard, your config JSONs will only be published to the EU CDN nodes. Therefore, if you forget to specify the `dataGovernance` option when initializing the ConfigCat SDK, feature flag data download requests will need to be redirected to the EU CDN. To avoid this, it's recommended to specify the correct `dataGovernance` option, otherwise response times can be significantly longer.

#### `Warning: The dataGovernance parameter specified at the client initialization is not in sync with the preferences on the ConfigCat Dashboard....`[​](#warning-the-datagovernance-parameter-specified-at-the-client-initialization-is-not-in-sync-with-the-preferences-on-the-configcat-dashboard "Direct link to warning-the-datagovernance-parameter-specified-at-the-client-initialization-is-not-in-sync-with-the-preferences-on-the-configcat-dashboard")

**Don't worry,** your feature flags will still be served. See above example.
