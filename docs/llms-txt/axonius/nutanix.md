# Source: https://docs.axonius.com/docs/nutanix.md

# Nutanix Prism Central

Nutanix delivers hybrid and multicloud management, unified storage, database services, and desktop services to support applications and workloads.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Suggested Ports**

* 9440

**Authentication Method**

* User Name/Password

## APIs

Axonius uses the [Prism Central V3 API](https://www.nutanix.dev/api_references/prism-central-v3/#/4b402d5ab3edd-introduction).

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 4.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Nutanix Prism Central server. Example IP address format: 198.0.0.1:9440

2. **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.

<Image alt="NutanixPrismCentral" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NutanixPrismCentral.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [Nutanix Prism Central - Associate Categories](https://docs.axonius.com/axonius-help-docs/docs/nutanix-prism-central-associate-categories)