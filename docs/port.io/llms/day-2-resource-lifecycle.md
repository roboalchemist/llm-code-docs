# Source: https://docs.port.io/solutions/resource-self-service/day-2-resource-lifecycle.md

# Day 2 - manage resource lifecycle

Managing the lifecycle of cloud resources is a critical aspect of platform engineering, often referred to as "Day 2 operations." After resources are provisionedâwhether they're databases, compute instances, storage buckets, or Kubernetes namespacesâthey require ongoing management to ensure reliability, security, and cost-effectiveness.

## Day 2 tasks[â](#day-2-tasks "Direct link to Day 2 tasks")

Day 2 management includes tasks such as:

* [**Scaling resources**](#scaling-resources-up-or-down-based-on-demand) up or down based on demand

  <!-- -->

  * [View ECS tasks and scale on-demand](/guides/all/manage-and-visualize-ecs-tasks.md)
  * [Scale Autoscaling Groups](/guides/all/manage-and-visualize-aws-autoscaling-groups.md)
  * [Start an EC2 Instance](/guides/all/visualize-and-manage-aws-ec2-instances.md#start-an-ec2-instance)
  * [Start a GCP Compute Engine Instance](/guides/all/manage-and-visualize-gcp-compute-engine-instances.md#start-a-compute-engine-instance)
  * [Stop a GCP Compute Engine Instance](/guides/all/manage-and-visualize-gcp-compute-engine-instances.md#stop-a-compute-engine-instance)
  * [Start Azure Webapp](/guides/all/manage-and-visualize-azure-web-apps.md#start-an-azure-web-app)
  * [Stop Azure Webapp](/guides/all/manage-and-visualize-azure-web-apps.md#stop-an-azure-web-app)
  * [Start an Azure Virtual Machine](/guides/all/manage-and-visualize-azure-virtual-machines.md#start-an-azure-virtual-machine)
  * [Deallocate an Azure Virtual Machine](/guides/all/manage-and-visualize-azure-virtual-machines.md#deallocate-an-azure-virtual-machine)
  * [Change Kubernetes Replica Count](/guides/all/change-replica-count.md)

![ECS Task Example](/img/guides/ecsTaskDashboard2.png)

* [**Patching and updating**](#patching-and-updating-software-or-configurations) software or configurations

  <!-- -->

  * [Toggle a Feature Flag](/guides/all/manage-and-visualize-your-launchdarkly-feature-flags.md#toggle-a-feature-flag)
  * [Archive a Feature Flag](/guides/all/manage-and-visualize-your-launchdarkly-feature-flags.md#archive-a-feature-flag)
  * [Add Tags to an EKS Cluster](/guides/all/manage-your-eks-clusters.md#add-tags-to-an-eks-cluster)
  * [Rollback ArgoCD Deployment](/guides/all/rollback-argocd-deployment.md)

![Launch Darkly Example](/img/guides/launchDarklyDashboard2.png)

* [**Restarting or Resyncing**](#restarting-or-resyncing-to-resolve-issues) to resolve issues

  <!-- -->

  * [Manage Kubernetes deployments](/guides/all/manage-your-kubernetes-deployment.md)
  * [Reboot an EC2 Instance](/guides/all/visualize-and-manage-aws-ec2-instances.md#reboot-an-ec2-instance)
  * [Reboot RDS instances](/guides/all/visualize-your-aws-storage-configuration.md#reboot-an-rds-instance)
  * [Restart Azure Webapp](/guides/all/manage-and-visualize-azure-web-apps.md#restart-an-azure-web-app)
  * [Restart an Azure Virtual Machine](/guides/all/manage-and-visualize-azure-virtual-machines.md#restart-an-azure-virtual-machine)
  * [Resync ArgoCD App](/guides/all/sync-argocd-app.md)
  * [Restart ArgoCD App](/guides/all/restart-argocd-app.md)

![Reboot EC2 Instance Example](/img/guides/ec2Dashboard2.png)

* [**Decommissioning or archiving**](#decommissioning-or-archiving-resources-when-theyre-no-longer-needed) resources when they're no longer needed

  <!-- -->

  * [Terminate an EC2 Instance](/guides/all/visualize-and-manage-aws-ec2-instances.md#terminate-an-ec2-instance)
  * [Delete an RDS instance](/guides/all/visualize-your-aws-storage-configuration.md#delete-an-rds-instance)
  * [Delete a Kubernetes namespace](/guides/all/manage-kubernetes-namespaces.md)
  * [Delete an SQS queue](/guides/all/manage-and-visualize-aws-sqs-queues.md#delete-an-sqs-queue)
  * [Delete an EKS Cluster](/guides/all/manage-your-eks-clusters.md#delete-an-eks-cluster)

![Launch Darkly Example](/img/guides/eksClusterDashboard.png)

* [**Monitoring usage and health**](#monitoring-usage-and-health-to-detect-issues-early) to detect issues early

  <!-- -->

  * [Monitor and Purge SQS queues](/guides/all/manage-and-visualize-aws-sqs-queues.md#purge-an-sqs-queue)
  * [Redrive messages from a DLQ](/guides/all/manage-and-visualize-aws-sqs-queues.md#redrive-messages-from-dlq)

![SQS Management Example](/img/guides/sqsQueueDashboard2.png)

* [**Rotating secrets and credentials**](#rotating-secrets-and-credentials-to-mitigate-risks) to mitigate risks
  <!-- -->
  * [Renew an ACM Certificate](/guides/all/manage-and-visualize-acm-certificates.md#renew-an-acm-certificate)

![ACM Example](/img/guides/acmDashboard2.png)

* [**Identify Security Misconfigurations**](#identify-security-misconfigurations-in-your-cloud-environments) in your cloud environments
  <!-- -->
  * [Find Issues in your AWS Storage Configuration](/guides/all/visualize-your-aws-storage-configuration.md)

![AWS Storage and Security Example](/img/guides/awsStorageAndSecurityDashboard.png)

By automating these processes and providing self-service capabilities for Day 2 operations, platform teams empower developers to manage their own resources safely, while maintaining governance and compliance. Port enables you to define self-service actions for common Day 2 tasks, set up approval workflows, and enforce policiesâensuring that your cloud resources remain well-managed throughout their lifecycle.

## Visualizing and tracking resources[â](#visualizing-and-tracking-resources "Direct link to Visualizing and tracking resources")

The guides above focus on managing the lifecycle of resources, but below, we cover how to visualize those same resources, to simplify their tracking.

There are two main appraoches:

### Track resources directly from cloud vendors[â](#track-resources-directly-from-cloud-vendors "Direct link to Track resources directly from cloud vendors")

* [Track Azure Resources](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/.md)
* [Track AWS Resources](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws/.md)
* [Track GCP Resources](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/gcp/.md)

### Track resources through your APM tools[â](#track-resources-through-your-apm-tools "Direct link to Track resources through your APM tools")

* [Ingest Cloud Resources from Dynatrace](/guides/all/ingest-cloud-resources-using-dynatrace.md)
* [Ingest Cloud Resources from Datadog](/guides/all/ingest-cloud-resources-using-datadog.md)
* [Ingest Cloud Resources from New Relic](/guides/all/ingest-cloud-resources-using-newrelic.md)
