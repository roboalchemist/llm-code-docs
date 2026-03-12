# Source: https://docs-v3.activeloop.ai/v3.6.0/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/example-code/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/example-code/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/example-code/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/example-code/tutorials/vector-store/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/examples/rag/tutorials/vector-search-options.md

# Source: https://docs-v3.activeloop.ai/examples/rag/tutorials/vector-search-options.md

# Vector Search Options

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
