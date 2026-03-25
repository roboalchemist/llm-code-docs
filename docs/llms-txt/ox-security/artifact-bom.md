# Source: https://docs.ox.security/inventory-with-ox-bom/artifact-bom.md

# Artifact BOM

The Artifact Bill of Materials (BOM) is a comprehensive capability designed to give organizations visibility into all software artifacts used across cloud and Kubernetes environments.

Artifact BOM supports integration with cloud-native platforms such as Kubernetes and container registries.

By continuously monitoring deployed workloads and associated artifacts, Artifact BOM enables organizations to understand how artifacts are used in production environments, evaluate their security, and enforce governance policies.

Key capabilities include:

* **Artifact Discovery:** Artifact BOM automatically detects and inventories deployed artifacts, including container images, Kubernetes Deployments, DaemonSets, Services, and more.
* **Security Monitoring:** Surfaces vulnerabilities, misconfigurations, and exposure details for each artifact, enabling teams to assess and prioritize risk.
* **Issue Investigation and Insights:** The platform highlights all issues associated with each artifact and links them to affected assets, streamlining triage and resolution.
* **Kubernetes-Native Support:** Deep integration with Kubernetes ensures complete visibility into the containerized software supply chain, from build to runtime.

### Unscanned images

OX Security also surfaces images that were not scanned, along with the reasons why. This helps teams understand potential visibility gaps and take corrective actions.

Unscanned images appear in the Artifact BOM list if:

* **Policy exclusions apply:** For example, if a policy is configured to skip images older than 8 months, those images will appear as unscanned.
* **The image was not selected in the connector configuration:** If a specific repository was connected, but certain images were excluded during setup, they will appear as unscanned.
* **There were scan errors:** If scanning failed due to technical issues or access problems, the image will be listed with an error indicator.

## Inventorying deployed artifacts

Each row in the Artifact BOM table represents a distinct artifact detected by OX Security. You can filter and sort the data using various categories on the left panel.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bda5f58100185000bd84286f0877cd637b362128%2FArtifact_BOM.png?alt=media" alt=""><figcaption></figcaption></figure>

| Column                | Description                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Issues**            | The number of issues detected in the artifact, typically categorized by severity (e.g., Critical, High).                               |
| **Artifact**          | The name of the container image detected by OX.                                                                                        |
| **Version/Tag**       | The specific version or tag associated with the artifact (e.g., `v1.19.0`).                                                            |
| **Application**       | The application name within OX platform associated with the artifact. Often includes registry origin, for example \*Public Amazon ECR. |
| **Business Priority** | A numerical score reflecting the business impact or criticality of the application the artifact is associated with.                    |
| **Code**              | Indicates whether the artifact is linked to a code repository.                                                                         |
| **CI/CD**             | Indicates whether the artifact has been traced to a CI/CD pipeline.                                                                    |
| **Registry**          | Indicates whether the artifact has been found in a connected container registry.                                                       |
| **Cloud**             | Indicates whether the artifact was detected running in a cloud environment, for example, AWS, GCP.                                     |
| **PBOM**              | A visual indicator showing traceability across the software supply chain, from source code to runtime deployment.                      |
| **Created**           | The relative timestamp showing when the artifact was first detected by the platform.                                                   |

Use the left-side panel to narrow down artifacts by various properties.

<table><thead><tr><th width="193.6666259765625">Filter</th><th>Description</th></tr></thead><tbody><tr><td><strong>Application</strong></td><td>Select one or more applications to view related artifacts.</td></tr><tr><td><strong>Account</strong></td><td>Filter by cloud account ID to focus on specific environments.</td></tr><tr><td><strong>Asset Name</strong></td><td>Enter a specific asset name to find exact matches.</td></tr><tr><td><strong>Type</strong></td><td>Filter by resource types such as Deployment, DaemonSet, Service, or Image.</td></tr><tr><td><strong>Cloud Provider</strong></td><td>Narrow results by provider (e.g., AWS, Azure, GCP).</td></tr><tr><td><strong>Region</strong></td><td>Focus on artifacts from specific cloud regions.</td></tr><tr><td><strong>Service Category</strong></td><td>Choose a category like Kubernetes.</td></tr><tr><td><strong>Kubernetes Cluster</strong></td><td>Filter by cluster to investigate issues per environment.</td></tr><tr><td><strong>Vulnerability Severity</strong></td><td>Show only artifacts with vulnerabilities of selected severities.</td></tr><tr><td><strong>Is Internet Exposed</strong></td><td>View only externally exposed or internal artifacts.</td></tr><tr><td><strong>Image Source</strong></td><td>Filter by source of the image, such as CI/CD pipeline, registry.</td></tr><tr><td><strong>Registry Name</strong></td><td>Focus on images from specific registries.</td></tr><tr><td><strong>Registry Type</strong></td><td>Filter by type, such as public or private.</td></tr><tr><td><strong>Image Scan Status</strong></td><td>Show only scanned, unscanned, or failed scan images.</td></tr></tbody></table>

In addition you can rearrange the Artifact BOM table according to:

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d7951a2a72b50ea6331b55e4343422c08f883e64%2Fadditional_filtering.png?alt=media" alt=""><figcaption></figcaption></figure>

* Cloud deployed artifacts
* Artifacts with high severity issues

## Understanding Artifact BOM details

When selecting an artifact, a panel with detailed information appears, including:

