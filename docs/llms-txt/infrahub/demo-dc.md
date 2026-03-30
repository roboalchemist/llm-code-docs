# Source: https://docs.infrahub.app/demo-dc.md

# Infrahub bundle-dc example

Welcome to the Infrahub bundle-dc example. This repository showcases how Infrahub serves as an infrastructure data management platform for managing modern network infrastructure with design-driven automation. It demonstrates Infrahub's core capabilities including:

* Schema-driven data modeling
* Composable topology generation
* Version control for infrastructure data
* Automated configuration generation
* Validation workflows

Whether you're a network engineer exploring automation, a developer building on Infrahub, or an architect evaluating infrastructure management platforms, this bundle provides hands-on experience with real-world patterns and workflows.

## Community contribution[​](#community-contribution "Direct link to Community contribution")

note

This demo repository is partially authored by the OpsMill community member [tomek](https://www.linkedin.com/in/tomekzajac/) from this example: [GitHub t0m3kz/infrahub-demo](https://github.com/t0m3kz/infrahub-demo)

## Documentation guide[​](#documentation-guide "Direct link to Documentation guide")

This documentation is organized following the [Diataxis framework](https://diataxis.fr/) to help you find exactly what you need:

### Getting started[​](#getting-started "Direct link to Getting started")

| Page                                          | Purpose                                                                                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Installation guide](/demo-dc/install.md)** | Step-by-step instructions to install and set up the demo environment on your system. Start here if this is your first time running the demo. |

### Tutorials[​](#tutorials "Direct link to Tutorials")

| Page                                                                              | Purpose                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[User walkthrough](/demo-dc/user-walkthrough.md)**                              | A complete hands-on tutorial that guides you through the end-user experience: creating topologies, managing branches, running generators, creating proposed changes, and validating configurations. Perfect for learning the workflow from start to finish.                                                        |
| **[Deploy a virtual lab with Containerlab](/demo-dc/containerlab-deployment.md)** | Learn how to deploy generated configurations to a virtual network lab using Containerlab. Extract device configurations and topology files from Infrahub, spin up virtual Arista cEOS switches, and test your data center fabric before production deployment.                                                     |
| **[Working with security management](/demo-dc/security-management.md)**           | Explore Infrahub's security management capabilities by examining firewall policies, security zones, and address objects. Learn how structured security data transforms into vendor-specific firewall configurations (Juniper JunOS) and how to modify policies safely using branches.                              |
| **[Cloud resource management](/demo-dc/cloud-management.md)**                     | Manage multi-cloud infrastructure (AWS, GCP, Azure) with a vendor-agnostic schema. Load demo cloud data including accounts, regions, virtual networks, instances, and security groups. Learn how Infrahub serves as a unified inventory for cloud resources.                                                       |
| **[Using the service catalog](/demo-dc/service-catalog.md)**                      | Learn how to use the Service Catalog web interface for simplified infrastructure provisioning. Enable the Streamlit application, navigate between branches, view existing infrastructure, and create new data centers through a guided form-based workflow that automates branch creation and generator execution. |

### Guides[​](#guides "Direct link to Guides")

| Page                                                    | Purpose                                                                                                                                                                                                                                                         |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Developer guide](/demo-dc/developer-guide.md)**      | Technical deep-dive into how the demo works under the hood. Covers schema architecture, bootstrap scripts, generators, transforms, checks, and testing. Use this when extending functionality, troubleshooting issues, or understanding implementation details. |
| **[Using Infrahub Enterprise](/demo-dc/enterprise.md)** | Instructions for configuring the demo environment to use Infrahub Enterprise edition. Learn how to switch between Community and Enterprise editions, configure environment variables, and understand the differences between editions.                          |

### Topics[​](#topics "Direct link to Topics")

| Page                                                   | Purpose                                                                                                                                                                                                                                         |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Understanding the concepts](/demo-dc/concepts.md)** | Explains the architectural patterns, design decisions, and core Infrahub concepts demonstrated in this project. Read this to understand the "why" behind design-driven automation, composable topologies, generators, and integration patterns. |

## Quick start[​](#quick-start "Direct link to Quick start")

If you're ready to dive in:

1. Follow the **[installation guide](/demo-dc/install.md)** to set up your environment
2. Walk through the **[user tutorial](/demo-dc/user-walkthrough.md)** to create your first data center topology
3. Deploy to a **[virtual lab with Containerlab](/demo-dc/containerlab-deployment.md)** to test configurations
4. Try the **[Service Catalog](/demo-dc/service-catalog.md)** for simplified infrastructure provisioning
5. Explore the **[concepts](/demo-dc/concepts.md)** to deepen your understanding
6. Reference the **[developer guide](/demo-dc/developer-guide.md)** when you're ready to extend or customize

## What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

Through this demo, you'll gain practical experience with:

* **Schema-driven infrastructure modeling** - Defining devices, networks, and services with flexible, extensible schemas
* **Design-driven automation** - Creating abstract topology designs that generators transform into concrete infrastructure
* **Composable topologies** - Building complex data center and POP architectures from reusable components
* **Version control for data** - Using branches and proposed changes to safely modify infrastructure
* **Automated resource allocation** - Generating IP prefixes, VLANs, and addressing from resource pools
* **Configuration generation** - Transforming structured data into device configurations via templates
* **Data validation** - Enforcing consistency with custom checks
* **GitOps patterns** - Managing infrastructure as code with full versioning and review workflows

## Architecture at a glance[​](#architecture-at-a-glance "Direct link to Architecture at a glance")

The demo implements realistic network topologies including:

* **Data center fabrics** with spine-leaf architecture and VxLAN/EVPN overlay
* **Point of presence (POP) networks** with edge routers and peering connections
* **Network segments** with load balancers and service endpoints
* **Security zones and policies** with firewall rules and access control
* **Cloud infrastructure** with vendor-agnostic modeling for AWS, GCP, and Azure
* **Resource pools** for IP address, VLAN, and ASN allocation
* **Multi-vendor support** (Arista, Juniper, Cisco, and SONiC templates)
* **Automated topology generation** from abstract design definitions

## Key features demonstrated[​](#key-features-demonstrated "Direct link to Key features demonstrated")

### Schema extensibility[​](#schema-extensibility "Direct link to Schema extensibility")

The demo includes comprehensive schemas for DCIM, IPAM, topology, routing, security, and load balancing. These schemas define not just object types, but relationships, constraints, and lifecycle behaviors.

### Generators and automation[​](#generators-and-automation "Direct link to Generators and automation")

When you create a topology design (for example, DC-3), generators automatically create all supporting objects including devices, interfaces, IP addresses, routing protocols, and BGP peer groups following best practices and business rules.

### Branch-based workflows[​](#branch-based-workflows "Direct link to Branch-based workflows")

All changes happen in branches. Proposed changes provide diff views, run validation checks, and regenerate artifacts before merging to main.

### Artifact generation[​](#artifact-generation "Direct link to Artifact generation")

Templates transform Infrahub data into deployable artifacts including device configurations, topology diagrams, and cabling matrices.

## Community and support[​](#community-and-support "Direct link to Community and support")

* **Source code**: [GitHub repository](https://github.com/opsmill/infrahub-demo-dc)
* **Infrahub documentation**: [docs.infrahub.app](https://docs.infrahub.app)
* **Discord community**: [Discord](https://discord.gg/opsmill)
* **OpsMill website**: [opsmill.com](https://opsmill.com)

## Next steps[​](#next-steps "Direct link to Next steps")

Ready to get started? Head to the **[installation guide](/demo-dc/install.md)** to set up your environment.
