# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods.md

# Connection Methods

OX supports multiple connection methods so you can connect source control systems, cloud platforms, and security tools using an approach that matches your deployment model, security posture, and permission requirements.\
Each method represents a common integration pattern used across OX connectors.

## How to choose a connection method

Select a connection method based on where your systems are hosted, how access is managed in your organization, and whether your environment allows inbound connectivity.

SaaS environments typically use App, Identity Provider, or Token connections.\
On-prem or restricted environments require OX Broker.

OX supports several connection methods that follow common integration patterns across connectors. Each method differs in how authentication is handled, how permissions are managed, and how connectivity is established.

### App

The App method is the most **straightforward and easy to apply**. It uses a standard OAuth-based installation flow that can be completed with minimal configuration.

During setup, permissions are requested and scoped automatically, lowering configuration overhead and reducing the steps you need to take. Because the integration is managed and permissions are granted through a guided install process, this method is ideal for quick onboarding.

### Identity Provider

The Identity Provider method relies on an external authentication system such as SSO, allowing users to authenticate through a centralized identity service instead of managing tokens directly.

This method removes the need for API token handling while providing federated access using established identity standards. It’s simple in terms of credential management and works well if you already use an identity provider for access control.

### Token

The Token method uses direct API credentials to create the connection. Tokens can be scoped with **granular permissions**, letting you control exactly what resources OX can access.

This pattern is common when an organization requires fine-tuned access restrictions or must comply with strict security policies. Unlike managed App integrations that abstract permission details, this method makes permissions explicit and configurable.

### OX Broker

OX Broker is a secure, containerized service that runs in your environment and enables communication between internal resources and OX services. Instead of requiring inbound access from the internet, the broker initiates a secure outbound connection to OX.

This reverses the traditional connectivity model, removing the need for open inbound ports or whitelisted IPs. It’s particularly useful for restricted or on-premises environments where network security or internal access constraints are high.

## Connection methods comparison

| Method            | Deployment model     | Primary use                | Token management       | Permission control     | Network model | Recommended when                      |
| ----------------- | -------------------- | -------------------------- | ---------------------- | ---------------------- | ------------- | ------------------------------------- |
| App               | SaaS                 | Managed integration        | Not required           | Limited                | Outbound      | Fast setup is preferred               |
| Identity Provider | SaaS                 | Centralized authentication | Not required           | Limited                | Outbound      | Central identity is in place          |
| Token             | SaaS                 | Direct API access          | Required               | Full                   | Outbound      | Fine-grained permissions are required |
| OX Broker         | On-Prem / Restricted | Internal system access     | Depends on integration | Depends on integration | Outbound-only | Inbound connectivity is restricted    |

### Notes

* Not all connectors support all connection methods.
* Available methods are listed on each connector’s setup page.
* Some connectors support multiple methods to address different deployment scenarios.
