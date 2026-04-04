# Source: https://docs-v3.activeloop.ai/v3.0.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.0.x/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/3.1.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/3.1.1/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials.md

# Storage & Credentials

## Storing Datasets in Your Own Cloud

Deep Lake can be used as a pure OSS package without any registration or relationship with Activeloop. However, registering with Activeloop offers several benefits:

* Storage provided by Activeloop
* Access to the [Tensor Database](https://docs-v3.activeloop.ai/v3.8.27/performance-features/managed-database) for performant vector search
* Access to [Deep Lake App](https://app.activeloop.ai/), which provides dataset visualization, querying, version control UI, dataset analytics, and other powerful features
* [Managed credentials](https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials) for Deep Lake datasets stored outside of Activeloop

{% hint style="info" %}
**When connecting data from your cloud using Managed Credentials, the data is never stored or cached in Deep Lake. All Deep Lake user interfaces (browser, python, etc.) fetch data directly from long-term storage.**
{% endhint %}

<figure><img src="https://content.gitbook.com/content/k6wVYPeYExL0GTAkhW6w/blobs/V7iTsztwIX61IRQcB9IR/Authentication_With_Managed_Creds.png" alt=""><figcaption><p>Authentication Using Managed Credentials</p></figcaption></figure>

{% content-ref url="storage-and-credentials/storage-options" %}
[storage-options](https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/storage-options)
{% endcontent-ref %}

{% content-ref url="storage-and-credentials/managed-credentials" %}
[managed-credentials](https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials)
{% endcontent-ref %}
