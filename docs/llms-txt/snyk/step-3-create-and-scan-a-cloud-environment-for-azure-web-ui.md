# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/azure-integration-for-cloud-configurations/azure-integration-web-ui/step-3-create-and-scan-a-cloud-environment-for-azure-web-ui.md

# Step 3: Create and scan a Cloud Environment for Azure (Web UI)

{% hint style="info" %}
**Recap**\
You have created the Azure app registration, federated identity credential, and service principal for Snyk. Now you can create and scan a Cloud Environment.
{% endhint %}

The steps follow to create and scan a Cloud Environment for Azure using the Web UI.

1. In the Snyk Web UI **Add Azure Environment** modal where you downloaded the Terraform template or Bash script, enter your application ID in the **Application ID** field.
2. Optionally, enter an environment name. If one is not provided, Snyk will use your subscription name.\
   ![Enter Application ID section of the Add Azure Environment modal in Snyk Cloud](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a0cbbee055965c6dda1d213dc418f55d2ce2ca71%2Fsnyk-cloud-onboard-azure-step-2.png?alt=media)
3. Select **Approve and begin scan**.
4. You will see a confirmation message: "Azure environment successfully added." Select **Add another environment** to return to the **Add Azure Environment** modal and onboard a new subscription, or select **Go to settings** if you are finished.

You can now do the following:

* View the cloud configuration issues Snyk finds. See [Manage cloud issues](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-issues).
* Prioritize your vulnerabilities with cloud context.
