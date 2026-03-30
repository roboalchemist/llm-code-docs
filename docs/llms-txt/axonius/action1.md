# Source: https://docs.axonius.com/docs/action1.md

# Action1  

Guide for setting up and configuring the Action1 adapter in Axonius, including asset types, permissions, and advanced settings.

## Adapter Description

Action1 is a cloud-based platform that automates patch management and vulnerability remediation.

### Asset Types Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications

## Before You Begin

### Authentication Method

Client ID and Client Secret

### APIs

Axonius uses the following APIs:

* [Action1 API /organizations](https://app.action1.com/apidocs/#/System/get_organizations)
* [Action1 API /endpoints/managed/`{orgId}`](https://app.action1.com/apidocs/#/Endpoints/get_endpoints_managed__orgId___endpointId_)

### Permissions

The following permissions are required:

* `view_endpoints`
* `view_vulnerabilities` - for the 'Enrich Devices with Vulnerabilities' advanced setting.
* `view_installed_software` - for the 'Enrich Devices with Software' advanced setting.

#### Supported From Version

Supported from Axonius version 6.1

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Action1, and click on the adapter tile. Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Action1 server.
2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that are required in order to access the Action1 API. For information on how to create your API credentials, see [API Credentials](https://www.action1.com/api-documentation/api-credentials/).

<Image alt="Action1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Action1.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

1. **Enrich Devices with Vulnerabilities** - Toggle on to enrich devices with vulnerabilities.
2. **Enrich Devices with Software** - Toggle on to enrich devices with installed software and missing patches.

## Related Enforcement Actions

* [Action1 - Deploy Package](https://docs.axonius.com/axonius-help-docs/docs/action1-deploy-package)