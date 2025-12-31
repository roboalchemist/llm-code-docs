# Source: https://docs.replit.com/replitai/warehouse-connectors.md

# Warehouse Connectors

> Connect Replit Agent to BigQuery, Databricks, and Snowflake to build data-driven applications.

Warehouse Connectors allow Replit Agent to securely access and query your organization's data warehouses. This Enterprise-only feature enables builders to create powerful, data-driven applications using natural language, with centralized admin control and role-based access.

## Supported warehouses

Replit supports connections to:

* **BigQuery**
* **Databricks**
* **Snowflake**

These connectors allow Agent to write and execute SQL queries against your data. You can build internal dashboards, data visualization tools, reporting systems, and applications that integrate directly with your warehouse data.

## Admin setup

Administrators must configure warehouse connectors before team members can use them. The setup process involves configuring an OAuth application in your warehouse provider and adding those credentials to Replit.

### Prerequisites

* Enterprise plan
* Admin access to your Replit organization
* Ability to create OAuth applications in your warehouse provider (or access to credentials from your IT/Data team)

### Configuration steps

<Steps>
  <Step title="Navigate to Integrations">
    Go to your organization's settings and select the **Integrations** tab.
  </Step>

  <Step title="Enable Connector">
    Select the warehouse you want to connect (BigQuery, Databricks, or Snowflake).
  </Step>

  <Step title="Enter Credentials">
    Provide the **Client ID** and **Client Secret** for the OAuth application you created in your warehouse provider.
  </Step>

  <Step title="Configure Access">
    Use Role-Based Access Control (RBAC) to specify which members or groups can use this connector.
  </Step>
</Steps>

### Warehouse-specific configuration

<AccordionGroup>
  <Accordion title="Databricks">
    Admins can configure Databricks connections using one of two methods: **User-OAuth** or **Service Account**.

    **Option 1: User-OAuth**

    This method involves minting OAuth application tokens within Databricks.

    <Warning>
      With User-OAuth, the credentials of the user who authenticates the connection are used for all subsequent access. This means that anyone using an application created with this connection will effectively have the same permissions as the authenticating user. Ensure the authenticating user has the appropriate scope of access intended for all application users.
    </Warning>

    **Option 2: Service Account**

    This method involves creating a service account (Service Principal) in Databricks to connect to Replit.

    The service account is shared among everyone given permission to use that integration. The permissions granted to the service account in Databricks will flow to all users enabled for the integration. Scope service accounts to READ-only access on the data when possible.

    **Managing Access Granularity**

    To differentiate access levels (for example, restricting specific tables to different teams):

    1. Create multiple Service Principals in Databricks
    2. Assign specific permissions to each Service Principal
    3. Create separate integrations in Replit for each Service Principal
    4. Open access to each integration only for the allowed individuals or groups
  </Accordion>
</AccordionGroup>

## Builder access and login

Once an admin has enabled a connector and granted you access, you can connect to the warehouse.

### Connecting to a warehouse

When you ask Agent to use a warehouse (for example, "Query the Snowflake database..."), or when you manually add the integration, you receive a login prompt.

Each warehouse requires specific information during the login or connection process:

<AccordionGroup>
  <Accordion title="BigQuery">
    **Required at login:**

    * **Project ID**: You must specify the Google Cloud Project ID you want to access.
  </Accordion>

  <Accordion title="Databricks">
    **Required information:**

    * **SQL Warehouse**: The specific SQL Warehouse compute resource to use.
    * **Account URL**: Your Databricks account URL.
  </Accordion>

  <Accordion title="Snowflake">
    **Required information:**

    * **Account ID**: Your Snowflake Account ID.
  </Accordion>
</AccordionGroup>

### Building with warehouse data

After connecting, you can ask Agent to build applications that use your data. Agent can:

* Build internal tools that fetch and display live data
* Create dashboards with charts and visualizations backed by your warehouse
* Generate SQL queries to power your application's backend
* Explain schema and table structures to help you understand what to build

<Note>
  While Agent can answer ad-hoc questions about your data, the primary purpose of Warehouse Connectors is to enable Agent to build functional applications that leverage your organization's data. Warehouse queries are executed directly against your instance, so make sure your OAuth scopes and database user permissions allow the necessary read and write operations.
</Note>

## Related documentation

* [Connectors overview](/replitai/integrations) — Learn about all integration types
* [Connectors for Organizations](/replitai/connectors-for-organizations) — Centralized connector management for Teams and Enterprise


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.replit.com/llms.txt