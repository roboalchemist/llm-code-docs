# Source: https://docs.replit.com/replitai/connectors-for-organizations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors for Organizations

> Centralize and manage app connectors across Teams and Enterprise Workspaces with admin controls, scoped permissions, and audit tracking.

Connectors for Organizations bring centralized, admin-managed connections to Teams and Enterprise Workspaces. Admins set up and manage connections once, then make them available to apps across the organization. This removes repetitive setup for builders, improves security for IT, and standardizes access to tools like Notion, GitHub, Google, Outlook, Dropbox, Salesforce, and more.

## Key capabilities

* **Centralized management**: Admin setup and approval for organization-wide connections
* **Role-based access controls**: Enforce scoped, least-privilege permissions
* **Visibility and audit tracking**: Track which apps use which services
* **Bring your own OAuth** (Enterprise only): Use organization-owned OAuth clients with custom scopes
* **Per-app consent and easy revocation**

## How it works

<Steps>
  <Step title="Admin sets up a service">
    Admin sets up a service once using organization credentials.
  </Step>

  <Step title="Admin approves access">
    Admin approves which groups can use the connector.
  </Step>

  <Step title="Builders use the connector">
    Members build with that service by asking Agent.
  </Step>

  <Step title="Admin monitors usage">
    Admins can monitor which members and apps use which services.
  </Step>
</Steps>

## Security and governance

* Scoped access with least-privilege permissions
* Credentials and tokens managed by the platform, not individual apps
* Centralized revocation and rotation without code changes

## Setup and management

### Enable new connectors

<Steps>
  <Step title="Navigate to Integrations">
    Navigate to the **Integrations** page from your organization's home page.
  </Step>

  <Step title="Enable new connector">
    Select **Enable new connector** in the top right.
  </Step>

  <Step title="Select the service">
    Select the service you want to enable for your organization.
  </Step>

  <Step title="Configure the connector">
    Enable the connector using default configuration, or (Enterprise only) create an OAuth connector using custom configuration (for example, Drive scopes `.../auth/drive.file`, `.../auth/drive.install`).
  </Step>

  <Step title="Submit">
    Select **Submit**.
  </Step>
</Steps>

### Configure RBAC

1. After enabling a connector, select **Manage**
2. Grant access to a specific group

### Modify connectors

* After enabling a connector, select **Manage**
* Deleting a connector removes connections for all builders in the organization
* Edit the scopes of a custom connector as needed

## Plan controls

| Feature                         | Teams | Enterprise |
| ------------------------------- | ----- | ---------- |
| Enable organization connectors  | ✓     | ✓          |
| Create custom OAuth clients     | —     | ✓          |
| Set access controls on API keys | —     | ✓          |

<Note>
  On Teams, API keys are available to all Members and Admins. Enterprise plans support access controls for API keys.
</Note>

## What's next

Connectors for Organizations is expanding to support:

* Webhook events for event-driven workflows
* Deeper admin experience with permissions, assignments, and analytics

## Related documentation

* [Connectors overview](/replitai/integrations) — Learn about all integration types
* [Warehouse Connectors](/replitai/warehouse-connectors) — Connect to BigQuery, Databricks, and Snowflake
