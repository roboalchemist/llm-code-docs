# Source: https://docs.axonius.com/docs/a-cloud-guru.md

# A Cloud Guru

A Cloud Guru is an online learning platform that specializes in teaching cloud computing and related technologies.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.acloud.guru/`)* - The hostname or IP address of the A Cloud Guru server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to create the API Key, see [API Settings](https://business.acloud.guru/settings/api).

3. **Consumer ID** - The consumer's ID from A Cloud Guru. For information on how to create the Consumer ID, see [API Settings](https://business.acloud.guru/settings/api).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![A%20Cloud%20Guru](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/A%20Cloud%20Guru.png)

## APIs

Axonius uses the [A Cloud Guru API](https://api-docs.acloud.guru/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1