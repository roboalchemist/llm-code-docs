# Source: https://docs.axonius.com/docs/symantec-control-compliance-suite.md

# Symantec Control Compliance Suite (CCS)

Symantec Control Compliance Suite (CCS) is a solution to help identify security gaps and vulnerabilities and automate compliance assessments for over 100 regulations, mandates, and best practice frameworks including GDPR, HIPAA, NIST, PCI and SWIFT. Symantec CCS discovers and inventories all networks and assets including managed and unmanaged devices allowing for assets to be profiled and ranked for risk potential.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Symantec CCS Domain** *(required)* - The hostname or IP address of the Symantec CCS server.
2. **User Name** and **Password** *(required)* - The user name and password for a read-only user with 'Assets Viewer' role.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![symnact control complaince.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/symnact%20control%20complaince.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Evaluation standard ids to fetch information from** - Enter a list of unique standard identifiers to fetch information from.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>