# Source: https://docs.axonius.com/docs/azure-defender-for-iot.md

# Azure Defender for IoT

Azure Defender for IoT is a solution for asset discovery, vulnerability management, and threat detection for Internet of Things (IoT) and operational technology (OT) devices.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications, Networks, Databases, Network Services

## Before You Begin

### APIs

Axonius uses the following APIs:

[Azure Defender for IOT API](https://docs.microsoft.com/en-us/azure/defender-for-iot/references-work-with-defender-for-iot-apis#retrieve-device-information---apiv1devices).

[Azure Resource Manager API](https://learn.microsoft.com/en-us/rest/api/azureresourcegraph/resourcegraph/resources/resources?view=rest-azureresourcegraph-resourcegraph-2024-04-01\&tabs=HTTP)

### Required Ports

Axonius must be able to communicate with the value supplied in [Domain](#parameters) via the following ports:

* **TCP port 443**

### Authentication Methods

You can authenticate the adapter using either a **Token** or **Azure Graph Resource Manager**. See the [Parameters](/docs/azure-defender-for-iot#parameters) section for more information.

## Parameters

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Azure Defender for IoT server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Select Connection Method** - Select between Token and Azure Graph Resource Manager.

### Authenticating with a Token

1. **Access token** *(required)* - An access token associated with a user account that has permissions to fetch assets.
2. **API Path** *(default: api/v1)* - You can specify a customizable API path instead of the default path.

<Image alt="AzureIoTParams1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-56NVCPBO.png" />

### Authenticating with Azure Graph Resource Manager

When this authentication method is selected, the adapter uses Azure Resource Graph to run queries to retrieve information about IoT Devices.

1. **Client ID**, **Client Secret**, and **Tenant ID** - See [Microsoft Azure Parameters](/docs/microsoft-azure#parameters) for instructions on how to configure these.

<Callout icon="📘" theme="info">
  Note

  The **Client ID** must have Reader access to the specific subscriptions that you want to fetch IoT Devices from.
</Callout>

2. **Fetch data from specific Azure Subscription IDs** *(Optional)* - Enter a list of comma-separated Subscription IDs to fetch data from, or leave this field empty to fetch from all subscriptions.
3. **Cloud Environment** *(Optional)* - Select the Azure cloud environment to fetch from.

<Image alt="AzureIoTParams2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-7BKZHHUD.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced Settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Devices to exclude by asset name** *(optional)* - Enter a comma-separated list of device asset names to exclude.
2. **Fetch Vulnerabilities** - Select to fetch vulnerabilities and attach them to their matching assets.

### Classify Azure IoT Defender Assets as Axonius Assets (Optional)

<Callout icon="📘" theme="info">
  Note

  This setting is not supported when the **Azure Graph Resource Manager** connection method is used. It's only supported when **Token** is used.
</Callout>

* **Enable custom asset fetch rules** - Enable this option to select specific Azure IoT Defender assets and define the Axonius assets types they will be fetched as.
  * **Azure IoT type to fetch as Network Devices assets** - Select between or both Switch and Router.
  * **Azure IoT type to fetch as Network Services assets** - Select between or both Internet and Multicast/Broadcast.
  * **Azure IoT type to fetch as Databases assets** - Here you can select only DB Server.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>