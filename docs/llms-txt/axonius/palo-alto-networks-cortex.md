# Source: https://docs.axonius.com/docs/palo-alto-networks-cortex.md

# Palo Alto Networks Cortex

The Palo Alto Networks Cortex adapter uses the Palo Alto Networks Cortex Hub to get information about Traps and GlobalProtect agents.

To connect the Palo Alto Cortex adapter, the adapter communicates with an Axonius Cloud endpoint that is authorized to fetch information from the Cortex hub.
Note that this adapter is not currently supported  by Palo Alto for integration with Axonius Customer-hosted deployments.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg) Aggregated Security Findings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents

## Parameters

1. **API Key** - An API key given by Axonius Cloud, as specified in the [Create an API Key](#creating-api-key) section.
2. **HTTPS Proxy** *(optional)* - A proxy to use when using the Palo Alto Cortex API.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Palo Alto Networks Cortex" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Palo%20Alto%20Networks%20Cortex.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Number of days to fetch** *(optional, default: 3)* - Enter the number of days which Axonius will fetch history. If no number is entered, all connections for this adapter will fetch 3 days of data.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Create an API Key

**To authorize Axonius to fetch data from Cortex Hub**

1. Log into [Cortex Hub](https://apps.paloaltonetworks.com/apps), then locate the [Axonius app](https://apps.paloaltonetworks.com/marketplace/axonius) and activate it.
2. Click on the Axonius app from the main portal.

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(734).png" />

3. You are redirected to the Axonius Cloud website. If this is your first time logging in, you need to register a new account in order to proceed.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(735).png" />

4. If the Request for Approval dialog appears, select **Read Logging Services** and click **Allow**.

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(736).png" />

5. From the Axonius Cloud website, click **Integrations** on the left menu to access the Integrations page. Then copy the API Key for the Palo Alto Networks Cortex integration.

   <Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(737).png" />

<Callout icon="📘" theme="info">
  Note

  The API Key might not display immediately upon login. If your Integrations page doesn't have a value for an extended period, contact Axonius support.
</Callout>

6. In Axonius, go to the Palo Alto Networks Cortex adapter, then add a new client and paste the API Key.