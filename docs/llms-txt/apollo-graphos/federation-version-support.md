# Source: https://www.apollographql.com/docs/graphos/routing/federation-version-support.md

# Federation Version Support

The GraphOS Router and Apollo Router Core support supergraph schemas that are generated via Apollo Federation 2.x [composition](https://www.apollographql.com/docs/federation/federated-types/composition/). This composition algorithm can be performed by Apollo GraphOS Studio, the Rover CLI, or the Apollo GraphOS Platform API.

Apollo Federation is an evolving project, and its composition algorithm regularly receives new features and bug fixes.

Update your router regularly to the latest stable version to ensure that it fully supports its supergraph schema.

## Checking version compatibility

To ensure your router's federation version is supported, check the [Apollo Federation Changelog](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions). Make sure that your router's federation version is *at least* as recent as the version used to compose your supergraph schema.

## Federation 1 support

Only Apollo Router Core and GraphOS Router v1.59 and earlier support Federation v1.x supergraphs. The following *don't* support Federation v1.x:

* Router v1.60 and later
* Router v2.0 and later

[Learn how to upgrade from Federation version 1 to 2.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/moving-to-federation-2)
