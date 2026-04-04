# Source: https://docs-v3.activeloop.ai/v3.0.x/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.0.15/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/3.1.0/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/3.1.1/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/storage-and-credentials/managed-credentials/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/storage-and-credentials/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/storage-and-creds/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/setup/storage-and-creds/managed-credentials/microsoft-azure/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/amazon-web-services/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/google-cloud/enabling-cors.md

# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/enabling-cors.md

# Enabling CORS

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
