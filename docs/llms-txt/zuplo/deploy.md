# Source: https://www.zuplo.com/docs/cli/deploy.md

# Zuplo CLI: Deploy

<CliCommand
  command="deploy"
  description="Deploys current Git branch of the current directory"
  options={[
  {
    "name": "project",
    "type": "string",
    "description": "The project name",
    "required": false,
    "deprecated": false,
    "hidden": true
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
    "name": "dir",
    "type": "string",
    "description": "The directory containing your Zuplo API",
    "default": ".",
    "required": false,
    "deprecated": false,
    "hidden": true,
    "normalize": true
  },
  {
    "name": "environment",
    "type": "string",
    "description": "The value to use for environment name, instead of the current branch name",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "self-hosted-endpoint",
    "type": "string",
    "description": "The endpoint of your self-hosted service to deploy to",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "override-repo-url",
    "type": "string",
    "description": "Override the repo url reference",
    "required": false,
    "deprecated": false,
    "hidden": true
  },
  {
    "name": "mtls-certificates-dir",
    "type": "string",
    "description": "Directory containing mtls certificates to use for the deployment, in the hierarchy that you want them to appear in the runtime. Ex: <cert-name>/tls.crt and <cert-name>/tls.keyAll certificates must be in pem format. Only for use for self-hosted deployments.",
    "required": false,
    "deprecated": false,
    "hidden": true
  },
  {
    "name": "verify-remote",
    "type": "boolean",
    "description": "Verify that this Git repository matches the one configured on Zuplo. Use --no-verify-remote to disable.",
    "default": false,
    "required": false,
    "deprecated": true,
    "hidden": false
  },
  {
    "name": "fetch-environments",
    "type": "boolean",
    "description": "Fetch the environments for your project from Zuplo. If this is false, then the environment will automatically be detected from the git branch.",
    "default": false,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 deploy",
    "Deploy the current Git branch using the branch name as the environment name"
  ],
  [
    "$0 deploy --environment my-env",
    "Override the environment name instead of using the Git branch name"
  ],
  [
    "$0 deploy --account my-account --project my-project --environment my-env",
    "Explicitly specify the account, project, and environment"
  ]
]}
  usage="$0 deploy [options]"
>

## Common use cases

The following examples assume that you are passing in your `--api-key` either as
an argument or through the `ZUPLO_API_KEY` environment variable.

### Deploying your gateway

```bash
# The following will use the current Git branch as the name of the environment

git checkout -b my-new-branch
zuplo deploy --project my-project
```

```bash
# If you don't wish to use the current Git branch as the name of the
# environment, you can specify one using --environment

zuplo deploy --project my-project --environment my-env-name
```

## Polling timeout

By default, the deploy command will poll the status of the deployment every
second for 150 seconds. For most deployments this is enough time for the build
and deploy process to complete. However, if you have a large project, this may
not be enough time. You can increase the timeout by setting the following
environment variables.

- `POLL_INTERVAL` - The interval in seconds between each poll. Default is 1
  second.
- `MAX_POLL_RETRIES` - The maximum number of retries before the command times
  out. Default is 150.

```bash
POLL_INTERVAL=5000 MAX_POLL_RETRIES=300 zuplo deploy
```

Note, that even if the CLI times out, the deployment will continue. You can
check the status of the deployment in the Zuplo portal.

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)

## Additional resources

- [Custom CI/CD](../articles/custom-ci-cd.mdx)
