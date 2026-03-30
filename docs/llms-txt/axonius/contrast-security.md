# Source: https://docs.axonius.com/docs/contrast-security.md

# Contrast Security

Contrast Security protects software applications against cyberattacks.

## Asset Types Fetched

* Devices
  , Aggregated Security Findings
  , Software
  , SaaS Applications

## Parameters

1. **Contrast URL** *(required)* - The Contrast URL supplied from the Organization Keys of your account.

2. **User Name** *(required)* - The user name for an account that has read access to the API.

3. **API Key** *(required)* - The API Key as shown through the Contrast Security web interface.

4. **Organization IDs** *(optional)* - The Organization IDs as shown in the Organization Keys of your account.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

<Image align="center" alt="image.png" border={false} width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(439).png" />

<Callout icon="📘" theme="info">
  NOTE

  For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).
</Callout>

## APIs

<Callout icon="📘" theme="info">
  Axonius uses the [Contrast Security API](https://api.contrastsecurity.com/)
</Callout>

## Accessing the configuration information

To begin using the Contrast API, you need your API key, Username, and Service Key:

1. Log in to TeamServer
2. Click the top right navigation's down arrow next to your name in the page header
3. Your API Key and Service Key are at the bottom of the page under **YOUR KEYS**
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(447\).png)