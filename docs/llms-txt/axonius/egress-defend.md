# Source: https://docs.axonius.com/docs/egress-defend.md

# Egress Defend

Egress Defend is an email security solution that provides protection against phishing and data breaches.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the Egress Defend API.

#### Supported From Version

Supported from Axonius version 6.1.63

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.us1.defend.egress.com`)* - The hostname or IP address of the Egress Defend server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

3. **Organization Domains list** - Enter a list of domains the data will be fetched for.

![Egress Defend.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Egress%20Defend.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).