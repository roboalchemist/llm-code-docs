# Source: https://docs.axonius.com/docs/add-dns-custom-data.md

# Axonius - Enrich DNS Custom Data

**Axonius - Enrich DNS Custom Data** enriches DNS records from devices, domains or URLs with the preferred hostname for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **DNS Queries to enrich** -The DNS entries returned by these queries are added to the devices.

## Additional Fields

These fields are optional.

* **Append hostname suffix if not provided** - If a suffix to the hostname is not provided, append this value.
* **Exclude hostnames contains strings** - Exclude hostnames that include this character string.

## APIs

Axonius uses the Python package [aiodns](https://pypi.org/project/aiodns/).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).