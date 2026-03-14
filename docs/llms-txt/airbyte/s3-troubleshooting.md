# Source: https://docs.airbyte.com/integrations/destinations/s3/s3-troubleshooting.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-s3/latest/icon.svg)

# Troubleshooting S3 Destinations

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.9.7](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-s3)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-s3)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `4816b78f-1489-44c1-9060-4b19d5fa9362`

## Connector Limitations[​](#connector-limitations "Direct link to Connector Limitations")

### Encryption at rest[​](#encryption-at-rest "Direct link to Encryption at rest")

[Server-Side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html) using S3 managed keys should work out of the box. We DO NOT support using [customer keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) or KMS.

### Vendor-Specific Connector Limitations[​](#vendor-specific-connector-limitations "Direct link to Vendor-Specific Connector Limitations")

warning

Not all implementations or deployments an "S3-compatible destinations" will be the same. This section lists specific limitations and known issues with the connector based on *how* or *where* it is deployed.

#### Linode Object Storage[​](#linode-object-storage "Direct link to Linode Object Storage")

Liniode Object Storage does not properly return etags after setting them, which Airbyte relies on to verify the integrity of the data. This makes this destination currently incompatible with Airbyte.
