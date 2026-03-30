# Source: https://docs.axonius.com/docs/secureworks-red-cloak.md

# Secureworks Red Cloak

Secureworks Red Cloak is an Endpoint Detection and Response technology that continuously monitors endpoints for signs of adversary activity.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **API Zone User Name** *(required)*  - The API Zone user name for an account with read access to device data.
2. **API Zone Password** *(required)*  - The API Zone password for an account with read access to device data.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![secureworksREdcloak.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/secureworksREdcloak\(1\).png)