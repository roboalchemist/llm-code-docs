# Source: https://docs.airbyte.com/ai-agents/api/api-reference/agent-engine-api.md

Version: 0.9.0

# Agent Engine API

![](https://cdn.prod.website-files.com/605e01bc25f7e19a82e74788/6335a39da8c96ba75520b156_Logo.svg)![](https://cdn.prod.website-files.com/605e01bc25f7e19a82e74788/6335a39da8c96ba75520b156_Logo.svg)

This is the public API documentation for Airbyte's Agent Engine. Use the API to manage authentication, connectors, and customers, and power their agentic workflows.

If you are a member of multiple Agent Engine organizations, add the `X-Organization-Id: organization's UUID` header to your requests. It specifies which organization you are making requests to. If you only belong to one organization, you don't need to set this header.

The API contains several types of endpoints.

* Authentication: Generate tokens to make other API requests.
* Connectors: Create and manage end-user connectors, and execute operations with connectors.
* Customers: manage customer workspaces and retrieve workspace statistics.
* Data replication: configure connection templates and destination definitions for data replication use cases.

Some endpoints are separated into Advanced categories. These endpoints are more specialized and should not be required for day-to-day use of the API.

## Authentication[​](#authentication "Direct link to Authentication")

* HTTP: Bearer Auth

| Security Scheme Type:      | http   |
| -------------------------- | ------ |
| HTTP Authorization Scheme: | bearer |
