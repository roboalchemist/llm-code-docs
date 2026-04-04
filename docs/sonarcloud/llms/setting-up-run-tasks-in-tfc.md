# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/advanced-administration/setting-up-run-tasks-in-tfc.md

# Setting up run tasks in TFC

{% hint style="info" %}
Currently, SonarQube Cloud only supports GitHub and GitLab for use with the TFC integration.
{% endhint %}

The run task allows Terraform Cloud (TFC) to interact with SonarQube Cloud at a specific point in the TFC run lifecycle. It retrieves the status of the latest SonarQube Cloud scan results and communicates the pass/fail result to Terraform, blocking the TFC workflow if the quality gate has failed. This ensures that no infrastructure changes in Terraform can take place until all unreviewed hotspots or security vulnerabilities within the code analyzed by SonarQube Cloud have been reviewed and remedied.

The process for integrating SonarQube Cloud into your TFC workflow consists of the steps described below.

{% stepper %}
{% step %}

### Generate an HMAC key

You must generate the HMAC key which will be used to authenticate SonarQube Cloud to TFC.

To ensure the security of your integration, you must use a high-entropy secret key. Do not use human-readable passwords or phrases. According to [NIST SP 800-107](https://csrc.nist.gov/pubs/sp/800/107/r1/final), the key should be randomly generated and at least as long as the hash output (e.g., 32 bytes for SHA-256).

Below is a recommended command to generate a compliant key.

```bash
# Generates a 32-byte key in Hex format (secure for HMAC-SHA256)
openssl rand -hex 32
```

{% endstep %}

{% step %}

### Configure the run task integration in SonarQube Cloud

You must have administrator permissions for your organization to be able to configure the Terraform Cloud integration.

Proceed as follows:

1. In SonarQube Cloud, retrieve your project. For more information, see [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention").
2. Go to **Administration** > **General settings** > **Integration.**
3. In **Terraform Cloud Run Task HMAC Key**, enter the HMAC key you generated in [#generate-an-hmac-key](#generate-an-hmac-key "mention") above.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4c93ec7c468220a47e4ca935fc54b3039fb71f93%2F2da33468520b67b3889c4640edf748a2ec03c2c7.png?alt=media" alt="Where to add your Terraform HMAC Key in the SonarQube Cloud UI." width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Configure the Terraform Cloud workspace to use the run task

You must create a new run task for SonarQube Cloud within TFC using the URL and HMAC key values from SonarQube Cloud. Note that these steps take place within TFC. For more details on Terraform and the Terraform Cloud workflow, see HashiCorp’s articles on run tasks in the [Terraform help center.](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/run-tasks)

To create the run task:

1. In [Terraform Cloud](https://app.terraform.io/), navigate to your organization’s global settings.
2. When logged in to your Terraform account, go to the run tasks settings for your TFC organization: `https://app.terraform.io/app/{YOUR_TFC_ORG}/settings/tasks`.
3. Go to **Settings** > **General** > **Run tasks** > **Create run task.**
4. In the on-screen form, edit the following fields:
   * **Name** (required)
   * **Endpoint URL** (required)**:** The URL endpoint configured in the run task to send requests to. Enter `https://api.sonarcloud.io/ci-interface/htc-integration/run-tasks`
   * **Description** (optional)
   * **HMAC key** (required): HMAC key you generated in [#generate-an-hmac-key](#generate-an-hmac-key "mention") above.\
     This field is required because the SonarQube Cloud project needs to validate the HMAC key with the one in the TFC workspace.
5. Choose **Create** to complete the configuration of your run task.

The run task is now available within the organization, and you can associate it with one or more workspaces. Go to the [Terraform Cloud registry](https://registry.terraform.io/browse/run-tasks?page=2) to view all available run tasks.
{% endstep %}

{% step %}

### Associate the TFC run task with your client workspace

Associate your newly-created run task with the TFC workspace that will use the run task:

1. In Terraform Cloud, click **Workspaces** and then go to the workspace where you want to associate your run tasks.
2. Go to **Settings** > **Run Tasks.**\
   The run task you created is available under **Available Run Tasks.** Click the ✚ next to the run task you want to add to the workspace.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4cca55640ff810a02a2eaf19c9846ee91f58e1c1%2Feb82bd6b7ee0e56ed6ff68444c599e4a10bd237a.png?alt=media" alt="Choose the correct Run stage for the SonarQube Cloud task in Terraform." width="563"><figcaption></figcaption></figure></div>

3. Select **Pre-plan** to indicate when Terraform Cloud should start the run task.
4. Select the Enforcement level **Mandatory**. If the task fails, the run will enter an errored state with a warning in the UI.
5. Click **Create** to complete the configuration of your run task.
   {% endstep %}
   {% endstepper %}

### Viewing the run task result

SonarQube Cloud will scan all Terraform plans on each push within your workspace.

If all goes well, you will receive a success message.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-68887c7a7df287f26741e2f19ada4d3a521cd89e%2Ff2075f267899345d63306569790a68d411ec56d8.png?alt=media" alt="Your SonarQube Cloud run task has passed the Pre-plan!" width="563"><figcaption></figcaption></figure></div>

If the run task has failed, then you will received a failure message and you will need to go back to SonarQube Cloud and address whatever caused your quality gate to fail.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-913d5cb1dca564f4e88f5105cfcf548e1cc46b2a%2Fa123f0527b215e63216c77fcc5b05d23cc947f76.png?alt=media" alt="Your SonarQube Cloud run task has failed the Pre-plan." width="563"><figcaption></figcaption></figure></div>
