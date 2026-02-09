# Source: https://docs.datadoghq.com/security/workload_protection/setup/agent_variables.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/guide/agent_variables.md

---
title: Cloud Security Agent Variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Guides > Cloud
  Security Agent Variables
---

# Cloud Security Agent Variables

The Datadog Agent has several environment variables that can be enabled for Cloud Security. This article describes the purpose of each environment variable.

| Variable                                                    | Description                                                                                                                                                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_COMPLIANCE_CONFIG_ENABLED`                              | Enables the Cloud Security Posture Management (CSPM) Agent (runs in the Security Agent).                                                                                                                      |
| `DD_COMPLIANCE_CONFIG_HOST_BENCHMARKS_ENABLED`              | Enables CSPM host benchmarks. Requires the CSPM Agent (`DD_COMPLIANCE_CONFIG_ENABLED`).                                                                                                                       |
| `DD_RUNTIME_SECURITY_CONFIG_ENABLED`                        | Enables Cloud Workload Security (CWS). Must be enabled for both the System Probe and Security Agent.                                                                                                          |
| `DD_SYSTEM_PROBE_ENABLED`                                   | Enables the System Probe, which is an add-on Agent. Similar to the Trace Agent or Process Agent, it supports different functionalities than the vanilla Datadog Agent. It is primarily used with NPM and CWS. |
| `DD_RUNTIME_SECURITY_CONFIG_REMOTE  _CONFIGURATION_ENABLED` | Enables Remote Configuration for automatic updates of default Agent rules and automatic deployment of custom Agent rules.                                                                                     |
| `DD_SBOM_ENABLED`                                           | Enables the Software Bill of Materials (SBOM) collection subsystem.                                                                                                                                           |
| `DD_SBOM_CONTAINER_IMAGE_ENABLED`                           | Enables SBOM collection on container images.                                                                                                                                                                  |
| `DD_SBOM_HOST_ENABLED`                                      | Enables SBOM collection on hosts.                                                                                                                                                                             |
| `DD_SBOM_CONTAINER_IMAGE_CONTAINER_EXCLUDE`                 | Allows denylisting of specific containers from SBOM collection.                                                                                                                                               |
| `DD_SBOM_CONTAINER_IMAGE_CONTAINER_INCLUDE`                 | Allows allowlisting of specific containers in SBOM collection.                                                                                                                                                |
