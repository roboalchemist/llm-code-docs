# Deep Lake Documentation

Source: https://docs-v3.activeloop.ai/llms-full.txt

---

# Deep Lake Docs

We hope you enjoy Docs for Deep Lake.

## Activeloop Deep Lake

### Use Cases for Deep Lake

> #### Please note this is the documentation for Deep Lake version 3.9.16 and  earlier.  For Deep Lake 4.0.0 and above, please use [the following link](https://docs.deeplake.ai/). We will be working on transitioning the documentation very soon - stay tuned!

#### Deep Lake as a Data Lake For Deep Learning

* Store and organize unstructured data (images, audios, nifti, videos, text, metadata, and more) in a versioned data format optimized for Deep Learning performance.
* Rapidly query and visualize your data in order to create optimal training sets.
* Stream training data from your cloud to multiple GPUs, without any copying or bottlenecks.

#### Deep Lake as a Vector Store for RAG Applications

* Store and search embeddings and their metadata including text, jsons, images, audio, video, and more. Save the data locally, in your cloud, or on Deep Lake storage.
* Build Retrieval Augmented Generation (RAG) Apps using our integrations with [LangChain](https://docs-v3.activeloop.ai/examples/rag/langchain-integration) and [LlamaIndex](https://docs-v3.activeloop.ai/examples/rag/llamaindex-integration)
* Run computations locally or on our [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database)

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/fK48LFXvYcKprMMnN44r/Two_Way_Utility.png" alt=""><figcaption><p>Deep Lake Architecture for Inference and Model Development Applications.</p></figcaption></figure>

### To start using Deep Lake ASAP, check out our [Deep Learning Quickstart](https://docs-v3.activeloop.ai/examples/dl/quickstart), [RAG Quickstart](https://docs-v3.activeloop.ai/examples/rag/quickstart), and [Deep Learning Playbooks](https://docs-v3.activeloop.ai/examples/dl/playbooks).

Please check out Deep Lake's [GitHub repository](https://github.com/activeloopai/Hub) and give us a ⭐ if you like the project. &#x20;

Join our [Slack Community ](https://slack.activeloop.ai)if you need help or have suggestions for improving documentation!

### Deep Lake Docs Overview

{% content-ref url="setup/authentication" %}
[authentication](https://docs-v3.activeloop.ai/setup/authentication)
{% endcontent-ref %}

{% content-ref url="examples/dl/quickstart" %}
[quickstart](https://docs-v3.activeloop.ai/examples/dl/quickstart)
{% endcontent-ref %}

{% content-ref url="examples/rag/quickstart" %}
[quickstart](https://docs-v3.activeloop.ai/examples/rag/quickstart)
{% endcontent-ref %}

{% content-ref url="examples/dl/playbooks" %}
[playbooks](https://docs-v3.activeloop.ai/examples/dl/playbooks)
{% endcontent-ref %}

{% content-ref url="examples/dl/tutorials" %}
[tutorials](https://docs-v3.activeloop.ai/examples/dl/tutorials)
{% endcontent-ref %}

{% content-ref url="technical-details/best-practices" %}
[best-practices](https://docs-v3.activeloop.ai/technical-details/best-practices)
{% endcontent-ref %}

{% content-ref url="examples/dl/api" %}
[api](https://docs-v3.activeloop.ai/examples/dl/api)
{% endcontent-ref %}


# Installation

Installing the Deep Lake Python package

## How to Install Deep Lake

Deep Lake is a python package that can be installed using pip.&#x20;

```bash
!pip install deeplake
```

**By default, Deep Lake does not install dependencies for google-cloud, video support, and other features.** [**Details on all installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.**&#x20;


# User Authentication

Registration and authentication in Deep Lake.

## How to Register and Authenticate in Deep Lake

### Registration and Login

In order to use Deep Lake features that require authentication (Activeloop storage, connecting your cloud dataset to the Deep Lake UI, etc.) you should register and login in the [Deep Lake App](https://app.activeloop.ai/).

### Authentication in Programmatic Interfaces

You can create an API token in the [Deep Lake App](https://app.activeloop.ai/) (top-right corner, user settings) and authenticate in programatic interfaces using 2 options:

#### Environmental Variable

Set the environmental variable `ACTIVELOOP_TOKEN` to your API token. In Python, this can be done using:

`os.environ['ACTIVELOOP_TOKEN'] = <your_token>`

#### Pass the Token to Individual Methods

You can pass your API token to individual methods that require authentication such as:

`ds = deeplake.load('hub://org_name/dataset_name', token = <your_token>)`


# Workload Identities (Azure Only)

How to authenticate using workload identities instead of user credentials.

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


# Storage and Credentials

How to access datasets in other clouds and manage their credentials.

## Storing Datasets in Your Own Cloud

Deep Lake can be used as a pure OSS package without any registration or relationship with Activeloop. However, registering with Activeloop offers several benefits:

* Storage provided by Activeloop
* Access to the [Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) for performant vector search
* Access to [Deep Lake App](https://app.activeloop.ai/), which provides dataset visualization, querying, version control UI, dataset analytics, and other powerful features
* [Managed credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials) for Deep Lake datasets stored outside of Activeloop

{% hint style="info" %}
**When connecting data from your cloud using Managed Credentials, the data is never stored or cached in Deep Lake. All Deep Lake user interfaces (browser, python, etc.) fetch data directly from long-term storage.**
{% endhint %}

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/T87OnAF93ohnETEcgwbC/Authentication_With_Managed_Creds.png" alt=""><figcaption><p>Authentication Using Managed Credentials</p></figcaption></figure>

{% content-ref url="storage-and-creds/storage-options" %}
[storage-options](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options)
{% endcontent-ref %}

{% content-ref url="storage-and-creds/managed-credentials" %}
[managed-credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials)
{% endcontent-ref %}


# Storage Options

How to authenticate using Activeloop storage, AWS S3, and Google Cloud Storage.

**Deep Lake datasets can be stored locally, or on several cloud storage providers including Deep Lake Storage, AWS S3, Microsoft Azure, and Google Cloud Storage.** Datasets are accessed by choosing the correct prefix for the dataset `path` that is passed to methods such as `deeplake.load(path)`, and `deeplake.empty(path)`. The path prefixes are:

<table data-header-hidden><thead><tr><th width="222.76694359979138">Storage</th><th>Path</th><th>Notes</th></tr></thead><tbody><tr><td><strong>Storage Location</strong></td><td><strong>Path</strong></td><td><strong>Notes</strong></td></tr><tr><td><strong>Local</strong></td><td><code>/local_path</code></td><td></td></tr><tr><td><strong>Deep Lake Storage</strong></td><td><code>hub://org_id/dataset_name</code></td><td></td></tr><tr><td><strong>Deep Lake Managed DB</strong></td><td><code>hub://org_id/dataset_name</code></td><td>Specify <code>runtime = {"tensor_db": True}</code> when creating the dataset</td></tr><tr><td><strong>AWS S3</strong></td><td><code>s3://bucket_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr><tr><td><strong>Microsoft Azure (Gen2 DataLake Only)</strong></td><td><code>azure://account_name/container_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr><tr><td><strong>Google Cloud</strong></td><td><code>gcs://bucket_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr></tbody></table>

{% hint style="info" %}
Connecting Deep Lake datasets stored in your own cloud via Deep Lake [Managed Credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials) is required for accessing enterprise features, and it significantly simplifies dataset access.
{% endhint %}

## Authentication for each cloud storage provider:

### Activeloop Storage and Managed Datasets

In order to access datasets stored in Deep Lake, or datasets in other clouds that are [managed by Activeloop](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials), users must register and authenticate using the steps in the link below:

{% content-ref url="../authentication" %}
[authentication](https://docs-v3.activeloop.ai/setup/authentication)
{% endcontent-ref %}

### AWS S3

Authentication with AWS S3 has 4 options:

1. Use Deep Lake on a machine in the AWS ecosystem that has access to the relevant S3 bucket via [AWS IAM](https://aws.amazon.com/iam/), in which case there is no need to pass credentials in order to access datasets in that bucket.
2. Configure AWS through the cli using `aws configure`. This creates a credentials file on your machine that is automatically access by Deep Lake during authentication.
3. Save the `AWS_ACCESS_KEY_ID` ,`AWS_SECRET_ACCESS_KEY` , and `AWS_SESSION_TOKEN (optional)` in environmental variables of the same name, which are loaded as default credentials if no other credentials are specified.
4. Create a dictionary with the `AWS_ACCESS_KEY_ID` ,`AWS_SECRET_ACCESS_KEY` , and `AWS_SESSION_TOKEN (optional)`, and pass it to Deep Lake using:

   **Note:** the dictionary keys must be lowercase!

```python
# Vector Store API
vector_store = VectorStore('s3://<bucket_name>/<dataset_name>', 
                           creds = {
                               'aws_access_key_id': <your_access_key_id>,
                               'aws_secret_access_key': <your_aws_secret_access_key>,
                               'aws_session_token': <your_aws_session_token>, # Optional
                               }
                               )

# Low Level API
ds = deeplake.load('s3://<bucket_name>/<dataset_name>', 
                   creds = {
                       'aws_access_key_id': <your_access_key_id>,
                       'aws_secret_access_key': <your_aws_secret_access_key>,
                       'aws_session_token': <your_aws_session_token>, # Optional
                       }
                       )
```

`endpoint_url` can be used for connecting to other object storages supporting S3-like API such as [MinIO](https://github.com/minio/minio), [StorageGrid](https://www.netapp.com/data-storage/storagegrid/) and others.

### Custom Storage with S3 API

In order to connect to other object storages supporting S3-like API such as [MinIO](https://github.com/minio/minio), [StorageGrid](https://www.netapp.com/data-storage/storagegrid/) and others, simply add `endpoint_url` the the `creds` dictionary.

```python
# Vector Store API
vector_store = VectorStore('s3://...', 
                           creds = {
                               'aws_access_key_id': <your_access_key_id>,
                               'aws_secret_access_key': <your_aws_secret_access_key>,
                               'aws_session_token': <your_aws_session_token>, # Optional
                               'endpoint_url': 'http://localhost:8888'
                               }
                               )

# Low Level API
ds = deeplake.load('s3://...', 
                   creds = {
                       'aws_access_key_id': <your_access_key_id>,
                       'aws_secret_access_key': <your_aws_secret_access_key>,
                       'aws_session_token': <your_aws_session_token>, # Optional
                       'endpoint_url': 'http://localhost:8888'
                       }
                       )
```

### Microsoft Azure

Authentication with Microsoft Azure has 4 options:

1. Log in from your machine's CLI using `az login`.
2. Save the `AZURE_STORAGE_ACCOUNT`, `AZURE_STORAGE_KEY`  , or other credentials in environmental variables of the same name, which are loaded as default credentials if no other credentials are specified.
3. Create a dictionary with the `ACCOUNT_KEY` or  `SAS_TOKEN` and pass it to Deep Lake using:

   **Note:** the dictionary keys must be lowercase!

```python
# Vector Store API
vector_store = VectorStore('azure://<account_name>/<container_name>/<dataset_name>', 
                           creds = {
                               'account_key': <your_account_key>,
                               'sas_token': <your_sas_token>,
                               }
                               )

# Low Level API
ds = deeplake.load('azure://<account_name>/<container_name>/<dataset_name>', 
                   creds = {
                       'account_key': <your_account_key>, 
                       #OR
                       'sas_token': <your_sas_token>,
                       }
                       )
```

### Google Cloud Storage

Authentication with Google Cloud Storage has 2 options:

1. Create a service account, download the JSON file containing the keys, and then pass that file to the `creds` parameter in `deeplake.load('gcs://.....', creds = 'path_to_keys.json')` . It is also possible to manually pass the information from the JSON file into the `creds` parameter using:&#x20;

   ```python
   # Vector Store API
   vector_store = VectorStore('gcs://.....', 
                              creds = {<information from the JSON file>}
                              )

   # Low Level API
   ds = deeplake.load('gcs://.....', 
                      creds = {<information from the JSON file>}
                      )
   ```
2. Authenticate through the browser using the steps below. This requires that the project credentials are stored on your machine, which happens after `gcloud` is [initialized](https://cloud.google.com/sdk/gcloud/reference/init) and [logged in](https://cloud.google.com/sdk/gcloud/reference/auth) through the CLI. Afterwards, `creds` can be switched to `creds = 'cache'`.

   ```python
   # Vector Store API
   vector_store = VectorStore('gcs://.....', 
                              creds = 'browser' # Switch to 'cache' after doing this once
                              )

   # Low Level API
   ds = deeplake.load('gcs://.....', 
                      creds = 'browser' # Switch to 'cache' after doing this once
                      )
   ```


# Setting up Deep Lake in Your Cloud

How to store Deep Lake data in your own cloud and manage credentials with Deep Lake

## Connecting Data From Your Cloud Using Deep Lake Managed Credentials

Connecting data from your own cloud and managing credentials in Deep Lake unlocks several important capabilities:

* Access to performant features such as the [Deep Lake Compute Engine](https://docs-v3.activeloop.ai/setup/storage-and-creds/broken-reference)
* Access to the [Deep Lake App](https://app.activeloop.ai/) for datasets stored in your own cloud
* Simpler access to Deep Lake datasets stored in your own cloud using the Python API
  * No need for continuously specifying cloud access keys in Python

### Managed Credentials

In order for the Deep Lake to access datasets or linked tensors stored in the user's cloud, Deep Lake must authenticate the respective cloud resources. Access can be provided using access keys or using role-based access ([provisioning steps here](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/provisioning-rbac)). The video below summarizes the UI for managing your cloud credentials.&#x20;

{% embed url="<https://www.loom.com/share/74be299eec16445c84a2f3b38301a40a>" %}

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/T87OnAF93ohnETEcgwbC/Authentication_With_Managed_Creds.png" alt=""><figcaption><p>Authentication Using Managed Credentials</p></figcaption></figure>

### Default Storage

Default storage enables you to map the Deep Lake path `hub://org_id/dataset_name`to a cloud path of your choice. Subsequently, all datasets created using the Deep Lake path will be stored at the user-specified specified, and they can be accessed using API tokens and managed credentials from Deep Lake. By default, the default storage is set as Activeloop Storage, and you may change it using the UI below.

{% embed url="<https://www.loom.com/share/962f130397b344cbbfe9168519f22691>" %}

{% hint style="warning" %}
Note: that in order to visualize data in the Deep Lake browser application, it is necessary to [enable CORS](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/enabling-cors) in the bucket containing any source data.
{% endhint %}

### Connecting Deep Lake Dataset in your Cloud to the Deep Lake to App

If you do not set the Default Storage as your own cloud, Datasets in user's clouds can be connected to the [Deep Lake App](https://app.activeloop.ai/) using the Python API below. Once a dataset is connected to Deep Lake, it is assigned a Deep Lake path `hub://org_id/dataset_name`, and it can be accessed using API tokens and managed credentials from Deep Lake, without continuously having to specify cloud credentials.

#### **Connecting Datasets in the Python API**

<pre class="language-python"><code class="lang-python"># Step 1: Create/load the dataset directly in the cloud using your org_id and
# Managed Credentials (creds_key) for accessing the data (See Managed Credentials above)
ds = deeplake.empty/load('s3://my_bucket/dataset_name', 
                    creds={'creds_key': 'managed_creds_key'}, org_id='my_org_id')

# Step 2a: Connect the dataset to Deep Lake, inheriting the dataset_name above
ds.connect()
## ->>> This produces a Deep Lake path for accessing the dataset such as:
## ---- 'hub://my_org_id/dataset_name'

<strong>## OR
</strong>
# Step 2b: Specify your own path and dataset name for future access to the dataset.
# You can also specify different managed credentials, if desired
ds.connect(dest_path = 'hub://org_id/dataset_name', creds_key = 'my_creds_key')
</code></pre>

### Using Manage Credentials with Linked Tensors

Managed credentials can be used for accessing data stored in [linked tensors](https://docs.deeplake.ai/en/latest/Htypes.html#link-htype). Simply add the managed credentials to the dataset's `creds_keys` and assign them to each sample.

```python
ds.create_tensors('images', htype = 'link[image]', sample_compression = 'jpeg')

ds.add_creds_key('my_creds_key', managed=True)

ds.images.append(deeplake.link(link_to_sample, creds_key = 'my_creds_key')
```


# Microsoft Azure

Azure-specific information for connecting data to Deep Lake

## Azure-Specific Information for Connecting Data to Deep Lake

{% content-ref url="microsoft-azure/provisioning-federated-credentials" %}
[provisioning-federated-credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/provisioning-federated-credentials)
{% endcontent-ref %}

{% content-ref url="microsoft-azure/enabling-cors" %}
[enabling-cors](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/enabling-cors)
{% endcontent-ref %}

{% content-ref url="microsoft-azure/configure-azure-sso-on-activeloop" %}
[configure-azure-sso-on-activeloop](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/configure-azure-sso-on-activeloop)
{% endcontent-ref %}


# Configure Azure SSO on Activeloop

Enabling Azure SSO on Activeloop

### Configure Azure SSO on Activeloop

### 1. Creating Application

* **Go to App registration page in** [**🌐Azure portal**](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
* **Click on add New Registration**

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F27dGrs7Z5kgIGhNU9Csb%2Fimage.png?alt=media&#x26;token=361ef49f-1ce7-453f-afff-0b1276df675f" alt=""><figcaption></figcaption></figure>

1. Put name for the application
2. For application type, select `Default Directory only - Single tenant`
3. For Redirect URI select the type `Web`
4. For Callback URL put `https://auth.activeloop.ai/login/callback`
5. Click on `Register`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FV8fIW2kawFgNIJ3dhS1j%2Fimage.png?alt=media&#x26;token=7113ceb0-7c1e-46f6-91b5-c0a1ac1d22dd" alt=""><figcaption></figcaption></figure>

#### Once it is created go to `Overview` page, copy and send us the `Application (client) ID` and the `Directory (tenant) ID`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FTZwGsAeMYMwCrejOvInL%2Fimage.png?alt=media&#x26;token=5232c389-5cd7-4e36-80a6-d38599680cbd" alt=""><figcaption></figcaption></figure>

#### Client secret creation

Go to `Certificates & Secrets` → `Client secrets` →`New client secret`

Name the secret, select preferred expiration and click `Add`

`NOTE: The secret need to be updated before it get expired`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FunO6OgJTvEPHloYJ14IW%2Fimage.png?alt=media&#x26;token=35997572-f307-4a30-8872-20d0a69890fd" alt=""><figcaption></figcaption></figure>

#### Send us the secret value

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FVOMuK1UzLwR3eXPw55UZ%2Fimage.png?alt=media&#x26;token=03be1998-30df-4ee4-8e1d-6955c336b306" alt=""><figcaption></figcaption></figure>

### 2. Granting Permissions

1. **Go to `API permissions` → `Microsoft Graph` → `Delegated Permissions` and select following permissions:**
   1. `email`
   2. `openid`
   3. `profile`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FtMvO1PUkmTGIs6K695yj%2Fimage.png?alt=media&#x26;token=9fa58e95-ddbd-43d3-9392-9d59e4ab694c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FsSuqMxw7JzmPXcuYxdh1%2Fimage.png?alt=media&#x26;token=5954a0d1-b47c-43b0-8edb-1f52ee6baeca" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FgyyycW0hQazFzf0tUUd3%2Fimage.png?alt=media&#x26;token=c81eefc8-2120-4445-823f-ac3072239380" alt=""><figcaption></figcaption></figure>

2. **In the search bar search `Directory.Read.All` and select the permission as well**

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F5lGg04O7OJ2W26XCHq3e%2Fimage.png?alt=media&#x26;token=0c136c69-7873-415d-bf8d-cb170a0505fc" alt=""><figcaption></figcaption></figure>

#### Click on `Add permissions`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2Fr6Xa66c0laZyJjItAoCP%2Fimage.png?alt=media&#x26;token=68839a7f-7444-4a70-b9b1-f04e8b9afc03" alt=""><figcaption></figcaption></figure>

### 3. Domain Name Validation in our side

We also will be needing domain of the azure tenant to authorize the SSO clients

1. Go to [🌐Domain Names](https://portal.azure.com/#view/Microsoft_AAD_IAM/DomainsList.ReactView) in Azure portal
2. Copy the domain name that will be used for SSO and send us

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FKedHnaMe4FkUUcWtNITt%2Fimage.png?alt=media&#x26;token=35e066e8-73d9-4fb3-a8d1-42995902bdf9" alt=""><figcaption></figcaption></figure>


# Provisioning Federated Credentials

How to setup Federated Credentials in Azure

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


# Enabling CORS

How to enable Cross-Origin Resource Sharing in your Azure account.

## Enabling CORS in Azure for Data Visualization

Cross-Origin Resource Sharing (CORS) is typically enabled by default in Azure. If that's not the case in your Azure account, in order to visualize Deep Lake datasets stored in your own Azure storage in the [Deep Lake app](https://app.activeloop.ai/), please enable [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in the storage account containing the Deep Lake dataset and any source data in linked tensors.

### Steps for enabling CORS in Azure

1\. Login to the Azure.

2\. Navigate to the `Storage account` with the relevant data.

3\. Open the `Resource sharing (CORS)` section on the left nav.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/co8SnhoZKJUyj3ixhViA/Screen%20Shot%202023-06-21%20at%209.41.27%20AM.png" alt=""><figcaption></figcaption></figure>

4\. Add the following items to the permissions.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/rbn4ndDqlJRRwoiqXAXx/Screen%20Shot%202023-06-21%20at%209.45.00%20AM%20edited.png" alt=""><figcaption></figcaption></figure>

| Allowed origins             | Allowed methods | Allowed headers |
| --------------------------- | --------------- | --------------- |
| <https://app.activeloop.ai> | GET, HEAD       | \*              |


# Google Cloud

Azure-specific information for connecting data to Deep Lake

## Azure-Specific Information for Connecting Data to Deep Lake

{% content-ref url="microsoft-azure/provisioning-federated-credentials" %}
[provisioning-federated-credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/provisioning-federated-credentials)
{% endcontent-ref %}

{% content-ref url="microsoft-azure/enabling-cors" %}
[enabling-cors](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/enabling-cors)
{% endcontent-ref %}


# Provisioning Federated Credentials

How to setup Federated Credentials in Google Cloud

## Setting up Federated Credentials in Google Cloud

The most secure method for connecting data from your Google Cloud Storage to Deep Lake is using Federated Credentials, which are set up using the steps below:

### Step 1: Create Google Cloud Service Account

**1. If you already have a service account, skip to Step 2**

2\. Navigate to `IAM & Admin` -> `Service Accounts` -> `CREATE SERVICE ACCOUNT`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F3avKxYVxQZQhEuluNzoO%2Fgcs_service_accounts.png?alt=media&#x26;token=b8e4506e-6811-4859-9ea0-851597e0bf33" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FJ06wuzpCbMuWeZf3jPqr%2Fgcs_service_account_create.png?alt=media&#x26;token=811d94e7-a7fa-4f43-8a53-7e951e14b747" alt=""><figcaption></figcaption></figure>

3\. Enter the service account `id`, and optional `name` and `description`. Make sure to copy the email address and and click on `CREATE AND CONTINUE`.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FdoqJMvBiQuNbrybatuqd%2Fgcs_service_account_details.png?alt=media&#x26;token=1f48ec8c-61e2-49fc-804c-ccc2e38f279d" alt=""><figcaption></figcaption></figure>

4\. Click `CONTINUE` without entering any information.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FPCoxZOxJcUBVD216qhB0%2Fgcs_service_account_grant.png?alt=media&#x26;token=521609c5-2712-48b0-bf69-14f44848721e" alt=""><figcaption></figcaption></figure>

5\. Enter `activeloop-platform@activeloop-saas-iam.iam.gserviceaccount.com` in the `Service account users role` and click `DONE`.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FMuVv2v6anH6N8gWL342p%2Fgcs_service_account_done.png?alt=media&#x26;token=674aff34-78f6-49cd-bf4a-384ab91444a3" alt=""><figcaption></figcaption></figure>

### Step 2: Grant Access to the bucket using a Service Account Principal

1\. Navigate to `Cloud Storage` and `Buckets`.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FQ6Yn7ciKWMqei41wA8ZO%2Fgcs_select_bucket.png?alt=media&#x26;token=efc0a579-0fca-4cce-9372-9a99ca05332a" alt=""><figcaption></figcaption></figure>

2.Select `Edit Access` for the bucket you want to connect to Activeloop.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FTav4RdZkMXEvXDyaI100%2Fgcs_edit_access.png?alt=media&#x26;token=3fd6306c-7a5f-4853-a6b6-272a343951e1" alt=""><figcaption></figcaption></figure>

3.Select `Add Principal`.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F2LxsUu3EwhmwFoTJz9sC%2Fgcs_add_principal.png?alt=media&#x26;token=4f1bdfe8-0a41-4190-a655-8648bc9b886f" alt=""><figcaption></figcaption></figure>

4.Enter the `Service Account Email`, select the role as `Storage Object Admin`, and click Save. If the bucket is encrypted with customer managed KMS key, then `Cloud KMS CryptoKey Encrypter/Decrypter` should be added in the `Role` field as well.

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FiMDFp5BDlpE9dlIZcFWh%2Fgcs_set_principal.png?alt=media&#x26;token=d07ba5b7-985e-4ef0-9475-d8aed5f1ec86" alt=""><figcaption></figcaption></figure>

### Step 3: Enter the Service Account Email (Step 2) into the Activeloop App

See the first video in the link below:

{% content-ref url=".." %}
[..](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials)
{% endcontent-ref %}


# Enabling CORS

How to enable Cross-Origin Resource Sharing in your GCS account.

## Enabling CORS in GCS for Data Visualization

In order to visualize Deep Lake datasets stored in your own GSC buckets in the [Deep Lake app](https://app.activeloop.ai/), please enable [Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in the buckets containing the Deep Lake dataset and any source data in linked tensors, by inserting the snippet below in the CORS section of the Permissions tab for the bucket:

```
[
    {
      "origin": ["https://app.activeloop.ai"],
      "method": ["GET", "HEAD"],
      "responseHeader": ["*"],
      "maxAgeSeconds": 3600
    }
]
```


# Amazon Web Services

AWS-specific information for connecting data to Deep Lake

## AWS-Specific Information for Connecting Data to Deep Lake

{% content-ref url="amazon-web-services/provisioning-rbac" %}
[provisioning-rbac](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/provisioning-rbac)
{% endcontent-ref %}

{% content-ref url="amazon-web-services/enabling-cors" %}
[enabling-cors](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/enabling-cors)
{% endcontent-ref %}


# Provisioning Role-Based Access

How to provision Role-Based Access in S3

## Setting up Role-Based Access for AWS S3

The most secure method for connecting data from your AWS account to Deep Lake is using Federated Credentials and Role-Based Access, which are set up using the steps below:

### Step 1: Create the AWS IAM Policy

1\. Login to the AWS account where the IAM Role will be created and where the data is stored.

2\. Go to the IAM page in the AWS UI, which can be done by searching "IAM" in the console and locating the IAM page under Services.

3\. In the left nav, open the `Policies` under `Access management` and on `Create policy` on the right.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/dwiz2jXmV62HOHGZJB0B/IAM_Provisioning_Screenshots.001.jpeg" alt=""><figcaption></figcaption></figure>

5\. Select the `JSON` tab instead of `Visual editor`.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/oYBmpIh2Kexcb2qfshkz/IAM_Provisioning_Screenshots.002.jpeg" alt=""><figcaption></figcaption></figure>

6\. Replace the code in the editor with the code below. Replace `BUCKET_NAME` with the bucket names for which you want to grant role-based access:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [ 
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET_NAME",
                "arn:aws:s3:::BUCKET_NAME/*"
            ]
        }
    ]
}

```

7\. On the bottom right, click `Next: Tags` (create tags if needed) and `Next: Preview`, enter the policy `name` and `description`, and click `Create policy`

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/dwHYD9qpNKHwaRdGJGpo/IAM_Provisioning_Screenshots.003.jpeg" alt=""><figcaption></figcaption></figure>

### Step 2: Create the AWS IAM Role&#x20;

1\. On the `IAM` page, in the left nav, open the `Roles` under `Access management`, and click `Create role` on the right.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/WISo2YVIY2pSaDAauvQE/IAM_Provisioning_Screenshots.004.jpeg" alt=""><figcaption></figcaption></figure>

3\. Select `Custom trust policy` from the list of options.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/Y3XJNjtPLphHnCmVKy4v/IAM_Provisioning_Screenshots.005.jpeg" alt=""><figcaption></figcaption></figure>

4\. Replace the policy definition with the code below and click `Next`

```
{
    "Version": "2012-10-17",
    "Statement": 
    [
        {
            "Sid": "AllowAssumeRoleFromActiveloopSaaS",
            "Effect": "Allow",
            "Principal": {
                 "AWS": "arn:aws:iam::597713067985:role/activeloop_backend"
        },
        "Action": "sts:AssumeRole"
      }
   ]
}
```

5\. From the provided policy list, select the previously created policy from Step 1 and click `Next`

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/SohHb8WHLxZnXbzfEDZN/IAM_Provisioning_Screenshots.010.jpeg" alt=""><figcaption></figcaption></figure>

6\. Set the `name` and `description` for the role and click `Create role` at the bottom.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/xWhTyfMdnsXCb6unSITx/IAM_Provisioning_Screenshots.007.jpeg" alt=""><figcaption></figcaption></figure>

### Step 3: Grant Access to AWS KMS Key (**only for buckets that are encrypted with customer managed KMS keys**)

1\. Navigate to the bucket in the AWS S3 UI

2\. Open the bucket Properties

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/NhNpo1yW31duQhaKMeAw/IAM_Provisioning_Screenshots.008.jpeg" alt=""><figcaption></figcaption></figure>

3\. Scroll down to Default encryption and copy the `AWS KMS key ARN`&#x20;

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/hRARnAoIJtdyqT2FGjFv/IAM_Provisioning_Screenshots.009.jpeg" alt=""><figcaption></figcaption></figure>

4\. In the Policy creation step (Step 1, Sub-step 6), use the JSON below in the policy statement, and replace `YOUR_KMS_KEY_ARN` with the copied Key ARN for the encrypted bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
		 "s3:GetBucketLocation",
                "s3:*Object*"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET_NAME",
                "arn:aws:s3:::BUCKET_NAME/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": [
                "YOUR_KMS_KEY_ARN”
            ]
        }
    ]
}

```

### Step 4: Enter the created AWS Role ARN (Step 2) into the Activeloop App

See the first video in the link below:

{% content-ref url=".." %}
[..](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials)
{% endcontent-ref %}


# Enabling CORS

How to enable Cross-Origin Resource Sharing in your AWS S3 buckets.

## Enabling CORS in AWS for Data Visualization

In order to visualize Deep Lake datasets stored in your own S3 buckets in the [Deep Lake app](https://app.activeloop.ai/), please enable [Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in the buckets containing the Deep Lake dataset and any source data in linked tensors, by inserting the snippet below in the CORS section of the Permissions tab for the bucket:

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD"
        ],
        "AllowedOrigins": [
            "*.activeloop.ai"
        ],
        "ExposeHeaders": []
    }
] 
```

### Visualizing Your Datasets Locally

In order to visualize Deep Lake datasets stored in your own cloud using `ds.visualize()` or using our [embedded visualizer](https://docs-v3.activeloop.ai/technical-details/visualization/visualizer-integration), the `AllowedOrigins` values in CORS should be set to `*`.&#x20;


# Deep Learning

Using Deep Lake for managing data in Deep Learning applications.

## Deep Lake as a Data Lake For Deep Learning

Deep Lake can be used as a data management tool for Deep Learning applications, enabling teams to create and ship models faster. Deep Lake's primary capabilities are:&#x20;

* Store and organize unstructured data (images, audios, nifti, videos, text, metadata, and more) in a versioned data format optimized for Deep Learning performance.
* Rapidly query and visualize your data in order to create optimal training sets.
* Stream training data from your cloud to multiple GPUs, without any copying or bottlenecks.


# Deep Learning Quickstart

A jump-start guide to using Deep Lake for Deep Learning.

## How to Get Started with Deep Learning in Deep Lake in Under 5 Minutes

### Installing Deep Lake

Deep Lake can be installed using pip. **By default, Deep Lake does not install dependencies for video, google-cloud, compute engine, and other features.** [**Details on all installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.**&#x20;

```bash
!pip install deeplake
```

### Fetching Your First Deep Lake Dataset

Let's load the [Visdrone dataset](https://app.activeloop.ai/activeloop/visdrone-det-train), a rich dataset with many object detections per image. [Datasets](https://datasets.activeloop.ai/docs/ml/datasets/) hosted by Activeloop are identified by the host organization id followed by the dataset name: `activeloop/visdrone-det-train`.

```python
import deeplake

dataset_path = 'hub://activeloop/visdrone-det-train'
ds = deeplake.load(dataset_path) # Returns a Deep Lake Dataset but does not download data locally
```

### Reading Samples From a Deep Lake Dataset

Data is not immediately read into memory because Deep Lake operates [lazily](https://en.wikipedia.org/wiki/Lazy_evaluation). You can fetch data by calling the `.numpy()` or `.data()` methods:

```python
# Indexing
image = ds.images[0].numpy() # Fetch the first image and return a numpy array
labels = ds.labels[0].data() # Fetch the labels in the first image

# Slicing
img_list = ds.labels[0:100].numpy(aslist=True) # Fetch 100 labels and store 
                                               # them as a list of numpy arrays
```

Other metadata such as the mapping between numerical labels and their text counterparts can be accessed using:

```python
labels_list = ds.labels.info['class_names']
```

### Visualizing a Deep Lake Dataset

Deep Lake enables users to visualize and interpret large datasets. The tensor layout for a dataset can be inspected using:

```python
ds.summary()
```

The dataset can be [visualized in the Deep Lake UI](https://app.activeloop.ai/activeloop/mnist-train), or using an iframe in a Jupyter notebook:

```python
ds.visualize()
```

{% hint style="info" %}
Visualizing datasets in [the Deep Lake UI](https://app.activeloop.ai/) will unlock more features and faster performance compared to visualization in Jupyter notebooks.
{% endhint %}

### Creating Your Own Deep Lake Datasets

You can access all of the features above and more with your own datasets! If your source data conforms to one of the formats below, you can ingest them directly with 1 line of code. The ingestion functions support source data from the cloud, as well as creation of Deep Lake datasets in the cloud.

* [YOLO](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_yolo)
* [COCO](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_coco)
* [Classifications](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_classification)

For example, a COCO format dataset can be ingested using:

```python
dataset_path = 's3://bucket_name_deeplake/dataset_name' # Destination for the Deep Lake dataset

images_folder = 's3://bucket_name_source/images_folder'
annotations_files = ['s3://bucket_name_source/annotations.json'] # Can be a list of COCO jsons.

ds = deeplake.ingest_coco(images_folder, annotations_files, dataset_path, src_creds = {...}, dest_creds = {...})
```

For creating datasets that do not conform to one of the formats above, [you can use our methods for manually creating datasets, tensors, and populating them with data.](https://docs-v3.activeloop.ai/examples/dl/guide/creating-datasets)&#x20;

### Authentication

To use Deep Lake features that require authentication (Activeloop storage, Tensor Database storage, connecting your cloud dataset to the Deep Lake UI, etc.) you should [register in the Deep Lake App](https://app.activeloop.ai/register/) and authenticate on the client using the methods in the link below:

#### Environmental Variable

Set the environmental variable `ACTIVELOOP_TOKEN` to your API token. In Python, this can be done using:

`os.environ['ACTIVELOOP_TOKEN'] = <your_token>`

#### Pass the Token to Individual Methods

You can pass your API token to individual methods that require authentication such as:

`ds = deeplake.load('hub://org_name/dataset_name', token = <your_token>)`

### Next Steps

Check out our [Getting Started Guide](https://docs-v3.activeloop.ai/examples/dl/guide) for a comprehensive walk-through of Deep Lake. Also check out tutorials on [Running Queries](https://docs-v3.activeloop.ai/examples/tql), [Training Models](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models), and [Creating Datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets), as well as [Playbooks](https://docs-v3.activeloop.ai/examples/dl/playbooks) about powerful use-cases that are enabled by Deep Lake.

Congratulations, you've got Deep Lake working on your local machine:nerd:&#x20;


# Deep Learning Guide

The comprehensive guide for Deep Lake in Deep Learning applications.

## This Deep Learning Getting Started guide is available as a [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/GH97x6fuAOPOaseTEKaD/image.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="guide/hello-world" %}
[hello-world](https://docs-v3.activeloop.ai/examples/dl/guide/hello-world)
{% endcontent-ref %}

{% content-ref url="guide/creating-datasets" %}
[creating-datasets](https://docs-v3.activeloop.ai/examples/dl/guide/creating-datasets)
{% endcontent-ref %}

{% content-ref url="guide/understanding-compression" %}
[understanding-compression](https://docs-v3.activeloop.ai/examples/dl/guide/understanding-compression)
{% endcontent-ref %}

{% content-ref url="guide/accessing-datasets" %}
[accessing-datasets](https://docs-v3.activeloop.ai/examples/dl/guide/accessing-datasets)
{% endcontent-ref %}

{% content-ref url="guide/visualizing-datasets" %}
[visualizing-datasets](https://docs-v3.activeloop.ai/examples/dl/guide/visualizing-datasets)
{% endcontent-ref %}

{% content-ref url="guide/using-activeloop-storage" %}
[using-activeloop-storage](https://docs-v3.activeloop.ai/examples/dl/guide/using-activeloop-storage)
{% endcontent-ref %}

{% content-ref url="guide/connecting-to-ml-frameworks" %}
[connecting-to-ml-frameworks](https://docs-v3.activeloop.ai/examples/dl/guide/connecting-to-ml-frameworks)
{% endcontent-ref %}

{% content-ref url="guide/parallel-computing" %}
[parallel-computing](https://docs-v3.activeloop.ai/examples/dl/guide/parallel-computing)
{% endcontent-ref %}

{% content-ref url="guide/dataset-version-control" %}
[dataset-version-control](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-version-control)
{% endcontent-ref %}

{% content-ref url="guide/dataset-filtering" %}
[dataset-filtering](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-filtering)
{% endcontent-ref %}


# Step 1: Hello World

Installing Deep Lake and accessing your first Deep Lake Dataset.

## How to Install Deep Lake and Get Started

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

### Installing Deep Lake

Deep Lake can be installed through pip. **By default, Deep Lake does not install dependencies for audio, video, google-cloud, and other features.** [**Details on all installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.**&#x20;

```bash
! pip install deeplake
```

### Fetching Your First Deep Lake Dataset

Let's load [MNIST](https://docs-v3.activeloop.ai/examples/dl/guide/broken-reference), the hello world dataset of machine learning.&#x20;

First, instantiate a `Dataset` by pointing to its storage location. Datasets hosted on Activeloop Platform are typically identified by the namespace of the organization followed by the dataset name: `activeloop/mnist-train`.

```python
import deeplake

dataset_path = 'hub://activeloop/mnist-train'
ds = deeplake.load(dataset_path) # Returns a Deep Lake Dataset but does not download data locally
```

### Reading Samples From a Deep Lake Dataset

Data is not immediately read into memory because Deep Lake operates [lazily](https://en.wikipedia.org/wiki/Lazy_evaluation). You can fetch data by calling the `.numpy()` method, which reads data into a NumPy array.

```python
# Indexing
img = ds.images[0].numpy()              # Fetch the 1st image and return a NumPy array
label = ds.labels[0].numpy(aslist=True) # Fetch the 1st label and store it as a 
                                        # as a list
                              
text_labels = ds.labels[0].data()['text'] # Fetch the first labels and return them as text

# Slicing
imgs = ds.images[0:100].numpy() # Fetch 100 images and return a NumPy array
                                # The method above produces an exception if 
                                # the images are not all the same size

labels = ds.labels[0:100].numpy(aslist=True) # Fetch 100 labels and store 
                                             # them as a list of NumPy arrays
```

Congratulations, you've got Deep Lake working on your local machine:nerd:


# Step 2: Creating Deep Lake Datasets

Creating and storing Deep Lake Datasets.

## How to Create Datasets in Deep Lake Format

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

**This guide creates Deep Lake datasets locally. You may create datasets in the Activeloop cloud by** [**registering**](https://app.activeloop.ai/register)**, creating an API token, and replacing the local paths below with the path to your Deep Lake organization `hub://org_id/dataset_name`**

You don't have to worry about uploading datasets after you've created them. They are automatically synchronized with [wherever they are being stored](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options).

### Manual Creation

Let's follow along with the example below to create our first dataset manually. First, download and unzip the small classification dataset below called *animals.*&#x20;

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/CQftGlzveKhX5GzN5TSJ/animals.zip>" %}
animals dataset
{% endfile %}

The dataset has the following folder structure:

```
_animals
|_cats
    |_image_1.jpg
    |_image_2.jpg
|_dogs
    |_image_3.jpg
    |_image_4.jpg
```

Now that you have the data, you can **create a Deep Lake Dataset** and initialize its tensors. Running the following code will create Deep Lake dataset inside of the `./animals_deeplake`folder.

```python
import deeplake
from PIL import Image
import numpy as np
import os

ds = deeplake.empty('./animals_deeplake') # Create the dataset locally
```

Next, let's inspect the folder structure for the source dataset `'./animals'` to find the class names and the files that need to be uploaded to the Deep Lake dataset.

```python
# Find the class_names and list of files that need to be uploaded
dataset_folder = './animals'

# Find the subfolders, but filter additional files like DS_Store that are added on Mac machines.
class_names = [item for item in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, item))]

files_list = []
for dirpath, dirnames, filenames in os.walk(dataset_folder):
    for filename in filenames:
        files_list.append(os.path.join(dirpath, filename))
```

Next, let's **create the dataset tensors** and upload metadata. Check out our page on [Storage Synchronization](https://docs-v3.activeloop.ai/technical-details/best-practices/storage-synchronization) for details about the `with` syntax below.

```python
with ds:
    # Create the tensors with names of your choice.
    ds.create_tensor('images', htype = 'image', sample_compression = 'jpeg')
    ds.create_tensor('labels', htype = 'class_label', class_names = class_names)
    
    # Add arbitrary metadata - Optional
    ds.info.update(description = 'My first Deep Lake dataset')
    ds.images.info.update(camera_type = 'SLR')
```

{% hint style="warning" %}
Specifying [`htype`](https://docs.deeplake.ai/en/latest/Htypes.html) and `dtype` is not required, but it is highly recommended in order to optimize performance, especially for large datasets. Use`dtype`to specify the numeric type of tensor data, and use`htype`to specify the underlying data structure.
{% endhint %}

Finally, let's **populate the data** in the tensors. The data is automatically uploaded to the dataset, regardless of whether it's local or in the cloud.        &#x20;

```python
with ds:
    # Iterate through the files and append to Deep Lake dataset
    for file in files_list:
        label_text = os.path.basename(os.path.dirname(file))
        label_num = class_names.index(label_text)
        
        #Append data to the tensors
        ds.append({'images': deeplake.read(file), 'labels': np.uint32(label_num)})
```

{% hint style="warning" %}
Appending the object `deeplake.read(path)`is equivalent to appending `PIL.Image.fromarray(path)`. However, the `deeplake.read()` method is significantly faster because it does not decompress and recompress the image if the compression matches the`sample_compression` for that tensor. Further details are available in [Understanding Compression](https://docs-v3.activeloop.ai/examples/dl/guide/understanding-compression).
{% endhint %}

{% hint style="warning" %}
In order to maintain proper indexing across tensors, `ds.append({...})` requires that you to append to all tensors in the dataset. If you wish to skip tensors during appending, please use `ds.append({...}, skip_ok = True)` or append to a single tensor using `ds.tensor_name.append(...)`.
{% endhint %}

Check out the first image from this dataset. More details about Accessing Data are available in [Step 4](https://docs-v3.activeloop.ai/examples/dl/guide/accessing-datasets).

```python
Image.fromarray(ds.images[0].numpy())
```

#### Dataset inspection

You can print a summary of the dataset structure using:

```
ds.summary()
```

Congrats! You just created your first dataset! 🎉

### Automatic Creation

If your source data conforms to one of the formats below, you can ingest them directly with 1 line of code.

* [YOLO](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_yolo)
* [COCO](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_coco)
* Classifications
* [Dataframe](https://docs.deeplake.ai/en/latest/deeplake.html#deeplake.ingest_dataframe)

For example, the above animals dataset can be converted to Deep Lake format using:

```python
src = './animals'
dest = './animals_deeplake_auto'

ds = deeplake.ingest_classification(src, dest)
```

### Creating Tensor Hierarchies

Often it's important to create tensors hierarchically, because information between tensors may be inherently coupled—such as bounding boxes and their corresponding labels. Hierarchy can be created using tensor `groups`:

```python
ds = deeplake.empty('./groups_test') # Creates the dataset

# Create tensor hierarchies
ds.create_group('my_group')
ds.my_group.create_tensor('my_tensor')

# Alternatively, a group can us created using create_tensor with '/'
ds.create_tensor('my_group_2/my_tensor') #Automatically creates the group 'my_group_2'
```

Tensors in groups are accessed via:

```python
ds.my_group.my_tensor

#OR

ds['my_group/my_tensor']
```

For more detailed information regarding accessing datasets and their tensors, check out [Step 4](https://docs-v3.activeloop.ai/examples/dl/guide/accessing-datasets).


# Step 3: Understanding Compression

Using compression to achieve optimal performance in Deep Lake.

## How to Use Compression in Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

#### Data in Deep Lake can be stored in raw uncompressed format. However, compression is highly recommended for achieving optimal performance in terms of speed and storage.

Compression is specified separately for each tensor, and it can occur at the `sample` or `chunk` level. For example, when creating a tensor for storing images, you can choose the compression technique for the image samples using the `sample_compression` input:

```python
ds.create_tensor('images', htype = 'image', sample_compression = 'jpeg')
```

In this example, every image added in subsequent `.append(...)` calls is compressed using the specified `sample_compression` method.&#x20;

The full list of available compressions is shown in the [API Reference](https://api-docs.activeloop.ai/index.html#hub.read).

### Choosing the Right Compression

There is no single answer for choosing the right compression, and the tradeoffs are described in detail in the next section. However, good rules of thumb are:

1. For data that has application-specific compressors (`image`, `audio`, `video`,...), choose the `sample_compression` technique that is native to the application such as `jpg`, `mp3`, `mp4`,...
2. For other data containing large samples (i.e. large arrays with >100 values), `lz4` is a generic compressor that works well in most applications.
   1. `lz4` can be used as a `sample_compression` or `chunk_compression` *.* In most cases, `sample_compression` is sufficient, but in theory, `chunk_compression` produces slightly smaller data.
3. For other data containing small samples (i.e. labels with <100 values), it is not necessary to use compression.

### Compression Tradeoffs

**Lossiness -** Certain compression techniques are [lossy](https://en.wikipedia.org/wiki/Lossy_compression), meaning that there is irreversible information loss when compressing the data. Lossless compression is less important for data such as images and videos, but it is critical for label data such as numerical labels, binary masks, and segmentation data.

**Memory -** Different compression techniques have substantially different memory footprints. For instance, `png` vs `jpeg` compression may result in a 10X difference in the size of a Hub dataset.&#x20;

**Runtime -** The primary variables affecting download and upload speeds for generating usable data are the network speed and available compute power for processing the data. In most cases, the network speed is the limiting factor. Therefore, the highest end-to-end throughput for non-local applications is achieved by maximizing compression and utilizing compute power to decompress/convert the data to formats that are consumed by deep learning models (i.e. arrays).&#x20;

**Upload Considerations** **-** When applicable, the highest uploads speeds can be achieved when the  `sample_compression` input matches the compression of the source data, such as:

```python
# sample_compression and my_image are 'jpeg'
ds.create_tensor('images', htype = 'image', sample_compression = 'jpeg')
ds.images.append(deeplake.read('my_image.jpeg'))
```

In this case, the input data is a `.jpg`, and the Deep Lake `sample_compression` is `jpg`.&#x20;

However, a mismatch between the compression of the source data and `sample_compression` in Deep Lake results in significantly slower upload speeds, because Deep Lake must decompress the source data and recompress it using the specified `sample_compression` before saving.

{% hint style="warning" %}
Therefore, due to the computational costs associated with decompressing and recompressing data, it is important that you consider the runtime implications of uploading source data that is compressed differently than the specified `sample_compression`.&#x20;
{% endhint %}


# Step 4: Accessing and Updating Data

Learn how Deep Lake Datasets can be accessed or loaded from a variety of storage locations.

## How to Access and Load Datasets with Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

### Loading Datasets

Deep Lake Datasets can be loaded from a variety of storage locations using:

```python
import deeplake

# Local Filepath
ds = deeplake.load('./my_dataset_path') # Similar functionality to deeplake.dataset(path)

# S3
ds = deeplake.load('s3://my_dataset_bucket', creds={...})

# Public Dataset hosted by Activeloop
## Activeloop Storage - See Step 6
ds = deeplake.load('hub://activeloop/public_dataset_name')

# Dataset in another organization on Activeloop Platform
ds = deeplake.load('hub://org_name/dataset_name')
```

{% hint style="warning" %}
Since `ds = deeplake.dataset(path)`can be used to both create and load datasets, you may accidentally create a new dataset if there is a typo in the path you provided while intending to load a dataset. If that occurs, simply use `ds.delete()` to remove the unintended dataset permanently.
{% endhint %}

### Referencing Tensors

Deep Lake allows you to reference specific tensors using keys or via the "." notation outlined below.&#x20;

Note: data is still not loaded by these commands.

```python
### NO HIERARCHY ###
ds.images # is equivalent to
ds['images']

ds.labels # is equivalent to
ds['labels']

### WITH HIERARCHY ###
ds.localization.boxes # is equivalent to
ds['localization/boxes']

ds.localization.labels # is equivalent to
ds['localization/labels']
```

### Accessing Data

Data within the tensors is loaded and accessed using the `.numpy()` , `.data()` , and .`tobytes()` commands. When the underlying data can be converted to a numpy array, `.data()` and `.numpy()` return equivalent objects.

```python
# Indexing
img = ds.images[0].numpy()              # Fetch the 1st image and return a NumPy array
label = ds.labels[0].numpy(aslist=True) # Fetch the 1st label and store it as a 
                                        # as a list
                                    
# frame = ds.videos[0][4].numpy()   # Fetch the 5th frame in the 1st video 
                                    # and return a NumPy array
                              
text_labels = ds.labels[0].data()['value'] # Fetch the first labels and return them as text

# Slicing
imgs = ds.images[0:100].numpy() # Fetch 100 images and return a NumPy array
                                # The method above produces an exception if 
                                # the images are not all the same size

labels = ds.labels[0:100].numpy(aslist=True) # Fetch 100 labels and store 
                                             # them as a list of NumPy arrays
```

{% hint style="info" %}
The `.numpy()`method produces an exception if all samples in the requested tensor do not have a uniform shape. If that's the case, running `.numpy(aslist=True)`returns a list of NumPy arrays, where the indices of the list correspond to different samples.&#x20;
{% endhint %}

### Updating Data

Existing data in a Deep Lake dataset can be updated using:

<pre class="language-python"><code class="lang-python">ds.images[1] = deeplake.read('https://i.postimg.cc/Yq2SNz9J/photo-1534567110243-8875d64ca8ff.jpg') # If the URI is not public, credentials should be specified using deeplake.read(URI, creds = {...})
<strong>
</strong><strong>ds.labels[1] = 'giraffe' # Tensors of htype = 'class_label' can be updated with either numeric values or text
</strong></code></pre>

```python
Image.fromarray(ds.images[1].numpy())
```


# Step 5: Visualizing Datasets

Visualizing and inspecting your datasets.

## How to Visualize Datasets in Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

One of Deep Lake's core features is to enable users to visualize and interpret large amounts of data. Let's load the COCO dataset, which is one of the most popular datasets in computer vision.

```python
import deeplake

ds = deeplake.load('hub://activeloop/coco-train')
```

The tensor layout for this dataset can be inspected using:

```python
ds.summary()
```

The dataset can be [visualized in the Activeloop App](https://app.activeloop.ai/activeloop/coco-tour) or using an iframe in a jupyter notebook. If you don't already have flask and ipython installed, make sure to install Deep Lake using `pip install deeplake[visualizer]`.

```python
ds.visualize()
```

{% hint style="info" %}
Visualizing datasets in [Activeloop App](https://app.activeloop.ai/activeloop/coco-tour) will unlock more features and faster performance compared to visualization in Jupyter notebooks.
{% endhint %}

### Visualizing your own datasets

Any Deep Lake dataset can be visualized using the methods above as long as it follows the conventions necessary for the visualization engine to interpret and parse the data. These conventions are explained in the link below:

{% content-ref url="../../../technical-details/visualization" %}
[visualization](https://docs-v3.activeloop.ai/technical-details/visualization)
{% endcontent-ref %}


# Step 6: Using Activeloop Storage

Storing and loading datasets from Deep Lake Storage.

## How to Use Activeloop-Provided Storage

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

### Register

You can store your Deep Lake Datasets with Activeloop by first creating an account in the [Deep Lake App](https://app.activeloop.ai/) or in the CLI using:

```python
activeloop register
```

### Login

In order for the Python API to authenticate with your account, you can use API tokens (see below), or log in from the CLI using:

```bash
!activeloop login

# Alternatively, you can directly input your username and password in the same line:
# activeloop login -u <your_username> -p <your_password>
```

You can then access or create Deep Lake Datasets by passing the Deep Lake path to `deeplake.dataset()`

```python
import deeplake

deeplake_path = 'hub://organization_name/dataset_name'
               #'hub://jane_smith/my_awesome_dataset'
               
ds = deeplake.dataset(deeplake_path)
```

{% hint style="info" %}
When you create an account in Deep Lake, a default organization is created that has the same name as your username. You can also create other organizations that represent companies, teams, or other collections of multiple users.&#x20;
{% endhint %}

Public datasets such as `'hub://activeloop/mnist-train'`  can be accessed without logging in.

### API Tokens

Once you have an Activeloop account, you can create tokens in the [Deep Lake App](https://app.activeloop.ai/) (`Organization Details` -> `API Tokens`) and authenticate by setting the environmental variable:&#x20;

```python
os.environ['ACTIVELOOP_TOKEN'] = <your_token>
```

Or login in the CLI using the token:

```bash
!activeloop login --token <your_token>
```

If you are not logged in through the CLI, you may also pass the token to python commands that require authentication:

```python
ds = deeplake.load(deeplake_path, token = 'xyz')
```


# Step 7: Connecting Deep Lake Datasets to ML Frameworks

Connecting Deep Lake Datasets to machine learning frameworks such as PyTorch and TensorFlow.

## How to use Deeplake with PyTorch or TensorFlow in Python

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

Deep Lake Datasets can be connected to popular ML frameworks such as PyTorch and TensorFlow, so you can train models while streaming data from the cloud without bottlenecking the training process!

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/wfsQR2CkWm4cVYT1AGvu/Data%20Streaming%20With%20DeepLake.png" alt=""><figcaption><p>Data Streaming using Deep Lake</p></figcaption></figure>

### Training models with PyTorch

There are **two syntaxes** that can be used to train models in Pytorch using Deep Lake datasets:

1. **Deep Lake Data Loaders** are highly-optimized and unlock the fastest streaming and shuffling using Deep Lake's internal shuffling method. However, they do not support custom sampling or fully-random shuffling that is possible using PyTorch datasets + data loaders.
2. **Pytorch Datasets + PyTorch Data Loaders** enable all the customizability supported by PyTorch. However, they have highly sub-optimal streaming using Deep Lake datasets and may result in 5X+ slower performance compared to using Deep Lake data loaders.

### 1. Deep Lake Data Loaders for PyTorch

{% hint style="success" %}
**Best option for fast streaming!**
{% endhint %}

The fastest streaming of data to GPUs using PyTorch is achieved using Deep Lake's built-in PyTorch dataloaders `ds.pytorch()` (OSS Dataloader written in Python) or `ds.dataloader().pytorch()` (C++ and accessible to registered users). If your model training is highly sensitive to the randomization of the input data, please pre-shuffle the data, or explore our writeup on [shuffling](https://docs-v3.activeloop.ai/technical-details/shuffling "mention").

```python
import deeplake
from torchvision import datasets, transforms, models

ds = deeplake.load('hub://activeloop/cifar100-train') # Deep Lake Dataset
```

#### ***Transform syntax #1 - For independent transforms per tensor***

The `transform` parameter in `ds.pytorch()` is a dictionary where the `key` is the tensor name and the `value` is the transformation function for that tensor. If a tensor does not need to be returned, the tensor should be omitted from the keys. If no transformation is necessary on a tensor, the transformation function is set as `None`.

```python
tform = transforms.Compose([
    transforms.ToPILImage(), # Must convert to PIL image for subsequent operations to run
    transforms.RandomRotation(20), # Image augmentation
    transforms.ToTensor(), # Must convert to pytorch tensor for subsequent operations to run
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
])

#PyTorch Dataloader
dataloader= ds.pytorch(batch_size = 16, num_workers = 2, 
    transform = {'images': tform, 'labels': None}, shuffle = True)
```

#### ***Transform syntax #2 - For complex or dependent transforms per tensor***

Sometimes a single transformation function might need to be applied to all tensors, or tensors need to be combined in a transform. In this case, you can use the syntax below to perform the exact same transform as above:

```python
def transform(sample_in):
    return {'images': tform(sample_in['images']), 'labels': sample_in['labels']}

#OSS PyTorch Dataloader
dataloader_oss = ds.pytorch(batch_size = 16, num_workers = 1,
    transform = transform, shuffle = True)


#C++ PyTorch Dataloader
dataloader_cpp= ds.dataloader().pytorch(num_workers = 1).transform(transform = transform).batch(batch_size = 16).shuffle(shuffle = True)
```

{% hint style="info" %}
Some datasets such as [ImageNet](https://app.activeloop.ai/activeloop/imagenet-train) contain both grayscale and color images, which can cause errors when the transformed images are passed to the model. To convert only the grayscale images to color format, you can add this Torchvision transform to your pipeline:

`transforms.Lambda(lambda x: x.repeat(int(3/x.shape[0]), 1, 1))`
{% endhint %}

### 2. PyTorch Datasets + PyTorch Data Loaders using Deep Lake

{% hint style="success" %}
**Best option for full customizability.**
{% endhint %}

Deep Lake datasets can be integrated in the PyTorch Dataset class by passing the `ds` object to the PyTorch Dataset's constructor and pulling data in the `__getitem__` method using `self.ds.image[ids].numpy()`:

```python
from torch.utils.data import DataLoader, Dataset

class ClassificationDataset(Dataset):
    def __init__(self, ds, transform = None):
        self.ds = ds
        self.transform = transform

    def __len__(self):
        return len(self.ds)
    
    def __getitem__(self, idx):
        image = self.ds.images[idx].numpy()
        label = self.ds.labels[idx].numpy(fetch_chunks = True).astype(np.int32)

        if self.transform is not None:
            image = self.transform(image)

        sample = {"images": image, "labels": label}

        return sample
```

{% hint style="info" %}
When loading data sequentially, or when randomly loading samples from a tensor that fits into the cache (such as `class_labels`) it is recommended to set `fetch_chunks = True`. This increases the data loading speed by avoiding separate requests for each individual sample. This is not recommended when randomly loading large tensors, because the data is deleted from the cache before adjacent samples from a chunk are used.
{% endhint %}

The PyTorch dataset + data loader is instantiated using the built-in PyTorch functions:

```python
cifar100_pytorch = ClassificationDataset(ds_train, transform = tform)

dataloader_pytroch = DataLoader(dataset_pt, batch_size = 16, num_workers = 2, shuffle = True)
```

### Iteration and Training

You can iterate through both data loaders above using the exact same syntax. Loading the first batch of data using the Deep Lake data loader may take up to 30 seconds because the [shuffle buffer](https://docs-v3.activeloop.ai/technical-details/shuffling) is filled before any data is returned.

```python
for data in dataloader_oss:
    print(data)    
    break
    
    # Training Loop
```

```python
for data in dataloader_cpp:
    print(data)
    break

    # Training Loop
```

```python
for data in dataloader_pytorch:
    print(data)    
    break
    
    # Training Loop
```

For end-2-end examples for training, check out our [Training Tutorials](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models).

### Training models with TensorFlow

Deep Lake Datasets can be converted to TensorFlow Datasets using `ds.tensorflow()`. Downstream, functions from the `tf.Data` API such as map, shuffle, etc. can be applied to process the data before training.

```python
ds # Deep Lake Dataset object, to be used for training
ds_tf = ds.tensorflow() # A TensorFlow Dataset
```


# Step 8: Parallel Computing

Running computations and processing data in parallel.

## How to Accelerate Deep Lake Workflows with Parallel Computing

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

Deep Lake enables you to easily run computations in parallel and significantly accelerate your data processing workflows. **This example primarily focuses on parallel dataset uploading.**

**Parallel computing use cases such as dataset transformations can be found in** [**this tutorial**](https://docs-v3.activeloop.ai/examples/dl/tutorials/data-processing-using-parallel-computing)**.**

Parallel compute using Deep Lake has two core steps:&#x20;

1. Define a function or pipeline that will run in parallel and
2. Evaluate the function using the appropriate inputs and outputs.&#x20;

### Defining the parallel computing function

The first step is to define a function that will run in parallel by decorating it using `@deeplake.compute`. In the example below, `file_to_deeplake` converts data from files into Deep Lake format, just like in [Step 2: Creating Hub Datasets Manually](https://docs-v3.activeloop.ai/examples/dl/guide/creating-datasets). If you have not completed Step 2, please download and unzip the example image classification dataset below:

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/CQftGlzveKhX5GzN5TSJ/animals.zip>" %}
animals dataset
{% endfile %}

```python
import deeplake
from PIL import Image
import numpy as np
import os

@deeplake.compute
def file_to_deeplake(file_name, sample_out, class_names):
    ## First two arguments are always default arguments containing:
    #     1st argument is an element of the input iterable (list, dataset, array,...)
    #     2nd argument is a dataset sample
    # Other arguments are optional
    
    # Find the label number corresponding to the file
    label_text = os.path.basename(os.path.dirname(file_name))
    label_num = class_names.index(label_text)
    
    # Append the label and image to the output sample
    sample_out.append({"labels": np.uint32(label_num),
                       "images": deeplake.read(file_name)})
    
    return sample_out
```

In all functions decorated using `@deeplake.compute`, the first argument must be a single element of any input iterable that is being processed in parallel. In this case, that is a filename `file_name`, because `file_to_deeplake` reads image files and populates data in the dataset's tensors.&#x20;

The second argument is a dataset sample `sample_out`, which can be operated on using similar syntax to dataset objects, such as `sample_out.append(...)`, `sample_out.extend(...)`, etc.

The function decorated using `@deeplake.compute` must return `sample_out`, which represents the data that is added or modified by that function.

### Executing the parallel computation

To execute the parallel computation, you must define the dataset that will be modified.

```python
ds = deeplake.empty('./animals_deeplake_transform') # Creates the dataset
```

Next, you define the input iterable that describes the information that will be operated on in parallel. In this case, that is a list of files `files_list`:

```python
# Find the class_names and list of files that need to be uploaded
dataset_folder = './animals'

class_names = os.listdir(dataset_folder)

files_list = []
for dirpath, dirnames, filenames in os.walk(dataset_folder):
    for filename in filenames:
        files_list.append(os.path.join(dirpath, filename))
```

You can now create the tensors for the dataset and **run the parallel computation** using the `.eval` syntax. Pass the optional input arguments to `file_to_deeplake` and skip the first two default arguments `file_name` and `sample_out`.&#x20;

The input iterable `files_list` and output dataset `ds` is passed to the `.eval` method as the first and second argument respectively.

```python
with ds:
    ds.create_tensor('images', htype = 'image', sample_compression = 'jpeg')
    ds.create_tensor('labels', htype = 'class_label', class_names = class_names)
    
    file_to_deeplake(class_names=class_names).eval(files_list, ds, num_workers = 2)
```

**Additional parallel computing use cases such as dataset transformations can be found in** [**this tutorial**](https://docs-v3.activeloop.ai/examples/dl/tutorials/data-processing-using-parallel-computing)**.**

```python
Image.fromarray(ds.images[0].numpy())
```

Congrats! You just created a dataset using parallel computing! 🎈


# Step 9: Dataset Version Control

Managing changes to your datasets using Version Control.

## How to Use Version Control in Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

Deep Lake dataset version control allows you to manage changes to datasets with commands very similar to Git. It provides critical insights into how your data is evolving, and it works with datasets of any size!

Let's check out how dataset version control works in Deep Lake! If you haven't done so already, please download and unzip the *animals* dataset from [Step 2](https://docs-v3.activeloop.ai/examples/dl/guide/creating-datasets).&#x20;

First let's create a Deep Lake dataset in the `./version_control_deeplake` folder.

```python
import deeplake
import numpy as np
from PIL import Image

# Set overwrite = True for re-runability
ds = deeplake.dataset('./version_control_deeplake', overwrite = True)

# Create a tensor and add an image
with ds:
    ds.create_tensor('images', htype = 'image', sample_compression = 'jpeg')
    ds.images.append(deeplake.read('./animals/cats/image_1.jpg'))
```

The first image in this dataset is a picture of a cat:

```
Image.fromarray(ds.images[0].numpy())
```

### Commit

To commit the data added above, simply run `ds.commit`:

```python
first_commit_id = ds.commit('Added image of a cat')

print('Dataset in commit {} has {} samples'.format(first_commit_id, len(ds)))
```

Next, let's add another image and commit the update:

```python
with ds:
    ds.images.append(deeplake.read('./animals/dogs/image_3.jpg'))
    
second_commit_id = ds.commit('Added an image of a dog')

print('Dataset in commit {} has {} samples'.format(second_commit_id, len(ds)))
```

The second image in this dataset is a picture of a dog:&#x20;

```
Image.fromarray(ds.images[1].numpy())
```

### Log

The commit history starting from the current commit can be show using `ds.log`:

```python
log = ds.log()
```

This command prints the log to the console and also assigns it to the specified variable `log`. The author of the commit is the username of the [Activeloop account](https://docs-v3.activeloop.ai/examples/dl/guide/using-activeloop-storage) that logged in on the machine.

### Branch

Branching takes place by running the `ds.checkout` command with the parameter `create = True` . Let's create a new branch `dog_flipped`, flip the second image (dog), and create a new commit on that branch.

```python
ds.checkout('dog_flipped', create = True)

with ds:
    ds.images[1] = np.transpose(ds.images[1], axes=[1,0,2])

flipped_commit_id = ds.commit('Flipped the dog image')
```

The dog image is now flipped and the log shows a commit on the `dog_flipped` branch as well as the previous commits on `main`:&#x20;

```
Image.fromarray(ds.images[1].numpy())
```

```
ds.log()
```

### Checkout

A previous commit of the branch can be checked out using `ds.checkout`:

```python
ds.checkout('main')

Image.fromarray(ds.images[1].numpy())
```

As expected, the dog image on `main` is not flipped.

### Diff

Understanding changes between commits is critical for managing the evolution of datasets. Deep Lake's `ds.diff` function enables users to determine the number of samples that were added, removed, or updated for each tensor. The function can be used in 3 ways:

```python
ds.diff() # Diff between the current state and the last commit

ds.diff(commit_id) # Diff between the current state and a specific commit

ds.diff(commit_id_1, commit_id_2) # Diff between two specific commits
```

### HEAD Commit

Unlike Git, Deep Lake's dataset version control does not have a local staging area because all dataset updates are immediately synced with the permanent storage location (cloud or local). Therefore, any changes to a dataset are automatically stored in a HEAD commit on the current branch. This means that the uncommitted changes do not appear on other branches, and uncommitted changes are visible to all users.

#### Let's see how this works:

You should currently be on the `main` branch, which has 2 samples. You can check for uncommited changes using:

```python
ds.has_head_changes
```

Let's add another image:

```python
print('Dataset on {} branch has {} samples'.format('main', len(ds)))

with ds:
    ds.images.append(deeplake.read('./animals/dogs/image_4.jpg'))
    
print('After updating, the HEAD commit on {} branch has {} samples'.format('main', len(ds)))
```

The 3rd sample is also an image of a dog:

```
Image.fromarray(ds.images[2].numpy())
```

Next, if you checkout `dog_flipped` branch, the dataset contains 2 samples, which is sample count from when that branch was created. Therefore, the additional uncommitted third sample that was added to the `main` branch above is not reflected when other branches or commits are checked out.

```python
ds.checkout('dog_flipped')

print('Dataset in {} branch has {} samples'.format('dog_flipped', len(ds)))
```

Finally, when checking our the `main` branch again, the prior uncommitted changes and available and they are stored in the HEAD commit on `main`:

```python
ds.checkout('main')

print('Dataset in {} branch has {} samples'.format('main', len(ds)))
```

The dataset now contains 3 samples and the uncommitted dog image is visible:

```
Image.fromarray(ds.images[2].numpy())
```

You can delete any uncommitted changes using the `reset` command below, which will bring the `main` branch back to the state with 2 samples.

```python
ds.reset()

print('Dataset in {} branch has {} samples'.format('main', len(ds)))
```

### Merge

Merging is a critical feature for collaborating on datasets. It enables you to modify data on separate branches before making those changes available on the `main` branch, thus enabling you to experiment on your data without affecting workflows by other collaborators.

We are currently on the `main` branch where the picture of the dog is right-side-up.

```
ds.log()
```

```python
Image.fromarray(ds.images[1].numpy())
```

We can merge the `dog_flipped` branch into `main` using the command below:

```python
ds.merge('dog_flipped')
```

After merging the `dog_flipped` branch, we observe that the image of the dog is flipped. The dataset log now has a commit indicating that a commit from another branch was merged to `main`.

```python
Image.fromarray(ds.images[1].numpy())
```

```python
ds.log()
```

Congrats! You just are now an expert in dataset version control! 🎓


# Step 10: Dataset Filtering

Filtering datasets using user-defined-functions or SQL-style queries.

## How to Filter and Query Data in Deep Lake

#### [Colab Notebook](https://colab.research.google.com/drive/1Va9cIxZpP0CbYjLZqTcMOntXPmfaeuVy?usp=sharing)

Filtering and querying is an important aspect of data engineering because analyzing and utilizing data in smaller units is much more productive than executing workflows on all data all the time.&#x20;

Queries can be performed in Deep Lake enables with user-defined functions, or they can be executed in [Activeloop Platform](https://app.activeloop.ai/) using our highly-performance SQL-style query language.

### Filtering using our Tensor Query Language (TQL)

Deep Lake offers a [highly-performant SQL-style query language](https://docs-v3.activeloop.ai/examples/tql) that is built in C++ and is optimized for Deep Lake datasets. Queries and their results are executed and saved in the UI, and they can be accessed in Deep Lake using using the the `Dataset Views` API described below.

Full details about the query language are described in a [standalone tutorial](https://docs-v3.activeloop.ai/examples/tql).

### Filtering with user-defined-functions (UDF)

The first step for querying using UDFs is to define a function that returns a boolean depending on whether an dataset sample meets the user-defined condition. In this example, we define a function that returns `True` if the labels in a tensor are in the desired `labels_list`. If there are inputs to the filtering function other than `sample_in`, it must be decorated with `@deeplake.compute`.

```python
import deeplake
from PIL import Image

# Let's create a local copy of the dataset (Explanation is in the next section)
ds = deeplake.deepcopy('hub://activeloop/mnist-train', './mnist-train-local') 
```

```python
labels_list = ['0', '8'] # Desired labels for filtering

@deeplake.compute
def filter_labels(sample_in, labels_list):
    
    return sample_in.labels.data()['text'][0] in labels_list
```

The filtering function is executed using the `ds.filter()` command below, and it returns a `Dataset View` that only contains the indices that met the filtering condition (*more details below*). Just like in the [Parallel Computing API](https://docs-v3.activeloop.ai/examples/dl/guide/parallel-computing), the `sample_in` parameter does not need to be passed into the filter function when evaluating it, and multi-processing can be specified using the `scheduler` and `num_workers` parameters.

```python
ds_view = ds.filter(filter_labels(labels_list), scheduler = 'threaded', num_workers = 0)
```

```python
print(len(ds_view))
```

{% hint style="info" %}
In most cases, multi-processing is not necessary for queries that involve simple data such as labels or bounding boxes. However, multi-processing significantly accelerates queries that must load rich data types such as images and videos.
{% endhint %}

### Dataset Views

A `Dataset View` is any subset of a Deep Lake dataset that does not contains all of the samples. It can be an output of a query, filtering function, or regular indexing like `ds[0:2:100]`.

{% hint style="info" %}
In the filtering example above, we copied `mnist-train` locally in order to gain write access to the dataset. With write access, the views are saved as part of the dataset. Without write access, views are stored elsewhere or in custom paths, and full details are [available here](https://api-docs.activeloop.ai/#hub.Dataset.save_view). Users have write access to their own datasets, regardless of whether the datasets are local or in the cloud.
{% endhint %}

The data in the returned `ds_view` can be accessed just like a regular dataset.&#x20;

```python
Image.fromarray(ds_view.images[10].numpy())
```

A `Dataset View` can be saved permanently using the method below, which stores its indices without copying the data:

```python
ds_view.save_view(message = 'Samples with 0 and 8')
```

{% hint style="warning" %}
In order to maintain data lineage, `Dataset Views` are immutable and are connected to specific commits. Therefore, views can only be saved if the dataset has a commit and there are no uncommitted changes in the `HEAD`.&#x20;
{% endhint %}

Each `Dataset View` has a unique `id`, and views can be examined or loaded using:

```python
views = ds.get_views()

print(views)
```

```python
ds_view = views[0].load()

# OR

# ds_view = ds.load_view(id)
```

```python
print(len(ds_view))
```

Congrats! You just learned to filter and query data with Deep Lake! 🎈


# Deep Learning Tutorials

Tutorials for using Deep Lake in deep-learning applications.

## How to use Deep Lake for Deep Learning Applications

Deep Lake can be used as tool for managing Deep Learning data, including rapidly training models while streaming data, running queries, tracking dataset versions, visualizing datasets, and more.

These tutorials show how to use Deep Lake's low-level API for deep-learning use cases.&#x20;

### Deep Learning Tutorials:

{% content-ref url="tutorials/creating-datasets" %}
[creating-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets)
{% endcontent-ref %}

{% content-ref url="tutorials/training-models" %}
[training-models](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models)
{% endcontent-ref %}

{% content-ref url="tutorials/updating-datasets" %}
[updating-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/updating-datasets)
{% endcontent-ref %}

{% content-ref url="tutorials/data-processing-using-parallel-computing" %}
[data-processing-using-parallel-computing](https://docs-v3.activeloop.ai/examples/dl/tutorials/data-processing-using-parallel-computing)
{% endcontent-ref %}


# Creating Datasets

Workflows for creating Deep Lake datasets

## How to Create Datasets in Deep Lake

Deep Lake can support almost any data schema and format that can be tabularized. [The full list of supported data types are shown here](https://docs.deeplake.ai/en/latest/Htypes.html), and details on the [Deep Lake dataset format are shown here](https://docs-v3.activeloop.ai/technical-details/data-format).&#x20;

Below is a series of tutorials for creating custom datasets using our low-level API. Deep Lake also supports [automatic data ingestion for the formats shown here](https://docs-v3.activeloop.ai/examples/dl/quickstart).&#x20;

{% content-ref url="creating-datasets/creating-complex-datasets" %}
[creating-complex-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-complex-datasets)
{% endcontent-ref %}

{% content-ref url="creating-datasets/creating-object-detection-datasets" %}
[creating-object-detection-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-object-detection-datasets)
{% endcontent-ref %}

{% content-ref url="creating-datasets/creating-time-series-datasets" %}
[creating-time-series-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-time-series-datasets)
{% endcontent-ref %}

{% content-ref url="creating-datasets/creating-datasets-with-sequences" %}
[creating-datasets-with-sequences](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-datasets-with-sequences)
{% endcontent-ref %}

{% content-ref url="creating-datasets/creating-video-datasets" %}
[creating-video-datasets](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-video-datasets)
{% endcontent-ref %}


# Creating Complex Datasets

Converting a multi-annotation dataset to Deep Lake format is helpful for understanding how to use Deep Lake with rich data.

## How to create datasets with multiple annotation types

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1H6T_jL3Eaqmm0pBR_Tf8bUEb9BC3QUl0?usp=sharing)

Datasets often have multiple labels such as classifications, bounding boxes, segmentations, and others.  In order to create an intuitive layout of tensors, it's advisable to create a dataset hierarchy that captures the relationship between the different label types. This can be done with Deep Lake tensor `groups`.

This example show to to use groups to create a dataset containing image classifications of "indoor" and "outdoor", as well as bounding boxes of objects such as "dog" and "cat".&#x20;

### Create the Deep Lake Dataset

The first step is to download the small dataset below called *animals complex*.

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/7rw1hQ4BTJwpKfxKdROe/animals_complex.zip>" %}
animals complex dataset
{% endfile %}

The images and their classes are stored in a `classification` folder where the subfolders correspond to the class names. Bounding boxes for object detection are stored in a separate `boxes` subfolder, which also contains a list of class names for object detection in the file `box_names.txt`.  In YOLO format, images and annotations are typically matched using a common filename such as `image -> filename.jpeg` and `annotation -> filename.txt` . The data structure for the dataset is shown below:

```python
data_dir
|_classification
    |_indoor
        |_image1.png
        |_image2.png
    |_outdoor
        |_image3.png
        |_image4.png
|_boxes
    |_image1.txt
    |_image3.txt
    |_image3.txt
    |_image4.txt
    |_classes.txt
```

Now that you have the data, let's **create a Deep Lake Dataset** in the `./animals_complex_deeplake` folder by running:&#x20;

```python
import deeplake
from PIL import Image, ImageDraw
import numpy as np
import os

ds = deeplake.empty('./animals_complex_deeplake') # Create the dataset locally
```

Next, let's specify the folder paths containing the classification and object detection data. It's also helpful to create a list of all of the image files and class names for classification and object detection tasks.

```python
classification_folder = './animals_complex/classification'
boxes_folder = './animals_complex/boxes'

# List of all class names for classification
class_names = os.listdir(classification_folder)

fn_imgs = []
for dirpath, dirnames, filenames in os.walk(classification_folder):
    for filename in filenames:
        fn_imgs.append(os.path.join(dirpath, filename))

# List of all class names for object detection        
with open(os.path.join(boxes_folder, 'classes.txt'), 'r') as f:
    class_names_boxes = f.read().splitlines()
```

Since annotations in YOLO are typically stored in text files, it's useful to write a helper function that parses the annotation file and returns numpy arrays with the bounding box coordinates and bounding box classes.

```python
def read_yolo_boxes(fn:str):
    """
    Function reads a label.txt YOLO file and returns a numpy array of yolo_boxes 
    for the box geometry and yolo_labels for the corresponding box labels.
    """
    
    box_f = open(fn)
    lines = box_f.read()
    box_f.close()
    
    # Split each box into a separate lines
    lines_split = lines.splitlines()
    
    yolo_boxes = np.zeros((len(lines_split),4))
    yolo_labels = np.zeros(len(lines_split))
    
    # Go through each line and parse data
    for l, line in enumerate(lines_split):
        line_split = line.split()
        yolo_boxes[l,:]=np.array((float(line_split[1]), float(line_split[2]), float(line_split[3]), float(line_split[4])))
        yolo_labels[l]=int(line_split[0]) 
         
    return yolo_boxes, yolo_labels
```

Next, let's create the groups and tensors for this data. In order to separate the two annotations, a `boxes` group is created to wrap around the `label` and `bbox` tensors which contains the coordinates and labels for the bounding boxes.

```python
with ds:
    # Image
    ds.create_tensor('images', htype='image', sample_compression='jpeg')
    
    # Classification
    ds.create_tensor('labels', htype='class_label', class_names = class_names)
    
    # Object Detection
    ds.create_group('boxes')
    ds.boxes.create_tensor('bbox', htype='bbox')
    ds.boxes.create_tensor('label', htype='class_label', class_names = class_names_boxes)
    # An alternate approach is to use '/' notation, which automatically creates the boxes group
    # ds.create_tensor('boxes/bbox', ...)
    # ds.create_tensor('boxes/label', ...)
    
    # Define the format of the bounding boxes
    ds.boxes.bbox.info.update(coords = {'type': 'fractional', 'mode': 'LTWH'})
```

{% hint style="warning" %}
In order for Activeloop Platform to correctly visualize the labels, `class_names` must be a list of strings, where the numerical labels correspond to the index of the label in the list.
{% endhint %}

Finally, let's iterate through all the images in the dataset in order to upload the data in Deep Lake. The first axis of the `boxes.bbox` sample array corresponds to the first-and-only axis of the `boxes.label` sample array (i.e. if there are 3 boxes in an image, the labels array is 3x1 and the boxes array is 3x4).

```python
with ds:
    #Iterate through the images
    for fn_img in fn_imgs:
        
        img_name = os.path.splitext(os.path.basename(fn_img))[0]
        fn_box = img_name+'.txt'
        
        # Get the class number for the classification
        label_text = os.path.basename(os.path.dirname(fn_img))
        label_num = class_names.index(label_text)
    
        # Get the arrays for the bounding boxes and their classes
        yolo_boxes, yolo_labels = read_yolo_boxes(os.path.join(boxes_folder,fn_box))
        
        # Append data to tensors
        ds.append({'images': deeplake.read(os.path.join(fn_img)),
                   'labels': np.uint32(label_num),
                   'boxes/label': yolo_labels.astype(np.uint32),
                   'boxes/bbox': yolo_boxes.astype(np.float32)
        })
```

### Inspect the Deep Lake Dataset&#x20;

Let's check out the second sample from this dataset and visualize the labels.

```python
# Draw bounding boxes and the classfication label for the second image

ind = 1
img = Image.fromarray(ds.images[ind].numpy())
draw = ImageDraw.Draw(img)
(w,h) = img.size
boxes = ds.boxes.bbox[ind].numpy()

for b in range(boxes.shape[0]):
    (xc,yc) = (int(boxes[b][0]*w), int(boxes[b][1]*h))
    (x1,y1) = (int(xc-boxes[b][2]*w/2), int(yc-boxes[b][3]*h/2))
    (x2,y2) = (int(xc+boxes[b][2]*w/2), int(yc+boxes[b][3]*h/2))
    draw.rectangle([x1,y1,x2,y2], width=2)
    draw.text((x1,y1), ds.boxes.label.info.class_names[ds.boxes.label[ind].numpy()[b]])
    draw.text((0,0), ds.labels.info.class_names[ds.labels[ind].numpy()[0]])
```

```python
# Display the image and its bounding boxes
img
```

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/nyFhCMC5JRI7rtyYWqgs/dog_and_cat_boxes_and_class.png)

Congrats! You just created a dataset with multiple types of annotations! 🎉


# Creating Object Detection Datasets

Converting an object detection dataset to Deep Lake format is a great way to get started with datasets of increasing complexity.

## How to convert a YOLO object detection dataset to Deep Lake format

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1ExJsPHoqrs0XS3KzVPZymkGPHgZ1o6hx?usp=sharing)

Object detection using bounding boxes is one of the most common annotation types for Computer Vision datasets. This tutorial demonstrates how to convert an object detection dataset from YOLO format to Deep Lake, and a similar method can be used to convert object detection datasets from other formats such as COCO and PASCAL VOC.

### Create the Deep Lake Dataset

The first step is to download the small dataset below called *animals object detection*.

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/UhCfaxMiNCspJ5ntY0KH/animals_od.zip>" %}
animals object detection dataset
{% endfile %}

The dataset has the following folder structure:

```
data_dir
|_images
    |_image_1.jpg
    |_image_2.jpg
    |_image_3.jpg
    |_image_4.jpg
|_boxes
    |_image_1.txt
    |_image_2.txt
    |_image_3.txt
    |_image_4.txt
    |_classes.txt
```

Now that you have the data, let's **create a Deep Lake Dataset** in the `./animals_od_deeplake`folder by running:

```python
import deeplake
from PIL import Image, ImageDraw
import numpy as np
import os

ds = deeplake.empty('./animals_od_deeplake') # Create the dataset locally
```

Next, let's specify the folder paths containing the images and annotations in the dataset. In YOLO format, images and annotations are typically matched using a common filename such as `image -> filename.jpeg` and `annotation -> filename.txt` . It's also helpful to create a list of all of the image files and the class names contained in the dataset.

```python
img_folder = './animals_od/images'
lbl_folder = './animals_od/boxes'

# List of all images
fn_imgs = os.listdir(img_folder)

# List of all class names
with open(os.path.join(lbl_folder, 'classes.txt'), 'r') as f:
    class_names = f.read().splitlines()
```

Since annotations in YOLO are typically stored in text files, it's useful to write a helper function that parses the annotation file and returns numpy arrays with the bounding box coordinates and bounding box classes.

```python
def read_yolo_boxes(fn:str):
    """
    Function reads a label.txt YOLO file and returns a numpy array of yolo_boxes 
    for the box geometry and yolo_labels for the corresponding box labels.
    """
    
    box_f = open(fn)
    lines = box_f.read()
    box_f.close()
    
    # Split each box into a separate lines
    lines_split = lines.splitlines()
    
    yolo_boxes = np.zeros((len(lines_split),4))
    yolo_labels = np.zeros(len(lines_split))
    
    # Go through each line and parse data
    for l, line in enumerate(lines_split):
        line_split = line.split()
        yolo_boxes[l,:]=np.array((float(line_split[1]), float(line_split[2]), float(line_split[3]), float(line_split[4])))
        yolo_labels[l]=int(line_split[0]) 
         
    return yolo_boxes, yolo_labels
```

Finally, let's create the tensors and iterate through all the images in the dataset in order to upload the data in Deep Lake. Boxes and their labels will be stored in separate tensors, and for a given sample, the first axis of the boxes array corresponds to the first-and-only axis of the labels array (i.e. if there are 3 boxes in an image, the labels array is 3x1 and the boxes array is 3x4).

```python
with ds:
    ds.create_tensor('images', htype='image', sample_compression = 'jpeg')
    ds.create_tensor('labels', htype='class_label', class_names = class_names)
    ds.create_tensor('boxes', htype='bbox')
    
    # Define the format of the bounding boxes
    ds.boxes.info.update(coords = {'type': 'fractional', 'mode': 'LTWH'})

    for fn_img in fn_imgs:

        img_name = os.path.splitext(fn_img)[0]
        fn_box = img_name+'.txt'
        
        # Get the arrays for the bounding boxes and their classes
        yolo_boxes, yolo_labels = read_yolo_boxes(os.path.join(lbl_folder,fn_box))
        
        # Append data to tensors
        ds.append({'images': deeplake.read(os.path.join(img_folder, fn_img)),
                   'labels': yolo_labels.astype(np.uint32),
                   'boxes': yolo_boxes.astype(np.float32)
                   })
```

{% hint style="warning" %}
In order for Activeloop Platform to correctly visualize the labels, `class_names` must be a list of strings, where the numerical labels correspond to the index of the label in the list.
{% endhint %}

### Inspect the Deep Lake Dataset&#x20;

Let's check out the third sample from this dataset, which contains two bounding boxes.

```python
# Draw bounding boxes for the fourth image

ind = 3
img = Image.fromarray(ds.images[ind ].numpy())
draw = ImageDraw.Draw(img)
(w,h) = img.size
boxes = ds.boxes[ind].numpy()

for b in range(boxes.shape[0]):
    (xc,yc) = (int(boxes[b][0]*w), int(boxes[b][1]*h))
    (x1,y1) = (int(xc-boxes[b][2]*w/2), int(yc-boxes[b][3]*h/2))
    (x2,y2) = (int(xc+boxes[b][2]*w/2), int(yc+boxes[b][3]*h/2))
    draw.rectangle([x1,y1,x2,y2], width=2)
    draw.text((x1,y1), ds.labels.info.class_names[ds.labels[ind].numpy()[b]])
```

```python
# Display the image and its bounding boxes
img
```

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/YNTEgkKW4M3TRVdovlp6/dog_and_cat_boxes.png)

Congrats! You just created a beautiful object detection dataset! 🎉

{% hint style="info" %}
**Note:** For optimal object detection model performance, it is often important for datasets to contain images with no annotations (See the 4th sample in the dataset above). Empty samples can be appended using:

`ds.boxes.append(None)`

or by specifying an empty array whose `len(shape)` is equal to that of the other samples in the tensor:

`ds.boxes.append(np.zeros(0,4))` #`len(sample.shape) == 2`
{% endhint %}


# Creating Time-Series Datasets

Deep Lake is a powerful tool for easily storing and sharing time-series datasets with your team.

## How to use Deep Lake to store time-series data

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1MX2PjzfPRXaxymWtGP81-81pm8E61sZQ?usp=sharing)

Deep Lake is intuitive format for storing large time-series datasets and it offers compression for reducing storage costs. This tutorial demonstrates how to convert a time-series data to Deep Lake format and load the data for plotting.&#x20;

### Create the Deep Lake Dataset

The first step is to download the small dataset below called *sensor data.*

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/O9DlMbh9xc6bdMSGJJyw/sensor_data.zip>" %}

This is a subset of a [dataset available on kaggle](https://www.kaggle.com/malekzadeh/motionsense-dataset), and it contains the iPhone x,y,z acceleration for 24 users (subjects) under conditions of walking and jogging. The dataset has the folder structure below. `subjects_info.csv` contains metadata such as `height`, `weight`, etc. for each subject, and the `sub_n.csv` files contains the time-series acceleration data for the `nth` subject.

```python
data_dir
|_subjects_into.csv
|_motion_data
    |_walk
        |_sub_1.csv
        |_sub_2.csv
        ...
        ...
    |_jog
        |_sub_1.csv
        |_sub_2.csv
        ...
        ...
```

Now that you have the data, let's **create a Deep Lake Dataset** in the `./sensor_data_deeplake` folder by running:&#x20;

```python
import deeplake
import pandas as pd
import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

ds = deeplake.empty('./sensor_data_deeplake') # Create the dataset locally
```

Next, let's specify the folder path containing the existing dataset, load the subjects metadata to a Pandas DataFrame, and create a list of all of the time-series files that should be converted to Deep Lake format.

```python
dataset_path= './sensor_data'

subjects_info = pd.read_csv(os.path.join(dataset_path, 'subjects_info.csv'))

fns_series = []
for dirpath, dirnames, filenames in os.walk(os.path.join(dataset_path, 'motion_data')):
    for filename in filenames:
        fns_series .append(os.path.join(dirpath, filename))
```

Next, let's create the `tensors` and add relevant metadata, such as the dataset source, the tensor units, and other information. We leverage `groups` to separate out the primary acceleration data from other user data such as the weight and height of the subjects.&#x20;

```python
with ds:
    #Update dataset metadata
    ds.info.update(source = 'https://www.kaggle.com/malekzadeh/motionsense-dataset', 
                   notes = 'This is a small subset of the data in the source link')

    #Create tensors. Setting chunk_compression is optional and it defaults to None
    ds.create_tensor('acceleration_x', chunk_compression = 'lz4') 
    ds.create_tensor('acceleration_y', chunk_compression = 'lz4')
    
    # Save the sampling rate as tensor metadata. Alternatively,
    # you could also create a 'time' tensor.
    ds.acceleration_x.info.update(sampling_rate_s = 0.1)
    ds.acceleration_y.info.update(sampling_rate_s = 0.1)
    
    # Encode activity as text
    ds.create_tensor('activity', htype = 'text')
    
    # Encode 'activity' as numeric labels and convert to text via class_names
    # ds.create_tensor('activity', htype = 'class_label', class_names = ['xyz'])
    
    ds.create_group('subjects_info')
    ds.subjects_info.create_tensor('age')
    ds.subjects_info.create_tensor('weight')
    ds.subjects_info.create_tensor('height')
    
    # Save the units of weight as tensor metadata
    ds.subjects_info.weight.info.update(units = 'kg')
    ds.subjects_info.height.info.update(units = 'cm')
```

Finally, let's iterate through all the time-series data and upload it to the Deep Lake dataset.  &#x20;

```python
with ds:
    # Iterate through the time series and append data
    for fn in tqdm(fns_series):
        
        # Read the data in the time series
        df_data = pd.read_csv(fn)
        
        # Parse the 'activity' from the file name
        activity = os.path.basename(os.path.dirname(fn))
        
        # Parse the subject code from the filename  and pull the subject info from 'subjects_info'
        subject_code = int(os.path.splitext(os.path.basename(fn))[0].split('_')[1])
        subject_info = subjects_info[subjects_info['code']==subject_code]
        
        # Append data to tensors
        ds.activity.append(activity)
        ds.subjects_info.age.append(subject_info['age'].values)
        ds.subjects_info.weight.append(subject_info['weight'].values)
        ds.subjects_info.height.append(subject_info['height'].values)
                
        ds.acceleration_x.append(df_data['userAcceleration.x'].values)
        ds.acceleration_y.append(df_data['userAcceleration.y'].values)
```

### Inspect the Deep Lake Dataset

Let's check out the first sample from this dataset and plot the acceleration time-series.

{% hint style="success" %}
**It is noteworthy that the Deep Lake dataset takes 36% less memory than the original dataset due to `lz4` chunk compression for the acceleration tensors.**
{% endhint %}

```python
s_ind = 0 # Plot the first time series
t_ind = 100 # Plot the first 100 indices in the time series

#Plot the x acceleration
x_data = ds.acceleration_x[s_ind].numpy()[:t_ind]
sampling_rate_x = ds.acceleration_x.info.sampling_rate_s

plt.plot(np.arange(0, x_data.size)*sampling_rate_x, x_data, label='acceleration_x')

#Plot the y acceleration
y_data = ds.acceleration_y[s_ind].numpy()[:t_ind]
sampling_rate_y = ds.acceleration_y.info.sampling_rate_s

plt.plot(np.arange(0, y_data.size)*sampling_rate_y, y_data, label='acceleration_y')

plt.legend()
plt.xlabel('time [s]', fontweight = 'bold')
plt.ylabel('acceleration [g]', fontweight = 'bold')
plt.title('Weight: {} {}, Height: {} {}'.format(ds.subjects_info.weight[s_ind].numpy()[0],
                                               ds.subjects_info.weight.info.units,
                                               ds.subjects_info.height[s_ind].numpy()[0],
                                               ds.subjects_info.height.info.units),
         fontweight = 'bold')

plt.xlim([0, 10])
plt.grid()
plt.gcf().set_size_inches(8, 5)
plt.show()
```

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/bRQTh4v3mY0SBQZDw1eq/time_series_plot.png)

Congrats! You just converted a time-series dataset to Deep Lake format! 🎉


# Creating Datasets with Sequences

Deep Lake sequences are a powerful tool for storing temporal annotations such as bounding boxes in each frame of a video.

## How to create a dataset with sequences of images and labels

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1HdQNTJhnFGDtv_zlWJ70tq_4l7-ty7jh?usp=sharing)

Deep learning with computer vision is increasingly moving in a direction of temporal data, where video frames and their labels are stored as sequences, rather than independent images. Models trained on this data directly account for the temporal information content, rather than making predictions frame-by-frame and then fusing them with non-deep-learning techniques.

### Create the Deep Lake Dataset

The first step is to download the dataset [Multiple Object Tracking Benchmark](https://motchallenge.net/data/MOT16/). Additional information about this data and its format is in [this GitHub Repo](https://github.com/JonathonLuiten/TrackEval/blob/master/docs/MOTChallenge-Official/Readme.md).

The dataset has the following folder structure:

```
data_dir
|_train
    |_MOT16_N (Folder with sequence N)
        |_det
        |_gt (Folder with ground truth annotations)
        |_img1 (Folder with images the sequence)
            |_00000n.jpg (image of n-th frame in sequence)
    |_MOT16_M
    ....
|_test (same structure as _train)
```

The annotations in `gt.txt` have the format below, and the last 4 items (conf->z) are not used in the Deep Lake dataset:

```
frame, id, bb_left, bb_top, bb_width, bb_height, conf, x, y, z
```

Now we're ready to **create a Deep Lake Dataset** in the `./mot_2016_train` folder by running:

```python
import deeplake
import os
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw

ds = deeplake.empty('./mot_2015_train') # Create the dataset locally
```

Next, let's write code to inspect the folder structure for the downloaded dataset and create a list of folders containing the sequences:

```python
dataset_folder = '/MOT16/train'

sequences = [ item for item in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, item)) ]
```

Finally, let's create the tensors by using the `sequence[...]` [htype](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/broken-reference), iterate through each sequence, and iterate through each frame within the sequence, one-by-one.&#x20;

{% hint style="success" %}
Data is appended to `sequence[...]` htypes using lists. The list contains the whole sample, and the individual elements of the list are the individual data points, such as the image frame, the bounding boxes in a particular frame, etc.&#x20;

See end of code block below.
{% endhint %}

```python
with ds:
    # Define tensors
    ds.create_tensor('frames', htype = 'sequence[image]', sample_compression = 'jpg')
    ds.create_tensor('boxes', htype = 'sequence[bbox]')
    ds.create_tensor('ids', htype = 'sequence[]', dtype = 'uint32') # Ids are not uploaded as htype = 'class_labels' because they don't contain information about the class of an object.

    ds.boxes.info.update(coords = {'type': 'pixel', 'mode': 'LTWH'}) # Bounding box format is left, top, width, height

    # Iterate through each sequence
    for sequence in sequences:

        # Define root directory for that sequence    
        root_local = os.path.join(dataset_folder,sequence, 'img1')
        
        # Get a list of all the image paths
        img_paths = [os.path.join(root_local, item) for item in sorted(os.listdir(root_local))]

        # Read the annotations and convert to dataframe
        with open(os.path.join(dataset_folder,sequence, 'gt', 'gt.txt')) as f:
            anns = [line.rstrip('\n') for line in f]
        
        anns_df = pd.read_csv(os.path.join(dataset_folder, sequence, 'gt', 'gt.txt'), header = None)

        # Get the frames from the annotations and make sure they're of equal length as the images
        frames = pd.unique(anns_df[0])
        assert len(frames) == len(img_paths)

        # Iterate through each frame and add data to sequence
        boxes_seq = []
        ids_seq = []
        for frame in frames:
            ann_df = anns_df[anns_df[0] == frame] # Find annotations in the specific frame

            boxes_seq.append(ann_df.loc[:, [2, 3, 4, 5]].to_numpy().astype('float32')) # Box coordinates are in the 3rd-6th column

            ids_seq.append(ann_df.loc[:, 1].to_numpy().astype('uint32')) # ids are in the second column
        
        # Append the sequences to the deeplake dataset
        ds.append({
            "frames": [deeplake.read(path) for path in img_paths],
            "boxes": boxes_seq,
            "ids": ids_seq})
```

{% hint style="warning" %}
This dataset identifies objects by `id`, where each `id` represents an instance of an object. However, the `id` does not identify the class of the object, such `person`, `car`, `truck`, etc. Therefore, the `ids` were not uploaded as `htype = "class_label"`.
{% endhint %}

### Inspect the Deep Lake Dataset&#x20;

Let's check out the 10th frame in the 6th sequence in this dataset. A complete visualization of this dataset is available in [Activeloop Platform](https://app.activeloop.ai/activeloop/mot2016-train).

```python
# Draw bounding boxes for the 10th frame in the 6th sequence

seq_ind = 5
frame_ind = 9
img = Image.fromarray(ds.frames[seq_ind][frame_ind].numpy())
draw = ImageDraw.Draw(img)
(w,h) = img.size
boxes = ds.boxes[seq_ind][frame_ind].numpy()

for b in range(boxes.shape[0]):
    (x1,y1) = (int(boxes[b][0]), int(boxes[b][1]))
    (x2,y2) = (int(boxes[b][0]+boxes[b][2]), int(boxes[b][1]+boxes[b][3]))
    draw.rectangle([x1,y1,x2,y2], width=2, outline = 'red')
```

```python
# Display the frame and its bounding boxes
img
```

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/3lutwx8g0kTb62zyntiH/sequence_tutorial.jpg)

Congrats! You just created a dataset using sequences! 🎉


# Creating Video Datasets

Get started with video datasets using Deep Lake.

## How to convert a video dataset to Deep Lake format

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1OynSW2a2zCGMujN9Wrabm_cCogNZIrzN?usp=sharing)

Video datasets are becoming increasingly common in Computer Vision applications. This tutorial demonstrates how to convert a simple video classification dataset into Deep Lake format. Uploading videos in Deep Lake is nearly identical as uploading images, aside from minor differences in sample compression that are described below.

{% hint style="warning" %}
When using Deep Lake with videos, make sure to install it using ***one*** of the following options:

`pip3 install "deeplake[av]"`

`pip3 install "deeplake[all]"`
{% endhint %}

### Create the Deep Lake Dataset

The first step is to download the small dataset below called *running walking*.

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/dUI6iqxxh0tPTMLIFdLp/running_walking.zip>" %}
animals object detection dataset
{% endfile %}

The dataset has the following folder structure:

```
data_dir
|_running
    |_video_1.mp4
    |_video_2.mp4
|_walking
    |_video_3.mp4
    |_video_4.mp4
```

Now that you have the data, let's **create a Deep Lake Dataset** in the `./running_walking_deeplake` folder by running:

```python
import deeplake
from PIL import Image, ImageDraw
import numpy as np
import os

ds = deeplake.empty('./running_walking_deeplake') # Create the dataset locally
```

Next, let's inspect the folder structure for the source dataset `./running_walking` to find the class names and the files that need to be uploaded to the Deep Lake dataset.

```python
# Find the class_names and list of files that need to be uploaded
dataset_folder = './running_walking'

class_names = os.listdir(dataset_folder)

fn_vids = []
for dirpath, dirnames, filenames in os.walk(dataset_folder):
    for filename in filenames:
        fn_vids.append(os.path.join(dirpath, filename))
```

Finally, let's create the tensors and iterate through all the images in the dataset in order to upload the data in Deep Lake.

{% hint style="warning" %}
They key difference between `video` and `image` `htypes` is that Deep Lake does not explicitly perform compression for videos. The `sample_compression` input in the `create_tensor` function is used to verify that the compression of the input video file to `deeplake.read()`matches the `sample_compression` parameter. If there is a match, the video is uploaded in compressed format. Otherwise, an error is thrown.&#x20;

Images have a slightly different behavior, because the input image files are stored and re-compressed (if necessary) to the `sample_compression` format.
{% endhint %}

```python
with ds:
    ds.create_tensor('videos', htype='video', sample_compression = 'mp4')
    ds.create_tensor('labels', htype='class_label', class_names = class_names)

    for fn_vid in fn_vids:
        label_text = os.path.basename(os.path.dirname(fn_vid))
        label_num = class_names.index(label_text)

        # Append data to tensors
        ds.videos.append(deeplake.read(fn_vid))
        ds.labels.append(np.uint32(label_num))
```

{% hint style="warning" %}
In order for Activeloop Platform to correctly visualize the labels, `class_names` must be a list of strings, where the numerical labels correspond to the index of the label in the list.
{% endhint %}

### Inspect the Deep Lake Dataset&#x20;

Let's check out the first frame in the second sample from this dataset.&#x20;

```python
video_ind = 1
frame_ind = 0

# Individual frames are loaded lazily
img = Image.fromarray(ds.videos[ind][frame_ind].numpy())
```

```python
# Load the numberic label and read the class name from ds.labels.info.class_names
ds.labels.info.class_names[ds.labels[ind].numpy()[frame_ind]]
```

```python
img
```

![You've successfully created a video dataset in Activeloop Deep Lake.](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/HbQtKYGTMV3mbv3TX1G7/creating-video-datasets-activeloop-hub.webp)

Congrats! You just created a video classification dataset! 🎉


# Training Models

Workflows for training models using Deep Lake datasets

## How to Train Deep Learning Models Using Deep Lake

Deep Lake provides [dataloaders](https://docs-v3.activeloop.ai/examples/dl/dataloaders) that can be used as a drop-in replacements in existing training scripts. The benefits of Deep Lake dataloaders is their data streaming speed and compatibility with [Deep Lakes query engine](https://docs-v3.activeloop.ai/examples/tql), which enables users to rapidly filter their data and connect it to their GPUs.

Below is a series of tutorials for training models using Deep Lake.

{% content-ref url="training-models/training-classification-pytorch" %}
[training-classification-pytorch](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-classification-pytorch)
{% endcontent-ref %}

{% content-ref url="training-models/training-od-and-seg-pytorch" %}
[training-od-and-seg-pytorch](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-od-and-seg-pytorch)
{% endcontent-ref %}

{% content-ref url="training-models/training-lightning" %}
[training-lightning](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-lightning)
{% endcontent-ref %}

{% content-ref url="training-models/splitting-datasets-training" %}
[splitting-datasets-training](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/splitting-datasets-training)
{% endcontent-ref %}

{% content-ref url="training-models/training-sagemaker" %}
[training-sagemaker](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-sagemaker)
{% endcontent-ref %}

{% content-ref url="training-models/training-mmdet" %}
[training-mmdet](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-mmdet)
{% endcontent-ref %}

{% content-ref url="../playbooks/training-reproducibility-wandb" %}
[training-reproducibility-wandb](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-reproducibility-wandb)
{% endcontent-ref %}

{% content-ref url="../playbooks/training-with-lineage" %}
[training-with-lineage](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-with-lineage)
{% endcontent-ref %}


# Splitting Datasets for Training

How to Split Datasets for Training in Deep Lake

## **How to Split Datasets for Training in Deep Lake**

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1WWX5ZUoUq6AYHYSHxFUIXu8bz5zIeUZN?usp=sharing)

Deep Lake offers two approaches for splitting dataset for training and validation:

* Fully random splitting by row number (index)
* Pseudo-random splitting using Deep Lake's internal method that is optimized for fast streaming

### Setting up the Environment

```python
import deeplake
from PIL import Image
import numpy as np
import os, time
import random
import torch
from torchvision import transforms
import getpass
```

First, let's set up our environment and copy the [Fashion MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) into your organization. This dataset is an image classification dataset that categorizes images by clothing type (trouser, shirt, etc.). Copying the dataset into your organization enables you to make edits.

```python
os.environ["ACTIVELOOP_TOKEN"] = getpass.getpass()
```

```python
org_id = <your_org_id> # You already have an org_id that shares your username
```

```python
ds = deeplake.deepcopy("hub://activeloop/fashion-mnist-train", f"hub://{org_id}/fashion-mnist-train-2", overwrite = True) # The second parameter can be a local path
```

If you run this tutorial again, you may load the dataset instead of copying it.

```python
# ds = deeplake.load(f'hub://{os.environ['ORG_ID']}/fashion-mnist-train')
```

***

*keyboard\_arrow\_down*

### Fully random splitting by row number (index)

Lets randomly split the dataset based on arbitrary row numbers:

```python
len_ds = len(ds)

train_frac = 0.8

x = list(range(len_ds))
random.shuffle(x)
x_lim = round(train_frac*len(ds))
train_indices, val_indices = x[:x_lim], x[x_lim:]

print(f"Length of train_indices is {len(train_indices)}")
print(f"Length of val_indices is {len(val_indices)}")
```

Deep Lake refer to subsets of a dataset as `views`:

```python
train_view = ds[train_indices]
val_view = ds[val_indices]
```

#### Saving the Views (Optional)

In order to achieve reproducibility, you may save the views and use them in the future. Each saved view is assigned a `id` for reference. Saved views are pointers to data, and they do not duplicate data in storage.

```python
train_view.save_view()
```

```python
val_view.save_view()
```

```python
views_list = ds.get_views()print(views_list)
```

We can also load a view using:

```python
train_view = ds.load_view(views_list[0].id)
val_view = ds.load_view(views_list[1].id)

print(f"Length of train_view is {len(train_view)}")
print(f"Length of val_view is {len(val_view)}")
```

When loading or saving a view, we can specify the flag `optimize = True`, which [rechunks](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.activeloop.ai%2Ftechnical-details%2Fdata-layout) the data for optimal streaming performance. Note that this is a computationally intensive and it will duplicate the data from the view at the storage location.

```python
train_view = ds.load_view(views_list[0].id, optimize = True, num_workers = 2)
val_view = ds.load_view(views_list[1].id, optimize = True, num_workers = 2)

print(f"Length of train_view is {len(train_view)}")
print(f"Length of val_view is {len(val_view)}")
```

### Pseudo-random Deep Lake splitting that is optimized for performance

If high performance is required without duplicating data, we recommend using Deep Lake's internal `random_split` method, which splits the dataset pseudo-randomly in order to maintain fast streaming.

```python
train_view, val_view = ds.random_split([0.8, 0.2])

print(f"Length of train_view is {len(train_view)}")
print(f"Length of val_view is {len(val_view)}")
```

### Training a Model Using Views

Views and datasets can be used interchangeably for training models. In this tutorial, we show how to create and iterate over dataloaders for the training and validation views, and a [full tutorial for training a classification model on Fashion MNIST is available here](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fdocs.activeloop.ai%2Fexample-code%2Ftutorials%2Fdeep-learning%2Ftraining-models%2Ftraining-an-image-classification-model-in-pytorch).

```python
tform = transforms.Compose([
    transforms.RandomRotation(20), # Image augmentation
    transforms.ToTensor(), # Must convert to pytorch tensor for subsequent operations to run
    transforms.Normalize([0.5], [0.5]),
])
```

```python
batch_size = 32

# Since torchvision transforms expect PIL images, we use the 'pil' decode_method for the 'images' tensor. This is much faster than running ToPILImage inside the transform
train_loader = train_view.pytorch(num_workers = 0, shuffle = True, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
val_loader = val_view.pytorch(num_workers = 0, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
```

```python
for train_batch in train_loader:
  ## Insert Train Code Here ##
  print(train_batch['images'].shape)
  break
```

<pre class="language-python"><code class="lang-python">for val_batch in val_loader:
<strong>  ## Insert Train Code Here ##
</strong>  print(val_batch['images'].shape)
  break
</code></pre>

Congrats! You successfully created dataloaders from Deep Lake views! 🎉


# Training an Image Classification Model in PyTorch

Training an image classification model is a great way to get started with model training using Deep Lake datasets.

## How to Train an Image Classification Model in PyTorch using Activeloop Deep Lake

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1tPFOgu5iuh7v3TAuWjLjVGNptwEryA3Z?usp=sharing)

Deep Lake enables users to manage their data more easily so they can train better ML models. This tutorial shows you how to train a simple image classification model while streaming data from a Deep Lake dataset stored in the cloud.

### Data Preprocessing

The first step is to select a dataset for training. This tutorial uses the [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset that has already been converted into Deep Lake format. It is a simple image classification dataset that categorizes images by clothing type (trouser, shirt, etc.)

```python
import deeplake
from PIL import Image
import numpy as np
import os, time
import torch
from torchvision import transforms, models

# Connect to the training and testing datasets
ds_train = deeplake.load('hub://activeloop/fashion-mnist-train')
ds_test = deeplake.load('hub://activeloop/fashion-mnist-test')
```

The next step is to define a transformation function that will process the data and convert it into a format that can be passed into a deep learning model. In this particular example, `torchvision.transforms` is used as a part of the transformation pipeline that performs operations such as normalization and image augmentation (rotation).

```python
tform = transforms.Compose([
    transforms.RandomRotation(20), # Image augmentation
    transforms.ToTensor(), # Must convert to pytorch tensor for subsequent operations to run
    transforms.Normalize([0.5], [0.5]),
])
```

You can now create a pytorch dataloader that connects the Deep Lake dataset to the PyTorch model using the provided method `ds.pytorch()`. This method automatically applies the transformation function, takes care of random shuffling (if desired), and converts Deep Lake data to PyTorch tensors. The `num_workers` parameter can be used to parallelize data preprocessing, which is critical for ensuring that preprocessing does not bottleneck the overall training workflow.

The `transform` input is a dictionary where the `key` is the tensor name and the `value` is the transformation function that should be applied to that tensor. If a specific tensor's data does not need to be returned, it should be omitted from the keys. If the transformation function is set as `None`, the input tensor is converted to a torch tensor without additional modification.

```python
# Since torchvision transforms expect PIL images, we use the 'pil' decode_method for the 'images' tensor. This is much faster than running ToPILImage inside the transform
train_loader = ds_train.pytorch(num_workers = 0, shuffle = True, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
test_loader = ds_test.pytorch(num_workers = 0, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
```

### Model Definition

This tutorial uses a pre-trained [ResNet18](https://pytorch.org/hub/pytorch_vision_resnet/) neural network from the `torchvision.models` module, converted to a single-channel network for grayscale images.

Training is run on a GPU if possible. Otherwise, run on a CPU.

```python
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(device)
```

```python
# Use a pre-trained ResNet18
model = models.resnet18(pretrained=True)

# Convert model to grayscale
model.conv1 = torch.nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

# Update the fully connected layer based on the number of classes in the dataset
model.fc = torch.nn.Linear(model.fc.in_features, len(ds_train.labels.info.class_names))

model.to(device)

# Specity the loss function and optimizer
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.1)
```

### Training the Model

Helper functions for training and testing the model are defined. Note that the output from Deep Lake's PyTorch dataloader is fed into the model just like data from ordinary PyTorch dataloaders.

```python
def train_one_epoch(model, optimizer, data_loader, device):

    model.train()

    # Zero the performance stats for each epoch
    running_loss = 0.0
    start_time = time.time()
    total = 0
    correct = 0
    
    for i, data in enumerate(data_loader):
        # get the inputs; data is a list of [inputs, labels]
        inputs = data['images']
        labels = torch.squeeze(data['labels'])

        inputs = inputs.to(device)
        labels = labels.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = model(inputs.float())
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        accuracy = 100 * correct / total
    
        # Print performance statistics
        running_loss += loss.item()
        if i % 10 == 0:    # print every 10 batches
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] loss: %.3f, speed: %.2f, accuracy: %.2f %%' %
                  (i, running_loss, speed, accuracy))

            running_loss = 0.0
            total = 0
            correct = 0

    
def test_model(model, data_loader):

    model.eval()

    start_time = time.time()
    total = 0
    correct = 0
    with torch.no_grad():
        for i, data in enumerate(data_loader):
            # get the inputs; data is a list of [inputs, labels]
            inputs = data['images']
            labels = torch.squeeze(data['labels'])

            inputs = inputs.to(device)
            labels = labels.to(device)

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = model(inputs.float())

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        accuracy = 100 * correct / total
            
        print('Finished Testing')
        print('Testing accuracy: %.1f %%' %(accuracy))
```

**The model and data are ready for training🚀!**

```python
num_epochs = 3
for epoch in range(num_epochs):  # loop over the dataset multiple times
    print("------------------ Training Epoch {} ------------------".format(epoch+1))
    train_one_epoch(model, optimizer, train_loader, device)

    test_model(model, test_loader)

print('Finished Training')
```

Congrats! You successfully trained an image classification model while streaming data directly from the cloud! 🎉


# Training Models Using MMDetection

How to Train Deep Learning models using Deep Lake's integration with MMDetection

## How to Train Deep Learning models using Deep Lake and MMDetection

{% hint style="info" %}
This tutorial assumes the reader has experience training models using MMDET and has installed it successfully.
{% endhint %}

{% hint style="danger" %}
Deep Lake works with`mmcv-full<=1.7.1` and `mmdet<=2.28.2`
{% endhint %}

Deep Lake offers an integration with [MMDetection](https://github.com/open-mmlab/mmdetection), a popular open-source object detection toolbox based on PyTorch. The integration enables users to train models while streaming Deep Lake datasets using the transformation, training, and evaluation tools built by MMDet.

### Integration Interface

Training using MMDET is typically executed using wrapper scripts like the one provided [here in their repo](https://github.com/open-mmlab/mmdetection/blob/master/tools/train.py). In the example below, we write a similar wrapper script for training using a Deep Lake dataset.

The integrations with MMDET occurs in the `deeplake.integrations.mmdet` module. At a high-level, Deep Lake is responsible for the pytorch dataloader that streams data to the training framework, while MMDET is used for the training, transformation, and evaluation logic.

In the example script below, the user should apply the `build_detector` and `train_detector` provided by Deep Lake. The `build_detector` is mostly boilerplate. and the Deep Lake-related features primarily exist in `train_detector`.

```python
import os
from mmcv import Config
import mmcv
from deeplake.integrations import mmdet as mmdet_deeplake
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Deep Lake Training Using MMDET")

    parser.add_argument(
        "--cfg_file",
        type=str,
        required=True,
        help="Path for loading the config file",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        default=True,
        help="Whether to run dataset validation",
    )
    parser.add_argument(
        "--distributed",
        action="store_true",
        default=False,
        help="Whether to run distributed training",
    )
    parser.add_argument(
        "--num_classes",
        type=int,
        default=None,
        help="Number of classes in the model",
    )

    args = parser.parse_args()

    return args

if __name__ == "__main__":

    args = parse_args()
    
    # Read the config file
    cfg = Config.fromfile(args.cfg_file)

    cfg.model.bbox_head.num_classes = args.num_classes

    # Build the detector
    model = mmdet_deeplake.build_detector(cfg.model)

    # Create work_dir
    mmcv.mkdir_or_exist(os.path.abspath(cfg.work_dir))

    # Run the training
    mmdet_deeplake.train_detector(model, cfg, distributed=args.distributed, validate=args.validate)
```

### Inputs to train\_detector &#x20;

Inputs to the Deep Lake `train_detector` are a modified MMDET config file, optional dataset objects (see below), and flags for specifying whether to perform distributed training and validation.&#x20;

#### Modifications to the cfg file

The Deep Lake train\_detector takes in a standard MMDET config file, but it also expect the inputs highlighted in the  `----Deep Lake Inputs----` section in the config file below:

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/c2zsxLGKnWmjejEW2dG2/yolo_coco_docs_cfg.py>" %}

```python
#--------------------------------------DEEPLAKE INPUTS------------------------------------------------------------#

data = dict(
    # samples_per_gpu=4, # Is used instead of batch_size if deeplake_dataloader is not specified below
    # workers_per_gpu=8, # Is used instead of num_workers if deeplake_dataloader is not specified below
    train=dict(
        pipeline=train_pipeline,

        # Credentials for authentication. See documendataion for deeplake.load() for details
        deeplake_path="hub://activeloop/coco-train",
        deeplake_credentials={
            #"token": <YOUR_TOKEN>, In case you don't want to use the env variable
            "creds": None,
        },
        #OPTIONAL - Checkout teh specified commit_id before training
        deeplake_commit_id="",
        #OPTIONAL - Loads a dataset view for training based on view_id
        deeplake_view_id="",

        # OPTIONAL - {"mmdet_key": "deep_lake_tensor",...} - Maps Deep Lake tensors to MMDET dictionary keys. 
        # If not specified, Deep Lake will auto-infer the mapping, but it might make mistakes if datasets have many tensors
        deeplake_tensors = {"img": "images", "gt_bboxes": "boxes", "gt_labels": "categories"},
        
        # OPTIONAL - Parameters to use for the Deep Lake dataloader. If unspecified, the integration uses
        # the parameters in other parts of the cfg file such as samples_per_gpu, and others.
        deeplake_dataloader = {"shuffle": True, "batch_size": 4, 'num_workers': 8}
    ),

    # Parameters as the same as for train
    val=dict(
        pipeline=test_pipeline,
        deeplake_path="hub://activeloop/coco-val",
        deeplake_credentials={
            #"token": <YOUR_TOKEN>, In case you don't want to use the env variable
            "creds": None,
        },
        deeplake_tensors = {"img": "images", "gt_bboxes": "boxes", "gt_labels": "categories"},
        deeplake_dataloader = {"shuffle": False, "batch_size": 1, 'num_workers': 8}
    ),
)

# Which dataloader to use
deeplake_dataloader_type = "c++"  # "c++" is available to enterprise users. Otherwise use "python"

# Which metrics to use for evaulation. In MMDET (without Deeplake), this is inferred from the dataset type.
# In the Deep Lake integration, since the format is standardized, a variety of metrics can be used for a given dataset.
deeplake_metrics_format = "COCO"

#----------------------------------END DEEPLAKE INPUTS------------------------------------------------------------#
```

#### Passing Deep Lake dataset objects to the `train_detector` (Optional)

The Deep Lake dataset object or dataset view can be passed to the `train_detector` directly, thus overwriting any dataset information in the config file. Below are the respective modifications that should be made to the training script above:

```python
ds_train = deeplake.load(dataset_path, token, ...)
ds_train.checkout(commit_id)
ds_train_view = ds_train.query("Add query string")

mmdet_deeplake.train_detector(model, cfg, ds_train = ds_train_view, ds_val = ..., distributed = args.distributed, validate = args.validate)
```

Congrats! You're now able to train models using MMDET while streaming Deep Lake Datasets! 🎉

### What is MMDetection?

MMDetection is a powerful open-source object detection toolbox that provides a flexible and extensible platform for computer vision tasks. Developed by the Multimedia Laboratory (MMLab) as part of the OpenMMLab project, MMDetection is built upon the [PyTorch](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-lightning) framework and offers a composable and modular API design. This unique feature enables developers to easily construct custom [object detection](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-od-and-seg-pytorch) and segmentation pipelines. This article will delve deeper into how to use MMDetection with Activeloop Deep Lake.&#x20;

### MMDetection Features

MMDetection's Modular and Composable API Design MMDetection's API design follows a modular approach, enabling seamless integration with frameworks like Deep Lake and easy component customization. This flexibility allows users to adapt the object detection pipeline to meet specific project requirements.

#### Custom Object Detection and Segmentation Pipelines

&#x20;MMDetection streamlines custom pipeline creation, allowing users to construct tailored models by selecting and combining different backbones, necks, and heads for more accurate and efficient computer vision pipelines.

#### Comprehensive Training & Inference Support

&#x20;MMDetection's toolbox supports various data augmentation techniques, distributed training, mixed-precision training, and detailed evaluation metrics to help users assess their model's performance and identify areas for improvement.

#### Extensive Model Zoo & Configurations

MMDetection offers a vast model zoo with numerous pre-trained models and configuration files for diverse computer vision tasks, such as object detection, instance segmentation, and panoptic segmentation.

### Primary Components of MMDetection

#### MMDetection Backbone

Backbones pre-trained convolutional neural networks (CNNs) to extract feature maps. Popular backbones include ResNet, VGG, and MobileNet.&#x20;

#### MMDetection Head

These components are meant for specific tasks, e.g. to generate the final predictions, such as bounding boxes, class labels, or masks. Examples include RPN (Region Proposal Network), FCOS (Fully Convolutional One-Stage Object Detector), and Mask Head. Neck: Components, like FPN (Feature Pyramid Network) and PAN (Path Aggregation Network), refine and consolidate features extracted by backbones, connecting them to the head.&#x20;

#### MMDetection ROI Extractor

Region of Interest Extractor is a critical MMDetection component extracting RoI features from the feature maps generated by the backbone and neck components, improving the accuracy of final predictions (e.g., bounding boxes and class labels). One of the most popular methods for RoI feature extraction is RoI Align (a technique that addresses the issue of misalignment between RoI features and the input image due to quantization in RoI Pooling).

#### Loss&#x20;

The loss component calculates loss values during training, estimating the difference between model predictions and ground truth labels. Users can choose suitable loss functions (e.g., Focal Loss, GHMLoss, L1 Loss) for specific use cases to [evaluate and improve the model's performance](https://docs-v3.activeloop.ai/examples/dl/playbooks/evaluating-model-performance).


# Training Models Using PyTorch Lightning

How to Train models using Deep Lake and PyTorch Lightning

## How to Train models using Deep Lake and PyTorch Lightning

**This tutorial is also available as a** [**Colab Notebook**](https://colab.research.google.com/drive/1oHUNH4HpZ5zvqUe2Njt4l1J_JV7FPLtW?usp=sharing)**.**

Deep Lake's integration with PyTorch can also be used to train models using an integration with [PyTorch Lightning](https://www.pytorchlightning.ai/), a popular open-source high-level interface for PyTorch.&#x20;

### Overview

**At a high-level, Deep Lake is connected to PyTorch lightning by passing the Deep Lake's PyTorch dataloader to any PyTorch Lightning API that expects a dataloader parameter, such as `trainer.fit(..., train_dataloaders = deeplake_dataloader)`. The only caveats are:**

{% hint style="danger" %}

* Deep Lake handles distributed training via it's `distributed` parameter in the [.pytorch() method](https://docs.deeplake.ai/en/latest/Dataloader.html#deeplake.enterprise.DeepLakeDataLoader.pytorch). Therefore, the PyTorch Lightning Trainer class should be initialized with `replace_sampler_ddp = False.`
  {% endhint %}

### Example Code

This tutorial uses PyTorch Lightning to execute the [identical training workflow that is shown here in PyTorch](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models/training-classification-pytorch).

### Data Preprocessing

The first step is to load the dataset for training. This tutorial uses the [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset that has already been converted into Deep Leake format. It is a simple image classification dataset that categorizes images by clothing type (trouser, shirt, etc.)

```python
import deeplake
from PIL import Image
import torch
from torchvision import transforms, models
import pytorch_lightning as pl

# Connect to the training and testing datasets
ds_train = deeplake.load('hub://activeloop/fashion-mnist-train')
ds_val = deeplake.load('hub://activeloop/fashion-mnist-test')
```

The next step is to define a transformation function that will process the data and convert it into a format that can be passed into a deep learning model. In this particular example, `torchvision.transforms` is used as a part of the transformation pipeline that performs operations such as normalization and image augmentation (rotation).

```python
tform = transforms.Compose([
    transforms.RandomRotation(20), # Image augmentation
    transforms.ToTensor(), # Must convert to pytorch tensor for subsequent operations to run
    transforms.Normalize([0.5], [0.5]),
])
```

You can now create a PyTorch dataloader that connects the Deep Lake dataset to the PyTorch model using the provided method `ds.pytorch()`. This method automatically applies the transformation function and takes care of random shuffling (if desired). The `num_workers` parameter can be used to parallelize data preprocessing, which is critical for ensuring that preprocessing does not bottleneck the overall training workflow.

The `transform` input is a dictionary where the `key` is the tensor name and the `value` is the transformation function that should be applied to that tensor. If a specific tensor's data does not need to be returned, it should be omitted from the keys. If the transformation function is set as `None`, the input tensor is converted to a torch tensor without additional modification.

```python
batch_size = 32

# Since torchvision transforms expect PIL images, we use the 'pil' decode_method for the 'images' tensor. This is much faster than running ToPILImage inside the transform
train_loader = ds_train.pytorch(num_workers = 0, shuffle = True, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
val_loader = ds_val.pytorch(num_workers = 0, transform = {'images': tform, 'labels': None}, batch_size = batch_size, decode_method = {'images': 'pil'})
```

### Model and LightningModule Definition

This tutorial uses a pre-trained [ResNet18](https://pytorch.org/hub/pytorch_vision_resnet/) neural network from the torchvision.models module, converted to a single-channel network for grayscale images. The [LightningModule](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html) organizes the training code.

```python
# Use a pre-trained ResNet18
def get_model(num_classes):
    model = models.resnet18(pretrained=True)

    # Convert model to grayscale
    model.conv1 = torch.nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

    # Update the fully connected layer based on the number of classes in the dataset
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    return model
```

```python
class FashionMnistModule(pl.LightningModule):
    def __init__(self, num_classes):
        """
        Inputs:
            num_classes: Number of classes in the dataset and model
        """
        super().__init__()

        # Create the model
        self.model = get_model(num_classes)

        # Create loss module
        self.loss_module = torch.nn.CrossEntropyLoss()

    def forward(self, imgs):
        return self.model(imgs)

    def configure_optimizers(self):
        return torch.optim.SGD(self.model.parameters(), lr=0.001, momentum=0.1)   

    def training_step(self, batch, batch_idx):
        images = batch['images']
        labels = torch.squeeze(batch['labels'])

        preds = self.model(images)
        loss = self.loss_module(preds, labels)
        
        acc = (preds.argmax(dim=-1) == labels).float().mean()

        self.log("train_acc", acc, on_step=True, on_epoch=True)
        self.log("train_loss", loss)
        
        return loss 

    def validation_step(self, batch, batch_idx):

        images = batch['images']
        labels = torch.squeeze(batch['labels'])
        preds = self.model(images).argmax(dim=-1)
        acc = (labels == preds).float().mean()

        # Log the valdation accuracy to the progress bar at the end of each epoch
        self.log("val_acc", acc, on_epoch=True, prog_bar=True)
```

### Training the Model

PyTorchLightning takes care of the training loop, so the remaining steps are to initialize the [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html) and call the `.fit()` method using the training and validation dataloaders.

```python
trainer = pl.Trainer(max_epochs = 3)
trainer.fit(model=FashionMnistModule(len(ds_train.labels.info.class_names)), train_dataloaders = train_loader, val_dataloaders = val_loader)
```

Congrats! You successfully trained an image classification model using PyTorch Lightning while streaming data directly from the cloud! 🎉


# Training on AWS SageMaker

How to Train models on AWS SageMaker using Deep Lake datasets

## How to Train an PyTorch Image Classification Model on AWS SageMaker Using Deep Lake Datasets

[AWS SageMaker](https://aws.amazon.com/sagemaker/) provides scalable infrastructure for developing, training, and deploying deep learning models. In this tutorial, we demonstrate how to run SageMaker training jobs for training a PyTorch image classification model using a Deep Lake dataset. This tutorial will focus on the SageMaker integration, and less so on the details of the training (see other [training tutorials](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models) for details)

### Dataset

In this tutorial we will use the [Stanford Cars Dataset](https://app.activeloop.ai/activeloop/stanford-cars-train), which classifies the make+model+year of various vehicles. Though the dataset contains bounding boxes, we ignore those and only use the data for classification purposes.

### Running the Sagemaker Job

We run the SageMaker job using the docker container below that can be found among [these deep learning containers provided by AWS](https://github.com/aws/deep-learning-containers/blob/master/available_images.md).&#x20;

`"763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.12.1-gpu-py38-cu113-ubuntu20.04-sagemaker"`

The SageMaker job is initiated using the script below. By also running this script in a SageMaker notebook, the permissions and role access are automatically taken care of within the AWS environment.

```python
import sagemaker

sess = sagemaker.Session()
role = sagemaker.get_execution_role()
```

The training script (`entry_point`) and the directory (`source_dir`) containing the training script and `requirements.txt` file is passed to the [`Estimator`](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator). The `argparse` parameters for the training script are passed via the `hyperparameters` dictinary in the `Estimator.` Note that we also pass the Deep Lake paths to the training and validation datasets via this input.

```python
 estimator = sagemaker.estimator.Estimator(
                source_dir = "./train_code",  # Directory of the training script
                entry_point = "train_cars.py", # File for the training script    
                image_uri = image_name,
                role = role,
                instance_count = 1,
                instance_type = instance_type,
                output_path = output_path,
                sagemaker_session = sess,
                max_run = 2*60*60,
                hyperparameters = {"train-dataset": "hub://activeloop/stanford-cars-train",
                                   "val-dataset": "hub://activeloop/stanford-cars-test",
                                   "batch-size": 64, "num-epochs": 40,
                                })
```

The training job is triggered using the command below. Typically, the `.fit()` function accepts as inputs the S3 bucket containing the training data, which is then downloaded onto the local storage of the SageMaker job. Since we've passed the Deep Lake dataset paths via the `hyperparameters`, and since Deep Lake does not require data to be downloaded prior to training, we skip these inputs. &#x20;

```
estimator.fit()
```

SageMaker offers a variety of method for advanced data logging. In this example, we can monitor the training performance in real-time in the training notebook where the jobs are triggered, or in the [CloudWatch](https://aws.amazon.com/cloudwatch/) logs for each job. We observe that the validation accuracy after 40 epochs is 75%.

### Training Script

The contents of the `train_code` folder, as well as the `train_cars.py` file, are shown below. The training script follow the same workflow as other PyTorch training workflows using Deep Lake. As mentioned above, the inputs to the `argparse` function are those from the `hyperparameters` inputs in the `estimator`.&#x20;

```python
import deeplake
import argparse
import logging
import os
import sys
import time 
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data
import torch.utils.data.distributed
from torchvision import transforms, models

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


#----------- Define transformations and their parameters -----------#

WIDTH = 320
HEIGHT = 320

tform_train = transforms.Compose([
#     transforms.ToPILImage(), # Not needed because decode_method is set to PIL in the dataloader
    transforms.RandomResizedCrop((WIDTH, HEIGHT), scale=(0.75, 1.0), ratio=(0.75, 1.25)),
    transforms.RandomRotation(25),
    transforms.ColorJitter(brightness=(0.8,1.2), contrast=(0.8,1.2), saturation=(0.8,1.2), hue=(-0.1,0.1)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x.repeat(int(3 / x.shape[0]), 1, 1)), # Adjust tensor if the image is grayscale
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
    
tform_val = transforms.Compose([
#     transforms.ToPILImage(), # Not needed because decode_method is set to PIL in the dataloader
    transforms.Resize((WIDTH, HEIGHT)),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x.repeat(int(3 / x.shape[0]), 1, 1)), # Adjust tensor if the image is grayscale
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])    




#----------- Define helper functions -----------#

# Helper function for loading the model
def get_model_classification(num_classes):
    # Load a pre-trained classification model
    model = models.resnet34(pretrained=True)
    
    # Adjust the fully connected layer based on the number of classes in the dataset
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    return model


# Helper function for training for 1 epoch
def train_one_epoch(model, optimizer, criterion, data_loader, device, log_interval):
        
    # Set the model to train mode    
    model.train()
    
    # Zero the performance stats for each epoch
    running_loss = 0.0
    start_time = time.time()
    total = 0
    correct = 0
    
    for i, data in enumerate(data_loader):
        
        # Parse the inputs
        inputs = data['images']
        labels = data['car_models'][:, 0] # Get rid of the extra axis

        inputs = inputs.to(device)
        labels = labels.to(device)

        # Zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = model(inputs.float())
        loss = criterion(outputs, labels.long())
        loss.backward()
        optimizer.step()
        
        # Update the accuracy for the epoch
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        accuracy = 100 * correct / total

        # Print statistics
        running_loss += loss.item()
        batch_time = time.time()
        
        if i % log_interval == 0:    # print every 100 mini-batches
            speed_cumulative = (i+1)/(batch_time-start_time)
            
            logger.debug('[%5d] running loss: %.3f, epoch accuracy: %.3f, cumulative speed: %.2f ' %
                    (i, running_loss, accuracy, speed_cumulative))

            running_loss = 0.0
      
    
# Helper function for testing the model      
def test_model(model, data_loader, device):
    
    # Set the model to eval mode
    model.eval()
    
    total = 0
    correct = 0
    
    with torch.no_grad():
        for i, data in enumerate(data_loader):
            
            # Parse the inputs
            inputs = data['images']
            labels = data['car_models'][:, 0]

            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs.float())

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
        accuracy = 100 * correct / total
    
    return accuracy
        
    
# Helper function for saving the model    
def save_model(model, model_dir):
    logger.info("Saving the model")
    path = os.path.join(model_dir, "model.pth")
    torch.save(model.state_dict(), path)

    
def train(args):
        
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    
    # Load dataset and create dataloaders.
    ds_train = deeplake.load(args.train_dataset, read_only = True, token = args.token, creds = args.creds)
    ds_val = deeplake.load(args.val_dataset, read_only = True, token = args.token, creds = args.creds)
    
    train_loader = ds_train.dataloader()\
                            .batch(args.batch_size)\
                            .shuffle(args.shuffle)\
                            .transform(transform = {'images': tform_train, 'car_models': None})\
                            .pytorch(num_workers = args.num_workers, decode_method = {'images': 'pil'})

    val_loader = ds_val.dataloader()\
                        .batch(args.batch_size)\
                        .transform(transform = {'images': tform_val, 'car_models': None})\
                        .pytorch(num_workers = args.num_workers, decode_method = {'images': 'pil'})
    
    # Load the model
    model = get_model_classification(len(ds_train.car_models.info.class_names))
    model = model.to(device)

    # Define the optimizer, loss, and learning rate scheduler
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    criterion = nn.CrossEntropyLoss()
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.2)
        
    # Run the training
    for epoch in range(args.num_epochs):
        logger.debug("Training Epoch: {}".format(epoch))
        
        train_one_epoch(model, optimizer, criterion, train_loader, device, args.log_interval)
        lr_scheduler.step()

        accuracy = test_model(model, val_loader, device)
        logger.debug("Validation Accuracy: {}".format(accuracy))
                
    logger.debug('Finished Training')
    
    save_model(model, args.model_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--train-dataset",
        type=str,
        required=True,
        help="path to deeplake training dataset",
    )
    parser.add_argument(
        "--val-dataset",
        type=str,
        required=True,
        help="path to deeplake validation dataset",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="input batch size for training (default: 64)",
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=8,
        help="number of workers for the dataloaders (default: 8)",
    )
    parser.add_argument(
        "--shuffle",
        type=bool,
        default=True,
        help="shuffling for the training dataloader (default: True)",
    )    
    parser.add_argument(
        "--num-epochs",
        type=int,
        default=10,
        help="number of epochs to train (default: 10)",
    )
    parser.add_argument(
        "--lr", 
        type=float, 
        default=0.001, 
        help="learning rate (default: 0.001)"
    )
    parser.add_argument(
        "--log-interval",
        type=int,
        default=10,
        metavar="N",
        help="how many batches to wait before logging training status (default: 10)",
    )
    parser.add_argument(
        "--token", 
        type=str, 
        default=None, 
        help="token for accessing the Deep Lake dataset (default: None)"
    )
    parser.add_argument(
        "--creds", 
        type=dict, 
        default=None, 
        help="creds dictionary for accessing the Deep Lake dataset (default: None)"
    )
    parser.add_argument(
        '--model_dir', 
        type=str, 
        default=os.environ['SM_MODEL_DIR'])
        
    train(parser.parse_args())
```

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/4JS0Cdj0Y2EUQSEGkP3l/train_code.zip>" %}

Congrats! You're now able to train models using AWS SageMaker Jobs while streaming Deep Lake Datasets! 🎉


# Training an Object Detection and Segmentation Model in PyTorch

Training an object detection and segmentation model is a great way to learn about complex data preprocessing for training models.

## How to train an object detection and instance segmentation model in PyTorch using Deep Lake

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1w9Y5TsUwfT_ccK1fpa_GtoJjamOSte_Z?usp=sharing)

The primary objective for Deep Lake is to enable users to manage their data more easily so they can train better ML models. This tutorial shows you how to train an object detection and instance segmentation model while streaming data from a Deep Lake dataset stored in the cloud.

Since these models are often complex, this tutorial will focus on data-preprocessing for connecting the data to the model. The user should take additional steps to scale up the code for logging, collecting additional metrics, model testing, and running on GPUs.

This tutorial is inspired by this [PyTorch tutorial](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html) on training object detection and segmentation models.

### Data Preprocessing

The first step is to select a dataset for training. This tutorial uses the [COCO](https://cocodataset.org/#home) dataset that has already been converted into Deep Lake format. It is a multi-modal image dataset that contains bounding boxes, segmentation masks, keypoints, and other data.

```python
import deeplake
import numpy as np
import math
import sys
import time
import torchvision
import albumentations as A
from albumentations.pytorch import ToTensorV2
import torch
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor
import torchvision.models.detection.mask_rcnn

# Connect to the training dataset
ds_train = deeplake.load('hub://activeloop/coco-train')
```

Note that the dataset can be visualized at the link printed by the `deeplake.load` command above.

We extract the number of classes for use later:

```python
num_classes = len(ds_train.categories.info.class_names)
```

For complex dataset like this one, it's critical to carefully define the pre-processing function that returns the torch tensors that are use for training. Here we use an [Albumentations](https://github.com/albumentations-team/albumentations) augmentation pipeline combined with additional pre-processing steps that are necessary for this particular model.

{% hint style="danger" %}
**Note:** This tutorial assumes that the number of masks and bounding boxes for each image is equal
{% endhint %}

```python
# Augmentation pipeline using Albumentations
tform_train = A.Compose([
    A.RandomSizedBBoxSafeCrop(width=128, height=128, erosion_rate = 0.2),
    A.HorizontalFlip(p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2(), # transpose_mask = True
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=25, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.


# Transformation function for pre-processing the Deep Lake sample before sending it to the model
def transform(sample_in):

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'])

    # Convert any grayscale images to RGB
    images = sample_in['images']
    if images.shape[2] == 1:
        images = np.repeat(images, int(3/images.shape[2]), axis = 2)

    # Pass all data to the Albumentations transformation
    # Mask must be converted to a list
    masks = sample_in['masks']
    mask_shape = masks.shape

    # This if-else statement was not necessary in Albumentations <1.3.x, because the empty mask scenario was handled gracefully inside of Albumentations. In Albumebtations >1.3.x, empty list of masks fails
    if mask_shape[2]>0:
        transformed = tform_train(image = images,
                                  masks = [masks[:,:,i].astype(np.uint8) for i in range(mask_shape[2])],
                                  bboxes = boxes,
                                  bbox_ids = np.arange(boxes.shape[0]),
                                  class_labels = sample_in['categories'],
                                  )
    else:
        transformed = tform_train(image = images,
                                  bboxes = boxes,
                                  bbox_ids = np.arange(boxes.shape[0]),
                                  class_labels = sample_in['categories'],
                                  )  
        


    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)

    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))
        

    # Filter out the masks that were dropped by filtering of bounding box area and visibility
    masks_torch = torch.zeros((len(transformed['bbox_ids']), transformed['image'].shape[1], transformed['image'].shape[2]), dtype = torch.int64)
    if len(transformed['bbox_ids'])>0:
        masks_torch = torch.tensor(np.stack([transformed['masks'][i] for i in transformed['bbox_ids']], axis = 0), dtype = torch.uint8)
    


    # Put annotations in a separate object
    target = {'masks': masks_torch, 'labels': labels_torch, 'boxes': boxes_torch}

    return transformed['image'], target


# Conversion script for bounding boxes from coco to Pascal VOC format
def coco_2_pascal(boxes):
    # Convert bounding boxes to Pascal VOC format and clip bounding boxes to make sure they have non-negative width and height

    return np.stack((boxes[:,0], boxes[:,1], boxes[:,0]+np.clip(boxes[:,2], 1, None), boxes[:,1]+np.clip(boxes[:,3], 1, None)), axis = 1)


def collate_fn(batch):
    return tuple(zip(*batch))
```

You can now create a PyTorch dataloader that connects the Deep Lake dataset to the PyTorch model using the provided method `ds.pytorch()`. This method automatically applies the transformation function and takes care of random shuffling (if desired). The `num_workers` parameter can be used to parallelize data preprocessing, which is critical for ensuring that preprocessing does not bottleneck the overall training workflow.

Since the dataset contains many tensors that are not used for training, a list of tensors for loading is specified in order to avoid streaming of unused data.

```python
batch_size = 8

train_loader = ds_train.pytorch(num_workers = 2, shuffle = False, 
    tensors = ['images', 'masks', 'categories', 'boxes'], # Specify the tensors that are needed, so we don't load unused data
    transform = transform, 
    batch_size = batch_size,
    collate_fn = collate_fn)
```

### Model Definition

This tutorial uses a pre-trained torchvision neural network from the `torchvision.models` module.

Training is performed on a GPU if possible. Otherwise, it's on a CPU.

```python
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(device)
```

```python
# Helper function for loading the model
def get_model_instance_segmentation(num_classes):
    # Load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)

    # Get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    # Get the number of input features for the mask classifier
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256
    # Replace the mask predictor with a new one
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask,
                                                       hidden_layer,
                                                       num_classes)

    return model
```

Let's initialize the model and optimizer.

```python
model = get_model_instance_segmentation(num_classes)

model.to(device)

# Specity the optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                            momentum=0.9, weight_decay=0.0005)
```

### Training the Model

Helper functions for training and testing the model are defined. Note that the output from Deep Lake's PyTorch dataloader is fed into the model just like data from ordinary PyTorch dataloaders.

```python
# Helper function for training for 1 epoch
def train_one_epoch(model, optimizer, data_loader, device):
    model.train()

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        targets = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
        
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()

        # Print performance statistics
        batch_time = time.time()
        speed = (i+1)/(batch_time-start_time)
        print('[%5d] loss: %.3f, speed: %.2f' %
              (i, loss_value, speed))

        if not math.isfinite(loss_value):
            print(f"Loss is {loss_value}, stopping training")
            print(loss_dict)
            break

        optimizer.zero_grad()

        losses.backward()
        optimizer.step()
```

**The model and data are ready for training 🚀!**

```python
# Train the model for 1 epoch
num_epochs = 1
for epoch in range(num_epochs):  # loop over the dataset multiple times
    print("------------------ Training Epoch {} ------------------".format(epoch+1))
    train_one_epoch(model, optimizer, train_loader, device)
    
    # --- Insert Testing Code Here ---

    print('Finished Training')
```

Congrats! You successfully trained an object detection and instance segmentation model while streaming data directly from the cloud! 🎉


# Updating Datasets

Updating Deep Lake datasets

## How to make updates to Deep Lake datasets

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1PPW17r-JBb3otkFwB0FIs7Y97pOkyY_W?usp=sharing)

After creating a Deep Lake dataset, you may need to edit it by adding, deleting, and modifying the data. In this tutorial, we show best practices for updating datasets.

### Create a Representative Deep Lake Dataset&#x20;

First, let's download and unzip representative source data and create a Deep Lake dataset for this tutorial:

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/pvwp33pWGWlxr4sadBSc/damaged_cars_tutorial.zip>" %}

This dataset includes segmentation and object detection of vehicle damage, but for this tutorial, we will only upload the images and labels (damage location)

```python
import deeplake
import pandas as pd
import os
from PIL import Image

images_directory = '/damaged_cars_tutorial' # Path to the COCO images directory
annotation_file = '/damaged_cars_tutorial/COCO_mul_val_annos.json' # Path to the COCO annotations file
deeplake_path = '/damaged_cars_dataset' # Path to the Deep Lake dataset

ds = deeplake.ingest_coco(images_directory, annotation_file, deeplake_path, 
                          key_to_tensor_mapping={'category_id': 'labels'}, # Rename category_id to labels
                          ignore_keys=['area', 'image_id', 'id', 'segmentation', 'image_id', 'bbox', 'iscrowd'])
```

`ds.summary()` shows the dataset has two tensors with 11 samples:

```
 tensor      htype            shape          dtype  compression
 -------    -------          -------        -------  ------- 
 images      image     (11, 1024, 1024, 3)   uint8    jpeg   
 labels   class_label       (11, 2:7)       uint32    None  
```

We can explore the damage in the first sample using `ds.labels[0].data()`, which prints:

```
{'value': array([0, 1, 2], dtype=uint32),
 'text': ['rear_bumper', 'door', 'headlamp']}
```

### Add Data to a New Tensor

Suppose you have another data source with supplemental data about the color of the vehicles. Let's create a Pandas DataFrame with this data.

```python
color_data = {'filename': ['1.jpg', '9.jpg', '62.jpg', '24.jpg'],
              'color': ['gray', 'blue', 'green', 'gray']}
  
df_color = pd.DataFrame(color_data)
```

There are two approaches for adding this new data to the Deep Lake dataset:

#### 1. Iterate through the Deep Lake samples and append data

{% hint style="info" %}
This approach is recommended when most Deep Lake samples are being updated using the supplemental data (dense update).
{% endhint %}

First, we create a `color` tensor and iterate through the samples. For each sample, we lookup the  color from the `df_color` DataFrame and append it to the `color` tensor. If no color exists for a filename, it is appended as `None`. We use the filename as the key to perform the lookup, which is available in `ds.images[index].sample_info` dictionary.

```python
with ds:
    ds.create_tensor('color', htype = 'class_label')
    
    # After creating an empty tensor, the length of the dataset is 0
    # Therefore, we iterate over ds.max_view, which is the padded version of the dataset
    for i, sample in enumerate(ds.max_view):
        filename = os.path.basename(sample.images.sample_info['filename'])
        color = df_color[df_color['filename'] == filename]['color'].values
        ds.color.append(None if len(color)==0 else color)
```

{% hint style="info" %}
[Learn more about dataset lengths and padding here.](https://docs-v3.activeloop.ai/technical-details/data-format)
{% endhint %}

Now we see that `ds.summary()` shows 3 tensors, each with 11 samples (though the `color` tensor has several empty samples):

```
 tensor      htype            shape          dtype  compression
 -------    -------          -------        -------  ------- 
 images      image     (11, 1024, 1024, 3)   uint8    jpeg   
 labels   class_label       (11, 2:7)       uint32    None   
  color   class_label       (11, 0:1)       uint32    None  
```

#### Iterate through the supplemental data and add data at the corresponding Deep Lake index&#x20;

{% hint style="info" %}
This approach is recommended when the data updates are sparse
{% endhint %}

First, let's create a `color2` tensor, and the load all the existing Deep Lake filenames into memory. We then iterate through the supplemental data and find the corresponding Deep Lake index to insert the color information.

```python
with ds:
    ds.create_tensor('color2', htype = 'class_label')

    filenames = [os.path.basename(sample_info['filename']) for sample_info in ds.images.sample_info]

    for fn in df_color['filename'].values:
        index = filenames.index(fn)
        ds.color2[index] = df_color[df_color['filename'] == fn]['color'].values[0]
```

Now we see that `ds.summary()` shows 4 tensors, each with 11 samples (though the `color` and `color2` tensors have several empty samples):

```
 tensor      htype            shape          dtype  compression
 -------    -------          -------        -------  ------- 
 images      image     (10, 1024, 1024, 3)   uint8    jpeg   
 labels   class_label       (10, 2:7)       uint32    None   
  color   class_label       (10, 0:1)       uint32    None   
 color2   class_label       (10, 0:1)       uint32    None   
```

### Update Existing Rows without TQL

Originally, we did not specify a color for image `3.jpg`. Let's find the index for this image, look at it, and add the color manually. We've already loaded the Deep Lake dataset's filenames into memory above, so we can find the index using:

```python
index = filenames.index('3.jpg')
```

Let's visualize the image using PIL. We could also visualize it using `ds.visualize()` (must `pip install "deeplake[visualizer]"`) or using the [Deep Lake App](https://app.activeloop.ai/).

```
Image.fromarray(ds.images[index].numpy())
```

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/AXukSwD3YbgTD742c7Ig/3.jpg" alt=""><figcaption></figcaption></figure>

Since the image is white, let's update the color using:

```python
ds.color[index] = 'white'
```

### Delete Samples

Rows from a dataset can be deleted using `ds.pop()`. To delete the row at index 8 we run:

```python
ds.pop(8)
```

Now we see that `ds.summary()` shows 10 rows in the dataset (instead of 11):

```
 tensor      htype            shape          dtype  compression
 -------    -------          -------        -------  ------- 
 images      image     (10, 1024, 1024, 3)   uint8    jpeg   
 labels   class_label       (10, 2:7)       uint32    None   
  color   class_label       (10, 0:1)       uint32    None   
 color2   class_label       (10, 0:1)       uint32    None   
```

To replace data with empty data without deleting a row, you can run:&#x20;

```python
ds.color[index] = None
```

Congrats! You just learned how to make a variety of updates to Deep Lake datasets! 🎉


# Data Processing Using Parallel Computing

Deeplake offers built-in methods for parallelizing dataset computations in order to achieve faster data processing.

## How to use `deeplake.compute` for parallelizing workflows

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1-6bDMs-UNc97DxoQ9sJcdSNdTeBP1wI6?usp=sharing)

[Step 8](https://docs-v3.activeloop.ai/examples/dl/guide/parallel-computing) in the [Getting Started Guide](https://docs-v3.activeloop.ai/examples/dl/guide) highlights how `deeplake.compute` can be used to rapidly upload datasets. This tutorial expands further and highlights the power of parallel computing for dataset processing.

### Transformations on New Datasets

Computer vision applications often require users to process and transform their data. For example, you may perform perspective transforms, resize images, adjust their coloring, or many others. In this example, a flipped version of the [MNIST dataset](https://app.activeloop.ai/activeloop/mnist-train) is created, which may be useful for training a model that identifies text in scenes where the camera orientation is unknown.&#x20;

First, let's define a function that will flip the dataset images.

```python
import deeplake
from PIL import Image
import numpy as np

@deeplake.compute
def flip_vertical(sample_in, sample_out):
    ## First two arguments are always default arguments containing:
    #     1st argument is an element of the input iterable (list, dataset, array,...)
    #     2nd argument is a dataset sample
    
    # Append the label and image to the output sample
    sample_out.append({'labels': sample_in.labels.numpy(),
                       'images': np.flip(sample_in.images.numpy(), axis = 0)})
    
    return sample_out
```

Next, the existing [MNIST dataset](https://app.activeloop.ai/activeloop/mnist-train) is loaded, and deeplake`.like` is used to create an empty dataset with the same tensor structure.

```python
ds_mnist = deeplake.load('deeplake://activeloop/mnist-train')

#We use the overwrite=True to make this code re-runnable
ds_mnist_flipped = deeplake.like('./mnist_flipped', ds_mnist, overwrite = True)
```

Finally, the flipping operation is evaluated for the 1st 100 elements in the input dataset `ds_in`, and the result is automatically stored in `ds_out`.

```python
flip_vertical().eval(ds_mnist[0:100], ds_mnist_flipped, num_workers = 2)
```

Let's check out the flipped images:

```python
Image.fromarray(ds_mnist.images[0].numpy())
```

```python
Image.fromarray(ds_mnist_flipped.images[0].numpy())
```

### Transformations on Existing Datasets

In the previous example, a new dataset was created while performing a transformation. In this example, a transformation is used to modify an existing dataset.&#x20;

First, download and unzip the small classification dataset below called *animals.*&#x20;

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/CQftGlzveKhX5GzN5TSJ/animals.zip>" %}

Next, use `deeplake.ingest_classification` to automatically convert this image classification dataset into Deep Lake format and save it in `./animals_deeplake`.

```python
ds = deeplake.ingest_classification('./animals', './animals_deeplake') # Creates the dataset
```

The first image in the dataset is a picture of a cat:

```python
Image.fromarray(ds.images[0].numpy())
```

The images in the dataset can now be flipped by evaluating the `flip_vertical()` transformation function from the previous example. If a second dataset is not specified as an input to `.eval()`, the transformation is applied to the input dataset.&#x20;

```python
flip_vertical().eval(ds, num_workers = 2)
```

The picture of the cat is now flipped:

```python
Image.fromarray(ds.images[0].numpy())
```

### Dataset Processing Pipelines

In order to modularize your dataset processing, it is helpful to create functions for specific data processing tasks and combine them in pipelines. In this example, you can create a pipeline using the `flip_vertical` function from the first example and the `resize` function below.

```python
@deeplake.compute
def resize(sample_in, sample_out, new_size):
    ## First two arguments are always default arguments containing:
    #     1st argument is an element of the input iterable (list, dataset, array,...)
    #     2nd argument is a dataset sample
    ## Third argument is the required size for the output images
    
    # Append the label and image to the output sample
    sample_out.labels.append(sample_in.labels.numpy())
    sample_out.images.append(np.array(Image.fromarray(sample_in.images.numpy()).resize(new_size)))
    
    return sample_out
```

Functions decorated using `deeplake.compute` can be combined into pipelines using `deeplake.compose`. Required arguments for the functions must be passed into the pipeline in this step:

```python
pipeline = deeplake.compose([flip_vertical(), resize(new_size = (64,64))])
```

Just like for the single-function example above, the input and output datasets are created first, and the pipeline is evaluated for the 1st 100 elements in the input dataset `ds_in`. The result is automatically stored in `ds_out`.

```python
#We use the overwrite=True to make this code re-runnable
ds_mnist_pipe = deeplake.like('./mnist_pipeline', ds_mnist, overwrite = True)
```

```python
pipeline.eval(ds_mnist[0:100], ds_mnist_pipe, num_workers = 2)
```

### Recovering From Errors

If an error occurs related to a specific `sample_in`, `deplake.compute` will throw a `TransformError` and the error-causing index or sample can be caught using:

<pre class="language-python"><code class="lang-python"># from deeplake.util.exceptions import TransformError

# try:
#     compute_fn.eval(...)
# except TransformError as e:
<strong>#     failed_idx = e.index
</strong>#     failed_sample = e.sample
</code></pre>

The traceback also typically shows information such as the filename of the data that was causing issues. One the problematic sample has been identified, it should be removed from the list of input samples and the `deeplake.compute` function should be re-executed.&#x20;

Congrats! You just learned how to make parallelize your computations using Deep Lake! 🎉


# Deep Learning Playbooks

How to perform complex workflows using Deep Lake.

## Playbooks are comprehensive examples of end-to-end workflows using Activeloop products

{% content-ref url="playbooks/training-with-lineage" %}
[training-with-lineage](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-with-lineage)
{% endcontent-ref %}

{% content-ref url="playbooks/evaluating-model-performance" %}
[evaluating-model-performance](https://docs-v3.activeloop.ai/examples/dl/playbooks/evaluating-model-performance)
{% endcontent-ref %}

{% content-ref url="playbooks/training-reproducibility-wandb" %}
[training-reproducibility-wandb](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-reproducibility-wandb)
{% endcontent-ref %}

{% content-ref url="playbooks/working-with-videos" %}
[working-with-videos](https://docs-v3.activeloop.ai/examples/dl/playbooks/working-with-videos)
{% endcontent-ref %}


# Querying, Training and Editing Datasets with Data Lineage

How to use queries and version control while training models.

## How to use queries and version control to train models with reproducible data lineage.

The road from raw data to a trainable deep-learning dataset can be treacherous, often involving multiple tools glued together with spaghetti code. Activeloop simplifies this journey so you can create high-quality datasets and train production-level deep-learning models.

#### This playbook demonstrates how to use [Activeloop Deep Lake](https://app.activeloop.ai/) to:

* Create a Deep Lake dataset from data stored in an S3 bucket
* Visualize the data to gain insights about the underlying data challenges&#x20;
* Update, edit, and store different versions of the data with reproducibility
* Query the data, save the query result, and materialize it for training a model.
* Train a object detection model while streaming data

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/AAIO8S6MCyhXTNtjHmRS/Data%20Lineage%20for%20Object%20Detection%20Diagram.png)

### Prerequisites

In addition to installation of commonly used packages, this playbook requires installation of:&#x20;

```python
pip3 install deeplake
pip3 install albumentations
pip3 install opencv-python-headless==4.1.2.30 #In order for Albumentations to work properly
pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```

The required python imports are:

```python
import deeplake
import numpy as np
import boto3
import math
import time
import os
from tqdm import tqdm
from pycocotools.coco import COCO
import albumentations as A
from albumentations.pytorch import ToTensorV2
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
```

You should also register with Activeloop and create an API token in the UI.

### Creating the Dataset

Since many real-world datasets use the COCO annotation format, the [COCO training dataset](https://app.activeloop.ai/activeloop/coco-train) is used in this playbook. To avoid data duplication, [linked tensors](https://docs.deeplake.ai/en/latest/Htypes.html#link-htype) are used to store references to the images in the Deep Lake dataset from the S3 bucket containing the original data. For simplicity, only the bounding box annotations are copied to the the Deep Lake dataset.

To convert the original dataset to Deep Lake format, let's establish a connection to the original data in S3.

```python
dataset_bucket = 'non-hub-datasets'

s3 = boto3.resource('s3',
         aws_access_key_id=os.environ.get('aws_access_key_id'), 
         aws_secret_access_key=os.environ.get('aws_secret_access_key'))

s3_bucket = s3.Bucket(dataset_bucket)
```

Next, let's load the annotations so we can access them later:

```python
ann_path = 'coco/annotations/instances_train2017.json'
local_ann_path = 'anns_train.json'

s3_bucket.download_file(ann_path, local_ann_path)
coco = COCO(local_ann_path)

category_info = coco.loadCats(coco.getCatIds())
```

Moving on, let's create an empty Deep Lake dataset and pull managed credentials from Platform, so that we don't have to manually specify the credentials to access the `s3` links every time we use this dataset. Since the Deep Lake dataset is stored in Deep Lake storage, we also provide an [API token](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options) to identify the user.

```python
ds = deeplake.empty('hub://dl-corp/coco-train', token = 'Insert API Token')

creds_name = "my_s3_creds"
ds.add_creds_key(creds_name, managed = True)
```

The UI for managed credentials in Platform is shown below, and more details are [available here](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials).

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/GTtDw3C7XNPyFh1IT0kN/Managed_Crerentials.png)

Last but not least, let's create the Deep Lake dataset's tensors. In this example, we ignore the segmentations and keypoints from the COCO dataset, only uploading the bounding box annotations as well as their labels.

```python
img_ids = sorted(coco.getImgIds()) # Image ids for uploading

with ds:
    ds.create_tensor('images', htype = 'link[image]', sample_compression = 'jpg')
    ds.create_tensor('boxes', htype = 'bbox')
    ds.create_tensor('categories', htype = 'class_label')
```

Finally, let's iterate through the data and append it to our Deep Lake dataset. Note that when appending data, we directly pass the s3 URL and the managed credentials key for accessing that URL using `deeplake.link(url, creds_key)`

```python
with ds:
    ## ---- Iterate through each image and upload data ----- ##
    for img_id in tqdm(img_ids):
        anns = coco.loadAnns(coco.getAnnIds(img_id))
        img_coco = coco.loadImgs(img_id)[0]
                
        #First create empty objects for all the annotations
        boxes = np.zeros((len(anns),4))
        categories = []
        
        #Then populate the objects with the annotations data
        for i, ann in enumerate(anns):
            boxes[i,:] = ann['bbox']
            categories.append([category_info[i]['name'] for i in range(len(category_info)) if category_info[i]['id']==ann['category_id']][0])
        
        #If there are no categories present, append the empty list as None.
        if categories == []: categories = None

        img_url = "s3://{}/coco/train2017/{}".format(dataset_bucket, img_coco['file_name'])
            
        ds.append({"images": deeplake.link(img_url, creds_key=creds_name),
        "boxes": boxes.astype('float32'),
        "categories": categories})
```

{% hint style="info" %}
**Note:** if dataset creation speed is a priority, it can be accelerated using 2 options:

* By uploading the dataset in parallel. An example is [available here](https://github.com/activeloopai/examples/blob/main/coco/coco_upload_linked_parallel.ipynb).
* By setting the optional parameters below to `False`. In this case, the upload machine  will not load any of the data before creating the dataset, thus speeding the upload by up to 100X. The parameters below are defaulted to `True` because they improve the query speed on image shapes and file metadata, and they also verify the integrity of the data before uploading. More information is [available here](https://api-docs.activeloop.ai/#hub.Dataset.create_tensor):

```
ds.create_tensor('images', htype = 'link[image]',
    verify = False,
    create_shape_tensor = False,
    create_sample_info_tensor = False
    )
```

{% endhint %}

### Inspecting the Dataset

In this example, we will train an object detection model for driving applications. Therefore, we are interested in images containing cars, busses, trucks, bicycles, motorcycles, traffic lights, and stop signs, which we can find by running a SQL query on the dataset in Platform. More details on the query syntax are [available here](https://docs-v3.activeloop.ai/examples/tql).

```sql
(select * where contains(categories, 'car') limit 1000)
  union 
(select * where contains(categories, 'bus') limit 1000)
  union 
(select * where contains(categories, 'truck') limit 1000)
  union 
(select * where contains(categories, 'bicycle') limit 1000)
  union 
(select * where contains(categories, 'motorcycle') limit 1000)
  union 
(select * where contains(categories, 'traffic light') limit 1000)
  union 
(select * where contains(categories, 'stop sign') limit 1000)
```

A quick visual inspection of the dataset reveals several problems with the data including:

* Sample `61` but is a-low quality image where it's very difficult to discern the features, and it is not clear whether the small object in the distance is an actual traffic light. Images like this do not positively contribute to model performance, so let's delete all the data in this sample.![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/x5W2VyHMvKT5sqWFQwg0/image.png)

```python
ds.pop(61)

ds.commit('Deleted index 61 because the image is low quality.')
```

* In sample `8`, a road sign is labeled as a `stop sign`, even though the sign is facing away from the camera. Even though it may be a `stop sign`, computer vision systems should positively identify the type of a road sign based on its visible text. Therefore, let's remove the stop sign label from this image. &#x20;

```python
ds.categories[8] = ds.categories[8].numpy()[np.arange(0,4)!=2]
ds.boxes[8] = ds.boxes[8].numpy()[np.arange(0,4)!=2,:]

ds.commit('Deleted bad label at index 8')
```

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/CTRVchZ2hArA35qFugUD/Edit_Labels.png)

Both changes are now evident in the visualizer, and they were both logged as separate commits in the version control history. A summary of this inspection workflow is shown below:

{% embed url="<https://www.loom.com/share/6cf198b6fcf54bab983cd74335daea79>" %}

### Optimizing the Dataset for Training

Now that the dataset has been improved, we save the query result containing the samples of interest and optimize the data for training. **Since query results are associated with a particular commit, they are immutable and can be retrieved at any point in time.**

First, let's re-run the query and save the result as a dataset view, which is uniquely identified by an `id`.

{% embed url="<https://www.loom.com/share/cd4b706cf13b47c0bc8d82a15963dc66>" %}

The dataset is currently storing references to the images in S3, so the images are not rapidly streamable for training. Therefore, we materialize the query result (`Dataset View`) by copying and re-chunking the data for maximum performance:

```python
ds.load_view('62d6d490e49d0d7bab4e251f', optimize = True, num_workers = 4)
```

Once we're finished using the materialized dataset view, we may choose to delete it using:

```python
# ds.delete_view('62d6d490e49d0d7bab4e251f')
```

### Training an Object Detection Model

An object detection model can be trained using the same approach that is used for all Deep Lake datasets, with several examples in [our tutorials](https://docs-v3.activeloop.ai/examples/dl/playbooks/broken-reference). Typically the training would occur on another machine with more GPU power, so we start by loading the dataset and and corresponding dataset view:

```python
ds = deeplake.load('hub://dl-corp/coco-train', token = 'Insert API Token')

ds_view = ds.load_view('62d6d490e49d0d7bab4e251f')
```

When using subsets of datasets, it's advised to remap the input classes for model training. In this example, the source dataset has 81 classes, but we are only interested in 7 classes (cars, busses, trucks, bicycles, motorcycles, traffic lights, and stop signs). Therefore, we remap the classes of interest to values 0,1,2,3,4,6 before feeding them into the model for training. We also specify resolution for resizing the data before training the model.

```python
WIDTH = 128
HEIGHT = 128

# These are the classes we care about and they will be remapped to 0,1,2,3,4,6 in the model
CLASSES_OF_INTEREST = ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'traffic light', 'stop sign']

# The classes of interest correspond to the following array values in the current dataset
INDS_OF_INTEREST = [ds.categories.info.class_names.index(item) for item in CLASSES_OF_INTEREST]
```

Next, let's specify an augmentation pipeline, which mostly utilizes [Albumentations](https://github.com/albumentations-team/albumentations). We perform the remapping of the class labels inside the transformation function.

```python
# Augmentation pipeline using Albumentations
tform_train = A.Compose([
    A.RandomSizedBBoxSafeCrop(width=WIDTH, height=HEIGHT, erosion_rate=0.2),
    A.Rotate(limit=20, p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=16, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.



# Transformation function for pre-processing the deeplake sample before sending it to the model
def transform_train(sample_in):

    # Convert any grayscale images to RGB
    image = sample_in['images']
    shape = image.shape 
    if shape[2] == 1:
        image = np.repeat(image, int(3/shape[2]), axis = 2)

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'], shape)
    
    # Filter only the labels that we care about for this training run
    labels_all = sample_in['categories']
    indices = [l for l, label in enumerate(labels_all) if label in INDS_OF_INTEREST]
    labels_filtered = labels_all[indices]
    labels_remapped = [INDS_OF_INTEREST.index(label) for label in labels_filtered]
    boxes_filtered = boxes[indices,:]
    
    # Make sure the number of labels and boxes is still the same after filtering
    assert(len(labels_remapped)) == boxes_filtered.shape[0]

    # Pass all data to the Albumentations transformation
    transformed = tform_train(image = image, 
                              bboxes = boxes_filtered, 
                              bbox_ids = np.arange(boxes_filtered.shape[0]),
                              class_labels = labels_remapped,
                              )

    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)
    
    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))


    # Put annotations in a separate object
    target = {'labels': labels_torch, 'boxes': boxes_torch}
    
    return transformed['image'], target


# Conversion script for bounding boxes from coco to Pascal VOC format
def coco_2_pascal(boxes, shape):
    # Convert bounding boxes to Pascal VOC format and clip bounding boxes to make sure they have non-negative width and height
    
    return np.stack((np.clip(boxes[:,0], 0, None), np.clip(boxes[:,1], 0, None), np.clip(boxes[:,0]+np.clip(boxes[:,2], 1, None), 0, shape[1]), np.clip(boxes[:,1]+np.clip(boxes[:,3], 1, None), 0, shape[0])), axis = 1)

def collate_fn(batch):
    return tuple(zip(*batch))
```

You can now create a PyTorch dataloader that connects the Deep Lake dataset to the PyTorch model using the provided method `ds_view.pytorch()`. This method automatically applies the transformation function and takes care of random shuffling (if desired). The `num_workers` parameter can be used to parallelize data preprocessing, which is critical for ensuring that preprocessing does not bottleneck the overall training workflow.

```python
train_loader = ds_view.pytorch(num_workers = 8, shuffle = True, 
                          transform = transform_train,
                          tensors = ['images', 'categories', 'boxes'],
                          batch_size = 16,
                          collate_fn = collate_fn)
```

This playbook uses a [pre-trained torchvision neural network](https://pytorch.org/vision/main/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html) from the `torchvision.models` module. We define helper functions for loading the model and for training 1 epoch.

```python
# Helper function for loading the model
def get_model_object_detection(num_classes):
    # Load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

    # Get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # Replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model
    
# Helper function for training for 1 epoch
def train_one_epoch(model, optimizer, data_loader, device):
    model.train()

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        targets = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
                
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()
        
        # Print performance statistics
        if i%10 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] loss: %.3f, speed: %.2f' %
                  (i, loss_value, speed))

        if not math.isfinite(loss_value):
            print(f"Loss is {loss_value}, stopping training")
            print(loss_dict)
            break

        optimizer.zero_grad()

        losses.backward()
        optimizer.step()
```

Training is performed on a GPU if possible. Otherwise, it's on a CPU.

```python
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(device)
```

Let's initialize the model and optimizer.

```python
model = get_model_object_detection(len(CLASSES_OF_INTEREST))
model.to(device)

# Specify the optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                            momentum=0.9, weight_decay=0.0005)
```

The model and data are ready for training 🚀!

```python
# Train the model for 1 epoch
num_epochs = 3

lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.1)
    
for epoch in range(num_epochs):  # Loop over the dataset multiple times
    print("------------------ Training Epoch {} ------------------".format(epoch+1))
    train_one_epoch(model, optimizer, train_loader, device)
    lr_scheduler.step()
    
    # --- Insert Testing Code Here ---

print('Finished Training')
```

#### Congratulations 🚀. You can now use Activeloop Deep Lake to edit and version control your datasets, as well as query datasets and train models on the results, all while maintaining data lineage!


# Evaluating Model Performance

How to compare ground-truth annotations with model predictions

## How to evaluate model performance and compare ground-truth annotations with model predictions.

Models are never perfect after the first training, and model predictions need to be compared with ground-truth annotations in order to iterate on the training process. This comparison often reveals incorrectly annotated data and sheds light on the types of data where the model fails to make the correct prediction.

**This playbook demonstrates how to use** [**Activeloop Deep Lake**](https://app.activeloop.ai/) **to:**

* Improve training data by finding data for which the model has poor performance
  * Train an object detection model using a Deep Lake dataset
  * Upload the training loss per image to a branch on the dataset designated for evaluating model performance
  * Sort the training dataset based on model loss and identify bad samples
  * Edit and clean the bad training data and commit the changes
* Evaluate model performance on validation data and identify difficult data
  * Compute model predictions of object detections for a validation Deep Lake dataset
  * Upload the model predictions to the validation dataset, compared them to ground truth annotations, and identify samples for which the model fails to make the correct predictions.

### Prerequisites

In addition to installation of commonly user packages, this playbook requires installation of:&#x20;

```python
pip3 install deeplake
pip3 install albumentations
pip3 install opencv-python-headless==4.1.2.30 #In order for Albumentations to work properly
```

The required python imports are:

```python
import deeplake
import numpy as np
import math
import sys
import time
from PIL import Image
import albumentations as A
from albumentations.pytorch import ToTensorV2
import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
```

You should also register with Activeloop and create an API token in the UI.

### Creating the Dataset

In this playbook we will use the `svhn-train` and `-test` datasets that are already [hosted by Activeloop](https://app.activeloop.ai/activeloop/svhn-train). Let's copy them to our own organization `dl-corp` in order to have write access:

```python
ds_train = deeplake.deepcopy('hub://activeloop/svhn-train', 'hub://dl-corp/svhn-train', )
ds_test = deeplake.deepcopy('hub://activeloop/svhn-test', 'hub://dl-corp/svhn-test')
```

These are object detection datasets that localize address numbers on buildings:

{% embed url="<https://www.loom.com/share/84e12b6974d3488b8281756d10f428bf>" %}

Let's create a branch called `training_run` on both datasets for storing the model results.

```python
ds_train.checkout('training_run', create = True)
ds_test.checkout('training_run', create = True)
```

Since we will write the model results back to the Deep Lake datasets, let's create a group called `model_evaluation` in the datasets and add tensors that will store the model results.

{% hint style="warning" %}
Putting the model results in a separate group will prevent the visualizer from confusing the predictions and ground-truth data.
{% endhint %}

```python
# Store the loss in the training dataset
ds_train.create_group('model_evaluation')
ds_train.model_evaluation.create_tensor('loss')

# Store the predictions for the labels, boxes, and the average iou of the 
# boxes, for the test dataset
ds_test.create_group('model_evaluation')
ds_test.model_evaluation.create_tensor('labels', htype = 'class_label', class_names = ds_test.labels.info.class_names)
ds_test.model_evaluation.create_tensor('boxes', htype = 'bbox', coords = {'type': 'pixel', 'mode': 'LTWH'})
ds_test.model_evaluation.create_tensor('iou')
```

### Training an Object Detection Model

An object detection model can be trained using the same approach that is used for all Deep Lake datasets, with several examples in [our tutorials](https://docs-v3.activeloop.ai/examples/dl/playbooks/broken-reference). First, let's specify an augmentation pipeline, which mostly utilizes [Albumentations](https://github.com/albumentations-team/albumentations). We also define several helper functions for resizing and converting the format of bounding boxes.

```
WIDTH = 128
HEIGHT = 64
NUM_CLASSES = len(ds_train.labels.info.class_names)
```

```python
# Augmentation pipeline for training using Albumentations
tform_train = A.Compose([
    A.RandomSizedBBoxSafeCrop(width=WIDTH, height=HEIGHT, erosion_rate=0.2),
    A.Rotate(limit=20, p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=8, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.

# Augmentation pipeline for validation using Albumentations
tform_val = A.Compose([
    A.Resize(width=WIDTH, height=HEIGHT),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=8, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.


# Transformation function for pre-processing the Deep Lake training sample before sending it to the model
def transform_train(sample_in):

    # Convert any grayscale images to RGB
    image = sample_in['images']
    shape = image.shape 
    if shape[2] == 1:
        image = np.repeat(image, 3, axis = 2)

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'], shape)    

    # Pass all data to the Albumentations transformation
    transformed = tform_train(image = image, 
                              bboxes = boxes, 
                              bbox_ids = np.arange(boxes.shape[0]),
                              class_labels = sample_in['labels'],
                              )

    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)

    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))
        

    # Put annotations in a separate object
    target = {'labels': labels_torch, 'boxes': boxes_torch}
    
    return transformed['image'], target


# Transformation function for pre-processing the Deep Lake validation sample before sending it to the model
def transform_val(sample_in):

    # Convert any grayscale images to RGB
    image = sample_in['images']
    shape = image.shape 
    if shape[2] == 1:
        image = np.repeat(images, 3, axis = 2)

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'], shape)    

    # Pass all data to the Albumentations transformation
    transformed = tform_val(image = image, 
                              bboxes = boxes, 
                              bbox_ids = np.arange(boxes.shape[0]),
                              class_labels = sample_in['labels'],
                              )

    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)

    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))
        

    # Put annotations in a separate object
    target = {'labels': labels_torch, 'boxes': boxes_torch}

    # We also return the shape of the original image in order to resize the predictions to the dataset image size
    return transformed['image'], target, sample_in['index'], shape


# Conversion script for bounding boxes from coco to Pascal VOC format
def coco_2_pascal(boxes, shape):
    # Convert bounding boxes to Pascal VOC format and clip bounding boxes to make sure they have non-negative width and height

    return np.stack((np.clip(boxes[:,0], 0, None), np.clip(boxes[:,1], 0, None), np.clip(boxes[:,0]+np.clip(boxes[:,2], 1, None), 0, shape[1]), np.clip(boxes[:,1]+np.clip(boxes[:,3], 1, None), 0, shape[0])), axis = 1)

# Conversion script for resizing the model predictions back to shape of the dataset image
def model_2_image(boxes, model_shape, img_shape):
    # Resize the bounding boxes convert them from Pascal VOC to COCO
    
    m_h, m_w = model_shape
    i_h, i_w = img_shape
    
    x0 = boxes[:,0]*(i_w/m_w)
    y0 = boxes[:,1]*(i_h/m_h)
    x1 = boxes[:,2]*(i_w/m_w)
    y1 = boxes[:,3]*(i_h/m_h)

    return np.stack((x0, y0, x1-x0, y1-y0), axis = 1)


def collate_fn(batch):
    return tuple(zip(*batch))
```

We can now create a PyTorch dataloader that connects the Deep Lake dataset to the PyTorch model using the provided method `ds.pytorch()`. This method automatically applies the transformation function and takes care of random shuffling (if desired). The `num_workers` parameter can be used to parallelize data preprocessing, which is critical for ensuring that preprocessing does not bottleneck the overall training workflow.

```python
train_loader = ds_train.pytorch(num_workers = 8, shuffle = True, 
                          transform = transform_train,
                          tensors = ['images', 'labels', 'boxes'],
                          batch_size = 4,
                          collate_fn = collate_fn)
```

This playbook uses a [pre-trained torchvision neural network](https://pytorch.org/vision/master/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html) from the `torchvision.models` module. We define helper functions for loading the model and for training 1 epoch.

```python
# Helper function for loading the model
def get_model_object_detection(num_classes):
    # Load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

    # Get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # Replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model
    
# Helper function for training for 1 epoch
def train_one_epoch(model, optimizer, data_loader, device):
    model.train()

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        targets = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
                
        loss_dict = model(images, targets)

        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()
        
        # Print performance statistics
        if i%100 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] loss: %.3f, speed: %.2f' %
                  (i, loss_value, speed))

        if not math.isfinite(loss_value):
            print(f"Loss is {loss_value}, stopping training")
            print(loss_dict)
            break

        optimizer.zero_grad()

        losses.backward()
        optimizer.step()
```

Training is performed on a GPU if possible. Otherwise, it's on a CPU.

```python
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(device)
```

Let's initialize the model and optimizer:

```python
model = get_model_object_detection(NUM_CLASSES)

model.to(device)

# Specify the optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                            momentum=0.9, weight_decay=0.0005)
```

The model and data are ready for training 🚀!

```python
# Train the model
num_epochs = 3

lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.1)
    
for epoch in range(num_epochs):  # loop over the dataset multiple times
    print("------------------ Training Epoch {} ------------------".format(epoch+1))
    train_one_epoch(model, optimizer, train_loader, device)
    lr_scheduler.step()
    
print('Finished Training')

torch.save(model.state_dict(), 'model_weights_svhn_first_train.pth')
```

### Evaluating Model Performance on Training Data

Evaluating the performance of the model on a per-image basis can be a powerful tool for identifying bad or difficult data. First, we define a helper function that does a forward-pass through the model and computes the `loss` per image, without updating the weights. Since the model outputs the loss per batch, this functions requires that the `batch size` is 1.

```python
def evaluate_loss(model, data_loader, device):
    # This function assumes the data loader may be shuffled, and it returns the loss in a sorted fashion
    # using knowledge of the indices that are being trained in each batch. 
    
    # Set the model to train mode in order to get the loss, even though we're not training.
    model.train()
    
    loss_list = []
    indices_list = []
    
    assert data_loader.batch_size == 1

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        targets = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
        indices = data[2]
        
        with torch.no_grad():
            loss_dict = model(images, targets)

        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()
        
        loss_list.append(loss_value)
        indices_list.append(indices)
        
        # Print performance statistics
        if i%100 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] loss: %.3f, speed: %.2f' %
                  (i, loss_value, speed))
        
    loss_list = [x for _, x in sorted(zip(indices_list, loss_list))]
    
    return loss_list
```

Next, let's create another PyTorch dataloader on the training dataset that is not shuffled, has a batch size of 1, uses the evaluation transform, and returns the indices of the current batch the dataloader using `return_index= True`:

```python
train_loader_eval = ds_train.pytorch(num_workers = 8, 
                                     shuffle = False,
                                     transform = transform_val,
                                     tensors = ['images', 'labels', 'boxes'],
                                     batch_size = 1,
                                     collate_fn = collate_fn,
                                     return_index = True)
```

Finally, we evaluate the loss for each image, write it back to the dataset, and add a commit to the `training_run` branch that we created at the start of this playbook:

```python
loss_per_image = evaluate_loss(model, train_loader_eval, device)
```

```python
with ds_train:
    ds_train.model_evaluation.loss.extend(loss_per_image)
    
ds_train.commit('Trained the model and computed the loss for each image.')
```

### Cleanup and Reverting Mistakes in The Workflow

If you make a mistake you can use the following commands to start over or delete the new data:

* Delete data in a tensor: `ds.<tensor_name>.clear()`
* Delete the entire tensor and its data: `ds.delete_tensor(<tensor_name>)`
* Reset all edits since the prior commit: `ds.reset()`
* Delete the branch you just created: `ds.delete_branch(<branch_name>)`
  * Must be on another branch, and deleted branch must not have been merged to another.

### Inspecting the Training Dataset based on Model Results

The dataset can be sorted based on `loss` in [Activeloop Platform](https://app.activeloop.ai/). An inspection of the high-loss images immediately reveals that many of them have poor quality or are incorrectly annotated.

{% hint style="danger" %}
The sort feature in the video below was removed. To sort, please run the query:

`select * order by "model_evaluation/loss" order by desc`
{% endhint %}

{% embed url="<https://www.loom.com/share/3335ef5c11074291ba5addbaedea3a10>" %}

We can edit some of the bad data by deleting the incorrect annotation of `"1"` at index `14997` , and by removing the poor quality samples at indices `2899` and `32467`.&#x20;

```python
# Remove label "1" from 14997. It's in the first positions in the labels and boxes arrays
ds_train.labels[14997] = ds_train.labels[14997].numpy()[1:]
ds_train.boxes[14997] = ds_train.boxes[14997].numpy()[1:,:]

# Delete bad samples
ds_train.pop(32467)
ds_train.pop(2899)
```

Lastly, we commit the edits in order to permanently store this snapshot of the data.&#x20;

```python
ds_train.commit('Updated labels at index 14997 and deleted samples at 2899 and 32467')
```

The next step would be perform a more exhaustive inspection of the high-loss data and make further improvements to the dataset, after which the model should be re-trained.

### Evaluating Model Performance on Validation Data

After iterating on the training data re-training the model, a general assessment of model performance should be performed on validation data that was not used to train the model. We create a helper function for running an inference of the model on the validation data that returns the model predictions and the average IOU ([intersection-over-union](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)) for each sample:

```python
# Run an inference of the model and compute the average IOU (intersection-over-union) for each sample
def evaluate_iou(model, data_loader, num_classes, device = 'cpu', score_thresh = 0.5):
    # This function removes predictions in the output and IUO calculation that are below a confidence threshold.

    # This function assumes the data loader may be shuffled, and it returns the loss in a sorted fashion
    # using knowledge of the indices that are being trained in each batch. 
    
    # Set the model to eval mode.
    model.eval()

    ious_list = []
    boxes_list = [] 
    labels_list = []
    indices_list = []

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        ground_truths = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
        indices = data[2]

        model_start = time.time()
        with torch.no_grad():
            predictions = model(images)
        model_end = time.time()

        assert len(ground_truths) == len(predictions) == len(indices) # Check if data in dataloader is consistent
        
        for j, pred in enumerate(predictions):
            
            # Ignore boxes below the confidence threshold
            thresh_inds = pred['scores']>score_thresh
            pred_boxes = pred['boxes'][thresh_inds]
            pred_labels = pred['labels'][thresh_inds]
            pred_scores = pred['scores'][thresh_inds]
            
            # Find the union of prediceted and groud truth labels and iterate through it
            all_labels = np.union1d(pred_labels.to('cpu'), ground_truths[j]['labels'].to('cpu'))

            ious = np.zeros((len(all_labels)))
            for l, label in enumerate(all_labels):
                
                # Find the boxes corresponding to the label
                boxes_1 = pred_boxes[pred_labels == label]
                boxes_2 = ground_truths[j]['boxes'][ground_truths[j]['labels'] == label]
                iou = torchvision.ops.box_iou(boxes_1, boxes_2).cpu() # This method returns a matrix of the IOU of each box with every other box.
                
                # Consider the IOU as the maximum overlap of a box with any other box. Find the max along the axis that has the most boxes. 
                if 0 in iou.shape:
                    ious[l] = 0
                else:
                    if boxes_1.shape>boxes_2.shape:
                        max_iou, _ = iou.max(dim=0)
                    else:
                        max_iou, _ = iou.max(dim=1)
                        
                    # Compute the average iou for that label
                    ious[l] = np.mean(np.array(max_iou))
            
            
            #Take the average iou for all the labels. If there are no labels, set the iou to 0.
            if len(ious)>0: 
                ious_list.append(np.mean(ious))
            else: 
                ious_list.append(0)
                            
            boxes_list.append(model_2_image(pred_boxes.cpu(), (HEIGHT, WIDTH), (data[3][j][0], data[3][j][1]))) # Convert the bounding box back to teh shape of the original image
            labels_list.append(np.array(pred_labels.cpu()))
            indices_list.append(indices[j])
        
        # Print progress
        if i%100 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] speed: %.2f' %
                  (i, speed))
    
    # Sort the data based on index, just in case shuffling was used in the dataloader
    ious_list = [x for _, x in sorted(zip(indices_list, ious_list))]
    boxes_list = [x for _, x in sorted(zip(indices_list, boxes_list))]
    labels_list = [x for _, x in sorted(zip(indices_list, labels_list))]

    return  ious_list, boxes_list, labels_list
```

Let's create a PyTorch dataloader using the validation data and run the inference using `evaluate_iou` above.

```python
val_loader = ds_test.pytorch(num_workers = 8, 
                             shuffle = False, 
                             transform = transform_val,
                             tensors = ['images', 'labels', 'boxes'],
                             batch_size = 16,
                             collate_fn = collate_fn,
                             return_index = True)
```

```python
iou_val, boxes_val, labels_val = evaluate_iou(model, 
                                              val_loader, 
                                              NUM_CLASSES, 
                                              device, 
                                              score_thresh = 0.5)
```

Finally, we write the predictions back to the dataset and add a commit to the `training_run` branch that we created at the start of this playbook:

```python
with ds_test:
    ds_test.model_evaluation.labels.extend(labels_eval_test)
    ds_test.model_evaluation.boxes.extend(boxes_eval_test)
    ds_test.model_evaluation.iou.extend(iou_eval_test)
    
ds_test.commit('Added model predictions.')
```

### Comparing Model Results to Ground-Truth Annotations.

When sorting the model predictions based on IOU, we observe that the model successfully makes the correct predictions in images with one street number and where the street letters are large relative to the image. However, the model predictions are very poor for data with small street numbers, and there exist artifacts in the data where the model interprets vertical objects, such as narrow windows that the model thinks are the number "1".

{% hint style="danger" %}
The sort feature in the video below was removed. To sort, please run the query:

`select * order by "model_evaluation/iou" order by asc`
{% endhint %}

{% embed url="<https://www.loom.com/share/4fa87d8a409d4636a32a47e77f069d9a>" %}

Understanding the edge cases for which the model makes incorrect predictions is critical for improving the model performance. If the edge cases are irrelevant given the model's intended use, they should be eliminated from both the training and validation data. If they are applicable, more representative edge cases should be added to the training dataset, or the edge cases should be sampled more frequently while training.

#### Congratulations 🚀. You can now use Activeloop Deep Lake to evaluate the performance of your Deep-Learning models and compare their predictions to the ground-truth!


# Training Reproducibility Using Deep Lake and Weights & Biases

How to achieve full reproducibility of model training using Deep Lake and W\&B

### How to achieve full reproducibility of model training by combining Deep Lake data lineage with W\&B logging

Experiment tracking tools such as [Weights & Biases](https://wandb.ai/) (W\&B) improve reproducibility of your machine learning experiments by offering logging of datasets, hyper parameters, source codes, and more. When running model training with W\&B and Deep Lake, Deep Lake automatically pushes information required to reproduce the data such as the `uri`, `commit_id`, and `view_id` to the active W\&B run. By fully logging the state of your dataset, model, and source code, you can achieve full reproducibility of model training run for datasets of any size.

**This playbook demonstrates how to use** [**Activeloop Deep Lake**](https://app.activeloop.ai/) **with** [**Weights & Biases**](https://wandb.ai/) **to:**

* Upload a Deep Lake dataset in a W\&B run and create a W\&B artifact
* Query the dataset using Activeloop and save the query result in optimized format for training
* Train an object detection model on the saved query result and log the training parameters in a W\&B run
* Re-train the model with adjusted parameters and use W\&B to compare the different training runs.

### Prerequisites&#x20;

In addition to installation of commonly used packages in deep-learning, this playbook requires installation of:&#x20;

```
!pip install deeplake
!pip install wandb
!pip install albumentations
```

The required python imports are:

```python
import deeplake
import albumentations as A
from albumentations.pytorch import ToTensorV2
import numpy as np
import torch
import wandb
import time
import sys
import math
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
```

You should also register with Activeloop and W\&B, create API tokens for both tools, and log in to your W\&B account via the CLI using:

```
!wandb login
```

### Creating a W\&B Artifact from a Deep Lake Dataset

While the most common use case W\&B is to track training and evaluation jobs, you may also wrap your dataset upload jobs in a W\&B run in order to create W\&B artifacts. Any future runs that consume this dataset will also consume the corresponding W\&B artifact. As a result, your Deep Lake datasets will be automatically tracked by W\&B and can be visualized in the W\&B artifacts lineage UI.

Any `commit`, `copy` or `deepcopy` operation inside a W\&B run will create a W\&B artifact. Here we emulate a dataset upload by copying a dataset that is already hosted by Activeloop.

```python
WANDB_PROJECT = 'deeplake-demos'

run = wandb.init(project=WANDB_PROJECT, job_type='dataset_upload')

ds_train = deeplake.deepcopy('hub://activeloop/visdrone-det-train', 'hub://dl-corp/visdrone-det-train',
                 dest_token = 'Insert API Token')

ds_val = deeplake.deepcopy('hub://activeloop/visdrone-det-val', 'hub://dl-corp/visdrone-det-val',
                 dest_token = 'Insert API Token')

run.finish()
```

{% hint style="info" %}
You may replace `dl-corp` in the dataset path above with your own Deep Lake organization in order to run the code.
{% endhint %}

If we open the W\&B page for the run above, we see that the datasets has been tracked that artifacts were created for both the training and validation datasets.&#x20;

{% embed url="<https://www.loom.com/share/5281d75fbae04345b06cf4733901e4ec>" %}

### Train a model using the Deep Lake dataset

Suppose we are building a surveillance system to count and classify vehicles in small-to-medium size parking lots. The [visdrone dataset](https://app.activeloop.ai/activeloop/visdrone-det-train) is suitable starting point because it contains a variety of images of vehicles taken in cities using a UAV. However, many images are taken from very large viewing distances, thus resulting in small objects that are difficult to detect in object detection models, and are also not relevant to our surveillance application, like the image below.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/3pDV4f00ktHDuIcdhZKK/Hard_Image.png" alt=""><figcaption></figcaption></figure>

Therefore, we filter out these images and train the model on a subset of the dataset that is more appropriate for our application.

#### Querying the dataset

Let's use the query engine on the [Deep Lake UI ](https://app.activeloop.ai)to filter out samples that contain any cars with a width or height below 20 pixels. Since most images with vehicles contain cars, this query is a reliable proxy for imaging distance.

```sql
select * where not any(logical_and(logical_or(boxes[:,2]<20, boxes[:,3]<20), labels == 'car'))
```

This query eliminates approximately 50% of the samples in the dataset.

{% embed url="<https://www.loom.com/share/352123e870e146209624bd1f0c57a4ff>" %}

The steps above can also be performed programmatically.

```python
# train_view = ds.query("select * where not any(logical_and(logical_or(boxes[:,2]<20, boxes[:,3]<20), labels == 'car'))")
# train_view.save_view()

# val_view = ds.query("select * where not any(logical_and(logical_or(boxes[:,2]<20, boxes[:,3]<20), labels == 'car'))")
# val_view.save_view()
```

#### Training the model

Before training the model, which will often happen on a different machine than where the dataset was created, we first re-load the data for training and optimize if for streaming performance.

```python
ds_train = deeplake.load('hub://dl-corp/visdrone-det-train', token = 'Insert API Token', read_only = True)

ds_val = deeplake.load('hub://dl-corp/visdrone-det-val', token = 'Insert API Token', read_only = True)
```

```python
ds_train_view = ds_train.load_view('6337166131028ba8bcf7f2ff', optimize = True, num_workers = 4)

ds_val_view = ds_val.load_view('633716a10c1052d4385ab5c8', optimize = True, num_workers = 4)
```

An object detection model can be trained using the same approach that is used for all Deep Lake datasets, with several examples in [our tutorials](https://docs.activeloop.ai/tutorials/training-models).

When using subsets of datasets, it's advised to remap the input classes for model training. In this example, the source dataset has 12 classes, but we are only interested in 9 classes containing objects we want to localize in our parking lot (`bicycle`, `car`, `van`, `truck`, `tricycle`, `awning-tricycle`, `bus`, `motor`, `others`). Therefore, we remap the classes of interest to values 0,1,2,3,4,6,7,8 before feeding them into the model for training.&#x20;

Later in this playbook, we will experiment with different transform resolutions, so we specify the transform resolution (`WIDTH`, `HEIGHT`), `BATCH_SIZE`, and minimum bounding box area for transformation (`MIN_AREA`).&#x20;

{% hint style="warning" %}
All bounding boxes below MIN\_AREA are ignored in the transformation and are not fed to the model
{% endhint %}

```python
WIDTH = 160
HEIGHT = 128
MIN_AREA = 32
BATCH_SIZE = 16

# These are the classes we care about and they will be remapped to 0,1,2,3,4,5,6,7,8 in the model
CLASSES_OF_INTEREST = ['bicycle', 'car', 'van', 'truck', 'tricycle', 'awning-tricycle', 'bus', 'motor', 'others']

# The classes of interest correspond to the following array values in the current dataset
INDS_OF_INTEREST = [ds_train.labels.info.class_names.index(item) for item in CLASSES_OF_INTEREST]
```

Next, let's specify an augmentation pipeline, which mostly utilizes [Albumentations](https://github.com/albumentations-team/albumentations). We perform the remapping of the class labels inside the transformation function.

```python
# Augmentation pipeline for training using Albumentations
tform_train = A.Compose([
    A.RandomSizedBBoxSafeCrop(width=WIDTH, height=HEIGHT, erosion_rate=0.2),
    A.Rotate(limit=20, p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=0.5),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=MIN_AREA, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.


# Augmentation pipeline for validation using Albumentations
tform_val = A.Compose([
    A.Resize(width=WIDTH, height=HEIGHT),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels', 'bbox_ids'], min_area=MIN_AREA, min_visibility=0.6)) # 'label_fields' and 'box_ids' are all the fields that will be cut when a bounding box is cut.



# Transformation function for pre-processing the Deep Lake sample before sending it to the model
def transform_train(sample_in):
    # sample_in is a row in the dataset, referenced as a dictionary. 
    # sample_in['images'] is like ds.images[index].numpy()
    
    # Convert any grayscale images to RGB
    image = sample_in['images']
    shape = image.shape 
    if shape[2] == 1:
        image = np.repeat(image, int(3/shape[2]), axis = 2)

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'], shape)
    
    # Filter only the labels that we care about for this training run
    labels_all = sample_in['labels']
    indices = [l for l, label in enumerate(labels_all) if label in INDS_OF_INTEREST]
    labels_filtered = labels_all[indices]
    labels_remapped = [INDS_OF_INTEREST.index(label) for label in labels_filtered]
    boxes_filtered = boxes[indices,:]
    
    # Make sure the number of labels and boxes is still the same after filtering
    assert(len(labels_remapped)) == boxes_filtered.shape[0]

    # Pass all data to the Albumentations transformation
    transformed = tform_train(image = image, 
                              bboxes = boxes_filtered, 
                              bbox_ids = np.arange(boxes_filtered.shape[0]),
                              class_labels = labels_remapped,
                              )

    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)
    
    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))


    # Put annotations in a separate object
    target = {'labels': labels_torch, 'boxes': boxes_torch}
    
    return transformed['image'], target


# Transformation function for pre-processing the Deep Lake validation sample before sending it to the model
def transform_val(sample_in):

    # Convert any grayscale images to RGB
    image = sample_in['images']
    shape = image.shape 
    if shape[2] == 1:
        image = np.repeat(image, 3, axis = 2)

    # Convert boxes to Pascal VOC format
    boxes = coco_2_pascal(sample_in['boxes'], shape)    

    # Filter only the labels that we care about for this training run
    labels_all = sample_in['labels']
    indices = [l for l, label in enumerate(labels_all) if label in INDS_OF_INTEREST]
    labels_filtered = labels_all[indices]
    labels_remapped = [INDS_OF_INTEREST.index(label) for label in labels_filtered]
    boxes_filtered = boxes[indices,:]
    
    # Make sure the number of labels and boxes is still the same after filtering
    assert(len(labels_remapped)) == boxes_filtered.shape[0]

    
    # Pass all data to the Albumentations transformation
    transformed = tform_val(image = image, 
                            bboxes = boxes_filtered, 
                            bbox_ids = np.arange(boxes_filtered.shape[0]),
                            class_labels = labels_remapped,
                            )

    # Convert boxes and labels from lists to torch tensors, because Albumentations does not do that automatically.
    # Be very careful with rounding and casting to integers, becuase that can create bounding boxes with invalid dimensions
    labels_torch = torch.tensor(transformed['class_labels'], dtype = torch.int64)

    boxes_torch = torch.zeros((len(transformed['bboxes']), 4), dtype = torch.int64)
    for b, box in enumerate(transformed['bboxes']):
        boxes_torch[b,:] = torch.tensor(np.round(box))
        
    # Put annotations in a separate object
    target = {'labels': labels_torch, 'boxes': boxes_torch}

    # We also return the shape of the original image in order to resize the predictions to the dataset image size
    return transformed['image'], target, sample_in['index'], shape



# Conversion script for bounding boxes from coco to Pascal VOC format
def coco_2_pascal(boxes, shape):
    # Convert bounding boxes to Pascal VOC format and clip bounding boxes to make sure they have non-negative width and height
    
    return np.stack((np.clip(boxes[:,0], 0, None), np.clip(boxes[:,1], 0, None), np.clip(boxes[:,0]+np.clip(boxes[:,2], 1, None), 0, shape[1]), np.clip(boxes[:,1]+np.clip(boxes[:,3], 1, None), 0, shape[0])), axis = 1)

def collate_fn(batch):
    return tuple(zip(*batch))
```

This playbook uses a [pre-trained torchvision neural network](https://pytorch.org/vision/master/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html) from the `torchvision.models` module. We define helper functions for loading the model, training for 1 epoch (including W\&B logging), and evaluating the model by computing the average IOU ([intersection-over-union](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)) for the bounding boxes.

```python
# Helper function for loading the model
def get_model_object_detection(num_classes):
    # Load an instance segmentation model pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

    # Get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model
    

# Helper function for training for 1 epoch
def train_one_epoch(model, optimizer, data_loader, device):
    model.train()

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        targets = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
                
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        loss_value = losses.item()
        
        wandb.log({"loss": loss_value})
        
        # Print performance statistics
        if i%10 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] loss: %.3f, speed: %.2f' %
                  (i, loss_value, speed))

        if not math.isfinite(loss_value):
            print(f"Loss is {loss_value}, stopping training")
            print(loss_dict)
            break

        optimizer.zero_grad()

        losses.backward()
        optimizer.step()
        
        
# Helper function for computing the average IOU (intersection-over-union) for all the data
def evaluate_iou(model, data_loader, device = 'cpu', score_thresh = 0.5):
    # This function removes predictions in the output and IUO calculation that are below a confidence threshold.
    
    # Set the model to eval mode.
    model.eval()

    ious_list = []

    start_time = time.time()
    for i, data in enumerate(data_loader):

        images = list(image.to(device) for image in data[0])
        ground_truths = [{k: v.to(device) for k, v in t.items()} for t in data[1]]
        
        model_start = time.time()
        with torch.no_grad():
            predictions = model(images)
        model_end = time.time()

        assert len(ground_truths) == len(predictions) # Check if data in dataloader is consistent
        
        for j, pred in enumerate(predictions):
            
            # Ignore boxes below the confidence threshold
            thresh_inds = pred['scores']>score_thresh
            pred_boxes = pred['boxes'][thresh_inds]
            pred_labels = pred['labels'][thresh_inds]
            pred_scores = pred['scores'][thresh_inds]
            
            # Find the union of prediceted and groud truth labels and iterate through it
            all_labels = np.union1d(pred_labels.to('cpu'), ground_truths[j]['labels'].to('cpu'))

            ious = np.zeros((len(all_labels)))
            for l, label in enumerate(all_labels):
                
                # Find the boxes corresponding to the label
                boxes_1 = pred_boxes[pred_labels == label]
                boxes_2 = ground_truths[j]['boxes'][ground_truths[j]['labels'] == label]
                iou = torchvision.ops.box_iou(boxes_1, boxes_2).cpu() # This method returns a matrix of the IOU of each box with every other box.
                
                # Consider the IOU as the maximum overlap of a box with any other box. Find the max along the axis that has the most boxes. 
                if 0 in iou.shape:
                    ious[l] = 0
                else:
                    if boxes_1.shape>boxes_2.shape:
                        max_iou, _ = iou.max(dim=0)
                    else:
                        max_iou, _ = iou.max(dim=1)
                        
                    # Compute the average iou for that label
                    ious[l] = np.mean(np.array(max_iou))


            #Take the average iou for all the labels. If there are no labels, set the iou to 0.
            if len(ious)>0: 
                ious_list.append(np.mean(ious))
            else: 
                ious_list.append(0)
            
        # Print progress
        if i%10 ==0:
            batch_time = time.time()
            speed = (i+1)/(batch_time-start_time)
            print('[%5d] speed: %.2f' %
                  (i, speed))
    
    return  sum(ious_list)/len(ious_list)
    

```

Training is performed on a GPU if possible. Otherwise, it's on a CPU.

```python
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(device)
```

Let's initialize the model and optimizer.

```python
model = get_model_object_detection(len(CLASSES_OF_INTEREST))
model.to(device)

# Specify the optimizer
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                            momentum=0.9, weight_decay=0.0005)
```

Next, we initialize the W\&B run and create the dataloaders for training and validation data. We will log the training loss and validation IOU, as well as other parameters like the transform resolution.

{% hint style="warning" %}
**Creation of the Deep Lake dataloaders is a trigger for the W\&B run to log Deep Lake-related information. Therefore, the the W\&B run should be initialized before dataloader creation.**
{% endhint %}

```python
config={"width": WIDTH, "height": HEIGHT, "min_area": MIN_AREA, "batch_size": BATCH_SIZE}

run = wandb.init(project=WANDB_PROJECT, config = config)

train_loader = ds_train_view.pytorch(num_workers = 8, shuffle = True, 
                          transform = transform_train,
                          tensors = ['images', 'labels', 'boxes'],
                          batch_size = BATCH_SIZE,
                          collate_fn = collate_fn)

val_loader = ds_val_view.pytorch(num_workers = 8, shuffle = False, 
                          transform = transform_val,
                          tensors = ['images', 'labels', 'boxes'],
                          batch_size = BATCH_SIZE,
                          collate_fn = collate_fn,
                          return_index = True)
```

The model and data are ready for training 🚀!

Let's train the model for 8 epochs and save the gradients, parameters, and final trained model as an artifact.

```python
# Train the model for 8 epoch
num_epochs = 8

lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=4, gamma=0.1)
    
wandb.watch(model, log="all", log_freq=50)
wandb.define_metric("epoch")
wandb.define_metric("validation_iou", step_metric="epoch")

for epoch in range(num_epochs):  # loop over the dataset multiple times
    print("------------------ Training Epoch {} ------------------".format(epoch))
    train_one_epoch(model, optimizer, train_loader, device)
    lr_scheduler.step()
    
    print("----------- Evaluating the Model ------------")
    iou = evaluate_iou(model, val_loader, device)
    wandb.log({"epoch": epoch, "validation_iou": iou})

torch.save(model.state_dict(), 'model_weights_wandb.pth')

model_artifact = wandb.Artifact("object_detection_model", "model")
model_artifact.add_file('model_weights_wandb.pth')
run.log_artifact(model_artifact)
run.finish()

print('Finished Training')
```

In the W\&B UI for this run, we see that in addition to the metrics and parameters that are typically logged by W\&B, the Deep Lake integration also logged the dataset `uri`, `commit_id`, and `view_id` for the training and evaluation data, which uniquely identifies all the data that was used in this training project.&#x20;

{% hint style="info" %}
The Deep Lake integration with W\&B logs the dataset `uri`, `commit_id`, and `view_id` in a training run even if a W\&B artifact was not created for the Deep Lake dataset.
{% endhint %}

{% embed url="<https://www.loom.com/share/b4a6ef1596fa45558a8405443a3abc6c>" %}
I
{% endembed %}

### Improving the Model Performance

The average IOU of 0.29 achieved in the previous training run is likely unsatisfactory for a deploying a working product. Two potential explanations for the poor performance are:

* Despite filtering our samples with tiny objects, the dataset still contains fairly small bounding boxes that are difficult to detect by object detection models
* The differences between some objects in a birds-eye view are subtle, even for human perception, such as the `cars` and `vans` in the image below.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/9BRuabB4xBI4TArOUYuy/Subtle_Image.png" alt=""><figcaption></figcaption></figure>

One remedy for both problems is to train models higher-resolution images, so let's increase the resolution of the transformation and examine its effect on model performance. In addition to changing the resolution, we must also scale `MIN_AREA` proportionally to the image area, so that the same bounding boxes are ignored in two training runs.

```python
WIDTH = 320
HEIGHT = 256
MIN_AREA = 128
```

After retraining the model using the same code above, we observe that the average IOU increased from 0.29 to 0.37, which is substantial given the simple increase in image resolution.&#x20;

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/hDSqniWGXIEKwaVMVLYm/WB_Run_Comparison_Chart_Annotated.png" alt=""><figcaption></figcaption></figure>

The model is still not production-ready, and further opportunities for improvement are:

* Assessing model performance on a per-image basis, which helps identify mislabeled or difficult data. A playbook for this workflow is available [here](https://docs-v3.activeloop.ai/examples/dl/playbooks/evaluating-model-performance).
* Adding random real-world images that do not contain the objects of interest. This helps the model eliminate false positives.&#x20;
* Adding more data to the training set. 3000 images is likely not enough for a high-accuracy model.
* Strengthening of transformations that affect image color, blur, warping, and others
* Exploring different optimizers, learning rates, and schedulers
* Further increasing the transform resolution until diminishing returns are achieved

### Notes on GPU Performance

Using W\&B automatic logging of CPU and GPU performance, we observe that the GPU utilization for the training runs on this Tesla V100 GPU was approximately 90%, aside from the dips between epochs when the shuffle buffer was filling. Note that the data was streamed from Activeloop storage (not in AWS) to an AWS SageMaker instance. This is made possible by Deep Lake's efficient data format and high-performance dataloader.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/3kteAnel5Hc6Kwt5TkNl/GPU_Util.png" alt=""><figcaption></figcaption></figure>

#### Congratulations 🚀. You can now use Activeloop Deep Lake and Weights & Biases to experiment and train models will full reproducibility!


# Working with Videos

How manage video datasets and train models using Deep Lake.

## How to manage video datasets and train models using Deep Lake.

Performing deep-learning on video data can be challenging due to the large size of video files, especially when they are uncompressed to raw numeric data that is fed into neural networks. Deep Lake abstracts these challenges away from the user so you can focus on building performant models.

### Setup

{% hint style="info" %}
Make sure to install Deep Lake with `pip install "deeplake[av]"` in order to use Deep Lake's audio and video features.
{% endhint %}

```python
import deeplake
ds = deeplake.empty("demo/video") # create a local dataset
```

### Creating a video tensor

To create a video tensor, we specify an `htype` of "video" and set `sample_compression` to the format of the video.

```python
ds.create_tensor("videos", htype="video", sample_compression="mp4")
```

### Adding video samples

We append videos to the newly created tensor by reading the video files with `deeplake.read`

```python
ds.videos.append(deeplake.read("./videos/example1.mp4"))
ds.videos.append(deeplake.read("./videos/example2.mp4"))
```

`deeplake.read` can also read videos from `http://`, `gcs://` and `s3://` urls given you have the credentials to access them. Examples include:

```python
ds.videos.append(
    deeplake.read(
        "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        creds=None,
    )
)
```

```python
ds.videos.append(
    deeplake.read(
        "s3://bucket-name/sample_video.mp4",
        creds={
            "aws_access_key_id": "...",
            "aws_secret_access_key": "...",
            "aws_session_token": "...",
        },
    )
)
```

{% hint style="info" %}
See [deeplake`.read`](https://api-docs.activeloop.ai/#hub.read) and check out [this notebook](https://colab.research.google.com/drive/10UjDqQ4BiogSluTjF7nUkcfggk1sGi7K?usp=sharing) to see this in action.
{% endhint %}

### Adding annotations

{% hint style="info" %}
See a complete example for this section in [this notebook](https://colab.research.google.com/drive/1z-KYuQWwiFb5Ye-BFm0dCKDbM-o7vsiT?usp=sharing).
{% endhint %}

Annotations like bounding boxes can be added and visualized in Deep Lake along with the video samples. We use tensors of htype `sequence[bbox]` for this purpose. Every sample in a `sequence[bbox]` tensor will be a sequence of bounding boxes which represents the annotations for the corresponding video sample in the `video` tensor.

{% hint style="info" %}
Learn more about sequences [here](https://docs-v3.activeloop.ai/examples/dl/tutorials/creating-datasets/creating-datasets-with-sequences).
{% endhint %}

```python
ds.create_tensor("boxes", htype="sequence[bbox]", coords={"type": "pixel", "mode": "LTWH"})
```

{% hint style="info" %}
See [this page](https://docs-v3.activeloop.ai/examples/dl/playbooks/broken-reference) for more details about the `bbox` htype.
{% endhint %}

Next, here's an example of an annotations file taken from the [LaSOT dataset](https://arxiv.org/abs/1809.07845). It contains annotations for every frame of a video.

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/14XAhCxM77rPzZHdmC63/groundtruth.txt>" %}
Example of an annotations file
{% endfile %}

We convert this to a numpy array and append it to our `boxes` tensor.

```python
import pandas as pd
df = pd.read_csv("groundtruth.txt", header=None)
boxes = df.to_numpy().astype(np.float32)[:, np.newaxis]
# boxes.shape == (2788, 1, 4) == (number of frames, number of boxes, 4)
```

```python
ds.boxes.append(boxes)
```

Visualize the bounding boxes within your notebook using `ds.visualize()`.

{% hint style="warning" %}
The shapes of the samples in the `video` and `sequence[bbox]`tensors have to match in order for visualization to work properly.

If the shape of video tensor is `(# frames, height, width, 3)`, the shape of the sequence tensor should be`(# frames, # of boxes in a frame, 4)`
{% endhint %}

![Visualize video annotations in notebook](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/iOFWOeho6bmEN3UXDJHP/visualize_bounding_box_in_notebook.gif)

### Accessing video metadata

#### Shape

We can get the shape of a video sample in (N, H, W, C) format using

```python
ds.videos[0].shape
```

```python
(400, 360, 640, 3)
```

#### Sample info

Info about a video sample can be accessed using

```python
ds.videos[0].sample_info
```

This returns info about the first sample as a dict:

```python
{
    'duration': 400400,
    'fps': 29.97002997002997,
    'timebase': 3.3333333333333335e-05,
    'shape': [400, 360, 640, 3],
    'format': 'mp4',
    'filename': './videos/example1.mp4',
    'modified': False
}
```

{% hint style="info" %}
`duration` is in units of`timebase`
{% endhint %}

### Accessing video frames

The most important part of working with videos on Deep Lake is retrieving the frames of a video sample as a numpy array.

```python
video = ds.videos[0].numpy()
```

This decompresses the entire first video sample and returns the frames as a numpy array.

```python
print(type(video))
print(video.shape)
```

```python
<class 'numpy.ndarray'>
(400, 360, 640, 3)
```

{% hint style="warning" %}
Be careful when decompressing an entire large video sample because it can blow up your memory.
{% endhint %}

Deep Lake allows you to index the video tensor like a numpy array and return the frames you want. *Only the required frames are decompressed.* See a few examples belo&#x77;*:*

**Getting a 100 frames from index 100 - 200**

```python
# 1st sample, frames 100 - 200
video = ds.videos[1, 100:200].numpy()
video.shape
```

```python
(100, 360, 640, 3)
```

**Indexing with step**

```python
# 0th sample, frames 100 - 200 with step of 5 frames
video = ds.videos[0, 100:200:5].numpy()
video.shape
```

```python
(20, 360, 640, 3)
```

**Getting a single frame**

```python
# 1st sample, last frame
last_frame = ds.videos[1, -1].numpy()
last_frame.shape
```

```python
(360, 640, 3)
```

### Accessing video timestamps

Presentation timestamps (PTS) of frames can be obtained (in seconds) through a video tensor's `.timestamp` attribute after indexing it just like in the previous section:

```python
# timestamps of frames 10 - 15 of 0th sample
ds.videos[0, 10:15].timestamp
```

```python
array([0.36703333, 0.4004    , 0.43376666, 0.46713334, 0.5005    ],
      dtype=float32)
```

#### `.data()`

Calling `ds.videos[index].data()` will return a dict with keys 'frames' and 'timestamps' with the corresponding numpy arrays as values. Indexing works the same way as it does with `.numpy()`.

```python
data = ds.videos[1, 15:20].data()
data['frames'].shape
data['timestamps']
```

```python
(5, 360, 640, 3)
array([0.5005    , 0.5672333 , 0.6006    , 0.6339667 , 0.76743335],
      dtype=float32)
```

### Visualizing videos

#### `.play()`

Individual video samples can be instantly visualized by calling `.play()` on them:

```python
ds.videos[1].play()
```

This will play the video on your web browser:

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/iHDzJI9gA3RdPeOeDATC/playback.png)

![video playback in browser](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/dI77oaHVDc79C61YgGgF/local_playback.png)

On a jupyter notebook this will look like:

![video playback on jupyter notebook](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/8iIpDZqoT7rJOYWn8hzB/video_playback_in_notebook.png)

{% hint style="info" %}
*This feature is not yet supported on colab*
{% endhint %}

#### `ds.visualize()`

The whole Deep Lake dataset can be visualized by calling `.visualize()` on your dataset in a jupyter or colab notebook.

```
ds.visualize()
```

![ds.visualize() on colab](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/ikrvJZCVQ4NAWldoudYT/visualize_video_dataset_in_notebook.png)

Try this out for yourself [here](https://colab.research.google.com/drive/1xyhi31ZPLOcOIYAbjobfyn_X2BgwKQeY?usp=sharing)!

{% hint style="info" %}
On colab, we only support visualizing `hub://`datasets
{% endhint %}

### Linked videos

Tensors of Deep Lake type `link[video]` can be used to store links to videos. All of the above features are supported for linked videos. `https://`, `gcs://`, `s3://`and `gdrive://`links are accepted.

```python
# create linked tensor
links = ds.create_tensor("video_links", htype="link[video]")

# append linked samples
links.append(deeplake.link("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4", creds_key=None)) # link to public video

# .numpy()
video = links[0].numpy()

# shape of numpy array
video.shape
```

```python
(360, 720, 1280, 3)
```

You will need to set credentials to link to private data on your S3 or GCS.

#### For Activeloop cloud datasets

This proccess is easy and streamlined for `deeplake://` datasets.

* First, go to your [Activeloop platform](https://app.activeloop.ai), login and choose 'Managed credentials' in settings.
* And then choose 'Add Credentials'.
* Select a credentials provider, set the credentials name (say, 'MY\_KEY'), fill the fields and save it.
* Done! Your credentials have now been set.

#### Add managed credentials to your dataset

Use `ds.add_creds_key` with `managed` set to True to add the credentials to your dataset. Multiple credentials can be added.

```python
ds.add_creds_key("MY_KEY", managed=True)
ds.add_creds_key("S3_KEY", managed=True)
```

#### Use credentials

And when adding linked data using `deeplake.link`, simply mention which credentials to use through the `creds_key` argument.

```python
ds.links.append(deeplake.link("s3://my-bucket/sample-video.mp4", creds_key="MY_KEY"))
```

#### For non Activeloop cloud datasets

For non-`hub://` datasets, you can use credentials set in your environment by mentioning `creds_key="ENV"`

```python
ds.links.append(deeplake.link("s3://my-bucket/sample-video.mp4", creds_key="ENV"))
```

Or you can temporarily add creds to your dataset

```python
creds={
        "aws_access_key_id": "...",
        "aws_secret_access_key": "...",
        "aws_session_token": "...",
    }

# add creds key (Note that managed is False)
ds.add_creds_key("TEMP_KEY")

# populate creds with a credentials dict
ds.populate_creds("TEMP_KEY", creds)
```

and then

```python
ds.links.append(deeplake.link("s3://my-bucket/sample-video.mp4", creds_key="TEMP_KEY"))
```

{% hint style="info" %}
See [deeplake`.link`](https://api-docs.activeloop.ai/#hub.link)
{% endhint %}

### Video streaming

{% hint style="info" %}
This section describes some implementation details regarding how video data is fetched and decompressed in Deep Lake.
{% endhint %}

Large video samples (> 16MB by default) stored in remote Deep Lake datasets are not downloaded in their entirety on calling `.numpy()`. Instead, they are streamed from storage. Only the required packets are decompressed and converted to numpy arrays based on how the tensor is indexed.

`.play()`also streams videos from storage.


# Deep Lake Dataloaders

Overview of Deep Lake's dataloader built and optimized in C++

## How to use Deep Lake's Dataloaders for Training Models

Deep Lake offers an optimized dataloader implementation built in C++, [which is 1.5-3X faster than the pure-python implementation](https://docs-v3.activeloop.ai/technical-details/best-practices/training-models-at-scale), and it supports distributed training. The C++ and Python dataloaders can be used interchangeably, and their syntax varies as shown below.&#x20;

The Deep Lake Compute Engine is only accessible to registered and authenticated users, and it applies usage restrictions based on your Deep Lake Plan.

### Pure-Python Dataloader

```python
train_loader = ds_train.pytorch(num_workers = 8,
                                transform = transform, 
                                batch_size = 32,
                                tensors=['images', 'labels'],
                                shuffle = True)
```

### C++ Dataloader

{% hint style="danger" %}
The C++ dataloader is only accessible to registered and authenticated users.
{% endhint %}

The Deep Lake query engine is only accessible to registered and authenticated users, and it applies usage restrictions based on your Deep Lake Plan.

#### PyTorch (returns PyTorch Dataloader)

<pre class="language-python"><code class="lang-python"><strong>train_loader = ds.dataloader()\
</strong>                 .transform(transform)\
                 .batch(32)\
                 .shuffle(True)\
                 .offset(10000)\
                 .pytorch(tensors=['images', 'labels'], num_workers = 8)
</code></pre>

#### TensorFlow

```
train_loader = ds.dataloader()\
                 .transform(transform)\
                 .batch(32)\
                 .shuffle(True)\
                 .offset(10000)\
                 .tensorflow(tensors=['images', 'labels'], num_workers = 8)
```

### Further Information

{% content-ref url="tutorials/training-models" %}
[training-models](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models)
{% endcontent-ref %}

{% content-ref url="playbooks/training-reproducibility-wandb" %}
[training-reproducibility-wandb](https://docs-v3.activeloop.ai/examples/dl/playbooks/training-reproducibility-wandb)
{% endcontent-ref %}


# API Summary

Summary of the most important low-level Deep Lake commands.

## Deep Lake Low-Level API Basics

### Import and Installation

**By default, Deep Lake does not install dependencies for audio, video, google-cloud, and other features.** [**Details on installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.**&#x20;

```python
!pip3 install deeplake

import deeplake
```

### Loading Deep Lake Datasets

Deep Lake datasets can be stored at a [variety of storage locations](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options) using the appropriate `dataset_path` parameter below. We support S3, GCS, Activeloop storage, and are constantly adding to the list.

```python
# Load a Deep Lake Dataset
ds = deeplake.load(<dataset_path>, creds = {'optional'}, token = 'optional')
```

### Creating Deep Lake Datasets

```python
# Create an empty Deep Lake dataset
ds = deeplake.empty('dataset_path', creds = {'optional'}, token = 'optional')

# Create an Deep Lake Dataset with the same tensors as another dataset
ds = deeplake.like(<new_dataset_path>, ds_object or <dataset_path>, creds = {'optional'})

# Automatically create a Deep Lake Dataset from another data source
ds = deeplake.ingest(<source_folder>, <deeplake_dataset_path>, ... 'see API reference for details')
ds = deeplake.ingest_coco(<images_folder>, 'annotations.json', <dataset_path>, ... 'see API reference for details')
ds = deeplake.ingest_yolo(<data_directory>, <dataset_path>, class_names_file, ... 'see API reference for details')
```

### Deleting Datasets

```python
ds.delete()

deeplake.delete(<dataset_path>, creds = {'optional'})
```

{% hint style="warning" %}
API deletions of Deep Lake Cloud datasets are immediate, whereas UI-initiated deletions are postponed by 5 minutes. Once deleted, dataset names can't be reused in the Deep Lake Cloud.
{% endhint %}

### Creating Tensors

```python
# Specifying htype is recommended for maximizing performance.
ds.create_tensor('my_tensor', htype = 'bbox')

# Specifiying the correct compression is critical for images, videos, audio and 
# other rich data types. 
ds.create_tensor('songs', htype = 'audio', sample_compression = 'mp3')
```

### Creating Tensor Hierarchies

```python
ds.create_group('my_group')
ds.my_group.create_tensor('my_tensor')
ds.create_tensor('my_group/my_tensor') #Automatically creates the group 'my_group'
```

### Visualizing and Inspecting Datasets

```python
ds.visualize()

ds.summary()
```

### Appending Data to Datasets

```python
ds.append({'tensor_1': np.ones((1,4)), 'tensor_2': deeplake.read('image.jpg')})
ds.my_group.append({'tensor_1': np.ones((1,4)), 'tensor_2': deeplake.read('image.jpg')})
```

### Appending/Updating Data in Individual Tensors

```python
# Append a single sample
ds.my_tensor.append(np.ones((1,4)))
ds.my_tensor.append(deeplake.read('image.jpg'))

# Append multiple samples. The first axis in the 
# numpy array is assumed to be the sample axis for the tensor
ds.my_tensor.extend(np.ones((5,1,4)))

# Editing or adding data at a specific index
ds.my_tensor[i] = deeplake.read('image.jpg')
```

### Deleting data

```python
# Removing samples by index
ds.pop[i]

# Delete all data in a tensor
ds.<tensor_name>.clear()

# Delete tensor and all of its data
ds.delete_tensor(<tensor_name>)
```

### Appending Empty Samples or Skipping Samples

```python
# Data appended as None will be returned as an empty array
ds.append('tensor_1': deeplake.read(...), 'tensor_2': None)
ds.my_tensor.append(None)

# Empty arrays can be explicitly appended if the length of the shape 
# of the empty array matches that of the other samples
ds.boxes.append(np.zeros((0,4))
```

### Accessing Tensor Data

```python
# Read the i-th tensor sample
np_array = ds.my_tensor[i].numpy()
text = ds.my_text_tensor[i].data() # More comprehensive view of the data
bytes = ds.my_tensor[i].tobytes() # More comprehensive view of the data

# Read the i-th dataset sample as a numpy array
image = ds[i].images.numpy()

# Read the i-th labels as a numpy array or list of strings
labels_array = ds.labels[i].numpy()
labels_array = ds.labels[i].data()['value'] # same as .numpy()
labels_string_list = ds.labels[i].data()['text']


# Read a tensor sample from a hierarchical group
np_array = ds.my_group.my_tensor_1[i].numpy()
np_array = ds.my_group.my_tensor_2[i].numpy()

# Read multiple tensor samples into numpy array
np_array = ds.my_tensor[0:10].numpy() 

# Read multiple tensor samples into a list of numpy arrays
np_array_list = ds.my_tensor[0:10].numpy(aslist=True)
```

### Maximizing performance

Make sure to [use the `with` context](https://docs-v3.activeloop.ai/technical-details/best-practices/storage-synchronization) when making any updates to datasets.&#x20;

```python
with ds:

    ds.create_tensor('my_tensor')
    
    for i in range(10):
        ds.my_tensor.append(i)
```

### Connecting Deep Lake Datasets to ML Frameworks

```python
# PyTorch Dataloader
dataloader = ds.pytorch(batch_size = 16, transform = {'images': torchvision_tform, 'labels': None}, num_workers = 2, scheduler = 'threaded')

# TensorFlow Dataset
ds_tensorflow = ds.tensorflow()

# Enterprise Dataloader
dataloader = ds.dataloader().batch(batch_size = 64).pytorch(num_workers = 8)
```

### Versioning Datasets

```python
# Commit data
commit_id = ds.commit('Added 100 images of trucks')

# Print the commit log
log = ds.log()

# Checkout a branch or commit 
ds.checkout('branch_name' or commit_id)

# Create a new branch
ds.checkout('new_branch', create = True)

# Examine differences between commits
ds.diff()

# Delete all changes since the previous commit
ds.reset()

# Delete a branch and its commits - Only allowed for branches that have not been merged
ds.delete_branch('branch_name')
```

### Querying Datasets and Saving Dataset Views

A full list of [supported queries](https://docs-v3.activeloop.ai/examples/tql/syntax) is shown here.&#x20;

```python
view = ds.query("Select * where contains(labels, 'giraffe')")

view.save_view(optimize = True)

view = ds.load_view(id = 'query_id')

# Return the original dataset indices that satisfied the query condition
indices = list(view.sample_indices)
```

### Adding Tensor and Dataset-Level Metadata

```python
# Add or update dataset metadata
ds.info.update(key1 = 'text', key2 = number)
# Also can run ds.info.update({'key1'='value1', 'key2' = num_value})

# Add or update tensor metadata
ds.my_tensor.info.update(key1 = 'text', key2 = number)

# Delete metadata
ds.info.delete() #Delete all metadata
ds.info.delete('key1') #Delete 1 key in metadata
```

### Copying datasets

<pre class="language-python"><code class="lang-python"><strong># Fastest option - copies everything including version history
</strong><strong>ds = deeplake.deepcopy('src_dataset_path', 'dest_dataset_path', src_creds, dest_creds)
</strong>
# Slower option - copies only data on the last commit
ds = deeplake.copy('src_dataset_path', 'dest_dataset_path', src_creds, dest_creds)
</code></pre>

### Advanced

```python
# Load a Deep Lake Dataset if it already exists (same as deeplake.load), or initialize 
# a new Deep Lake Dataset if it does not already exist (same as deeplake.empty)
ds = deeplake.dataset('dataset_path', creds = {'optional'}, token = 'optional')


# Append multiple samples using a list
ds.my_tensor.extend([np.ones((1,4)), np.ones((3,4)), np.ones((2,4)


# Fetch adjacent data in the chunk -> Increases speed when loading 
# sequantially or if a tensor's data fits in the cache.
numeric_label = ds.labels[i].numpy(fetch_chunks = True)
```


# RAG

Using Deep Lake for Vector Store in RAG applications.

## Deep Lake as a Vector Store for LLM Applications

* Store and search embeddings and their metadata including text, jsons, images, audio, video, and more. Save the data locally, in your cloud, or on Deep Lake storage.
* Build Retrieval Augmented Generation (RAG) Apps using our integrations with [LangChain](https://docs-v3.activeloop.ai/examples/rag/langchain-integration) and [LlamaIndex](https://docs-v3.activeloop.ai/examples/rag/llamaindex-integration)
* Run computations locally or on our [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database)


# RAG Quickstart

A jump-start guide to using Deep Lake for Vector Search.

## How to Get Started with Vector Search in Deep Lake in Under 5 Minutes

{% hint style="success" %}
**If you prefer to use higher level wrappers, please check out our** [**LangChain**](https://docs-v3.activeloop.ai/examples/rag/langchain-integration) **or** [**LlamaIndex**](https://docs-v3.activeloop.ai/examples/rag/llamaindex-integration) **tutorials. This Quickstart focuses on vector storage and search, instead of end-2-end LLM apps, and it offers more customization and search options compared to other wrappers.**
{% endhint %}

### Installing Deep Lake

Deep Lake can be installed using pip. **By default, Deep Lake does not install dependencies for google-cloud, video support, and other features.** [**Details on all installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.** This quickstart also requires OpenAI.

```bash
!pip3 install deeplake
!pip3 install openai
```

### Creating Your First Vector Store

Let's embed and store one of [Paul Graham's essays](http://www.paulgraham.com/articles.html) in a Deep Lake Vector Store stored locally. First, we download the data:

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/AxmArlLLOi8FLy7DNc1a/paul_graham_essay.txt>" %}

Next, let's import the required modules and set the OpenAI environmental variables for embeddings:

```python
from deeplake.core.vectorstore import VectorStore
import openai
import os

os.environ['OPENAI_API_KEY'] = <OPENAI_API_KEY>
```

Next, lets specify paths for the source text and the Deep Lake Vector Store. Though we store the Vector Store locally, Deep Lake Vectors Stores can also be created in memory, in the Deep Lake [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database), or in your cloud. [Further details on storage options are available here](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options).&#x20;

Let's also read and chunk the essay text based on a constant number of characters.&#x20;

```python
source_text = 'paul_graham_essay.txt'
vector_store_path = 'pg_essay_deeplake'

with open(source_text, 'r') as f:
    text = f.read()

CHUNK_SIZE = 1000
chunked_text = [text[i:i+CHUNK_SIZE] for i in range(0,len(text), CHUNK_SIZE)]
```

Next, let's define an embedding function using OpenAI. It must work for a single string and a list of strings, so that it can both be used to embed a prompt and a batch of texts.&#x20;

```python
def embedding_function(texts, model="text-embedding-ada-002"):
   
   if isinstance(texts, str):
       texts = [texts]

   texts = [t.replace("\n", " ") for t in texts]
   
   return [data.embedding for data in openai.embeddings.create(input = texts, model=model).data]
```

Finally, let's create the Deep Lake Vector Store and populate it with data. We use a default tensor configuration, which creates tensors with `text (str)`, `metadata(json)`, `id (str, auto-populated)`, `embedding (float32)`. [Learn more about tensor customizability here.](https://docs-v3.activeloop.ai/examples/rag/tutorials/step-4-customizing-vector-stores)&#x20;

<pre class="language-python"><code class="lang-python"><strong>vector_store = VectorStore(
</strong>    path = vector_store_path,
)

vector_store.add(text = chunked_text, 
                 embedding_function = embedding_function, 
                 embedding_data = chunked_text, 
                 metadata = [{"source": source_text}]*len(chunked_text))
</code></pre>

{% hint style="info" %}
The `path` parameter is bi-directional:

* When a new `path` is specified, a new Vector Store is created
* When an existing path is specified, the existing Vector Store is loaded
  {% endhint %}

The Vector Store's data structure can be summarized using `vector_store.summary()`, which shows 4 tensors with 76 samples:

```
  tensor      htype      shape      dtype  compression
  -------    -------    -------    -------  ------- 
 embedding  embedding  (76, 1536)  float32   None   
    id        text      (76, 1)      str     None   
 metadata     json      (76, 1)      str     None   
   text       text      (76, 1)      str     None   
```

To create a vector store using pre-compute embeddings instead of the `embedding_data` and `embedding_function`, you may run

```python
# vector_store.add(text = chunked_text, 
#                  embedding = <list_of_embeddings>, 
#                  metadata = [{"source": source_text}]*len(chunked_text))
```

### Performing Vector Search&#x20;

Deep Lake offers highly-flexible vector search and hybrid search options [discussed in detail in these tutorials](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options). In this Quickstart, we show a simple example of vector search using default options, which performs cosine similarity search in Python on the client.&#x20;

```python
prompt = "What are the first programs he tried writing?"

search_results = vector_store.search(embedding_data=prompt, embedding_function=embedding_function)
```

The `search_results` is a dictionary with keys for the `text`, `score`, `id`, and `metadata`, with data ordered by score. If we examine the first returned text using `search_results['text'][0]`, it appears to contain the answer to the prompt.

```
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in
```

### Visualizing your Vector Store

Visualization is available for Vector Stores stored in or connected to Deep Lake. The vector store above is stored locally, so it cannot be visualized, but [here's an example of visualization for a representative Vector Store.](https://app.activeloop.ai/activeloop/twitter-algorithm)&#x20;

### Authentication

To use Deep Lake features that require authentication (Deep Lake storage, Tensor Database storage, connecting your cloud dataset to the Deep Lake UI, etc.) you should [register in the Deep Lake App](https://app.activeloop.ai/register/) and authenticate on the client using the methods in the link below:

#### Environmental Variable

Set the environmental variable `ACTIVELOOP_TOKEN` to your API token. In Python, this can be done using:

`os.environ['ACTIVELOOP_TOKEN'] = <your_token>`

#### Pass the Token to Individual Methods

You can pass your API token to individual methods that require authentication such as:

`ds = VectorStore('hub://org_name/dataset_name', token = <your_token>)`

### Creating Vector Stores in the Deep Lake Managed Tensor Database

Deep Lake provides [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) that stores and runs queries on Deep Lake infrastructure, instead of the client. To use this service, specify `runtime = {"tensor_db": True}` when creating the Vector Store.

```python
# vector_store = VectorStore(
#     path = vector_store_path,
#     runtime = {"tensor_db": True}
# )

# vector_store.add(text = chunked_text, 
#                  embedding_function = embedding_function, 
#                  embedding_data = chunked_text, 
#                  metadata = [{"source": source_text}]*len(chunked_text))
                 
# search_results = vector_store.search(embedding_data = prompt, 
#                                      embedding_function = embedding_function)
```

### Next Steps

Check out our [Getting Started Guide](https://docs-v3.activeloop.ai/examples/rag/broken-reference) for a comprehensive walk-through of Deep Lake Vector Stores. For scaling Deep Lake to production-level applications, check out our [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) and [Support for Concurrent Writes](https://docs-v3.activeloop.ai/technical-details/best-practices/concurrent-writes).

Congratulations, you've created a Vector Store and performed vector search using Deep Lake:nerd:&#x20;


# RAG Tutorials

Tutorials for using Deep Lake in Vector Store applications

## How to use Deep Lake as a Vector Store for LLM applications

Deep Lake can be used as a Vector Store for storing embeddings and their metadata including text, jsons, images, audio, video, and more. Its serverless architecture can be self-hosted, and it is also available via [fully managed service](https://docs-v3.activeloop.ai/examples/rag/managed-database).&#x20;

### RAG Tutorials:

{% content-ref url="tutorials/vector-store-basics" %}
[vector-store-basics](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-store-basics)
{% endcontent-ref %}

{% content-ref url="langchain-integration" %}
[langchain-integration](https://docs-v3.activeloop.ai/examples/rag/langchain-integration)
{% endcontent-ref %}

{% content-ref url="llamaindex-integration" %}
[llamaindex-integration](https://docs-v3.activeloop.ai/examples/rag/llamaindex-integration)
{% endcontent-ref %}

{% content-ref url="tutorials/vector-search-options" %}
[vector-search-options](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options)
{% endcontent-ref %}

{% content-ref url="tutorials/image-similarity-search" %}
[image-similarity-search](https://docs-v3.activeloop.ai/examples/rag/tutorials/image-similarity-search)
{% endcontent-ref %}

{% content-ref url="managed-database" %}
[managed-database](https://docs-v3.activeloop.ai/examples/rag/managed-database)
{% endcontent-ref %}

{% content-ref url="tutorials/deepmemory" %}
[deepmemory](https://docs-v3.activeloop.ai/examples/rag/tutorials/deepmemory)
{% endcontent-ref %}


# Vector Store Basics

Creating the Deep Lake Vector Store

## How to Create a Deep Lake Vector Store

Let's create a Vector Store in LangChain for storing and searching information about the [Twitter OSS recommendation algorithm](https://github.com/twitter/the-algorithm).

### Downloading and Preprocessing the Data

First, let's import necessary packages and **make sure the Activeloop and OpenAI keys are in the environmental variables `ACTIVELOOP_TOKEN`, `OPENAI_API_KEY`.**

```python
from deeplake.core.vectorstore import VectorStore
import openai
import os
```

Next, let's clone the Twitter OSS recommendation algorithm and define paths for for source data and the Vector Store.

```bash
!git clone https://github.com/twitter/the-algorithm
```

```python
vector_store_path = '/vector_store_getting_started'
repo_path = '/the-algorithm'
```

Next, let's load all the files from the repo into list of data that will be added to the Vector Store (`chunked_text` and `metadata`). We use simple text chunking based on a constant number of characters.&#x20;

```python
CHUNK_SIZE = 1000

chunked_text = []
metadata = []
for dirpath, dirnames, filenames in os.walk(repo_path):
    for file in filenames:
        try: 
            full_path = os.path.join(dirpath,file)
            with open(full_path, 'r') as f:
               text = f.read()
            new_chunkned_text = [text[i:i+CHUNK_SIZE] for i in range(0,len(text), CHUNK_SIZE)]
            chunked_text += new_chunkned_text
            metadata += [{'filepath': full_path} for i in range(len(new_chunkned_text))]
        except Exception as e: 
            print(e)
            pass
```

Next, let's define an embedding function using OpenAI. It must work for a single string and a list of strings, so that it can both be used to embed a prompt and a batch of texts.&#x20;

```python
def embedding_function(texts, model="text-embedding-ada-002"):
   
   if isinstance(texts, str):
       texts = [texts]

   texts = [t.replace("\n", " ") for t in texts]
   
   return [data.embedding for data in openai.embeddings.create(input = texts, model=model).data]
```

Finally, let's create the Deep Lake Vector Store and populate it with data. We use a default tensor configuration, which creates tensors with `text (str)`, `metadata(json)`, `id (str, auto-populated)`, `embedding (float32)`. [Learn more about tensor customizability here](https://docs-v3.activeloop.ai/examples/rag/tutorials/step-4-customizing-vector-stores).&#x20;

```python
vector_store = VectorStore(
    path = vector_store_path,
)

vector_store.add(text = chunked_text, 
                 embedding_function = embedding_function, 
                 embedding_data = chunked_text, 
                 metadata = metadata
)
```

The Vector Store's data structure can be summarized using `vector_store.summary()`, which shows 4 tensors with 21055 samples:

```
  tensor      htype        shape       dtype  compression
  -------    -------      -------     -------  ------- 
 embedding  embedding  (21055, 1536)  float32   None   
    id        text      (21055, 1)      str     None   
 metadata     json      (21055, 1)      str     None   
   text       text      (21055, 1)      str     None   
```

To create a vector store using pre-compute embeddings, instead of  `embedding_data` and `embedding_function`, you may run:

```python
# vector_store.add(text = chunked_text, 
#                  embedding = <list_of_embeddings>, 
#                  metadata = [{"source": source_text}]*len(chunked_text))
```

### Performing Vector Search&#x20;

Deep Lake offers highly-flexible vector search and hybrid search options. First, let's show a simple example of vector search using default options, which performs simple cosine similarity search in Python on the client (your machine).&#x20;

```python
prompt = "What do trust and safety models do?"

search_results = vector_store.search(embedding_data=prompt, embedding_function=embedding_function)
```

The `search_results` is a dictionary with keys for the `text`, `score`, `id`, and `metadata`, with data ordered by score. By default, the search returns the top 4 results which can be verified using:&#x20;

```python
len(search_results['text']) 

# Returns 4
```

If we examine the first returned text, it appears to contain the text about trust and safety models that is relevant to the prompt.

```python
search_results['text'][0]
```

Returns:

```
Trust and Safety Models
=======================

We decided to open source the training code of the following models:
- pNSFWMedia: Model to detect tweets with NSFW images. This includes adult and porn content.
- pNSFWText: Model to detect tweets with NSFW text, adult/sexual topics.
- pToxicity: Model to detect toxic tweets. Toxicity includes marginal content like insults and certain types of harassment. Toxic content does not violate Twitter's terms of service.
- pAbuse: Model to detect abusive content. This includes violations of Twitter's terms of service, including hate speech, targeted harassment and abusive behavior.

We have several more models and rules that we are not going to open source at this time because of the adversarial nature of this area. The team is considering open sourcing more models going forward and will keep the community posted accordingly.
```

We can also retrieve the corresponding filename from the metadata, which shows the top result came from the README.

```python
search_results['metadata'][0]

# Returns: {'filepath': '/the-algorithm/trust_and_safety_models/README.md'}
```

### Customization of Vector Search&#x20;

You can customize your vector search with simple parameters, such as selecting the `distance_metric` and top `k` results:

```python
search_results = vector_store.search(embedding_data=prompt, 
                                     embedding_function=embedding_functiondding, 
                                     k=10,
                                     distance_metric='l2')
```

The search now returns 10 search results:

```python
len(search_results['text']) 

# Returns: 10
```

The first search result with the `L2` distance metric returns the same text as the previous `Cos` search:

```python
search_results['text'][0]
```

Returns:

```
Trust and Safety Models
=======================

We decided to open source the training code of the following models:
- pNSFWMedia: Model to detect tweets with NSFW images. This includes adult and porn content.
- pNSFWText: Model to detect tweets with NSFW text, adult/sexual topics.
- pToxicity: Model to detect toxic tweets. Toxicity includes marginal content like insults and certain types of harassment. Toxic content does not violate Twitter's terms of service.
- pAbuse: Model to detect abusive content. This includes violations of Twitter's terms of service, including hate speech, targeted harassment and abusive behavior.

We have several more models and rules that we are not going to open source at this time because of the adversarial nature of this area. The team is considering open sourcing more models going forward and will keep the community posted accordingly.
```

### Full Customization of Vector Search&#x20;

Deep Lake's [Compute Engine](https://docs-v3.activeloop.ai/examples/rag/tutorials/broken-reference) can be used to rapidly execute a variety of different search logic. It is available with `!pip install "deeplake[enterprise]"` (Make sure to restart your kernel after installation), and it is only available for data stored in or [connected to](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials) Deep Lake.&#x20;

Let's load a representative Vector Store that is already stored in  [Deep Lake Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database). If data is not being written, is advisable to use `read_only = True`.

```python
vector_store = VectorStore(
    path = "hub://activeloop/twitter-algorithm",
    read_only=True
)
```

The query should be constructed using the [Tensor Query Language (TQL)](https://docs-v3.activeloop.ai/examples/tql) syntax.

```python
prompt = "What do trust and safety models do?"

embedding = embedding_function(prompt)[0]

# Format the embedding array or list as a string, so it can be passed in the REST API request.
embedding_string = ",".join([str(item) for item in embedding])

tql_query = f"select * from (select text, cosine_similarity(embedding, ARRAY[{embedding_string}]) as score) order by score desc limit 5"
```

Let's run the query, noting that the query execution happens in the Managed Tensor Database, and not on the client.

```python
search_results = vector_store.search(query=tql_query)
```

If we examine the first returned text, it appears to contain the same text about trust and safety models that is relevant to the prompt.

```python
search_results['text'][0]
```

Returns:

```
Trust and Safety Models
=======================

We decided to open source the training code of the following models:
- pNSFWMedia: Model to detect tweets with NSFW images. This includes adult and porn content.
- pNSFWText: Model to detect tweets with NSFW text, adult/sexual topics.
- pToxicity: Model to detect toxic tweets. Toxicity includes marginal content like insults and certain types of harassment. Toxic content does not violate Twitter's terms of service.
- pAbuse: Model to detect abusive content. This includes violations of Twitter's terms of service, including hate speech, targeted harassment and abusive behavior.

We have several more models and rules that we are not going to open source at this time because of the adversarial nature of this area. The team is considering open sourcing more models going forward and will keep the community posted accordingly.
```

We can also retrieve the corresponding filename from the metadata, which shows the top result came from the README.

```python
print(search_results['metadata'][0])

# Returns {'filepath': '/Users/istranic/ActiveloopCode/the-algorithm/trust_and_safety_models/README.md', 'extension': '.md'}
```

#### [Deep Lake also offers a variety of search options](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options) depending on where data is stored (load, cloud, Deep Lake storage, etc.) and where query execution should take place (client side or server side)


# Vector Search Options

Overview of Vector Search Options in Deep Lake

## Overview of Vector Search Options in Deep Lake

Deep Lake offers a variety of vector search options depending on the [Storage Location](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options) of the Vector Store and infrastructure that should run the computations.

| Storage Location                                                                                                         | Compute Location | Execution Algorithm       |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------- |
| In memory or local                                                                                                       | Client-side      | Deep Lake OSS Python Code |
| User cloud ([must be connected to Deep Lake](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials)) | Client-side      | Deep Lake C++             |
| Deep Lake Storage                                                                                                        | Client-side      | Deep Lake C++             |
| Deep Lake Managed Tensor Database                                                                                        | Managed Database | Deep Lake C++             |

### APIs for Search

Vector search can occur via a variety of APIs in Deep Lake. They are explained in the links below:

{% content-ref url="vector-search-options/vector-store-api" %}
[vector-store-api](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options/vector-store-api)
{% endcontent-ref %}

{% content-ref url="vector-search-options/rest-api" %}
[rest-api](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options/rest-api)
{% endcontent-ref %}

{% content-ref url="vector-search-options/langchain-api" %}
[langchain-api](https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options/langchain-api)
{% endcontent-ref %}

### Overview of Options for Search Computation Execution

The optimal option for search execution is automatically selected based on the Vector Stores storage location. The different computation options are explained below.

#### Python (Client-Side)

Deep Lake OSS offers query execution logic that run on the client (your machine) using OSS code in Python. This compute logic is accessible in all Deep Lake Python APIs and is available for Vector Stores stored in any location. See individual APIs below for details.&#x20;

#### Compute Engine (Client-Side)

Deep Lake Compute Engine offers query execution logic that run on the client (your machine) using C++ Code that is called via Python API. This compute logic is accessible in all Deep Lake Python APIs and is only available for Vector Stores stored Deep Lake storage or in user clouds [connected to Deep Lake](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials). See individual APIs below for details.&#x20;

To run queries using Compute Engine, make sure to `!pip install "deeplake[enterprise]"`.

#### Managed Tensor Database (Server-Side Running Compute Engine)

Deep Lake offers a Managed Tensor Database that executes queries on Deep Lake infrastructure while running Compute Engine under-the-hood. This compute logic is accessible in all Deep Lake Python APIs and is only available for Vector Stores stored in the Deep Lake Managed Tensor Database. See individual APIs below for details.&#x20;


# LangChain API

Vector Search using Deep Lake in LangChain

## How to Execute Vector Search Using Deep Lake in LangChain

This tutorial requires installation of:

```bash
!pip3 install langchain deeplake openai tiktoken
```

Let's load the same vector store used in the Quickstart and run embeddings search based on a user prompt using the LangChain API.&#x20;

<pre class="language-python"><code class="lang-python">from langchain.vectorstores import DeepLake
<strong>from langchain.chains import RetrievalQA
</strong>from langchain.llms import OpenAIChat
from langchain.embeddings.openai import OpenAIEmbeddings
import os

os.environ['OPENAI_API_KEY'] = &#x3C;OPENAI_API_KEY>

vector_store_path = 'hub://activeloop/paul_graham_essay'

embedding_function = OpenAIEmbeddings(model = 'text-embedding-ada-002')

# Re-load the vector store
db = DeepLake(dataset_path = vector_store_path, 
              embedding = embedding_function, 
              read_only = True)

qa = RetrievalQA.from_chain_type(llm=OpenAIChat(model = 'gpt-3.5-turbo'), 
                                 chain_type = 'stuff', 
                                 retriever = db.as_retriever())
</code></pre>

### Vector Similarity Search

Let's run a similarity search on Paul Graham's essay based on a query we want to answer. The query is embedded and a similarity search is performed against the stored embeddings, with execution taking place on the client.

```python
prompt = 'What are the first programs he tried writing?'

query_docs = db.similarity_search(query = prompt)
```

If we print the first document using query\_docs`[0].page_content`, it appears to be relevant to the query:

```python
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.
```

### Vector Search in an LLM Context

We can directly use LangChain to run a Q\&A using an LLM and answer the question about Paul Graham's essay. Internally, this API performs an embedding search to find the most relevant data to feeds them into the LLM context.

```python
qa = RetrievalQA.from_chain_type(llm = OpenAIChat(model = 'gpt-3.5-turbo'), 
                                 chain_type = 'stuff', 
                                 retriever = db.as_retriever())

qa.run(prompt)
```

`'The first programs he tried writing were on the IBM 1401 that his school district used for "data processing" in 9th grade.'`

### Vector Search Using the Managed Tensor Database

For Vector Stores in the [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database), queries will automatically execute on the database (instead of the client). Vector Stores are created in the Managed Tensor Database by specifying `vector_store_path = hub://org_id/dataset_name` and `runtime = {"tensor_db": True}` during Vector Store creation.

```python
# db = DeepLake(dataset_path = "hub://<org_id>/<dataset_name>", 
#               runtime = {"tensor_db": True},
#               embedding = embedding_function
#              )
```

If Vector Stores are not in the Managed Tensor Database, [they can be migrated using these steps](https://docs-v3.activeloop.ai/examples/rag/managed-database/migrating-datasets-to-the-tensor-database):


# Deep Lake Vector Store API

Running Vector Search in the Deep Lake Vector Store module.

## Search Options for Deep Lake Vector Stores in the Deep Lake API

This tutorial requires installation of:

```bash
!pip3 install "deeplake[enterprise]" langchain openai tiktoken
```

### Vector Search on the Client

Let's load the same vector store used in the Quickstart and run embeddings search based on a user prompt using the Deep Lake Vector Store module. (Note: `DeepLakeVectorStore` class is deprecated, but you can still use it. The new API for calling Deep Lake's Vector Store is: `VectorStore`)

```python
from deeplake.core.vectorstore import VectorStore
import openai
import os

os.environ['OPENAI_API_KEY'] = <OPENAI_API_KEY>

vector_store_path = 'hub://activeloop/paul_graham_essay'

vector_store = VectorStore(
    path = vector_store_path,
    read_only = True
)
```

Next, let's define an embedding function using OpenAI. It must work for a single string and a list of strings so that it can be used to embed a prompt and a batch of texts.&#x20;

```python
def embedding_function(texts, model = "text-embedding-ada-002"):
   
   if isinstance(texts, str):
       texts = [texts]

   texts = [t.replace("\n", " ") for t in texts]
   return [data['embedding']for data in openai.Embedding.create(input = texts, model=model)['data']]
```

#### Simple Vector Search

Let's run a simple vector search using default options, which performs a simple cosine similarity search in Python on the client.&#x20;

```python
prompt = "What are the first programs he tried writing?"

search_results = vector_store.search(embedding_data=prompt, 
                                     embedding_function=embedding_function)
```

The `search_results` is a dictionary with keys for the `text`, `score`, `id`, and `metadata`, with data ordered by score. By default, it returns 4 samples ordered by similarity score, and if we examine the first returned text, it appears to contain the text about trust and safety models that is relevant to the prompt.

```python
search_results['text'][0]
```

Returns:

```
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.
```

#### Filter Search Using UDFs

Vector search can be combined with other search logic for performing more advanced queries. Let's define a function compatible with [deeplake.filter](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-filtering) for filtering data before the vector search. The function below will filter samples that contain the word `"program"` in the `text` tensor.

```python
def filter_fn(x):
    # x is a single row in Deep Lake, 'text' is the tensor name, .data()['value'] is the method for fetching the data
    return "program" in x['text'].data()['value'].lower()
```

Let's run the vector search with the filter above, and return more samples (`k = 10`), and perform similarity search using L2 metric (`distance_metric = "l2"`):

```python
prompt = "What are the first programs he tried writing?"

search_results_filter = vector_store.search(embedding_data = prompt, 
                                            embedding_function = embedding_function,
                                            filter = filter_fn,
                                            k = 10,
                                            distance_metric = 'l2',
                                            exec_option = "python")
```

We can verity that the word `"program"` is present in all of the results:

```python
all(["program" in result for result in search_results_filter["text"]])

# Returns True
```

{% hint style="info" %}
UDFs are only supported with query execution using the Python engine, so in the search above, `exec_option = "python"` should be specified.
{% endhint %}

#### Filter Search Using Metadata Filters

Instead of using UDFs, a filter can be specified using dictionary syntax. For json tensors, the syntax is `filter = {"tensor_name": {"key": "value"}}`. For text tensors, it is `filter = {"tensor": "value"}`. In all cases, an exact match is performed.

```python
search_results_filter = vector_store.search(embedding_data = prompt, 
                                            embedding_function = embedding_function,
                                            filter = {"metadata": {"source": "paul_graham_essay.txt"}})
```

#### Filter Search using TQL

Deep Lake offers advanced search that executes queries with higher performance in C++, and offers querying using Deep Lake's [Tensor Query Language (TQL)](https://docs-v3.activeloop.ai/examples/tql).&#x20;

{% hint style="warning" %}
In order to use Compute Engine, Deep Lake data must be stored in Deep Lake Storage, or in the user's cloud while being connected to Deep Lake using [Managed Credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials).&#x20;
{% endhint %}

Let's load a larger Vector Store for running more interesting queries:

```python
vector_store_path = "hub://activeloop/twitter-algorithm"

vector_store = VectorStore(
    path = vector_store_path,
    read_only = True
)
```

{% hint style="warning" %}
NOTE: this Vector Store is stored in `us-east`, and query performance may vary significantly depending on your location. In real-world use-cases, users would store their Vector Stores in regions optimized for their use case.
{% endhint %}

Now let's run a search that includes filtering of `text`, `metadata`, and `embedding` tensors. We do this using [TQL](https://docs-v3.activeloop.ai/examples/tql/syntax) by combining embedding search syntax (`cosine_similarity(embedding, ...)`) and filtering syntax (`where ....`).&#x20;

We are interested in answering a prompt based on the question:

```python
prompt = "What does the python code do?"
```

Therefore, we apply a filter to only search for `text` that contains the word `"python"` and `metadata` where the `source` key contains `".py"`.

```python
embedding = embedding_function(prompt)[0]

# Format the embedding array or list as a string, so it can be passed in the REST API request.
embedding_string = ",".join([str(item) for item in embedding])

tql_query = f"select * from (select text, metadata, cosine_similarity(embedding, ARRAY[{embedding_string}]) as score where contains(text, 'python') or contains(metadata['source'], '.py')) order by score desc limit 5"
```

```python
search_results = vector_store.search(query = tql_query)
```

### Vector Search Using the Managed Tensor Database (Server-Side)

For Vector Stored in the [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database), queries will automatically execute on the database (instead of the client). Vector Stores are created in the Managed Tensor Database by specifying `vector_store_path = hub://org_id/dataset_name` and `runtime = {"tensor_db": True}` during Vector Store creation.

<pre class="language-python"><code class="lang-python"><strong># vector_store = VectorStore(
</strong>#     path = "hub://&#x3C;org_id>/&#x3C;dataset_name>",
#     runtime = {"tensor_db": True}
# )
<strong>
</strong><strong>search_results = vector_store.search(embedding_data=prompt, 
</strong>                                     embedding_function=embedding_function)
</code></pre>

If Vector Stores are not in the Managed Tensor Database, [they can be migrated using these steps](https://docs-v3.activeloop.ai/examples/rag/managed-database/migrating-datasets-to-the-tensor-database):


# Managed Database REST API

Running Vector Search in the Deep Lake Tensor Database using the REST API

## How to Run Vector Search in the Deep Lake Tensor Database using the REST API

{% hint style="danger" %}
The REST API is currently in Alpha, and the syntax may change without announcement.
{% endhint %}

To use the REST API, Deep Lake data must be stored in the [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) by specifying the `deeplake_path = hub://org_id/dataset_name` and `runtime = {"tensor_db": True}`. [Full details on path and storage management are available here](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options).

### Performing Vector Search Using the REST API

Let's query this Vector Store stored in the Managed Tensor Database using the [REST API](https://docs-v3.activeloop.ai/examples/rag/managed-database/rest-api). The steps are:

1. Define the authentication tokens and search terms
2. Embed the search search term using OpenAI
3. Reformat the embedding to an `embedding_search` string that can be passed to the REST API request.
4. Create the query string using [Deep Lake TQL](https://docs-v3.activeloop.ai/examples/tql/syntax). The `dataset_path` and `embedding_search` are a part of the query string. &#x20;
5. Submit the request and print the response data data

{% tabs %}
{% tab title="Python" %}

```python
import requests
import openai
import os

# Tokens should be set in environmental variables.
ACTIVELOOP_TOKEN = os.environ['ACTIVELOOP_TOKEN']
DATASET_PATH = 'hub://activeloop/twitter-algorithm'
ENDPOINT_URL = 'https://app.activeloop.ai/api/query/v1'
SEARCH_TERM = 'What do the trust and safety models do?'
# os.environ['OPENAI_API_KEY'] OPEN AI TOKEN should also exist in env variables

# The headers contains the user token
headers = {
    "Authorization": f"Bearer {ACTIVELOOP_TOKEN}",
}

# Embed the search term
embedding = openai.Embedding.create(input=SEARCH_TERM, model="text-embedding-ada-002")["data"][0]["embedding"]

# Format the embedding array or list as a string, so it can be passed in the REST API request.
embedding_string = ",".join([str(item) for item in embedding])

# Create the query using TQL
query = f"select * from (select text, cosine_similarity(embedding, ARRAY[{embedding_string}]) as score from \"{dataset_path}\") order by score desc limit 5"
          
# Submit the request                              
response = requests.post(ENDPOINT_URL, json={"query": query}, headers=headers)

data = response.json()

print(data)
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

OPENAI_API_KEY = process.env.OPENAI_API_KEY;
ACTIVELOOP_TOKEN = process.env.ACTIVELOOP_TOKEN;

const QUERY = 'What do the trust and safety models do?';
const DATASET_PATH = 'hub://activeloop/twitter-algorithm';
const ENDPOINT_URL = 'https://app.activeloop.ai/api/query/v1';

// Function to get the embeddings of a text from Open AI API
async function getEmbedding(text) {
  const response = await axios.post('https://api.openai.com/v1/embeddings', {
    input: text,
    model: "text-embedding-ada-002"
  }, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${OPENAI_API_KEY}`
    }
  });

  return response.data;
}

// Function to search the dataset using the given query on Activeloop
async function searchDataset(query) {
  const response = await axios.post(${ENDPOINT_URL}, {
    query: query,
  }, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${ACTIVELOOP_TOKEN}`
    }
  });

  return response.data;
}

// Main function to search for similar texts in the dataset based on the query_term
async function searchSimilarTexts(query, dataset_path) {
  // Get the embedding of the query_term
  const embedding = await getEmbedding(query);
  const embedding_search = embedding.data[0].embedding.join(',');

  // Construct the search query
  const TQL = `SELECT * FROM (
                    SELECT text, l2_norm(embedding - ARRAY[${embedding_search}]) AS score 
                    from "${dataset_path}"
                  ) ORDER BY score DESC LIMIT 5`;

  // Search the dataset using the constructed query
  const response = await searchDataset(TQL);

  // Log the search results
  console.log(response);
}

searchSimilarTexts(QUERY, DATASET_PATH)
```

{% endtab %}
{% endtabs %}

Congrats! You performed a vector search using the Deep Lake Managed Database! 🎉


# Customizing Your Vector Store

Customizing the Deep Lake Vector Store

## How to Customize Deep Lake Vector Stores for Images, Multi-Embedding Applications, and More.

Under-the-hood, Deep Lake vector stores use the Deep Lake tabular format, where `Tensors` are conceptually equivalent to columns. A unique feature in Deep Lake is that Tensors can be customized to a variety of use-cases beyond simple embeddings of text.

### Creating vector stores with non-text data

To create a Vector Store for images, we should write a custom embedding function that embeds images from a file using a neural network, since we cannot use OpenAI for embedding images yet.

```python
import os
import torch
from torchvision import transforms, models
from torchvision.models.feature_extraction import create_feature_extractor
from PIL import Image

model = models.resnet18(pretrained=True)

return_nodes = {
    "avgpool": "embedding"
}
model = create_feature_extractor(model, return_nodes=return_nodes)

model.eval()
model.to("cpu")
```

```python
tform = transforms.Compose([
    transforms.Resize((224,224)), 
    transforms.ToTensor(),
    transforms.Lambda(lambda x: torch.cat([x, x, x], dim=0) if x.shape[0] == 1 else x),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

def embedding_function(images, model = model, transform = tform, batch_size = 4):
    """Creates a list of embeddings based on a list of image filenames. Images are processed in batches."""

    if isinstance(images, str):
        images = [images]

    #Proceess the embeddings in batches, but return everything as a single list
    embeddings = []
    for i in range(0, len(images), batch_size):
        batch = torch.stack([transform(Image.open(item)) for item in images[i:i+batch_size]])
        batch = batch.to("cpu")
        with torch.no_grad():
            embeddings+= model(batch)['embedding'][:,:,0,0].cpu().numpy().tolist()

    return embeddings
```

Lets download and unzip 6 example images with common objects and create a list of containing their filenames.

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/rYKE8GEhDANiu2iFGClB/common_objects.zip>" %}

```python
data_folder = '/Users/istranic/ActiveloopCode/Datasets/common_objects'

image_fns = [os.path.join(data_folder, file) for file in os.listdir(data_folder) if os.path.splitext(file)[-1]=='.jpg']
```

Earlier in this tutorial, we did not specify any data-structure-related information when initializing the Vector Store, which by default creates a vector store with tensors for `text`, `metadata`, `id (auto-populated)`, and `embedding`. &#x20;

Here, we create a Vector Store for image similarity search, which should contains tensors for the `image`, its `embedding`, and the `filename` for the image. This can be achieved by specifying custom `tensor_params`.

```python
vector_store_path = '/vector_store_getting_started_images"

vector_store = VectorStore(
    path = vector_store_path,
    tensor_params = [{'name': 'image', 'htype': 'image', 'sample_compression': 'jpg'}, 
                     {'name': 'embedding', 'htype': 'embedding'}, 
                     {'name': 'filename', 'htype': 'text'}],
)
```

We add data to the Vector Store just as if we were adding text data earlier in the Getting Started Guide.

```python
vector_store.add(image = image_fns,
                 filename = image_fns,
                 embedding_function = embedding_function, 
                 embedding_data = image_fns)
```

#### Performing image similarity search

Let's find the image in the Vector Store that is most similar to the reference image below.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/urVFy2SyQlJmPBcXUutD/reference_image.jpg" alt=""><figcaption></figcaption></figure>

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/urVFy2SyQlJmPBcXUutD/reference_image.jpg>" %}

```python
image_path = '/reference_image.jpg'

result = vector_store.search(embedding_data = [image_path], embedding_function = embedding_function)
```

We can display the result of the most similar image, which shows a picture of a yellow Lamborghini, which is fairly similar to the black Porsche above.&#x20;

```python
Image.fromarray(result['image'][0])
```

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/KEiGhsveCOioJaIFPQtf/image_2.jpg" alt=""><figcaption></figcaption></figure>

### Creating Vector Stores with multiple embeddings

COMING SOON


# Image Similarity Search

Using Deep Lake for image similarity search

## How to Use Deep Lake as a Vector Store for Images

Deep Lake is a unique Vector Store because it supports storage of various data types including images, video, and audio. In this tutorial we show how to use Deep Lake to perform similarity search for images.&#x20;

### Creating the Vector Store

We will use \~5k images in the [COCO Validation Dataset](https://cocodataset.org/#home) as a source of diverse images. First, let's download the data.

```python
!wget -O "<download_path>" http://images.cocodataset.org/zips/val2017.zip
# MAC !curl -o "<download_path>" http://images.cocodataset.org/zips/val2017.zip
```

We must unzip the images and specify their parent folder below.

```python
images_path = <download_path>
```

Next, let's define a [ResNet18 PyTorch model](https://pytorch.org/vision/main/models/resnet.html) to embed the images based on the output from the second-to-last layer. We use the `torchvision` feature extractor to return the output of the `avgpool` layer to the `embedding` key, and we run on a GPU if available. (Note: `DeepLakeVectorStore` class was deprecated, but you can still use it. The new API for calling Deep Lake's Vector Store is: `VectorStore.`)

```python
from deeplake.core.vectorstore.deeplake_vectorstore import VectorStore
import os
import torch
from torchvision import transforms, models
from torchvision.models.feature_extraction import create_feature_extractor
from PIL import Image

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
```

```python
model = models.resnet18(pretrained=True)

return_nodes = {
    'avgpool': 'embedding'
}
model = create_feature_extractor(model, return_nodes=return_nodes)

model.eval()
model.to(device)
```

Let's define an embedding function that will embed a list of image filenames and return a list of embeddings. A transformation must be applied to the images so they can be fed into the model, including handling of grayscale images.

```python
tform= transforms.Compose([
    transforms.Resize((224,224)), 
    transforms.ToTensor(),
    transforms.Lambda(lambda x: torch.cat([x, x, x], dim=0) if x.shape[0] == 1 else x),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

def embedding_function(images, model = model, transform = tform, batch_size = 4):
    """Creates a list of embeddings based on a list of image filenames. Images are processed in batches."""

    if isinstance(images, str):
        images = [images]

    #Proceess the embeddings in batches, but return everything as a single list
    embeddings = []
    for i in range(0, len(images), batch_size):
        batch = torch.stack([transform(Image.open(item)) for item in images[i:i+batch_size]])
        batch = batch.to(device)
        with torch.no_grad():
            embeddings+= model(batch)['embedding'][:,:,0,0].cpu().numpy().tolist()

    return embeddings
```

Now we can create the vector store for storing the data. The Vector Store does not have the default configuration with `text`, `embedding`, and `metadata` tensors, so we use the `tensor_params` input to define the structure of the Vector Store.&#x20;

```python
vector_store_path = 'hub://<org_id>/<dataset_name>'

vector_store = VectorStore(
    path = vector_store_path,
    tensor_params = [{'name': 'image', 'htype': 'image', 'sample_compression': 'jpg'}, 
                     {'name': 'embedding', 'htype': 'embedding'}, 
                     {'name': 'filename', 'htype': 'text'}],
)
```

Finally, we can create a list of images from the source data and add it to the vector store.&#x20;

```python
image_fns = [os.path.join(images_path, item) for item in os.listdir(images_path) if os.path.splitext(item)[-1]=='.jpg']
```

```python
vector_store.add(image = image_fns,
                 filename = image_fns,
                 embedding_function = embedding_function, 
                 embedding_data = image_fns)
```

We observe in the automatically printed summary that the Vector Store has tensors for the `image`, their `filename`, their `embedding`, and an `id`, with 5000 samples each. This summary is also available via `vector_store.summary()`.

```
  tensor      htype                shape               dtype  compression
  -------    -------              -------             -------  ------- 
 embedding  embedding           (5000, 512)           float32   None   
 filename     text               (5000, 1)              str     None   
    id        text               (5000, 1)              str     None   
   image      image    (5000, 145:640, 200:640, 1:3)   uint8    jpeg   
```

### Similarity Search

Let's perform a similarity search on a reference image to find similar images in our Vector Store. First we download the image:

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/f1x74JEyLY6bO7eaTQG9/image_similarity.jpg" alt=""><figcaption></figcaption></figure>

{% file src="<https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/f1x74JEyLY6bO7eaTQG9/image_similarity.jpg>" %}

The similarity search will return data for the top k (defaults to 4) similar samples, including numpy arrays for the underlying images.

<pre class="language-python"><code class="lang-python">image_path = '/image_similarity.jpg'
<strong>
</strong><strong>result = vector_store.search(embedding_data = image_path, 
</strong>                             embedding_function = embedding_function)
</code></pre>

The key-value pairs in the result contains the tensor as the key and a list of values for the data:

```python
result.keys() 

# Returns: dict_keys(['filename', 'id', 'image', 'score'])
```

```python
len(result['score']) 

# Returns: 4
```

<pre class="language-python"><code class="lang-python"><strong>result['image'][0].shape
</strong><strong>
</strong># Returns: (427, 640, 3)
</code></pre>

Since images can be quite large, and we may not want to return them as numpy arrays, so we use `return_tensors` to specify that only the `filename` and `id` tensors should be returned:

```python
result = vector_store.search(embedding_data = image_path, 
                             embedding_function = embedding_function,
                             return_tensors = ['id', 'filename'])
```

```python
result.keys() 

# Returns: dict_keys(['filename', 'id', 'image', 'score'])
```

### Visualizing the Similarity Results

Instead of returning the results of the similarity search directly, we can use `return_view = True` to get the Deep Lake dataset view, which is a lazy pointer to the underlying data that satisfies the similarity search (no data is retrieved locally).

```python
view = vector_store.search(embedding_data = image_path, 
                             embedding_function = embedding_function, 
                             return_view = True)
```

We can then save the view and visualize it in the Deep Lake UI:

```python
view.save_view()
```

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/Sa9rfvjFKOuu9CDyXx0W/image_similarity_result.png" alt=""><figcaption></figcaption></figure>

The images are all fairly similar to the reference image, so it looks like the similarity search worked well!

Congrats! You just used the Deep Lake VectorStore in for image similarity search! 🎉


# Improving Search Accuracy using Deep Memory

Using Deep Memory to improve the accuracy of your Vector Search

## How to Use Deep Memory to Improve the Accuracy of your Vector Search <a href="#how-to-use-deep-memory-to-improve-the-accuracy-of-your-vector-search" id="how-to-use-deep-memory-to-improve-the-accuracy-of-your-vector-search"></a>

#### This tutorial is also available as a [Colab Notebook](https://colab.research.google.com/drive/1Hu6lkVwXPdLvWXwQIcFTs8OxKQgYzmJp?usp=sharing)

[Deep Memory](https://docs-v3.activeloop.ai/examples/rag/deep-memory) computes a transformation that converts your embeddings into an embedding space that is tailored for your use case, based on several examples for which the most relevant embedding is known. This can increase the accuracy of your Vector Search by up to 22%.

**In this example, we'll use Deep Memory to improve the accuracy of Vector Search on the SciFact dataset, where the input prompt is a scientific claim, and the search result is the corresponding abstract.**

### Downloading the Data <a href="#downloading-the-data" id="downloading-the-data"></a>

First let's specify out Activeloop and OpenAI tokens. Make sure to install `pip install datasets` because we'll download the source data from HuggingFace.

```python
from deeplake import VectorStore
import os
import getpass
import datasets
import openai
from pathlib import Path
```

```python
os.environ['OPENAI_API_KEY'] = getpass.getpass()
```

```python
# Skip this step if you logged in through the CLI
os.environ['ACTIVELOOP_TOKEN'] = getpass.getpass()
```

Next, let's download the dataset locally:

```python
corpus = datasets.load_dataset("scifact", "corpus")
```

### Creating the Vector Store <a href="#creating-the-vector-store" id="creating-the-vector-store"></a>

Now let's define an embedding function for the text data and create a Deep Lake Vector Store in our Managed Database. Deep Memory is only available for Vector Stores in our Managed Database.

```python
def embedding_function(texts, model="text-embedding-ada-002"):
   
   if isinstance(texts, str):
       texts = [texts]

   texts = [t.replace("\n", " ") for t in texts]
   return [data['embedding']for data in openai.Embedding.create(input = texts, model=model)['data']]
```

```python
path = 'hub://<org_id>/<vector_store_name>'
```

```python
vectorstore = VectorStore(
    path=path,
    embedding_function=embedding_function,
    runtime={"tensor_db": True},
)
```

#### Adding data to the Vector Store <a href="#adding-data-to-the-vector-store" id="adding-data-to-the-vector-store"></a>

Next, let's extract the data from the SciFact dataset and add it to our Vector Store. In this example, we embed the abstracts of the scientific papers. Normally, the `id` tensor is auto-populated, but in this case, we want to use the ids in the SciFact dataset, in order to use the internal connection between ids, abstracts, and claims, that already exists in SciFact.

```python
ids = [f"{id_}" for id_ in corpus["train"]["doc_id"]]
texts = [' '.join(text) for text in corpus["train"]["abstract"]]
metadata = [{"title": title} for title in corpus["train"]["title"]]
```

```python
vectorstore.add(
    text=texts,
    id=ids,
    embedding_data=texts,
    embedding_function=embedding_function,
    metadata=metadata,
)
```

#### Generating claims <a href="#generating-claims" id="generating-claims"></a>

We must create a relationship between the claims and their corresponding most relevant abstracts. This correspondence already exists in the SciFact dataset, and we extract that information using the helper function below.

```python
def preprocess_scifact(claims_dataset, dataset_type="train"):

    # Using a dictionary to store unique claims and their associated relevances
    claims_dict = {}

    for item in claims_dataset[dataset_type]:
        claim = item['claim']  # Assuming 'claim' is the field for the question
        relevance = item['cited_doc_ids']  # Assuming 'cited_doc_ids' is the field for relevance
        relevance = [(str(r), 1) for r in relevance]

        # Check for non-empty relevance
        if claim not in claims_dict:
            claims_dict[claim] = relevance
        else:
            # If the does not exist in the dictionary, append the new relevance
            if relevance not in claims_dict[claim]:
                claims_dict[claim].extend(relevance)

    # Split the dictionary into two lists: claims and relevances
    claims = list(claims_dict.keys())
    relevances = list(claims_dict.values())
    return claims, relevances
```

```python
claims_dataset = datasets.load_dataset('scifact', 'claims')
claims, relevances = preprocess_scifact(claims_dataset, dataset_type="train")
```

Let's print the first 10 claims and their relevant abstracts. The relevances are a list of tuples, where each the id corresponds to the `id` tensor value in the Abstracts Vector Store, and 1 indicates a positive relevance.

```python
claims[:10]
```

```
['1 in 5 million in UK have abnormal PrP positivity.',
 '32% of liver transplantation programs required patients to discontinue methadone treatment in 2001.',
 '40mg/day dosage of folic acid and 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression.',
 '76-85% of people with severe mental disorder receive no treatment in low and middle income countries.',
 'A T helper 2 cell (Th2) environment impedes disease development in patients with systemic lupus erythematosus (SLE).',
 "A breast cancer patient's capacity to metabolize tamoxifen influences treatment outcome.",
 "A country's Vaccine Alliance (GAVI) eligibility is not indictivate of accelerated adoption of the Hub vaccine.",
 'A deficiency of folate increases blood levels of homocysteine.',
 'A diminished ovarian reserve does not solely indicate infertility in an a priori non-infertile population.',
 'A diminished ovarian reserve is a very strong indicator of infertility, even in an a priori non-infertile population.']
```

```python
relevances[:10]
```

```
[[('31715818', 1)],
 [('13734012', 1)],
 [('22942787', 1)],
 [('2613775', 1)],
 [('44265107', 1)],
 [('32587939', 1)],
 [('32587939', 1)],
 [('33409100', 1), ('33409100', 1)],
 [('641786', 1)],
 [('22080671', 1)]]
```

### Running the Deep Memory Training <a href="#running-the-deep-memory-training" id="running-the-deep-memory-training"></a>

Now we can run a Deep Memory training, which runs asynchronously and executes on our managed service.

```python
job_id = vectorstore.deep_memory.train(
    queries = claims,
    relevance = relevances,
    embedding_function = embedding_function,
)
```

All of the Deep Memory training jobs for this Vector Store can be listed using the command below. The PROGRESS tells us the state of the training job, as well as the recall improvement on the data.

**`recall@k` corresponds to the percentage of rows for which the correct (most relevant) answer was returned in the top `k` vector search results**

```python
vectorstore.deep_memory.list_jobs()
```

```
This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/activeloop-test/test-deepmemory-ivo
ID                        STATUS     RESULTS                        PROGRESS       
6525a94bbfacbf7e75a08c76  completed  recall@10: 0.00% (+0.00%)      eta: 45.5 seconds
                                                                    recall@10: 0.00% (+0.00%)
6538186bc1d2ffd8e8cd3b49  completed  recall@10: 85.81% (+21.78%)    eta: 1.9 seconds
                                                                    recall@10: 85.81% (+21.78%)
```

### Evaluating Deep Memory's Performance <a href="#evaluating-deep-memorys-performance" id="evaluating-deep-memorys-performance"></a>

Let's evaluate the recall improvement for an evaluation dataset that was not used in the training process. Deep Memory inference, and by extension this evaluation process, runs on the client.

```python
validation_claims, validation_relevances = preprocess_scifact(claims_dataset, dataset_type="validation")
```

<pre class="language-python"><code class="lang-python"><strong>recalls = vectorstore.deep_memory.evaluate(
</strong>    queries = validation_claims,
    relevance = validation_relevances,
    embedding_function = embedding_function,
)
</code></pre>

We observe that the recall has improved by p to 16%, depending on the `k` value.

```
---- Evaluating without Deep Memory ---- 
Recall@1:	  44.2%
Recall@3:	  56.9%
Recall@5:	  61.3%
Recall@10:	  67.3%
Recall@50:	  77.2%
Recall@100:	  79.9%
---- Evaluating with Deep Memory ---- 
Recall@1:	  60.4%
Recall@3:	  67.6%
Recall@5:	  71.7%
Recall@10:	  75.4%
Recall@50:	  79.1%
Recall@100:	  80.2%
```

### Using Deep Memory in your Application <a href="#using-deep-memory-in-your-application" id="using-deep-memory-in-your-application"></a>

To use Deep Memory in your applications, specify the `deep_memory = True` parameter during vector search. If you are using the LangChain integration, you may specify this parameter during Vector Store initialization. Let's try searching embedding using a prompt, with and without Deep Memory.

```python
prompt = "Which diseases are inflammation-related processes"
```

```python
results = vectorstore.search(embedding_data = prompt)
```

```python
results['text']
```

```
['Inflammation is a fundamental protective response that sometimes goes awry and becomes a major cofactor in the pathogenesis of many chronic human diseases, including cancer.',
 'Kidney diseases, including chronic kidney disease (CKD) and acute kidney injury (AKI), are associated with inflammation.',
 'BACKGROUND Persistent inflammation has been proposed to contribute to various stages in the pathogenesis of cardiovascular disease.',
 'Inflammation accompanies obesity and its comorbidities-type 2 diabetes, non-alcoholic fatty liver disease and atherosclerosis, among others-and may contribute to their pathogenesis.']
```

```python
results_dm = vectorstore.search(embedding_data = prompt, deep_memory = True)
```

```python
results_dm['text']
```

```
['Kidney diseases, including chronic kidney disease (CKD) and acute kidney injury (AKI), are associated with inflammation.',
 'OBJECTIVES Calcific aortic valve (AV) disease is known to be an inflammation-related process.',
 "Crohn's disease and ulcerative colitis, the two main types of chronic inflammatory bowel disease, are multifactorial conditions of unknown aetiology.",
 'BACKGROUND Two inflammatory disorders, type 1 diabetes and celiac disease, cosegregate in populations, suggesting a common genetic origin.']
```

We observe that there are overlapping results for both search methods, but 50% of the answers differ.

Congrats! You just used Deep Memory to improve the accuracy of Vector Search on a specific use-case! 🎉


# LangChain Integration

Using Deep Lake as a Vector Store in LangChain

## How to Use Deep Lake as a Vector Store in LangChain

Deep Lake can be used as a [VectorStore](https://python.langchain.com/en/latest/reference/modules/vectorstores.html#langchain.vectorstores.DeepLake) in [LangChain](https://github.com/hwchase17/langchain) for building Apps that require filtering and vector search. In this tutorial we will show how to create a Deep Lake Vector Store in LangChain and use it to build a Q\&A App about the [Twitter OSS recommendation algorithm](https://github.com/twitter/the-algorithm). This tutorial requires installation of:

```bash
!pip3 install langchain deeplake openai tiktoken
```

### Downloading and Preprocessing the Data

First, let's import necessary packages and **make sure the Activeloop and OpenAI keys are in the environmental variables `ACTIVELOOP_TOKEN`, `OPENAI_API_KEY`.**

```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
import os
```

Next, let's clone the Twitter OSS recommendation algorithm:

```python
!git clone https://github.com/twitter/the-algorithm
```

Next, let's load all the files from the repo into a list:

```python
repo_path = '/the-algorithm'

docs = []
for dirpath, dirnames, filenames in os.walk(repo_path):
    for file in filenames:
        try: 
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e: 
            print(e)
            pass
```

#### A note on chunking text files:

Text files are typically split into chunks before creating embeddings. In general, more chunks increases the relevancy of data that is fed into the language model, since granular data can be selected with higher precision. However, since an embedding will be created for each chunk, more chunks increase the computational complexity.

```python
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)
```

{% hint style="warning" %}
Chunks in the above context should not be confused with Deep Lake chunks!
{% endhint %}

### Creating the Deep Lake Vector Store

First, we specify a path for storing the Deep Lake dataset containing the embeddings and their metadata.&#x20;

```python
dataset_path = 'hub://<org-id>/twitter_algorithm'
```

Next, we specify an OpenAI algorithm for creating the embeddings, and create the VectorStore. This process creates an embedding for each element in the `texts` lists and stores it in Deep Lake format at the specified path.&#x20;

```python
embeddings = OpenAIEmbeddings()
```

```python
db = DeepLake.from_documents(texts, embeddings, dataset_path=dataset_path)
```

The Deep Lake Vector Store has 4 tensors including the `text`, `embedding`, `ids`, and  `metadata` .

```
  tensor     htype       shape       dtype  compression
  -------   -------     -------     -------  ------- 
 embedding  generic  (23156, 1536)  float32   None   
    ids      text     (23156, 1)      str     None   
 metadata    json     (23156, 1)      str     None   
   text      text     (23156, 1)      str     None   
```

### Use the Vector Store in a Q\&A App

We can now use the VectorStore in Q\&A app, where the embeddings will be used to filter relevant documents (`texts`) that are fed into an LLM in order to answer a question.

If we were on another machine, we would load the existing Vector Store without recalculating the embeddings:

```python
db = DeepLake(dataset_path=dataset_path, read_only=True, embedding=embeddings)
```

We have to create a `retriever` object and specify the search parameters.

```python
retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['k'] = 20
```

Finally, let's create an `RetrievalQA` chain in LangChain and run it:

```python
model = ChatOpenAI(model='gpt-4') # 'gpt-3.5-turbo',
qa = RetrievalQA.from_llm(model, retriever=retriever)
```

```python
qa.run('What programming language is most of the SimClusters written in?')
```

This returns:

`Most of the SimClusters code is written in Scala, as seen in the provided context with the file path [src/scala/com/twitter/simclusters_v2/scio/bq_generation](scio/bq_generation) and the package declarations that use the Scala package syntax.`

{% hint style="info" %}
We can tune `k` in the `retriever` depending on whether the prompt exceeds the model's token limit. Higher `k` increases the accuracy by including more data in the prompt.
{% endhint %}

### Adding data to to an existing Vector Store

Data can be added to an existing Vector Store by loading it using its path and adding documents or texts.&#x20;

```python
db = DeepLake(dataset_path=dataset_path, embedding=embeddings)

# Don't run this here in order to avoid data duplication
# db.add_documents(texts)
```

### Adding Hybrid Search to the Vector Store

Since embeddings search can be computationally expensive, you can simplify the search by filtering out data using an explicit search on top of the embeddings search. Suppose we want to answer to a question related to the trust and safety models. We can filter the filenames (`source`) in the `metadata` using a custom function that is added to the retriever:

```python
def filter(deeplake_sample):
    return 'trust_and_safety_models' in deeplake_sample['metadata'].data()['value']['source']

retriever.search_kwargs['filter'] = filter
```

```python
qa = RetrievalQA.from_llm(model, retriever=retriever)

qa.run("What do the trust and safety models do?")
```

This returns:

`"The Trust and Safety Models are designed to detect various types of content on Twitter that may be inappropriate, harmful, or against their terms of service.........."`

Filters can also be specified as a dictionary. For example, if the `metadata` tensor had a key `year`, we can filter based on that key using:

<pre class="language-python"><code class="lang-python"><strong># retriever.search_kwargs['filter'] = {"metadata": {"year": 2020}}
</strong></code></pre>

### Using Deep Lake in Applications that Require Concurrency

For applications that require writing of data concurrently, users should set up a lock system to queue the write operations and prevent multiple clients from writing to the Deep Lake Vector Store at the same time. This can be done with a few lines of code in the example below:

{% content-ref url="../../technical-details/best-practices/concurrent-writes/concurrency-using-zookeeper-locks" %}
[concurrency-using-zookeeper-locks](https://docs-v3.activeloop.ai/technical-details/best-practices/concurrent-writes/concurrency-using-zookeeper-locks)
{% endcontent-ref %}

### Accessing the Low Level Deep Lake API (Advanced)

When using a Deep Lake Vector Store in LangChain, the underlying Vector Store and its low-level Deep Lake dataset can be accessed via:

```python
# LangChain Vector Store
db = DeepLake(dataset_path=dataset_path)

# Deep Lake Vector Store object
ds = db.vectorstore

# Deep Lake Dataset object
ds = db.vectorstore.dataset
```

### SelfQueryRetriever with Deep Lake

Deep Lake supports the [SelfQueryRetriever](https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.self_query.base.SelfQueryRetriever.html) implementation in LangChain, which translates a user prompt into a metadata filters.&#x20;

{% hint style="warning" %}
This section of the tutorial requires installation of additional packages:

`pip install "deeplake[enterprise]" lark`
{% endhint %}

First let's create a Deep Lake Vector Store with relevant data using the documents below.

```python
docs = [
    Document(
        page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",
        metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    Document(
        page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",
        metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},
    ),
    Document(
        page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",
        metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},
    ),
    Document(
        page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",
        metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    Document(
        page_content="Toys come alive and have a blast doing so",
        metadata={"year": 1995, "genre": "animated"},
    ),
    Document(
        page_content="Three men walk into the Zone, three men walk out of the Zone",
        metadata={
            "year": 1979,
            "rating": 9.9,
            "director": "Andrei Tarkovsky",
            "genre": "science fiction",
            "rating": 9.9,
        },
    ),
]
```

Since this feature uses Deep Lake's [Tensor Query Language](https://docs-v3.activeloop.ai/examples/tql) under the hood, the Vector Store must be stored in or connected to Deep Lake, which requires [registration with Activeloop](https://app.activeloop.ai/register/):

```python
org_id = <YOUR_ORG_ID> #By default, your username is an org_id
dataset_path = f"hub://{org_id}/self_query"

vectorstore = DeepLake.from_documents(
    docs, embeddings, dataset_path = dataset_path, overwrite = True,
)
```

Next, let's instantiate our retriever by providing information about the metadata fields that our documents support and a short description of the document contents.

```python
from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

metadata_field_info = [
    AttributeInfo(
        name="genre",
        description="The genre of the movie",
        type="string or list[string]",
    ),
    AttributeInfo(
        name="year",
        description="The year the movie was released",
        type="integer",
    ),
    AttributeInfo(
        name="director",
        description="The name of the movie director",
        type="string",
    ),
    AttributeInfo(
        name="rating", description="A 1-10 rating for the movie", type="float"
    ),
]

document_content_description = "Brief summary of a movie"
llm = OpenAI(temperature=0)

retriever = SelfQueryRetriever.from_llm(
    llm, vectorstore, document_content_description, metadata_field_info, verbose=True
)
```

And now we can try actually using our retriever!

```python
# This example only specifies a relevant query
retriever.get_relevant_documents("What are some movies about dinosaurs")
```

Output:

```
[Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'year': 1993, 'rating': 7.7, 'genre': 'science fiction'}),
 Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'}),
 Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'rating': 9.9, 'director': 'Andrei Tarkovsky', 'genre': 'science fiction'}),
 Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'director': 'Satoshi Kon', 'rating': 8.6})]
```

Now we can run a query to find movies that are above a certain ranking:

```python
# This example only specifies a filter
retriever.get_relevant_documents("I want to watch a movie rated higher than 8.5")
```

Output:

```
[Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'director': 'Satoshi Kon', 'rating': 8.6}),
 Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'rating': 9.9, 'director': 'Andrei Tarkovsky', 'genre': 'science fiction'})]
```

Congrats! You just used the Deep Lake Vector Store in LangChain to create a Q\&A App! 🎉


# LlamaIndex Integration

Using Deep Lake as a Vector Store in LlamaIndex

## How to Use Deep Lake as a Vector Store in LlamaIndex

Deep Lake can be used as a [VectorStore](https://python.langchain.com/en/latest/reference/modules/vectorstores.html#langchain.vectorstores.DeepLake) in [LlamaIndex](https://github.com/run-llama/llama_index) for building Apps that require filtering and vector search. In this tutorial we will show how to create a Deep Lake Vector Store in LangChain and use it to build a Q\&A App about the [Twitter OSS recommendation algorithm](https://github.com/twitter/the-algorithm). This tutorial requires installation of:

```bash
%pip3 install llama-index-vector-stores-deeplake
!pip3 install langchain llama-index deeplake
```

### Downloading and Preprocessing the Data

First, let's import necessary packages and **make sure the Activeloop and OpenAI keys are in the environmental variables `ACTIVELOOP_TOKEN`, `OPENAI_API_KEY`.**

```python
import os
import textwrap

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.deeplake import DeepLakeVectorStore
from llama_index.core import StorageContext
```

Next, let's clone the Twitter OSS recommendation algorithm:

```python
!git clone https://github.com/twitter/the-algorithm
```

Next, let's specify a local path to the files and add a reader for processing and chunking them.

```python
repo_path = 'the-algorithm'
documents = SimpleDirectoryReader(repo_path, recursive=True).load_data()
```

### Creating the Deep Lake Vector Store

First, we create an empty Deep Lake Vector Store using a specified path:

```python
dataset_path = 'hub://<org-id>/twitter_algorithm'
vector_store = DeepLakeVectorStore(dataset_path=dataset_path)
```

The Deep Lake Vector Store has 4 tensors including the `text`, `embedding`, `ids`, and  `metadata` which includes the filename of the `text` .

```
  tensor      htype     shape    dtype  compression
  -------    -------   -------  -------  ------- 
   text       text      (0,)      str     None   
 metadata     json      (0,)      str     None   
 embedding  embedding   (0,)    float32   None   
    id        text      (0,)      str     None  
```

Next, we create a LlamaIndex `StorageContext` and `VectorStoreIndex`, and use the `from_documents()` method to populate the Vector Store with data. This step takes several minutes because of the time to embed the text.

```python
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context,
)
```

We observe that the Vector Store has 8286 rows of data:

```
  tensor      htype       shape       dtype  compression
  -------    -------     -------     -------  ------- 
   text       text      (8262, 1)      str     None   
 metadata     json      (8262, 1)      str     None   
 embedding  embedding  (8262, 1536)  float32   None   
    id        text      (8262, 1)      str     None 
```

### Use the Vector Store in a Q\&A App

We can now use the VectorStore in Q\&A app, where the embeddings will be used to filter relevant documents (`texts`) that are fed into an LLM in order to answer a question.

If we were on another machine, we would load the existing Vector Store without re-ingesting the data

<pre class="language-python"><code class="lang-python"><strong>vector_store = DeepLakeVectorStore(dataset_path=dataset_path, read_only=True)
</strong>index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
</code></pre>

Next, Let's create the LlamaIndex query engine and run a query:

```
query_engine = index.as_query_engine()
```

```python
response = query_engine.query("What programming language is most of the SimClusters written in?")
print(str(response))
```

`Most of the SimClusters project is written in Scala.`

Congrats! You just used the Deep Lake Vector Store in LangChain to create a Q\&A App! 🎉


# Managed Tensor Database

Deep Lake Managed Database

## Overview of Deep Lake's Managed Tensor Database

Deep Lake offers a serverless Managed Tensor Database that eliminates the complexity of self-hosting and substantially lowers costs. Currently, it only supports dataset queries, including vector search, but additional features for creating and modifying data being added in December 2023.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/K3tTkpXoP4wBU4GBgBsc/Deep_Lake_Embedded_vs_Managed.png" alt=""><figcaption><p>Comparison of Deep Lake as a Managed Database vs Embedded Database</p></figcaption></figure>

### User Interfaces

#### LangChain and LlamaIndex

To use the Managed Vector Database in LangChain or Llama Index, specify `dataset_path = hub://org_id/dataset_name` and `runtime = {"tensor_db": True}` during Vector Store creation.

#### REST API

A standalone REST API is available for interacting with the Managed Database:

{% content-ref url="managed-database/rest-api" %}
[rest-api](https://docs-v3.activeloop.ai/examples/rag/managed-database/rest-api)
{% endcontent-ref %}

### Further Information:

{% content-ref url="managed-database/migrating-datasets-to-the-tensor-database" %}
[migrating-datasets-to-the-tensor-database](https://docs-v3.activeloop.ai/examples/rag/managed-database/migrating-datasets-to-the-tensor-database)
{% endcontent-ref %}


# REST API

How to Use the Deep Lake REST API

## Overview of the Managed Database REST API

{% hint style="danger" %}
The REST API is currently in Alpha, and the syntax may change without announcement.
{% endhint %}

The Deep Lake Tensor Database can be accessed via REST API. The datasets must be stored in the Tensor Database by specifying the `deeplake_path = hub://org_id/dataset_name` and `runtime = {"tensor_db": True}`. [Full details on path and storage management are available here](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options).

### Querying via the REST API

The primary input to the query API is a query string that contains all the necessary information for executing the query, including the path to the Deep Lake data. [Full details on the query syntax are available here](https://docs-v3.activeloop.ai/examples/tql/syntax).

#### Input

```python
url = "https://app.activeloop.ai/api/query/v1"

headers = {
    "Authorization": f"Bearer {user_token}"
    }

# Format the embedding array or list as a string, so it can be passed in the REST API request.
embedding_string = ",".join([str(item) for item in embedding])

request = {
    "query": f"select * from (select text, cosine_similarity(embedding, ARRAY[{embedding_string}]) as score from \"{dataset_path}\") order by score desc limit 5",
    "as_list": True/False # Defaults to True.
    }
```

#### Response

If `as_list = True (default).` Returns a list of jsons, one per row.

```
{
  "message": "Query successful.",
  "tensors": [
    "text",
    "score"
  ],
  "data": [
    {
      "text": "# Twitter's Recommendation Algorithm\n\nTwitter's Recommendation Algorithm is a set of services and jobs that are responsible for constructing and serving the\nHome Timeline. For an introduction to how the algorithm works, please refer to our [engineering blog](https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm). The\ndiagram below illustrates how major services and jobs interconnect.\n\n![](docs/system-diagram.png)\n\nThese are the main components of the Recommendation Algorithm included in this repository:",
      "score": 22.59016227722168
    },
    {
      "text": "![](docs/system-diagram.png)\n\nThese are the main components of the Recommendation Algorithm included in this repository:",
      "score": 22.5976619720459
    },...
    ]
```

If `as_list = False.` Returns a list of values per tensor.

```
{
  "message": "Query successful.",
  "tensors": [
    "text",
    "score"
  ],
  "data": {
    "text": [
      "# Twitter's Recommendation Algorithm\n\nTwitter's Recommendation Algorithm is a set of services and jobs that are responsible for constructing and serving the\nHome Timeline. For an introduction to how the algorithm works, please refer to our [engineering blog](https://blog.twitter.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm). The\ndiagram below illustrates how major services and jobs interconnect.\n\n![](docs/system-diagram.png)\n\nThese are the main components of the Recommendation Algorithm included in this repository:",
      "![](docs/system-diagram.png)\n\nThese are the main components of the Recommendation Algorithm included in this repository:",
      "| Type | Component | Description |\n|------------|------------|------------|\n| Feature | [SimClusters](src/scala/com/twitter/simclusters_v2/README.md) | Community detection and sparse embeddings into those communities. |\n|         | [TwHIN](https://github.com/twitter/the-algorithm-ml/blob/main/projects/twhin/README.md) | Dense knowledge graph embeddings for Users and Tweets. |\n|         | [trust-and-safety-models](trust_and_safety_models/README.md) | Models for detecting NSFW or abusive content. |\n|         | [real-graph](src/scala/com/twitter/interaction_graph/README.md) | Model to predict the likelihood of a Twitter User interacting with another User. |\n|         | [tweepcred](src/scala/com/twitter/graph/batch/job/tweepcred/README) | Page-Rank algorithm for calculating Twitter User reputation. |\n|         | [recos-injector](recos-injector/README.md) | Streaming event processor for building input streams for [GraphJet](https://github.com/twitter/GraphJet) based services. |\n|         | [graph-feature-service](graph-feature-service/README.md) | Serves graph features for a directed pair of Users (e.g. how many of User A's following liked Tweets from User B). |\n| Candidate Source | [search-index](src/java/com/twitter/search/README.md) | Find and rank In-Network Tweets. ~50% of Tweets come from this candidate source. |\n|                  | [cr-mixer](cr-mixer/README.md) | Coordination layer for fetching Out-of-Network tweet candidates from underlying compute services. |\n|                  | [user-tweet-entity-graph](src/scala/com/twitter/recos/user_tweet_entity_graph/README.md) (UTEG)| Maintains an in memory User to Tweet interaction graph, and finds candidates based on traversals of this graph. This is built on the [GraphJet](https://github.com/twitter/GraphJet) framework. Several other GraphJet based features and candidate sources are located [here](src/scala/com/twitter/recos). |\n|                  | [follow-recommendation-service](follow-recommendations-service/README.md) (FRS)| Provides Users with recommendations for accounts to follow, and Tweets from those accounts. |\n| Ranking | [light-ranker](src/python/twitter/deepbird/projects/timelines/scripts/models/earlybird/README.md) | Light Ranker model used by search index (Earlybird) to rank Tweets. |\n|         | [heavy-ranker](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md) | Neural network for ranking candidate tweets. One of the main signals used to select timeline Tweets post candidate sourcing. |\n| Tweet mixing & filtering | [home-mixer](home-mixer/README.md) | Main service used to construct and serve the Home Timeline. Built on [product-mixer](product-mixer/README.md). |\n|                          | [visibility-filters](visibilitylib/README.md) | Responsible for filtering Twitter content to support legal compliance, improve product quality, increase user trust, protect revenue through the use of hard-filtering, visible product treatments, and coarse-grained downranking. |\n|                          | [timelineranker](timelineranker/README.md) | Legacy service which provides relevance-scored tweets from the Earlybird Search Index and UTEG service. |\n| Software framework | [navi](navi/README.md) | High performance, machine learning model serving written in Rust. |\n|                    | [product-mixer](product-mixer/README.md) | Software framework for building feeds of content. |\n|                    | [twml](twml/README.md) | Legacy machine learning framework built on TensorFlow v1. |",
      "We include Bazel BUILD files for most components, but not a top-level BUILD or WORKSPACE file.\n\n## Contributing",
      "We include Bazel BUILD files for most components, but not a top-level BUILD or WORKSPACE file.\n\n## Contributing\n\nWe invite the community to submit GitHub issues and pull requests for suggestions on improving the recommendation algorithm. We are working on tools to manage these suggestions and sync changes to our internal repository. Any security concerns or issues should be routed to our official [bug bounty program](https://hackerone.com/twitter) through HackerOne. We hope to benefit from the collective intelligence and expertise of the global community in helping us identify issues and suggest improvements, ultimately leading to a better Twitter.\n\nRead our blog on the open source initiative [here](https://blog.twitter.com/en_us/topics/company/2023/a-new-era-of-transparency-for-twitter)."
    ],
    "score": [
      22.843185424804688,
      22.83962631225586,
      22.835460662841797,
      22.83342170715332,
      22.832916259765625
    ]
  }
}
```


# Migrating Datasets to the Tensor Database

Migrating datasets to the Tensor Database

## How to migrate existing Deep Lake datasets to the Tensor Database

Datasets are created in the Tensor Database by specifying the `dest = "hub://<org_id>/<dataset_name>"` and `runtime = {"tensor_db": True})` during dataset creation. If datasets are currently stored locally, in your cloud, or in non-database Activeloop storage, they can be migrated to the Tensor Database using:

<pre class="language-python"><code class="lang-python"><strong>import deeplake
</strong>
<strong>ds_tensor_db = deeplake.deepcopy(src = &#x3C;current_path>, 
</strong>                                 dest = "hub://&#x3C;org_id>/&#x3C;dataset_name>", 
                                 runtime = {"tensor_db": True}, 
                                 src_creds = {&#x3C;creds_dict>}, # Only necessary if src is in your cloud
                                 )
</code></pre>


# Deep Memory

Overview of Deep Lake tools for increasing retrieval accuracy

## How to Use Deep Memory to Improve Retrieval Accuracy in Your LLM Apps

Deep Memory is a suite of tools that enables you to optimize your Vector Store for your use-case and achieve higher accuracy in your LLM apps.

### Embedding Transformation

Deep Memory computes a transformation that converts your embeddings into an embedding space that is tailored for your use case. This increases the accuracy of your Vector Search by up to 22%, which significantly impacts the user experience of your LLM applications.&#x20;

Furthermore, Deep Memory can also be used to decrease costs by reducing the amount of context `(k)` that must be injected into the LLM prompt to achieve a given accuracy, thereby reducing token usage.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/DoiLsFPfthHde8CFepsa/Deep_Memory_Comparison.png" alt=""><figcaption></figcaption></figure>


# How it Works

Understanding Deep Memory

## How Deep Memory Works

Deep Memory computes transformation of your embeddings based on several examples of embeddings for which the most relevant embedding in the Vector Store is known. The transformation is computed computed on a Deep Lake Managed Service, and it is applied at inference in Deep Lake's Tensor Query Language (TQL).

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/nPovuk6AmYIYZbywGzUe/Deep_Memory_Architecture.png" alt=""><figcaption></figcaption></figure>


# Tensor Query Language (TQL)

Deep Lake offers a performant SQL-style query engine for data analysis.

## How to Query Using  Deep Lake Tensor Query Language (TQL)

Querying enables users to filter data, gather insights, and focus their work on the most relevant data. Deep Lake offers a highly-performant query engine built in C++ and optimized for the Deep Lake data format.&#x20;

{% hint style="danger" %}
The Deep Lake query engine is only accessible to registered and authenticated users and cannot be used with local datasets.
{% endhint %}

### Dataset Query Summary

#### Querying in the App

{% embed url="<https://www.loom.com/share/40f8f10af5064f9a8baf3dfd37029700>" %}

#### Querying in the Vector Store Python API

```
view = vector_store.search(query = <query_string>)
```

#### Querying in the Deep Learning Python API

Queries can also be performed in the Python API using:

```python
view = ds.query(<query_string>)
```

### Query Syntax

{% content-ref url="tql/syntax" %}
[syntax](https://docs-v3.activeloop.ai/examples/tql/syntax)
{% endcontent-ref %}

### Saving and Using Views In Deep Lake

The query results (`Dataset Views`) can be saved in the UI as shown above, or if the view is generated in Python, it can be saved using the Python API below. Full details are [available here](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-filtering).

```python
view.save_view(message = 'Samples with monarchs')
```

{% hint style="warning" %}
In order to maintain data lineage, `Dataset Views` are immutable and are connected to specific commits. Therefore, views can only be saved if the dataset has a commit and there are no uncommitted changes in the `HEAD`. You can check for this using `ds.has_head_changes`
{% endhint %}

`Dataset Views` can be loaded in the python API and they can passed to ML frameworks just like regular datasets:

```python
ds_view = ds.load_view(view_id, optimize = True, num_workers = 2)

for data in ds_view.pytorch():
    # Training loop here
```

{% hint style="warning" %}
The `optimize` parameter in `ds.load_view(...,`` `**`optimize = True`**`)` materializes the `Dataset View` into a new sub-dataset that is optimized for streaming. If the original dataset uses [linked tensors](https://docs-v3.activeloop.ai/examples/broken-reference), the data will be copied to Deep Lake format.

Optimizing the `Dataset View` is critical for achieving rapid streaming.
{% endhint %}

If the saved `Dataset View` is no longer needed, it can be deleted using:

```python
ds.delete_view(view_id)
```


# TQL Syntax

How to properly format TQL queries

### Query syntax for the Tensor Query Language (TQL)

#### CONTAINS and ==

```sql
-- Exact match, which generally requires that the sample
-- has 1 value, i.e. no lists or multi-dimensional arrays
select * where tensor_name == 'text_value'   # If value is text
select * where tensor_name == numeric_value  # If values is numeric

select * where contains(tensor_name, 'text_value')
```

{% hint style="warning" %}
Tensor or group names with special characters should be wrapped with double-quotes:

```
select * where contains("tensor-name", 'text_value')

select * where "tensor_name/group_name" == numeric_value
```

Make sure to wrap double-quotes with escape characters in Python:

```
select * where contains(\"tensor-name\", 'text_value')
```

{% endhint %}

#### SHAPE

```sql
select * where shape(tensor_name)[dimension_index] > numeric_value 
select * where shape(tensor_name)[1] > numeric_value # Second array dimension > value
```

#### LIMIT

```sql
select * where contains(tensor_name, 'text_value') limit num_samples
```

#### AND, OR, NOT

```sql
select * where contains(tensor_name, 'text_value') and NOT contains(tensor_name_2, numeric_value)
select * where contains(tensor_name, 'text_value') or tensor_name_2 == numeric_value

select * where (contains(tensor_name, 'text_value') and shape(tensor_name_2)[dimension_index]>numeric_value) or contains(tensor_name, 'text_value_2')
```

#### UNION and INTERSECT

```sql
(select * where contains(tensor_name, 'value')) intersect (select * where contains(tensor_name, 'value_2'))

(select * where contains(tensor_name, 'value') limit 100) union (select * where shape(tensor_name)[0] > numeric_value limit 100)
```

#### ORDER BY

<pre class="language-sql"><code class="lang-sql"><strong>-- Order by requires that sample is numeric and has 1 value, 
</strong>-- i.e. no lists or multi-dimensional arrays

-- The default order is ASCENDING (asc)

select * where contains(tensor_name, 'text_value') order by tensor_name asc
</code></pre>

#### ANY, ALL, and ALL\_STRICT

{% hint style="warning" %}
**`all`** adheres to NumPy and list logic where `all(empty_sample)` returns `True`

**`all_strict`** is more intuitive for queries so `all_strict(empty_sample)` returns `False`
{% endhint %}

```sql
select * where all(tensor_name==0) # Returns True for empty samples

select * where all_strict(tensor_name[:,2]>numeric_value) # Returns False for empty samples

select * where any(tensor_name[0:6]>numeric_value)
```

#### IN and BETWEEN

{% hint style="warning" %}
Only works for scalar numeric values and text references to class\_names
{% endhint %}

<pre class="language-sql"><code class="lang-sql">select * where tensor_name in (1, 2, 6, 10)

select * where class_label_tensor_name in ('car', 'truck')

<strong>select * where tensor_name between 5 and 20
</strong></code></pre>

**LOGICAL\_AND** and **LOGICAL\_OR**

```sql
select * where any(logical_and(tensor_name_1[:,3]>numeric_value, tensor_name_2 == 'text_value'))
```

#### REFERENCING SAMPLES IN EXISTING TENORS

```sql
# Select based on index (row_number)
select * where row_number() == 10

# Referencing values of of a tensor at index (row_number)
select * order by l2_norm(<tensor_name> - data(<tensor_name>, index))
# Finds rows of data with embeddings most similar to index 10
select * order by l2_norm(embedding - data(embedding, 10)) 
```

#### SAMPLE BY

```sql
select * sample by weight_choice(expression_1: weight_1, expression_2: weight_2, ...)
        replace True limit N
```

* **`weight_choice`** resolves the weight that is used when multiple expressions evaluate to `True` for a given sample. Options are `max_weight, sum_weight`. For example, if `weight_choice` is `max_weight`, then the maximum weight will be chosen for that sample.
* **`replace`** determines whether samples should be drawn with replacement. It defaults to `True`.
* **`limit`** specifies the number of samples that should be returned. If unspecified, the sampler will return the number of samples corresponding to the length of the dataset

#### EMBEDDING SEARCH

Deep Lake supports several vector operations for embedding search. Typically, vector operations are called by returning data ordered by the score based on the vector search method.

```sql
select * from (select tensor_1, tensor_2, <VECTOR_OPERATION> as score) order by score desc limit 10

-- THE SUPPORTED VECTOR_OPERATIONS ARE:

l1_norm(<embedding_tensor> - ARRAY[<search_embedding>]) # Order should be asc

l2_norm(<embedding_tensor> - ARRAY[<search_embedding>]) # Order should be asc

linf_norm(<embedding_tensor> - ARRAY[<search_embedding>]) # Order should be asc

cosine_similarity(<embedding_tensor>, ARRAY[<search_embedding>]) # Order should be desc

```

#### VIRTUAL TENSORS

Virtual tensors are the result of a computation and are not tensors in the Deep Lake dataset. However, they can be treated as tensors in the API.

```sql
-- "score" is a virtual tensor
select * from (select tensor_1, tensor_2, <VECTOR_OPERATION> as score) order by score desc limit 10

-- "box_beyond_image" is a virtual tensor
select *, any(boxes[:,0])<0 as box_beyond_image where ....

-- "tensor_sum" is a virtual tensor
select *, tensor_1 + tensor_3 as tensor_sum where ......
```

{% hint style="success" %}
When combining embedding search with filtering (`where` conditions), the filter condition is evaluated prior to the embedding search.&#x20;
{% endhint %}

#### GROUP BY AND UNGROUP BY

`Group by` creates a sequence of data based on the common properties that are being grouped (i.e. frames into videos). `Ungroup by` splits sequences into their individual elements (i.e. videos into images).

```sql
select * group by label, video_id # Groups all data with the same label and video_id in to the same sequence

select * ungroup by split # Splits sequences into their original pieces
```

#### EXPAND BY

`Expand by`  includes samples before and after a query condition is satisfied.

```sql
select * where <condition> expand by rows_before, rows_after 
```


# Index for ANN Search

Overview of Deep Lake's Index implementation for ANN search.

## How Deep Lake Implements an Index for ANN Search

Deep Lake implements the Hierarchical Navigable Small World (HSNW) index for Approximate Nearest Neighbor (ANN) search. The index is based on the [OSS Hsnwlib package](https://github.com/nmslib/hnswlib) with added optimizations. The implementation enables users to run queries on >35M embeddings in less than 1 second.

#### Unique aspects of Deep Lake's HSNW implementation

* Rapid index creation with multi-threading optimized for Deep Lake
* Efficient memory management that reduces RAM usage

#### Memory Management in Deep Lake

<mark style="color:green;">`RAM Cost  >>  On-disk Cost  >>  Object Storage Cost`</mark>

Minimizing RAM usage and maximizing object store significantly reduces costs of running a Vector Database. Deep Lake has a unique implementation of memory allocation that minimizes RAM requirement without any performance penalty:

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/a8UIj0ohjpnKm98rkz8X/Index_Memory_Usage.png" alt=""><figcaption><p>Memory Architecture for the Deep Lake Vector Store</p></figcaption></figure>

### Using the Index

By default, Deep Lake performs linear embedding search for up to 100,000 rows of data. Once the data exceeds that limit, the index is created and the embedding search uses ANN.  This index threshold is chosen because linear search is the most accurate, and for less than 100,000 rows, there is almost no performance penalty compared to ANN search.

You may update the threshold for creating the index using the API below:

```python
vectorstore = VectorStore(path, index_params = {threshold: <threshold_int>})
```

### Limitations

The following limitations of the index are being implemented in upcoming releases:

* If the search is performed using a combination of attribute and vector search, the index is not used and linear search is applied instead.


# Caching and Optimization

Understanding Caching to Increase Query Performance in Deep Lake

## How to Extract Maximum Performance from Your Vector Search

### Tuning the Index Parameters

The parameters of the HSNW index can be tuned using the `index_params` shown below:

```python
vectorstore = VectorStore(path, 
                          index_params = {"threshold": -1,
                                          "distance_metric":"COS",
                                          "additional_params": {
                                              "efConstruction": 600,
                                              "M": 32}})
```

Further information about the impact of the index parameters [can be found here](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

### Caching of Embeddings and Index

Either of the following operations caches the embeddings are on disk and the index in RAM:

* The index is created
* The first vector search is executed after the Vector Store is loaded

Since the first query caches critical information, subsequent queries will execute much faster compared to the first query. Since the cache is invalidated after the Vector Store is loaded or initialized, the optimal access pattern is **not** to re-load the Vector Store each search, unless you believe it was updated by another client.

{% hint style="info" %}
The embeddings are cached on disk in the following locations:

Mac: `/tmp/....`

Linux: `/var/folders/`
{% endhint %}

### Caching of Other Tensors

Tensors containing other information such as text and metadata are also cached in memory when they are used in queries. As a result, the first query that utilized this data will be slowest, with subsequent queries running much faster.&#x20;

If the data size exceeds the cache size, it will be re-fetched with every query, thus reducing query performance. The default cache size is 2 MB, and you may increase the cache size using the parameter below:

```python
vectorstore = VectorStore(path, memory_cache_size = <cache_in_MB))
```


# Sampling Datasets

Implementation of samplers in TQL

## How to sample datasets using Deep Lake's query engine

Sampling is often used when training models in order to modify the distribution of data that models are trained on. A common objective of samplers is to rebalance the data in order to achieve an more uniform distribution of classes in the training loop. Deep Lake provides a powerful API for several sampling methods via the query engine.&#x20;

{% hint style="danger" %}
Sampler queries in Deep Lake are only accessible to registered and authenticated users, and it applies usage restrictions based on your Deep Lake Plan.
{% endhint %}

**The general syntax for sampling is using the `sample by` keywords:**

```sql
select * sample by weight_choice(expression_1: weight_1, expression_2: weight_2, ...)
        replace True limit N
```

* **`weight_choice`** resolves the weight that is used when multiple expressions evaluate to `True` for a given sample. Options are `max_weight, sum_weight`. For example, if `weight_choice` is `max_weight`, then the maximum weight will be chosen for that sample.
* **`replace`** determines whether samples should be drawn with replacement. It defaults to `True`.
* **`limit`** specifies the number of samples that should be returned. If unspecified, the sampler will return the number of samples corresponding to the length of the dataset

Sampling can be performed in the query interface in the Deep Lake UI, or in the Python API as shown below.&#x20;

### Example Usage

Suppose we're working with a medical imaging dataset such as the [NIH Chest X-Ray](https://app.activeloop.ai/activeloop/nih-chest-xray-train). Let's use samplers to create a more balanced `view` of the dataset that we can use for training a model. First, let's load the dataset:

```python
import deeplake
import numpy as np
from matplotlib import pyplot as plt

ds = deeplake.load('hub://activeloop/nih-chest-xray-train')
```

Next, let's calculate the a histogram of the medical findings (`findings` tensor) and plot it.

```python
# Extract the list of class_names in a separate variable for re-use
class_names = ds.findings.info.class_names
num_classes = len(class_names)

class_count_raw = np.bincount(np.concatenate(ds.findings.numpy(aslist = True), axis=0))
```

```python
plt.bar(np.arange(num_classes), class_count_raw, tick_label = class_names)
plt.xlabel('Condition', weight='bold')
plt.xticks(rotation='vertical')
plt.ylabel('Number of Instances', weight='bold')
plt.title('Frequency per Condition', weight='bold')
plt.show()
```

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/rUgns0a5I4DTcxzBB3iS/nih_raw_histogram_edited_white.png" alt=""><figcaption></figcaption></figure>

We observe that findings such as `Hernia`, `Pneumonia`, `Fibrosis`, `Edema` , and `Emphysema` are very rare, which may cause our model to underperform when predicting these conditions. Note that even though many images have `No_Finding`, this is desirable for avoiding false positives when training models for medical imaging applications.

We can use Deep Lake Tensor-Query-Language to upsample the under-represented findings in order to create a more balanced dataset.

<pre class="language-sql"><code class="lang-sql"><strong>select * sample by max_weight(contains(findings, 'Hernia'): 20, 
</strong>                               contains(findings, 'Pneumonia'): 8, 
                               contains(findings, 'Fibrosis'): 5, 
                               contains(findings, 'Edema'): 5,
                               contains(findings, 'Emphysema'): 2, True: 1)
</code></pre>

We can run this query in the UI or in the Python API using `ds.query(...)`:

```
balanced_view = ds.query("select * sample by max_weight(contains(findings, 'Hernia'): 20, contains(findings, 'Pneumonia'): 8, contains(findings, 'Fibrosis'): 5, contains(findings, 'Edema'): 5, contains(findings, 'Emphysema'): 2, True: 1)")
```

In this sampler query, we're upsampling `Hernia`, by 20x, `Pneumonia` by 8x, `Fibrosis` by 5x, `Edema` by 5x, and `Emphysema` by 2x. Let's recalculate the histogram for the balanced dataset and compare it to the raw data histogram.&#x20;

```python
class_count_balanced = np.bincount(np.concatenate(balanced_view.findings.numpy(aslist = True), axis=0))
```

```python
X_axis = np.arange(len(class_names))

plt.figure(figsize=(8, 4))

plt.bar(X_axis - 0.2, class_count_raw, 0.4, label = 'Raw Data')
plt.bar(X_axis + 0.2, class_count_balanced, 0.4, label = 'Sampled Data')
  
plt.xticks(X_axis, class_names)
plt.xlabel('Condition', weight='bold')
plt.xticks(rotation='vertical')
plt.ylabel('Number of Instances', weight='bold')
plt.title('Frequency per Condition', weight='bold')
plt.legend()
plt.show()
```

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/ftus8WyEXLd8EZNdvs4i/nih_balanced_histogram_edited_white.png" alt=""><figcaption></figcaption></figure>

The data in the upsampled dataset has much better representation of the rare conditions. Note that since a given image may have multiple conditions, and since conditions can be correlated, upsampling by one condition may implicitly upsample another condition, if they tend to occur in the same image.&#x20;

#### Training Models on Sampled Views

The sampled `dataset view` can be passed to a dataloader just like an ordinary Deep Lake dataset. Examples of dataset training [can be found in our training tutorials](https://docs-v3.activeloop.ai/examples/dl/tutorials/training-models).

```python
pytorch_dataloader = balanced_view.pytorch(...)

for data in pytorch_dataloader:
    # Training loop
```


# Best Practices

How to use Deep Lake at scale with best practices.

## How to use Deep Lake at Scale with Best Bractices

Here are suggestions for advanced usage of Deep Lake at scale:

{% content-ref url="best-practices/creating-datasets-at-scale" %}
[creating-datasets-at-scale](https://docs-v3.activeloop.ai/technical-details/best-practices/creating-datasets-at-scale)
{% endcontent-ref %}

{% content-ref url="best-practices/training-models-at-scale" %}
[training-models-at-scale](https://docs-v3.activeloop.ai/technical-details/best-practices/training-models-at-scale)
{% endcontent-ref %}

{% content-ref url="best-practices/storage-synchronization" %}
[storage-synchronization](https://docs-v3.activeloop.ai/technical-details/best-practices/storage-synchronization)
{% endcontent-ref %}

{% content-ref url="best-practices/restoring-corrupted-datasets" %}
[restoring-corrupted-datasets](https://docs-v3.activeloop.ai/technical-details/best-practices/restoring-corrupted-datasets)
{% endcontent-ref %}

{% content-ref url="best-practices/concurrent-writes" %}
[concurrent-writes](https://docs-v3.activeloop.ai/technical-details/best-practices/concurrent-writes)
{% endcontent-ref %}


# Creating Datasets at Scale

Creating large Deep Lake datasets with high performance and reliability

## How to create Deep Lake datasets at scale

{% hint style="info" %}
This workflow assumes the reader has experience [uploading datasets using Deep Lake's distributed framework `deeplake.compute`](https://docs-v3.activeloop.ai/examples/dl/guide/parallel-computing).
{% endhint %}

### **When creating large Deep Lake datasets, it is recommended to:**

* **Parallelize the ingestion using `deeplake.compute` with a large `num_workers` (8-32)**
* **Use checkpointing to periodically auto-commit data using `.eval(... checkpoint_interval = <commit_every_N_samples>)`**
  * **If there is an error during the data ingestion, the dataset is automatically reset to the last auto-commit with valid data.**

Additional recommendations are:

* If upload errors are intermittent and error-causing samples may be skipped (like bad links), you can run `.eval(... ignore_errors=True)`.
* When uploading [linked data](https://docs.deeplake.ai/en/latest/Htypes.html#link-htype), if a data integrity check is not necessary, and if querying based on shape information is not important, you can increase the upload speed by 10-100X by setting the following parameters to `False` when [creating the linked tensor](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.create_tensor): `verify`, `create_shape_tensor` ,  `create_sample_info_tensor`

{% hint style="danger" %}
We highly recommend performing integrity checks for linked data during dataset creation, even though it slows data ingestion. This one-time check will significantly reduce debugging during querying, training, or other workflows.&#x20;
{% endhint %}

### Example Dataset Creation Using Checkpointing

In this example we upload the COCO dataset originally stored as an S3 bucket to a Deep Lake dataset stored in another S3 bucket. The images are uploaded as links and the annotations (categories, masks, bounding boxes) are stored in the Deep Lake dataset. Annotations such as pose keypoints or supercategories are omitted.

```python
import deeplake
import numpy as np
import boto3
import os
from pycocotools.coco import COCO
import getpass
```

First, let's define the S3 buckets where the source COCO data is stored, and where the Deep Lake dataset will be stored. Let's also connect to the source data via `boto3` and define a credentials dictionary (on some systems credentials, can be automatically pulled from the environment).

```python
coco_bucket = <bucket_containing_the_source_data>
deeplake_bucket = <bucket_for_storing_the_deep_lake_dataset>

creds = {'aws_access_key_id': os.environ.get('aws_access_key_id'), 
         'aws_secret_access_key': os.environ.get('aws_secret_access_key')}

# Create the connection to the source data
s3 = boto3.resource('s3', 
                    aws_access_key_id = creds['aws_access_key_id'], 
                    aws_secret_access_key = creds['aws_secret_access_key'])

s3_bucket = s3.Bucket(coco_bucket)
```

The annotations are downloaded locally for simplifying the upload code, since the COCO API was designed to read the annotations from a local file.

```python
cloud_ann_path = 'coco/annotations/instances_train2017.json'
local_ann_path = 'anns_train.json'

s3_bucket.download_file(ann_path, local_ann_path)
coco = COCO(local_ann_path)

category_info = coco.loadCats(coco.getCatIds())
```

Next, let's create an empty Deep Lake dataset at the desired path and connect it to the Deep Lake backend. We also add managed credentials for accessing linked data. In this case, the managed credentials for accessing the dataset are the same as those for accessing the linked data, but that's not a general requirement. [More details on managed credentials are available here](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials).&#x20;

```python
ds = deeplake.empty('s3://{}/coco-train'.format(deeplake_bucket), creds = creds, overwrite = True)
creds_key = <managed_creds_key>

ds.connect(org_id = <org_id>, creds_key = creds_key, token = <your_token>)
ds.add_creds_key(creds_key, managed = True)
```

Next, we define the list `category_names` that maps the numerical annotations to the index in this list. If label annotations are uploaded as text (which is not the case here), the list is auto-populated. We pass `category_names` to the `class_names` parameter during tensor creation, though it can also be updated later, or omitted entirely if the numerical labels are sufficient.

```python
category_names = [category['name'] for category in category_info]
```

```python
with ds:
    ds.create_tensor('images', htype = 'link[image]', sample_compression = 'jpg')
    ds.create_tensor('categories', htype = 'class_label', class_names = category_names)
    ds.create_tensor('boxes', htype = 'bbox')
    ds.create_tensor('masks', htype = 'binary_mask', sample_compression = 'lz4')
```

Next, we define the input iterable and `deepake.compute` function. The elements in the iterable are parallelized among the workers during the execution of the function.

```python
img_ids = sorted(coco.getImgIds())
```

```python
@deeplake.compute
def coco_2_deeplake(img_id, sample_out, coco_api, category_names, category_info, bucket, creds_key):

    anns = coco_api.loadAnns(coco_api.getAnnIds(img_id))
    img_coco = coco_api.loadImgs(img_id)[0]
            
    # First create empty arrays for all annotations
    categories = np.zeros((len(anns)), dtype = np.uint32)
    boxes = np.zeros((len(anns),4), dtype = np.float32)
    masks = np.zeros((img_coco['height'], img_coco['width'], len(anns)), dtype = bool)
    
    # Then populate the arrays with the annotations data
    for i, ann in enumerate(anns):
        mask = coco.annToMask(ann)  # Convert annotation to binary mask
        masks[:, :, i] = mask
        boxes[i,:] = ann['bbox']
        
        # Find the deep lake category_names index from the coco category_id
        categories[i] = category_names.index([category_info[i]['name'] for i in range(len(category_info)) if category_info[i]['id']==ann['category_id']][0])
    
    # Append the data to a deeplake sample
    sample_out.append({'images': deeplake.link('s3://{}/coco/train2017/{}'.format(bucket, img_coco['file_name']), creds_key = creds_key),
                       'categories': categories,
                       'boxes': boxes,
                       'masks': masks})
```

Finally, execute the `deeplake.compute` function and set `checkpoint_interval` to 25000. The dataset has a total of \~118000 samples.

```python
coco_2_deeplake(coco_api = coco, 
                bucket = coco_bucket, 
                category_names = category_names, 
                category_info = category_info, 
                creds_key = creds_key).eval(img_ids,
                                            ds, 
                                            num_workers = 8, 
                                            checkpoint_interval=25000)
```

After the upload is complete, we see commits like the one below in `ds.log()`.

```
Commit : firstdbf9474d461a19e9333c2fd19b46115348f (main) 
Author : <username>
Time   : 2023-03-27 19:18:14
Message: Auto-commit during deeplake.compute of coco_2_deeplake after 20.0% progress
Total samples processed in transform: 25000
```

**If an upload error occurs but the script completes, the dataset will be reset to the prior checkpoint and you will see a message such as:**

`TransformError: Transform failed at index <51234> of the input data on the item: <item_string>. Last checkpoint: 50000 samples processed. You can slice the input to resume from this point. See traceback for more details.`

**If the script does not complete due to a system failure or keyboard interrupt, you should load the dataset and run `ds.reset()`, or load the dataset using `ds = deeplake.load(... reset = True)`. This will restore the dataset to the prior checkpoint. You may find how many samples were successfully processed using:**

```python
len(ds) -> length of the shortest tensor
ds.max_len -> length of the longest tensor

ds.log() -> Prints how many samples were processed by the checkpointing
```


# Training Models at Scale

Train models at scale using Deep Lake

## How to optimize Deep Lake for training models at scale

There are several Deep Lake related tuning parameters that affect the speed of Deep Lake [OSS](https://docs-v3.activeloop.ai/examples/dl/guide/connecting-to-ml-frameworks) and [Performant](https://docs-v3.activeloop.ai/examples/dl/dataloaders) dataloaders. The plot below shows performance of the Deep Lake dataloaders under different scenarios, and it is discussed in detail below.

<div align="center"><figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/zngUZDV5n6fEcyW6XRci/ImageNet%20Streaming%20from%20S3%20to%20EC2%20HR.png" alt=""><figcaption><p>ImageNet data streaming speeds from S3 to a p3.8xlarge EC2 instance. The average image size is 0.114 MB. Details on the simple and complex transform are available in the appending at the end of this page. </p></figcaption></figure></div>

### Choosing the optimal dataloader

The Deep Lake Performant dataloader streams data faster compared to the OSS dataloaer, due to its C++ implementation that optimizes asynchronous data fetching and decompression.

* The Performant dataloader is \~1.5-3X faster compared to the OSS version, depending on the complexity of the transform and the number of workers available for parallelization.
* Distributed training is only available in the Performant dataloader.

### Setting `num_workers`

Both the [OSS](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.pytorch) and [Performant](https://docs.deeplake.ai/en/latest/Dataloader.html#deeplake.enterprise.DeepLakeDataLoader.pytorch) dataloaders in Deep Lake have a `num_workers` parameter that parallelizes the data fetching, decompression, and transformation.

* Increasing `num_workers` will not improve performance in GPU-bottlenecked scenarios. Therefore, we recommend starting with 2-4 workers, and increasing `num_workers` it if the GPU utilization is low.
* Increasing `num_workers` beyond the number of CPUs on a machine does not improve performance.
  * It is common for GPU machines to have 8x CPUs per GPU&#x20;
* Increasing `num_workers` linearly improves streaming speed, with diminishing returns beyond 8+ workers.
* Increasing `num_workers` beyond 16 is generally unnecessary, unless you are running complex transformations.

### Choosing the optimal `decode_method` for images

Faster dataloading is achieved by minimizing the amount of operations that take place before data is delivered to the GPU. It is important to the `decode_method` parameter in the OSS and Performant dataloaders based on the following guidelines:

* When transforming images using tools the require numpy arrays as inputs, such as [Albumentations](https://albumentations.ai/), `decode_method` should be to numpy, which is the default (No parameters changes are needed)
* When transforming images using tools the require PIL images as inputs, such as [torchvision transforms](https://pytorch.org/vision/stable/transforms.html), `decode_method` should be to `{'image_tensor_name': 'pil'}`. `torchvision.transforms.ToPIL()` should be removed from the top of the transforms stack.
  * Leaving the `decode_method` as numpy may decrease dataloading speed by up to 2X, because the image is decoded to a numpy array and then re-encoded as a PIL image, instead of being directly decoded to a PIL image.

#### APPENDIX TO THE PLOT ABOVE

The torchvision transforms used to create the comparison in the plot above are:

```python
tform_simple = transforms.Compose(
    [
        transforms.Resize((128, 128)),
        transforms.RandomAffine(20),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.repeat(int(3 / x.shape[0]), 1, 1)),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)


tform_complex = transforms.Compose(
    [
        transforms.Resize((256, 256)),
        transforms.RandomAffine(20),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5),
        transforms.RandomPerspective(distortion_scale=0.5, p=0.5),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.repeat(int(3 / x.shape[0]), 1, 1)),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)
```

&#x20;


# Storage Synchronization and "with" Context

Synchronizing data with long-term storage and achieving optimal performance using Deep Lake.

## How Deep Lake Datasets are Synchronized with Long-Term Storage

{% hint style="danger" %}
**Using `with` context when updating Deep Lake datasets is critical for achieving rapid write performance.**
{% endhint %}

### BAD PRACTICE - Code without `with` context

Any standalone update to a Deep Lake dataset is immediately pushed to the dataset's long-term storage location. Due to the high number of write operations, there may be a significant increase in runtime when the data is stored in the cloud. In the example below, an update is pushed to storage for every call to the `.append()` command.

```python
for i in range(10):
    ds.my_tensor.append(i)
```

### Code using `with` context

To increase write speeds when using Deep Lake, the `with` syntax significantly improves performance because it only pushes updates to long-term storage after the code block inside the `with` statement has been executed, or when the local cache is full. This significantly reduces the number of discreet write operations, thereby increasing the speed by up to 100X.&#x20;

```python
with ds:
    for i in range(10):
        ds.my_tensor.append(i)
```


# Restoring Corrupted Datasets

Restoring Deep Lake datasets that may be corrupted.

## How to restore a corrupted Deep Lake dataset

**Deliberate of accidental interruption of code may make a Deep Lake dataset or some of its tensors unreadable. At scale, code interruption is more likely to occur, and Deep Lake's version control is the primary tool for recovery.**

### How to Use Version Control to Retrieve Data

When manipulating Deep Lake datasets, it is recommended to commit periodically in order to create snapshots of the dataset that can be accessed later. This can be done automatically when [creating datasets with `deeplake.compute`](https://docs-v3.activeloop.ai/technical-details/best-practices/creating-datasets-at-scale), or manually using [our version control API.](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-version-control)

If a dataset becomes corrupted, when loading the dataset, you may see an error like:

```markup
DatasetCorruptError: Exception occured (see Traceback). The dataset maybe corrupted. Try using `reset=True` to reset HEAD changes and load the previous commit. This will delete all uncommitted changes on the branch you are trying to load.
```

To reset the uncommitted corrupted changes, `load` the dataset with the `reset = True` flag:

```python
ds = deeplake.load(<dataset_path>, reset = True)
```

{% hint style="danger" %}
Note: this operation deletes *all* uncommitted changes.
{% endhint %}


# Concurrent Writes

Concurrent writes in Deep Lake

## How to Write Data Concurrently to Deep Lake Datasets

Deep Lake offers 3 solutions for concurrently writing data, depending on the required scale of the application. Concurrency is not native to the Deep Lake format, so these solutions use locks and queues to schedule and linearize the write operations to Deep Lake.

### Concurrency Using External Locks&#x20;

Concurrent writes can be supported using an in-memory database that serves as the locking mechanism for Deep Lake datasets. Tools such as [Zookeper](https://zookeeper.apache.org/) or [Redis](https://redis.com/meeting/?utm_source=google\&utm_medium=cpc\&utm_campaign=redis360-brand-us-15152278745\&utm_term=redis\&utm_content=cr-all_contact_us_forms\&gclid=CjwKCAjw-7OlBhB8EiwAnoOEk4idBmC0YCgC5yjd7ehb18y2aaC5otcJedmWUh4_oLG3AhbzbvQIPRoC-mMQAvD_BwE) are highly performant and reliable and can be deployed using a few lines of code. External locks are recommended for small-to-medium workloads.

{% content-ref url="concurrent-writes/concurrency-using-zookeeper-locks" %}
[concurrency-using-zookeeper-locks](https://docs-v3.activeloop.ai/technical-details/best-practices/concurrent-writes/concurrency-using-zookeeper-locks)
{% endcontent-ref %}

### Managed Concurrency

**COMING SOON.** Deep Lake will offer a [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) that supports read (search) and write operations at scale. Deep Lake ensures the operations are performant by provisioning the necessary infrastructure and executing the underlying user requests in a distributed manner. This approach is recommended for production applications that require a separate service to handle the  high computational loads of vector search.

### Concurrency Using Deep Lake Locks

Deep Lake datasets internally support file-based locks. File-base locks are generally slower and less reliable that the other listed solutions, and they should only be used for prototyping.

#### Default Behavior

By default, Deep Lake datasets are loaded in write mode and a lock file is created. This can be avoided by specifying `read_only = True` to APIs that load datasets.&#x20;

An error will occur if the Deep Lake dataset is locked and the user tries to open it in write mode. To specify a waiting time for the lock to be released, you can specify `lock_timeout = <timeout_in_s>`  to APIs that load datasets.&#x20;

#### Manipulating Locks

Locks can manually be set or released using:

```python
from deeplake.core.lock import lock_dataset, unlock_dataset

unlock_dataset(<dataset_path>)
lock_dataset(<dataset_path>)
```


# Concurrency Using Zookeeper Locks

Using Zookeeper for locking Deep Lake datasets.

{% hint style="warning" %}
This tutorial assumes the reader has knowledge of Deep Lake APIs and does not explain them in detail. For more information, check out our [Deep Learning Quickstart](https://docs-v3.activeloop.ai/examples/dl/quickstart) or [Vector Store Quickstart](https://docs-v3.activeloop.ai/examples/rag/quickstart).
{% endhint %}

## How to Implement External Locks using Zookeeper&#x20;

[Apache Zookeeper](https://zookeeper.apache.org/) is a tool that can be used to manage Deep Lake locks and ensure that only 1 worker is writing to a Deep Lake dataset at a time. It offers a simple API for managing locks using a few lines of code.

### Setup

First, let's install Zookeper and launch a local server using Docker in the CLI.

```
pip install zookeeper

docker run --rm -p 2181:2181 zookeeper
```

### Write Locks

All write operations should be executed while respecting the lock.

Let's connect a Python client to the local server and create a `WriteLock` using:

```python
from kazoo.client import KazooClient

zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()
deeplake_writelock = zk.WriteLock("/deeplake")
```

The client can be blocked from performing operations without a WriteLock using the code below. The code will wait until the lock becomes available, and the internal Deep Lake lock should be disabled by specifying `lock_enabled=False`:

```python
from deeplake.core.vectorstore import VectorStore

with deeplake_writelock:

    # Initialize the Vector Store
    vector_store = VectorStore(<vector_store_path>, lock_enabled=False)
    
    # Add data
    vector_store.add(text = <your_text>, 
                     metadata = <your_metadata>, 
                     embedding_function = <your_embedding_function>)

    # This code can also be used with the Deep Lake LangChain Integration
    # from langchain.vectorstores import DeepLake
    # db = DeepLake(<dataset_path>, embedding = <your_embedding_function>)
    # db.add_texts(tests = <your_texts>, metadatas = <your_metadatas>, ...)

    # This code can also be used with the low-level Deep Lake API
    # import deeplake
    # ds = deeplake.load(dataset_path)
    # ds.append({...})
```

### Read Locks (Optional)

#### When Writes are Append-Only

If the write operations are only appending data, it is not necessary to use locks during read operations like as vector search. However, the Deep Lake datasets must be reloaded or re-initialized in order to have the latest available information from the write operations.&#x20;

```python
from deeplake.core.vectorstore import VectorStore

# Initialize the Vector Store 
vector_store = VectorStore(<vector_store_path>, read_only = True)

# Search for data
search_results = vector_store.search(embedding_data = <your_prompt>, 
                                     embedding_function = <your_embedding_function>)


# This code can also be used with the Deep Lake LangChain Integration
# from langchain.vectorstores import DeepLake
# db = DeepLake(<dataset_path>, embedding = <your_embedding_function>, read_only = True)
# retriever = db.as_retriever()
# qa = RetrievalQA.from_llm(llm = <your_model>, retriever = retriever)


# This code can also be used with the low-level Deep Lake API
# import deeplake
# ds = deeplake.load(<dataset_path>, read_only = True)
# dataloader = ds.dataloader().pytorch(...)
```

#### When Writes Update and Delete Data

If the write operations are updating or deleting rows of data, the read operations should also lock the dataset in order to avoid corrupted read operations.&#x20;

Let's connect a Python client to the same local server above and create a `ReadLock` . Multiple clients can have a `ReadLock` without blocking each other, but they will all be blocked by the `WriteLock` above.

```python
from kazoo.client import KazooClient

zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()
deeplake_readlock = zk.ReadLock("/deeplake")
```

The syntax for restricting operations using the `ReadLock` is:

```python
from deeplake.core.vectorstore import VectorStore

with deeplake_readlock:

    # Initialize the Vector Store 
    vector_store = VectorStore(<vector_store_path>, read_only = True)

    # Search for data
    search_results = vector_store.search(embedding_data = <your_prompt>, 
                                        embedding_function = <your_embedding_function>)


    # This code can also be used with the Deep Lake LangChain Integration
    # from langchain.vectorstores import DeepLake
    # db = DeepLake(<dataset_path>, embedding = <your_embedding_function>, read_only = True)
    # retriever = db.as_retriever()
    # qa = RetrievalQA.from_llm(llm = <your_model>, retriever = retriever)


    # This code can also be used with the low-level Deep Lake API
    # import deeplake
    # ds = deeplake.load(<dataset_path>, read_only = True)
    # dataloader = ds.dataloader().pytorch(...)
```

Congrats! You just learned how manage your own lock for Deep Lake using Zookeeper! 🎉


# Deep Lake Data Format

Understanding the data layout in Deep Lake

## Understanding Deep Lake's Data Format

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/1Oh1Vwdk4Z5ZwAqq0pmn/image.png" alt=""><figcaption></figcaption></figure>

### Tensors

Deep Lake uses a [columnar storage architecture](https://en.wikipedia.org/wiki/Column-oriented_DBMS), and the columns in Deep Lake are referred to as **`tensors`**. Data in the tensors can be added or modified, and the data in different tensors are independent of each other.

#### Hidden Tensors

When data is appended to Deep Lake, certain important information is broken up and duplicated in a separate tensor, so that the information can be accessed and queried without loading all of the data. Examples include the shape of a sample (i.e. width, height, and number of channels for an image), or the metadata from file headers that were passed to `deeplake.read('filename')`.&#x20;

### Indexing and Samples

Deep Lake datasets and their tensors are indexed, and data at a given index that spans multiple tensors are referred to as **`samples`**. Data at the same index are assumed to be related. For example, data in a `bbox` tensor at index 100 is assumed to be related to data in the tensor `image` at index 100.&#x20;

### Chunking

Most data in Deep Lake format is stored in **`chunks`**, which are a blobs of data of a pre-defined size. The purpose of chunking is to accelerate the streaming of data across networks by increasing the amount of data that is transferred per network request.

Each tensors has its own chunks, and the default chunk size is 8MB. A single chunk consists of data from multiple indices when the individual data points (image, label, annotation, etc.) are smaller than the chunk size. Conversely, when individual data points are larger than the chunk size, the data is split among multiple chunks (tiling).&#x20;

Exceptions to chunking logic are video data. Videos that are larger than the specified chunk size are not broken into smaller pieces, because Deep Lake uses efficient libraries to stream and access subsets of videos, thus making it unnecessary to split them apart.

### Groups

Multiple tensor can be combined into **`groups`**. Groups do not fundamentally change the way data is stored, but they are useful for helping Activeloop Platform understand [how different tensors are related](https://docs-v3.activeloop.ai/technical-details/data-format/tensor-relationships).

### Length of a Dataset

Deep Lake allows for ragged tensors (tensors of different length), so it is important to understand the terminology around dataset length:

* **length (`ds.len` or `len(ds)`)** - The length of the shortest tensor, as determined by its last index.
* **minimum length (`ds.min_len`)** - Same as length
* **maximum length (`ds.max_len`)** - The length of the longest tensor, as determined by its last index.&#x20;

By default, Deep Lake throws an error if a tensor is accessed at an index at which data (empty or non-empty) has not been added. In the example below, `ds.bbox[3].numpy()` would throw an error.&#x20;

To pad the unspecified data and create a virtual view where the missing samples are treated as empty data, use `ds.max_view()`. In the example below, the length of this virtual view would be 6.

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/0mw8ntA6SzflledhVm1W/image.png" alt=""><figcaption></figcaption></figure>


# Tensor Relationships

Understanding the correct data layout for successful visualization.

## Understanding the Relationships Between Deep Lake Tensors

### Indexing

Hub datasets and their tensors are indexed like `ds[index]` or `ds.tensor_name[index]`, and data at the same index are assumed to be related. For example, a `bounding_box` at index 100 is assumed to apply to the `image` at index 100.

### Relationships Between Tensors

For datasets with multiple tensors, it is important to follow the conventions below in order for the visualizer to correctly infer how tensors are related.

{% hint style="info" %}
By default, in the absence of `groups`, the visualizer assumes that all tensors are related to each other.&#x20;
{% endhint %}

This works well for simple use cases. For example, it is correct to assume that the `images`, `labels`, and `boxes` tensors are related in the dataset below:

```
ds
-> images (htype = image)
-> labels (htype = class_label)
-> boxes (htype = bbox)
```

However, if datasets are highly complex, assuming that all tensor are related may lead to visualization errors, because every tensor may not be related to every other tensor:

```
ds
-> images (htype = image)
-> vehicle_labels (htype = class_label)
-> vehicle_boxes (htype = bbox)
-> people_labels (htype = class_label)
-> people_masks (htype = binary_mask)
```

In the example above, only some of the annotation tensors are related to each other:&#x20;

* `vehicle_labels -> vehicle_boxes`: Boxes and labels describing cars, trucks, etc.
* `people_labels -> people_masks`: Binary masks and labels describing adults, toddlers, etc.

{% hint style="info" %}
The best method for disambiguating the relationships between tensors is to place them in `groups`, because the visualizer assumes that annotation tensors in different groups are not related.
{% endhint %}

In the example above, the following groups could be used to disambiguate the annotations:

```
ds
-> images (htype = image)
-> vehicles (group)
   -> vehicle_labels (htype = class_label)
   -> vehicle_boxes (htype = bbox)
-> people (group)
   -> people_labels (htype = class_label)
   -> people_masks (htype = binary_mask) 
```


# Version Control and Querying

Understanding Deep Lake's Version control and Querying Layout

## Understanding the Interaction Between Deep Lake's Versions, Queries, and Dataset Views.

Version control is the core of the Deep Lake data format, and it interacts with queries and view as follows:

* Datasets have commits and branches, and they can be traversed or merged using Deep Lake's Python API.&#x20;
* Queries are applied on top of commits, and in order to save a query result as a `view`, the dataset cannot be in an uncommitted state (no changes were performed since the prior commit).&#x20;
* Each saved `view` is associated with a particular commit, and the view itself contains information on which dataset indices satisfied the query condition.

This logical approach was chosen in order to preserve data lineage. Otherwise, it would be possible to change data on which a query was executed, thereby potentially invalidating the saved view, since the indices that satisfied the query condition may no longer be correct after the dataset was changed.&#x20;

**Please check out our** [**Getting Stated Guide**](https://docs-v3.activeloop.ai/examples/dl/guide) **to learn how to use the Python API to** [**version your data**](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-version-control)**,** [**run queries, and save views**](https://docs-v3.activeloop.ai/examples/tql)**.**&#x20;

An example workflow using version control and queries is shown below.&#x20;

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/895vvEFPvrrpyGuapREz/image.png" alt=""><figcaption></figcaption></figure>

### Version Control HEAD Commit

Unlike Git, Deep Lake's dataset version control does not have a local staging area because all dataset updates are immediately synced with the permanent storage location (cloud or local). Therefore, any changes to a dataset are automatically stored in a HEAD commit on the current branch. This means that the uncommitted changes do not appear on other branches, and uncommitted changes are visible to all users.


# Dataset Visualization

How to visualize Deep Lake datasets

## How to visualize machine learning datasets

[Deep Lake](https://app.activeloop.ai/) has a web interface for visualizing, versioning, and querying [machine learning datasets](https://datasets.activeloop.ai/). It utilizes the Deep Lake format under-the-hood, and it can be connected to datasets stored in all Deep Lake [storage locations](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options).

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/mdNDbwxNep1fLz2CI4F0/computer_vision_dataset_visualization_coco_dataset.webp)

### Visualization can be performed in 3 ways:

1. **In the** [**Deep Lake UI**](https://app.activeloop.ai/) **(most feature-rich and performant option)**
2. **In the** [**python API**](https://docs-v3.activeloop.ai/examples/dl/guide/visualizing-datasets) **using `ds.visualize()`**
3. **In your own application using** [**our integration options**](https://docs-v3.activeloop.ai/technical-details/visualization/visualizer-integration)**.**

### Requirements for correctly visualizing your own datasets

Deep Lake makes assumptions about underlying data types and relationships between tensors in order to display the data correctly. Understanding the following concepts is necessary in order to  use the visualizer:&#x20;

1. [Data Types (htypes)](https://docs.deeplake.ai/en/latest/Htypes.html)
2. [Relationships between tensors](https://docs-v3.activeloop.ai/technical-details/data-format/tensor-relationships)

### Visualizer Controls and Modes

{% embed url="<https://youtu.be/N-yvvo2_rrA>" %}

### Downsampling Data for Faster Visualization

For faster visualization of images and masks, tensors can be downsampled during dataset creation. The downsampled data are stored in the dataset and are automatically rendered by the visualizer depending on the zoom level.&#x20;

To add downsampling to your tensors, specify the downsampling factor and the number of downsampling layers during [tensor creation](https://docs.deeplake.ai/en/latest/deeplake.core.dataset.html#deeplake.core.dataset.Dataset.create_tensor):

```python
# 3X downsampling per layer, 2X layers
ds.create_tensor('images', htype = 'image', downsampling = (3,2))
```

{% hint style="warning" %}
Note: since downsampling requires decompression and recompression of data, it will slow down dataset ingestion.
{% endhint %}


# Visualizer Integration

How to embed our visualizer in your application.

## How to embed the Activeloop visualizer into your own web applications

Visualization engine allows the user to visualize, explore, and interact with Deep Lake datasets. In addition to using through the [Activeloop UI](https://app.activeloop.ai/) or [in Python](https://docs-v3.activeloop.ai/examples/dl/guide/visualizing-datasets), the Activeloop visualizer can also be embedded into your application.

### HTML iframe (Alpha)

To embed into your html page, you can use our iframe integration:

```html
<iframe src="https://app.activeloop.ai/visualizer/iframe?url=hub://activeloop/imagenet-train" width="800px" height="600px">
```

**iframe URL:** `https://app.activeloop.ai/visualizer/iframe?url=hub://$org/$ds&{checkpoint=$checkpoint}&{vs=$visualizer_state}&{token=$token}`

**Params:**

`url` - The url of the dataset \
`vs` - Visualizer state, which can be obtained from the platform url \
`token` - User token, for private datasets. If the value is \
`ask` then the UI will be populated for entering the token \
`checkpoint` - Dataset checkpoint \
`query` - Query string to apply on the dataset

### Javascript API (Alpha)

To have more fine grained control, you can embed the visualizer using Javascript:

```html
<div id='container'></div>
<script src="https://app.activeloop.ai/visualizer/vis.js"></script>
<script>
  let container = document.getElementById('container')
  window.vis.visualize("hub://activeloop/imagenet-train", null, null, container, null)
</script>
```

or to visualize private datasets with authentication

```html
<div id='container'></div>
<script src="https://app.activeloop.ai/visualizer/vis.js"></script>
<script>
  let container = document.getElementById('container')
  window.vis.visualize("hub://org/private", null, null, container, {
		requireSignin: true
	})
</script>
```

**Interface**

Below you can find definitions of the arguments.

```javascript
/// ds - Dataset url
/// commit - optional commit id
/// state - optional initial state of the visualizer
/// container - HTML element serving as container for visualizer elements
/// options - optional Visualization options
static visualize(
  ds: string,
  commit: string | null = null,
  state: string | null = null,
  container: HTMLElement,
  options: VisOptions | null
): Promise<Vis>;

/// backlink - Show backlink to platform button
/// singleSampleView - Enable single sample view through enter key
/// requireSignin - Requires signin to get access token
/// token - Token id
/// gridMode - Canvas vs Grid
/// queryString - Query to apply on the iframe
export type VisOptions = {
  backlink?: Boolean
  singleSampleView?: Boolean
  requireSignin?: Boolean
  token: string | null
  gridMode?: "canvas" | "grid"
  queryString?: string
}
```

This `visualize` returns `Promise<Vis>` which can be used to dynamically change the visualizer state. Vis supports only `query` functions for now

```jsx
class Vis
{
	/// Asynchronously runs a query and resolves the promise when query completed.
  /// In case of error in query, rejects the promise.
	query(queryString: string): Promise<void>
}
```


# Shuffling in Dataloaders

Understanding data shuffling in Deep Lake's pytorch dataloader

{% hint style="warning" %}
It is important to understand the pseudo-random shuffling in Deep Lake's dataloaders because it may affect model performance in some cases.
{% endhint %}

## How Shuffling Works in Deep Lake's PyTorch DataLoader

The Deep Lake shuffling algorithm is based upon a shuffle buffer that preloads a specified amount of data (in MB) determined by the `buffer_size` parameter in `ds.pytorch(buffer_size = 2048)`. First, the dataloader randomly selects chunks from the applicable tensors until the shuffle buffer is full. Next, the indices in shuffle buffer are randomly sampled to construct the batches that are returned by the dataloader. As the data in the shuffle buffer is consumed, new chunks are randomly selected and added to the buffer.

* In the [OSS dataloader](https://docs-v3.activeloop.ai/examples/dl/guide/connecting-to-ml-frameworks), the shuffle buffer contains the decompressed, decoded, and transformed samples. When using the PyTorch dataloaders, this corresponds to torch tensors.&#x20;
* In the [Performant dataloader](https://docs-v3.activeloop.ai/examples/dl/dataloaders), the shuffle buffer contains the non-decompressed data in the format they are stored in. For images, this typically corresponds to compressed bytes in jpeg, png, or other compressions.&#x20;
  * Since compressed data is stored more efficiently than uncompressed data, there are typically more distinct samples of data in the Performant dataloader shuffle buffer compared to the OSS shuffle buffer.&#x20;

If many chunks in the buffer contain data from the same class, which may occur if data was uploaded in non-random order, the shuffle buffer may contain fewer unique classes than if the samples were chosen fully randomly based on index. The most extreme case of reduced randomness occurs when datasets are much larger than the shuffle buffer, when they have many classes, and when those classes occur in sequence within the dataset indices.&#x20;

One example dataset is *Unshuffled* ImageNet, which has 1000 classes, 1.2M images, 140GB of data, and approximately 140 images per 16MB chunk. When the images are uploaded in sequence, the plot below shows how many unique classes are returned by the loader vs the number of images that have been returned in total. It is evident that fully randomly sampling returns more unique values than the Deep Lake dataloader.&#x20;

![](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/crMD1JdStQ6yYHclKt8F/Shuffling_Sweep_General_8_workers.png)

{% hint style="warning" %}
If reduced randomness has an impact on model performance in your workflows, the recommended countermeasures are:

* Store the dataset in a shuffled fashion such that the data does not appear in order by class. This completely mitigates the randomness concerns at the output of the data loader.
* Store the dataset with a smaller chunk size. This increases randomness because the shuffle buffer selects more discreet chunks before filling up. The current default size is 8, and reducing chunk size to 4MB significantly increases randomness (see plot above) with only a modest slowdown in data transfer speed.
* Increase the size of the shuffle buffer. This mitigates the randomness concerns but may not completely alleviate them.
  {% endhint %}


# How to Contribute

Guidelines for open source enthusiasts to contribute to our open-source data format.

## How to Contribute to Activeloop Open-Source

#### Deep Lake relies on feedback and contributions from our wonderful community. Let's make it amazing with your help! Any and all contributions are appreciated, including code profiling, refactoring, and tests.

### Providing Feedback

We love feedback! Please [join our Slack Community ](http://slack.activeloop.ai/)or [raise an issue in Github](https://github.com/activeloopai/Hub/issues).

### Getting Started With Development

Clone the repository:

```bash
git clone https://github.com/activeloopai/deeplake 
cd deeplake
```

&#x20;If you are using Linux, install environment dependencies:

```
apt-get -y update
apt-get -y install git wget build-essential python-setuptools python3-dev libjpeg-dev libpng-dev zlib1g-dev
apt install build-essential
```

If you are planning to work on videos, install codecs:

```
apt-get install -y ffmpeg libavcodec-dev libavformat-dev libswscale-dev
```

Install the package locally with plugins and development dependencies:

```
pip install -r deeplake/requirements/plugins.txt
pip install -r deeplake/requirements/tests.txt
pip install -e .
```

Run local tests to ensure everything is correct:

```
pytest -x --local . 
```

#### **Using Docker** (optional)

You can use docker-compose for running tests

```
docker-compose -f ./bin/docker-compose.yaml up --build local
```

and even work inside the docker by building the image and bashing into.

```
docker build -t activeloop-deeplake:latest -f ./bin/Dockerfile.dev .
docker run -it -v $(pwd):/app activeloop-deeplake:latest bash
$ python3 -c "import deeplake"
```

Now changes done on your local files will be directly reflected into the package running inside the docker.&#x20;

### Contributing Guidelines

#### Linting

Deep Lake uses the [black](https://pypi.org/project/black/) python linter. You can auto-format your code by running `pip install black`, and the run `black .` inside the directory you want to format.

#### Docstrings

Deep Lake uses Google Docstrings. Please refer to [this example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) to learn more.

#### Typing

Deep Lake uses static typing for function arguments/variables for better code readability. Deep Lake has a GitHub action that runs `mypy .`, which runs similar to `pytest .` to check for valid static typing. You can refer to [mypy documentation](https://mypy.readthedocs.io/en/stable/) for more information.

#### Testing

Deep Lake uses [pytest](https://docs.pytest.org/en/6.2.x/) for tests. In order to make it easier to contribute, Deep Lake also has a set of custom options defined [here](https://github.com/activeloopai/Hub/tree/main/hub/tests).

#### Prerequisites

* Understand how to write [pytest](https://docs.pytest.org/en/6.2.x/) tests.
* Understand what a [pytest fixture](https://docs.pytest.org/en/6.2.x/fixture.html) is.
* Understand what [pytest parametrizations](https://docs.pytest.org/en/6.2.x/parametrize.html) are.

#### Options

To see a list of Deep Lake's custom pytest options, run this command: `pytest -h | sed -En '/custom options:/,/\[pytest\] ini\-options/p'`.

#### Fixtures

You can find more information on pytest fixtures [here](https://docs.pytest.org/en/6.2.x/fixture.html).

* `memory_storage`: If `--memory-skip` is provided, tests with this fixture will be skipped. Otherwise, the test will run with only a `MemoryProvider`.
* `local_storage`: If `--local` is **not** provided, tests with this fixture will be skipped. Otherwise, the test will run with only a `LocalProvider`.
* `s3_storage`: If `--s3` is **not** provided, tests with this fixture will be skipped. Otherwise, the test will run with only an `S3Provider`.
* `storage`: All tests that use the `storage` fixture will be parametrized with the enabled `StorageProvider`s (enabled via options defined below). If `--cache-chains` is provided, `storage` may also be a cache chain. Cache chains have the same interface as `StorageProvider`, but instead of just a single provider, it is multiple chained in a sequence, where the last provider in the chain is considered the actual storage.
* `ds`: The same as the `storage` fixture, but the storages that are parametrized are wrapped with a `Dataset`.

Each `StorageProvider`/`Dataset` that is created for a test via a fixture will automatically have a root created, and it will be destroyed after the test. If you want to keep this data after the test run, you can use the `--keep-storage` option.

#### **Fixture Examples**

Single storage provider fixture:

```python
def test_memory(memory_storage):
    # Test will skip if `--memory-skip` is provided
    memory_storage["key"] = b"1234"  # This data will only be stored in memory

def test_local(local_storage):
    # Test will skip if `--local` is not provided
    memory_storage["key"] = b"1234"  # This data will only be stored locally

def test_local(s3_storage):
    # Test will skip if `--s3` is not provided
    # Test will fail if credentials are not provided
    memory_storage["key"] = b"1234"  # This data will only be stored in s3
```

Multiple storage providers/cache chains:

```python
from deeplake.core.tests.common import parametrize_all_storages, parametrize_all_caches, parametrize_all_storages_and_caches

@parametrize_all_storages
def test_storage(storage):
    # Storage will be parametrized with all enabled `StorageProvider`s
    pass

@parametrize_all_caches
def test_caches(storage):
    # Storage will be parametrized with all common caches containing enabled `StorageProvider`s
    pass

@parametrize_all_storages_and_caches
def test_storages_and_caches(storage):
    # Storage will be parametrized with all enabled `StorageProvider`s and common caches containing enabled `StorageProvider`s
    pass
```

Dataset storage providers/cache chains:

```
from deeplake.core.tests.common import parametrize_all_dataset_storages, parametrize_all_dataset_storages_and_caches

@parametrize_all_dataset_storages
def test_dataset(ds):
    # `ds` will be parametrized with 1 `Dataset` object per enabled `StorageProvider`
    pass

@parametrize_all_dataset_storages_and_caches
def test_dataset(ds):
    # `ds` will be parametrized with 1 `Dataset` object per enabled `StorageProvider` and all cache chains containing enabled `StorageProvider`s
    pass
```

### Benchmarks

Deep Lake uses [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/usage.html) for benchmarking, which is a plugin for [pytest](https://docs.pytest.org/en/6.2.x/).

### Here's a list of people who are building the future of data!

Deep Lake would not be possible without the work of our community.

![Activeloop Deep Lake open-source contributors](https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/h4kwtfFZG6a1yrTy5qCd/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6163746976656c6f6f7061692f687562.svg)


# Deep Lake Docs

We hope you enjoy Docs for Deep Lake.

## Activeloop Deep Lake

### Use Cases for Deep Lake

#### Deep Lake as a Data Lake For Deep Learning

* Store and organize unstructured data (images, audios, nifti, videos, text, metadata, and more) in a versioned data format optimized for Deep Learning performance.
* Rapidly query and visualize your data in order to create optimal training sets.
* Stream training data from your cloud to multiple GPUs, without any copying or bottlenecks.

#### Deep Lake as a Vector Store for RAG Applications

* Store and search embeddings and their metadata including text, jsons, images, audio, video, and more. Save the data locally, in your cloud, or on Deep Lake storage.
* Build Retrieval Augmented Generation (RAG) Apps using our integrations with [LangChain](https://docs-v3.activeloop.ai/examples/rag/langchain-integration) and [LlamaIndex](https://docs-v3.activeloop.ai/examples/rag/llamaindex-integration)
* Run computations locally or on our [Managed Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database)

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/tJAy1FylqzgHpx7b8KdH/Two_Way_Utility.png" alt=""><figcaption><p>Deep Lake Architecture for Inference and Model Development Applications.</p></figcaption></figure>

### To start using Deep Lake ASAP, check out our [Deep Learning Quickstart](https://docs-v3.activeloop.ai/examples/dl/quickstart), [RAG Quickstart](https://docs-v3.activeloop.ai/examples/rag/quickstart), and [Deep Learning Playbooks](https://docs-v3.activeloop.ai/examples/dl/playbooks).

Please check out Deep Lake's [GitHub repository](https://github.com/activeloopai/Hub) and give us a ⭐ if you like the project. &#x20;

Join our [Slack Community ](https://slack.activeloop.ai)if you need help or have suggestions for improving documentation!

### Deep Lake Docs Overview

{% content-ref url="setup/authentication" %}
[authentication](https://docs-v3.activeloop.ai/setup/authentication)
{% endcontent-ref %}

{% content-ref url="examples/dl/quickstart" %}
[quickstart](https://docs-v3.activeloop.ai/examples/dl/quickstart)
{% endcontent-ref %}

{% content-ref url="examples/rag/quickstart" %}
[quickstart](https://docs-v3.activeloop.ai/examples/rag/quickstart)
{% endcontent-ref %}

{% content-ref url="examples/dl/playbooks" %}
[playbooks](https://docs-v3.activeloop.ai/examples/dl/playbooks)
{% endcontent-ref %}

{% content-ref url="examples/dl/tutorials" %}
[tutorials](https://docs-v3.activeloop.ai/examples/dl/tutorials)
{% endcontent-ref %}

{% content-ref url="technical-details/best-practices" %}
[best-practices](https://docs-v3.activeloop.ai/technical-details/best-practices)
{% endcontent-ref %}

{% content-ref url="examples/dl/api" %}
[api](https://docs-v3.activeloop.ai/examples/dl/api)
{% endcontent-ref %}


# Installation

Installing the Deep Lake Python package

## How to Install Deep Lake

Deep Lake is a python package that can be installed using pip.&#x20;

```bash
!pip install deeplake
```

**By default, Deep Lake does not install dependencies for google-cloud, video support, and other features.** [**Details on all installation options are available here**](https://docs.deeplake.ai/en/latest/Installation.html)**.**&#x20;


# User Authentication

Registration and authentication in Deep Lake.

## How to Register and Authenticate in Deep Lake

### Registration and Login

In order to use Deep Lake features that require authentication (Activeloop storage, connecting your cloud dataset to the Deep Lake UI, etc.) you should register and login in the [Deep Lake App](https://app.activeloop.ai/).

### Authentication in Programmatic Interfaces

You can create an API token in the [Deep Lake App](https://app.activeloop.ai/) (top-right corner, user settings) and authenticate in programatic interfaces using 2 options:

#### Environmental Variable

Set the environmental variable `ACTIVELOOP_TOKEN` to your API token. In Python, this can be done using:

`os.environ['ACTIVELOOP_TOKEN'] = <your_token>`

#### Pass the Token to Individual Methods

You can pass your API token to individual methods that require authentication such as:

`ds = deeplake.load('hub://org_name/dataset_name', token = <your_token>)`


# Workload Identities (Azure Only)

How to authenticate using workload identities instead of user credentials.

## Authenticating Using Workload Identities Instead of User Credentials

Workload identities enable you to define a cloud workload that will have access to your Deep Lake organization without authenticating using Deep Lake user tokens. This enables users to manage and define Deep Lake permissions for jobs that many not be attributed to a specific user.&#x20;

Set up a Workload Identity using the following steps:

1. Define an Azure Managed Identity in your cloud
2. Attached the Azure Managed Identity to your workload
3. Create a Deep Lake Workload Identity using the Azure Managed Identity
4. Run the workload in Azure

### Step 1: Define the workload identity in Azure

1. Navigate to Managed Identities in Azure

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/FxSNv8bT0MCZ8JlKclmK/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:27:48%20PM.png" alt=""><figcaption></figcaption></figure>

2. Click `Create` a Managed Identity

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/MRLOll4cfnTqC3k9RYfF/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:28:21%20PM.png" alt=""><figcaption></figcaption></figure>

3. Select the `Subscription` and `Resource Group` containing the workload, and give the Managed Identity a `Name`. Click `Review + Create`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/E8ontP2W1PU2j4UVCKhG/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:41:40%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 2: Attached the Azure Managed Identity to your workload (Example below is for Azure ML)

When creating or updating a resource that will serve as the Client running Deep Lake, assign the Managed Identity from Step 1 to this resource.&#x20;

For example, in Azure Machine Learning Studio, when creating a compute instance, toggle `Assign Identity` and select the `Managed Identity` from Step 1.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/E6hkSEbd6X8xy6WpOzss/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%204:48:02%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 3: Create a Deep Lake Workload Identity using the Azure Managed Identity

1. Navigate to the `Permissions` tab for your organization in the [Deep Lake App](https://app.activeloop.ai/), locate the  `Workload Identities`, and select `Add.`

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/GcTSMoTZ6cio9iCyB1l1/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:59:18%20PM.png" alt=""><figcaption></figcaption></figure>

2. Specify a `Display Name`, `Client ID` (for the Managed Identity), and `Tenant ID`. The `Client ID` can be found in the main page for the Managed Identity, and the `Tenant ID` can be found in `Tenant Properties` in Azure. Click `Add`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/HtZbqZkPnSdkBfyUXtZw/Screenshot%20by%20Snip%20My%20at%20Mar%2021,%202024%20at%203:55:39%20PM.png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/zMQPM3n1KmtPz14zFp1M/Screenshot%20by%20Snip%20My%20at%20Mar%2022,%202024%20at%209:37:45%20AM.png" alt=""><figcaption></figcaption></figure>


# Storage and Credentials

How to access datasets in other clouds and manage their credentials.

## Storing Datasets in Your Own Cloud

Deep Lake can be used as a pure OSS package without any registration or relationship with Activeloop. However, registering with Activeloop offers several benefits:

* Storage provided by Activeloop
* Access to the [Tensor Database](https://docs-v3.activeloop.ai/examples/rag/managed-database) for performant vector search
* Access to [Deep Lake App](https://app.activeloop.ai/), which provides dataset visualization, querying, version control UI, dataset analytics, and other powerful features
* [Managed credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials) for Deep Lake datasets stored outside of Activeloop

{% hint style="info" %}
**When connecting data from your cloud using Managed Credentials, the data is never stored or cached in Deep Lake. All Deep Lake user interfaces (browser, python, etc.) fetch data directly from long-term storage.**
{% endhint %}

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/zlUvmMzvn3vPyPR9Pqv5/Authentication_With_Managed_Creds.png" alt=""><figcaption><p>Authentication Using Managed Credentials</p></figcaption></figure>

{% content-ref url="storage-and-creds/storage-options" %}
[storage-options](https://docs-v3.activeloop.ai/setup/storage-and-creds/storage-options)
{% endcontent-ref %}

{% content-ref url="storage-and-creds/managed-credentials" %}
[managed-credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials)
{% endcontent-ref %}


# Storage Options

How to authenticate using Activeloop storage, AWS S3, and Google Cloud Storage.

**Deep Lake datasets can be stored locally, or on several cloud storage providers including Deep Lake Storage, AWS S3, Microsoft Azure, and Google Cloud Storage.** Datasets are accessed by choosing the correct prefix for the dataset `path` that is passed to methods such as `deeplake.load(path)`, and `deeplake.empty(path)`. The path prefixes are:

<table data-header-hidden><thead><tr><th width="222.76694359979138">Storage</th><th>Path</th><th>Notes</th></tr></thead><tbody><tr><td><strong>Storage Location</strong></td><td><strong>Path</strong></td><td><strong>Notes</strong></td></tr><tr><td><strong>Local</strong></td><td><code>/local_path</code></td><td></td></tr><tr><td><strong>Deep Lake Storage</strong></td><td><code>hub://org_id/dataset_name</code></td><td></td></tr><tr><td><strong>Deep Lake Managed DB</strong></td><td><code>hub://org_id/dataset_name</code></td><td>Specify <code>runtime = {"tensor_db": True}</code> when creating the dataset</td></tr><tr><td><strong>AWS S3</strong></td><td><code>s3://bucket_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr><tr><td><strong>Microsoft Azure (Gen2 DataLake Only)</strong></td><td><code>azure://account_name/container_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr><tr><td><strong>Google Cloud</strong></td><td><code>gcs://bucket_name/dataset_name</code></td><td>Dataset can be connected to Deep Lake via <a href="managed-credentials">Managed Credentials</a></td></tr></tbody></table>

{% hint style="info" %}
Connecting Deep Lake datasets stored in your own cloud via Deep Lake [Managed Credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials) is required for accessing enterprise features, and it significantly simplifies dataset access.
{% endhint %}

## Authentication for each cloud storage provider:

### Activeloop Storage and Managed Datasets

In order to access datasets stored in Deep Lake, or datasets in other clouds that are [managed by Activeloop](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials), users must register and authenticate using the steps in the link below:

{% content-ref url="../authentication" %}
[authentication](https://docs-v3.activeloop.ai/setup/authentication)
{% endcontent-ref %}

### AWS S3

Authentication with AWS S3 has 4 options:

1. Use Deep Lake on a machine in the AWS ecosystem that has access to the relevant S3 bucket via [AWS IAM](https://aws.amazon.com/iam/), in which case there is no need to pass credentials in order to access datasets in that bucket.
2. Configure AWS through the cli using `aws configure`. This creates a credentials file on your machine that is automatically access by Deep Lake during authentication.
3. Save the `AWS_ACCESS_KEY_ID` ,`AWS_SECRET_ACCESS_KEY` , and `AWS_SESSION_TOKEN (optional)` in environmental variables of the same name, which are loaded as default credentials if no other credentials are specified.
4. Create a dictionary with the `AWS_ACCESS_KEY_ID` ,`AWS_SECRET_ACCESS_KEY` , and `AWS_SESSION_TOKEN (optional)`, and pass it to Deep Lake using:

   **Note:** the dictionary keys must be lowercase!

```python
# Vector Store API
vector_store = VectorStore('s3://<bucket_name>/<dataset_name>', 
                           creds = {
                               'aws_access_key_id': <your_access_key_id>,
                               'aws_secret_access_key': <your_aws_secret_access_key>,
                               'aws_session_token': <your_aws_session_token>, # Optional
                               }
                               )

# Low Level API
ds = deeplake.load('s3://<bucket_name>/<dataset_name>', 
                   creds = {
                       'aws_access_key_id': <your_access_key_id>,
                       'aws_secret_access_key': <your_aws_secret_access_key>,
                       'aws_session_token': <your_aws_session_token>, # Optional
                       }
                       )
```

`endpoint_url` can be used for connecting to other object storages supporting S3-like API such as [MinIO](https://github.com/minio/minio), [StorageGrid](https://www.netapp.com/data-storage/storagegrid/) and others.

### Custom Storage with S3 API

In order to connect to other object storages supporting S3-like API such as [MinIO](https://github.com/minio/minio), [StorageGrid](https://www.netapp.com/data-storage/storagegrid/) and others, simply add `endpoint_url` the the `creds` dictionary.

```python
# Vector Store API
vector_store = VectorStore('s3://...', 
                           creds = {
                               'aws_access_key_id': <your_access_key_id>,
                               'aws_secret_access_key': <your_aws_secret_access_key>,
                               'aws_session_token': <your_aws_session_token>, # Optional
                               'endpoint_url': 'http://localhost:8888'
                               }
                               )

# Low Level API
ds = deeplake.load('s3://...', 
                   creds = {
                       'aws_access_key_id': <your_access_key_id>,
                       'aws_secret_access_key': <your_aws_secret_access_key>,
                       'aws_session_token': <your_aws_session_token>, # Optional
                       'endpoint_url': 'http://localhost:8888'
                       }
                       )
```

### Microsoft Azure

Authentication with Microsoft Azure has 4 options:

1. Log in from your machine's CLI using `az login`.
2. Save the `AZURE_STORAGE_ACCOUNT`, `AZURE_STORAGE_KEY`  , or other credentials in environmental variables of the same name, which are loaded as default credentials if no other credentials are specified.
3. Create a dictionary with the `ACCOUNT_KEY` or  `SAS_TOKEN` and pass it to Deep Lake using:

   **Note:** the dictionary keys must be lowercase!

```python
# Vector Store API
vector_store = VectorStore('azure://<account_name>/<container_name>/<dataset_name>', 
                           creds = {
                               'account_key': <your_account_key>,
                               'sas_token': <your_sas_token>,
                               }
                               )

# Low Level API
ds = deeplake.load('azure://<account_name>/<container_name>/<dataset_name>', 
                   creds = {
                       'account_key': <your_account_key>, 
                       #OR
                       'sas_token': <your_sas_token>,
                       }
                       )
```

### Google Cloud Storage

Authentication with Google Cloud Storage has 2 options:

1. Create a service account, download the JSON file containing the keys, and then pass that file to the `creds` parameter in `deeplake.load('gcs://.....', creds = 'path_to_keys.json')` . It is also possible to manually pass the information from the JSON file into the `creds` parameter using:&#x20;

   ```python
   # Vector Store API
   vector_store = VectorStore('gcs://.....', 
                              creds = {<information from the JSON file>}
                              )

   # Low Level API
   ds = deeplake.load('gcs://.....', 
                      creds = {<information from the JSON file>}
                      )
   ```
2. Authenticate through the browser using the steps below. This requires that the project credentials are stored on your machine, which happens after `gcloud` is [initialized](https://cloud.google.com/sdk/gcloud/reference/init) and [logged in](https://cloud.google.com/sdk/gcloud/reference/auth) through the CLI. Afterwards, `creds` can be switched to `creds = 'cache'`.

   ```python
   # Vector Store API
   vector_store = VectorStore('gcs://.....', 
                              creds = 'browser' # Switch to 'cache' after doing this once
                              )

   # Low Level API
   ds = deeplake.load('gcs://.....', 
                      creds = 'browser' # Switch to 'cache' after doing this once
                      )
   ```


# Setting up Deep Lake in Your Cloud

How to store Deep Lake data in your own cloud and manage credentials with Deep Lake

## Connecting Data From Your Cloud Using Deep Lake Managed Credentials

Connecting data from your own cloud and managing credentials in Deep Lake unlocks several important capabilities:

* Access to performant features such as the [Deep Lake Compute Engine](https://docs-v3.activeloop.ai/setup/storage-and-creds/broken-reference)
* Access to the [Deep Lake App](https://app.activeloop.ai/) for datasets stored in your own cloud
* Simpler access to Deep Lake datasets stored in your own cloud using the Python API
  * No need for continuously specifying cloud access keys in Python

### Managed Credentials

In order for the Deep Lake to access datasets or linked tensors stored in the user's cloud, Deep Lake must authenticate the respective cloud resources. Access can be provided using access keys or using role-based access ([provisioning steps here](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/provisioning-rbac)). The video below summarizes the UI for managing your cloud credentials.&#x20;

{% embed url="<https://www.loom.com/share/74be299eec16445c84a2f3b38301a40a>" %}

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/zlUvmMzvn3vPyPR9Pqv5/Authentication_With_Managed_Creds.png" alt=""><figcaption><p>Authentication Using Managed Credentials</p></figcaption></figure>

### Default Storage

Default storage enables you to map the Deep Lake path `hub://org_id/dataset_name`to a cloud path of your choice. Subsequently, all datasets created using the Deep Lake path will be stored at the user-specified specified, and they can be accessed using API tokens and managed credentials from Deep Lake. By default, the default storage is set as Activeloop Storage, and you may change it using the UI below.

{% embed url="<https://www.loom.com/share/962f130397b344cbbfe9168519f22691>" %}

{% hint style="warning" %}
Note: that in order to visualize data in the Deep Lake browser application, it is necessary to [enable CORS](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/enabling-cors) in the bucket containing any source data.
{% endhint %}

### Connecting Deep Lake Dataset in your Cloud to the Deep Lake to App

If you do not set the Default Storage as your own cloud, Datasets in user's clouds can be connected to the [Deep Lake App](https://app.activeloop.ai/) using the Python API below. Once a dataset is connected to Deep Lake, it is assigned a Deep Lake path `hub://org_id/dataset_name`, and it can be accessed using API tokens and managed credentials from Deep Lake, without continuously having to specify cloud credentials.

#### **Connecting Datasets in the Python API**

```python
# Step 1: Create the dataset directly in the cloud using your own cloud creds
ds = deeplake.empty('s3://my_bucket/dataset_name', creds = {...})

# Step 2: Connect the dataset to Deep Lake and specify the managed credentials
# (creds_key) for accessing the data (See Managed Credentials above)
ds.connect(org_id = 'org_id', creds_key = 'my_creds_key', token = 'my_token')

OR

ds.connect(dest_path = 'hub://org_id/dataset_name', creds_key = 'my_creds_key', token = 'my_token')
```

{% hint style="info" %}
Specifying `org_id` creates the dataset in the specified org using the `dataset_name` from the cloud path.&#x20;

Specifying the `dest_path` creates the dataset at the `org_id` and `dataset_name` from the specified path.&#x20;
{% endhint %}

### Using Manage Credentials with Linked Tensors

Managed credentials can be used for accessing data stored in [linked tensors](https://docs.deeplake.ai/en/latest/Htypes.html#link-htype). Simply add the managed credentials to the dataset's `creds_keys` and assign them to each sample.

```python
ds.create_tensors('images', htype = 'link[image]', sample_compression = 'jpeg')

ds.add_creds_key('my_creds_key', managed=True)

ds.images.append(deeplake.link(link_to_sample, creds_key = 'my_creds_key')
```


# Microsoft Azure

Azure-specific information for connecting data to Deep Lake

## Azure-Specific Information for Connecting Data to Deep Lake

{% content-ref url="microsoft-azure/provisioning-federated-credentials" %}
[provisioning-federated-credentials](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/provisioning-federated-credentials)
{% endcontent-ref %}

{% content-ref url="microsoft-azure/enabling-cors" %}
[enabling-cors](https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/enabling-cors)
{% endcontent-ref %}


# Provisioning Federated Credentials

How to setup Federated Credentials in Azure

## Setting up Federated Credentials in Microsoft Azure

The most secure method for connecting data from your Azure storage to Deep Lake is using Federated Credentials, which are set up using the steps below:

### Step 1: Register Application Credentials with the Microsoft Identity Platform

1\. Login to the Azure account where the App will be registered and where the data is stored.

2\. Go to the `App Registrations` page in the Azure UI, which can be done by searching "App registrations" in the console.

3\. Click on `Register an application` or `New registration`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/yGAa8eTLZCG4bS3IBUZr/Screen%20Shot%202023-06-04%20at%208.39.56%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Enter the `Name` and `Supported account type` (`Personal Microsoft Accounts` are not supported) and click `Register`

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/r5yRwskMhF68yGLlo2F8/Screen%20Shot%202023-06-04%20at%208.47.45%20PM.png" alt=""><figcaption></figcaption></figure>

5\. In the application console, click `Certificates & secrets`. &#x20;

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/daOZzoyOIhu7M1udygiZ/Screen%20Shot%202023-06-04%20at%209.00.11%20PM.png" alt=""><figcaption></figcaption></figure>

6\. Click on `Federated credentials` and `Add credential`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/yfVj2yDGQ7eknYDR0kcf/Screen%20Shot%202023-06-05%20at%2010.37.45%20AM.png" alt=""><figcaption></figcaption></figure>

7\. Click on `Select scenario` and select `Other issuer`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/77CZtJctuJEm5ljPBNoU/Screen%20Shot%202023-06-05%20at%2010.41.30%20AM.png" alt=""><figcaption></figcaption></figure>

8\. Enter the following information in the form, and click `Add`.

* **Issuer:** <https://cognito-identity.amazonaws.com>
  * This is for trusting Activeloop's Cognito issuer. There's no need to create AWS Cognito by the user.
* **Subject identifier:** us-east-1:7bc30eb1-bac6-494b-bf53-5747849d45aa
* **Name:** enter a name with your choice
* **Description (optional):** enter description a with your choice
* **Audience:** us-east-1:57e5de2f-e2ec-4514-b9b0-f3bb8c4283c3

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/dzSEZYUifyzqlrLkiTqO/Screen%20Shot%202023-06-05%20at%2010.52.31%20AM.png" alt=""><figcaption></figcaption></figure>

### Step 2a: Apply the Application Credentials to your Azure storage account&#x20;

{% hint style="warning" %}
Skip to 2b if you want to assign Application Credentials to a specific Azure container&#x20;
{% endhint %}

1\. Go to the `Storage accounts` page in the Azure UI, which can be done by searching "Storage accounts" in the console.

2\. Select the `Storage account` to which you want to add Application Credentials.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/ytoy5VQSCXtrg67ob7E3/Screen%20Shot%202023-06-05%20at%203.50.53%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Select `Access Control (IAM)` and click `Add`, and `select Add role assignment`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/yZIUXCVCD2cf0UEVbuvR/Screen%20Shot%202023-06-05%20at%204.07.05%20PM.png" alt=""><figcaption></figcaption></figure>

5\. Search and select `Storage Blob Data Contributor` under the role names and click `Next`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/FRpsWgEHhDBZeobTeNsD/Screen%20Shot%202023-06-05%20at%204.12.07%20PM.png" alt=""><figcaption></figcaption></figure>

6\. Click on the `Select members` link, and in the tab that opens up on the right, search by name and select the application you created in Step 1. Click `Select` at the bottom of the page.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/i1lSZQEYSdrCTKNhkhqb/Screen%20Shot%202023-06-05%20at%204.20.14%20PM.png" alt=""><figcaption></figcaption></figure>

&#x20;7\. The application should appear in the list of Members, at which point you can click `Review + assign`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/IizCP1SV0yANicjqnk8f/Screen%20Shot%202023-06-05%20at%204.31.31%20PM.png" alt=""><figcaption></figcaption></figure>

### Step 2b: Apply the Application Credentials to a specific Azure container in your Azure storage account

1\. Go to the `Storage accounts` page in the Azure UI, which can be done by searching "Storage accounts" in the console.

2\. Select the `Storage account` to which you want to add Application Credentials.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/ytoy5VQSCXtrg67ob7E3/Screen%20Shot%202023-06-05%20at%203.50.53%20PM.png" alt=""><figcaption></figcaption></figure>

3. Select the `Container` to which you add the Application Credentials.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/M3I8L0tX0TXHDwKmZdQx/Screen%20Shot%202023-06-05%20at%204.48.26%20PM.png" alt=""><figcaption></figcaption></figure>

4\. Select `Access Control (IAM)` and click `Add`, and `select Add role assignment`.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/HL5XAQUPLl8td8KR8tUX/Screen%20Shot%202023-06-05%20at%204.56.32%20PM.png" alt=""><figcaption></figcaption></figure>

### IMPORTANT TO PERFORM STEPS BELOW TO COMPLETE 2b - PLEASE DO NOT SKIP

5\. **Perform substeps 5-7 from Step 2a above, in order to add the Application Credentials to the Container**

6\. **Execute the steps in Step 2a above on your Storage Account, except set the Storage Account Role Assignment to `Storage Blob Delegator` in substep 5.**


# Enabling CORS

How to enable Cross-Origin Resource Sharing in your Azure account.

## Enabling CORS in Azure for Data Visualization

Cross-Origin Resource Sharing (CORS) is typically enabled by default in Azure. If that's not the case in your Azure account, in order to visualize Deep Lake datasets stored in your own Azure storage in the [Deep Lake app](https://app.activeloop.ai/), please enable [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in the storage account containing the Deep Lake dataset and any source data in linked tensors.

### Steps for enabling CORS in Azure

1\. Login to the Azure.

2\. Navigate to the `Storage account` with the relevant data.

3\. Open the `Resource sharing (CORS)` section on the left nav.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/imHCfdgJtJqzePlE5Kne/Screen%20Shot%202023-06-21%20at%209.41.27%20AM.png" alt=""><figcaption></figcaption></figure>

4\. Add the following items to the permissions.

<figure><img src="https://content.gitbook.com/content/1YVqlvZPvs9bGBYtDupb/blobs/nL2NF2T8Vi2BZg2fRvoU/Screen%20Shot%202023-06-21%20at%209.45.00%20AM%20edited.png" alt=""><figcaption></figcaption></figure>

| Allowed origins             | Allowed methods | Allowed headers |
| --------------------------- | --------------- | --------------- |
| <https://app.activeloop.ai> | GET, HEAD       | \*              |




---

[Next Page](/llms-full.txt/1)

