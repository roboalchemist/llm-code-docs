# Source: https://docs.prefect.io/v3/api-ref/python/prefect-runtime-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.runtime`

Module for easily accessing dynamic attributes for a given run, especially those generated from deployments.

Example usage:

```python  theme={null}
from prefect.runtime import deployment

print(f"This script is running from deployment {deployment.id} with parameters {deployment.parameters}")
```


Built with [Mintlify](https://mintlify.com).