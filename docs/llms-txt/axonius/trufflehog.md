# Source: https://docs.axonius.com/docs/trufflehog.md

# TruffleHog

TruffleHog is a security tool that scans code repositories for vulnerabilities related to secret keys, such as private encryption keys and passwords.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Secrets

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TruffleHog server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **API Secret** *(optional)* - The API Key secret displayed when the API key is created.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TruffleHog(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TruffleHog\(1\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch only verified secrets** *(default: true)* - By default, Axonius fetches only verified secrets. Clear this option to fetch all secrets.

Note: do not select both of the options below

* **Enrich Secrets with Locations** - Select this enrich each secret with its location information. Enable this option when fetching **ONLY VERIFIED SECRETS**.
* **Enrich Secrets with All Locations** - Select this option to enrich secrets with location information by fetching all locations from the TruffleHog API regardless of which secrets were fetched. Locations are matched to secrets by secret ID. Enable this option when fetching **ALL SECRETS** (both verified and unverified). Disable this option when fetching only verified secrets (use "Enrich Secrets with Locations" instead).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Refer to the <Anchor label="TruffleHog documentation" target="_blank" href="https://docs.trufflesecurity.com/">TruffleHog documentation</Anchor>.

## Supported From Version

Supported from Axonius version 6.0.