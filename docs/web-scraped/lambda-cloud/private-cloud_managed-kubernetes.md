# Overview -

Source: https://docs.lambda.ai/private-cloud/managed-kubernetes/

---

[managed kubernetes](../../tags/#tag:managed-kubernetes) [private cloud](../../tags/#tag:private-cloud)

# Overview

During the Private Cloud reservation process, you can choose to configure your cluster as a Managed Kubernetes cluster. In this configuration, Lambda manages your cluster's underlying environment, and you interact with the cluster through a browser-based Kubernetes administration UI and the Kubernetes API.

This document outlines the standard configuration for a Managed Kubernetes cluster in Lambda Private Cloud.

## Hardware

Lambda Private Cloud provides single-tenant clusters that are isolated from other clusters. The hardware details for your specific cluster depend on what you chose when reserving your cluster. Each cluster includes at least three control (CPU) nodes for cluster administration and job scheduling.

## Software

Your Managed Kubernetes deployment is configured to use Rancher with Rancher Kubernetes Engine 2 (RKE2).

- [Rancher](https://ranchermanager.docs.rancher.com/) provides a web UI for monitoring and managing aspects of your Kubernetes cluster. Rancher also provides your cluster's Kubenetes API server.
- [RKE2](https://docs.rke2.io/) is a fully conformant Kubernetes distribution focused on security and compliance.

## Cluster management

### Rancher dashboard

The Rancher dashboard serves as the main UI for your Managed Kubernetes cluster. After you set up your SSL VPN connection, you can access your dashboard at [https://10.141.3.1](https://10.141.3.1). The login details for your dashboard can be found in your 1Password vault.

For details on setting up your SSL VPN connection, see [Getting started > Establishing a secure connection to your cluster](getting-started/#establishing-a-secure-connection).

### Kubernetes API

The Kubernetes API is available at `https://10.141.0.250:6443` through your SSL VPN connection. You can obtain your `kubeconfig` file from the Rancher dashboard. For details, see [Getting started > Accessing the Kubernetes API](getting-started/#accessing-the-kubernetes-api).

## Storage

In the default cluster configuration, your cluster comes with three types of storage, each with its own performance and access characteristics:

- Common (Longhorn)
- Shared workload (Intelliflash)
- Scratch/HPC (directly attached local storage)

Each type is mapped to a corresponding storage class in Kubernetes:

- `longhorn`
- `intelliflash`
- `local-path`

Note

Each cluster also includes a `local-storage` storage class that Lambda uses to route monitoring metric replication. You can safely ignore this class— `local-path` is the dynamic provisioner routed to the fast NVMe arrays.
