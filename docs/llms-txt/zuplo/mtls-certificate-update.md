# Source: https://www.zuplo.com/docs/cli/mtls-certificate-update.md

# Zuplo CLI: Mtls Certificate Update

<CliCommand
  command="mtls-certificate update"
  description="Updates the environment settings for an mTLS certificate"
  options={[
  {
    "name": "cert-id",
    "type": "string",
    "description": "The ID of the certificate to update",
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
  },
  {
    "name": "environment-type",
    "type": "array",
    "description": "Environment types where the certificate should be enabled (can be repeated: --environment-type development --environment-type production)",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "choices": [
      "development",
      "preview",
      "production"
    ]
  }
]}
  examples={[
  [
    "$0 mtls-certificate update --cert-id cert_abc123 --environment-type production",
    "Update certificate to be enabled only for production environment type"
  ],
  [
    "$0 mtls-certificate update \\\n  --cert-id cert_abc123 \\\n  --environment-type development \\\n  --environment-type preview \\\n  --environment-type production",
    "Update certificate to be enabled for all environment types"
  ],
  [
    "$0 mtls-certificate update \\\n  --cert-id cert_abc123 \\\n  --environment-type development \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates update --cert-id <id> --environment <env> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
