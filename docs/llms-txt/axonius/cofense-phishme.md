# Source: https://docs.axonius.com/docs/cofense-phishme.md

# Cofense PhishMe

Cofense PhishMe provides phishing awareness training and threat simulations for employees.

The Cofense PhishMe adapter enables Axonius to fetch and catalog users and their simulation data to provide visibility into organizational phishing awareness.

## Asset Types Fetched

* Users

## Before You Begin

### Authentication Methods

* API Token

### Required Parameters

The connection requires an API token associated with a user account that has the necessary permissions to fetch assets from the Cofense PhishMe server.

### APIs

Axonius uses the Cofense PhishMe API V2 to retrieve asset data. For more details, see the documentation available within your <Anchor label="Cofense PhishMe portal" target="_blank" href="https://login.phishme.com">Cofense PhishMe portal</Anchor> or the <Anchor label="Cofense Knowledge Center" target="_blank" href="https://cofense.com/knowledge-center">Cofense Knowledge Center</Anchor>.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Cofense PhishMe Domain** - Enter the Cofense PhishMe domain that is used, either *`https://login.phishme.com`* or *`https://login.phishme.co.uk`*.

2. **API Token** - Enter an API token associated with a user account that has permissions to fetch assets.

<Image align="center" alt="Cofense PhishMe adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Cofense_PhishMe_Add_Connection.png" className="border" />

### Optional Parameters

1. **Email Include list** - Enter a comma-separated list of email addresses.
   * If specified, the connection for this adapter will only fetch users whose email address is in the specified list.
   * If not specified, the connection for this adapter will fetch all users.

2. **Campaign Include list** - Enter a comma-separated list of full or partial campaign names.
   * If specified, the connection for this adapter will only fetch users participated in a campaign that its name contains at least one value in the specified list.
   * If not specified, the connection for this adapter will fetch all users.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Cofense PhishMe Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Enter an HTTPS proxy address to use when connecting to the value supplied in **Cofense PhishMe Domain**.

5. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Cofense PhishMe Domain** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - Enter the password to use when connecting to the value supplied in **Cofense PhishMe Domain** via the value supplied in **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Wait for scenario export to finish for X minutes before giving up** (*optional, default: 60*) – Enter the number of minutes the adapter should wait for a scenario export to complete before terminating the attempt.
2. **Use most recent Date Finished value as User Last Seen** (*optional*) – Select this option to use the latest **Date Finished** value from a campaign as the **User Last Seen** value in Axonius.