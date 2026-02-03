# Source: https://docs.vespa.ai/en/operations/kubernetes/vespa-on-kubernetes.html.md

# Vespa on Kubernetes

 

Vespa applications can be deployed on Kubernetes using the Vespa Operator. The Vespa Operator provides a native Kubernetes experience to the management of Vespa infrastructure and applications. This includes the deployment, configuration, and upgrades to a Vespa cluster and critical lifecycle operations.

## Overview

The Vespa Operator simplifies running Vespa on Kubernetes by providing:

- Declarative configuration with a [Custom Resource Definition (CRD)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- Automated Vespa infrastructure deployment and management
- Automated deployment, updates, and upgrades to Vespa applications
- Critical lifecycle operations such as failure handling
- Secure clusters with TLS
- Kubernetes-native monitoring of Vespa applications
- Integration with Kubernetes-native tooling

Refer to the following sections to install, configure, and manage Vespa on Kubernetes. For more details on the design and setup of Vespa on Kubernetes, refer to the [Architecture](architecture.html) section.

- [Install Vespa on Kubernetes](installation.html)
- [Lifecycle Operations for Vespa on Kubernetes](operations.html)
- [Enable TLS Encryption for Vespa on Kubernetes](tls.html)
- [Monitor a Vespa on Kubernetes Deployment](monitoring.html)
- [Configure Log Collection](logging.html)
- [Configure External Access Layer for Vespa on Kubernetes](ingress.html)
- [Provide Custom Overrides](custom-overrides-podtemplate.html)

 Copyright © 2026 - [Cookie Preferences](#)

