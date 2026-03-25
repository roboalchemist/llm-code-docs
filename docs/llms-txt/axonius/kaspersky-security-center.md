# Source: https://docs.axonius.com/docs/kaspersky-security-center.md

# Kaspersky Security Center

Kaspersky Security Center is an administration console for Kaspersky Labs security solutions and systems management tools.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Kaspersky Security Center Domain** *(required)* - The hostname or IP address of the Kaspersky Security Center server.

2. **User Name** and **Password** *(required)* -  The credentials for an internal read-only user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Kaspersky Security Center.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Kaspersky%20Security%20Center.png)

## Required Ports

* Port 13299

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                      | Supported | Notes |
| ---------------------------- | --------- | ----- |
| Kaspersky Security Center 11 | Yes       |       |