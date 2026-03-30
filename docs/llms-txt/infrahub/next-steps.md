# Source: https://docs.infrahub.app/overview/next-steps.md

# Next Steps

If you completed the [Quick Start](/overview/quickstart.md), you have a local Infrahub instance with a sample schema and some data. This page outlines the key steps to turn that into a proof of concept that demonstrates value to your organization.

## 1. Design your schema[​](#1-design-your-schema "Direct link to 1. Design your schema")

The Quick Start used pre-built schemas from the Schema Library. For a POC, model a slice of your actual infrastructure — the devices, services, or resources that matter most to your team.

Start with a focused scope. Pick one domain (for example: data center fabric, WAN sites, or firewall policies) and model it. You can always expand later. The [Schema Library](https://github.com/opsmill/schema-library) remains a good starting point to extend from.

[Create a schema../guides/create-schema](/guides/create-schema.md)

## 2. Load real data[​](#2-load-real-data "Direct link to 2. Load real data")

With a schema that reflects your infrastructure, bring in real data. If you already have a source of truth (Netbox, Nautobot, IP Fabric, or others), [Infrahub Sync](https://github.com/opsmill/infrahub-sync) can pull data from these systems directly.

Alternatively, describe your data in YAML object files and load them with `infrahubctl`, the same way you did in the Quick Start. This works well for initial seeding or for data that doesn't live in another system yet.

[Sync data from external systems../sync](/sync.md)

## 3. Connect a Git repository[​](#3-connect-a-git-repository "Direct link to 3. Connect a Git repository")

In the Quick Start, schemas and data files lived on your local machine. For a POC, store them in a Git repository and connect it to Infrahub. This unlocks Git-native workflows: Infrahub will sync branches, track changes, and consume files like Jinja2 templates and Python scripts directly from the repository.

Push the project created during the Quick Start to a remote repository (GitHub, GitLab, Bitbucket, etc.) and connect it through the UI or CLI.

[Connect a repository to Infrahub../guides/repository](/guides/repository.md)

## 4. Generate artifacts[​](#4-generate-artifacts "Direct link to 4. Generate artifacts")

Once you have real data and a connected repository, use Transformations to generate outputs from your data — device configurations, cabling plans, documentation, compliance reports, or anything else your team needs.

This is where Infrahub starts delivering tangible value: a single data change can regenerate all affected artifacts automatically.

[Generate artifacts../guides/artifact](/guides/artifact.md)

## 5. Deploy to a shared environment[​](#5-deploy-to-a-shared-environment "Direct link to 5. Deploy to a shared environment")

A local Docker setup works for development, but for a POC that involves your team, deploy Infrahub to a shared environment. Infrahub is packaged as Docker images and supports multiple deployment options:

* **Docker Compose** on a shared VM for quick team access
* **Kubernetes** via Helm Chart for production-grade deployments

[Installation guide../guides/installation](/guides/installation.md)

## Going further[​](#going-further "Direct link to Going further")

At this point, you have a running Infrahub instance with your own schema, real data, a connected Git repository, and generated artifacts. From here you can:

* [Build Generators](/guides/generator.md) to automate the creation of infrastructure objects from templates and business logic.
* [Set up events and webhooks](/guides/events-rules-actions.md) to trigger external systems when data changes.
* [Deploy artifacts with Ansible](/ansible.md) or [Nornir](/nornir.md) to push configurations to your infrastructure.

If you need guidance on which feature to explore next or how to implement a specific use case, reach out to the community on [Discord](https://discord.gg/opsmill) or book a meeting with OpsMill.

[Book a meeting with OpsMillhttps://cal.com/team/opsmill/meet](https://cal.com/team/opsmill/meet)
