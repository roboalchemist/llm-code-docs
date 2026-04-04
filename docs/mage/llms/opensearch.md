# Source: https://docs.mage.ai/guides/streaming/destinations/opensearch.md

# Source: https://docs.mage.ai/data-integrations/destinations/opensearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenSearch

> How to configure OpenSearch as a destination in Mage to stream pipeline data into OpenSearch indices using JSON records with support for authentication, ECS metadata, and SSL.

## Overview

Use **OpenSearch** as a destination in Mage to publish JSON-formatted records into an OpenSearch index. This is ideal for search indexing, log aggregation, and real-time analytics.

By default, Mage uses the pipeline’s `table` name to set the OpenSearch **index name**. You can also define dynamic index patterns using JSONPath expressions.

***

## Configuration Parameters

| Key                   | Description                                                                                                                                     | Default     | Required |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `scheme`              | HTTP scheme used for connecting to OpenSearch. Use `http` or `https`.                                                                           | `http`      | ✅        |
| `host`                | Hostname or IP address of the OpenSearch node or cluster.                                                                                       | `localhost` | ✅        |
| `port`                | Port number for the OpenSearch HTTP endpoint.                                                                                                   | `9200`      | ✅        |
| `username`            | *(Optional)* Username for basic authentication.                                                                                                 | `None`      | ❌        |
| `password`            | *(Optional)* Password for basic authentication.                                                                                                 | `None`      | ❌        |
| `bearer_token`        | *(Optional)* Bearer token for token-based authentication.                                                                                       | `None`      | ❌        |
| `api_key_id`          | *(Optional)* API key ID for key-based authorization.                                                                                            | `None`      | ❌        |
| `api_key`             | *(Optional)* API key secret for key-based authorization.                                                                                        | `None`      | ❌        |
| `ssl_ca_file`         | *(Optional)* Path to the SSL CA certificate file for verifying HTTPS connections.                                                               | `None`      | ❌        |
| `index_schema_fields` | *(Optional)* JSONPath mapping used to dynamically generate the index name based on record values.                                               | `None`      | ❌        |
| `metadata_fields`     | *(Optional)* Dictionary mapping fields (using JSONPath) to populate ECS-style metadata fields in the index request (e.g., `_id`, `@timestamp`). | `None`      | ❌        |

***

## Notes

* Mage automatically converts each record into JSON format and indexes it into the specified OpenSearch index.
* If `index_schema_fields` is configured, Mage will use the JSONPath-extracted values from each record to generate dynamic index names.
* `metadata_fields` is useful for setting OpenSearch ECS-compatible fields like `_id`, `@timestamp`, etc., from the incoming data stream.
* Authentication can be configured using **basic auth**, **bearer tokens**, or **API key pairs**.
* For production use, we recommend enabling `https` and providing a trusted `ssl_ca_file`.

***

## Related Resources

* [OpenSearch Documentation](https://opensearch.org/docs/)
* [OpenSearch Python Client](https://opensearch-project.github.io/opensearch-py/)
* [ECS (Elastic Common Schema) Fields](https://www.elastic.co/guide/en/ecs/current/ecs-field-reference.html)
* [OpenSearch Security Configuration](https://opensearch.org/docs/latest/security-plugin/)


Built with [Mintlify](https://mintlify.com).