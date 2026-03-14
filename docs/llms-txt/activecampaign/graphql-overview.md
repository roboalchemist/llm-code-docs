# Source: https://developers.activecampaign.com/reference/graphql-overview.md

# Overview

The Ecommerce GraphQL API is an iteration upon the existing Deep Data REST API endpoints. While the [v3 DeepData endpoints](https://developers.activecampaign.com/reference/connections) provided a powerful tool to integrate more deeply with the ActiveCampaign platform, they lacked the flexibility necessary to scale to all use cases. The Ecommerce GraphQL API provides the flexibility to request only the specific data necessary which provides an advantage over the REST endpoints.

# Ecommerce GraphQL API and Custom Objects

The Ecommerce GraphQL API saves order, product, and recurring payment data as [ActiveCampaign Custom Objects](https://help.activecampaign.com/hc/en-us/articles/4408415902738-Custom-objects-overview). This allows you to use order and recurring payment data in the segmentation builder, for triggering automations, and in personalization tags. Product data cannot be used for segmentation, automation triggers, or personalization. These custom objects can be accessed via the Custom Object API, but the Ecommerce GraphQL APIs provide an abstraction layer.

Users are not billed for Ecommerce Custom Objects. The schemas for these Custom Objects are managed by ActiveCampaign.

There are a few details around this behavior to be aware of.