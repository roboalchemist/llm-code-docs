# Source: https://docs.portainer.io/2.33-lts/faqs/getting-started/what-is-portainers-architecture.md

# Source: https://docs.portainer.io/sts/faqs/getting-started/what-is-portainers-architecture.md

# Source: https://docs.portainer.io/faqs/getting-started/what-is-portainers-architecture.md

# What is Portainer's architecture?

Portainer consists of two elements: the Portainer Server and the Portainer Agent. Both run as lightweight containers on your existing containerized infrastructure. The Portainer Agent should be deployed to each node in your cluster and configured to report back to the Portainer Server container.

A single Portainer Server will accept connections from any number of Portainer Agents, providing the ability to manage multiple clusters from one centralized interface. To do this, the Portainer Server container requires data persistence. The Portainer Agents are stateless, with data being shipped back to the Portainer Server container.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FyEAvW327tFa9AoEfRcen%2F2.38-portainer-architecture-detailed.png?alt=media&#x26;token=84ca8e46-7b8c-4600-8676-5f80694da60c" alt=""><figcaption></figcaption></figure>

For a deeper dive into the architecture of Portainer, have a look at our [technical architecture overview](https://dl.portainer.io/dl/whitepapers/portainer-technical-architecture.pdf).
