# Source: https://docs.ox.security/inventory-with-ox-bom/cloud-bom.md

# Cloud BOM

The Cloud Bill of Materials (BOM) is a comprehensive tool designed to provide organizations with an inventory of all cloud assets across multiple cloud platforms. It helps security and operations teams understand the resources in use, their configurations, and the associated security vulnerabilities.

Cloud BOM currently supports integration with AWS.

By connecting to these platforms, Cloud BOM automatically discovers cloud resources, such as virtual machines, storage buckets, Kubernetes clusters—and categorizes them by asset type. This automated discovery enhances visibility into the organization's cloud environment and its security posture, as follows:

* **Asset Discovery:** Cloud BOM automatically identifies and catalogs cloud assets by type, including services like AWS EC2, S3, Lambda, Kubernetes, and more.
* **Security Monitoring:** Provides visibility into security issues associated with each asset, including exposure to the internet, misconfigurations, and vulnerabilities.
* **Detailed Asset Information:** For each asset, Cloud BOM provides metadata, including the asset’s region, security issues, and configuration details, helping users assess the risk posture of their environment.
* **Recommendations and Best Practices:** Based on security findings, Cloud BOM offers actionable remediation recommendations, ensuring assets adhere to cloud security best practices.
* **Kubernetes Support:** Integration with Kubernetes (EKS, AKS) provides detailed insights into Kubernetes clusters and containers, enhancing visibility into cloud-native applications.

## Understanding Cloud BOM Inventory Data

The main inventory data is presented in the Cloud BOM table, and you can filter the table by column names or by filters on the left.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0bb82a516dcf07e973f89e78a9fd00dcf8747700%2FCBOM%20table.png?alt=media" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="198.51849365234375"></th><th></th></tr></thead><tbody><tr><td><strong>Column Name</strong></td><td><strong>Description</strong></td></tr><tr><td><strong>Issues</strong></td><td>Indicates the number of security issues associated with the asset.</td></tr><tr><td><strong>Service Category</strong></td><td>The type of service the asset belongs to, for example Kubernetes.</td></tr><tr><td><strong>Type</strong></td><td>The specific type of service, such as S3 (Simple Storage Service) in AWS.</td></tr><tr><td><strong>Asset Name</strong></td><td>The name of the asset being analyzed, for example, bank-website-service.</td></tr><tr><td><strong>Cloud Provider</strong></td><td>The cloud service provider hosting the asset, such as AWS.</td></tr><tr><td><strong>Account</strong></td><td>The cloud account identifier associated with the asset.</td></tr><tr><td><strong>Internet Exposed</strong></td><td>Indicates whether the asset is exposed to the Internet, N/A stands for not analyzed for exposure.</td></tr><tr><td><strong>First Seen</strong></td><td>The date or time the asset was first discovered by OX platform, for example, 4 months ago.</td></tr><tr><td><strong>App Name</strong></td><td>The name of the application associated with the asset, for example, OX-Security-Demo/Bank-Website.</td></tr></tbody></table>

### Filtering Cloud BOM Data

| **Filter**                 | **Description**                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Application**            | A filter to search and view assets based on the specific application they are associated with.        |
| **Account**                | A filter to view assets by the cloud account they are associated with.                                |
| **Asset Name**             | A filter to search assets by their unique name.                                                       |
| **Type**                   | A filter to view assets based on their type (e.g., S3, EC2, etc.).                                    |
| **Cloud Provider**         | A filter to view assets based on the cloud provider (e.g., AWS, GCP, Azure).                          |
| **Region**                 | A filter to view assets based on their geographical region.                                           |
| **Service Category**       | A filter to view assets based on their service category (e.g., storage, compute).                     |
| **Kubernetes Cluster**     | A filter to view assets based on the specific Kubernetes cluster they belong to.                      |
| **Vulnerability Severity** | A filter to view assets based on the severity of associated vulnerabilities.                          |
| **Is Internet Exposed**    | A filter to check whether assets are exposed to the internet.                                         |
| **Image Source**           | A filter to search assets by the source of their image (e.g., public, private).                       |
| **Registry Name**          | A filter to search assets by the name of the registry they are stored in.                             |
| **Registry Type**          | A filter to search assets based on the type of registry, for example, ECR.                            |
| **Image Scan Status**      | A filter to view the scanning status of images associated with cloud assets (e.g., scanned, pending). |

### Cloud BOM Individual Asset Info

Depending on the asset type, the OX Security platform presents additional information for each asset in the Cloud BOM table. This information can help the security team conduct more successful investigations and prioritize the handling of security issues.

#### Analyzing Images

The images information can help you understand which images are running in their cloud environment and provide visibility into any potential issues with these images.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-eee4a200a382ca2907cf28d6ccd12dc50b1d1484%2FCBOM_images.png?alt=media" alt=""><figcaption></figcaption></figure>

When relevant, container images are displayed providing key details about the images associated with the selected workload, such as:

* **Image Name**: The name of the container image.
* **Tag**: The version tag for the image.
* **Hash**: The unique hash of the image (if available). Users can click on the hash to be redirected to the Artifact BOM page if the image is from a connected registry.

This provides detailed information about the image, including its associated vulnerabilities, which could pose security risks.

#### Internet Exposure Info

You can click through the exposure path to explore the various components in the route, gaining visibility into how the asset is accessed externally. This info is important for understanding potential vulnerabilities in assets that are publicly exposed, helping you identify and mitigate security risks related to internet-facing assets.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-833472588cd6d79db75445416493f7e3af567128%2FCBOM_exposure.png?alt=media" alt=""><figcaption></figcaption></figure>

For example:

* **Ingress**: The point where external traffic enters the system.
* **Load Balancer**: The device or service routing traffic to the exposed workload.

## Cloud BOM Use Cases

**Filtering by Exposed Assets**

By filtering cloud assets that are exposed to the Internet, organizations can gain better visibility into potentially vulnerable assets, ensuring they are properly secured.

For example, filtering for the assets exposed to the Internet provides a list of assets with a high amount of issues. Now the appsec team can start analyzing these assets.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ee588436e5c21f171b8d5f9ed7d2eb9916f2723e%2FCBOM_exposed_to_internet.png?alt=media" alt=""><figcaption></figcaption></figure>

**Individual Asset Analysis**

This use case enables security teams to filter and review issues associated with specific assets, improving their ability to track vulnerabilities and manage risks at the individual asset level.

For example, here is the asset from the first use case. This asset is exposed to the Internet and also has a lot of issues, so it's worth checking its issues.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f989248fc63307a9d90d8583673e11c89a6632d1%2FCBOM_issues.png?alt=media" alt=""><figcaption></figcaption></figure>

Checking the High severity issues of the asset provides valuable info and focuses the appsec team on the real risks.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b529ba00b9fdfdb31612358e0bae81d9887812e4%2FCBOM_issues1.png?alt=media" alt=""><figcaption></figcaption></figure>
