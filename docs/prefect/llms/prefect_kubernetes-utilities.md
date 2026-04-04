# Source: https://docs.prefect.io/integrations/prefect-kubernetes/api-ref/prefect_kubernetes-utilities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# utilities

# `prefect_kubernetes.utilities`

Utilities for working with the Python Kubernetes API.

## Classes

### `KeepAliveClientRequest` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/utilities.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

aiohttp only directly implements socket keepalive for incoming connections
in its RequestHandler. For client connections, we need to set the keepalive
ourselves.

Refer to [https://github.com/aio-libs/aiohttp/issues/3904#issuecomment-759205696](https://github.com/aio-libs/aiohttp/issues/3904#issuecomment-759205696)

**Methods:**

#### `send` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/utilities.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
send(self, conn: Connection) -> ClientResponse
```


Built with [Mintlify](https://mintlify.com).