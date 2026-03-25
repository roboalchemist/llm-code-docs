# Source: https://docs.axonius.com/docs/the-shared-security-responsibility-model-for-axonius-customers.md

# The Shared Security Responsibility Model for Axonius Customers

What cybersecurity measures are within Axonius’ purview when a customer purchases our solutions, and what security responsibilities rest with the customer? Our [Terms of Use](https://www.axonius.com/terms-conditions/) and related contractual agreements formally outline our obligations and the customer’s expectations.

This document aims to provide an overview of certain security expectations and realities, for informational purposes only, in the spirit of the Shared Responsibility Model. In this model, an industry best practice, customers and providers of cloud and SaaS products should understand the scope of each other’s security programs and capabilities. For additional details, Axonius customers and prospects under NDA can review our answers to the [Consensus Assessments Initiative Questionnaire (CAIQ)](https://trust.axonius.com/?itemUid=d1cd6f4f-d63b-4f76-95fd-46df378c8a79) from the [Axonius Trust Center](https://trust.axonius.com/), which describes many aspects of our cybersecurity program.

At a high level, below are the parties having feasible visibility/control in relation to certain key security areas, drawing a distinction between the deployment model where [Axonius hosts](/docs/saas-deployment) the product and one where  the [customer self-hosts](/docs/on-premise-and-private-cloud-deployments) it:

|                                         |                           |                                          |
| --------------------------------------- | ------------------------- | ---------------------------------------- |
| Security Area                           | Axonius Hosts the Product | Customer Hosts the Product (Self-Hosted) |
| Physical Data Center                    | Axonius                   | Customer                                 |
| Network, Hypervisor, and Infrastructure | Axonius                   | Customer                                 |
| The Product’s Virtual Machine           | Axonius                   | Customer                                 |
| Product Application Code                | Axonius                   | Axonius                                  |
| Product Application Configuration       | Customer                  | Customer                                 |
| End-User Access and Endpoints           | Customer                  | Customer                                 |

Take a closer look at each security area and the associated expectations below.

### Physical Data Center

When Axonius hosts the product for the customer,  we use AWS as our hosting provider and rely on [AWS to ensure the physical security](https://aws.amazon.com/compliance/data-center/controls/) of the environment.

When our customer hosts the Axonius product instance, the customer is responsible for the physical security measures of the hosting environment. (Sometimes, this deployment model is called private cloud or on-premises.)

### Network, Hypervisor, and Infrastructure

In the Axonius-hosted deployment model, Axonius handles the management and security of the network, hypervisor configuration, and other aspects of the hosting infrastructure where the product resides, including network access controls and infrastructure security monitoring.

Self-hosting Axonius customers are responsible for such security measures since the Axonius product resides in their environment, which they manage and control.

### The Product’s Virtual Machine

For Axonius-hosted customers, Axonius manages the Operating System and packages inside the virtual machine where our product application runs. This includes the ability to monitor certain security activities occurring within the virtual machine and update it with appropriate security patches.

Self-hosting customers are responsible for managing the virtual machine in which our product application runs, including monitoring it for security events and managing its security configuration and patches. Such customers may decide to install their own security agent software into the Axonius-provided virtual machine to monitor it in a way consistent with their security practices.

### Product Application Code

As the software provider, Axonius manages various aspects of our applications' product security. This includes having a formal Secure Development Lifecycle (SDL) program, which seeks to identify and appropriately remediate vulnerabilities in our code and its dependencies.

### Product Application Configuration

As the administrators and users of our products, Axonius customers are responsible for configuring the application to meet their requirements according to their change management expectations, which includes determining how to [add adapters](/docs/adapters-page) or [manage other application settings](/docs/using-the-system-settings-page). Customers are also responsible for monitoring application-level activity logs to identify security anomalies [within the Axonius application.](/docs/activity-logs-page)

### End-User Access and Endpoints

Customers are responsible for managing the end-users who access the customer's product instance which includes creating and removing users within the product application and providing them with the appropriate access using its [Role-based Access Control (RBAC) features.](/docs/role-based-access-control-rbac-management)