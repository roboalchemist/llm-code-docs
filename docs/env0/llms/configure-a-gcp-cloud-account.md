# Source: https://docs.envzero.com/guides/cloud-compass/cloud-compass/configure-a-gcp-cloud-account.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure a GCP Cloud Account

> Connect your GCP project to env zero Cloud Compass with Cloud Logging API and service account

## Configure a Cloud Account

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/f21ecc5cfaa193a33f4100a3d4f8f092b3ab8830d2bb9008758ff2dfac0e2d0d-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=8d94993433def6aef3112c9c2208aee8" alt="" width="1416" height="641" data-path="images/guides/cloud-compass/cloud-compass/f21ecc5cfaa193a33f4100a3d4f8f092b3ab8830d2bb9008758ff2dfac0e2d0d-image.png" />

### Requirements

To successfully integrate your GCP account with env zero, ensure the following prerequisites are met in your GCP project:

#### Enable Cloud Logging API for your GCP project

The Cloud Logging API must be enabled for your GCP project to allow env zero to read log data.

* Verify the Cloud Logging API status
  * If not enabled, proceed to enable it.

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/46234e129ab59f4c9f0d16bb1a2483af3a8922c004f08c8f30fd3a4dc257e4dc-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=db4e8d7f759d86bf8cd2217cef19bb4a" alt="" width="1003" height="396" data-path="images/guides/cloud-compass/cloud-compass/46234e129ab59f4c9f0d16bb1a2483af3a8922c004f08c8f30fd3a4dc257e4dc-image.png" />

#### Create a Service Account with permissions to read logs

You need a dedicated Service Account that env zero will use to read logs from your GCP project.

* Navigate to IAM & Admin > Service Accounts in the GCP Console
* Create a new `Service Account`
* Ensure this Service Account is granted permissions to read logs. The [predefined roles/logging.viewer role](https://cloud.google.com/logging/docs/access-control#logging.viewer) is recommended for this purpose as it provides necessary read access to logs

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/616c5703d5046341d005d904b9b479ffc01d17a2f3af1e2a1c985287fc8b87ab-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=93cf18c61df8fd85bd24b448024ef968" alt="" width="626" height="333" data-path="images/guides/cloud-compass/cloud-compass/616c5703d5046341d005d904b9b479ffc01d17a2f3af1e2a1c985287fc8b87ab-image.png" />

#### Create a Workload Identity Pool and OIDC Provider

Workload Identity Federation enables secure, keyless authentication for external identities like env zero.

* Navigate to IAM & Admin > Workload Identity Federation
* Create a new `Workload Identity Pool`
* Within this pool, create a new `Workload Identity OIDC Provider`
* For detailed instructions on this process, refer to the [env zero guide on OIDC with Google Cloud Platform](/guides/integrations/oidc-integrations/oidc-with-google-cloud-platform/#workload-identity-federation-pool-and-provider).

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/ad4832f35bd92ca701831098540ba162505c1078585fc7c63e2d82782ae6ef07-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=d5c2f4fe98df37964a2841ac3d1b54a7" alt="" width="1436" height="401" data-path="images/guides/cloud-compass/cloud-compass/ad4832f35bd92ca701831098540ba162505c1078585fc7c63e2d82782ae6ef07-image.png" />

#### Grant impersonation rights to the OIDC principal on the Service Account

This step connects your newly created Service Account with the Workload Identity Pool, allowing env zero (via the OIDC provider) to impersonate the Service Account and assume its permissions.

* From within your `Workload Identity Pool`, click on `Grant Access`
* Select the `Grant access using service account impersonation` radio button
* Choose the `Service Account` you created
* For the `Subject` value, copy it directly from the env zero application by clicking on `Show OIDC` Token in the Cloud Account Wizard. This value uniquely identifies the env zero organization within your OIDC setup

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/8e6023e6f25256e534c071bb22acb2bcad7b06e5641dfaf9fc99fa6ef8dcaa7b-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=d25ff2ecbf79ee2218dd4c9936ee6900" alt="" width="590" height="821" data-path="images/guides/cloud-compass/cloud-compass/8e6023e6f25256e534c071bb22acb2bcad7b06e5641dfaf9fc99fa6ef8dcaa7b-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/0bbdfe9b899642ba3de7680f4a7e0488343437e1e7d9ad87d791e584e488a206-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=c503a5d674f3c20b6c67b95a31396117" alt="" width="782" height="365" data-path="images/guides/cloud-compass/cloud-compass/0bbdfe9b899642ba3de7680f4a7e0488343437e1e7d9ad87d791e584e488a206-image.png" />

#### Setting Up Access Configuration

Once the GCP prerequisites are satisfied, you will configure the Cloud Account in env zero.

##### Fill the Account Config form

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/f1ffd2b0d5df98fdfd3d9ee5c7ec263b446efdd0b9029c0178a6c2131bfb31e0-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=7b7c78eb13e7eb046bfb089a30d1af5c" alt="" width="1418" height="574" data-path="images/guides/cloud-compass/cloud-compass/f1ffd2b0d5df98fdfd3d9ee5c7ec263b446efdd0b9029c0178a6c2131bfb31e0-image.png" />

In the env zero Cloud Account configuration form, you'll need to specify the following details:

`Account name`: A descriptive name for your account in env zero (for identification purposes only)

`Project ID`: Your Google Cloud Project ID (the alphanumeric string identifier)

`JSON configuration file content`: The content of the credential configuration file, explained in the next step.

##### Download the JSON configuration file content

This JSON file contains the necessary credentials for env zero to authenticate with your GCP Workload Identity Pool Provider.

* In your `Workload Identity Pool`, navigate to the `Connected Service Accounts` tab
* Locate the `Service Account` you connected to the pool and click the `Download` button next to it
* In the download dialog:
  * Select the `OIDC provider` you previously created
  * Enter "file.json" in the `OIDC ID token path` field
  * Select "json" in the `Format type` dropdown
  * Keep "access\_token" as the value in the `Subject` token field name
  * Click `Download config`

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/fabf87b66e0770b8c777b8d64d51e43ed5280dc2f1a009c7b516367150f313c5-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=fc0d5180f1108a0b13e754518ca9981d" alt="" width="639" height="749" data-path="images/guides/cloud-compass/cloud-compass/fabf87b66e0770b8c777b8d64d51e43ed5280dc2f1a009c7b516367150f313c5-image.png" />

Built with [Mintlify](https://mintlify.com).
