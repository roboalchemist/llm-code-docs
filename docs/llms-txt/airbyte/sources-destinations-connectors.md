# Source: https://docs.airbyte.com/platform/move-data/sources-destinations-connectors.md

# Source: https://docs.airbyte.com/platform/2.0/move-data/sources-destinations-connectors.md

# Source: https://docs.airbyte.com/platform/1.8/move-data/sources-destinations-connectors.md

# Sources, destinations, and connectors

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

In Airbyte, you move data from **sources** to **destinations** using **connectors**.

## Sources and destinations[​](#sources-and-destinations "Direct link to Sources and destinations")

A **source** is the database, API, or other system **from** which you sync data. A **destination** is the data warehouse, data lake, database, or other system **to** which you sync data.

## Connectors[​](#connectors "Direct link to Connectors")

A **connector** is the component Airbyte uses to connect to and interact with your source or destination. Connectors are a key difference between a resilient Airbyte deployment and a more brittle in-house data pipeline.

Airbyte has two types of connectors: source connectors and destination connectors. Sometimes, people abbreviate these to "sources" and "destinations." That can be a little confusing, so to be clear, a connector isn't the same thing as the source or destination it connects to, but it's closely related to them.

Connectors have [different support levels](/integrations/connector-support-levels.md). Some are built and maintained by Airbyte and some are contributed by members of Airbyte's community.

### Connectors are open source[​](#connectors-are-open-source "Direct link to Connectors are open source")

Airbyte provides over 600 connectors, almost all of which are open source. You can contribute to connectors to make them better or keep them up-to-date as third-parties make changes, or fork it to make it more suitable to your particular needs.

If you don't see the connector you need, you can build one from scratch. Airbyte provides a no-code and low-code [Connector Builder](/platform/1.8/connector-development/connector-builder-ui/overview.md). For advanced use cases, you can use Connector Development Kits (CDKs), which are more traditional software development tools.

## Add and manage sources and destinations[​](#add-and-manage-sources-and-destinations "Direct link to Add and manage sources and destinations")

## [📄️<!-- --> <!-- -->Add and manage sources](/platform/1.8/using-airbyte/getting-started/add-a-source.md)

[A source is the database, API, or other system from which you sync data. Adding a source connector is the first step when you want to start syncing data with Airbyte.](/platform/1.8/using-airbyte/getting-started/add-a-source.md)

## [📄️<!-- --> <!-- -->Add and manage destinations](/platform/1.8/using-airbyte/getting-started/add-a-destination.md)

[A destination is the data warehouse, data lake, database, or other system to which you sync data. Adding a destination is the next step after you create a source.](/platform/1.8/using-airbyte/getting-started/add-a-destination.md)

## [📄️<!-- --> <!-- -->Using OAuth to Connect](/platform/1.8/using-airbyte/oauth.md)

[Many Airbyte connectors support OAuth 2.0, enabling secure and seamless integration between Airbyte and third-party APIs. This guide explains how OAuth works for connectors in Airbyte.](/platform/1.8/using-airbyte/oauth.md)

## [📄️<!-- --> <!-- -->Delivery methods](/platform/1.8/using-airbyte/delivery-methods.md)

[Airbyte supports two methods for delivering source data to the destination.](/platform/1.8/using-airbyte/delivery-methods.md)
