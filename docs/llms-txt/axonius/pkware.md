# Source: https://docs.axonius.com/docs/pkware.md

# PKWARE

PKWARE’s data protection platform finds, classifies, and protects sensitive data, allowing security managers to define data protection policies and monitor activity across the organization.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **PKWARE Domain** - The hostname of the PKWARE server.
2. **API Token** - Specify the API token you have generated.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PKWare.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PKWare.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - By default this adapter enriches devices via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Enrich Devices with Assignments** *(default: true)* - By default this adapter enriches devices with assignments. Toggle off to not enrich devices with assignments.
  * **Enrich Devices with Lockers** *(default: true)* - By default this adapter enriches devices with lockers. Toggle off to not enrich devices with lockers.
  * **Enrich Devices with Locker Status** *(default: true)* - By default this adapter enriches devices with locker status. Toggle off to not enrich devices with locker status.
* **Global Endpoints Config** - Click on `>` to open the following settings for configurable global endpoints:
  * **Avoid Locker duplications** *(default: true)* - By default this adapter avoids locker duplications. Clear this option to allow locker duplications.
  * **Avoid hostname duplications** - Select this option to avoid hostname duplications.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>