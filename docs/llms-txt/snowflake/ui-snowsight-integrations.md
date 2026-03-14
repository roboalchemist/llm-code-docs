# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight-integrations.md

# Managing integrations in Snowsight

Snowflake supports a large variety of integrations that allow you to connect to external services and data sources.

This topic provides an overview of the different types of integrations and how to manage them using Snowsight.

Supported integrations include:

* [API integrations](../sql-reference/sql/create-api-integration.md) supporting integrating services reached via HTTPS API, including information about the cloud platform, types of services, access credentials, and more.
* [Catalog integrations](../sql-reference/sql/create-catalog-integration.md) supporting integrating [Apache Iceberg™ tables](tables-iceberg.md).
* [External integrations](../sql-reference/sql/create-external-access-integration.md) to enable access to specific external network locations, including network rules and credentials.
* [Notification integration](../sql-reference/sql/create-notification-integration.md) providing an interface between Snowflake and third-party messaging services.
* [Security integrations](../sql-reference/sql/create-security-integration.md) for external access to services that require authentication and authorization.
* [Storage integration](../sql-reference/sql/create-storage-integration.md) for storing generated identity and access management (IAM) entity for your external cloud storage.

To manage integrations in Snowsight:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Integrations. The list of integrations is displayed.

Then:

* Create a new integration:

  1. Click Create and select the integration type to create.
  2. Complete the associated template to create the integration.
* View, disable/enable, drop, or transfer ownership of an integration:

  1. Select an integration and click …
  2. Select one of Disable, Enable, Drop, or Transfer Ownership.
  3. Confirm the operation or cancel.
* Grant a privileges to select roles for a given integration:

  > **Note:**
  >
  > You must be the owner of an integration to grant privileges on that integration.

  1. Click anywhere in an integration row. The details of the selected integration are displayed.
  2. in the Privileges section, click + Privilege. The Grant new privilege on <integration> dialog box is displayed.
  3. From the ROLES drop down select a role.
  4. From the privileges drop down select either USAGE, USE_ANY_ROLE or both.
  5. Click Grant Privileges to grant the privilege to the selected role or Cancel to cancel the operation.
