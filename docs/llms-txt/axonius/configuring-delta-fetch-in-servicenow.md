# Source: https://docs.axonius.com/docs/configuring-delta-fetch-in-servicenow.md

# Configuring Delta Fetch in ServiceNow

Use Delta Fetch to fetch big ServiceNow inventories, which can take a long time to fetch. In order to use Delta Fetch you need to configure two ServiceNow connections. This is relevant for both the Axonius Cyber Assets and Axonius SaaS Applications products.

<Callout icon="📘" theme="info">
  To perform this configuration, you must have access permissions  to ServiceNow's “sys\_audit\_delete” table.
</Callout>

# Configuring Full Fetch for the first Connection (not delta)

1. Configure the first connection to run at a low frequency (our best practice for big inventories is once a week, usually over the  weekend). Refer to [Adapter Custom Schedule](https://docs.axonius.com/docs/adapter-discovery-configuration#adapter-custom-cycle)
2. In the ServiceNow Add Connection dialog, make sure the following parameters are left empty:
   * Fetch devices updated in ServiceNow in the last X hours
   * Fetch users updated in ServiceNow in the last X hours

<Image alt="DeltaFEtchSErvuceNow" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-02XMB3D0.png" />

# Configuring Delta Fetch for the Second Connection

1. Configure a second ServiceNow connection (a delta connection), that will perform the delta fetch.

2. Configure this connection to run more frequently than the first,  (our best practice is once a day or each discovery cycle).

3. On the ServiceNow Add Connection dialog, configure the following parameters to fetch only the latest updated assets (our best practice is to set the value to 48 hours).
   * Fetch devices updated in ServiceNow in the last X hours
   * Fetch users updated in ServiceNow in the last X hours
     Note: make sure that the value of *Fetch users created in ServiceNow in the last X hours* is empty.
   * <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Z4ZEALGE.png" />

# General Configuration for Delta Fetch

In the adapter [Advanced Settings ](/docs/advanced-settings)  the values of the following parameters must be greater than the frequency set for the full fetch connection.

* Ignore devices that have not been seen by the source in the last X hours
* Ignore users that have not been seen by the source in the last X hours
* Delete devices and other assets that have not been returned from the source in the last X hours
* Delete users that were not been returned from the source in the last X hours

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-AM8BFFML.png" />