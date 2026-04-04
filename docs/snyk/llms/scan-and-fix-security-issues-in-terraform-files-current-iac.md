# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-terraform-files/scan-and-fix-security-issues-in-terraform-files-current-iac.md

# Scan and fix security issues in Terraform files

Snyk scans your Terraform code for misconfigurations and security issues as well. After scanning configuration files, Snyk reports on any misconfigurations based on the settings your administrator implemented, and makes recommendations for fixing accordingly.

## Prerequisites for scanning and fixing issues in Terraform files in SCM repositories

* An administrator should integrate your Organization with your preferred Git repository and enable detection of configuration files as described on [Configure your integration to find security issues in your Terraform files](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-terraform-files/configure-your-integration-to-find-security-issues-in-your-terraform-files-current-iac)
* You must have a Snyk account, and your Terraform files should be in `.tf` format.
* Snyk detects AWS, Azure, and Google Cloud-related security issues.

## Scan and fix your Terraform configuration files

* Log in to your account and navigate to the relevant Group and Organization that you want to manage.
* If you imported your repositories for testing before the infrastructure as code feature was enabled by your administrator, from the **Add project** screen, re-import that repository in order to detect the Terraform code:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5f44f056215677b57605c2cdced3cf0ca15d2ce6%2Fscreenshot_2020-07-09_at_12.44.03%20(1)%20(1)%20(3)%20(3)%20(2)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20%20%20(1).png?alt=media" alt="Add project screen"><figcaption><p>Add project screen</p></figcaption></figure>

Every time a repository is scanned, every Terraform file is imported as a separate Project, grouped together per repository, similar to the example shown.

If you re-imported the repository in order to import the Terraform files, then Snyk imports and re-tests the already imported application manifest files, displaying the test time as "now".

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-97edd1815b8c2bb763b0d4f1ff9f909108a957be%2Fimage%20(63).png?alt=media" alt="List of Terraform Projects"><figcaption><p>List of Terraform Projects</p></figcaption></figure>

* Click the link for the Project of interest to you to view the scan results and to help correct your Terraform code:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-82814b57108d473fdd2739f8e1a97377a502e719%2Fimage%20(340).png?alt=media&#x26;token=9aef4451-6e45-4cd0-ad47-65c9d4544fdb" alt="Terraform Project detail"><figcaption><p>Terraform Project detail</p></figcaption></figure>
