# Harbor docs | Harbor Installation Prerequisites

**Source:** https://goharbor.io/docs/2.14.0/install-config/installation-prereqs/

Harbor Installation Prerequisites

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

Harbor can be deployed to a Docker host using Docker Compose, or to a Kubernetes cluster using Helm.

### Resource Requirement

The table below outlines the minimum and recommended resource requirement for deploying Harbor.

| Resource | Minimum | Recommended |
| --- | --- | --- |
| CPU | 2 CPU | 4 CPU |
| Mem | 4 GB | 8 GB |
| Disk | 40 GB | 160 GB |

### Software Stack Requirements Compose

The following table lists the software versions that must be installed on the target host.

| Software | Version | Description |
| --- | --- | --- |
| Docker Engine | Version > 20.10 | [Docker Engine Installation](https://docs.docker.com/engine/install/) |
| Docker Compose | Docker compose > 2.3 | Docker Compose is part of Docker Engine |
| OpenSSL | Latest (optional) | Used to generate certificate and keys for Harbor |

### Network ports

Harbor requires that the following ports be open on the target host.

| Port | Protocol | Description |
| --- | --- | --- |
| 443 | HTTPS | Harbor portal and core API accept HTTPS requests on this port. You can change this port in the configuration file. |
| 80 | HTTP | Harbor portal and core API accept HTTP requests on this port. You can change this port in the configuration file. |

## Install Harbor on Kubernetes

To install docker with Helm, see the dedicated repository
[github.com/goharbor/harbor-helm](https://github.com/goharbor/harbor-helm)

## Next Steps

[Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/).

On this page

  
  

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/installation-prereqs.md)
[Create issue](https://github.com/goharbor/harbor/issues)