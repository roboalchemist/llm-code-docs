# Source: https://docs.api7.ai/enterprise/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/apisix/enterprise-feature/gateway-groups.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md

# Source: https://docs.api7.ai/apisix/enterprise-feature/gateway-groups.md

# Gateway Groups

A gateway group is a logical unit that combines one or more API gateway instances. These instances share the same configurations and behaviors when processing API requests. This ensures consistent API handling and simplifies administration across the group.

The default gateway group is sufficient for simple scenarios with only a single cluster or production environment. The advanced gateway groups are used for complex scenarios with separate API policies for different subsidiaries, lines of business, clusters, and environments like UAT and Staging. Although API7 Enterprise lacks concepts of multiple clusters and environments, you can achieve the same goal by naming and labeling gateway groups.

A gateway group contains one or more gateway instances, but each gateway instance belongs to only one gateway group. The gateway instances can be deployed on the same or different virtual machines, bare metal servers, or Kubernetes nodes. Such combinations can meet users' diverse requirements across multiple lines of business, clusters, work zones, and environments.

For example, in the diagram below, two teams are using API gateway in a company: Payment Team and Quote Team. The Payment Team has Production and UAT environments while the Quote Team has only one Production environment. In this case, three gateway groups can be created: `Payment Prod`, `Payment UAT`, and `Quote Prod`, and they can be labeled with `Env:Prod` and `Env:UAT`.

![Gateway Groups](https://static.api7.ai/uploads/2024/12/03/33FfJDFD_gateway-groups.jpeg)

## Key Features[â](#key-features "Direct link to Key Features")

* **API Gateway Group Management**: Managing a collection of API gateways as a logical unit sharing the same configurations. This simplifies administration and ensures consistent policy enforcement across the gateway instances.

* **Business-Aligned Gateway Partitioning**: Segregating an enterprise's lines of business and solutions by assigning them to dedicated API gateway groups. This architectural approach enables better alignment between the API infrastructure and the organization's functional domains.

* **Physical Isolation**: Gateway group isolates multiple API gateway instances in different physical environments, including datacenters, cloud platforms, and virtual machines. This effectively prevents interference between gateway groups and enhances system stability and security.

* **Elastic Scaling**: Gateway group dynamically adds or removes API gateway instances based on traffic fluctuations to meet business demands. This improves resource utilization and reduces operational costs.

* **Scalable and Flexible Infrastructure**: The logical architecture of the API gateway group is decoupled from the physical deployment of the individual gateway instances. This approach provides increased flexibility and scalability for the API infrastructure.

* **Fine-Grained Permission Control**: Gateway group enables different permission configurations for different gateway instances and APIs to adhere to compliance requirements.

## Use Cases[â](#use-cases "Direct link to Use Cases")

The versatility of gateway groups is reflected in their diverse range of use cases, which this section will explore in detail.

### Segregating Development, Test, UAT, and Production Environments[â](#segregating-development-test-uat-and-production-environments "Direct link to Segregating Development, Test, UAT, and Production Environments")

API deployment and release go through different stages and environments, which vary depending on companies' API management processes. Suppose your company has four environments: Dev, Test, UAT, and Prod. Without using gateway groups, you need to deploy 4 separate instances of API7 Enterprise, each with its independent control plane and data plane. Developers, QA, and Ops engineers need to develop, test, and release the same API by accessing API7 Enterprise's control plane with different domain names.

This approach has significant drawbacks. When you have 5 business lines, each with 4 environments, you need to deploy a total of 20 sets of API7 Enterprise, resulting in resource wastage and increased management costs.

By utilizing the gateway groups feature of API7 Enterprise, you can easily overcome this challenge. You can create 20 different gateway groups, following a naming convention that combines business line and environment names, and add labels for filtering and selection. Additionally, Role-Based Access Control (RBAC) can be applied to enable fine-grained permission control. In this manner, the developers can only modify the configuration in the development environment.

### Managing Multiple Clusters across Different Regions[â](#managing-multiple-clusters-across-different-regions "Direct link to Managing Multiple Clusters across Different Regions")

It is challenging to manage API services across multiple regions and clusters while ensuring data compliance for companies with a global customer base. Suppose your company operates in NA, EU, and APAC regions with 4 production clusters in each. Without gateway groups, you would need to maintain 12 sets of API gateway control planes and data planes. However, configuration discrepancies can easily occur with this approach. Even when most API gateway configurations are consistent, it takes additional effort to ensure that the encryption, privacy, and compliance-related settings of other components such as loggers, secret managers, and observability tools are consistent.

API7 Enterprise's gateway groups provide a solution to centrally manage and configure API gateway clusters across multiple regions using a single control plane. You can use environment variables, service discovery, and registry centers to simplify and unify management and maintenance to reduce overall maintenance costs.

Moreover, API7 Enterprise supports multi-layer networking, enabling seamless data processing and compliance across regions. If a US user named John logs in from Europe, the EU cluster can determine and redirect his API requests to the NA cluster based on his user ID. This capability ensures compliance and efficient API request handling.

### Meeting Service Level Objectives for Different Projects[â](#meeting-service-level-objectives-for-different-projects "Direct link to Meeting Service Level Objectives for Different Projects")

Services within various projects vary in their Service Level Objectives (SLOs). For instance, the SLO for a payment service can be 99.999%, while the SLO for a historical order service might be 99%. Specific strategies can be used for each service to align with their respective SLOs.

The infrastructure and operations teams can deploy the payment service in multiple regions, and then allocate more gateway instances and higher-quality machine resources to this gateway group, and set strict alerting policies and detailed observability metrics for it. Conversely, the historical order service with lower SLO requirements can adopt a lightweight deployment strategy with relaxed alerts and monitoring to reduce resource allocation.
