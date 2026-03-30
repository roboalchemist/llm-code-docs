# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-notification-integration.md

# ALTER NOTIFICATION INTEGRATION

Modifies the properties for an existing notification integration.

The properties that you can set depend on the type of the messaging service and whether the message is inbound or outbound. The
following topics explain the syntax for altering notification integrations for different use cases:

* [ALTER NOTIFICATION INTEGRATION (inbound from an Azure Event Grid topic)](alter-notification-integration-queue-inbound-azure.md)
* [ALTER NOTIFICATION INTEGRATION (inbound from a Google Pub/Sub topic)](alter-notification-integration-queue-inbound-gcp.md)
* [ALTER NOTIFICATION INTEGRATION (outbound to an Amazon SNS topic)](alter-notification-integration-queue-outbound-aws.md)
* [ALTER NOTIFICATION INTEGRATION (outbound to an Azure Event Grid topic)](alter-notification-integration-queue-outbound-azure.md)
* [ALTER NOTIFICATION INTEGRATION (outbound to a Google Pub/Sub topic)](alter-notification-integration-queue-outbound-gcp.md)
* [ALTER NOTIFICATION INTEGRATION (email)](alter-notification-integration-email.md)
* [ALTER NOTIFICATION INTEGRATION (webhooks)](alter-notification-integration-webhooks.md)

See also:
:   [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md) , [DESCRIBE INTEGRATION](desc-integration.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)
