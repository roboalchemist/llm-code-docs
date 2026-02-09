# Source: https://docs.datadoghq.com/getting_started/containers.md

# Source: https://docs.datadoghq.com/account_management/billing/containers.md

# Source: https://docs.datadoghq.com/api/latest/containers.md

# Source: https://docs.datadoghq.com/containers.md

---
title: Containers
description: Install & configure the Agent to collect data on containerized infrastructures
breadcrumbs: Docs > Containers
---

# Containers

To maintain the health, performance, and security of your containerized environments, you can install the Datadog Agent and use [Datadog Container Monitoring](https://app.datadoghq.com/containers).

## Get started{% #get-started %}

Log into Datadog and use the [Install Agents](https://app.datadoghq.com/fleet/install-agent/latest?platform=overview) page to install the Datadog Agent on your selected platform.

## Datadog Container Monitoring{% #datadog-container-monitoring %}

- [Containers Explorer: Use and configure Containers Explorer for real-time visibility into your containers.](https://docs.datadoghq.com/containers/monitoring/containers_explorer)
- [Container Images Explorer: Use and configure Containers Images Explorer to monitor the container](https://docs.datadoghq.com/containers/monitoring/container_images)
- [Kubernetes Explorer: Use the Kubernetes Explorer page to monitor your Kubernetes resources.](https://docs.datadoghq.com/containers/monitoring/kubernetes_explorer)
- [Configure Kubernetes Explorer: Configure the Kubernetes Explorer page.](https://docs.datadoghq.com/containers/monitoring/kubernetes_explorer_configuration)
- [Kubernetes Resource Utilization: Using and configuring the Kubernetes Resource Utilization page](https://docs.datadoghq.com/containers/monitoring/kubernetes_resource_utilization)
- [Kubernetes Autoscaling: Using and configuring Kubernetes Autoscaling](https://docs.datadoghq.com/containers/autoscaling)
- [Kubernetes Remediation: Using and configuring the Kubernetes Remediation page](https://docs.datadoghq.com/containers/bits_ai_kubernetes_remediation)
- [Amazon ECS Explorer: Using and configuring the ECS Explorer page](https://docs.datadoghq.com/containers/monitoring/amazon_elastic_container_explorer)

## Docker-based environments{% #docker-based-environments %}

- [Datadog Docker Agent: Install and configure the Datadog Docker Agent for Docker, containerd, and Podman runtimes](https://docs.datadoghq.com/containers/docker)
- [APM: Configure APM trace collection for applications running in Docker containers using the Datadog Agent](https://docs.datadoghq.com/containers/docker/apm)
- [Log collection: Configure log collection for applications running in Docker containers using the Datadog Agent](https://docs.datadoghq.com/containers/docker/log)
- [Tag extraction: Configure automatic tag extraction from Docker container labels and environment variables](https://docs.datadoghq.com/containers/docker/tag)
- [Integrations: Configure monitoring integrations for applications running in Docker containers using Autodiscovery](https://docs.datadoghq.com/containers/docker/integrations)
- [Prometheus: Collect Prometheus and OpenMetrics metrics from containerized Docker applications using the Datadog Agent](https://docs.datadoghq.com/containers/docker/prometheus)
- [Data Collected: Reference guide for metrics and events collected by the Datadog Agent from Docker containers](https://docs.datadoghq.com/containers/docker/data_collected)

## Kubernetes environments{% #kubernetes-environments %}

- [Kubernetes: Install and configure the Datadog Agent on Kubernetes](https://docs.datadoghq.com/containers/kubernetes)
- [Installation: Install and configure the Datadog Agent on Kubernetes using the Datadog Operator, Helm, or kubectl](https://docs.datadoghq.com/containers/kubernetes/installation)
- [Further Configuration: Additional configuration options for APM, logs, processes, events, and other capabilities after installing the Datadog Agent](https://docs.datadoghq.com/containers/kubernetes/configuration)
- [Distributions: Platform-specific installation and configuration instructions for Datadog Agent on various Kubernetes distributions](https://docs.datadoghq.com/containers/kubernetes/distributions)
- [APM: Enable APM trace collection for containerized applications running in Kubernetes environments](https://docs.datadoghq.com/containers/kubernetes/apm)
- [App and API Protection: Automatically enable App and API Protection for your Kubernetes ingress proxies and gateways](https://docs.datadoghq.com/containers/kubernetes/appsec)
- [Log collection: Configure log collection from containerized applications running on Kubernetes using the Datadog Agent](https://docs.datadoghq.com/containers/kubernetes/log)
- [Tag extraction: Configure automatic tag extraction from Kubernetes pod labels and annotations for enhanced monitoring](https://docs.datadoghq.com/containers/kubernetes/tag)
- [Integrations: Configure monitoring integrations for applications running in Kubernetes using Autodiscovery templates](https://docs.datadoghq.com/containers/kubernetes/integrations)
- [Prometheus & OpenMetrics: Collect Prometheus and OpenMetrics from Kubernetes workloads using the Datadog Agent with Autodiscovery](https://docs.datadoghq.com/containers/kubernetes/prometheus)
- [Control plane monitoring: Monitor Kubernetes control plane components including API server, etcd, controller manager, and scheduler](https://docs.datadoghq.com/containers/kubernetes/control_plane)
- [Data collected: Reference guide for metrics and events collected by the Datadog Agent from Kubernetes clusters](https://docs.datadoghq.com/containers/kubernetes/data_collected)
- [kubectl Plugin: The`kubectl`plugin for the Datadog Operator, which provides a set of helper utilities that give visibility into certain internal components.](https://docs.datadoghq.com/containers/kubernetes/kubectl_plugin)
- [Datadog CSI Driver: Observability for secure Kubernetes environments using the Datadog CSI Driver](https://docs.datadoghq.com/containers/kubernetes/csi_driver)
- [Data security: Information about the security of Kubernetes data sent to Datadog](https://docs.datadoghq.com/data_security/kubernetes/)

- [Cluster Agent for Kubernetes: Centralized approach to collecting cluster-level monitoring data with the Datadog Cluster Agent](https://docs.datadoghq.com/containers/cluster_agent)
- [Datadog Operator: Deploy and manage the Datadog Agent on Kubernetes using the Datadog Operator](https://docs.datadoghq.com/containers/datadog_operator)

## Amazon ECS{% #amazon-ecs %}

- [Amazon ECS: Install and configure the Datadog Agent on Amazon Elastic Container Service](https://docs.datadoghq.com/containers/amazon_ecs)
- [Tracing ECS Applications: Configure APM trace collection for containerized applications running on Amazon ECS](https://docs.datadoghq.com/containers/amazon_ecs/apm)
- [Log collection: Configure log collection from containerized applications running on Amazon ECS using the Datadog Agent](https://docs.datadoghq.com/containers/amazon_ecs/logs)
- [Tag extraction: Configure automatic tag extraction from container labels and environment variables in Amazon ECS](https://docs.datadoghq.com/containers/amazon_ecs/tags)
- [Data collection: Reference guide for metrics, logs, and events collected by the Datadog Agent on Amazon ECS](https://docs.datadoghq.com/containers/amazon_ecs/data_collected)
- [Managed Instances: Install and configure the Datadog Agent on Amazon ECS Managed Instances](https://docs.datadoghq.com/containers/amazon_ecs/managed_instances)
- [AWS Fargate with ECS: Monitor AWS Fargate for Amazon ECS](https://docs.datadoghq.com/integrations/ecs_fargate)

## Miscellaneous{% #miscellaneous %}

- [Container Troubleshooting: Troubleshooting containers-related issues](https://docs.datadoghq.com/containers/troubleshooting)
- [Container Guides: List of guides for container monitoring setup and configuration](https://docs.datadoghq.com/containers/guide)

## Further reading{% #further-reading %}

- [Datadog's Annual State of Containers Report](https://www.datadoghq.com/container-report/)
