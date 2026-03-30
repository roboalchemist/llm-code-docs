# Source: https://docs.api7.ai/enterprise/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/api-version-control.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md

# API Version Control

Maintaining API functionality after logic changes requires updating configurations on the API gateway. API7 Gateway simplifies this process with robust version control at the service level. You can publish specific service versions with their corresponding configurations to different gateway groups, ensuring consistent deployments and smoother rollbacks.

Strong and forced version control is not required in API7 Gateway. The decision to implement even a basic version control system depends on the specific needs of your organization and the desired level of control over API Gateway configurations.

## Version Control Range[â](#version-control-range "Direct link to Version Control Range")

Unique service version numbers represent consistent business logic.

### Routes/Stream Routes[â](#routesstream-routes "Direct link to Routes/Stream Routes")

Route/Stream route changes in API7 Gateway are tied to the service version. Modifying routes/stream routes within a published service version can potentially cause disruptions for developers who are using those APIs. This is because their existing code might rely on the specific behavior of the previous route configuration.

### Upstream[â](#upstream "Direct link to Upstream")

API7 Gateway relies on upstream configurations to manage connections with its backend applications (e.g., servers and databases). These configurations determine how the gateway interacts with your backend, and they typically vary based on the deployment environment.

For instance, in a development environment, the API Gateway might be configured to connect to applications running on developer machines (e.g., devserver). While in production, it would connect to the actual backend servers deployed in datacenters.

However, it is important to note that upstream configurations themselves are independent of the core logic your API implements. They focus on the "how" of communication, while your API code focuses on the "what" - the specific functionality it provides.

Even with the same API version, different gateway groups can point to different backend servers through upstream configurations. Developers using these APIs remain unaffected. Their code calls to the API will function identically regardless of the underlying backend configuration.

In general, upstream configurations in API7 Enterprise offer flexibility as "runtime configurations." They are independent of versioning, allowing you to modify them at any time without publishing new versions.

### Host, Path Prefix[â](#host-path-prefix "Direct link to Host, Path Prefix")

Host and Path Prefix are configuration elements within API7 Gateway that manage how clients access your API. They are independent of the core logic your API implements, focusing on the "where" and "how" of API calls.

The Host and Path Prefix can vary based on your deployment environment (development, staging, production) to provide appropriate access points for each stage. Changing the Host or Path Prefix typically requires developers to update their code to reflect the new access details. However, compared to modifying core API logic, this update usually involves replacing the host address or path prefix in their code rather than a complete rewrite. This minimizes disruption for developers when managing environment-specific configurations.

For example:

* The API URL in the `test` environment is <https://api7-test.ai/v1/pet>, while the endpoint address is 127.0.0.1:80.
* The API URL in the `production` environment is <https://api7.ai/petstore/pet>, while the endpoint address is 192.168.0.1:80.

In general, host and path prefixes in API7 Gateway offer flexibility as "runtime configurations." They are independent of versioning, allowing you to modify them at any time without publishing new versions.

## Key Features[â](#key-features "Direct link to Key Features")

1. Service Change Tracking: Maintain a Clear History

The service version logs every modification made to your services, including details like the specific changes made, who made them, and the exact time of the change. This detailed history provides several advantages. It allows for faster debugging by enabling you to trace issues back to specific changes.

2. Service Rollbacks: A Safety Net for Unexpected Issues

This acts as a safety net in case a new configuration deployment introduces problems. If unintended consequences or malfunctions arise, you can quickly roll back to a known-good version. This rollback capability minimizes downtime and ensures service continuity for your users, preventing disruptions.

3. Gateway Group Synchronization: Consistent Configurations Across Deployments

For complex deployments involving multiple gateway groups, maintaining identical configurations across all groups is crucial. Service version management simplifies this process with synchronization functionality. This ensures that all gateway groups have the exact same API logic-related configurations, guaranteeing consistent behavior for your API calls and the experience of the developers.

## Use Reasonable Version Numbers[â](#use-reasonable-version-numbers "Direct link to Use Reasonable Version Numbers")

* Major version increments (v1, v2) are used only when necessary breaking changes are required.
* Minor version increments (v1.1) are preferred for backward compatibility.
* Bug-fixing version increments (v1.1.1) should be harmless to the API consumers.
* Do not reuse deprecated version numbers.

## Typical Version Control Workflow[â](#typical-version-control-workflow "Direct link to Typical Version Control Workflow")

1. Add two gateway groups for the `test` and the `production` environments.
2. Publish the service to the `Test Group` with service version `1.0.0`.
3. Validate APIs in the `test` environment.
4. Update API configurations in the service template.
5. Publish the bug fix to the `Test Group` again with version `1.0.1`.
6. Synchronize services to the `Production Group` with service version `1.0.1`.
7. For a new sprint, edit the service template to add more routes.
8. Publish the service to the `Test Group` with service version `1.1.0`.
9. Validate APIs in the `test` environment and an emergency happens.
10. Rollback the service version to `1.0.0` for recovery.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)

* Getting Started

  <!-- -->

  * [Publish Service Version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md)
  * [Synchronize Published Service Version between Gateway Groups](https://docs.api7.ai/enterprise/3.3.x/getting-started/sync-service.md)
  * [Rollback a Published Service](https://docs.api7.ai/enterprise/3.3.x/getting-started/rollback-service.md)
