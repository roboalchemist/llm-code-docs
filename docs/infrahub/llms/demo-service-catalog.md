# Source: https://docs.infrahub.app/demo-service-catalog.md

## Infrahub - PoC of a service catalog[​](#infrahub---poc-of-a-service-catalog "Direct link to Infrahub - PoC of a service catalog")

This repository demonstrates a proof of concept for a service catalog using Infrahub and Streamlit.

For more information about the business case and the development of this PoC, read the [blog post](https://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/) on the OpsMill website.

[Blog posthttps://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/](https://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/)

## The problem[​](#the-problem "Direct link to The problem")

Organizations strive to deliver services efficiently, as this is where value is created.

The stakes are high: the structure of a service determines everything downstream—from invoicing and lifecycle management to resource allocation and capacity planning. A poorly designed service layer can lead to inefficiencies and challenges at every stage.

The service catalog forms the foundation of this structure, serving as a blueprint for how services are defined, managed, and delivered. It enables infrastructure self-service across the organization to streamline operations and enhance service delivery.

## Use case[​](#use-case "Direct link to Use case")

![Otternet](/assets/images/otternet-491510e07a59395b882e6f8abe580b5f.png)

This demo follows a fictional ISP, Otter-net, which provides standard internet connectivity.

![Backbone](/assets/images/network-backbone-230ca1a3cfa0412b7a5a7825ea721e8c.png)

The company operates multiple points of presence across Europe. Currently, it offers a single service: dedicated internet access. This service provides customers with a physical port and a set of public IP addresses for hosting services. Additional services are planned for the future!

![Service](/assets/images/network-customer-service-355b7b6ffae51cc19bb9cc1d0468d873.png)

The operational team at Otter-net is divided into two groups:

* Network Architects: Experts with extensive networking experience, responsible for operating and maintaining the backbone network.
* Service Delivery Team: Customer-facing professionals responsible for provisioning and connecting services to the backbone.

The goal

The goal of the company is to automate the service delivery process, allowing the service delivery team to request new services without needing to involve network architects for every request. This will enable faster and more efficient service delivery.

## The solution[​](#the-solution "Direct link to The solution")

Implementing a service catalog is a complex operation that many organizations struggle with. It demands a deep understanding of the product lifecycle, the interplay of various components, and coordination among numerous stakeholders. Beyond that, it requires a robust technical implementation to automate all the associated rules and processes properly.

In many ways, Infrahub is the perfect tool to support your service catalog implementation:

* **Flexible Schema**: Infrahub's schema can be tailored to fit the specific needs of your service catalog, allowing you to define services, components, and their relationships in a way that makes sense for your organization.
* **Version Control**: Infrahub's native version control capabilities enable you to track changes, ensuring that you have full visibility into the evolution of your network.
* **Generators**: Infrahub's generators can be used to codify the rules and processes associated with your service implementation, enabling fast and consistent implementation across the board.
* **Resource Managers**: Infrahub's resource managers can be used to automate the allocation and management of resources, ensuring robust and efficient resource management.
* **Branching**: Infrahub's branching capabilities allow you to isolate changes in a separate branch, paving the way for testing and validation before deploying changes to production.

If you want more information about the business case and how this PoC was built, you can read the corresponding [blog post](https://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/) on the OpsMill website.

[Blog posthttps://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/](https://opsmill.com/blog/how-to-turn-your-source-of-truth-into-a-service-factory/)
