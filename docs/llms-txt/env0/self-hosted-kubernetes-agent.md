# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview: Self-Hosted Kubernetes Agent

> Overview and installation guide for the env zero self-hosted Kubernetes agent

Self-hosted agents allow you to run env zero deployment workloads on your own Kubernetes cluster.

* Execution is contained within your own servers/infrastructure
* The agent requires an internet connection but no inbound network access.
* Secrets can be stored on your own infrastructure.

<Note>
  Feature Availability

  Self-hosted agents are only available to Enterprise level customers. Click [here for more details](https://www.env0.com/pricing)
</Note>

## Requirements

* Kubernetes cluster at version >= 1.24
  * [Autoscaler](/guides/admin-guide/self-hosted-kubernetes-agent/#autoscaler-recommended-but-optional)
  * [Persistent Volume/Storage Class](/guides/admin-guide/self-hosted-kubernetes-agent/#persistent-volumestorage-class-optional)(Optional)
  * AMD64 or ARM64-based nodes.
* The agent will be installed using a [Helm chart](#installation).

<Info>
  **Cluster Installation**

  The Agent can be run on an existing Kubernetes cluster in a dedicated namespace, or you can create a cluster just for the agent.

  Use our [k8s-modules](https://github.com/env0/k8s-modules) repository, which contains Terraform code for easier cluster installation. You can use the main provider folder for a complete installation, or a specific module to fulfill only certain requirements.
</Info>

## Autoscaler (recommended, but optional)

* While optional, configuring horizontal auto-scaling will allow your cluster to adapt to the concurrency and deployment requirements based on your env zero usage. Otherwise, your deployment concurrency will be limited by the cluster's capacity. Please also see [Job Limits](/guides/admin-guide/self-hosted-kubernetes-agent/#job-limits) if you wish you to control the maximum concurrent deployment.
* The env zero agent will create a new pod for each deployment you run on env zero.\
  Pods are ephemeral and will be destroyed after a single deployment.
* A pod running a single deployment requires *at least* `cpu: 460m` and `memory: 1500Mi`, so the cluster nodes must be able to provide this resource request. Limits can be adjusted by providing [custom configuration](/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration) during chart installation.
* Minimum node requirements: an instance with at least 2 CPU and 8GiB memory.

For the EKS cluster, you can use this [TF example](https://github.com/env0/k8s-modules/blob/main/aws/autoscaler/main.tf).

## Persistent Volume/Storage Class (optional)

* env zero will store the deployment state and working directory on a persistent volume in the cluster.
* Must support Dynamic Provisioning and ReadWriteMany access mode.
* The requested storage space is `300Gi`.
* The cluster must include a `StorageClass` named `env0-state-sc`.
* The Storage Class should be set up with `reclaimPolicy: Retain`, to prevent data loss in case the agent needs to be replaced or uninstalled.

We recommend the current implementations for the major cloud providers:

| Cloud | Solution                                                                                                                                                                                                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS   | [EFS CSI](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html)<br />For the EKS cluster, you can use this TF example - [EFS](https://github.com/env0/k8s-modules/blob/main/aws/efs/main.tf) [CSI-Driver/StorageClass](https://github.com/env0/k8s-modules/blob/main/aws/csi-driver/main.tf) |
| GCP   | [Filestore](https://cloud.google.com/filestore/docs), [OpenSource NFS](https://github.com/env0/k8s-modules/tree/main/gcp)                                                                                                                                                                              |
| Azure | [Azure Files](https://docs.microsoft.com/en-us/azure/aks/azure-files-dynamic-pv)                                                                                                                                                                                                                       |

<Info>
  **PVC Alternative**

  By default, the deployment state and working directory is stored in a PV (Persistent Volume) which is configured on your Kubernetes cluster. Whenever PV creation or management is difficult, or not required, you can use [env zero-Hosted Encrypted State](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state) with `env0StateEncryptionKey`.
</Info>

## Sensitive Secrets

* Using secrets stored on the env zero platform is not allowed for self-hosted agents, since self-hosted agents allow you to store secrets on your own infrastructure.
* Customers using self-hosted agents may use their own Kubernetes Secret to store sensitive values - see *env0ConfigSecretName* below.
* If you are migrating from SaaS to a self-hosted agent, deployments attempting to use these secrets will fail.
* This includes sensitive configuration variables, SSH keys, and Cloud Deployment credentials. The values for these secrets should be replaced with references to your secret store, as detailed in the table below.
* In order to use an external secret store, authentication to the secret store must be configured using a custom Helm values file. The required parameters are detailed in [Custom/Optional Configuration](/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration).
* Storing secrets is supported using these secret stores:

| Secret store                    | Secret reference format                                              | Secret Region & Permissions                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Secrets Manager (us-east-1) | `${ssm:<secret-name>}`                                               | Set by the `awsSecretsRegion` helm value. Defaults to `us-east-1`<br />Role must have permissions: `secretsmanager:GetSecretValue`                                                                                                                                                                                                        |
| GCP Secrets Manager             | `${gcp:<secret-id>}`                                                 | Your GCP project's default region<br />Access to the secret must be possible using the `customerGoogleCredentials` configuration or using GKE workload identity. The `customerGoogleProject` configuration must be supplied and will be used to access secrets in that project only. The permission 'secrets.versions.access' is required |
| Azure Key Vault                 | `${azure:<secret-name>@<vault-name>}`                                | Your Azure subscription's default region                                                                                                                                                                                                                                                                                                  |
| HashiCorp Vault                 | `${vault:<path>.<key>@<namespace>}` where `@<namespace>` is optional |                                                                                                                                                                                                                                                                                                                                           |
| OCI Vault Secrets               | `${oci:<secret-id>}`                                                 | The region defined in the credentials provided in the agent configuration.                                                                                                                                                                                                                                                                |

<Info>
  **Allow storing secrets in env zero**

  Alternatively, you could explicitly allow env zero to store [secrets](/guides/admin-guide/variables/#secrets) on its platform, by opting-in in your organization's policy - For more info read [here](/guides/policies-governance/allow-env-zero-secrets)
</Info>

## Internal Values

The following secrets are required for the agent components to communicate with env zero's backend, they are generated and supplied in your values file.

* `awsAccessKeyIdEncoded`
* `awsSecretAccessKeyEncoded`
* `env0ApiGwKeyEncoded`

## Custom/Optional Configuration

A Helm `values.yml` will be provided by env zero with the configuration env zero provides.
The customer will need to provide a `values.customer.yml` with optional values to enable specific features.

For the complete list of configuration options, see [Custom/Optional Configuration](/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration).

## Further Configuration

The env zero agent externalizes a [wide array of values](/guides/admin-guide/self-hosted-kubernetes-agent/custom-optional-configuration) that may be set to configure the agent.

We do our best to support all common configuration case scenarios, but sometimes a more exotic or pre-released configuration is required.

For such advanced cases, see [this reference example](https://github.com/env0/self-hosted/tree/gh-pages/examples/kustomize) of utilizing [Kustomize](https://kustomize.io/) alongside [Helm Post Rendering](https://helm.sh/docs/topics/advanced/#post-rendering) to further customize our chart.

### Job Limits

You may wish to add a limit on the number of concurrent runs. To do so, add a Resource Quota to the agent namespace with a parameter on `count/jobs.batch`.

See [here](https://kubernetes.io/docs/concepts/policy/resource-quotas/) for more details.

## Installation

1. Add our Helm Repo

   ```shell  theme={null}
   helm repo add env0 https://env0.github.io/self-hosted
   ```

2. Update Helm Repo

   ```shell  theme={null}
   helm repo update
   ```

3. Download the configuration file: `<your_agent_key>_values.yaml` from Organization Settings -> Agents tab

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/organization_settings_agents_tab.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=47448c7eab258b407851ba395e3ca8bb" alt="Organization Settings Agents tab" width="1518" height="586" data-path="images/guides/admin-guide/organization_settings_agents_tab.png" />
</Frame>

1. Install the Helm Charts

   ```shell  theme={null}
   helm install --create-namespace env0-agent env0/env0-agent --namespace env0-agent -f <your_agent_key>_values.yaml -f values.customer.yaml
   # values.customer.yaml should contain any optional configuration options as detailed above
   ```

<Info>
  **TF example**

  Example for [helm install](https://github.com/env0/k8s-modules#installing-the-env0-agent)

  Helm provider must be greater >= 2.5.0
</Info>

<Info>
  **Installing from source**

  If you decide not to install the helm chart from our helm repo, and you want to install using the source code (for example by using git clone) you might need to run:

  ```shell  theme={null}
  helm dependency build <path-to-the-source-code>
  ```

</Info>

## Upgrade

```shell  theme={null}
helm upgrade env0-agent env0/env0-agent --namespace env0-agent
```

<Info>
  **Upgrade Changes**

  Previously, you would have had to download the values.yaml file. This is no longer required for an upgrade. However, we do recommend keeping the version of the values.yaml file you used to install the agent with, in case a rollback is required during the upgrade progress.
</Info>

<Warning>
  Custom Agent Docker Image

  If you [extended](/guides/admin-guide/self-hosted-kubernetes-agent/using-a-custom-image-in-an-agent) the docker image on the agent, you should update the agent version in your custom image as well.
</Warning>

## Verify Installation/Upgrade

After installing a new version of the env zero agent helm chart, it is highly recommended to verify the installation by running:

```shell  theme={null}
helm test env0-agent --namespace env0-agent --logs --timeout 1m
```

## Using the `helm template` command

Alternatively to using `helm` to install the agent directly, you could use `helm template` in order to generate the K8S yaml files for you. Then you'd be able to run these files with a different K8S pipeline, like running `kubectl apply` or using ArgoCD.

In order to generate the yaml files using `helm template`, you should first add the env zero helm chart

```shell  theme={null}
helm repo add env0 https://env0.github.io/self-hosted
helm repo update
```

Then, run the following command.

**If your Kubernetes cluster is version 1.21 and up:**

```shell  theme={null}
helm template env0-agent env0/env0-agent --kube-version=<KUBERNETES_VERSION> --api-version=batch/v1/CronJob -n <MY_NAMESPACE> -f values.yaml
```

**If your Kubernetes cluster version is less than 1.21:**

```shell  theme={null}
helm template env0-agent env0/env0-agent --kube-version=<KUBERNETES_VERSION> -n <MY_NAMESPACE> -f values.yaml
```

* `<KUBERNETES_VERSION>` is the version of your kubernetes cluster
* `<MY_NAMESPACE>` is the k8s namespace in which the agent will be installed
* values.yaml is the values file downloaded from env zero's Organization Settings -> Agents tab. You can also add your own custom values into said file.

<Warning>
  Using `env0ConfigSecretName` with the `helm template` command

  If using `helm template`, the feature that checks the Kubernetes secret defined by the env0ConfigSecretName Helm value to determine whether the PVC should be created will not function. This feature relies on an active connection to the cluster
</Warning>

### 🌐 Required Outbound Domains

| **Wildcard / Domain**                            | **Purpose / Used By**                                                                                                                  |
| :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| `*.env0.com`, `*.amazonaws.com`                  | **env zero SaaS Platform** - Required for the agent to communicate with the env zero SaaS platform.                                    |
| `ghcr.io`                                        | **GitHub Container Registry** - Hosts the Docker image of the env zero agent.                                                          |
| `*.hashicorp.com`                                | **HashiCorp** - Used to download Terraform binaries.                                                                                   |
| `registry.terraform.io`, `registry.opentofu.org` | **Module Registries** - Used to download public modules from the Terraform or OpenTofu registries.                                     |
| `github.com`, `gitlab.com`, `bitbucket.org`      | **Version Control Systems (VCS)** - Used for Git operations over ports **22**, **9418**, **80**, and **443**.                          |
| `*.infracost.io`                                 | **Infracost** - Used for cost estimation functionality.                                                                                |
| `github.com`                                     | **External Tools & Integrations** - Used to download external tools required for **custom flows** or **env zero native integrations**. |
| `dl.k8s.io`                                      | **Kubernetes** - Used to download and install `kubectl`.                                                                               |
| `get.helm.sh`                                    | **Helm** - Used to download and install `helm`.                                                                                        |
| `dl.google.com`                                  | **Google Cloud SDK** - Used to download and install `gcloud`.                                                                          |

***

> 💡 **Note:** All domains listed above require **outbound HTTPS (port 443)** access from the env zero agent.\
> Only open access to the domains for the features you are actually using.

<Warning>
  Firewall Rules

  Note that if your cluster is behind a managed firewall, you might need to whitelist the Cluster's API server's FQDN and corresponding Public IP.
</Warning>

Built with [Mintlify](https://mintlify.com).
