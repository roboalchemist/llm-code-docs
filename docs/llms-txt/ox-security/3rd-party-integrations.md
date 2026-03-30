# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations.md

# 3rd Party Integrations

OX integrates with a wide range of third-party systems to collect security signals, enrich findings with contextual data, and reflect how your applications are built, deployed, and operated in practice.

Integrations allow OX to connect to source control systems, CI/CD platforms, cloud providers, container registries, and security tools, and to correlate data across them into a single application-centric security view.

### What integrations enable

By connecting third-party systems to OX, you enable the platform to:

* Discover applications, repositories, and workloads automaticallyIngest findings from multiple security sources
* Enrich issues with build, runtime, and ownership context
* Track risk across the full application lifecycle

Integrations are the foundation for accurate prioritization, policy evaluation, and end-to-end visibility.

### Integration models in OX

OX supports multiple integration models to accommodate different environments and security requirements.

Some integrations connect directly to external SaaS platforms.\
Others connect to internal systems running in private or restricted environments.

The available integration model depends on the system you are connecting and how your environment is deployed.

### Authentication and connectivity

Each integration uses a defined connection method that determines how authentication, permissions, and network access are handled.

Common connection methods include managed App integrations, identity-based authentication, direct API tokens, and broker-based connectivity for restricted environments.

For an overview of available connection methods and guidance on choosing the right one, see [Connection Methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

### Connector-specific configuration

While the integration concepts are consistent, each connector has its own configuration requirements based on the third-party system it connects to.

Connector setup pages describe:

* Supported connection methods
* Required permissions or scopes
* Environment prerequisites
* Connector-specific behavior and limitations

Not all connectors support all connection methods.

### How to get started

Start by identifying which third-party systems are part of your development and deployment workflow.\
Then, choose the appropriate connector and connection method based on your environment and security requirements.
