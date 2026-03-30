# Source: https://docs.axonius.com/docs/foreman.md

# Foreman

Foreman is a free open source project that automates repetitive tasks, quickly deploys applications, and proactively manages server lifecycle, on-premises or in the cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Foreman Domain** *(required)* - The hostname or IP address of the Foreman server that Axonius can communicate with.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Foreman Adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Foreman.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch host packages** - Select this option to fetch host packages.
2. **Fetch APT security updates** - Select this option to fetch the APT security updates count.
3. **Fetch Encryption Keys** - Select this option to fetch encryption keys.
4. **Fetch Errata Information** - Select this option to fetch errata information from the Katello extension. Only available for Foreman instances with Katello installed.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [**Foreman Domain**](#parameters) via the following ports:

* **TCP port 443**