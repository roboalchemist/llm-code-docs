# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/incident-management/servicenow.md

# ServiceNow

![](/img/guides/icons/ServiceNow.svg)![](/img/guides/icons/ServiceNow.svg)

Loading version...

Port's ServiceNow integration allows you to model ServiceNow resources in your software catalog and ingest data into them.

Supported resources ![](/img/icons/external-link.svg)GroupService CatalogIncidentRelease ManagementVulnerabilityCustom

Ingesting extra resources

The ServiceNow integration uses the [ServiceNow Table API](https://developer.servicenow.com/dev.do#!/reference/api/xanadu/rest/c_TableAPI#table-GET) to ingest entities, which means you can ingest any resource that exists in the Table API, not just the ones listed above. Simply specify the `table name` as a new `kind` in the [Data sources configuration page](/build-your-software-catalog/sync-data-to-catalog/.md#customize-your-integrations) and the records from the table will be ingested to Port.

## Setup[â](#setup "Direct link to Setup")

### Authentication methods[â](#authentication-methods "Direct link to Authentication methods")

The ServiceNow integration supports two authentication methods:

1. **Basic authentication** - Uses a ServiceNow username and password.
2. **OAuth 2.0 client credentials** - Uses OAuth client ID and client secret for more secure authentication.

OAuth authentication recommended

OAuth 2.0 is the recommended authentication method as it provides better security and doesn't require sharing user credentials. The integration automatically handles token refresh and expiration.

You can configure the authentication method by providing the appropriate credentials:

* For **basic authentication**, provide `servicenowUsername` and `servicenowPassword`.
* For **OAuth authentication**, provide `servicenowClientId` and `servicenowClientSecret`.

The integration will automatically detect and use OAuth authentication if client credentials are provided.

**Setting up OAuth in ServiceNow (click to expand)**

To use OAuth authentication, you need to create an OAuth application endpoint in ServiceNow:

1. Log in to your ServiceNow instance as an administrator.

2. Navigate to **System OAuth** > **Application Registry**.

3. Click **New** to create a new application.

4. Select **Create an OAuth API endpoint for external clients**.

5. Fill in the following details:

   <!-- -->

   * **Name**: Give your application a descriptive name (e.g., "Port Integration").
   * **Client ID**: This will be auto-generated, or you can specify a custom one.
   * **Client Secret**: This will be auto-generated. Make sure to copy it securely.
   * **Accessible from**: Select "All application scopes".

6. Click **Submit** to save the configuration.

7. Use the generated **Client ID** and **Client Secret** in your integration configuration.

For detailed information about OAuth client credentials configuration in ServiceNow, refer to the [ServiceNow OAuth documentation](https://www.servicenow.com/docs/bundle/zurich-platform-security/page/integrate/machine-identity/task/configure-an-oauth-client-credential-grant.html).

### Installation methods[â](#installation-methods "Direct link to Installation methods")

Choose your preferred installation method below. Not sure which to pick? See the [installation methods overview](/build-your-software-catalog/sync-data-to-catalog/.md#installation-methods).

1Choose method2Install

Hosted by Port

* â§Port hosts and manages the integration
* â§Customizable resync interval for data ingestion
* â§Access control flexibility

Self-hosted

* â§Host and manage the integration in your infrastructure
* â§Real-time updates via webhooks
* â§Best for high-security or custom networking needs

CI

* â§Run as a one-time job in your CI pipeline or on a scheduled basis
* â§Minimal infrastructure management

Install

## Configuration[â](#configuration "Direct link to Configuration")

Port integrations use a [YAML mapping block](/build-your-software-catalog/customize-integrations/configure-mapping.md#configuration-structure) to ingest data from the third-party api into Port.

The mapping makes use of the [JQ JSON processor](https://stedolan.github.io/jq/manual/) to select, modify, concatenate, transform and perform other operations on existing fields and values from the integration API.

### Default mapping configuration[â](#default-mapping-configuration "Direct link to Default mapping configuration")

This is the default mapping configuration for this integration:

**Default mapping configuration (click to expand)**

```
resources:
- kind: sys_user_group
  selector:
    query: 'true'
    apiQueryParams:
      sysparmDisplayValue: 'true'
      sysparmExcludeReferenceLink: 'false'
  port:
    entity:
      mappings:
        identifier: .sys_id
        title: .name
        blueprint: '"servicenowGroup"'
        properties:
          description: .description
          isActive: .active
          createdOn: .sys_created_on | (strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%dT%H:%M:%SZ"))
          createdBy: .sys_created_by
- kind: sc_catalog
  selector:
    query: 'true'
    apiQueryParams:
      sysparmDisplayValue: 'true'
      sysparmExcludeReferenceLink: 'false'
  port:
    entity:
      mappings:
        identifier: .sys_id
        title: .title
        blueprint: '"servicenowCatalog"'
        properties:
          description: .description
          isActive: .active
          createdOn: .sys_created_on | (strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%dT%H:%M:%SZ"))
          createdBy: .sys_created_by
- kind: incident
  selector:
    query: 'true'
    apiQueryParams:
      sysparmDisplayValue: 'true'
      sysparmExcludeReferenceLink: 'false'
  port:
    entity:
      mappings:
        identifier: .number | tostring
        title: .short_description
        blueprint: '"servicenowIncident"'
        properties:
          category: .category
          reopenCount: .reopen_count
          severity: .severity
          assignedTo: .assigned_to.link
          urgency: .urgency
          contactType: .contact_type
          createdOn: .sys_created_on | (strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%dT%H:%M:%SZ"))
          createdBy: .sys_created_by
          isActive: .active
          priority: .priority
  - kind: release_project
    selector:
      query: 'true'
      apiQueryParams:
        sysparmDisplayValue: 'true'
        sysparmExcludeReferenceLink: 'false'
        sysparmFields: 'sys_id,number,name,type,workflow_state,description,planned_start_date,planned_end_date,priority,risk,sys_created_on,sys_created_by,sys_updated_on,sys_updated_by,active'
    port:
      entity:
        mappings:
          identifier: .sys_id
          title: (.name // .number // "Release")
          blueprint: '"servicenowRelease"'
          properties:
            number: .number
            name: .name
            type: .type
            workflowState: .workflow_state
            description: .description
            priority: .priority
            risk: .risk
            plannedStartDate: .planned_start_date
            plannedEndDate: .planned_end_date
            createdOn: '.sys_created_on | (strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%dT%H:%M:%SZ"))'
            createdBy: .sys_created_by
            updatedOn: '.sys_updated_on | (strptime("%Y-%m-%d %H:%M:%S") | strftime("%Y-%m-%dT%H:%M:%SZ"))'
            updatedBy: .sys_updated_by
            isActive: .active
```

## Mapping & examples per resource[â](#mapping--examples-per-resource "Direct link to Mapping & examples per resource")

GroupService CatalogIncidentRelease ManagementVulnerability

Default mappingYAML

Sample payloadJSON

Port entityJSON

## Filter ServiceNow resources[â](#filter-servicenow-resources "Direct link to Filter ServiceNow resources")

Port's ServiceNow integration provides an option to filter the data that is retrieved from the ServiceNow Table API using the following attributes:

1. `sysparmDisplayValue`: Determines the type of data returned, either the actual values from the database or the display values of the fields. The default is `true`

2. `sysparmFields`: Comma-separated list of fields to return in the response

3. `sysparmExcludeReferenceLink`: Flag that indicates whether to exclude Table API links for reference fields. The default is `false`

4. `sysparmQuery`: Encoded query used to filter the result set. The syntax is `<col_name><operator><value>`:

   1. `<col_name>`: Name of the table column to filter against
   2. `<operator>`: =, !=, ^, ^OR, LIKE, STARTSWITH, ENDSWITH, `ORDERBY<col_name>`, `ORDERBYDESC<col_name>`
   3. `<value>`: Value to match against

   Queries can be chained using ^ or ^OR for AND/OR logic. An example query could be this: `active=true^nameLIKEdev^urgency=3` which returns all active incidents with an urgency level of 3 and have a name like `dev`

The filtering attributes described above can be enabled using the `selector.apiQueryParams` path, for example:

```
- kind: <name of table>
  selector:
    query: "true"
    apiQueryParams:
      sysparmDisplayValue: 'true'
      sysparmExcludeReferenceLink: 'false'
      sysparmQuery: active=true^nameLIKEdev^urgency=3
      sysparmFields: sys_id,priority,created_by,state,active
```

## Monitoring and sync status[â](#monitoring-and-sync-status "Direct link to Monitoring and sync status")

To learn more about how to monitor and check the sync status of your integration, see the [relevant documentation](/build-your-software-catalog/sync-data-to-catalog/.md#monitoring-and-sync-status).

## Relevant Guides[â](#relevant-guides "Direct link to Relevant Guides")

For relevant guides and examples, see the [guides section](https://docs.port.io/guides?tags=ServiceNow).
