# Source: https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/enterprise-features/compute-engine.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/compute-engine.md

# Compute Engine

## Overview of Deep Lake's Optimized Compute Engine built in C++

#### Compute Engine maximize performance of compute-heavy Deep Lake's features, such as distributed dataloading or large queries, by running certain operations in C++.

**The interface for the Compute Engine is still in Python**, and it is installed using `pip install "deeplake[enterprise]"`, which delivers the compiled C++ code from binaries.&#x20;

{% hint style="warning" %}
In order to use Compute Engine, Deep Lake data must be stored in Deep Lake Storage, or in the user's cloud while being connected to Deep Lake using [Managed Credentials](https://docs-v3.activeloop.ai/v3.6.18/storage-and-credentials/managed-credentials).&#x20;
{% endhint %}

### Features in the Optimized Compute Engine:

{% content-ref url="compute-engine/querying-datasets" %}
[querying-datasets](https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/compute-engine/querying-datasets)
{% endcontent-ref %}

{% content-ref url="compute-engine/performant-dataloader" %}
[performant-dataloader](https://docs-v3.activeloop.ai/v3.6.18/enterprise-features/compute-engine/performant-dataloader)
{% endcontent-ref %}
