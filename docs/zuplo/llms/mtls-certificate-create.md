# Source: https://www.zuplo.com/docs/cli/mtls-certificate-create.md

# Zuplo CLI: Mtls Certificate Create

<CliCommand
  command="mtls-certificate create"
  description="Creates a new mTLS certificate for a project"
  options={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the certificate (alphanumeric with underscores)",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "cert",
    "type": "string",
    "description": "Path to the PEM-encoded certificate file",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "normalize": true
  },
  {
    "name": "key",
    "type": "string",
    "description": "Path to the PEM-encoded private key file",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "normalize": true
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
    "$0 mtls-certificate create \\\n  --name my_cert \\\n  --cert ./cert.pem \\\n  --key ./key.pem \\\n  --environment-type production",
    "Create an mTLS certificate enabled for the production environment type"
  ],
  [
    "$0 mtls-certificate create \\\n  --name dev_cert \\\n  --cert ./cert.pem \\\n  --key ./key.pem \\\n  --environment-type development \\\n  --environment-type preview",
    "Create an mTLS certificate enabled for multiple environment types"
  ],
  [
    "$0 mtls-certificate create \\\n  --name my_cert \\\n  --cert ./cert.pem \\\n  --key ./key.pem \\\n  --environment-type production \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates create \
  --name <name> \
  --cert <file> \
  --key <file> \
  --environment <env> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