* [Overview](#overview)
* [Registry](#registry)
* [Cloud](#cloud)
* [Public Image CVEs](#public-image-cves)
* [PBOM](#pbom)

### Overview

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cfebfcef4c41834e4c69702c70de33c11a06a172%2FOverview.png?alt=media" alt=""><figcaption></figcaption></figure>

| Field                  | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **Artifact Type**      | Indicates the type of artifact (e.g., Container).                                    |
| **Name**               | The artifact’s name as detected in your environment.                                 |
| **Application**        | The logical application associated with the artifact.                                |
| **Version/Tag**        | The specific tag or version of the artifact.                                         |
| **Business Priority**  | A calculated score that reflects the artifact’s importance to the business.          |
| **Created**            | How long ago the artifact was first detected.                                        |
| **Severities**         | Number and severity of issues found in the artifact (e.g., 1 Critical).              |
| **Artifact Integrity** | Indicates whether integrity data is available. If N/A, verification is not provided. |
| **Hash**               | The unique SHA256 hash used to identify the artifact version.                        |

### Registry

The Registry tab provides details about the image's origin in your container registry.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-72c3ed1f59e09aef0141e022e68614ece5275e2b%2FRegistry.png?alt=media" alt=""><figcaption></figcaption></figure>

| Field               | Description                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registry Type**   | The type of registry where the image is stored (e.g., Amazon ECR).                                                                                               |
| **Registry Name**   | <p>The full hostname of the registry where the image was found.<br>When the an image is included in multiple registries, all the registry names appear here.</p> |
| **Repository Name** | Full path of the repository including the image name.                                                                                                            |
| **Hash**            | The unique SHA256 hash of the image.                                                                                                                             |
| **Tags**            | The tag(s) assigned to the image version.                                                                                                                        |
| **Username**        | The user or service account that uploaded the image.                                                                                                             |
| **Time Upload**     | Timestamp of when the image was pushed to the registry.                                                                                                          |
| **Last Update**     | The most recent update detected for the image in the registry.                                                                                                   |
| **Build Time**      | The original build timestamp of the image, if available.                                                                                                         |

### Cloud

The Cloud tab shows where the artifact was observed running in cloud environments. This helps you trace image usage across clusters and workloads.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc8da9cfc2dac756ec7a9900dbb3fc459056ae97%2FCloud.png?alt=media" alt=""><figcaption></figcaption></figure>

| Field              | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| **Cloud Type**     | The cloud provider where the image was observed (e.g., AWS).          |
| **Cloud Services** | The specific service running the artifact (e.g., EKS for Kubernetes). |
| **Cluster**        | Name of the Kubernetes cluster where the image was deployed.          |
| **Namespace**      | Kubernetes namespace in which the image was running.                  |
| **Zone**           | Cloud region or availability zone (e.g., eu-west-1).                  |
| **Account**        | Cloud account ID where the image was detected.                        |
| **Hash**           | The SHA256 hash identifying the deployed image.                       |

### Public Image CVEs

The Public Image CVEs tab lists known vulnerabilities found in public base images or libraries used by the artifact. It provides visibility into inherited risks even if the image wasn’t built internally.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7f8f0205cd920776179b3f494d0afbe4a9d19d02%2FCVE.png?alt=media" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="204.33331298828125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Vulnerability ID</strong></td><td>The CVE identifier linked to the issue, with a link to external details.</td></tr><tr><td><strong>Library</strong></td><td>The affected library and version (e.g., <code>stdlib@v1.20.4</code>).</td></tr><tr><td><strong>Description</strong></td><td>A short summary of the vulnerability’s root cause and impact.</td></tr><tr><td><strong>Context</strong></td><td>Icons representing the environment or use case where the CVE was found (e.g., build, CI/CD, cloud runtime).</td></tr><tr><td><strong>Discovered</strong></td><td>Approximate time when the vulnerability was disclosed.</td></tr><tr><td><strong>CVSS</strong></td><td>The CVSS base score and severity (Critical, High, etc.) from the NVD.</td></tr><tr><td><strong>OX Severity</strong></td><td>OX's adjusted severity score, considering context like exploitability and impact.</td></tr></tbody></table>

### PBOM

The Pipeline Bill of Materials (PBOM) tab displays information about the application the artifact is associated with.

## Artifact BOM use cases

#### Tracing issues across artifacts

By reviewing the issues linked across containers and code repositories, security teams can identify root causes and reduce noise.

For example, when the same CVE appears in both the container and its associated repository, the platform links the issues. Fixing the problem in the code eliminates it in future versions of the container.

**To view the linked issues:**

* In filtering panel of the **Active Issues** page, select **Actions > Linked Issues**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6263a4475f32f51937a0b3c58c2dd119f9d6e0a6%2Flinked_issue.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Visibility into cloud-running images

Even if an image comes from a public registry, Artifact BOM shows where it’s running in Kubernetes clusters and connects it to the relevant cloud account and region.

For example, if an image is not found in your connected registries but is detected running in AWS or GCP, it still appears in the Artifact BOM with [full metadata](#cloud), helping teams track unmanaged or shadow artifacts.

#### Reviewing registry upload and build details

Artifact BOM allows AppSec teams to view metadata from [container registries](#registry), including when the image was uploaded, who uploaded it, and what [hash](#overview) it carries. This helps with auditing, identifying outdated images, and enforcing upload policies.

For example, if two identical images exist in different registries, you can use the artifact hash and upload time to validate which one is current and safe to use.

#### Investigating Public Image Vulnerabilities

The [Public Image CVEs](#public-image-cves) tab surfaces vulnerabilities inherited from base images or open-source libraries. This gives security teams insight into third-party risks, even when the application code itself does not contain vulnerabilities.

For example, vulnerabilities in Go’s `stdlib` package or OS-level libraries can be tracked across multiple containers using the same base image.
