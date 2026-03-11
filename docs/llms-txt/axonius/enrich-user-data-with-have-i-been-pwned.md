# Source: https://docs.axonius.com/docs/enrich-user-data-with-have-i-been-pwned.md

# Have I Been Pwned - Enrich Users' Data

**Have I Been Pwned - Enrich Users' Data**  enriches users returned by the selected query or selected on the relevant asset page with breaches, pastes and pwned passwords identified by 'Have I Been Pwned' (HIBP) website.

<Callout icon="📘" theme="info">
  Note

  1. This Enfocrement Set supports only Users assets.
  2. For more information on the breaches, pastes and pwned password identified by 'Have I Been Pwned' (HIBP) API, see [HIBP API](https://haveibeenpwned.com/API/v3)
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **API key** - The API Key that have been purchased from ['Have I Been Pwned'](https://haveibeenpwned.com/API/Key).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Have I Been Pwned (HIBP) domain** *(default: `https://haveibeenpwned.com`)* - The hostname or IP address of the Have I Been Pwned (HIBP) server.

  * **API Key** - Use the API key you purchased from ['Have I Been Pwned'](https://haveibeenpwned.com/API/Key).

  * **Fetch All Subscribed Domains** - Select this option to fetch all subscribed domains under the API key.

  * **Account Domain** - Specify the account domain.

  * **Account Email** - Specify a specific email account (for example:  `axonius@axonius.com`).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Rate Limit (requests per minute)** *(default: `10`)* - Use this field to handle rate limit issues by HIBP documentation. It is possible to buy an account with a better rate limit.
</Callout>

* **Extra fields for enrichment** - Add email fields to be evaluated by Have I Been Pwned. Select an adapter and a field. Click **Add Fields** to add more fields. Click the **x** to the right of a field to delete it.

* **Skip Unchanged Enrichment** - Select this option to not perform the enrichment if no new breaches were found.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).