# Source: https://docs.axonius.com/docs/symantec-cloud-workload-protection-cwp.md

# Symantec Cloud Workload Protection (CWP)

The Symantec Cloud Workload Protection (CWP) adapter automates security policy enforcement to protect public cloud workloads.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Symantec Cloud Workload Protection (CWP) Domain** *(required, default: scwp.securitycloud.symantec.com)* - The hostname or IP address of the Symantec Cloud Workload Protection server.
2. **Domain ID** *(required)* - Enter your unique domain ID.
3. **Customer ID** *(required)* - Enter your unique identifier.
4. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. You can renew the client secret key on the Symantec Cloud Workload Protection product portal.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![symnatcecloudprotection.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/symnatcecloudprotection.png)