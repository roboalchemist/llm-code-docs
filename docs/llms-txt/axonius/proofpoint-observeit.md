# Source: https://docs.axonius.com/docs/proofpoint-observeit.md

# Proofpoint's ObserveIT Insider Threat Management Platform

Proofpoint's ObserveIT Insider Threat Management (ITM) platform is a cloud-based solution that provides insider risk detection, incident response, and unified visibility across user activity, data interaction, and threat context.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Proofpoint's ObserveIT Insider Threat Management (ITM) platform server.
   You can find the **Host Name** in the ObserveIT API explorer library. For example, `https://app.oitroot.us-east-1-op1.op.observeit.net` (note the region may be different).

2. **Client ID** and **Client Secret** *(required)* - A Client ID and Client Secret associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="ProofPointObservit.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProofPointObservit.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use the alias field as hostname if os = OSX** *(required, default: true)* - Select whether to use the alias field as hostname if the macOS is OS X.
2. **Use the Alias field as the Serial Number for MacOS Devices** *(optional)* - Select to use the value in the Alias field for the Serial Number field for OS X hosts.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

**To create Proofpoint API credentials**

1. Go to the Proofpoint Developer console.
2. Create new application credentials.
3. Grant **All Scope (\*)**.
4. Click the **Shield** icon next to the new application.
5. Add policy permissions: **Full View Permissions**.