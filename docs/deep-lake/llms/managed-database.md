# Source: https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/performance-features/managed-database.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/examples/rag/managed-database.md

# Source: https://docs-v3.activeloop.ai/examples/rag/managed-database.md

# Managed Tensor Database

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
