# Source: https://grafbase.com/docs/cli/commands/trust.md

# Grafbase Trust Command

Submit a trusted documents manifest to the platform for gateway document fetching.

**Usage:**

```bash
grafbase trust --manifest <MANIFEST> --client-name <CLIENT_NAME> <GRAPH_REF>
```

**Arguments:**

- `<GRAPH_REF>`: Graph reference that uses the format `account/graph@branch`.

**Options:**

- `-m, --manifest <MANIFEST>`: Path to the trusted documents manifest file.
- `-c, --client-name <CLIENT_NAME>`: Name of the client.

## Examples

Read more about [trusted documents](https://grafbase.com/docs/gateway/security/trusted-documents.md).