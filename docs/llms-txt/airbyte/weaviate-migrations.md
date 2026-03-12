# Source: https://docs.airbyte.com/integrations/destinations/weaviate-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-weaviate/latest/icon.svg)

# Weaviate Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.60](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-weaviate)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-weaviate)(last updated 5 months ago)

* CDK Version

  [0.81.6](https://pypi.org/project/airbyte-cdk/0.81.6/)

* Sync Success Rate

* Usage Rate

* Definition ID

  `7b7d7a0d-954c-45a0-bcfc-39a634b97736`

## Upgrading to 0.2.0[​](#upgrading-to-020 "Direct link to Upgrading to 0.2.0")

This version adds several new features like flexible embedding options, overwrite and append+dedup sync modes. When upgrading from prior versions on this connector, a one-time migration of existing connections is required. This is done to align the behavior of vector database destinations in Airbyte. The following changes are included:

### Changed configuration object structure[​](#changed-configuration-object-structure "Direct link to Changed configuration object structure")

Due to a change of the configuration structure, it's necessary to reconfigure existing destinations with the same information (e.g. credentials).

### Auto-generated ids[​](#auto-generated-ids "Direct link to Auto-generated ids")

It's no longer possible to configure `id` fields in the destination. Instead, the destination will generate a UUID for each Weaviate object. The `id` for each record is stored in the `_ab_record_id` property and can be used to identify Weaviate objects by Airbyte record.

### Vector fields[​](#vector-fields "Direct link to Vector fields")

It's not possible anymore to configure separate vector fields per stream. To load embedding vectors from the records itself, the embedding method `From Field` can be used and configured with a single field name that has to be available in records from all streams. If your records contain multiple vector fields, you need to configure separate destinations and connections to configure separate vector field names.
