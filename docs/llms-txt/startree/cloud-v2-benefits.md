# Source: https://docs.startree.ai/reference/cloud-v2-benefits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Benefits of StarTree V2 Cloud Architecture

Since the last couple years, we've evolved the StarTree Cloud architecture to enhance security, enable modular updates, and support faster feature iteration. This new architecture introduces several advancements, including improved security through our Uber Agent model, a centralized config-driven approach, and enhanced data plane features.

## Key Features

### Stronger Security

In the new design, we’re introducing a new component called *Uber Agent* that does most of the heavy lifting. Once deployed, the Uber agent can fetch the corresponding environment configuration from the control plane and take necessary actions.

* Uber agent does the heavy lifting and sits in the Data Plane
  * It pulls instructions and configs from control plane and do the needful
  * No inbound access needed for day-day managing the cluster

### Centralized Configs

All changes to an environment (including first deployment) now go through a “Config Service” hosted in the StarTree Control plane. There are well defined templates for various components which are under version control and managed in a centralized fashion. This makes it very easy for the StarTree Ops team to make changes, specify environment specific overrides - directly through our Admin portal. Each change is reviewed, versioned and safely applied. This avoids any manual tinkering in the customer environment.

* All changes versioned, audited, and templated
* Any customisation is auto synced with the dataplane
* No overrides of the configs going forward

### Safer upgrades

The new cloud architecture is more modular which also helps in upgrades, We can now update/upgrade individual components (Pinot, DM, Query console, Platform) in a safe manner. We’ve also improved the component release cadence across the entire fleet. For instance, Pinot, Data Manager and other software components can now be upgraded at a monthly cadence.

### Enhanced Automation

A lot of the routine operataional tasks are handled via automation with minimal human effort. This includes enhanced pre-checks on Pinot to catch any issues early on and not during the upgrades.

### Enhanced data plane features

In addition to changing the way infrastructure is deployed and managed, we’re also releasing new features in the data plane such as

* **Heterogeneous Pinot clusters**: We can now create multiple server pools in the same Pinot cluster with ease (each pool can be customized in terms of the instance SKU)
* **Secret management service**: store your credentials in a secure manner in standard systems (eg: AWS Secrets Manager) and reference it when creating datasets in StarTree Cloud
* **Graviton instance support**: New environments can now be configured with Graviton instances which are roughly 10-20% cheaper
* **Custom AMI support**
* **Custom Grafana Dashboards** and custom alert rules
* Support for **Kafka AZ awareness**
* **Workspaces** support: Users can now provision workspaces for ensuring logical separation of their Pinot cluster.

Built with [Mintlify](https://mintlify.com).
