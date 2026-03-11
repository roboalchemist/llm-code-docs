# Source: https://docs.axonius.com/docs/replace-kenna-tag.md

# Kenna - Replace Tag in Assets

**Kenna - Replace Tag in Assets**  replaces Kenna tags for each of the entities that are the result of the saved query supplied as a trigger (or devices selected in the asset table).

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from the Kenna adapter** *(required, default: False)* - Select this option to use the first connected [Kenna Security Platform](/docs/kenna-security-platform) adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a [Kenna Security Platform](/docs/kenna-security-platform) adapter connection.
    * The user name and the password used for the adapter connection must have the required permissions to replace tags.
  </Callout>

* **New tag name** *(required)* - The new name of the tag.

* **Tag to replace** *(required)* - The old name of the tag.

  <Callout icon="📘" theme="info">
    Note

    * Only one tag can be replaced at a time.
  </Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Kenna Security Platform URL** - The URL for the Kenna Security Platform admin panel. This may be a default domain or a company specific URL.

  * **API Token** - Specify your account API key or an API token you have created.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).