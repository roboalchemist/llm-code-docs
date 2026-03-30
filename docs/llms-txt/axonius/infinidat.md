# Source: https://docs.axonius.com/docs/infinidat.md

# Infinibox

Infinidat InfiniBox provides enterprise storage for mixed application workloads.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the InfiniBox server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![InfiniboxAdapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/InfiniboxAdapter.png)

## APIs

Axonius uses the [Infinibox REST API](https://infinisdk.readthedocs.io/en/latest/).

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0.