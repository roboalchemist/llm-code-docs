# Source: https://docs.api7.ai/enterprise/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/api-products.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/api-products.md

# API Products

Think of an API7 Portal as your digital storefront, showcasing the valuable APIs you offer to developers. Within this storefront, *API Products* act as curated bundles of APIs, tailored to specific needs and use cases. Just as a store might offer different product packages, your API7 portal uses API Products to present your APIs in a way that makes them easy to understand, consume, and manage.

## Overview[â](#overview "Direct link to Overview")

An API Product is essentially a container that holds one or more APIs, and the smallest unit for developers to subscribe to or buy your APIs.

API7 Portal supports two types of API Products:

* **From API7 Gateway (Recommended)**: API Products leverage published services from API7 Gateway, enabling centralized management and simplified delivery to developers. API7 Portal facilitates subscription management and future monetization features for these API Products. Changes made to published services are automatically reflected in the associated API Products on the API7 Portal, ensuring seamless updates for your developers.
* **Import OpenAPI**: Enables developers to explore external API definitions within the API7 Portal. This feature provides a sandbox environment for developers to interact with APIs that are not hosted on API7 Gateway. Advanced features such as authentication, subscription, and monetization are not supported for imported APIs.

## Use Cases[â](#use-cases "Direct link to Use Cases")

* **Simplified Consumption:** Developers can easily discover and subscribe to the required set of APIs without needing to understand the underlying service architecture.
* **Targeted Offerings:** Create different API Products for different audiences or use cases (e.g., a "starter" product with limited access, a "premium" product with higher quotas).
* **Efficient Management:** Apply policies and manage access for a group of APIs as a single unit.
* **Improved Developer Experience:** Present a clear and organized view of your API offerings, making it easier for developers to find what they need and get started quickly.

## Relationship with Published Services[â](#relationship-with-published-services "Direct link to Relationship with Published Services")

An API Product can be composed of multiple published services from API7 Gateway. However, the following limitations apply:

* One-to-one association: A published service can only be associated with a single API Product.
* Gateway Group Restriction: Published services from different gateway groups with the same service template cannot be included within the same API Product.

The published service - API Product relationship promotes clear roles and responsibilities within your development team.

Engineers focus on the technical aspects:

* Designing, developing, and maintaining published services.
* Ensuring the accuracy and quality of OpenAPI specifications.

API Product Managers focus on the business aspects:

* Defining and managing API products according to developer needs.
* Overseeing subscription management and developer engagement.
* Driving overall product strategy.

This separation of concerns allows for more efficient and effective API development and management.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
* API Portal
  <!-- -->
  * [Productize services](https://docs.api7.ai/enterprise/3.3.x/api-portal/productize-services.md)
