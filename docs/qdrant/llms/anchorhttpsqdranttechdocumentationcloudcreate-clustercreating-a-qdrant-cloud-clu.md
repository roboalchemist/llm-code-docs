# [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#creating-a-qdrant-cloud-cluster) Creating a Qdrant Cloud Cluster

Qdrant Cloud offers two types of clusters: **Free** and **Standard**.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#free-clusters) Free Clusters

Free tier clusters are perfect for prototyping and testing. You don’t need a credit card to join.

A free tier cluster only includes 1 single node with the following resources:

| Resource | Value |
| --- | --- |
| RAM | 1 GB |
| vCPU | 0.5 |
| Disk space | 4 GB |
| Nodes | 1 |

This configuration supports serving about 1 M vectors of 768 dimensions. To calculate your needs, refer to our documentation on [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/).

The choice of cloud providers and regions is limited.

It includes:

- Standard Support
- Basic monitoring
- Basic log access
- Basic alerting
- Version upgrades with downtime
- Only manual snapshots and restores via API
- No dedicated resources

If unused, free tier clusters are automatically suspended after 1 week, and deleted after 4 weeks of inactivity if not reactivated.

You can always upgrade to a standard cluster with more resources and features.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#standard-clusters) Standard Clusters

On top of the Free cluster features, Standard clusters offer:

- Response time and uptime SLAs
- Dedicated resources
- Backup and disaster recovery
- Multi-node clusters for high availability
- Horizontal and vertical scaling
- Monitoring and log management
- Zero-downtime upgrades for multi-node clusters with replication

You have a broad choice of regions on AWS, Azure and Google Cloud.

For payment information see [**Pricing and Payments**](https://qdrant.tech/documentation/cloud/pricing-payments/).

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#create-a-cluster) Create a Cluster

![Create Cluster Page](https://qdrant.tech/documentation/cloud/create-cluster.png)

This page shows you how to use the Qdrant Cloud Console to create a custom Qdrant Cloud cluster.

> **Prerequisite:** Please make sure you have provided billing information before creating a custom cluster.

01. Start in the **Clusters** section of the [Cloud Dashboard](https://cloud.qdrant.io/).

02. Select **Clusters** and then click **\+ Create**.

03. In the **Create a cluster** screen select **Free** or **Standard**
    Most of the remaining configuration options are only available for standard clusters.

04. Select a provider. Currently, you can deploy to:

    - Amazon Web Services (AWS)
    - Google Cloud Platform (GCP)
    - Microsoft Azure
    - Your own [Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) Infrastructure
05. Choose your data center region or Hybrid Cloud environment.

06. Configure RAM for each node.


    > For more information, see our [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/) guidance.

07. Choose the number of vCPUs per node. If you add more
    RAM, the menu provides different options for vCPUs.

08. Select the number of nodes you want the cluster to be deployed on.


    > Each node is automatically attached with a disk, that has enough space to store data with Qdrant’s default collection configuration.

09. Select additional disk space for your deployment.


    > Depending on your collection configuration, you may need more disk space per RAM. For example, if you configure `on_disk: true` and only use RAM for caching.

10. Review your cluster configuration and pricing.

11. When you’re ready, select **Create**. It takes some time to provision your cluster.


Once provisioned, you can access your cluster on ports 443 and 6333 (REST) and 6334 (gRPC).

![Cluster configured in the UI](https://qdrant.tech/documentation/cloud/cluster-detail.png)

You should now see the new cluster in the **Clusters** menu.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#deleting-a-cluster) Deleting a Cluster

You can delete a Qdrant database cluster from the cluster’s detail page.

![Delete Cluster](https://qdrant.tech/documentation/cloud/delete-cluster.png)

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#next-steps) Next Steps

You will need to connect to your new Qdrant Cloud cluster. Follow [**Authentication**](https://qdrant.tech/documentation/cloud/authentication/) to create one or more API keys.

You can also scale your cluster both horizontally and vertically. Read more in [**Cluster Scaling**](https://qdrant.tech/documentation/cloud/cluster-scaling/).

If a new Qdrant version becomes available, you can upgrade your cluster. See [**Cluster Upgrades**](https://qdrant.tech/documentation/cloud/cluster-upgrades/).

For more information on creating and restoring backups of a cluster, see [**Backups**](https://qdrant.tech/documentation/cloud/backups/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/create-cluster.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/create-cluster.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-155-lllmstxt|>
## running-with-gpu
- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Running with GPU