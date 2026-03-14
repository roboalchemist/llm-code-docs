# Source: https://docs.anyscale.com/services.md

# What are Anyscale services?

[View Markdown](/services.md)

# What are Anyscale services?

Anyscale services deploy Ray Serve applications to production endpoints. Anyscale services offer additional benefits on top of Ray Serve, including high availability and zero-downtime upgrades.

## Best practices[​](#best-practices "Direct link to Best practices")

Anyscale recommends the following best practices when deploying services:

* Use zero-downtime incremental rollouts for model updates. See [Update an Anyscale service](/services/update.md).
* Deploy and manage up to 10 versions of a service behind a single endpoint for A/B testing and controlled rollouts. See [Deploy multiple versions of an Anyscale service](/services/versions.md).
* Enable high-throughput serving. See [High-throughput serving](/runtime/serve.md#high-throughput).
* Distribute replicas across nodes and availability zones for high reliability.
* Use spot instances for cost savings. See [Configure replica scaling for Anyscale services](/services/scale.md).
* Use head node fault tolerance. See [Configure head node fault tolerance](/administration/resource-management/head-node-fault-tolerance.md).
* Avoid scheduling on the head node. See [Control head node scheduling](/configuration/compute/advanced.md#head-node).
* Configure retries and timeouts to control latency and backpressure. See [Manage timeouts and retries for Anyscale services](/services/retries-timeouts.md).

## Permission requirements[​](#permissions "Direct link to Permission requirements")

You can optionally deploy an Anyscale cloud without permissions to deploy services, and you must opt-in to support head node fault tolerance for all cloud deployment options.

Cloud infrastructure to support Anyscale services uses the networking you configure while deploying your Anyscale cloud. Deploy a cloud with private networking if you need your load balancer to be private.

For Anyscale cloud resources using virtual machines, services require additional IAM permissions in your cloud provider account to configure a Redis in-memory store and load balancer. See IAM permissions for [AWS](/admin/cloud/configure-aws.md#minimal-iam) or [Google Cloud](/admin/cloud/configure-google-cloud.md).

The following table provides an overview of support for services with different cloud deployment options:

| Cloud deployment                                              | Deployment method         | Details                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Serverless Anyscale cloud (also called Anyscale-hosted cloud) | Deployed by default       | Enables services by default. No support for head node fault tolerance or private networking.                                                                                                                                                                                                                                           |
| Anyscale cloud on AWS                                         | `anyscale cloud setup`    | Enables services by default. Opt-in to head node fault tolerance using the `--enable-head-node-fault-tolerance` flag.                                                                                                                                                                                                                  |
| Anyscale cloud on AWS                                         | `anyscale cloud register` | You must configure IAM roles and a MemoryDB instance when deploying your cloud. Contact [Anyscale support](mailto:support@anyscale.com) for assistance customizing the [Anyscale Terraform modules for AWS](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules).                                               |
| Anyscale cloud on Google Cloud                                | `anyscale cloud setup`    | Enables services by default. Opt-in to head node fault tolerance using the `--enable-head-node-fault-tolerance` flag.                                                                                                                                                                                                                  |
| Anyscale cloud on Google Cloud                                | `anyscale cloud register` | You must configure service account roles and a Memorystore instance when deploying your cloud. Contact [Anyscale support](mailto:support@anyscale.com) for assistance customizing the [Anyscale Terraform modules for Google Cloud](https://github.com/anyscale/terraform-google-anyscale-cloudfoundation-modules).                    |
| Anyscale cloud on Kubernetes                                  | `anyscale cloud register` | You can't enable head node fault tolerance at the cloud level. You must configure `ray_gcs_external_storage_config` in each service config and provision your own Redis-compatible cluster. See [Manually configure fault tolerance for an Anyscale service](/administration/resource-management/head-node-fault-tolerance.md#manual). |

important

Anyscale clouds on AWS have changed default behavior for deploying Anyscale services.

Legacy Anyscale clouds on AWS use CloudFormation to configure Elastic Load Balancing for your service. Anyscale now directly configures Elastic Load Balancing for your services.

All new Anyscale clouds on AWS deployed with `anyscale cloud setup` use this configuration by default. You can run `anyscale cloud update` to upgrade your legacy AWS clouds deployed with `anyscale cloud setup` to the new behavior.

Anyscale has updated the [Anyscale Terraform modules for AWS](https://github.com/anyscale/terraform-aws-anyscale-cloudfoundation-modules) to provide the proper IAM permissions for the new default behavior. If you have a legacy Anyscale cloud deployed using `anyscale cloud register`, contact [Anyscale support](mailto:support@anyscale.com) for assistance updating your cloud IAM permissions.

See [Update your IAM role for services on Anyscale clouds on AWS](/services/cloudformation-eol.md).

## Capacity limit[​](#capacity-limit "Direct link to Capacity limit")

There's a quota of 20 running services per Anyscale cloud. A service can have many deployments and can scale to greater than 2000 nodes. If you need to increase your quota, contact [Anyscale support](mailto:support@anyscale.com).

## Pricing[​](#pricing "Direct link to Pricing")

Services use standard Anyscale pricing based on the type of machines used. See the [Anyscale pricing page](https://www.anyscale.com/pricing-detail).

In addition to Anyscale costs and virtual machine costs, Anyscale uses load balancer resources and a Redis-compatible in-memory store in your cloud provider account.

Use the following links to learn about pricing details for these services:

| Cloud        | Pricing links                                                                                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS          | - [Elastic Load Balancing Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/?nc=sn\&loc=3)<br />- [Memory DB Pricing](https://aws.amazon.com/memorydb/pricing/)                                        |
| Google Cloud | - [Load Balancing Pricing](https://console.cloud.google.com/marketplace/product/google-cloud-platform/cloud-load-balancing)<br />- [Memorystore Pricing](https://cloud.google.com/memorystore/docs/redis/pricing) |
