# Source: https://docs.axonius.com/docs/servicenow-tickets-fetch.md

# ServiceNow Tickets Fetch

**ServiceNow Tickets Fetch**, a flavor of the [ServiceNow](https://docs.axonius.com/axonius-help-docs/docs/servicenow) adapter, fetches all tickets from:

* The incident table (this is the default behavior).
* Additional tables specified under **Additional ticket table names** in the adapter's [Advanced Settings](#advanced-settings) below, if configured.

<Callout icon="📘" theme="info">
  Note

  You can use the [ServiceNow adapter](/docs/servicenow) to fetch updates to tickets that were created by Axonius Enforcement Actions, provided these tickets have not been deleted from Axonius.
</Callout>

See detailed information on this adapter, including all parameters, in the [ServiceNow adapter documentation](/docs/servicenow).

## Asset Types Fetched

* Tickets

<Image border={false} src="https://files.readme.io/bd333c0da5ba5683e40170460b283fb2e97330de8666fc881f3037c1fac068ad-image.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch from the following Read Replica category (Must be supported on instance)** *(optional)* - Specify the name of a 'Read Replica' of the 'Operational' database to remove the load from the main database. The value must be an existing 'Read Replica Category' within ServiceNow. This depends on configuration in ServiceNow.
   * When supplied, all connections for this adapter fetch all data from the replica ServiceNow database instead of from the main database.
   * When not supplied, all connections for this adapter fetch data from the main database.

2. **Use the following field when filtering last updated** *(optional)* - Enter a ServiceNow field name to be used as the field that Axonius filters by for the *Fetch devices updated in ServiceNow in the last X hours*  and *Fetch users updated in ServiceNow in the last X hours*  configurations.
   * When a field is set, all connections for this adapter fetch devices or users which have the set field that was updated in the time defined.
   * When not supplied, all connections for this adapter fetch devices or users which were last updated  according to the ‘sys\_updated\_on’ ServiceNow field.

3. **Entries fetched per page** *(required, default: 500)* - Specify the maximum number of entries all connections for this adapter fetch per page when connecting the ServiceNow server.
   * The supplied value lets you control the performance of all the connections for this adapter. To reduce the number of requests sent to ServiceNow, but to avoid impact on overall performance, you can reduce the **Number of requests to perform in parallel** value and increase the **Entries fetched per page** value.

4. **Date Format** *(required)* - Generally, ServiceNow automatically identifies the date format. In some cases, the identification is ambiguous. You can set a specific date format for timestamps in ServiceNow. From the dropdown, select one of the following:
   * Automatically Identify (default)
   * DD/MM/YYYY
   * MM/DD/YYYY

5. **Number of requests to perform in parallel** *(required, default: 10)* - Specify the maximum parallel requests all connections for this adapter create when connecting the ServiceNow server. This setting lets you control the performance of all the connections for this adapter.

6. **Fetch Tickets By The Following Query** *(optional, default: sys\_updated\_on>javascript:gs.beginningOfLast120Days())*

7. **Additional ticket table names** - Enter a comma-separated list of additional ServiceNow table names from which to fetch tickets. This adapter will always fetch tickets created with Axonius enforcement actions (the default), in addition to any tables specified here.

8. **Custom (Tickets) schema** - Refer to the [ServiceNow adapter documentation](https://docs.axonius.com/docs/servicenow-adv-settings-custom-asset-schema) to learn about this capability.

9. **Advanced fields to show in basic view (Tickets)** *(optional)* - Open this section to configure one or more fields that generally appear in 'Advanced' to appear in the Tickets 'Basic' view (i.e., in the **Assets> Tickets** table).

   <Image alt="ServiceNowTicketsFetchAdvancedFieldsBasicVIew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowTicketsFetchAdvancedFieldsBasicVIew.png" />

   * **Custom schema entry (JSON)** - Type the custom schema of a field (in JSON format; see code below) that you would like to show in the Tickets basic view. Click the plus sign (`+`) to open a new box for entering the custom schema for each field that you want to show in the Tickets basic view.

     * **label** - The field name to appear in the basic Ticket view.
     * **raw\_field** - The field name as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table).
     * **field\_type** - The field type as  it appears in JSON format. The following field types are supported: int, string, datetime, float, bool. You can write them in the following ways: "int", "string", "str", "date", "datetime", "float", "bool", "boolean".

```JSON
[
{
    "label":"Field A", 
    "raw_field": "field_a",
    "field_type": "str"
}
]
```

<Callout icon="📘" theme="info">
  Note

  To learn more about the **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.0