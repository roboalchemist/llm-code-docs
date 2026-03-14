# Source: https://docs.airbyte.com/integrations/sources/amazon-sqs-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-amazon-sqs/latest/icon.svg)

# Amazon SQS Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.0.15](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-sqs)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-amazon-sqs)(last updated 10 months ago)

* CDK Version

  [6.48.10](https://pypi.org/project/airbyte-cdk/6.48.10/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `983fd355-6bf3-4709-91b5-37afa391eeb6`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

The verison migrates the Amazon SQS connector to the low-code framework for greater maintainability.

Changes regarding configuration of specs:

* `access_key`, `secret_key`, `queue_url`, `region`, `target` are required for this connector to work
* Other specification parameters has default values which could be changed by user
* `Delete messages after read` is no longer supported as it is removed from the supported attributes of API request, Supported attributes reference - <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html>

New features:

* Support for builder with latest version updates
* Support for new action stream - GetQueueAttributes
* Users could experiments new action streams using the builder with local setup
