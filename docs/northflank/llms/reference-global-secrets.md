# Source: https://northflank.com/docs/v1/application/secure/reference-global-secrets.md

# Reference global secrets

Global secrets can be referenced directly in your template definitions to inject configuration and sensitive data. You can choose when secrets are resolved: at template execution time or at container runtime.

## Syntax

**Template-time resolution** (`${}`):

```
${secrets.<SECRET_ID>.values.<KEY_PATH>}
${secrets.<SECRET_ID>.files.<FILE_ID>.path}
```

Values are replaced when the template runs and appear in template run logs.

**Runtime resolution** (`${{}}`):

```
${{secrets.<SECRET_ID>.values.<KEY_PATH>}}
${{secrets.<SECRET_ID>.files.<FILE_ID>.path}}
```

Values are resolved when containers start and do NOT appear in template run logs. Use this for sensitive data.

## Accessing values

Use dot notation to access nested values:

```json
{
  "runtimeEnvironment": {
    "DATABASE_HOST": "${secrets.db-config.values.DB_HOST}",
    "DATABASE_PORT": "${secrets.db-config.values.DB_PORT}",
    "DATABASE_PASSWORD": "${{secrets.db-config.values.DB_PASSWORD}}"
  }
}
```

Arrays can be referenced directly:

```json
{
  "ports": [{
    "security": {
      "policies": [{
        "addresses": "${secrets.network.values.allowedIPs}",
        "action": "ALLOW"
      }]
    }
  }]
}
```

## Accessing files

Reference files using their identifier (not path):

```json
{
  "runtimeFiles": {
    "/etc/ssl/cert.pem": {
      "data": "${secrets.ssl-certs.files.cert.data}",
      "encoding": "utf-8"
    },
    "/etc/ssl/key.pem": {
      "data": "${{secrets.ssl-certs.files.key.data}}",
      "encoding": "utf-8"
    }
  }
}
```

## Secret inheritance

The [Secret Inheritance node](/docs/v1/application/infrastructure-as-code/template-nodes#secret-inheritance) allows you to merge multiple global secrets in a specific order within your template. This enables layered configurations by combining base settings with overrides.

### How it works

Add a Secret Inheritance node to your template:

```json
{
  "kind": "SecretInheritance",
  "ref": "merged-config",
  "spec": {
    "secrets": [
      "base-secrets"
      "club-secrets"
      ],
    "requiredKeys": [
      "API_KEY", 
      "DATABASE_HOST"
      ]
  }
}
```

Secrets are merged in order, with the last secret taking precedence for conflicting keys. Objects are deeply merged, while arrays and primitives are replaced.

### Accessing merged data

```json
{
  "runtimeEnvironment": {
    "API_KEY": "${{refs.merged-config.values.API_KEY}}",
    "DB_HOST": "${refs.merged-config.values.DATABASE_HOST}"
  }
}
```

### Required validation

Specify `requiredKeys` and `requiredFiles` to enforce that critical configuration is present in the merged result. The template run will fail if any required items are missing.

## Visual editor considerations

When using the visual template editor, file encoding fields may be removed on save. Use the code editor for custom encoding values or dynamic file paths.

## Next steps

- [Tag your workloads and resources: Create tags to assign to your Northflank workloads and resources to help keep track of them.](/v1/application/release/tag-workloads-and-resources)
- [Link connection details to group: Use your database in your application by linking it to a secret group.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)
