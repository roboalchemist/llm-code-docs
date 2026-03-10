# Source: https://docs.aws.amazon.com/msk/latest/developerguide/llms.txt

# Amazon Managed Streaming for Apache Kafka Developer Guide

> Developer guide for Amazon Managed Streaming for Apache Kafka.

- [Welcome](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [Setting up](https://docs.aws.amazon.com/msk/latest/developerguide/before-you-begin.html)
- [Quota](https://docs.aws.amazon.com/msk/latest/developerguide/limits.html)
- [Document history](https://docs.aws.amazon.com/msk/latest/developerguide/doc-history.html)

## [MSK Provisioned](https://docs.aws.amazon.com/msk/latest/developerguide/msk-provisioned.html)

### [Get started](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)

Get up and running with Amazon MSK.

- [Create a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster.html): Create an MSK cluster using the AWS Management Console.
- [Create an IAM role](https://docs.aws.amazon.com/msk/latest/developerguide/create-client-iam-role.html): Create an IAM policy that grants access to create topics on the cluster and to send data to those topics.
- [Create a client machine](https://docs.aws.amazon.com/msk/latest/developerguide/create-client-machine.html): Create a client machine for creating an Apache Kafka topic and for producing and consuming data in Amazon MSK.
- [Create a topic](https://docs.aws.amazon.com/msk/latest/developerguide/create-topic.html): Create a topic in your newly created MSK cluster.
- [Produce and consume data](https://docs.aws.amazon.com/msk/latest/developerguide/produce-consume.html): Produce and consume data.
- [View metrics](https://docs.aws.amazon.com/msk/latest/developerguide/view-metrics.html): View the metrics for your MSK cluster using CloudWatch.
- [Delete the tutorial resources](https://docs.aws.amazon.com/msk/latest/developerguide/delete-cluster.html): Delete the resources that you created for this tutorial.

### [How it works](https://docs.aws.amazon.com/msk/latest/developerguide/msk-cluster-management.html)

Common Amazon MSK operations.

### [Create a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster.html)

Create an MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [Create a cluster using AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster-console.html): The procedures in this topic describe the common task of creating an MSK Provisioned cluster using the Custom create option in the AWS Management Console.
- [Create a provisioned Amazon MSK cluster using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster-cli.html): This process describes the common task of creating an MSK Provisioned cluster using the AWS CLI.
- [Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster-cli-custom-config.html): This process describes the common task of creating an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI.
- [Create an MSK Provisioned cluster using the Amazon MSK API](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster-api.html): This process describes the common task of creating and MSK Provisioned cluster using the API.

### [List clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-clusters.html)

List all clusters in your account using the AWS Management Console, the AWS CLI, or the API.

- [List clusters using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/list-clusters-console.html): To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon Resource Name (ARN).
- [List clusters using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/list-clusters-cli.html): To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon Resource Name (ARN).
- [List clusters using the API](https://docs.aws.amazon.com/msk/latest/developerguide/list-clusters-api.html): To get a bootstrap broker for an Amazon MSK cluster, you need the cluster Amazon Resource Name (ARN).

### [Connect to an MSK Provisioned cluster](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html)

How to connect to your MSK Provisioned cluster from client machines.

- [Turn on public access](https://docs.aws.amazon.com/msk/latest/developerguide/public-access.html): Amazon MSK gives you the option to turn on public access to the brokers of MSK Provisioned clusters running Apache Kafka 2.6.0 or later versions.

### [Access from within AWS](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access.html)

To connect to an MSK cluster from inside AWS but outside the cluster's Amazon VPC, the following options exist.

### [Multi-VPC private connectivity in a single Region](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access-mult-vpc.html)

Multi-VPC private connectivity for cross-account clients in the same Region.

### [Multi-VPC get started tutorial](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-getting-started.html)

Step-by-step use case for setting up multi-VPC private connectivity

- [Cluster owner turns on multi-VPC](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cluster-owner-action-turn-on.html): The MSK cluster owner needs to make configuration settings on the MSK cluster after the cluster is created and in an ACTIVE state.
- [Cluster owner attaches cluster policy](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cluster-owner-action-policy.html): The cluster owner can attach a cluster policy (also known as a resource-based policy) to the MSK cluster where you will turn on multi-VPC private connectivity.
- [Cross-account user configures VPC connections](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-user-action.html): To set up multi-VPC private connectivity between a client in a different account from the MSK cluster, the cross-account user creates a managed VPC connection for the client.
- [Update auth schemes on a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-update-authschemes.html): Multi-VPC private connectivity supports several authorization schemes: SASL/SCRAM, IAM, and TLS.
- [Reject managed VPC connection](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-reject-connection.html): From the Amazon MSK console on the cluster admin account, you can reject a client VPC connection.
- [Delete managed VPC connection](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-delete-connection.html): The cross-account user can delete a managed VPC connection for an MSK cluster from the client account console.
- [Multi-VPC private connectivity permissions](https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-permissions.html): This section summarizes the permissions needed for clients and clusters using the multi-VPC private connectivity feature.
- [Port information](https://docs.aws.amazon.com/msk/latest/developerguide/port-info.html): Use the following port numbers so that Amazon MSK can communicate with client machines:

### [Get the bootstrap brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html)

Get the bootstrap brokers for your cluster using the AWS Management Console, the AWS CLI, or the API.

- [Get the bootstrap brokers using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/get-bootstrap-console.html): This process describes how to get bootstrap brokers for a cluster using the AWS Management Console.
- [Get the bootstrap brokers using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/get-bootstrap-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) that you obtained when you created your cluster.
- [Get the bootstrap brokers using the API](https://docs.aws.amazon.com/msk/latest/developerguide/get-bootstrap-api.html): To get the bootstrap brokers using the API, see GetBootstrapBrokers.

### [Monitor a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)

Learn how to monitor your Amazon MSK Provisioned cluster.

- [View metrics using CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/cloudwatch-metrics.html): You can monitor metrics for Amazon MSK using the CloudWatch console, the command line, or the CloudWatch API.

### [CloudWatch metrics for Standard brokers](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html)

Amazon MSK integrates with Amazon CloudWatch so that you can collect, view, and analyze CloudWatch metrics for your MSK Standard brokers.

- [MSK Provisioned cluster states](https://docs.aws.amazon.com/msk/latest/developerguide/msk-cluster-states.html): The following table shows the possible states of a MSK Provisioned cluster and describes what they mean.
- [CloudWatch metrics for Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details-express.html): Amazon MSK integrates with CloudWatch so that you can collect, view, and analyze CloudWatch metrics for your MSK Express brokers.

### [Monitor with Prometheus](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html)

You can monitor your MSK Provisioned cluster with Prometheus, an open-source monitoring system for time-series metric data.

- [Enable open monitoring on new clusters](https://docs.aws.amazon.com/msk/latest/developerguide/enable-open-monitoring-at-creation.html): This procedure describes how to enable open monitoring on a new MSK cluster using the AWS Management Console, the AWS CLI, or the Amazon MSK API.
- [Enable open monitoring on existing Provisioned clusters](https://docs.aws.amazon.com/msk/latest/developerguide/enable-open-monitoring-after-creation.html): To enable open monitoring, make sure that the MSK Provisioned cluster is in the ACTIVE state.
- [Set up a Prometheus host](https://docs.aws.amazon.com/msk/latest/developerguide/set-up-prometheus-host.html): This procedure describes how to set up a Prometheus host using a prometheus.yml file.
- [Use Prometheus metrics](https://docs.aws.amazon.com/msk/latest/developerguide/prometheus-metrics.html): All metrics emitted by Apache Kafka to JMX are accessible using open monitoring with Prometheus.
- [Store Prometheus metrics](https://docs.aws.amazon.com/msk/latest/developerguide/managed-service-prometheus.html): Amazon Managed Service for Prometheus is a Prometheus-compatible monitoring and alerting service that you can use to monitor Amazon MSK clusters.
- [Monitor consumer lags](https://docs.aws.amazon.com/msk/latest/developerguide/consumer-lag.html): Monitoring consumer lag allows you to identify slow or stuck consumers that aren't keeping up with the latest data available in a topic.
- [Use storage capacity alerts](https://docs.aws.amazon.com/msk/latest/developerguide/cluster-alerts.html): On Amazon MSK provisioned clusters, you choose the cluster's primary storage capacity.

### [Update cluster security](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html)

Update the authentication and encryption settings for an existing Amazon MSK cluster using the AWS Management Console, the AWS CLI, or the API.

- [Update cluster security settings using console](https://docs.aws.amazon.com/msk/latest/developerguide/update-security-console.html): Describes how to updated Amazon MSK cluster security settings using the AWS Management Console.
- [Update cluster security settings using CLI](https://docs.aws.amazon.com/msk/latest/developerguide/update-security-cli.html): Describes how to updated Amazon MSK cluster security settings using the AWS CLI.
- [Update cluster security settings using API](https://docs.aws.amazon.com/msk/latest/developerguide/update-security-api.html): Describes how to updated Amazon MSK cluster security settings using the API.
- [Expand a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-broker-count.html): Increase the number of brokers in an Amazon MSK cluster using the AWS Management Console, the AWS CLI, or the API.
- [Remove a broker](https://docs.aws.amazon.com/msk/latest/developerguide/msk-remove-broker.html): Increase the number of brokers in an Amazon MSK cluster using the AWS Management Console, the AWS CLI, or the API.
- [Update cluster broker size](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-broker-type.html): Update the Amazon MSK cluster broker size for all the brokers in the cluster using the AWS Management Console, the AWS CLI, or the API.
- [Use Cruise Control](https://docs.aws.amazon.com/msk/latest/developerguide/cruise-control.html): How to use Cruise Control to rebalance and monitor your Amazon MSK cluster.
- [Update cluster configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-cluster-config.html): Update the configuration of a Amazon MSK clustercluster.
- [Configure dual-stack network type](https://docs.aws.amazon.com/msk/latest/developerguide/mskp-choose-cluster-network-type.html): Configure IPv4 or dual-stack network type for your MSK Provisioned clusters.
- [Reboot a broker for an Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-reboot-broker.html): Reboot a broker for an Amazon MSK cluster using the AWS Management Console, the AWS CLI, or the API.

### [Tag a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging.html)

Assign your own metadata tags to your Amazon MSK resources (such as clusters) to help you manage them.

- [Tag basics for clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging-basics.html): Assign your own metadata tags to your Amazon MSK resources (such as clusters) to help you manage them.
- [Track costs](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging-billing.html): Assign your own metadata tags to your Amazon MSK resources, such as clusters, to help you manage them.
- [Tag restrictions](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging-restrictions.html): Assign your own metadata tags to your Amazon MSK resources, such as clusters, to help you manage them.
- [Tag resources using API](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging-howto.html): Describes API operations to tag or untag an Amazon MSK resource or list the current set of tags.
- [Migrate to MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/migration.html): Explore cluster migration options using Amazon MSK Replicator and Apache MirrorMaker 2.0.

### [Delete a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-delete-cluster.html)

Delete an Amazon MSK cluster using the AWS Management Console, the AWS CLI, or the API.

- [Delete an Amazon MSK Provisioned cluster using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/delete-cluster-console.html): This process describes how to delete an Amazon MSK Provisioned cluster using the AWS Management Console.
- [Delete an Amazon MSK Provisioned cluster using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/delete-cluster-cli.html): This process describes how to delete an MSK Provisioned cluster using the AWS CLI.
- [Delete an Amazon MSK Provisioned cluster using the API](https://docs.aws.amazon.com/msk/latest/developerguide/delete-cluster-api.html): The Amazon MSK API allows you to programmatically create and manage your MSK Provisioned cluster as part of automated infrastructure provisioning or deployment scripts.

### [Key features and concepts](https://docs.aws.amazon.com/msk/latest/developerguide/operations.html)

Amazon MSK key features and concepts explanations and reference material.

### [Broker types](https://docs.aws.amazon.com/msk/latest/developerguide/broker-instance-types.html)

MSK Provisioned offers two broker types - Standard and Express.

- [Standard brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-broker-types-standard.html): Standard brokers for MSK Provisioned offer the most flexibility to configure your cluster's performance.
- [Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-broker-types-express.html): Express brokers for MSK Provisioned make Apache Kafka simpler to manage, more cost-effective to run at scale, and more elastic with the low latency you expect.
- [Broker sizes](https://docs.aws.amazon.com/msk/latest/developerguide/broker-instance-sizes.html): When you create an Amazon MSK Provisioned cluster you specify the size of brokers that you want it to have.

### [Storage management](https://docs.aws.amazon.com/msk/latest/developerguide/msk-storage-management.html)

Configuring tiered storage, provisioning storage throughput, and scaling up broker storage.

### [Tiered storage](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tiered-storage.html)

Enable and disable tiered storage mode on Amazon MSK clusters and topics.

- [Tiered storage scenario](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tiered-storage-retention-rules.html): When you enable tiered storage for a new or existing topic, Apache Kafka copies closed log segments from primary storage to tiered storage.
- [Create tiered storage cluster with console](https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster-tiered-storage-console.html): Create a tiered storage-enabled Amazon MSK cluster with the AWS Management Console.
- [Create tiered storage cluster with AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster-tiered-storage-cli.html): Create a tiered storage-enabled Amazon MSK cluster with the AWS CLI.
- [Enable and disable tiered storage on a topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-enable-disable-topic-tiered-storage-cli.html): Enable and disable tiered storage on a topic
- [Enable tiered storage using CLI](https://docs.aws.amazon.com/msk/latest/developerguide/msk-enable-cluster-tiered-storage-cli.html): Enable tiered storage on an existing Amazon MSK cluster using AWS CLI
- [Update tiered storage using console](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-tiered-storage-console.html): Make sure the current Apache Kafka version of your MSK cluster is 2.8.2.tiered.

### [Scale up broker storage](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-storage.html)

Update the volume of storage associated with Amazon MSK brokers.

### [Automatic scaling for clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand.html)

Use automatic scaling for Amazon MSK to increase storage capacity for a Amazon MSK cluster.

- [Auto-scaling policies](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-details.html): An auto-scaling policy defines the following parameters for your cluster:

### [Set up automatic scaling](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup.html)

You can use the Amazon MSK console, the Amazon MSK API, or CloudFormation to implement automatic scaling for storage.

- [Set up automatic scaling](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup-console.html): This process describes how to use the Amazon MSK console to implement automatic scaling for storage.
- [Set up auto scaling using CLI](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup-cli.html): This process describes how to use the Amazon MSK CLI to implement automatic scaling for storage.
- [Set up auto scaling using API](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup-api.html): This process describes how to use the Amazon MSK API to implement automatic scaling for storage.
- [Manual scaling](https://docs.aws.amazon.com/msk/latest/developerguide/manually-expand-storage.html): To increase storage, wait for the cluster to be in the ACTIVE state.

### [Manage broker storage throughput](https://docs.aws.amazon.com/msk/latest/developerguide/msk-provision-throughput-management.html)

manage provisioned storage throughput for brokers in a Amazon MSK cluster.

- [Provision storage throughput for brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-provision-throughput.html): Configure provisioned storage throughput for brokers in a Amazon MSK cluster.

### [Broker configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration.html)

Configure properties and values for Amazon MSK cluster, brokers, topics, and Apache ZooKeeper nodes.

### [Standard broker configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-standard.html)

Setting Standard broker configuration properties for Amazon MSK cluster.

- [Custom Amazon MSK configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html): Setting custom configuration properties for Amazon MSK cluster.
- [Default Amazon MSK configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-default-configuration.html): The values of the properties in the default Amazon MSK configuration.
- [Guidelines for tiered storage topic-level configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-guidelines-tiered-storage-topic-level-config.html): Guidelines for Amazon MSK tiered storage topic-level configuration.

### [Express broker configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-express.html)

Setting Express broker configuration properties for Amazon MSK cluster.

- [Custom read/write access configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-express-read-write.html): Create, describe, update, delete, and list custom Amazon MSK configurations, and use them to create Amazon MSK cluster.
- [Read-only configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-express-read-only.html): Express brokers read-only configurations

### [Broker configuration operations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations.html)

Create, describe, update, delete, and list custom Amazon MSK Express broker configurations, and use them to create Amazon MSK cluster.

- [Create configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-create.html): Create a custom Amazon MSK configuration, and use it to create Amazon MSK cluster.
- [Update configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-update.html): Update a custom Amazon MSK configuration.
- [Delete configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-delete.html): Delete a custom Amazon MSK configuration.
- [Get configuration metadata](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-describe.html): Get metadata about a custom Amazon MSK configuration.
- [Get configuration revision details](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-describe-revision.html): Get a detailed description of the Amazon MSK configuration revision.
- [List configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-list.html): Describes how to list all Amazon MSK configurations in your account for the current AWS Region
- [Amazon MSK configuration states](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-states.html): An Amazon MSK configuration can be in one of the following states.

### [Intelligent rebalancing](https://docs.aws.amazon.com/msk/latest/developerguide/intelligent-rebalancing.html)

Amazon MSK provides intelligent rebalancing for all new MSK Provisioned clusters with Express brokers.

- [Scaling Amazon MSK clusters](https://docs.aws.amazon.com/msk/latest/developerguide/intelligent-rebalancing-scaling-clusters.html): With intelligent rebalancing, you can scale your clusters up or down by editing the broker count in your clusters in a single action.
- [Steady state rebalancing](https://docs.aws.amazon.com/msk/latest/developerguide/intelligent-rebalancing-self-balancing-paritions.html): Steady state rebalancing is a part of the intelligent rebalancing feature, which is turned on by default for all new MSK Provisioned clusters with Express brokers.
- [Patching Provisioned clusters](https://docs.aws.amazon.com/msk/latest/developerguide/patching-impact.html): The impact of software updates on Kafka clients and applications.
- [Broker offline and client failover](https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting-offlinebroker-clientfailover.html): Kafka allows for an offline broker; a single offline broker in a healthy and balanced cluster following best practices will not see impact or cause failure to produce or consume.

### [Security](https://docs.aws.amazon.com/msk/latest/developerguide/security.html)

Configure Amazon Managed Streaming for Apache Kafka to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Amazon MSK resources.

### [Data protection](https://docs.aws.amazon.com/msk/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Managed Streaming for Apache Kafka.

- [Amazon MSK encryption](https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html): How to encrypt your data when using Amazon MSK.

### [Get started with Amazon MSK encryption](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html)

Describes how to encrypt your data when using Amazon MSK.

- [Specify encryption settings when creating a Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption-cluster-create.html): Describes how to specify encryption settings when creating a Amazon MSK cluster.
- [Test Amazon MSK TLS encryption](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption-test-tls.html): Describes how to test TLS encryption with Amazon MSK.
- [APIs with Interface VPC Endpoints](https://docs.aws.amazon.com/msk/latest/developerguide/privatelink-vpc-endpoints.html): Use an Interface VPC endpoint, powered by AWS PrivateLink, to prevent traffic between your Amazon VPC and Amazon MSK APIs from leaving the Amazon network.

### [Authentication and authorization for Amazon MSK APIs](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam.html)

How to authenticate clients and manage access to Amazon MSK APIs.

### [How Amazon MSK works with IAM](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam.html)

Before you use IAM to manage access to Amazon MSK, you should understand what IAM features are available to use with Amazon MSK.

- [Amazon MSK identity-based policies](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam-id-based-policies.html): With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied.
- [Amazon MSK resource-based policies](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam-resource-based-policies.html): Amazon MSK supports a cluster policy (also known as a resource-based policy) for use with Amazon MSK clusters.
- [Authorization based on Amazon MSK tags](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam-tags.html): You can attach tags to Amazon MSK clusters.
- [Amazon MSK IAM roles](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam-roles.html): An IAM role is an entity within your Amazon Web Services account that has specific permissions.

### [Identity-based policy examples](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_id-based-policy-examples.html)

By default, IAM users and roles don't have permission to execute Amazon MSK API actions.

- [Policy best practices](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_service-with-iam-policy-best-practices.html): Identity-based policies determine whether someone can create, access, or delete Amazon MSK resources in your account.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_id-based-policy-examples-view-own-permissions.html): This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.
- [Accessing one Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_id-based-policy-examples-access-one-cluster.html): In this example, you want to grant an IAM user in your Amazon Web Services account access to one of your clusters, purchaseQueriesCluster.
- [Accessing Amazon MSK clusters based on tags](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_id-based-policy-examples-view-widget-tags.html): You can use conditions in your identity-based policy to control access to Amazon MSK resources based on tags.

### [Service-linked roles](https://docs.aws.amazon.com/msk/latest/developerguide/using-service-linked-roles.html)

Describes service-linked roles to give Amazon MSK access to resources in your AWS account.

- [Service-linked role permissions](https://docs.aws.amazon.com/msk/latest/developerguide/slr-permissions.html): Amazon MSK uses the service-linked role named AWSServiceRoleForKafka.
- [Create a service-linked role](https://docs.aws.amazon.com/msk/latest/developerguide/create-slr.html): You don't need to create a service-linked role manually.
- [Edit a service-linked role](https://docs.aws.amazon.com/msk/latest/developerguide/edit-slr.html): Amazon MSK does not allow you to edit the AWSServiceRoleForKafka service-linked role.
- [Supported Regions for service-linked roles](https://docs.aws.amazon.com/msk/latest/developerguide/slr-regions.html): Amazon MSK supports using service-linked roles in all of the Regions where the service is available.

### [AWS managed policies](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol.html)

Learn about AWS managed policies for Amazon MSK and recent changes to those policies.

- [Managed policy AmazonMSKFullAccess](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-AmazonMSKFullAccess.html): This policy grants administrative permissions that allow a principal full access to all Amazon MSK actions.
- [Managed policy AmazonMSKReadOnlyAccess](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-AmazonMSKReadOnlyAccess.html): This policy grants read-only permissions that allow users to view information in Amazon MSK.
- [Managed policy KafkaServiceRolePolicy](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-KafkaServiceRolePolicy.html): You can't attach KafkaServiceRolePolicy to your IAM entities.
- [Managed policy AWSMSKReplicatorExecutionRole](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.html): The AWSMSKReplicatorExecutionRole policy grants permissions to the Amazon MSK replicator to replicate data between MSK clusters.
- [Managed policy updates](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-updates.html): View details about updates to AWS managed policies for Amazon MSK since this service began tracking these changes.
- [Troubleshoot Amazon MSK identity and access](https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon MSK and IAM.

### [Authentication and authorization for Apache Kafka APIs](https://docs.aws.amazon.com/msk/latest/developerguide/kafka_apis_iam.html)

You can use IAM to authenticate clients and to allow or deny Apache Kafka actions.

### [IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html)

How to use IAM for authentication and authorization.

### [How IAM access control for Amazon MSK works](https://docs.aws.amazon.com/msk/latest/developerguide/how-to-use-iam-access-control.html)

To use IAM access control for Amazon MSK, perform the following steps, which are described in detail in these topics:

- [Create a Amazon MSK cluster that uses IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/create-iam-access-control-cluster-in-console.html): This section explains how you can use the AWS Management Console, the API, or the AWS CLI to create a Amazon MSK cluster that uses IAM access control.
- [Configure clients for IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/configure-clients-for-iam-access-control.html): To enable clients to communicate with an MSK cluster that uses IAM access control, you can use either of these mechanisms:
- [Create authorization policies for the IAM role](https://docs.aws.amazon.com/msk/latest/developerguide/create-iam-access-control-policies.html): Attach an authorization policy to the IAM role that corresponds to the client.
- [Get the bootstrap brokers for IAM access control](https://docs.aws.amazon.com/msk/latest/developerguide/get-bootstrap-brokers-for-iam.html): See .
- [Semantics of IAM authorization policy actions and resources](https://docs.aws.amazon.com/msk/latest/developerguide/kafka-actions.html)
- [Common use cases for client authorization policy](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control-use-cases.html): The first column in the following table shows some common use cases.

### [Mutual TLS authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html)

How to use TLS-based client authentication with Amazon MSK.

- [Create a Amazon MSK cluster that supports client authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication-cluster.html)
- [Set up a client to use authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication-client.html): This process describes how to set up an Amazon EC2 instance to use as a client to use authentication.
- [Produce and consume messages using authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication-messages.html): This process describes how to produce and consume messages using authentication.

### [SASL/SCRAM authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html)

How to use sign-in credentials-based client authentication with AWS Secrets Manager and Amazon MSK.

- [How sign-in credentials authentication works](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-howitworks.html): Sign-in credentials authentication for Amazon MSK uses SASL/SCRAM (Simple Authentication and Security Layer/ Salted Challenge Response Mechanism) authentication.

### [Set up SASL/SCRAM authentication for an Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-tutorial.html)

To set up a secret in AWS Secrets Manager, follow the Creating and Retrieving a Secret tutorial in the AWS Secrets Manager User Guide.

- [Connecting to your cluster with sign-in credentials](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-tutorial-connect.html): After you create a secret and associate it with your cluster, you can connect your client to the cluster.
- [Working with users](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-users.html): Creating users: You create users in your secret as key-value pairs.
- [Limitations when using SCRAM secrets](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-limitations.html): Note the following limitations when using SCRAM secrets:
- [Apache Kafka ACLs](https://docs.aws.amazon.com/msk/latest/developerguide/msk-acls.html): How to use Apache Kafka ACLs with Amazon MSK.
- [Changing security groups](https://docs.aws.amazon.com/msk/latest/developerguide/change-security-group.html): How to change the security group that's associated with an existing Amazon MSK cluster.

### [Controlling access to Apache ZooKeeper](https://docs.aws.amazon.com/msk/latest/developerguide/zookeeper-security.html)

How to limit access to the Apache ZooKeeper nodes in your Amazon MSK cluster.

- [To place your Apache ZooKeeper nodes in a separate security group](https://docs.aws.amazon.com/msk/latest/developerguide/zookeeper-security-group.html): To limit access to Apache ZooKeeper nodes, you can assign a separate security group to them.
- [Using TLS security with Apache ZooKeeper](https://docs.aws.amazon.com/msk/latest/developerguide/zookeeper-security-tls.html): You can use TLS security for encryption in transit between your clients and your Apache ZooKeeper nodes.
- [Compliance validation](https://docs.aws.amazon.com/msk/latest/developerguide/MSK-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/msk/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Managed Streaming for Apache Kafka features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/msk/latest/developerguide/infrastructure-security.html): Learn how Amazon Managed Streaming for Apache Kafka isolates service traffic.

### [Amazon MSK logging](https://docs.aws.amazon.com/msk/latest/developerguide/msk-logging.html)

You can deliver Apache Kafka broker logs to one or more of the following destination types: Amazon CloudWatch Logs, Amazon S3, Amazon Data Firehose.

- [CloudTrail events](https://docs.aws.amazon.com/msk/latest/developerguide/logging-API-using-cloudtrail.html)
- [Metadata management](https://docs.aws.amazon.com/msk/latest/developerguide/metadata-management.html): Amazon MSK supports Apache ZooKeeper and KRaft metadata management modes.

### [Topic Operations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-topic-operations-information.html)

Manage topics in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

### [List topics](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-topics.html)

List all topics in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [List topics using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/list-topics-console.html)
- [List topics using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/list-topics-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster.
- [List topics using the API](https://docs.aws.amazon.com/msk/latest/developerguide/list-topics-api.html): To list topics using the API, see ListTopics.

### [Describe a topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-describe-topic.html)

Get detailed information about a specific topic in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [Describe a topic using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-console.html)
- [Describe a topic using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster and TopicName with the name of the topic you want to describe.
- [Describe a topic using the API](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-api.html): To describe a topic using the API, see DescribeTopic.

### [Describe topic partitions](https://docs.aws.amazon.com/msk/latest/developerguide/msk-describe-topic-partitions.html)

View detailed partition information for a specific topic in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [View partition information using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-partitions-console.html)
- [View partition information using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-partitions-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster and TopicName with the name of the topic.
- [View partition information using the API](https://docs.aws.amazon.com/msk/latest/developerguide/describe-topic-partitions-api.html): To view partition information using the API, see DescribeTopicPartitions.

### [Create topics](https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-topic.html)

Create topics in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [Create topics using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/create-topic-console.html)
- [Create a topic using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/create-topic-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster.
- [Create a topic using the API](https://docs.aws.amazon.com/msk/latest/developerguide/create-topic-api.html): To create a topic using the API, see CreateTopic.

### [Update a topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-topic.html)

Update a topic in your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [Update a topic using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/update-topic-console.html)
- [Update a topic using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/update-topic-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster and TopicName with the name of the topic you want to update.
- [Update a topic using the API](https://docs.aws.amazon.com/msk/latest/developerguide/update-topic-api.html): To update a topic using the API, see UpdateTopic.

### [Delete a topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-delete-topic.html)

Delete a topic from your MSK Provisioned cluster using the AWS Management Console, the AWS CLI, or the API.

- [Delete a topic using the AWS Management Console](https://docs.aws.amazon.com/msk/latest/developerguide/delete-topic-console.html)
- [Delete a topic using the AWS CLI](https://docs.aws.amazon.com/msk/latest/developerguide/delete-topic-cli.html): Run the following command, replacing ClusterArn with the Amazon Resource Name (ARN) of your cluster and TopicName with the name of the topic you want to delete.
- [Delete a topic using the API](https://docs.aws.amazon.com/msk/latest/developerguide/delete-topic-api.html): To delete a topic using the API, see DeleteTopic.
- [Resources](https://docs.aws.amazon.com/msk/latest/developerguide/resources.html): Amazon MSK resources.

### [Apache Kafka versions](https://docs.aws.amazon.com/msk/latest/developerguide/kafka-versions.html)

Information about the Apache Kafka versions that Amazon Managed Streaming for Apache Kafka (Amazon MSK) supports and related cluster operations.

- [Supported Apache Kafka versions](https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html): Amazon Managed Streaming for Apache Kafka (Amazon MSK) supports the following Apache Kafka and Amazon MSK versions.

### [Amazon MSK version support](https://docs.aws.amazon.com/msk/latest/developerguide/version-support.html)

This topic describes the and the procedure for .

- [Upgrade the Apache Kafka version](https://docs.aws.amazon.com/msk/latest/developerguide/version-upgrades.html): You can upgrade an existing MSK cluster to a newer version of Apache Kafka.
- [Best practices for version upgrades](https://docs.aws.amazon.com/msk/latest/developerguide/version-upgrades-best-practices.html): To ensure client continuity during the rolling update that is performed as part of the Kafka version upgrade process, review the configuration of your clients and your Apache Kafka topics as follows:
- [Troubleshoot Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting.html): Troubleshoot issues with your Amazon MSK cluster.

### [Best practices](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices-intro.html)

This section describes best practices to follow for Standard brokers and Express brokers.

- [Best practices for Standard brokers](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html): Best practices for managing your MSK Provisioned cluster when using Standard brokers.
- [Best practices for Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices-express.html): Best practices for managing your Amazon MSK cluster when using Express brokers.
- [Best practices for Apache Kafka clients](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices-kafka-client.html): Best practices for managing Apache Kafka clients.


## [MSK Serverless](https://docs.aws.amazon.com/msk/latest/developerguide/serverless.html)

### [Use MSK Serverless clusters](https://docs.aws.amazon.com/msk/latest/developerguide/serverless-getting-started.html)

Get up and running with Amazon MSK serverless clusters.

- [Create a cluster](https://docs.aws.amazon.com/msk/latest/developerguide/create-serverless-cluster.html): Create an Amazon MSK Serverless cluster.
- [Create an IAM role](https://docs.aws.amazon.com/msk/latest/developerguide/create-iam-role.html): Create an IAM role that can create topics on the cluster and write to them.
- [Create a client machine](https://docs.aws.amazon.com/msk/latest/developerguide/create-serverless-cluster-client.html): Create a client that can access the serverless cluster.
- [Create a topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-serverless-create-topic.html): Create an Apache Kafka topic on an MSK Serverless cluster.
- [Produce and consume data](https://docs.aws.amazon.com/msk/latest/developerguide/msk-serverless-produce-consume.html): In this step, you produce and consume data using the topic that you created in the previous step.
- [Delete resources](https://docs.aws.amazon.com/msk/latest/developerguide/delete-resources.html): Delete the resources that you created in this getting started tutorial for MSK Serverless.
- [Configuration properties](https://docs.aws.amazon.com/msk/latest/developerguide/serverless-config.html): Amazon MSK sets broker configuration properties for serverless clusters.
- [Configure dual-stack network type](https://docs.aws.amazon.com/msk/latest/developerguide/serverless-config-dual-stack.html): Amazon MSK supports dual-stack network type for existing MSK Serverless clusters that use Kafka version 3.6.0 or later at no additional cost.
- [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/serverless-monitoring.html): Amazon MSK integrates with Amazon CloudWatch so that you can collect, view, and analyze metrics for your MSK Serverless cluster.


## [MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html)

### [Getting started](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-getting-started.html)

This is a step-by-step tutorial that uses the AWS Management Console to create an MSK cluster and a sink connector that sends data from the cluster to an S3 bucket.

- [Set up resources required for MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-tutorial-setup.html): In this step you create the following resources that you need for this getting-started scenario:
- [Create custom plugin](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-plugin.html): A plugin contains the code that defines the logic of the connector.
- [Create client machine and Apache Kafka topic](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-topic.html): In this step you create an Amazon EC2 instance to use as an Apache Kafka client instance.
- [Create connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-connector.html): This procedure describes how to create a connector using the AWS Management Console.
- [Send data to the MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-send-data.html): In this step you send data to the Apache Kafka topic that you created earlier, and then look for that same data in the destination S3 bucket.

### [Understand connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-connectors.html)

A connector integrates external systems and Amazon services with Apache Kafka by continuously copying streaming data from a data source into your Apache Kafka cluster, or continuously copying data from your cluster into a data sink.

- [Understand connector capacity](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-capacity.html): The total capacity of a connector depends on the number of workers that the connector has, as well as on the number of MSK Connect Units (MCUs) per worker.
- [Understand maximum autoscaling task count](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-max-autoscaling-task-count.html): The maxAutoscalingTaskCount parameter is an optional capacity field available for autoscaling connectors in Amazon MSK Connect.
- [Configure dual-stack network type](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dual-stack.html): Amazon MSK Connect supports dual-stack network type for new connectors.
- [Create a connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-connector-intro.html): This procedure describes how to create a connector using the AWS Management Console.
- [Update a connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-update-connector.html): This procedure describes how to update the configuration of an existing MSK Connect connector using the AWS Management Console.
- [Connecting from connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-from-connectors.html): The following best practices can improve the performance of your connectivity to Amazon MSK Connect.
- [Create custom plugins](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-plugins.html): A plugin is an AWS resource that contains the code that defines your connector logic.

### [Understand MSK Connect workers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-workers.html)

Learn about workers for Amazon MSK Connect.

- [Supported worker configuration properties](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-supported-worker-config-properties.html): MSK Connect provides a default worker configuration.
- [Create a custom configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-create-custom-worker-config.html): This procedure describes how to create a custom worker configuration using the AWS Management Console.

### [Manage connector offsets](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-manage-connector-offsets.html)

This section provides information to help you manage source connector offsets using the offset storage topic.

- [Use the default offset storage topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-default-offset-storage-topic.html): By default, Amazon MSK Connect generates a new offset storage topic on your Kafka cluster for each connector that you create.
- [Use custom offset storage topic](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-set-offset-storage-topic.html): To provide offset continuity between source connectors, you can use an offset storage topic of your choice instead of the default topic.
- [Configuration providers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-config-provider.html): This page provides information about externalizing secrets for Amazon MSK Connect with an open source configuration provider.

### [IAM roles and policies](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-iam.html)

This section helps you set up the appropriate IAM policies and roles to securely deploy and manage Amazon MSK Connect within your AWS environment.

- [Understand service execution role](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-service-execution-role.html)
- [Example policy](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-iam-policy-examples.html): To give a non-admin user full access to all MSK Connect functionality, attach a policy like the following one to the user's IAM role.
- [Prevent cross-service confused deputy problem](https://docs.aws.amazon.com/msk/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [AWS managed policies](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-security-iam-awsmanpol.html): Learn about AWS managed policies for MSK Connect and recent changes to those policies.
- [Use service-linked roles](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-using-service-linked-roles.html): How to use service-linked roles to give MSK Connect access to resources in your AWS account.

### [Enable internet access](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access.html)

This page includes information to help you configure internet access for Amazon MSK Connect.

- [Set up a NAT gateway](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-internet-access-private-subnets-example.html): The following steps show you how to set up a NAT gateway to enable internet access for a connector.

### [Understand private DNS hostnames](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dns.html)

Describes Private DNS hostname resolution feature in MSK Connect.

- [Configure a VPC DHCP option](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dns-config-dhcp.html): Describes the configuration requirements for publicly and privately resolvable DNS hostnames.
- [Configure DNS attributes](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dns-attributes.html): Describes recommended settings for your connector VPC.
- [Handle connector creation failures](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-dns-failure-handling.html): Possible connector creation failures associated with DNS resolution and suggested actions to resolve the issues.
- [Security](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-security.html): Security and data protection in Amazon MSK Connect using Amazon MSK APIs with Interface VPC Endpoints.
- [Logging](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-logging.html): MSK Connect can write log events that you can use to debug your connector.
- [Monitoring MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-monitoring-overview.html): Monitor MSK Connect to maintain reliability, availability, and performance.

### [Examples](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-examples.html)

Examples for Amazon MSK Connect that demonstrate how to set up common connectors and configuration providers.

- [Set up Amazon S3 sink connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-S3sink-connector-example.html): This example shows how to set up the Confluent Amazon S3 sink connector for Amazon MSK connect.
- [Set up EventBridge Kafka sink connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-eventbridge-kafka-connector.html): Learn how to set up MSK Connect with EventBridge to stream data from Apache Kafka topics to EventBridge for building event-driven architectures.

### [Use Debezium source connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-debeziumsource-connector-example.html)

This example shows how to use the Debezium MySQL connector with a MySQL-compatible Amazon Aurora database as the source.

- [Complete prerequisites to use Debezium source connector](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-debeziumsource-connector-example-prereqs.html): Your connector must be able to access the internet so that it can interact with services such as AWS Secrets Manager that are outside of your Amazon Virtual Private Cloud.
- [Create a Debezium source connector](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-debeziumsource-connector-example-steps.html): This procedure describes how to create a Debezium source connector.
- [Update a Debezium connector configuration](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-debeziumsource-connector-update.html): To update the configuration of the Debezium connector, follow these steps:

### [Migrate to Amazon MSK Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-migrating.html)

This section describes how to migrate your Apache Kafka connector application to Amazon Managed Streaming for Apache Kafka Connect (Amazon MSK Connect).

- [Understand internal topics used by Kafka Connect](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-kafka-connect-topics.html): An Apache Kafka Connect application thatâs running in distributed mode stores its state by using internal topics in the Kafka cluster and group membership.
- [State management](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-state-management.html): By default, Amazon MSK Connect creates three separate topics in the Kafka cluster for each Amazon MSK Connector to store the connectorâs configuration, offset, and status.
- [Migrate source connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-migrate-source-connectors.html): Source connectors are Apache Kafka Connect applications that import records from external systems into Kafka.
- [Migrate sink connectors](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-migrate-sink-connectors.html): Sink connectors are Apache Kafka Connect applications that export data from Kafka to external systems.
- [Troubleshooting](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-troubleshooting.html): The following information can help you troubleshoot problems that you might have while using MSK Connect.


## [MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator.html)

- [How Amazon MSK Replicator works](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-how-it-works.html): To get started with MSK Replicator, you need create a new Replicator in your target clusterâs AWS Region.

### [Set up source and target clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-getting-started.html)

Get up and running with Amazon MSK Replicator.

- [Prepare the Amazon MSK source cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-prepare-cluster.html): If you already have an MSK source cluster created for the MSK Replicator, make sure that it meets the requirements described in this section.
- [Prepare the Amazon MSK target cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-prepare-target-cluster.html): Create an MSK target cluster (provisioned or serverless) with IAM access control turned on.

### [Tutorial: Create an Amazon MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-create.html)

After you set up the source and target clusters, you can use those clusters to create an Amazon MSK Replicator.

### [Considerations for creating an Amazon MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-requirements.html)

The following sections give an overview of the prerequisites, supported configurations, and best practices for using the MSK Replicator feature.

- [Supported cluster types and versions](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-supported-clusters-versions.html): These are requirements for supported instance types, Kafka versions, and network configurations.
- [Supported MSK Serverless cluster configuration](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-serverless-requirements.html)
- [Create replicator with AWS console](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-create-console.html): The following section explains the step-wise console workflow for creating a replicator.
- [Edit MSK Replicator settings](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-edit-settings.html): You canât change the source cluster, target cluster, Replicator starting position, or topic name replication configuration once the MSK Replicator has been created.
- [Delete an MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-delete.html): You may need to delete a MSK Replicator if it fails to create (FAILED status).
- [Monitor replication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-monitor.html): You can use https://console.aws.amazon.com/cloudwatch/ in the target cluster Region to view metrics for ReplicationLatency, MessageLag, and ReplicatorThroughput at a topic and aggregate level for each Amazon MSK Replicator.

### [Use replication to increase resiliency](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-increase-resiliency.html)

You can use MSK Replicator to set up active-active or active-passive cluster topologies to increase resiliency of your Apache Kafka application across AWS Regions.

- [Create an active-passive Kafka cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicators-active-passive-cluster-setup.html): For an active-passive setup, we recommend you to operate a similar setup of producers, MSK clusters, and consumers (with the same consumer group name) in two different AWS Regions.
- [Failover to the secondary Region](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-when-planned-failover.html): We recommend that you monitor replication latency in the secondary AWS Region using Amazon CloudWatch.
- [Perform a planned failover](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-perform-planned-failover.html): You can conduct a planned failover to test the resiliency of your application against an unexpected event in your primary AWS region which has your source MSK cluster.
- [Perform an unplanned failover](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-perform-unplanned-failover.html): You can conduct an unplanned failover when there is a service event in the primary AWS Region which has your source MSK cluster and you want to temporarily redirect your traffic to the secondary Region which has your target MSK cluster.
- [Perform failback](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-perform-failback.html): You can failback to the primary AWS region after the service event in that region has ended.
- [Create an active-active setup](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-active-active.html): If you want to create an active-active setup where both MSK clusters are actively serving reads and writes, we recommend that you use an MSK Replicator with Prefixed topic name replication (Add prefix to topics name in console).
- [Migrate from one Amazon MSK cluster to another](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-migrate-cluster.html): You can use Identical topic name replication for cluster migration, but your consumers must be able to handle duplicate messages without downstream impact.
- [Migrate from self-managed MirrorMaker2 to MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-migrate-mirrormaker2.html): To migrate from MirrorMaker (MM2) to MSK Replicator, follow these steps:
- [Troubleshoot MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-troubleshooting.html): The following information can help you troubleshoot problems that you might have with MSK Replicator.
- [Best practices for using MSK Replicator](https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-best-practices.html): This section covers common best practices and implementation strategies for using Amazon MSK Replicator.


## [MSK integrations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-integrations.html)

- [Athena connector for Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/integrations-athena.html): Reference for Amazon Athena connector for Amazon MSK.
- [Redshift integration for Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/integrations-redshift.html): Reference for Amazon MSK support for Amazon Redshift streaming data ingestion feature.
- [Firehose integration for Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/integrations-kinesis-data-firehose.html): Reference for Amazon MSK support for Amazon Data Firehose streaming data ingestion feature.
- [Lambda integration with Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/integrations-lambda.html): Reference for Amazon MSK support for data processing with AWS Lambda.
- [Access EventBridge pipes](https://docs.aws.amazon.com/msk/latest/developerguide/eb-pipes-integration.html): Create pipes with a Amazon MSK cluster as the source from within the Amazon MSK console.
- [Kafka Streams with Express brokers and MSK Serverless](https://docs.aws.amazon.com/msk/latest/developerguide/use-kafka-streams-express-brokers-msk-serverless.html): Configure and run Kafka Streams applications with MSK Express brokers and MSK Serverless.

### [Real-time vector embedding blueprints](https://docs.aws.amazon.com/msk/latest/developerguide/ai-vector-embedding-integration-learn-more.html)

Create real-time AI apps with a Amazon MSK cluster as the source from within the Amazon MSK console.

- [Logging and observability](https://docs.aws.amazon.com/msk/latest/developerguide/ai-vector-embedding-integration-logging-observability.html): This section lists the CloudWatch metrics for real-time vector embedding blueprints.
- [Notes before enabling real-time vector embedding blueprints](https://docs.aws.amazon.com/msk/latest/developerguide/ai-vector-embedding-integration-notes.html): This section lists some notes to be aware of before enabling real-time vector embedding blueprints.
- [Deploy streaming data vectorization blueprint](https://docs.aws.amazon.com/msk/latest/developerguide/ai-vector-embedding-integration-deploy.html): This section is a procedure for deploying a streaming data vectorization blueprint.
