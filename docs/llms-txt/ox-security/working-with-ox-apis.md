# Source: https://docs.ox.security/api-documentation/working-with-ox-apis.md

# Working with OX APIs

## Overview of Possible Flows

The OX APIs provide structured access to critical information about applications, artifacts, and security issues. Understanding how these components interact is essential for retrieving relevant data efficiently and ensuring security vulnerabilities are properly assessed.

With OX APIs, you can perform 1000 requests per hour, 15000 per day.

Here is an outline of the key workflows for working with OX APIs, covering four interconnected areas:

1. **Retrieving Application Information:** Understanding available applications and their associated artifacts.
2. **Retrieving Artifact Information:** Digging deeper into artifacts, including repository and deployment details.
3. **Retrieving Issues and Severity Factors:** Identifying security issues and assessing their severity.
4. **Visualizing Attack Paths:** Analyzing how security issues propagate through an environment to prioritize remediation efforts.

Each flow builds upon the previous one, creating a systematic approach to data retrieval and security analysis.

***

### **Flow 1: Retrieving Application Information**

To work with application data:

1. **Call `getApplications` API**: Retrieve a list of all applications, including their **IDs** and **names**.
2. **Identify the relevant application**: Determine which applications are relevant based on their names using the `appName` variable.
3. **Extract the Application ID**: Obtain the ID of the relevant application from the list using the `appId` variable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-31f26afcb2e48280434b8e9dc409e548dd9aa683%2FapplicationsAPI.png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Call `getSingleApplicationInfo` API**: Use the extracted ID to retrieve detailed information about that specific application using the `applicationId` variable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ae3ae0b3a0ebbdfb58955c161aa4ab7f009cdf87%2FSingle_applicationAPI%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Retrieve Related Artifacts**: Extract the **list of artifacts** or **containers** associated with the application from the retrieved details using the `artifacts` variable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-64e2c33b195088bf7e92f47ace903fd476ff4bc6%2FArtifact_info_in_Application.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### **Flow 2: Retrieving Artifact Information**

Once application details are retrieved, artifact information can be accessed as follows:

1. **Call `getArtifacts` API**: Retrieve a list of all artifacts.
2. **Extract Artifact ID**: Identify the relevant artifact ID needed for further details using the `id` variable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fbd0ad8355f4af8e8572d661448f317c0bc594a7%2FArtifacts.png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Call `getArtifact` API**: Use the extracted ID to obtain detailed information about the artifact using the `artifactId` variable.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c4017def46618c9a64f37cb3677399d1b3336308%2FArtifact.png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Key Information in `getArtifact` API Response**:
   * **Cloud deployment information**
   * **List of repositories** `appDescription`
   * **List of registries**

***

### **Flow 3: Retrieving Issues and Severity Factors**

To understand issues affecting applications and artifacts, use the following steps:

1. **Call `getIssues` API**: Retrieve a list of all issues.
2. **Extract Issue ID**: Identify the `issueId` for further investigation.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3c3a07a8d10ded865ecd0943e64a5034cf44c614%2Fgetissues.png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Call `getSingleIssue` API**: Use the extracted ID to obtain detailed information about the issue.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-76b38d8f606189e3249d0262ce777ddd4812b2d5%2FgetsingleIssueInfo%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

1. **Retrieve Severity Factors**: Since severity factors are **not included** in the `getIssues` metadata, they must be retrieved separately from `getSingleIssue`.

***

### **Flow 4: Visualizing Attack Paths with `getIssueGraph`**

Security issues are rarely isolated; they often propagate through dependencies and infrastructure, creating attack paths that can be exploited. The `getIssueGraph` API provides a visualization of these relationships, helping security teams assess risks more effectively.

#### **How `getIssueGraph` Connects Everything**

The attack path graph integrates insights from applications, artifacts, and issues:

* It **links artifacts to vulnerabilities**, showing how weaknesses in a specific component can impact an application.
* It **identifies dependencies** between applications, artifacts, and infrastructure elements, illustrating how a security issue could spread.
* It **prioritizes remediation**, helping teams understand which vulnerabilities pose the greatest risk based on their connectivity and exploitability.
