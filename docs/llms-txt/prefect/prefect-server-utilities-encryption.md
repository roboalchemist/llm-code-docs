# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-encryption.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# encryption

# `prefect.server.utilities.encryption`

Encryption utilities

## Functions

### `encrypt_fernet` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/encryption.py#L40" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
encrypt_fernet(session: AsyncSession, data: Mapping[str, Any]) -> str
```

### `decrypt_fernet` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/encryption.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
decrypt_fernet(session: AsyncSession, data: str) -> dict[str, Any]
```


Built with [Mintlify](https://mintlify.com).