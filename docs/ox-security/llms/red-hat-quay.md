# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/red-hat-quay.md

# Red Hat Quay

Integrating Red Hat Quay with OX Security's Active Application Security Posture Management (ASPM) Platform enhances your organization's container image security and management.

Red Hat Quay is a scalable, security-focused container image registry designed for storing, building, and distributing container images across enterprise environments.

As a fully-featured registry, Quay provides robust capabilities, including automated vulnerability scanning, image signing, access control, and geo-replication, making it a preferred choice for organizations that prioritize security and compliance.

By integrating Red Hat Quay with OX Security's Active ASPM Platform, organizations can achieve:

* **Unified Visibility**: Consolidate data from Quay and other sources to gain a comprehensive view of your container images and their security posture.​
* **Automated Vulnerability Management**: Leverage OX Security's capabilities to continuously monitor and prioritize vulnerabilities detected in container images stored within Quay.​
* **Streamlined Compliance**: Ensure that container images meet organizational and regulatory compliance standards through automated policies and reporting.

## Prerequisites

* Red Hat account.

## Connecting to Red Hat Quay

1. In the **OX app**, go to **Connectors** and search for Red Hat Quay.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bf58f1f15208978ce2d703e56b1451f12c69208d%2FQuay%20icon.png?alt=media" alt="" width="186"><figcaption></figcaption></figure>

1. Select **Red Hat Quay** and The **Configure your Red Hat Quay credentials** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4a7bc97951c11873bfe4bfeb6054744bc01a16c5%2FConfig_credentials.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

| Parameter                 | Description                                |
| ------------------------- | ------------------------------------------ |
| **Red Hat Quay Host URL** | Add your Red Hat account URL.              |
| **Token**                 | Paste the token you have created.          |
| **Token Name**            | The name is generated automatically by OX. |

1. Select **CONNECT**. The Red Hat Quay connector is configured.

<mark style="color:red;">need to rewrite this part:</mark>

1. <mark style="color:red;">Sign in to Quay account.</mark>
2. <mark style="color:red;">Select organization.</mark>
3. <mark style="color:red;">Go to 'Applications' and create new application.</mark>
4. <mark style="color:red;">Select application and press 'Generate Token'.</mark>
5. <mark style="color:red;">Set 'View all visible repositories' and 'Read User Information' checkboxes.</mark>
6. <mark style="color:red;">Press 'Generate Access Token'.</mark>

Querying and managing container images in a registry

## How the Integration Works

Quay projects are associated with images, which accumulate over time as new commits are made.

OX connects to the registry and starts managing images created each time a developer pushes new code.

### Configuring which images to retain

By default, OX Security selects and retains the last image from each project. You can configure which images to retain.

You can specify images to scan based on tags, allowing different versions to be stored for different customers or environments.

**To configure images for scanning:**

1. In the **OX app**, go to **Settings > Scan > Container Security > Enter Regex for Container Scanning**.
2. To select container images that you want to include in the scan, enter a regex pattern and select **UPDATE**.

### Extending retention period

By default, only images from the last six months are retained. You can extend the retention period if needed.

The system automatically deletes the latest images unless configured otherwise. Images older than six months are removed by default unless you specify a longer retention period.

If a project has no new commits for six months, its images are not deleted.

**To change the retention period:**

1. In the **OX app**, go to **Settings > Scan > Container Security > Container Age Threshold for Scanning.**
2. Set the number of months after which the container is excluded from scan.
3. **Database & Requirements**:
   * A database is needed for this functionality.
   * The system is mostly self-sufficient beyond this requirement.
4. **Upcoming Feature on Unscanned Containers**:
   * A new feature related to unscanned containers is being introduced.
   * A new screen will display information about why certain images were not deleted.
   * This screen will include image details such as name, tag, creation date, and the reason for retention.
5. **Conclusion**:
   * The logic ensures that only relevant images are retained while providing users with flexibility in configuration.
   * The system balances automated cleanup with user-defined retention rules.
   * Future updates will enhance visibility into image retention decisions.

##
