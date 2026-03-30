# Source: https://docs.api7.ai/enterprise/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/developers.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/developers.md

# Developers

An API portal is like a bustling marketplace, and *Developers* are its most important customers. They are the builders, the innovators, and the driving force behind the success of your APIs. These technically skilled individuals come to your API portal seeking the digital tools and resources they need to create amazing applications, integrate systems, and solve real-world problems.

## Overview[â](#overview "Direct link to Overview")

Developers are end users of your API portal. They have the capability to:

* **Discover APIs:** Explore your API catalog and find the functionalities they need.
* **Learn and Experiment:** Access documentation, tutorials, and code samples to understand how to use your APIs.
* **Try out APIs:** Use interactive tools like API consoles or sandboxes to test APIs before integrating them.
* **Subscribe to API Products:** Gain access to the specific set of APIs they require for their projects.
* **Manage their usage:** Monitor their API consumption, track their subscriptions, and manage their API keys.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Internal Developers[â](#internal-developers "Direct link to Internal Developers")

For internal use cases, leverage employee accounts for secure and convenient access to the API Portal via Single Sign-On (SSO). This approach simplifies user management as developers and providers can utilize their existing employee credentials.

### Partner Developers[â](#partner-developers "Direct link to Partner Developers")

For partner users, authentication can be achieved through either SSO or email registration.

### Public Developers[â](#public-developers "Direct link to Public Developers")

For public API Portals, anonymous users can view the API Hub and documentation pages. User registration via email requires administrative approval.

## Developers vs Consumers[â](#developers-vs-consumers "Direct link to Developers vs Consumers")

[Consumers](https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md) can also manage API credentials and utilize access control through plugins, but they are typically used in different scenarios compared to developers.

|             | Developers                                               | Consumers            |
| ----------- | -------------------------------------------------------- | -------------------- |
| Credentials | Managed by developers themselves, invisible to providers | Managed by providers |
| Credentials | Managed by developers themselves, invisible to providers | Managed by providers |

Developers and consumers can be used concurrently for different APIs, operating independently. However, for a given published service and its associated API Product, either API7 Gateway authentication plugins or API Product authentication configurations should be used.

For private services, restrict access through consumer management within API7 Gateway. For public services, group them into well-defined API Products and manage developer access through API Product configurations.

Combining both API7 Gateway authentication plugins and API Product authentication configurations for the same published service is strongly not recommended (only for very special cases). This can lead to authentication conflicts, requiring multiple credentials for successful API requests.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [API Products](https://docs.api7.ai/enterprise/3.3.x/key-concepts/api-products.md)
* API Portal
  <!-- -->
  * [Support Developer SSO](https://docs.api7.ai/enterprise/3.3.x/api-portal/developer-sso.md)
