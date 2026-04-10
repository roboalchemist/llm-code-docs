# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/user-authentication/workload-identities.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/authentication/workload-identities.md

# Source: https://docs-v3.activeloop.ai/setup/authentication/workload-identities.md

# Workload Identities (Azure Only)

## Authenticating Using Workload Identities Instead of User Credentials

Workload identities enable you to define a cloud workload that will have access to your Deep Lake organization without authenticating using Deep Lake user tokens. This enables users to manage and define Deep Lake permissions for jobs that many not be attributed to a specific user.&#x20;

Set up a Workload Identity using the following steps:

1. Define an Azure Managed Identity in your cloud
2. Attached the Azure Managed Identity to your workload
3. Create a Deep Lake Workload Identity using the Azure Managed Identity
4. Run the workload in Azure

### Step 1: Define the workload identity in Azure

1. Navigate to Managed Identities in Azure

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/i2UGqKFRudC154twXDDb/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:27:48%20PM.png" alt=""><figcaption></figcaption></figure>

2. Click `Create` a Managed Identity

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/tcRGMK1F7SoygNC2caja/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:28:21%20PM.png" alt=""><figcaption></figcaption></figure>

3. Select the `Subscription` and `Resource Group` containing the workload, and give the Managed Identity a `Name`. Click `Review + Create`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/YAddATtnuGH3RfuonmYJ/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:41:40%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 2: Attached the Azure Managed Identity to your workload (Example below is for Azure ML)

When creating or updating a resource that will serve as the Client running Deep Lake, assign the Managed Identity from Step 1 to this resource.&#x20;

For example, in Azure Machine Learning Studio, when creating a compute instance, toggle `Assign Identity` and select the `Managed Identity` from Step 1.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/W5EwFypdT1BcjG8kFhsg/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%204:48:02%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 3: Create a Deep Lake Workload Identity using the Azure Managed Identity

1. Navigate to the `Permissions` tab for your organization in the [Deep Lake App](https://app.activeloop.ai/), locate the  `Workload Identities`, and select `Add.`

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/VvULGOdpGrqzDVX9COzy/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:59:18%20PM.png" alt=""><figcaption></figcaption></figure>

2. Specify a `Display Name`, `Client ID` (for the Managed Identity), and `Tenant ID`. The `Client ID` can be found in the main page for the Managed Identity, and the `Tenant ID` can be found in `Tenant Properties` in Azure. Click `Add`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/hWQq7M2WlPjaaWeDW2vc/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:55:39%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 4: Run the workload

Specify the environmental variables below in the Deep Lake client and run other Deep APIs as normal.

{% hint style="danger" %}
Note: the `CLIENT_ID` below is for the compute instance, not the Managed Identity.
{% endhint %}

```python
#### THIS IS THE CLIENT_ID FOR THE COMPUTE, NOT THE MANAGED IDENTITY #####
os.environ["AZURE_CLIENT_ID"] = <azure_client_id>

os.environ["ACTIVELOOP_AUTH_PROVIDER"] = "azure" 
```

Specifying the `AZURE_CLIENT_ID` is not necessary in some environments because the correct value may automatically be set.

For a compute instance in the Azure Machine Learning Studio, the Client ID can be found in instance settings below:

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/uQj5sFkMEvHx6mbBk5GW/Screenshot%20by%20Snip%20My%20at%20Mar%2022,%202024%20at%209:37:45%20AM.png" alt=""><figcaption></figcaption></figure>
