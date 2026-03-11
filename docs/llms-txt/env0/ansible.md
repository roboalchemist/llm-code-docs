# Source: https://docs.envzero.com/guides/admin-guide/templates/ansible.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ansible Integration

> Configure and deploy Ansible playbooks with env zero for automated configuration management

[Ansible](https://www.ansible.com/) is an open-source automation tool for IT tasks such as configuration management, application deployment, and orchestration. Ansible uses simple YAML-based playbooks to define tasks, making it easy to automate complex processes.

<Info>
  **Supported Versions**

  env zero supports all standard Ansible versions from `3.0.0` and above.
</Info>

## Environment Deployment

In order to manage your Ansible runs in env zero, you must follow these steps:

1. Create an Ansible [Template](/guides/admin-guide/templates) first
2. Optionally - Create [`env0.yml`](/guides/admin-guide/custom-flows) file in the target repository to run any custom command (ansible or otherwise). This is also needed to run commands during the destroy process
3. [Connect your cloud account](/guides/getting-started/getting-started/connect-your-cloud-account)
4. Create an environment

## Execution Steps

Beyond the common steps such as Clone, Loading variables, Deploy/Destroy, etc., Ansible environments offers the following execution steps:

1. Ansible Galaxy - `ansible-galaxy install -r requirements.yml`
2. Ansible Check Playbook - `ansible-playbook --check --diff`

<Warning>
  Note

  Using [check\_mode: false](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html#enforcing-or-preventing-check-mode-on-tasks) will cause Ansible code to be deployed prematurely.
  It can cause regular Deployments still pending approval, Plans, and Drift Detection to deploy Ansible code.
</Warning>

1. Ansible Playbook - `ansible-playbook`

<Warning>
  Destroying Ansible Environments

  Please note that env zero does not execute any Ansible commands for destroying Ansible environments.

  It serves solely to attach [custom flows](/guides/admin-guide/custom-flows).

  Another thing to note - is that when Destroying Ansible Environments, there's no approval flow, unless you set [Approval Policies](/guides/policies-governance/approval-policies).
</Warning>

## Additional Controls

### Setting a custom Playbook file

By default, env zero will run the `ansible-playbook` commands with `playbook.yml` or `playbook.yaml` (whichever is present).

If you want to set a custom playbook file name, you can set the `ENV0_ANSIBLE_PLAYBOOK` variable with whichever value you desire.

### Setting  custom flags

To set any `ansible-playbook` flag, you can set an `ANSIBLE_CLI_flagName` environment variable.

The flagName is always preceded by a `--`, like so:

`--flagName`

If a value is set to the variable, it will be appended to the flag with a space after the flag name, like so:

`--flagName value`

For example:

1. `ANSIBLE_CLI_become` would add the `--become` flag.
2. `ANSIBLE_CLI_inventory`, and setting its value to `hosts` would add the `--inventory hosts` flag.

### Setting extra variables

To set any extra variable for `ansible-playbook`, you can set an `ANSIBLE_VAR_varName` variable.
Any variable you add here will be parsed and added to the `--extra-vars` flag.

For example, setting a `ANSIBLE_VAR_myVar` with a value `my-value`, would add the `--extra-vars 'myVar="my-value"'` flag.

Multiple variables are supported, so setting `ANSIBLE_VAR_firstVar`=`value-one` and `ANSIBLE_VAR_secondVar`=`value-two`, would add `--extra-vars 'firstVar="value-one" secondVar="value-two"'`.

### Skipping Ansible Check Step

In some cases, Ansible checks might fail but for a good reason, and in those cases you might want to skip those checks during the deployment.

For this use case, you can set an environment variable named `ENV0_SKIP_ANSIBLE_CHECK` and set the value to be `true` - This will cause the deployment to skip that step and mark the step as `Skipped` and continue to the next steps in the deployment flow.

<Info>
  **Using the Lean Docker Image with Ansible**

  If you wish to use our [lean docker image](/guides/admin-guide/self-hosted-kubernetes-agent/using-a-custom-image-in-an-agent/lean-docker-image)  along with Ansible, make sure [Python is installed](/guides/admin-guide/self-hosted-kubernetes-agent/using-a-custom-image-in-an-agent/lean-docker-image/#adding-python)
</Info>

Built with [Mintlify](https://mintlify.com).
