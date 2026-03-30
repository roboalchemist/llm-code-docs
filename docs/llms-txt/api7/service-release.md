# Source: https://docs.api7.ai/apisix/enterprise-feature/service-release.md

# Service Release

The core function of an API gateway is to expose backend services to developers and frontend applications via APIs. This process typically involves the following key steps:

1. **Creating Services**: The API gateway organizes and manages the microservices backend by defining services, allowing frontend applications to interact with backend services through a unified API interface.

2. **Configuring Routing Rules**: By setting up routing rules in the API gateway, external requests can be controlled and forwarded appropriately to internal microservices.

3. **Targeting Deployment Environment**: Selecting the appropriate gateway group for deployment ensures that the service configuration is effective in the intended environment.

4. **Adding Plugins**: The API gateway enhances its functionality through plugins, including authentication, data encryption, and rate limiting to meet requirements of API security, monitoring, and rate limiting.

This entire process, from service definition to deployment, is collectively called service release. In practical business scenarios, effectively managing service releases and avoiding production environment failures caused by deployment errors has become a crucial task of API gateway management in enterprises.

## Two Main Approaches to Service Release[â](#two-main-approaches-to-service-release "Direct link to Two Main Approaches to Service Release")

In production environments, companies choose various service release processes and rules based on their specific needs and development strategies. Broadly, these processes can be categorized into two main approaches:

### Rapid Service Release[â](#rapid-service-release "Direct link to Rapid Service Release")

Some enterprises opt for a rapid iteration approach. They release services directly to the production environment after developing and verifying the services in the development and testing phases. This method is typically suitable for scenarios where requirements change rapidly and there is a high demand for service responsiveness. To mitigate deployment risks, these companies often implement strategies such as canary releases and blue-green deployments, which enable phased rollouts of new service versions, ensuring that any anomalies can be quickly rolled back to a stable version.

For instance, an e-commerce platform might directly release a newly configured payment service to the production environment after validation. During the deployment process, they use a canary release strategy to allocate the new service version to a specific percentage of users, allowing for immediate detection and adjustment in case of issues in the production environment.

### Version-Based Service Release[â](#version-based-service-release "Direct link to Version-Based Service Release")

Conversely, some companies prefer to ensure the stability and availability of services through a more rigorous process before releasing services to production. These organizations typically deploy services first to a testing environment, followed by thorough validation, then to a User Acceptance Testing (UAT) environment, and finally to the production environment. This multi-stage validation reduces the risk of failures in the production environment.

For example, a financial institution might adopt this process by first validating a new version of its authentication service in the testing environment. After successful validation, it would proceed to the UAT environment for performance verification, ensuring the service can operate stably under high concurrency conditions, before finally deploying it to production.

Both approaches have their advantages: rapid service release is ideal for fast-paced iteration, while version-based service release emphasizes service stability and reliability.

## Key Features[â](#key-features "Direct link to Key Features")

In API7 Enterprise, service release is robust and capable of meeting various business needs. Key capabilities include:

### Service Templates[â](#service-templates "Direct link to Service Templates")

One of the key features is the introduction of service templates, which provide flexible and reusable configuration templates for service release. Users can define a standard set of service configurations as a template for reuse across different environments. This process simplifies the release process, enhances efficiency, and reduces human error.

For example, users can create a "Generic Payment Service Template" that defines common payment service interfaces and routing rules. Whenever a new payment service needs to be published, teams can quickly generate a comprehensive service by selecting this template, deploying it to the desired environment, and inputting specific parameters.

Service templates also support version control, allowing users to flexibly choose which version of the service template to use based on different requirements and historical versions. This way, when service configurations change, teams can track all published changes through version management, ensuring that each version has a clear historical record.

### Published Version Management[â](#published-version-management "Direct link to Published Version Management")

API7 Enterprise not only supports creating new services but also allows users to view and manage published service versions. Each service version can be managed independently, enabling users to review historical configuration settings, perform version rollbacks, or reference previous configurations when releasing new versions.

This management approach greatly enhances the flexibility and security of service publishing. If an issue arises with a particular version during the publishing process, users can directly roll back to the previous version, avoiding service interruptions in the production environment.

### Historical Version Tracking[â](#historical-version-tracking "Direct link to Historical Version Tracking")

API7 Enterprise also provides a historical version feature that helps users track change records for each service release. This is particularly important for long-term service maintenance, especially in multi-team collaboration scenarios. By reviewing historical versions, developers can easily pinpoint issues caused by specific configuration changes, thereby reducing the time required for troubleshooting and fixing problems.

For instance, if a performance issue arises in the payment service after a particular release, developers can quickly identify that a certain configuration item in the service template has changed by examining the historical versions, allowing them to trace the specific cause.

## Use Cases[â](#use-cases "Direct link to Use Cases")

The service release feature of API7 Enterprise is applicable to various real-world scenarios, providing significant convenience in multi-environment deployment and version management.

### Multi-Environment Deployment[â](#multi-environment-deployment "Direct link to Multi-Environment Deployment")

In large enterprises, service deployment typically involves multiple environments, such as development, testing, UAT, and production environments. API7 Enterprise supports reusing configurations through service templates, greatly simplifying the service release process across different environments.

For example, developers can complete the service configuration in the development environment and, once validated, easily migrate that configuration to the testing environment using service templates. After successful testing, the service can then be promoted to the UAT environment and finally deployed to production.

### Version Management and Rollback[â](#version-management-and-rollback "Direct link to Version Management and Rollback")

For services that require frequent updates, version management and rollback are crucial. The version control feature in API7 Enterprise helps organizations effectively manage the history of service deployments. In the event of an issue, services can be quickly rolled back to a stable version, preventing serious failures in the production environment.

For instance, if an incompatible change in the API payment interface in a particular version leads to payment failures for some users, developers can swiftly use the rollback feature of API7 Enterprise to revert the service to the previous version, ensuring that payment functionality is restored.
