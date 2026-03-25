# Source: https://docs.axonius.com/docs/knowb4-phisher.md

# KnowBe4 PhishER

KnowBe4 PhishER is a security awareness tool that helps train users to identify and mitigate phishing threats.

### Asset Types Fetched

* Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [KnowBe4 APIs](https://developer.knowbe4.com/graphql/phisher/page/Introduction).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 6.1.45

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - Specify the appropriate KnowBe4 PhishER FQDN from [this list](https://developer.knowbe4.com/graphql/phisher/page/Base-URL) in the form: `https://region.knowbe4.com`
   This adapter requires access to this destination on port 443.

<Callout icon="📘" theme="info">
  Note

  The suffix '/graphql' should not be specified in the adapter configuration.
</Callout>

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Authentication](https://developer.knowbe4.com/graphql/phisher/page/Authentication).

<Image alt="KnowBe4 PhishER" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KnowBe4%20PhishER.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).