# Source: https://docs.axonius.com/docs/absolute.md

# Absolute

Absolute specializes in software to manage and secure Windows computers and Android smartphones.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications

## Parameters

1. **Absolute Domain** *(required)* - Your Absolute API access domain. For a list of possible API access URLs, see [API access](https://api.absolute.com/api-doc/doc.html#:~:text=Accessing%20the%20API-,API%20access,-The%20URL%20you).

2. **Token ID**  and **Client Secret** *(required)* - Absolute API requires an authentication token that consists of two parts: token ID and secret key. You need to generate those from the Absolute console, using a custom user role, defined by your organization, or the Guest user role.
   For more details on creating a Token ID and a Secret Key, see [Create your API token](https://api.absolute.com/api-doc/doc.html#section/Getting-started:-Create-your-credentials/Create-your-API-token).

<Callout icon="📘" theme="info">
  Note

  The System Administrator of your Absolute console can assign the role.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Absolute" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Absolute.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch applications** - Select whether to fetch device applications from the Absolute server.
2. **Devices fetched per page** *(required, default: 50)* - Enter the maximum number of devices to fetch per paginated API request. The maximum value is 1000.
3. **Applications fetched per page** *(required, default: 1000)* - Enter the maximum number of applications to fetch per paginated API request. The maximum value is 10000.
4. **Fetch groups** - Select this option to fetch groups.
5. **Fetch only latest installed app version of devices** - Select this option to fetch only the latest installed app version of devices.
6. **Fetch custom data points device fields data** - Select this option to fetch all custom data points and their scan results for the device specified.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Absolute API v3](https://api.absolute.com/api-doc/doc.html).

## Troubleshooting

If you're experiencing issues with connectivity, enable **Authentication Debugging** in the Absolute console on the API Token Management page. After that, repeat the failed API requests to log the details. You can then contact Technical Support with the details collected in the log. Make sure you include the following:

* tokenID
* canonicalRequest
* x-abs-date
* signature

## Related Enforcement Actions

* [Absolute - Run Script](/docs/run-absolute-reach-scripts)
* [Absolute - Unenroll Asset](/docs/absolute-unenroll-asset)
* [Absolute - Update Custom Device Field](/docs/absolute-update-custom-device-field)
* [Absolute - Freeze Devices](https://docs.axonius.com/axonius-help-docs/docs/absolute-freeze)
* [Absolute - Unfreeze Devices](https://docs.axonius.com/axonius-help-docs/docs/absolute-unfreeze)