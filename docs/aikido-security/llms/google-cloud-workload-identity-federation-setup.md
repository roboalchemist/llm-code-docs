# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/gcp/google-cloud-workload-identity-federation-setup.md

# Google Cloud Workload Identity Federation Setup

Google Cloud Workload Identity Federation (WIF) enables you to let Aikido scan your Google Cloud projects without service account keys or any other secrets.

You configure a Workload Identity Federation pool and provider that allow Aikido to exchange its specific credentials for credentials valid in your GCP environment. These are short-lived and not stored anywhere, making this approach much safer and compliant with various compliance requirements.

You can read more about WIF in [the Google Cloud documentation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds).

## **Why Workload Identity Federation?**

* Eliminates long-lived service account keys.
* Simplifies key rotation and secret management.
* Meets stricter compliance and security requirements.

## Getting Started

Workload Identity Federation is available as an option in the Google Cloud onboarding wizard, on the "Configure Access" step.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F5VvIGcQ6CkwsXtUWGI73%2Fimage.png?alt=media&#x26;token=32a761c6-9968-45a7-a983-a56885b08e6b" alt="" width="563"><figcaption><p>Choosing between Service Account and Workload Identity Federation in the Aikido GCP onboarding</p></figcaption></figure>

Aikido will provide the CLI commands needed to set up the workload identity pool and provider in your Google Cloud project.

If you prefer to configure WIF through other means, here are the details you will need:

### Provider Details

{% hint style="info" %}
We highly recommend retrieving these values from the CLI commands offered by Aikido in app.
{% endhint %}

* Provider: **AWS** (this lets Aikido exchange its AWS IAM credentials for GCP credentials)
* AWS account ID: **881830977366** (this is the AWS account from which Aikido will initiate the credential exchange)
* Attribute mapping (these should be the default mappings for AWS):
  * `google.subject` = `assertion.arn`
  * `attribute.aws_role` = `assertion.arn.contains('assumed-role') ? assertion.arn.extract('{account_arn}assumed-role/') + 'assumed-role/' + assertion.arn.extract('assumed-role/{role_name}/') : assertion.arn`

### IAM Permissions

You grant access **only** to the specific Aikido IAM roles that need it, as opposed to all principals from the Aikido AWS account.

Here is how to assemble the principals for the Aikido IAM roles:

`principalSet://iam.googleapis.com/projects/` + `<your_project_number>` + `/locations/global/workloadIdentityPools/` + `<your_wif_pool>` + `/attribute.aws_role/arn:aws:sts::` + `<aikido_aws_acocunt_id>` + `:assumed-role/` + `<aikido_aws_role_name>`

Aikido needs the following permissions at the project or [organization](https://help.aikido.dev/cloud-scanning/connect-your-cloud/gcp/connect-google-cloud-organization) level:

* **Viewer/Reader** (Reader is preferred if it is available) and **Security Reviewer** for the Aikido role `lambda-gcp-cloud-findings-role-1muvqxle`.
* **Artifact Registry Viewer** for:
  * If you want Aikido to scan your container images from Artifact Registry for the Aikido role `lambda-container-image-scanner-role-pb0qotst`.
  * Or, if you only want Aikido to ingest findings from Artifact Registry Vulnerability Scanning for the Aikido role `lambda-gcp-cloud-findings-role-1muvqxle`.

{% hint style="info" %}
If your project or organization IAM policy already contains **conditional bindings**, `gcloud` requires all new bindings to explicitly specify a condition.

When applying the IAM bindings for Aikido, make sure to **explicitly disable conditions**. You can do this by adding `--condition=None` to the `gcloud` command, or by selecting **None** when prompted by the CLI.
{% endhint %}

Once the Workload Identity Federation pool and provider, together with the IAM permissions are configured, you will generate the config file that you will upload in Aikido. The recommended and simpler approach is **direct access** (as opposed to service account impersonation).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FTyNJm35QKpqd5KVOsTSK%2Fimage.png?alt=media&#x26;token=580623a9-e826-439a-853c-724fe0f626bc" alt="" width="563"><figcaption><p>Google Cloud WIF config file generation using direct access</p></figcaption></figure>

## FAQs

* **Can I migrate already connect GCP projects from service account to WIF?**

Yes. You can configure WIF in your project by following the in-app steps and, instead of completing the onboarding, update the credentials of your already connected GCP project with the generate config file.

* **Can I use an already existing WIF pool?**

Yes, you can add a new provider to one of your WIF pools. You will need to adjust the CLI commands to use the name of your existing pool.

* **Should I also configure attribute conditions on the WIF provider?**

Since you already grant access only to specific Aikido principals (as opposed to the entire WIF pool), [attribute conditions](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions) become less critical. However, if your policy mandates them, you can add conditions for the two IAM roles mentioned above.

* **Can I configure access through service account impersonation instead of direct?**

Yes, though direct access is simpler. Use impersonation if your organization mandates that all external identities act through a service account. You can create a service account, allow the Aikido principals mentioned above to impersonate it (`roles/iam.workloadIdentityUser`), grant it the required IAM permissions, and generate the config file for the service account.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fm4ElGTtvly6g6bK5RAVg%2Fimage.png?alt=media&#x26;token=fc4efb6a-e56c-49c6-ad42-609a980843d0" alt="" width="375"><figcaption><p>Generating the config file for a service account</p></figcaption></figure>
