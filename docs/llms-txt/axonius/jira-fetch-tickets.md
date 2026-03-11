# Source: https://docs.axonius.com/docs/jira-fetch-tickets.md

# Jira Service Management (Service Desk) Fetch Tickets

Jira Service Management (Service Desk) is a project management tool that helps software development teams plan, track, and release software.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/tickets.svg) Tickets

## Before You Begin

### APIs

Axonius uses the [The Jira Cloud platform REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-search/#api-rest-api-2-search-get)(**/rest/api/2/search** with **JQL**) to fetch tickets.

### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Jira Service Management (Jira Service Desk) server.

2. **User Name** and **API Token** - The credentials for a user account that has permission to fetch assets. Note: The API Token is not the same as the Admin Key. For information on how to create an API Token, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Jira%20Tickets%20add%20connection.png" />

### Optional Parameters

<Callout icon="📘" theme="info">
  **Note**

  The **Workspace IDs** optional parameter is inherited from the [Jira Service Management](https://docs.axonius.com/axonius-help-docs/docs/atlassian-jira-service-desk) adapter and is not relevant to this adapter. You can leave this field empty.
</Callout>

1. **Jira Service Management API version** - The version type. The default value is 1.0.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

6. **Use Cloud API** - Use this option to add support for cloud-based installations of Jira Service Management (Service Desk) with Jira Insight.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **JQL** *(optional)* - Enter JQL code that will manually override the JQL query.

2. **Custom fields to show in basic view (Tickets)** *(Custom Schema Entry (JSON))* - Use these settings to add JSON text that represents the SNAP structure to parse the raw data field to basic view in the GUI. Refer to [Using Custom Schema Entries to Add JSON Text to Show in Basic View](/docs/jira-fetch-tickets#using-custom-schema-entries-to-add-json-text-to-show-in-basic-view) for examples of SNAP structures.

3. **Custom Parsing** - see [Adapter Custom Parsing](https://docs.axonius.com/axonius-help-docs/docs/adapter-custom-parsing) for more information on this capability.

4. **Fetch Child work items for Epic tickets** *(default: disabled)*- Enable this option to fetch child work items (i.e., epic links) for each epic ticket.

5. **Enable real-time asset updates (Supported events: New Tickets)** *(default: disabled)* - For `{{variable.IDM}}` only. When enabled, fetches newly created tickets after the last successful fetch run. If the JQL field is not empty, ' AND created `>` -`{last_run}`m' is appended to 'JQL'. When a new ticket is created, this enabled option causes the adapter to trigger a **Jira Ticket Created** event.

6. **Fetch EC Action ticket updates** - Select this option to fetch ticket updates from the ticketing system for tickets that were created by Axonius EC actions.

#### Using Custom Schema Entries to Add JSON Text to Show in Basic View

You can use custom schema entries to add JSON text to show in basic view. Use the plus sign to add an entry to each field.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Jira%20Fetch%20Tickets%20Custom%20schema%20entry%20advanced%20config.png" />

Enter fields in the following JSON format:

```json
[
  {
    "label": "Asset ID",
    "raw_field": "asset_id",
    "field_type": "str"
  },
  {
    "label": "Updated at",
    "raw_field": "updated",
    "field_type": "datetime"
  }
]
```

Custom field example:

```json
    {
    "label": "My Title",
    "raw_field": "fields/customfield_10907/value",
    "field_type": "str"
  }
```

* **label** - The name for the field you want to appear in the basic view.
* **raw\_field** - The name of the field as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table). The following is the raw\_field breakdown:
  `fields / fieldID / childelementkeyname`
  literal “fields” / field Identifier from Asset JSON View / Key Name of Child Element
* **field\_type** - The field type as  it appears in JSON format. The following field types are supported. int, string, datetime, float, bool. You can write them in the following ways:

  'int', 'string', 'str', 'date', 'datetime', 'float', 'bool', 'boolean'.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />