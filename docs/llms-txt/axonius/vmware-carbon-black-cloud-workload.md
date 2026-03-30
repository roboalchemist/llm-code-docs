# Source: https://docs.axonius.com/docs/vmware-carbon-black-cloud-workload.md

# VMware Carbon Black Cloud Workload

VMware Carbon Black Cloud Workload offers cloud workload protection and attack surface reduction.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the VMware Carbon Black Cloud Workload server.

2. **API Key** and **API ID** *(required)* - Use the API Key and  API ID you generated from the Connectors page of the VMware Carbon Black Cloud console.
   For details on generating the API Key and API ID, see [Carbon Black Cloud API Access Authentication](https://developer.carbonblack.com/reference/cb-defense/authentication/).

3. **Organization Key** *(optional, default: empty)* - Your organization key, which is located in the Carbon Black product console under **Settings `>` API Access `>` API Keys**.
   * If specified, Axonius will use [CB Defense REST API v6](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/devices-api/) to fetch data from the VMware Carbon Black Cloud adapter connection.
   * If not specified, Axonius will use [CB Defense REST API v3](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/rest-api/#devices) to fetch data from the VMware Carbon Black Cloud adapter connection.

4. **Verify SSL** *(required, default: false)* - Select to verify the SSL certificate offered by the value supplied in **VMware Carbon Black Cloud Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **VMware Carbon Black Cloud Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **VMware Carbon Black Cloud Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **VMware Carbon Black Cloud Domain**.

6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="VMware Carbon Black Cloud_Workload" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VMware%20Carbon%20Black%20Cloud_Workload.png" />

## APIs

Axonius uses the following CB Defense REST APIs:

* [CB Defense REST API - intergrationServices (v3)](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/deprecated/rest-api/#devices), if you have not specified an organization key.

* [CB Defense REST API - appservices (v6)](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/devices-api/), if you have specified an organization key.

It is highly recommended to use the [CB Defense REST API - appservices (v6)](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/devices-api/).

## Required Permissions

If CB Defense REST API - appservices (v6) is utilized, the value supplied in [API Key](#parameters) must be associated with credentials that have 'Device - General Information - Read' custom permissions.\
In addition, to create:

* [Change VMware Carbon Black Cloud Policy Enforcement Actions](/docs/change-carbon-black-cb-defense-policy-by-policy-id)
* [Isolate and Unisolate in VMware Carbon Black Cloud Enforcement Actions](/docs/isolate-and-unisolate-in-carbon-black-cb-defense)

you also need 'Device - Quarantine - Execute' permissions.

Refer to [Carbon Black Cloud API Access](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/#creating-a-custom-access-level) for full details of the custom access level steps.