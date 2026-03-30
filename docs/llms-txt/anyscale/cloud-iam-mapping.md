# Source: https://docs.anyscale.com/iam/cloud-iam-mapping.md

# Anyscale cloud IAM mapping

[View Markdown](/iam/cloud-iam-mapping.md)

# Anyscale cloud IAM mapping

Use cloud IAM mapping to configure different IAM roles for Ray clusters deployed in your organization. You can set IAM mapping rules based on workload type, project, or user.

This page uses the term *IAM role* to describe permissions governing identity and access management (IAM). The specifics of configuring IAM roles vary by cloud deployments. See [IAM on Anyscale](/iam.md).

info

Cloud IAM mapping is in beta release.

## What is cloud IAM mapping?[​](#what-is "Direct link to What is cloud IAM mapping?")

When you deploy an Anyscale cloud, Anyscale configures a default IAM role to attach to all clusters in your Anyscale cloud (sometimes called a *data plane role*). The exact permissions for this role vary based on how you configured and deployed your Anyscale cloud, but all users that can run code in your Anyscale cloud have the same permissions for interacting with resources in your cloud provider account by default.

Cloud IAM mapping allows cloud admins to configure rules that apply different IAM roles to Anyscale clusters based on customizable parameters. When Anyscale launches a cluster, the control plane matches the request against the configured rules and assigns the corresponding IAM role for the first rule matching the conditions for the cluster.

## Cloud IAM mapping for Kubernetes[​](#kubernetes "Direct link to Cloud IAM mapping for Kubernetes")

Anyscale also supports cloud IAM mapping for Amazon Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), and Google Kubernetes Engine (GKE).

Cloud IAM mapping for Kubernetes interacts with Kubernetes service accounts to assign IAM permissions to Pods. You must configure annotations for your Kubernetes service accounts to map IAM permissions from your cloud provider. See [Configure IAM roles for clusters on Anyscale on EKS](/iam/eks.md), [Configure service accounts for clusters on Anyscale on GKE](/iam/gke.md), and [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).

## Configure IAM mapping settings[​](#configure "Direct link to Configure IAM mapping settings")

You must be an organization owner to configure cloud IAM mapping.

* Anyscale console
* CLI

To configure cloud IAM mapping in the Anyscale console, complete the following steps:

