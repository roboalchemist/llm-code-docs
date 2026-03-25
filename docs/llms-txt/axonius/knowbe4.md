# Source: https://docs.axonius.com/docs/knowbe4.md

# KnowBe4

KnowBe4 provides Security Awareness Training for anti-phishing behavior, social engineering and ransomware attacks, and general security awareness.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the [KnowBe4 API](https://developer.knowbe4.com/reporting/).

You are required to enable the Reporting API key in KnowBe4 and then create the API key to work with this adapter.

**To enable the Reporting API key in KnowBe4**

1. From the KnowBe4 console, click your email address at the top-right corner of the page and select **Account Settings**.
2. Navigate to \*\*Account Integrations> API.
3. Under **Reporting API**, select the **Enable Reporting API Access** checkbox.

**To create the API key**

1. Under **Reporting API**, click **Reporting API**.
2. In the **Reporting API** subtab that opens, click **+ Create New API Token**.
3. In the **Create New API Token** dialog, enter the following information:
   * **Name** - A descriptive name for this API token.
   * **Status** - Enable or disable the API token.
4. Click **Create Token**. The **Reporting API Token** pop-up window opens.
5. Copy the **Reporting API Token** into [**API Key**](#required-parameters). Make sure to save your copied API token somewhere that you can easily access. After you close this window, you will not be able to view this token again.
6. Click **OK**.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the KnowBe4 server. Use one of the following values:
   * Accounts on the US server (located at training.knowbe4.com) - Use `https://us.api.knowbe4.com`
   * Accounts on the EU server (located at eu.knowbe4.com) - Use `https://eu.api.knowbe4.com`
2. **API Key** - The Reporting API key from Knowbe4. Used to pull data from the KnowBe4 console for reporting purposes. For details, see [APIs](#apis).

<Image alt="KnowBe4.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KnowBe4.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Remove fields without value from the latest fetch** - By default, all adapters keep the last known value of each field, in case that field was not populated during the last fetch. Select this option to remove fields without value from the latest fetch.
2. **User status include list** *(optional)* - Specify a comma-separated list of user statuses.
3. **Ignore archived users** - Select this option so that all connections for this adapter do not fetch archived users from KnowBe4.
4. **Parse employee number as employee ID** - Select this option to parse the employee number as the employee ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>