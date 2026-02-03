# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/terraform-cloud-integration-for-snyk-iac-using-run-tasks/set-up-the-terraform-cloud-integration-for-iac.md

# Set up the Terraform Cloud integration for IaC

{% hint style="warning" %}
You must be an administrator of the Snyk Organization to configure the Terraform Cloud integration.
{% endhint %}

From the **Integrations** page in the Snyk Web UI, navigate to the dedicated Terraform Cloud integration settings page, and follow the steps on this page to set up Terraform plan scanning.

In the Snyk Web UI, go to the Terraform Cloud integration settings page for your organization:\
`https://app.snyk.io/org/{YOUR-SNYK-ORG}/manage/integrations/terraform-cloud` to find the provided URL and HMAC Key.

![Snyk Integration settings for Terraform Cloud](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c5e04daa809f7cdd73de03202f1ec7d64af11894%2Fterraform_cloud.png?alt=media)

## Create the Snyk Run Task for Terraform Cloud

Now navigate to [Terraform Cloud](https://app.terraform.io) in the organization global settings:

![Terraform Cloud Settings](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-70d4402b6f140052c85d88eaadccf22e74cf5113%2Fimage.png?alt=media)

1. Go to the run tasks settings for your TFC organization:\
   `https://app.terraform.io/app/{YOUR_TFC_ORG}/settings/tasks`
2. Create a new run task for Snyk with the URL and HMAC key values.\
   The HMAC key is mandatory for the Snyk integration to work, even though it is identified as optional on Terraform Cloud.

## Associate the Run Task with your Terraform Cloud Workspace

1. Navigate to your Terraform Cloud Workspace, enter the **Settings** \_\_ menu, and choose **Run Tasks***.*
2. Find the run task you created under **Available Run Tasks**; click on **+** to associate it.
3. Choose the enforcement level (**Advisory** or **Mandatory**) and click **Create**.

After your integration is set up, Snyk scans Terraform plans for each run triggered in your workspace.
