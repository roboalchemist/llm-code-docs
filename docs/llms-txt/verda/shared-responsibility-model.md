# Source: https://docs.verda.com/resources/shared-responsibility-model.md

# Shared Responsibility Model

## Shared Responsibility

Our goal with the shared responsibility model is to outline the critical and complementary roles that both Verda and you, as a customer, play in ensuring the security and compliance of your projects. Our aim is to be a secure and reliable operator that you can trust.

### Customer

As the customer, you are the most knowledgeable about your security and compliance needs and ensure that they are met. While working within our services, it is important that you understand and identify your usage of our services and how they impact your needs.

There are certain actions you must take to ensure your security and compliance. This will require appropriately configuring your implementations and services with secure best practices.

For example, if you deploy a GPU instance within our services, you are responsible for managing the configurations of the operating system, network, firewall, access management, and data encryption. You are also responsible for your backups, disaster recovery, and any continuity of service that falls outside of our responsibilities.

### Provider Responsibilities

As the provider, Verda is responsible for the operation and protection of the infrastructure in which we offer our services. Depending on the level of service, this can include the facilities, hardware, networking, and software that make up the collection of our service offerings.

For instance, if you deploy a GPU instance within our services, we will maintain and secure the physical infrastructure (e.g., power, network connections, location), access to the physical infrastructure, provisioning of the service, and provide a method for you to access your instance.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-0a0dc2a3d2767767e034cd392865c99b8e5187ae%2FShared%20Responsibility%20Model.png?alt=media" alt=""><figcaption></figcaption></figure>

In the model above, the columns include but are not limited to:

* **Bare metal as a service** - physical servers and bare-metal clusters,
* **Infrastructure as a service** - virtual machine instances, storage,
* **Platform as a service** - serverless containers,
* **Software as a service** - cloud console, billing, IAM,
* **Model** - managed model endpoints.
