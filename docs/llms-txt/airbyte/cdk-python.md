# Source: https://docs.airbyte.com/platform/connector-development/cdk-python.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/cdk-python.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/cdk-python.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/cdk-python.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/cdk-python.md

# Connector Development Kit

Copy Page

info

This section is for the Python CDK. See our [community-maintained CDKs section](/platform/1.6/connector-development/.md#community-maintained-cdks) if you want to write connectors in other languages.

The Airbyte Python CDK is a framework for rapidly developing production-grade Airbyte connectors. The CDK currently offers helpers specific for creating Airbyte source connectors for:

* HTTP APIs (REST APIs, GraphQL, etc..)
* Generic Python sources (anything not covered by the above)

This document is a general introduction to the CDK. Readers should have basic familiarity with the [Airbyte Specification](https://docs.airbyte.com/understanding-airbyte/airbyte-protocol/) before proceeding.

If you have any issues with troubleshooting or want to learn more about the CDK from the Airbyte team, head to [the Connector Development section of our Airbyte Forum](https://github.com/airbytehq/airbyte/discussions) to inquire further!

## Getting Started[​](#getting-started "Direct link to Getting Started")

In most cases, you won't need to use the CDK directly, and should start building connectors in Connector Builder, an IDE that is powerd by Airbyte Python CDK. If you do need customization beyond what it offers, you can do so by using `airbyte_cdk` as aa dependency in your Python project.

[Airbyte CDK reference documentation](https://airbytehq.github.io/airbyte-python-cdk/airbyte_cdk.html) is published automatically with each new CDK release. The rest of this document explains the most basic concepts applicable to any Airbyte API connector.

### Concepts & Documentation[​](#concepts--documentation "Direct link to Concepts & Documentation")

#### Basic Concepts[​](#basic-concepts "Direct link to Basic Concepts")

If you want to learn more about the classes required to implement an Airbyte Source, head to our [basic concepts doc](/platform/1.6/connector-development/cdk-python/basic-concepts.md).

#### Full Refresh Streams[​](#full-refresh-streams "Direct link to Full Refresh Streams")

If you have questions or are running into issues creating your first full refresh stream, head over to our [full refresh stream doc](/platform/1.6/connector-development/cdk-python/full-refresh-stream.md). If you have questions about implementing a `path` or `parse_response` function, this doc is for you.

#### Incremental Streams[​](#incremental-streams "Direct link to Incremental Streams")

Having trouble figuring out how to write a `stream_slices` function or aren't sure what a `cursor_field` is? Head to our [incremental stream doc](/platform/1.6/connector-development/cdk-python/incremental-stream.md).

#### Practical Tips[​](#practical-tips "Direct link to Practical Tips")

You can find a complete tutorial for implementing an HTTP source connector in [this tutorial](/platform/1.6/connector-development/tutorials/custom-python-connector/getting-started.md)

## Contributing[​](#contributing "Direct link to Contributing")

We're welcoming all contributions to Airbyte Python CDK! [`airbytehq/airbyte-python-cdk` Github repository](https://github.com/airbytehq/airbyte-python-cdk) CONTRIBUTING.md is the best spot to see up to date guide on how to get started.
