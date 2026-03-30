# Source: https://docs.axonius.com/docs/datadog.md

# Datadog

Datadog is a monitoring service for cloud-scale applications, providing monitoring of servers, databases, tools, and services.

**Related Enforcement Actions:**

* [Datadog - Create User](/docs/create-datadog-user)
* [Datadog - Update User](/docs/update-datadog-user)
* [Datadog - Suspend User](/docs/suspend-datadog-user)
* [Datadog - Update Network Device Tags](/docs/update-datadog-device-tags)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications
* Containers
* Compute Images

## Parameters

1. **Datadog Domain** *(required)* - The hostname or IP address of the Datadog server.
2. **Application Key** and **API Key** *(required)* - API and Application Keys associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  You must generate the API and Application Keys from two locations in the Datadog admin console.  In order for this to work, you need to pair both keys in the adapter wizard, as Datadog doesn't authenticate using only the Application Key — even with the scope of the key specified.
</Callout>

3. **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Datadog Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Datadog Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Datadog_parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SFHHTUCF.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Network Devices Monitoring** - Toggle on this option to fetch network devices.
  * **Fetch Network Devices Monitoring Interfaces** - Select this option to fetch interfaces for each network device.
* **Fetch Containers And Container Images** *(default: disabled)* - Select to fetch these asset types.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [**Application Key**](#parameters) must be associated with a user account that has read access to hosts and to users.

The following permissions are required in Application Key:

* host\_read
* user\_access\_read

To add a Datadog API key, application key, or client token, navigate to **Integration -> APIs**, enter a name for your key or token, and click **Create API key** or **Create Application Key** or **Create Client Token**.<br />
For more details, see [Datadog - API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/).

<Callout icon="📘" theme="info">
  Note

  If you are receiving a 403 "missing scopes" error, please attempt removing all Scope assignments from the Application Key and testing again.
</Callout>