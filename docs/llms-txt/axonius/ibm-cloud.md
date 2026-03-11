# Source: https://docs.axonius.com/docs/ibm-cloud.md

# IBM Cloud

IBM's cloud computing platform combines platform as a service (PaaS) with infrastructure as a service (IaaS) and cloud services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Username** and **API Key** *(required)* - The SoftLayer username and API key credentials for a user account that has the permissions to fetch assets.
   * If you are using the SoftLayer ID, the supplied user name should be in the following format: SLXXXXXXX (e.g. SL1234567)
   * If you are using IBMid to authenticate, this is usually not your email address. The SoftLayer username will usually be in the form of `<AccountID>_EMAIL_ADDRESS@email.com`.
     * **Username** - The username will also be your VPN username for your account. You can find this in the cloud console by going to: **Manage** -> **Access (IAM)** -> **Users** -> (select your user) -> **VPN section**
     * **API Key** - This API key is under the **classic infrastructure** dropdown of the apikeys page. You can only have one classic infrastructure API key per user. Once created, it will not be displayed again, so make sure to write it down.
       :::
2. **Endpoint URL** *(optional, default: `https://api.service.softlayer.com/rest/v3.1/`)* - Specify the SoftLayer API endpoint URL.
   * If supplied, the connection for this adapter will use the specified URL as the SoftLayer API endpoint URL
   * If not supplied, the connection for this adapter will use the default value.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Endpoint URL**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Endpoint URL** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Endpoint URL** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Endpoint URL**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Endpoint URL**.
   * If not supplied, Axonius will connect directly to the value supplied in **Endpoint URL**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1860).png" />