# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/storage-and-creds.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds.md

# Storage and Credentials

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
