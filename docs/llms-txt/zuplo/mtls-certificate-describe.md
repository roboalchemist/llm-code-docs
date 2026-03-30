# Source: https://www.zuplo.com/docs/cli/mtls-certificate-describe.md

# Zuplo CLI: Mtls Certificate Describe

<CliCommand
  command="mtls-certificate describe"
  description="Describes an mTLS certificate"
  options={[
  {
    "name": "cert-id",
    "type": "string",
    "description": "The ID of the certificate to describe",
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
    "$0 mtls-certificates describe --cert-id cert_abc123",
    "Get details about an mTLS certificate"
  ],
  [
    "$0 mtls-certificates describe \\\n  --cert-id cert_abc123 \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates describe --cert-id <id> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
