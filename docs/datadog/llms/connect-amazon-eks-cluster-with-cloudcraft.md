# Source: https://docs.datadoghq.com/cloudcraft/getting-started/connect-amazon-eks-cluster-with-cloudcraft.md

---
title: Connect an Amazon EKS Cluster with Cloudcraft
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Connect an Amazon EKS
  Cluster with Cloudcraft
---

# Connect an Amazon EKS Cluster with Cloudcraft

By scanning your Amazon EKS clusters, Cloudcraft allows you to generate system architecture diagrams to help visualize your deployed workloads and pods.

Cloudcraft uses [access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) to grant [Cloudcraft's existing read-only IAM entity role](https://docs.datadoghq.com/cloudcraft/faq/how-cloudcraft-connects-to-aws/) access to the Kubernetes API. Cloudcraft does not require any special software or agent to be installed on your cluster.

{% alert level="info" %}
The ability to scan Amazon EKS clusters and AWS accounts is only available to Cloudcraft Pro subscribers. Check out [our pricing page](https://www.cloudcraft.co/pricing) for more information.
{% /alert %}

## Prerequisites{% #prerequisites %}

Before connecting your Amazon EKS clusters with Cloudcraft, you must connect your AWS account and generate diagrams that include your clusters.

To connect your AWS account and familiarize yourself with Cloudcraft, see the following articles:

- [Connect your AWS account with Cloudcraft](https://docs.datadoghq.com/cloudcraft/getting-started/connect-aws-account-with-cloudcraft/)
- [Crafting Better Diagrams: Cloudcraft's Live Diagramming and Filtering](https://docs.datadoghq.com/cloudcraft/getting-started/crafting-better-diagrams/)

[Install and configure `kubectl`](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html), a tool that allows you to control Kubernetes clusters through the command line. Cloudcraft recommends using the latest version to avoid issues.

In addition, you'll want to [install and configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to manage your AWS services from the command line. As with `kubectl`, Cloudcraft recommends using the latest version.

Finally, in order to scan your cluster successfully, Cloudcraft requires clusters to have public access enabled and no IP filtering applied. The **Public Access Source Allow List** option in the networking configuration must remain set to its default value of 0.0.0.0/0.

## Create access entries{% #create-access-entries %}

Start by opening a blueprint with an existing Amazon EKS cluster or creating a new blueprint to scan an account with Amazon EKS clusters.

With your AWS environment mapped into a blueprint, select the Amazon EKS cluster that you wish to scan, and click the **Enable cluster scanning** button that appears in the component toolbar.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-amazon-eks-cluster-with-cloudcraft/enable-cluster-scanning.dc1656584c3d1fe80c8eb53955c4601b.png?auto=format"
   alt="Interactive Cloudcraft diagram showing an AWS EKS cluster with enable cluster scanning button highlighted." /%}

The next screen provides step-by-step commands to run in your favorite terminal application.

As the Amazon EKS cluster creator or user with admin access, run the following command to map the Cloudcraft IAM role to the Kubernetes group `cloudcraft-view-only`:

```
aws eks create-access-entry \
  --cluster-name ${EKS_CLUSTER_NAME} \
  --principal-arn ${CLOUDCRAFT_IAM_ROLE_ARN} \
  --kubernetes-groups 'cloudcraft-view-only'
```

## Granting view-only access to the Cloudcraft IAM role{% #granting-view-only-access-to-the-cloudcraft-iam-role %}

Next, use [ClusterRoleBinding](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding) to bind the IAM role to a Kubernetes role.

A ClusterRoleBinding grants permissions defined in a role to a user or set of users in all namespaces in a cluster. Kubernetes defines some default user-facing roles. For Cloudcraft, use the predefined "view" role that allows view-only access to most objects in a namespace.

Enter the following multi-line command to create the ClusterRoleBinding and grant view-only permission to users in the **cloudcraft-view-only** group.

```
cat << EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cloudcraft-view-only
subjects:
  - kind: Group
    name: cloudcraft-view-only
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: rbac.authorization.k8s.io
EOF
```

## Testing access to the cluster{% #testing-access-to-the-cluster %}

To test that Cloudcraft can access to the cluster, click **Test cluster access** at the bottom of the **Enable Kubernetes Cluster Scanning** screen.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-amazon-eks-cluster-with-cloudcraft/test-cluster-access.e1022f375163fffdf8dc87595612f620.png?auto=format"
   alt="Cloudcraft interface showing Kubernetes cluster role configuration with a 'Test Cluster Access' button highlighted by an arrow." /%}

To scan other clusters, repeat the process as many times as needed.
