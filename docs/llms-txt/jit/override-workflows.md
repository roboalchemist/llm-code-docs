# Source: https://docs.jit.io/docs/override-workflows.md

# Override workflows

## Overview

> ⚠️ Note
>
> Security Plan configuration is managed directly in the Jit platform.\
> As-code configuration is no longer the source of truth and is considered redundant.\
> If you previously used as-code configuration, it has been automatically synced to Jit.\
> Please contact us if anything is unclear or behaves differently than expected.

The override feature allows you to modify 'as code' YAML configurations of the original workflows.\
You can create, modify, or replace environment variables of security controls by setting variables (`env`) and arguments (`args`) in the override section.

The `env` section defines all the variables that you want to override:

* Setting an existing variable name will override its original value
* Setting a new variable name that does not exist in the original workflow will create it in the control.

# Examples

Here's an example of override usage:

```yaml
override:
  workflows:
    mfa-aws-checker:
      jobs:
        mfa-aws-checker:
          runner:
            setup:
              auth_type: no_auth
              checkout: false
            type: github_actions
          steps:
            - name: Run MFA checker
              uses: registry.jit.io/aws-mfa:latest
              with:
                env:
                  AWS_ACCESS_KEY_ID: ${{ secrets.GENERIC_RUNNER_TEST_AWS_ACCESS_KEY_ID }}
                  AWS_REGION_NAME: us-east-1
                  AWS_SECRET_ACCESS_KEY: ${{ secrets.GENERIC_RUNNER_TEST_AWS_SECRET_ACCESS_KEY }}
                  AWS_SESSION_TOKEN: null
                args: --output-file override_output.json
```

In the above example, we override all the origin values of `AWS_SESSION_TOKEN` `AWS_SECRET_ACCESS_KEY` `AWS_ACCESS_KEY_ID` `AWS_REGION_NAME` with new values.\
and override the args that the control receives, so it will receive the argument: `--output-file override_output.json`

If the names in the `env` section already exist in the original workflow file, their values will be overridden; if not, they will be created. The `args` will always be replaced by those appearing in the override section.