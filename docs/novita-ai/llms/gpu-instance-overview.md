# Source: https://novita.ai/docs/guides/gpu-instance-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

<u>**GPU Instance**</u> provides cost-effective, accessible high-performance computing with easy GPU access, making it ideal for complex AI tasks. Users benefit from on-demand rental, optimizing both efficiency and cost-effectiveness.

## Features

* Rich **built-in templates** help you quickly deploy GPU instances for AI tasks out of the box;
* Start a GPU instance **in seconds**, helping you quickly handle traffic peaks;
* Provides nodes in **multiple global regions** to deploy GPUs closer to your users for minimal latency;
* Provides **free local storage** and allows you to attach network volume, also provides free network transfer;
* Billing is **accurate to the second**, charging only for the actual running time of the GPU container instances;
* **Affordable pricing** save costs by up to 50%.

## Terminology

* **Container Image**: Docker-compatible OCI image reference, supporting both public registries and private repositories with authentication.
* **Environment Variables**: Runtime configuration key-value pairs injected into containers for dynamic configuration and secrets management.
* **HTTP/TCP Ports**: Network endpoints exposed by containers for communication. HTTP ports (e.g., 80, 443) for web services, TCP ports for general network protocols.
* **Container Disk**: Root filesystem partition containing OS and system binaries. Mounted as read-write at container startup.
* **Volume Disk**: High-performance ephemeral storage directly attached to the GPU instance. Optimized for I/O intensive workloads but non-persistent across instance restarts.
* **Network Volume**: Network-attached storage service that allows users to access and manage data through a network. Data can be stored on remote servers and accessed from any device.

If you have any questions, you can first check the [FAQs for GPU Instance](/guides/faq#gpu-instance).


Built with [Mintlify](https://mintlify.com).