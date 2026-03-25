# Source: https://docs.startree.ai/getstarted/deployment/deployment_models.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Options

> StarTree Cloud provides a fully managed experience for deploying and managing real-time analytics. Leverage the Shared SaaS option for fast setup, or use your own cloud for more control.

StarTree Cloud provides three deployment options built for varying requirements and allowing you to focus on the most important part — elevating the experience for your customers.

* **Shared SaaS (Public SaaS):** A traditional SaaS edition of StarTree cloud is great for customers who want a low-touch experience and prefer a hassle-free, convenient SaaS service.
* **Bring Your Own Cloud (BYOC):** Also called Private SaaS (Dedicated SaaS), this edition of StarTree Cloud caters to customers who want additional control over how data is managed and stored.
* **Bring Your Own Kubernetes (BYOK):** Available in preview, this deployment option gives customers complete control over the StarTree Cloud infrastructure within their own Kubernetes environments, and is ideal for security-sensitive customers who require strict data controls.

There are two main components in each deployment model:

* **Data Plane:** All the components required for data collection, management, and query processing along with the value-added services and tools.
* **Control Plane:** Responsible for deployment, management, and coordination across all StarTree data planes.

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/getstarted/images/startree-cloud-byoc-saas-comparison.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=1984af5a7e59ba5a7c11b69742fc0e66" alt="Public SaaS and BYOC Deployment Models" width="2370" height="1148" data-path="getstarted/images/startree-cloud-byoc-saas-comparison.png" />

In a **Public SaaS** deployment, both the StarTree control plane and data plane are deployed in the cloud network managed by StarTree. In this case, data and queries from your cloud network are sent to the StarTree cloud network.

In a **BYOC** deployment, the StarTree data plane is deployed in your cloud network so that it is co-located with your other data systems and applications. In this case, the StarTree control plane remotely manages the data plane.

A **BYOK** deployment is similar to BYOC, with the added security of network isolation. The environment is managed by a local StarTree agent, which is responsible for pulling upgrade packages and configuration metadata.

## Benefits

### Public SaaS

* Fully hands-free: You don’t need to be involved at all in administering the data plane
* Simpler setup: You just focus on your data, your schema, and queries.
* Isolation guarantee: Your SaaS instance is isolated from an infrastructure as well as the Pinot cluster point of view.

### BYOC

* Compliance & Data Security: Data never leaves the customer’s security perimeter Customers have full control over who gets access to the data as well as adhere to their data compliance and governance standards.
* Fully managed: Customers get a comprehensive SaaS-like experience without the need for any in-house expertise. They don’t need to worry about deployment, upgrades, and routine cluster maintenance.
* SLA: Customers get the same SLA guarantees as that of a traditional SaaS deployment
* Flexibility: Since infrastructure is deployed in the customer’s environment, they can choose from a variety of supported compute and storage instance types and advanced customizations.
* Cost savings: Allows the customer’s cloud savings plan to be applied towards this infrastructure.
* No persistent connection is needed between the control and the data plane.

### BYOK

* Provides a way to completely air-gap the Pinot cluster for enhanced security.
* Compliance & Data Security: Data never leaves the customer’s security perimeter Customers have full control over who gets access to the data as well as adhere to their data compliance and governance standards.
* Flexibility: Since infrastructure is deployed in the customer’s environment, they can choose from a variety of supported compute and storage instance types and advanced customizations.
* Cost savings: Allows the customer’s cloud savings plan to be applied towards this infrastructure.
* No inbound access from Startree Control plane.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/concepts/images/deployment_flexibility.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=089ad273c419af289da9402597f1ca6f" alt="Deployment Flexibility" title="Deployment Flexibility" className="mx-auto" style={{ width:"40%" }} width="641" height="1033" data-path="concepts/images/deployment_flexibility.png" />

## Feature Checklist

| Feature                              | Public SaaS                                              | BYOC                                                                  | BYOK                                                                  |
| ------------------------------------ | -------------------------------------------------------- | :-------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Fully Managed**                    | Yes                                                      | Yes                                                                   | Partial                                                               |
| **SLA Guarantees**                   | Yes                                                      | Yes                                                                   | Partial                                                               |
| **24x7 Support**                     | Yes                                                      | Yes                                                                   | Yes                                                                   |
| **Provisioning Complexity**          | Simple                                                   | Simple                                                                | Moderate                                                              |
| **Authentication and Authorization** | Supported                                                | Supported                                                             | Supported                                                             |
| **Isolation Guarantees**             | Supported                                                | Supported                                                             | Supported                                                             |
| **Data management and Security**     | Stored securely in StarTree operated clusters            | Data never leaves customer’s compliance boundary                      | Data never leaves customer’s compliance boundary                      |
| **Data Governance and Compliance**   | Standard                                                 | Flexible: customer dictates the policies                              | Flexible: customer dictates the policies                              |
| **Certifications**                   | Soc2 Type2   ISO27001             HIPAA BAA              | Soc2 Type2        ISO27001                  HIPAA BAA                 | Soc2 Type2        ISO27001                  HIPAA BAA                 |
| **Infrastructure Customization**     | Standard compute and storage instance types              | Broader range of compute and storage types to choose from             | Broader range of compute and storage types to choose from             |
| **Cost Optimizations**               | Standard: Uses StarTree Cloud account for cloud provider | Can apply customer cloud account savings for additional TCO reduction | Can apply customer cloud account savings for additional TCO reduction |
| **Software Upgrades**                | Supported                                                | Supported                                                             | Supported                                                             |
| **Infrastructure Upgrades**          | Supported                                                | Supported                                                             | Customer owned                                                        |
| **Monitoring and Observability**     | Supported                                                | Supported                                                             | Supported                                                             |

Built with [Mintlify](https://mintlify.com).
