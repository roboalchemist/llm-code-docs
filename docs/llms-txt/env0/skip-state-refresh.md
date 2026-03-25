# Source: https://docs.envzero.com/guides/policies-governance/skip-state-refresh.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Skipping State Refresh

> Skip state refresh as a last resort when facing state mismatches that cause terraform plan to fail

Skip State Refresh policy is used as a last resort when facing state mismatches that cause the terraform plan to fail. You can read more about it [here](https://www.terraform.io/cli/commands/plan#refresh-false).

This policy is the equivalent of `terraform plan -refresh=false` and is available only for destroying environments. To skip the state refresh during deployment, set the `TF_CLI_ARGS_plan` environment variable to `-refresh=false`.

While destroying an environment, you can also tick the `skip state refresh` checkbox, and the environmental destruction process ignores any state mismatches and will remove the resources that match the current state.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/policies-governance/destroy_environment_skip_state_refresh_option.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=59f147c6eec8ea04dcd87619b517e442" alt="Destroy environment skip state refresh option" width="1108" height="528" data-path="images/guides/policies-governance/destroy_environment_skip_state_refresh_option.png" />
</Frame>

## Common errors that can be addressed using this policy

| Error message                                                                                           | Description                                                                                                                                                          |
| :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "aws\_secretsmanager\_secret ... You can't perform this operation on secret ... because it was deleted" | A secret used by a resource is marked for deletion or is already deleted. This data source throws an error on the plan phase and prevents the environment's deletion |
| "Error during making a request: ... /get ... in data "http ..."                                         | An HTTP Data source that was available during the deploy phase is not available during the destroy phase                                                             |

Built with [Mintlify](https://mintlify.com).
