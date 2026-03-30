# Source: https://docs.axonius.com/docs/cloudflare-dns.md

# Cloudflare DNS

Cloudflare DNS runs one of the largest DNS networks in the world.

## &#x20;Assets Types Fetched

This adapter fetches the following types of assets:

* Devices
* Users (when **Fetch Users** is selected)
* Domains & URLs
* Certificates (when **Fetch Certificates** is selected)
* Load Balancers (when **Fetch Load Balancers** is selected)

## Before You Begin

### Authentication Method

API Key (legacy) or API Token

### Required Permissions

* Account Settings Read
* Zone Read
* DNS Read
* SSL and Certifates Read
* Include All accounts
* Include All zones

<br />

### APIs

The following API endpoints are used:

* accounts -> [https://developers.cloudflare.com/api/resources/accounts/](https://developers.cloudflare.com/api/resources/accounts/)
* zones -> [https://developers.cloudflare.com/api/resources/zones/](https://developers.cloudflare.com/api/resources/zones/)
* dns records -> [https://developers.cloudflare.com/api/resources/dns/subresources/records/](https://developers.cloudflare.com/api/resources/dns/subresources/records/)
* custom hostnames -> [https://developers.cloudflare.com/api/resources/custom\_hostnames/](https://developers.cloudflare.com/api/resources/custom_hostnames/)
* rule sets -> [https://developers.cloudflare.com/api/resources/rulesets/](https://developers.cloudflare.com/api/resources/rulesets/)

<br />

#

### Setting Up Cloudflare DNS to Work with Axonius

To create a token, open your Cloudflare account and navigate to **Get your API Key** -> **API Tokens** -> **Create Token**.

Then create the a token with the permissions listed in the image below. Once completed, obtain the generated API Token.

<Image alt="APITokenCreation" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-96EFLWLE.png" />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Cloudflare DNS, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Cloudflare Domain** - Keep as *`https://api.cloudflare.com`*.

<Tabs>
  <Tab title="Legacy">
    1) **User Email (legacy)** - the Email address associated with your Cloudflare account. For more details, see [Cloudflare API documentation](https://api.cloudflare.com/#getting-started-endpoints)
    2) **API Key** (a legacy authentication method) - Provides full permissions.
  </Tab>

  <Tab title="API Token">
    **API Token** -  Provides custom permissions, which you can configure.

    <Callout icon="💡" theme="warn">
      Note

      The adapter configuration does not support account-owned tokens. The token you provide must be a user token.
    </Callout>
  </Tab>
</Tabs>

<br />

<Image alt="CloudFlareDNS.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudFlareDNS.png" />

<br />

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse A and AAAA records as devices** - By default Axonius also parses A and AAA records as Devices.  Use this option to parse them only as Domains and URLs.
2. **Parse CNAME records as devices** - Select whether to fetch each CNAME record as a separate device.
3. **Fetch Custom Hostnames** - Select whether to fetch additional custom hostname information.
4. **Fetch users** - Select whether to fetch users, in addition to devices.
5. **Fetch Cloudflare WAF Rules** - Select this option to fetch WAF rules and associate them to devices based on the Zone they belong to.
6. **Fetch Certificates** - Select this option to fetch certificates.
7. **Fetch Load Balancers** - Select this option to fetch load balancers.
8. **Fetch Spectrum Applications** - Select this option to fetch spectrum applications as Devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>