# Source: https://docs.axonius.com/docs/have-i-been-pwned.md

# Have I Been Pwned

Have I Been Pwned is a website to check whether email accounts have been compromised in a data breach.

The Enrich User Data by Have I Been Pwned (HIBP) adapter uses the HIBP API to provide information on breaches, pastes and pwned password identified by the 'Have I Been Pwned' (HIBP) website for a given email account.

<Callout icon="📘" theme="info">
  Note

  For details on the breaches, pastes and pwned password identified by 'Have I Been Pwned' (HIBP) API, see [HIBP API](https://haveibeenpwned.com/API/v3).
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Have I Been Pwned Domain** - Specify the Have I Been Pwned (HIBP) domain or use the default configured HIBP public domain. This allows you to use the domain of a proxy instead of connecting directly to the server using the default domain of *[https://haveibeenpwned.com](https://haveibeenpwned.com)*.

<Callout icon="📘" theme="info">
  Note

  The Domain field doesn't support multiple values. If you want to use multiple domains, you need to configure a separate adapter connection for each domain.
</Callout>

3. **API Key** - Use the API key you purchased from ['Have I Been Pwned'](https://haveibeenpwned.com/API/Key).
4. **Fetch All Subscribed Domains** - Select this option to fetch all subscribed domains under the API key.
5. **Account Domain** *(optional)* - Specify the account domain.

<Callout icon="📘" theme="info">
  Note

  When **Account Email** is not supplied, **Account Domain** is required.
</Callout>

4. **Account Email** *(optional)* - Specify a specific email account (e.g. [axonius@axonius.com](mailto:axonius@axonius.com)).

<Callout icon="📘" theme="info">
  Note

  When **Account Domain** is not supplied, **Account Email** is required.
  To run the HIBP query against multiple Account Emails, you must use the [Enrich User Data with Have I Been Pwned](/docs/enrich-user-data-with-have-i-been-pwned) Enforcement Center action.
</Callout>

4. **Verify SSL** - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **Rate Limit (requests per minute)** *(optional, default: 10)* - Use this field to handle rate limit issues by HIBP documentation. It is possible to  buy an account with a better rate limit.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Callout icon="📘" theme="info">
  Note

  When configuring this adapter, set the value of 'Wait for a connection to the source for up to X seconds' on the **Adapter Configuration** **[Advanced Settings](/docs/advanced-settings#wait-for-a-connection-to-the-source-for-up-to-x-seconds)** to at least 900.
</Callout>

![parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-YCAPJAM7.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch stealer logs** - Select this option to enrich users with stealer logs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>