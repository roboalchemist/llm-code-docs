# Source: https://docs.gitguardian.com/ggscout-docs/sync-secrets.md

# Secret synchronization

> The ggscout sync-secrets command that writes unvaulted secrets from GitGuardian into configured secrets managers for remediation.

# Secret synchronization

The `sync-secrets` command allows ggscout to receive secrets from your GitGuardian platform and write them directly into your integrated secrets managers. This enables a secure way to provision secrets discovered elsewhere into your vault infrastructure.

## How sync-secrets Works

1. **GitGuardian identifies unvaulted secrets** in your monitored sources
2. **You mark secrets for vaulting** through the GitGuardian platform
3. **ggscout receives sync instructions** from GitGuardian when running `sync-secrets`
4. **ggscout writes the secrets** to your configured destination integrations

## Example Workflow

1. **Secret Discovery**: GitGuardian finds a leaked secret in your code. Thanks to the inventory provided by ggscout, you can see that this secret is not vaulted.
2. **Platform Review**: Security team reviews the secret in GitGuardian platform
3. **Mark for Vaulting**: Team marks the secret to be moved to HashiCorp Vault
4. **Automatic Sync**: ggscout `sync-secrets` command receives the instruction
5. **Vault Writing**: Secret is securely written to the specified Vault path
6. **Confirmation**: GitGuardian platform is notified of successful vaulting

## Requirements

To use the `sync-secrets` command, you need:

- **GitGuardian API token with `nhi:write-vault` scope** - See [GitGuardian Authentication](./configure-ggscout#1-gitguardian-authentication) for setup instructions
- **Integration configured in `read/write` or `write` mode** - Only [certain integrations](#integration-write-support) support writing
- **Proper write permissions** in your destination secrets manager

## Command Usage

```bash
# Write secrets from GitGuardian directly into your destination integration
ggscout sync-secrets config.toml
```

The sync-secrets command is typically run on a schedule (every minute in production deployments) to ensure secrets are synchronized promptly when requested through the GitGuardian platform.

## Integration Write Support

Not all integrations support writing secrets. The table below shows which integrations support the `sync-secrets` command:

| Integration Type | Integration Name | Write Support | Notes |
|------------------|------------------|---------------|-------|
| **Secrets Managers** | HashiCorp Vault (`hashicorpvault`) | â Yes | Full read/write support |
| | AWS Secrets Manager (`awssecretsmanager`) | â Yes | Full read/write support |
| | CyberArk Secrets Manager SaaS (`cyberarksaas`) | â Yes | Full read/write support |
| | CyberArk Secrets Manager Self-Hosted (`cyberarkselfhosted`) | â Yes | Full read/write support |
| | Akeyless (`akeyless`) | â Yes | Full read/write support |
| | Delinea Secret Server (`delineasecretserver`) | â Yes | Full read/write support |
| | Azure Key Vault (`azurekeyvault`) | â No | Read-only support |
| | Google Secret Manager (`googlesecretsmanager`) | â No | Read-only support |
| **CI/CD Systems** | GitLab CI (`gitlabci`) | â No | Read-only support |
| **Infrastructure** | Kubernetes (`kubernetes`) | â No | Read-only support |

:::info
Integrations that don't support writing can still be used for secret discovery and monitoring with the `fetch` and `fetch-and-send` commands.
:::

## Configuration Example

To enable writing, set the integration mode to `read/write` or `write`:

```toml
[sources.my-vault]
type = "hashicorpvault"
vault_address = "https://vault.example.com"
mode = "read/write"  # Enables both reading and writing
# ... other configuration options
```

## Deployment Considerations

### Scheduling

The `sync-secrets` command should run frequently to ensure timely secret provisioning:

- **Production**: Every minute (`* * * * *`)
- **Development**: Every 5 minutes (`*/5 * * * *`)

### Error Handling

ggscout handles various error scenarios gracefully:

- **Permission errors**: Logged with details for debugging
- **Already exists**: Can be configured as recoverable or non-recoverable
- **Network issues**: Retry logic with exponential backoff
- **Invalid data**: Clear error messages for troubleshooting

## Troubleshooting

### Common Issues

**Authentication Failures**
- Verify the GitGuardian API token has `nhi:write-vault` scope
- Check that integration credentials have write permissions

**Permission Denied**
- Review vault policies and ensure write access to target paths
- Verify service account permissions in cloud environments

**Secret Already Exists**
- Configure error handling policy for duplicate secrets
- Review vault versioning settings

**Network Connectivity**
- Ensure ggscout can reach both GitGuardian platform and destination vault
- Check firewall rules and network policies

### Debug Mode

Enable debug logging for detailed troubleshooting:

```bash
ggscout sync-secrets config.toml --verbose debug
```

This provides detailed information about:
- API calls to GitGuardian platform
- Authentication attempts
- Write operations to destination vaults
- Error details and stack traces
