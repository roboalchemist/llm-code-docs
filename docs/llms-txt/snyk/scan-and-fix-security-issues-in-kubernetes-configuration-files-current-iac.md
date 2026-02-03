# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-kubernetes-configuration-files/scan-and-fix-security-issues-in-kubernetes-configuration-files-current-iac.md

# Scan and fix security issues in Kubernetes configuration files

Snyk Infrastructure as Code scans your manifest files for security vulnerabilities and scans your Kubernetes configuration files for misconfigurations and security issues as well. After configuration files are scanned, Snyk reports on any misconfigurations based on the settings your administrator has implemented and makes recommendations for fixing accordingly.

## Prerequisites for scanning and fixing issues in Kubernetes files

* An administrator should [integrate your Organization](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-terraform-files/configure-your-integration-to-find-security-issues-in-your-terraform-files-current-iac) with your preferred Git repository and enable the detection of configuration files.
* You must have a Snyk account, and your configuration files should be in either JSON or YAML format.

Snyk Infrastructure as Code supports:

* Deployments, Pods, and Services.
* CronJobs, Jobs, StatefulSet, ReplicaSet, DaemonSet, and ReplicationController.

## Scan and fix your Kubernetes configuration files

* Log in to your account and navigate to the relevant Group and Organization that you want to manage.
* If you imported your repositories for testing before cloud configuration file detection was enabled by your administrator, re-import that repository to import the relevant JSON or YAML configuration files.

Every time a repository is scanned, every supported manifest file and every supported configuration file is imported as a separate Project, grouped together per repository.

When you re-import the repository in order to import the cloud configuration files, Snyk imports and tests the configuration files and re-tests the already imported application manifest files, displaying the test time as "now".

* Click the link for the Project of interest to you to view the scan results and to correct your configuration files accordingly:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4c724974942aad93a88db6f17dae6487e129b155%2Fimage%20(343).png?alt=media&#x26;token=a96fa62b-7e7f-40f9-b251-039c189a40de" alt="Kubernetes Proejct detail"><figcaption><p>Kubernetes Proejct detail</p></figcaption></figure>
