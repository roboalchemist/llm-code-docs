# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/cloud-platform-integrations/google-cloud-integration/google-cloud-integration-web-ui/step-3-create-and-scan-a-cloud-environment-for-google-web-ui.md

# Step 3: Create and scan a Cloud Environment for Google (Web UI)

{% hint style="info" %}
**Recap**\
You have created the Google service account for Snyk. Now you can create and scan a Cloud Environment.
{% endhint %}

To create and scan a Cloud Environment for Google, you must provide the Google service account's email address and your project ID.

1. In the Snyk Web UI **Add Google Cloud Environment** modal where you downloaded the service account template, enter your service account email in the **Service account email** field.\
   For example, `"`[`snyk-cloud-mt-us-abcd1234@my-project.iam.gserviceaccount.com`](mailto:snyk-cloud-mt-us-abcd1234@my-project.iam.gserviceaccount.com)`"`
2. Enter the identity provider in the **Identity provider** field. This must be a full URL including workload identity pool ID, identity provider ID, and project ID.\
   For example, `"`[`https://iam.googleapis.com/projects/12345567/locations/global/workloadIdentityPools/workload-identity-123456/providers/identity-provider-123456`](https://iam.googleapis.com/projects/12345567/locations/global/workloadIdentityPools/workload-identity-123456/providers/identity-provider-123456)`"`
3. Optionally, enter an environment name. If one is not provided, Snyk will use your Google Project name.
4. Select **Approve and begin scan**.
5. You will see a confirmation message: **Google Cloud environment successfully added**.\
   Select **Add another environment** to return to the **Add Google Cloud Environment** modal and onboard a new account, or select **Go to settings** if you are finished:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4c09a69eb70b3851cb86db2857916c83e122fc63%2Fsnyk-cloud-onboard-google-ui-success.png?alt=media" alt=""><figcaption><p>Success message after adding a Google Cloud environment in the Snyk Web UI</p></figcaption></figure>

{% hint style="info" %}
It can take Google 60 seconds or more to create your service account. If you try to create an environment immediately after you create a service account and you receive a "could not validate credentials" error, wait at least 60 seconds and try again.
{% endhint %}

**What's next?**

You can now do the following:

* View the cloud configuration issues Snyk finds. See [Manage cloud issues](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-issues).
* Prioritize your vulnerabilities with cloud context.
