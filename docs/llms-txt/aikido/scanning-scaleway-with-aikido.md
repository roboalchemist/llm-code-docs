# Source: https://help.aikido.dev/workflows-and-guides/additional-cloud-providers/scanning-scaleway-with-aikido.md

# Scanning Scaleway with Aikido

Aikido fully supports protecting workloads on Scaleway through specific integrations. A native integration may be added in the future, but you can already achieve full coverage by combining:<br>

* [**Container image scanning**](#container-image-scanning) for Scaleway registry or any other OCI-compatible registry
* [**Kubernetes cluster scanning**](#kubernetes-cluster-scanning) for Scaleway Managed Kubernetes or self-managed clusters
* [**Kubernetes cluster image scanning**](#kubernetes-cluster-image-scanning) for Scaleway Managed Kubernetes or self-managed clusters
* [**Virtual machine scanning**](#virtual-machine-scanning) via the Local VM Scanner on Scaleway instances

## Features

### Container image scanning

Scaleway’s container registry and most third-party registries you use from Scaleway are OCI-compatible, so they can be scanned using Aikido.

Create a read-only or pull-only user in Scaleway registry: <https://www.scaleway.com/en/docs/container-registry/how-to/connect-docker-cli/>

Follow the OCI guide below to configure container image scanning

{% content-ref url="../../container-image-scanning/standalone-registries/generic-oci-compatible-registry" %}
[generic-oci-compatible-registry](https://help.aikido.dev/container-image-scanning/standalone-registries/generic-oci-compatible-registry)
{% endcontent-ref %}

### Kubernetes cluster scanning

If you use Scaleway Managed Kubernetes or run your own Kubernetes clusters on Scaleway VMs, you can connect them as generic Kubernetes clusters.

{% content-ref url="../../cloud-scanning/kubernetes-cluster-scanning" %}
[kubernetes-cluster-scanning](https://help.aikido.dev/cloud-scanning/kubernetes-cluster-scanning)
{% endcontent-ref %}

### Kubernetes cluster image scanning&#x20;

If you use Scaleway Managed Kubernetes or run your own Kubernetes clusters on Scaleway VMs, you can scan the images of running containers with Kubernetes image scanning.

{% content-ref url="../../cloud-scanning/kubernetes-cluster-scanning/kubernetes-in-cluster-image-scanning" %}
[kubernetes-in-cluster-image-scanning](https://help.aikido.dev/cloud-scanning/kubernetes-cluster-scanning/kubernetes-in-cluster-image-scanning)
{% endcontent-ref %}

### Virtual Machine scanning

To scan Virtual Machines on Scaleway, use the Local VM Scanner. It inspects packages, system dependencies and configuration directly on the instance.

{% content-ref url="../../virtual-machine-scanning/local-vm-scanning" %}
[local-vm-scanning](https://help.aikido.dev/virtual-machine-scanning/local-vm-scanning)
{% endcontent-ref %}

You can roll this out centrally using your usual automation tooling (e.g. Ansible, Terraform-provisioned scripts, or cloud-init) so that new Scaleway instances are automatically enrolled.
