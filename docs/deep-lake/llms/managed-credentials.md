# Source: https://docs-v3.activeloop.ai/v3.0.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/3.1.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/3.1.1/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/storage-and-creds/managed-credentials.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials.md

# Setting up Deep Lake in Your Cloud

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
