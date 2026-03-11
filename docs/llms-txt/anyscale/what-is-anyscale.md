# Source: https://docs.anyscale.com/get-started/what-is-anyscale.md

# What is Anyscale?

[View Markdown](/get-started/what-is-anyscale.md)

# What is Anyscale?

Anyscale is a unified AI platform from the creators of Ray. Anyscale adds optimizations, observability, data governance, and developer tooling that make it the best place to run Ray workloads. This page provides an overview of how Anyscale can accelerate and simplify getting AI and ML workloads into production at scale.

Anyscale uses a consumption-based model to manage Ray clusters configured with the Anyscale Runtime. Anyscale also offers additional paid professional services including customized training and dedicated support. See [Anyscale pricing](https://www.anyscale.com/pricing).

If you're new to Ray, see [What is Ray?](/get-started/what-is-ray.md).

Anyscale workloads use an optimized version of Ray known as the Anyscale Runtime. See [What is the Anyscale Runtime?](/runtime.md).

## Deploy and manage Ray clusters[​](#clusters "Direct link to Deploy and manage Ray clusters")

Anyscale helps you launch and manage Ray clusters of any size using resources in your cloud provider of choice. You deploy an Anyscale cloud to configure access to resources on AWS, Azure, Google Cloud, or Kubernetes. See [Introduction to Anyscale clouds](/admin/cloud.md).

Compute configuration is highly customizable, and allows you to take advantage of your existing infrastructure and compute, including the following features:

* Deploy to on-prem or cloud-hosted Kubernetes clusters.
* Leverage virtual machine reservations in your cloud provider.
* Create clusters that combine CPUs and GPUs of varying sizes.
* Assign priority and preemption rules for Ray workloads, including the ability to schedule components of your workloads to certain worker nodes.
* Auto-scale Ray clusters by worker type, including adding new nodes to Kubernetes clusters or adding on-demand virtual machines to your reserved instances.

When you launch a cluster, Anyscale builds and caches an optimized version of your container image. This cached image allows Anyscale to rapidly add new nodes to your cluster when needed. This allows for efficient upscaling, aggressive downscaling, and the ability to use spot instances with fallback.

You use container images and compute configs when configuring clusters for workspaces, jobs, and services. The Anyscale console provides interfaces for defining and managing custom container images and compute configs. See [Define a Ray cluster](/configuration.md).

## Secure and share Ray workloads[​](#governance "Direct link to Secure and share Ray workloads")

Anyscale allows you to manage, observe, and share Ray workloads deployed across multiple cloud providers on VMs or Kubernetes from a single organization. Admins can restrict access to clouds or projects, ensuring that the right users can view, monitor, and run workloads in the correct cloud environments. Use [SSO](/administration/organization/configure-sso.md) to manage logins and restrict access to users still active in your identity provider of choice. See [Anyscale organization overview](/get-started/org-overview.md).

Anyscale uses a [shared responsibility model](/administration/security-and-compliance/shared-responsibility-model.md), where you configure identity and access management policies to allow Anyscale to deploy and manage cloud infrastructure in your cloud provider of choice. Your data stays in your cloud storage and compute in the regions of your choice.

Anyscale has certified compliance with SOC 2 Type 2. Learn more about security from the [Anyscale Trust Center](https://trust.anyscale.com/).

For a complete overview of admin tasks and features on Anyscale, see [Anyscale for admins](/administration/overview.md).

## Develop on Anyscale[​](#workspaces "Direct link to Develop on Anyscale")

The Anyscale console includes numerous features for accelerating developer workflows. Many of these features center on Anyscale workspaces for interactive development against Ray clusters.

Workspaces provide a hosted VS Code, Jupyter Lab, and web terminal for a similar developer experience to programming in virtual environments or cloud VMs. You can also connect IDEs such as VS Code and Cursor to your Anyscale workspace to run code directly in a containerized environment from your local machine.

The Anyscale console provides a graphical user interface for writing code, managing files, running applications, configuring dependencies, and monitoring logs and metrics for your workload. See [Workspaces](/platform/workspaces.md).

You can directly launch jobs or services from an Anyscale workspace, accelerating testing on the way to deploying code in production. See [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md).

Because workspaces, jobs, and services use the same basic configurations and options, you can quickly package your code and dependencies and move from interactive development to production. See [Develop Anyscale applications](/development.md).

Anyscale provides a complete CLI and SDK for developers who prefer to develop code locally. See [Anyscale API reference](/reference.md).

## Run data processing and ML training jobs[​](#jobs "Direct link to Run data processing and ML training jobs")

Use Anyscale jobs to submit production Ray applications for workloads such as batch inference, model training, and data processing. See [What are Anyscale jobs?](/jobs.md).

You use the CLI or SDK to trigger jobs manually, or you can use the same tools to automate Anyscale jobs using CI/CD or scheduling tools. See [Job API Reference](/reference/job-api.md).

Use [job queues](/jobs/queues.md) to enable multiple workloads to share compute resources, or use [job schedules](/jobs/schedules.md) for workloads that need to run on a fixed cadence.

## Serve AI models at scale[​](#services "Direct link to Serve AI models at scale")

Anyscale services provide a managed solution for hosting and serving ML and AI models to power production applications.

Anyscale services are an extension of Ray Serve that provide zero downtime upgrades and high availability. You can host multiple models on shared infrastructure and dynamically scale cluster size to meet serving demands. See [What are Anyscale services?](/services.md).

## Monitor and debug Ray workloads[​](#observability "Direct link to Monitor and debug Ray workloads")

Anyscale offers robust monitoring and logging tools for observability and debugging your Ray workloads. See [Monitor and debug Anyscale workloads](/monitoring.md)

Anyscale includes high-level dashboards to observe all workspace, jobs, and services in an Anyscale cloud. You can use these dashboards to identify underutilized resources and navigate to individual Ray clusters to get more granular details.

For all Ray clusters on Anyscale, you have access to built-in metrics and logs and the ability to define custom metrics and logs. You can view logs and metrics using built-in tools or configure integrations with third party tools.

Anyscale workspaces and jobs provide additional insights with granular metrics and logging for Ray Data and Ray Train. See [Workload dashboards](/monitoring/workload-debugging.md).

Anyscale services provide metrics about Ray Serve, including CPU profiling and node-level monitoring for your Ray cluster. See [Monitor a service](/services/monitoring.md).

## Get support from the creators of Ray[​](#support "Direct link to Get support from the creators of Ray")

Anyscale customers can elect to enroll in an [Anyscale support offering](https://www.anyscale.com/support), gaining access to support SLAs, dedicated Slack channels, and other benefits.

Use the **Help** portal in the Anyscale product to submit feedback and bug reports and access other help resources. You can also [contact Anyscale support using email](mailto:support@anyscale.com).

You can [join the official Ray Slack](https://www.ray.io/join-slack). Use the `#anyscale-support` channel to ask questions about Anyscale if you don't have a support subscription that includes a dedicated Slack channel.
