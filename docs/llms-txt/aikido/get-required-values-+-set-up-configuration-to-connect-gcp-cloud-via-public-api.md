# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/gcp/get-required-values-+-set-up-configuration-to-connect-gcp-cloud-via-public-api.md

# Get Required Values + Set Up Configuration to Connect GCP Cloud via Public API

Login to your [Google Cloud](https://console.cloud.google.com/) and click your **project name** in the header to open the resource selection modal.

Select the project you want to add and save your **project id**

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FsuzAmHF2dpYQiRhUK9qG%2Fimage.png?alt=media&#x26;token=7449b842-ff55-4313-97fd-091e2dab0372" alt=""><figcaption></figcaption></figure>

Activate a cloud shell&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXl4MGFN8oM4gAL31tXHU%2Fimage.png?alt=media&#x26;token=8ff918f7-bedc-41f1-8ca9-1d9c028efcc8" alt=""><figcaption></figcaption></figure>

Paste and execute following command. A success message should be visible.

```
gcloud services enable compute.googleapis.com storage-component.googleapis.com iam.googleapis.com container.googleapis.com logging.googleapis.com monitoring.googleapis.com cloudresourcemanager.googleapis.com cloudkms.googleapis.com bigquery-json.googleapis.com dns.googleapis.com sqladmin.googleapis.com
```

Create a [service account](https://console.cloud.google.com/iam-admin/serviceaccounts/create). You can freely name the account but we recommend having **aikido** in it.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ft0YwZmscxdXgEkdpxDm7%2Fimage.png?alt=media&#x26;token=8eae8b9e-f28e-4916-bc3e-f5efcce24ff0" alt="" width="375"><figcaption></figcaption></figure>

Add both **Security Reviewer** and **Viewer** roles

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fnyp8PPohC2AWyAW6gNbs%2Fimage.png?alt=media&#x26;token=8bb19d06-ac49-4ee1-8ce6-731eb8081bf8" alt="" width="375"><figcaption></figcaption></figure>

Click **done**, step 3 of the create service account can be skipped

Navigate to the detail page of the newly created service account

Go to the **Keys** tab and **create a new key**

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FFTJ7NiASPp8jEfK7RJNt%2Fimage.png?alt=media&#x26;token=0830d03d-4aef-47f8-8552-f2b2553892e9" alt="" width="375"><figcaption></figcaption></figure>

Select the **JSON** option. A json-file should be downloaded. Save this file.

You can now connect this cloud to Aikido using the public API.
