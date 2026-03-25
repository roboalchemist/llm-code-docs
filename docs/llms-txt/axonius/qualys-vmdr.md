# Source: https://docs.axonius.com/docs/qualys-vmdr.md

# Qualys VMDR OT

Qualys VMDR OT is a cloud-based platform for asset inventory and vulnerability management of critical industrial infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Qualys VMDR server. This depends on the platform and is defined [here](https://www.qualys.com/platform-identification/) in the **API Gateway URL** field.

2. **User Name** and **Password** *(required)* - The Qualys account credentials that you should use to fetch asset data.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Qualys VMDR OT](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Qualys%20VMDR%20OT.png)

## APIs

Axonius uses the [Qualys VMDR OT API](https://docs.qualys.com/en/vmdr-ot/api/#t=vmdrot_api%2Fch01%2Fget_started.htm).

## Required Permissions

The value supplied in [User Name](#parameters) must have VMDR OT.API.ACCESS permissions in order to fetch assets. Assign this permission in the Administration Utility in the Qualys platform.

## Supported From Version

Supported from Axonius version 6.1