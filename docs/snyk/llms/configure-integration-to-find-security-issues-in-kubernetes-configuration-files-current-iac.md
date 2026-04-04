# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-kubernetes-configuration-files/configure-integration-to-find-security-issues-in-kubernetes-configuration-files-current-iac.md

# Configure integration to find security issues in Kubernetes configuration files

Snyk tests and monitors Kubernetes configurations stored in your source code repositories and provides information, tips, and tricks to better [secure a Kubernetes environment](https://snyk.io/learn/kubernetes-security/). This helps to catch misconfigurations before they are pushed to production, as well as provide fixes for vulnerabilities.

## Supported Git repositories and Kubernetes file formats

Snyk scans your Kubernetes configuration files in JSON and YAML format when they are imported from your integrated Git repository.

## Configure Snyk to scan Kubernetes configuration files

### **Prerequisites for scanning Kubernetes configuration files**

* Administrator access for the Organization
* Git repository access and authorization\
  For details, see [Git repository (SCM) integrations](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations).

### **Configure Snyk to scan Kubernetes configuration files**

* Log in to the Snyk Web UI ([app.snyk.io](https://app.snyk.io)), and navigate to the relevant Group and Organization that you want to manage.\
  Integrations are managed per Organization.
* To enable Snyk to detect Kubernetes configuration files, in the Infrastructure as Code settings, toggle the setting to enable Snyk to detect Infrastructure as code files.
* If needed, review and adjust the **Infrastructure as code** **Severity settings** on the Kubernetes tab in the example.\
  Check to select the file types to scan, CloudFormation, Terraform, or both, and from the pulldown selection, choose the severity level for each Deployment.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bfc09aafde0e7e940faaf3b9e0ed7ad7663e7721%2Fimage.png?alt=media" alt="Select Severity settings for IaC scans"><figcaption><p>Select Severity settings for IaC scans</p></figcaption></figure>

The number of tests you can run per product is based on your account plan. For details, see the [plans and pricing](https://snyk.io/plans/) page.