1. Click your user icon.
2. Click **Clouds**.
3. Click the name of your cloud.
4. Click **Settings**.
5. Click **IAM mapping**. The IAM mapping configuration appears.
6. Click **Edit**.
7. Define your cloud IAM mapping rules and fallback options. See [Define IAM mapping rules](#rules).
8. Click **Save**.

To configure cloud IAM mapping with the Anyscale CLI, complete the following steps:

1. Retrieve your existing cloud configuration by running the following command:

```
anyscale cloud config get -n <cloud-name>
```

The results return as YAML-formatted text.

1. Copy the returned YAML into a new file. Update your configuration to add cloud IAM mapping rules and fallback options. See [Define IAM mapping rules](#rules).

2. Run the following command passing your configuration to the `--spec-file` option:

```
anyscale cloud config update -n <cloud-name> --spec-file=/path/to/cloud-config.yaml
```

## Define IAM mapping rules[​](#rules "Direct link to Define IAM mapping rules")

You configure cloud IAM mapping rules using YAML and Kubernetes label selector syntax.

The order of rules matters. Each cluster can only have one IAM role attached. Anyscale evaluates the rules in the order specified and applies the IAM role from the first rule that has selector values that match the conditions of the cluster.

This configuration has the following structure:

```
rules:
  - selector: # workload-type, project, and user rules
    value: # IAM instance profile name, service account email, or Kubernetes service account name
fallback_rule: # CLOUD_DEFAULT or FAIL
```

### Define rule conditions[​](#conditions "Direct link to Define rule conditions")

Use the `selector` field to define the conditions for applying an IAM role using Kubernetes label selector syntax.

The following table describes the options:

| Option          | Description                                                                          |   |
| --------------- | ------------------------------------------------------------------------------------ | - |
| `workload-type` | The type of cluster, either `job`, `service`, or `workspace`.                        |   |
| `project`       | The Anyscale project name.                                                           |   |
| `user`          | The email of an Anyscale user or Anyscale service account that launches the cluster. |   |

important

Anyscale only validates the identity of the user when first launching the cluster.

Any user that can access and run code on an Anyscale workspace uses the identity and IAM role of the user that created the workspace, including when you restart a terminated workspace.

### Specify the IAM role value[​](#specify-the-iam-role-value "Direct link to Specify the IAM role value")

For each rule, use the `value` field to specify an IAM instance profile name (AWS), service account email (Google Cloud), or Kubernetes service account name (AKS, EKS, or GKE).

note

For AWS, make sure you use the instance profile name and not the ARN. For example, for the ARN `arn:aws:iam::12345:instance-profile/cld_abc-cluster_node_role`, the instance profile name is `cld_abc-cluster_node_role`.

Google Cloud uses service account emails to identify Google Cloud service accounts. GKE and EKS use Kubernetes service account names.

### Configure default behavior[​](#configure-default-behavior "Direct link to Configure default behavior")

Use the `fallback_rule` to define the default behavior when no mapping rule matches a workload:

| Option          | Description                                                                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CLOUD_DEFAULT` | Use the default IAM role of the Anyscale cloud.Anyscale recommends using this option when your IAM mapping rules grant additional permissions beyond the default role.              |
| `FAIL`          | Fail to start a workload if no rule matches.Anyscale recommends using this option when your IAM mapping rules applies permissions that are more restrictive than your default role. |

## Cloud permission requirements[​](#cloud-permission-requirements "Direct link to Cloud permission requirements")

You must configure IAM role permissions in your cloud provider account to use cloud IAM mapping. Configuration details and defaults differ by cloud provider and deployment method, but the following are the minimum requirements:

* The control plane role configured for your Anyscale cloud must be able to assign IAM roles to virtual machines.
* Each IAM role used with cloud IAM mapping must have read and write access to the default storage location configured with your Anyscale cloud.

Anyscale clouds on EKS and GKE have the same basic requirements as deployments using virtual machines. For details, see the following:

* [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md)
* [Minimum privileges for Anyscale cluster IAM roles](/iam/aws.md#minimum)
* [Minimum privileges for Anyscale cluster service accounts](/iam/google-cloud.md#minimum)

## Example AWS IAM mapping configuration[​](#example-aws-iam-mapping-configuration "Direct link to Example AWS IAM mapping configuration")

The following is an example configuration for AWS:

```
cloud_deployment_id: cldrsrc_XXXX
cloud_provider: AWS
compute_stack: VM
dataplane_iam_mapping:
  rules:
    - selector: workload-type in (workspace),user=user1@example.com
      value: role_name1
    - selector: workload-type in (job, service),user=user2@example.com
      value: role_name2
  fallback_rule: CLOUD_DEFAULT
```

## Example Google Cloud IAM mapping configuration[​](#example-google-cloud-iam-mapping-configuration "Direct link to Example Google Cloud IAM mapping configuration")

The following is an example configuration for Google Cloud:

```
cloud_deployment_id: cldrsrcgcp_i93p4pp6k8fe1hca7kggbjvdyu
cloud_provider: GCP
compute_stack: VM
dataplane_iam_mapping:
  rules:
    - selector: workload-type in (workspace),user=user1@example.com
      value: sa1@xxx.iam.gserviceaccount.com
    - selector: workload-type in (job, service),user=user2@example.com
      value: sa2@xxx.iam.gserviceaccount.com
  fallback_rule: CLOUD_DEFAULT
```

## Example AKS IAM mapping configuration[​](#example-aks-iam-mapping-configuration "Direct link to Example AKS IAM mapping configuration")

The following is an example configuration for AKS:

```
cloud_deployment_id: cldrsrc_XXXX
cloud_provider: AZURE
compute_stack: K8S
dataplane_iam_mapping:
  rules:
    - selector: workload-type in (workspace),user=user1@example.com
      value: kubernetes-service-account-name1
    - selector: workload-type in (job, service),user=user2@example.com
      value: kubernetes-service-account-name2
  fallback_rule: CLOUD_DEFAULT
```

## Example EKS IAM mapping configuration[​](#example-eks-iam-mapping-configuration "Direct link to Example EKS IAM mapping configuration")

The following is an example configuration for EKS:

```
cloud_deployment_id: cldrsrc_XXXX
cloud_provider: AWS
compute_stack: K8S
dataplane_iam_mapping:
  rules:
    - selector: workload-type in (workspace),user=user1@example.com
      value: kubernetes-service-account-name1
    - selector: workload-type in (job, service),user=user2@example.com
      value: kubernetes-service-account-name2
  fallback_rule: CLOUD_DEFAULT
```

## Example GKE IAM mapping configuration[​](#example-gke-iam-mapping-configuration "Direct link to Example GKE IAM mapping configuration")

The following is an example configuration for GKE:

```
cloud_deployment_id: cldrsrc_XXXX
cloud_provider: GCP
compute_stack: K8S
dataplane_iam_mapping:
  rules:
    - selector: workload-type in (workspace),user=user1@example.com
      value: kubernetes-service-account-name1
    - selector: workload-type in (job, service),user=user2@example.com
      value: kubernetes-service-account-name2
  fallback_rule: CLOUD_DEFAULT
```
