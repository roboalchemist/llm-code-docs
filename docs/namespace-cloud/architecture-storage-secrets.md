<!-- Source: https://namespace.so/docs/architecture/storage/secrets -->

# Secrets

Never store sensitive values like API keys, passwords, or tokens as plaintext in workflow files or configuration.
Namespace Secrets provide a secure way to store and manage sensitive information across your workloads.

## Managing Secrets

You can manage secrets using the [CLI](/docs/reference/cli/vault-add) or the [VaultService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.vault.v1beta).

Secrets are **versioned** — each update creates a new version. You can use optimistic concurrency control
to prevent concurrent modifications by passing the current version when updating or deleting a secret.

Secrets can optionally be marked as **revealable** at creation time. Only revealable secrets can have their
value retrieved later via the API or CLI. This setting is immutable after creation.

**Labels** can be attached to secrets at creation time for organization and filtering. Labels are immutable
and shared across all versions of a secret.

## Using Secrets in Instances

Secrets can be injected as environment variables into containers at instance creation time.
Use the `env_vars` field in `ContainerRequest` with `from_secret_id` set to the secret's object ID:

```
{
  "env_vars": [
    { "name": "DATABASE_URL", "from_secret_id": "secret-object-id" }
  ]
}
```

The secret value is resolved at instance creation time and injected into the container's environment.
No secrets are injected by default — they must be explicitly requested.

## Encryption at Rest

All secrets stored in Namespace are encrypted at rest using industry-standard encryption algorithms. Your sensitive data is never stored in plaintext on our systems.

## Comprehensive Audit Logging

Every secret access — whether revealed, created, updated, or deleted — emits a detailed, immutable [audit log](/docs/workspaces/security#audit-logs). This provides complete visibility into how and when your secrets are being used, supporting compliance and security monitoring requirements.

Last updated March 20, 2026
