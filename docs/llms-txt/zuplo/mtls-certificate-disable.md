# Source: https://www.zuplo.com/docs/cli/mtls-certificate-disable.md

# Zuplo CLI: Mtls Certificate Disable

<CliCommand
  command="mtls-certificate disable"
  description="Disables an mTLS certificate for all environment types"
  options={[
  {
    "name": "cert-id",
    "type": "string",
    "description": "The ID of the certificate to disable",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "account",
    "type": "string",
    "description": "The account name",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "project",
    "type": "string",
    "description": "The project name",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 mtls-certificate disable --cert-id cert_abc123",
    "Disable certificate for all environment types"
  ],
  [
    "$0 mtls-certificate disable \\\n  --cert-id cert_abc123 \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates disable --cert-id <id> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
