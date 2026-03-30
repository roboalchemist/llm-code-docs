# Source: https://docs.axonius.com/docs/enrich-device-data-with-censys.md

# Censys - Enrich Asset Data

**Censys - Enrich Asset Data** (**Enrich Device Data with Censys**) enriches assets returned by the selected query with additional data from Censys, such as: ports open to the world, address information (country, region, city), ASN and more.
The data enrichment is done per device based on its public IP address (IPv4) or its domain name.

<Callout icon="📘" theme="info">
  Note

  You can use the **IPv4 Public Subnets** devices saved query as the trigger for a workflow that executes the **Censys - Enrich Asset Data** action.
  For more details, see [Selecting and Configuring Workflow Triggers](https://docs.axonius.com/axonius-help-docs/docs/selecting-the-workflow-trigger).
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Censys domain** - The Censys default domain is censys.io. You can change it, if required.

* **API ID** and **API secret** - Specify the Censys **API ID** and **API Secret**. See [Generating a Censys API ID and API Secret](/docs/enrich-device-data-with-censys#generating-a-censys-api-id-and-api-secret).
  **To generate a Censys API ID and API Secret:**

  1. Register for an account with Censys.
  2. Log into Censys and navigate to [/account/api](https://censys.io/account/api).
  3. Copy the API ID and Secret to use for the *censys\_api* fields in the config.py file.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Is paid tier** - Select if your API key is associated with a paid Censys account with a higher API quota.
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **Censys domain** - Should be ‘censys.io' if you are using API Version 1, or 'search.censys.io’ if you are using API Version 2.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).