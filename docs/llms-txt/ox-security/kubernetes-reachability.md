# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability.md

# Kubernetes Reachability

Kubernetes reachability defines how OX Security collects K8s workloads context from your Kubernetes clusters.

## Kubernetes visibility in OX

Regardless of the connection model, OX enriches security findings with the Kubernetes Workloads context.

This includes:

* Identifying which container images are actively running in workloads such as deployments and jobs.
* Enriching issues with severity factors based on actual reachability and exposure.
* Supporting prioritization based on whether workloads are internet-exposed or internally restricted.

### Cloud provider context

When a cloud provider is connected (GCP, AWS, or Azure), OX adds cloud-level context to Kubernetes data.

This is used to:

* Authenticate access to your cloud project or account as a prerequisite for Kubernetes connectivity
* Enrich Kubernetes workloads with internet exposure
* Generate a Cloud Bill of Materials (Cloud BOM) reflecting deployed assets

This applies to:

* Direct integrations with GKE, EKS, and AKS
* Inspector-based deployments that run in cloud environments

## Kubernetes connection models

OX supports the following connection models:

* Direct cloud integrations
* Inspector-based model

In general, if your cluster is externally reachable, use direct cloud integration. Otherwise, deploy the Inspector.

The following table provides detailed explanations about how to choose a connection model.

| Connection model                | How OX connects                                                             | When this applies                                                                                                                   | Supported combinations                                                                                                                        |
| ------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Direct cloud integration**    | OX connects to the Kubernetes service through the cloud provider API.       | Use this model when the cluster is externally reachable and inbound access is allowed by your network and security policies.        | <p><a href="gcp-and-gke">GKE with GCP</a><br><a href="eks">EKS</a> with <a href="aws">AWS</a><br><a href="azure-cloud">AKS with Azure</a></p> |
| **Inspector-based integration** | The Inspector runs inside your environment and sends Kubernetes data to OX. | Use this model when the cluster is private, inbound connections are restricted, or the cluster is a native Kubernetes installation. | <p>Inspector with GCP<br>Inspector with AWS<br>Inspector with Azure<br>Inspector with native Kubernetes</p>                                   |

## Enriched visibility across OX

When you connect your GKE clusters to OX Security, the platform adds context to enhance visibility and prioritization across the system:

* The **Applications** page is enriched with cloud deployment details, including Application Flow and Tags that reflect Kubernetes deployment and internet exposure.
* Issues from **SAST**, **SCA**, and **container scanning** are enhanced with Kubernetes reachability severity factors.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-34e5314735df2c0fc7d68dd9d28c7f51442a6508%2FIssues%20from%20SAST%2C%20SCA%20and%20container%20scanning%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* The **Attack Path** tab in Active Issues reflects full cloud reachability, helping you understand how issues can be exploited in your Kubernetes environment.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e1a27ac57f6c1e1b2fbb488ea3b4b67d1227b922%2FAttack%20Path%20tab%20in%20Issues%20reflects%20full%20cloud%20reachability.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* **Artifact integrity issues** are raised for images that are running in the cluster but originate from untrusted or unknown sources.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-00bc123bff466be197995e2bb0c422c9120a1434%2FArtifact%20integrity%20issues.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* The **Artifact BOM** page includes cloud deployment visibility, helping track where and how artifacts are used across clusters.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4896622499f32b4355471ec7c5bb4ada39315e78%2FArtifact%20BOM%20page%20includes%20cloud%20deployment%20visibility.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* OX scans the **specific versions of container images found in the cloud**, not just the latest versions available in your registry.
* OX surfaces vulnerability findings for public container images referenced by workloads and scans these images by pulling them from the public registry.
