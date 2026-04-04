# Source: https://docs.snowflake.com/en/sql-reference/sql/create-notification-integration.md

# CREATE NOTIFICATION INTEGRATION

Creates a new notification integration in the account or replaces an existing integration. A notification integration is a
Snowflake object that provides an interface between Snowflake and third-party messaging services (third-party cloud message
queuing services, email services, webhooks, etc.).

The syntax of the command depends on the type of the messaging service and whether the message is inbound or outbound. The
following topics explain the syntax for creating notification integrations for different use cases:

* [CREATE NOTIFICATION INTEGRATION (inbound from an Azure Event Grid topic)](create-notification-integration-queue-inbound-azure.md)
* [CREATE NOTIFICATION INTEGRATION (inbound from a Google Pub/Sub topic)](create-notification-integration-queue-inbound-gcp.md)
* [CREATE NOTIFICATION INTEGRATION (outbound to an Amazon SNS topic)](create-notification-integration-queue-outbound-aws.md)
* [CREATE NOTIFICATION INTEGRATION (outbound to an Azure Event Grid topic)](create-notification-integration-queue-outbound-azure.md)
* [CREATE NOTIFICATION INTEGRATION (outbound to a Google Pub/Sub topic)](create-notification-integration-queue-outbound-gcp.md)
* [CREATE NOTIFICATION INTEGRATION (email)](create-notification-integration-email.md)
* [CREATE NOTIFICATION INTEGRATION (webhooks)](create-notification-integration-webhooks.md)

See also:
:   [ALTER NOTIFICATION INTEGRATION](alter-notification-integration.md) , [DESCRIBE INTEGRATION](desc-integration.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)
