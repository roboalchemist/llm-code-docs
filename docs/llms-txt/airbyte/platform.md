# Source: https://docs.airbyte.com/platform.md

# Source: https://docs.airbyte.com/ai-agents/platform.md

# Agent engine platform

Copy Page

The Agent Engine has two main components: the platform and [connectors](/ai-agents/connectors/.md). The platform is the subscription-based, cloud component that manages credentials and data replication.

## Log in and sign up[​](#log-in-and-sign-up "Direct link to Log in and sign up")

Log in and sign up to the Agent Engine at [app.airbyte.ai/](https://app.airbyte.ai/).

## Use the platform[​](#use-the-platform "Direct link to Use the platform")

<!-- -->

## [📄️<!-- --> <!-- -->Enable a connector](/ai-agents/platform/enable-connector.md)

[Before your AI agents can interact with external data sources, you need to enable connectors in the Agent Engine. Enabling a connector makes it available for your end users to authenticate and use with their own credentials.](/ai-agents/platform/enable-connector.md)

## [🗃️<!-- --> <!-- -->Authenticate](/ai-agents/platform/authenticate/.md)

[3 items](/ai-agents/platform/authenticate/.md)

## [📄️<!-- --> <!-- -->Execute operations](/ai-agents/platform/execute.md)

[You can execute operations using either the Python SDK or the Agent Engine API.](/ai-agents/platform/execute.md)

## [📄️<!-- --> <!-- -->Manage customers](/ai-agents/platform/customers.md)

[In Agent Engine, a customer represents an end-user of your service who connects their own data sources. Each customer gets an isolated environment that stores their credentials, connectors, and data separately from other customers. You may occasionally see the terms workspace or external\_customer in the Agent Engine API. These terms are essentially interchangeable. All of them map to a customer.](/ai-agents/platform/customers.md)

## [📄️<!-- --> <!-- -->Context store](/ai-agents/platform/context-store.md)

[Some APIs have search endpoints, but many don't. This makes search operations resource-intensive. Imagine prompts like these:](/ai-agents/platform/context-store.md)
