# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/azure-pipelines-and-azure-devops/ox-scan-extension-for-azure-devops.md

# OX Scan Extension for Azure DevOps

OX Security provides an Azure DevOps extension that directly integrates with your pipeline, allowing security scans to be part of your CI/CD process. This integration method is suitable for broader DevOps enhancements, including security across various areas.

The overall process involves installing the OX Security Scan Extension from the Azure Marketplace, then authorizing it in your Azure DevOps environment.

Following installation, you integrate the extension by creating a service connection with your OX API key, configuring necessary settings, and optionally granting permissions for broader project access.

### Installing OX Security Scan Extension

1. To install the extension from the Azure Marketplace, follow the process [OX Security Scan Extension](https://marketplace.visualstudio.com/items?itemName=oxsecurity.ox-security-scan-task).
2. To authorize the extension:

   a. Go to **Azure Organization Settings** → **Extensions**.

   b. Select **OX Security Scan Extension**.

   c. Ensure there is no **Authorize** button next to the extension name (this confirms authorization is complete).

### Integrating OX Security Scan Extension in your Azure DevOps environment

#### Step 1: Creating a service connection

1. Navigate to:\
   **Azure Project** → **Project Settings** → **Service connections** → **New service connection**.
2. Search for **OX** and select **OX Security Authentication**.
3. Configure the connection:
   * Keep the default **Server URL**.
   * Enter your [**OX API key**](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/creating-ci-cd-integration-key).
   * Set a **Service connection name**.
4. Optional settings:
   * Enable **Grant access permission to all pipelines**.\
     [Learn more](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/repository-resource?view=azure-devops#add-pipeline-permission-to-a-repository-resource)
   * Share the service connection across projects:\
     [Learn more](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/permissions?view=azure-devops#set-service-connection-project-permissions)

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fc06f1a8e42eac660c2997c0a72232d73026afa7%2FAzureDevOps1.png?alt=media" alt="" width="449"><figcaption></figcaption></figure>

#### Step 2: (Optional) Adding branch [build validation](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops\&tabs=browser#build-validation) policies

This step allows enforcing scans before merging pull requests.

#### Step 3: Adding the OX scan task to your Azure pipeline

1. Edit your [Azure pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops).
2. Search for **OX** and [select the **OX Security Scan** task](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/tasks?view=azure-devops\&tabs=yaml).
3. Under **API key**, choose the previously created **Service Connection**.
4. Review and configure other task properties.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8632448a0e1e2b79cd77d0b37f8fedc2f490e6f3%2FAzureDevOps_scan_task.png?alt=media" alt="" width="269"><figcaption></figcaption></figure>

| Step Number      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| General Settings | [Make sure the settings are the same as in the General Settings in OX Security.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/pipeline-scan-settings)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Advanced         | <ul><li><strong>Enable debug mode</strong><br>Turns on detailed logging to help troubleshoot issues during pipeline scan execution. Use this option only for debugging, as it may generate verbose internal logs.</li><li><strong>Disable SSL validation</strong><br>Skips SSL certificate validation when connecting to external services. Recommended only for testing or non-production environments where SSL certificates may not be trusted.</li><li><strong>Override blocking issues</strong><br>Allows the pipeline to continue even if blocking security issues are detected. Useful in development or staging environments where you want to test despite unresolved issues.</li></ul> |

1. Each field includes a short description accessible using the ⓘ icon.
2. Add the task as a pipeline step.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6f053357a7d34025df18c08a8cfdac4c34d2358c%2FAzureDevOps2%20(1).png?alt=media" alt="" width="396"><figcaption></figcaption></figure>

* After adding the scan task, you see the **OXSecurityScan** step in your pipeline run.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f284811bd0a9e37ad428d8f0861888a04e418714%2FAzureDevOps3.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* When the scan completes, a new **OX Security Scan** tab appears in the Azure DevOps pipeline interface, showing scan results.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-66fc1343120a1179e219ae33c38dee5023aebae8%2FAzureDevOps4.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
