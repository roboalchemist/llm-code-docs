# Source: https://docs.axonius.com/docs/trend-micro-worry-free.md

# Trend Micro Worry-Free

Trend Micro Worry-Free is an endpoint and SaaS solution protecting against malware, scripts, injection, ransomware, memory and browser attacks, and exploits.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Login Domain** *(required, Default: `https://tm.login.trendmicro.com`)* - The hostname or IP address of the Trend Micro Worry-Free server.

2. **Console Domain**  *(required, Default: `https://wfbs-svc-emea.trendmicro.com`)* - The domain to which the user who signed in is redirected.

3. **Tenant ID** *(required, Default: TM)* - The authentication tenant ID. This is the prefix of the 'Login Domain'.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has permissions to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TrendMicroWorryFreeUP.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrendMicroWorryFreeUP.png)

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to fetch assets.
It is recomended to create an API  account with read only permissions to fetch information for this adapter. and log into Trend Micro Worry-Free using this account.

<Image alt="TrendMicroAPI1.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrendMicroAPI1.png" />