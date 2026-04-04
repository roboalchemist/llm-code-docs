# Source: https://docs.zenml.io/pro/deployments/scenarios/saas-deployment.md

# SaaS

ZenML Pro SaaS is the fastest and easiest way to get started with enterprise-grade MLOps. With zero infrastructure setup required, you can be running production pipelines within minutes while maintaining full control over your data and compute resources.

{% hint style="info" %}
To get access to ZenML Pro, [book a call](https://www.zenml.io/book-your-demo).
{% endhint %}

## Overview

In a SaaS deployment, ZenML manages all server infrastructure while your sensitive data and compute resources remain in your own cloud environment. This architecture provides the fastest time-to-value while maintaining data sovereignty for your ML workloads.

![ZenML Pro SaaS deployment architecture](https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-af36262b2904af6d61af854f044fa903809a2380%2Fcloud_architecture_scenario_1.png?alt=media)

## Architecture

### What Runs Where

| Component         | Location                                                           | Purpose                                                        |
| ----------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| ZenML Pro Server  | ZenML Infrastructure                                               | Manages pipeline orchestration and metadata                    |
| Pro Control Plane | ZenML Infrastructure                                               | Handles authentication, RBAC, and workspace management         |
| Metadata Store    | ZenML Infrastructure                                               | Stores pipeline runs, model metadata, and tracking information |
| Secrets Store     | ZenML Infrastructure (default)                                     | Stores credentials for accessing your infrastructure           |
| Compute Resources | Your infrastructure through [stacks](https://docs.zenml.io/stacks) | Executes pipeline steps and training jobs                      |
| Data & Artifacts  | Your infrastructure through [stacks](https://docs.zenml.io/stacks) | Stores datasets, models, and pipeline artifacts                |

## Key Benefits

### Fastest Setup

Get to production in minutes rather than weeks. There's no infrastructure provisioning required for ZenML services—updates and patches are handled automatically, and the infrastructure scales with your needs without any manual intervention.

### Security & Compliance

ZenML Pro SaaS is SOC 2 Type II and ISO 27001 certified. Your ML data stays in your infrastructure, maintaining data sovereignty, while all communications are encrypted in transit. If needed, you can optionally use your own secret management solution instead of the ZenML-managed one.

### Production Ready from Day 1

The platform comes with built-in redundancy and failover for high availability. Metadata is backed up continuously, health checks and alerting are pre-configured, and you get direct access to ZenML engineers through professional support.

### Collaboration Features

ZenML Pro SaaS supports full team collaboration with multi-user capabilities. You can connect your identity provider through SSO integration, manage granular permissions with role-based access control, and organize teams and resources using workspaces and projects.

## Ideal Use Cases

ZenML Pro SaaS works well for startups and scale-ups that need production MLOps quickly without infrastructure overhead, as well as teams without dedicated DevOps who want managed infrastructure and support. It's also a good fit for organizations with existing cloud infrastructure that are comfortable with SaaS tools, teams prioritizing velocity over complete infrastructure control, and POC or pilot projects that need to demonstrate value quickly.

## Secret Management Options

### Default: ZenML-Managed Secrets Store

By default, ZenML Pro SaaS stores your cloud credentials securely in our managed secrets store. This requires zero configuration and provides automatic encryption at rest and in transit, with access controls managed via RBAC.

### Alternative: Customer-Managed Secrets Store

For organizations with strict security requirements, you can configure ZenML to use your own [secrets management](https://github.com/zenml-io/zenml/blob/main/docs/book/getting-started/deploying-zenml/secret-management.md) solution such as AWS Secrets Manager, Google Cloud Secret Manager, Azure Key Vault, or HashiCorp Vault.

![SaaS with customer secret store](https://884225131-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FoT4CiM88wQeSLTcwLU2J%2Fuploads%2Fgit-blob-eda040d58a553bde9dc9ddb3a4e7502cecd02a62%2Fcloud_architecture_saas_detailed_2.png?alt=media)

This keeps all credentials within your infrastructure while still benefiting from managed ZenML services. [Book a call](https://www.zenml.io/book-your-demo) with us if you want this set up.

## Network Architecture

### Core Platform

ZenML Pro SaaS requires no inbound connectivity into your infrastructure. All communication is initiated from your environment to ZenML, keeping your systems protected behind your firewall.

### Features Requiring Limited Ingress

Some features require you to whitelist ZenML to access specific resources in your environment. These include artifact visualizations (which need limited access to your artifact store), step logs (which need limited access to your artifact store or log collector), and running Snapshots (which relies on limited access to your orchestration environment). You control this access by configuring appropriate cloud IAM permissions.

## Getting Started

Start by [booking a demo](https://www.zenml.io/book-your-demo) to get access to ZenML Pro SaaS. Once your account is set up, connect your cloud infrastructure by configuring an artifact store (S3, GCS, Azure Blob, etc.), setting up compute resources (AWS, GCP, Azure, or Kubernetes), and providing the necessary credentials via secrets. After that, you're ready to run your pipelines and monitor them through the dashboard.

## Pricing & Support

ZenML Pro SaaS includes managed infrastructure and updates, professional support with SLA, regular security patches, and access to pro-exclusive features. Pricing follows a usage-based model. [Contact us](https://www.zenml.io/book-your-demo) for pricing details and custom plans.

## Comparison with Other Deployments

| Feature                | SaaS               | Hybrid SaaS           | Self-hosted          |
| ---------------------- | ------------------ | --------------------- | -------------------- |
| Setup Time             | Minutes            | Hours                 | Days                 |
| Maintenance            | Zero               | Workspace only        | Full stack           |
| Infrastructure Control | Minimal            | Moderate              | Complete             |
| Data Sovereignty       | Metadata on ZenML  | Full                  | Full                 |
| Best For               | Fast time-to-value | Security requirements | Strictest compliance |

[Compare all deployment options →](https://docs.zenml.io/pro/deployments/scenarios)

## Migration Path

Already running ZenML OSS? Migrating to SaaS is possible with the assistance of the ZenML support team. Reach out to us at <hello@zenml.io> or on [Slack](https://zenml.io/slack) to learn more.

## Related Resources

* [System Architecture](https://docs.zenml.io/pro/system-architecture)
* [Scenarios](https://docs.zenml.io/pro/deployments/scenarios)
* [Hybrid SaaS Deployment](https://docs.zenml.io/pro/deployments/scenarios/hybrid-deployment)
* [Self-hosted Deployment](https://docs.zenml.io/pro/deployments/scenarios/self-hosted-deployment)
* [Configuration Details](https://docs.zenml.io/pro/manage/configuration-details)
* [Upgrades and Updates](https://docs.zenml.io/pro/manage/upgrades-updates)

## Get Started

Ready to get started with ZenML Pro SaaS? [Book a Demo](https://www.zenml.io/book-your-demo) or [contact us](mailto:cloud@zenml.io) with questions.
