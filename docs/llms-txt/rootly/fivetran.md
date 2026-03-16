# Source: https://docs.rootly.com/integrations/fivetran.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fivetran

> Connect Rootly with Fivetran to automatically sync incident data to your data warehouse for advanced analytics and reporting.

Fivetran is a no-code data movement platform that allows you to automatically transform data and then send it to your data warehouse.

Rootly provides plenty of built-in, customizable metrics right in the web platform, but if you want to dive even deeper into the data, the Fivetran integration will pull your Rootly data right into your centralized data location.

### Use Cases

With Rootly data synced to your data warehouse, you can:

* Build custom dashboards and visualizations in your BI tool of choice
* Analyze incident trends over time and identify patterns
* Combine Rootly incident data with other business metrics
* Create executive reports on MTTR, incident frequency, and team performance
* Perform advanced analytics and forecasting on incident data

### Synced Data Tables

Fivetran syncs these data tables from Rootly:

* **Audit** - Audit logs and history
* **Cause** - Incident root causes
* **Form fields** - Custom form field data
* **Incidents** - Core incident information
* **Roles** - User roles and assignments
* **Workflows** - Workflow definitions and runs

### Requirements

* Fivetran account with a configured destination (data warehouse)
* Rootly admin or owner access (required to generate API keys)

### Installation

To set up the integration:

1. Ensure you have a destination configured in Fivetran (e.g., Snowflake, BigQuery, Redshift)
2. Generate a Rootly API key from **Organization Settings > API Keys**
3. In Fivetran, create a new Rootly connector
4. Enter your destination schema name and Rootly API key
5. Click **Save & Test** to begin syncing

Fivetran will perform an initial sync and then sync data on a regular schedule according to your connector settings.

### Additional Resources

* [Fivetran's Rootly setup guide](https://fivetran.com/docs/connectors/applications/rootly/setup-guide) - Detailed configuration instructions
* [Fivetran's Rootly API configuration](https://fivetran.com/docs/connectors/applications/rootly/api-configuration) - API setup details
* [Rootly connector ERD](https://fivetran.com/connector-erd/rootly) - Database schema and relationships

### Notes

* Sync frequency is managed by Fivetran and depends on your Fivetran plan
* Historical data will be synced during the initial connector setup
* Ensure your data warehouse has sufficient storage for the synced data


Built with [Mintlify](https://mintlify.com).