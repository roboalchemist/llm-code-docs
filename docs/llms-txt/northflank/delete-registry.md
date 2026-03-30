# Source: https://northflank.com/docs/v1/api/team/integrations/delete-registry.md

# Delete registry

Deletes a set of registry credential data.

Required permission: Account > Credentials > General > Delete

**Path parameters:**

{object}
- `credentialId`: (string) (required) ID of the registry credential

**Response body:**

{object}
- `data`: {object}

## API reference

DELETE /v1/integrations/registries/{credentialId}

DELETE /v1/teams/{teamId}/integrations/registries/{credentialId}

### Example Response

200 OK: The operation was performed successfully.

```json
{
  "data": {}
}
```

## CLI reference

$ northflank delete registry-credentials

Options:

- `--credentialId <credentialId>`: ID of the registry credential

- `--verbose `: Verbose output

- `--quiet `: No console output

- `--force `: Don't ask for confirmation

- `-o --output <format>`: Output formatting 

### Example Response

 The operation was performed successfully.

```json
{}
```

## JavaScript client reference

### Example request



```javascript
await apiClient.delete.registryCredentials({
  parameters: {
    "credentialId": "example-credentials"
  }    
});
```

### Example Response

 The operation was performed successfully.

```json
{
  "data": {},
  "rawResponse": "...",
  "request": "...",
  "error": "..."
}
```

Previous: [Update registry](/docs/v1/api//team/integrations/update-registry)

Next: [List SSH identities](/docs/v1/api//team/integrations/list-ssh-identities)