# Source: https://docs.gitguardian.com/self-hosting/architecture.md

# GitGuardian Architecture

> Overview of GitGuardian self-hosted architecture, including Kubernetes components, ingress configuration, and deployment topology.

The GitGuardian application is built on a flexible cloud-native architecture. It leverages Helm charts for streamlined deployment, offering two primary methods: the KOTS admin interface (KOTS-based deployment) or the Helm CLI (Helm-based deployment).

## Scalable and Modular Architecture

GitGuardian employs a modular architecture, where each core component is deployed as an independent service. This design enhances scalability and allows for greater flexibility:

- **Replica Scaling:** Adjust the number of replicas for each service to meet demand.
- **Resource Configurations:** Fine-tune resource requests and limits. These settings can be configured via Helm during installation or within the KOTS UI with some restrictions.
- **Dedicated Workers:** Create dedicated worker pods to handle high-demand queues (available in Helm-based deployments).
- **Autoscaling:** Leverage Horizontal Pod Autoscaling to automatically adjust worker pod counts based on load.

#### Architecture Overview

The GitGuardian architecture uses a single entry point for all API callsâeither an Ingress or a Service of type LoadBalancerâwhich routes traffic through an Nginx service acting as both a frontend and a reverse proxy. Nginx is responsible for distributing incoming requests among the internal APIs, public APIs, and hook APIs. In this setup, Nginx handles all the routing logic, and there is only one Ingress or LoadBalancer resource exposing the application to the outside world.

![GitGuardian Architecture](/img/self-hosting/gitguardian-arch-ingress-agnostic.drawio.png)

For more details on deployment configurations, pod types, and usage, check the [GitGuardian Application Topology](./troubleshoot/topology) page. For scaling guidelines, visit [Scaling GitGuardian](./management/infrastructure-management/scaling).

## Helm command line support

The `helm install` feature enables streamlined deployment and management via the widely adopted Helm package manager. This integration simplifies installation, upgrades, and configuration as code.

Looking ahead, future releases will extend support for GitOps tools like ArgoCD and introduce more advanced configuration options, including:

- External Secrets Operator
- Istio Service Mesh & Gateway
- Certificate Manager

**Learn More:** [Install on an Existing Cluster using Helm](./installation/installation-existing-cluster-helm).

## Enhanced security with Chainguard integration

The GitGuardian architecture incorporates [Chainguard](https://www.chainguard.dev), a next-generation security tool that helps mitigate Common Vulnerabilities and Exposures (CVEs) in self-hosted container images.

With Chainguard, GitGuardian strengthens its security posture by:

- Reducing vulnerability risks in container images.
- Implementing FIPS-approved cryptographic modules for secure encryption of sensitive data both at rest and in transit.

This integration reinforces GitGuardianâs commitment to meeting the highest security and compliance standards.

**Read More:** [Common Vulnerabilities and Exposures](./security/recommendations#common-vulnerabilities-and-exposures).
