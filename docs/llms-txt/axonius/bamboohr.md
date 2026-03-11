# Source: https://docs.axonius.com/docs/bamboohr.md

# BambooHR

BambooHR is HR software used to collect, maintain, and analyze data for hiring, onboarding employees, and managing company culture.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data

**Related Enforcement Actions**

* [BambooHR - Suspend Employee](/docs/bamboohr-suspend-user)

## Parameters

The BambooHR adapter connection requires the following parameters:

1. **BambooHR Subdomain** – The BambooHR Subdomain value is used to log into your BambooHR instance. For example, if your BambooHR instance is *mycompany.bamboohr.com*, specify "mycompany".
2. **API Key** – To get the required API key value, go to *https\://\<your\_subdomain>.bamboohr.com/settings/permissions/api.php* and create a new key. If you do not have permission to do this, contact your BambooHR administrator.
3. **HTTPS Proxy** *(optional)* – Connect the adapter to a proxy instead of directly connecting it to the domain.
4. **Fetch users from endpoint** - Select the endpoint, either *employees/directory*  or  *report/custom*. report/custom is recommended. Refer to [Custom report API](https://documentation.bamboohr.com/reference/request-custom-report-1). for information.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="bamboo.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/bamboo.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore inactive users** - Select whether to exclude inactive users from the fetch.
2. **Ingest custom fields** - Toggle on this option to add custom fields.
   * **Custom fields list** - Enter a comma-separated list of custom fields to ingest.
   * **Fetch from table** *(optional)* - Enter a comma-separated list of the name(s) of the table(s) to fetch from.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>