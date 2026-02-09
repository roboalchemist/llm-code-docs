# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/identity-provider-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl identity-provider create

> Creates a new identity provider.

```
firectl identity-provider create [flags]
```

### Examples

```
# Create SAML identity provider
firectl identity-provider create --display-name="Company SAML" \
  --saml-metadata-url="https://company.okta.com/app/xyz/sso/saml/metadata"

# Create OIDC identity provider
firectl identity-provider create --display-name="Company OIDC" \
  --oidc-issuer="https://auth.company.com" \
  --oidc-client-id="abc123" \
  --oidc-client-secret="secret456"

# Create OIDC identity provider with multiple domains
firectl identity-provider create --display-name="Example OIDC" \
  --oidc-issuer="https://accounts.google.com" \
  --oidc-client-id="client123" \
  --oidc-client-secret="secret456" \
  --tenant-domains="example.com,example.co.uk"
```

### Flags

```
      --display-name string            The display name of the identity provider (required)
      --dry-run                        Print the request proto without running it.
      --enable-jit-user-provisioning   Enable Just-In-Time (JIT) user provisioning. When enabled, users are automatically created on first SSO login if they don't already exist.
  -h, --help                           help for create
      --oidc-client-id string          The OIDC client ID for OIDC providers
      --oidc-client-secret string      The OIDC client secret for OIDC providers
      --oidc-issuer string             The OIDC issuer URL for OIDC providers
  -o, --output Output                  Set the output format to "text", "json", or "flag". (default text)
      --saml-metadata-url string       The SAML metadata URL for SAML providers
      --tenant-domains string          Comma-separated list of allowed domains for the organization (e.g., 'example.com,example.co.uk'). If not provided, domain will be derived from account email.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
