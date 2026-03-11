# Source: https://docs.axonius.com/docs/microfocus-sa.md

# Micro Focus Server Automation (HP Server Automation, Opsware)

Micro Focus Server Automation (formerly known as HP Server Automation or Opsware) provides operating system provisioning, automated patch management, and compliance control.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Hostname or IP Address** *(required)* - The Hostname or IP address of the Micro Focus Server Automation server that  Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![microfocus\_cnx\_screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/microfocus_cnx_screen.png)

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following ports:

* **TCP port 443**: SOAP API

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                                                    | Supported | Notes |
| ---------------------------------------------------------- | --------- | ----- |
| Micro Focus Server Automation 2018.08 (build 75.0.79007.0) | Yes       |       |