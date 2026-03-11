# Source: https://docs.axonius.com/docs/logrhythm.md

# LogRhythm

LogRhythm combines SIEM, user and entity behavior analytics, network traffic and behavior analytics, and security automation and orchestration.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**
Port 8501 must be accessible for Axonius to communicate with the API in [LogRhythm Domain](#required-parameters).

**Authentication Method**

* API Token

### Generating API Token for LogRhythm API

1. Launch the **LogRhythm client console**.
2. Select  **Deployment Manager** `>` **Third Party Applications**.
3. Create a new third-party application. To do this:
   * Click the green **Plus** sign in the Client Console toolbar. The **Third Party Application** Properties window is displayed.
   * Specify the name and description for your application in the appropriate fields.
4. Click **Apply** to generate the token. This will force a quick restart of the authentication server to set up and validate the token. After a few moments, the client ID and client secret will appear.
5. Adjust the expiry date as desired to make the token last longer or expire faster. By default, the token expires after 365 days (one year).
6. Click **Generate Token** to create an API token.
7. Enter the user name and password of the LogRhythm account that the token should connect with.
8. Copy and paste the token into a text file that can be referenced from the PowerShell script.

<Image alt="image.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(469).png" />

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **LogRhythm Domain** - The hostname of the LogRhythm server. The LogRhythm Domain format is https\://\[instance]:8501.
2. **API Token** - API Token generated to use the LogRhythm API. For more details, see [Generating API Token](/docs/logrhythm#generating-api-token-for-logrhythm-api).

![LogRhythm.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LogRhythm.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **LogRhythm Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **LogRhythm Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Assets** *(default: true)* - Select this option to fetch data from the 'agent' endpoint.
2. **Fetch log sources behind collectors** - Select this option to fetch configured syslog log sources.
3. **Fetch recent device logs for determining Last Seen** *(default: true)* - Select this option to only fetch the most recent device logs to determine the 'Last Seen' value.
4. **Ignore devices with record status** *(default: Retired)* - Enter a record status with which to ignore devices.
5. **Avoid parsing IP address as asset name** - Select this option to avoid parsing the asset name if it contains a valid IP address.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>