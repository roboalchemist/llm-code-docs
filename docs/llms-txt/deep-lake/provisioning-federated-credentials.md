# Source: https://docs-v3.activeloop.ai/v3.6.0/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/storage-and-creds/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/google-cloud/provisioning-federated-credentials.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/provisioning-federated-credentials.md

# Provisioning Federated Credentials

## Setting up Federated Credentials in Microsoft Azure

The most secure method for connecting data from your Azure storage to Deep Lake is using Federated Credentials, which are set up using the steps below:

### Step 1: Register Application Credentials with the Microsoft Identity Platform

1\. Login to the Azure account where the App will be registered and where the data is stored.

2\. Go to the `App Registrations` page in the Azure UI, which can be done by searching "App registrations" in the console.

3\. Click on `Register an application` or `New registration`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/PjxaIk8Jke2StcBrNCZW/Screen%20Shot%202023-06-04%20at%208.39.56%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Enter the `Name` and `Supported account type` (`Personal Microsoft Accounts` are not supported) and click `Register`

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/PKFxPWssO1Qi0KUBRatM/Screen%20Shot%202023-06-04%20at%208.47.45%20PM.png" alt=""><figcaption></figcaption></figure>

5\. In the application console, click `Certificates & secrets`. &#x20;

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/dsZ71bdsMy1WsMnMR63w/Screen%20Shot%202023-06-04%20at%209.00.11%20PM.png" alt=""><figcaption></figcaption></figure>

6\. Click on `Federated credentials` and `Add credential`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/ASBMyS0jkT9hPy0y1SKc/Screen%20Shot%202023-06-05%20at%2010.37.45%20AM.png" alt=""><figcaption></figcaption></figure>

7\. Click on `Select scenario` and select `Other issuer`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/BDoabK73TeQXTUki76CH/Screen%20Shot%202023-06-05%20at%2010.41.30%20AM.png" alt=""><figcaption></figcaption></figure>

8\. Enter the following information in the form, and click `Add`.

* **Issuer:** <https://cognito-identity.amazonaws.com>
  * This is for trusting Activeloop's Cognito issuer. There's no need to create AWS Cognito by the user.
* **Subject identifier:** us-east-1:7bc30eb1-bac6-494b-bf53-5747849d45aa
* **Name:** enter a name with your choice
* **Description (optional):** enter description a with your choice
* **Audience:** us-east-1:57e5de2f-e2ec-4514-b9b0-f3bb8c4283c3

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/lXrJRqvXS7ecqP1jboIt/Screen%20Shot%202023-06-05%20at%2010.52.31%20AM.png" alt=""><figcaption></figcaption></figure>

### Step 2a: Apply the Application Credentials to your Azure storage account&#x20;

{% hint style="warning" %}
Skip to 2b if you want to assign Application Credentials to a specific Azure container&#x20;
{% endhint %}

1\. Go to the `Storage accounts` page in the Azure UI, which can be done by searching "Storage accounts" in the console.

2\. Select the `Storage account` to which you want to add Application Credentials.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/vuhEpOETzTJm8ApfZM5j/Screen%20Shot%202023-06-05%20at%203.50.53%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Select `Access Control (IAM)` and click `Add`, and `select Add role assignment`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/nCV1L6AvjqUmaH21kxBp/Screen%20Shot%202023-06-05%20at%204.07.05%20PM.png" alt=""><figcaption></figcaption></figure>

5\. Search and select `Storage Blob Data Contributor` under the role names and click `Next`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/ZkG8IlO9RhHqBSCu1s0w/Screen%20Shot%202023-06-05%20at%204.12.07%20PM.png" alt=""><figcaption></figcaption></figure>

6\. Click on the `Select members` link, and in the tab that opens up on the right, search by name and select the application you created in Step 1. Click `Select` at the bottom of the page.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/ZR1R6Gq0OZM2veNKgIhn/Screen%20Shot%202023-06-05%20at%204.20.14%20PM.png" alt=""><figcaption></figcaption></figure>

&#x20;7\. The application should appear in the list of Members, at which point you can click `Review + assign`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/G5DvmzQ5QCgF95qIuIZK/Screen%20Shot%202023-06-05%20at%204.31.31%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 2b: Apply the Application Credentials to a specific Azure container in your Azure storage account

1\. Go to the `Storage accounts` page in the Azure UI, which can be done by searching "Storage accounts" in the console.

2\. Select the `Storage account` to which you want to add Application Credentials.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/vuhEpOETzTJm8ApfZM5j/Screen%20Shot%202023-06-05%20at%203.50.53%20PM.png" alt=""><figcaption></figcaption></figure>

3. Select the `Container` to which you add the Application Credentials.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/JB0QGF2IVj9N2iabAXIz/Screen%20Shot%202023-06-05%20at%204.48.26%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Select `Access Control (IAM)` and click `Add`, and `select Add role assignment`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/TfC24ITOUF6d2Ay37ECA/Screen%20Shot%202023-06-05%20at%204.56.32%20PM.png" alt=""><figcaption></figcaption></figure>

### IMPORTANT TO PERFORM STEPS BELOW TO COMPLETE 2b - PLEASE DO NOT SKIP

5\. **Perform substeps 5-7 from Step 2a above, in order to add the Application Credentials to the Container**

6\. **Execute the steps in Step 2a above on your Storage Account, except set the Storage Account Role Assignment to `Storage Blob Delegator` in substep 5.**
