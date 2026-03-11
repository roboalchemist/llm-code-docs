# Source: https://docs.axonius.com/docs/openshift.md

# Red Hat OpenShift Container

Red Hat OpenShift is a Kubernetes container platform that allows developers and operators to manage cloud-native applications throughout the DevOps cycle, for any cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Containers

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Red Hat OpenShift Container server.

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![OpenShift.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OpenShift.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Include Pods in device data** - Select this option to enrich devices with their pods data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Red Hat OpenShift Container Platform](https://docs.openshift.com/container-platform/3.11/welcome/index.html) API.

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5