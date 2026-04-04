# Source: https://www.zuplo.com/docs/cli/mtls-certificate-delete.md

# Zuplo CLI: Mtls Certificate Delete

<CliCommand
  command="mtls-certificate delete"
  description="Deletes an mTLS certificate by ID"
  options={[
  {
    "name": "cert-id",
    "type": "string",
    "description": "The ID of the certificate to delete",
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
    "$0 mtls-certificates delete --cert-id cert_abc123",
    "Delete an mTLS certificate"
  ],
  [
    "$0 mtls-certificates delete \\\n  --cert-id cert_abc123 \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates delete --cert-id <id> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
