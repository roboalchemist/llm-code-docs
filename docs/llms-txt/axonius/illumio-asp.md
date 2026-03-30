# Source: https://docs.axonius.com/docs/illumio-asp.md

# Illumio Core

Illumio Core is a security platform that provides micro-segmentation to prevent unauthorized lateral movement within networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Load Balancers, Containers, Network/Firewall Rules, Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Illumio Core server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Authentication User Name** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. This is a randomized name generated when a user creates an API key.

3. **API Secret** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Organization ID** \*(required) - Auto generated when the API Secret is created.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Illumio.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Illumio.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch workloads**  *(default: true)* - Clear this option to stop fetching devices of the type “Workload”
2. **Additional Assets to Fetch** - From the dropdown, select one or more additional asset types to fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Illumio Core 24.2.10 REST API](https://product-docs-repo.illumio.com/Tech-Docs/Core/24.2/REST-APIs/REST_API_24.2.10/index.html#Illumio-Core).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8443**

## Required Permissions

The value supplied in [**Authentication User Name** and **API Secret**](#parameters) must have at least read-only role.
That user can have also one of the following Roles: Organization owner, Administrator.

To generate [**Authentication User Name**, **API Secret** and **Organization ID**](#parameters):

1. Log into the Illumio PCE web console.

2. Click your name in the top right corner:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1373\).png)

3. Click **My API Keys** in the drop-down list.

4. Click **+Add** in the window that appears:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1375\).png)

5. Fill in the **Name** (mandatory) and **Description** (optional).

6. Click **Save**.

7. Click **Show Credentials**:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1374\).png)

8. Copy and paste this information into a safe place. There is no way to
   retrieve it once you close this screen.

9. Optionally, you may choose to download the credentials into a file by
   clicking on **Download Credentials**. Keep this file in a very safe place.

## Related Enforcement Actions

* [Illumio - Create Workload](/docs/illumio-create-workload)
* [Illumio - Delete Workload](/docs/illumio-delete-workload)
* [Illumio - Unpair VEN from Workload](/docs/illumio-unpair-vens)
* [Illumio Update Workload](/docs/illumio-update-workload)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | No        |       |
| V2      | Yes       |       |