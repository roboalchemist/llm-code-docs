# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github-ocean.md

# Source: https://docs.port.io/actions-and-automations/setup-backend/github-ocean.md

# GitHub workflow via Ocean

The GitHub Ocean backend allows you to trigger GitHub workflows for your self-service actions and automations, using the [GitHub Ocean integration](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/.md).

Integration-based backend

The GitHub Ocean backend uses the `INTEGRATION_ACTION` type and requires you to specify which GitHub Ocean integration installation to use via the `installationId` field.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before using the GitHub Ocean backend, you need to:

1. Install the [GitHub Ocean integration](/build-your-software-catalog/sync-data-to-catalog/git/github-ocean/installation/.md) in your Port organization.
2. Ensure that actions processing is enabled. This is automatically enabled via the UI and OAuth installations.
3. Ensure the integration uses Port machine tokens (organization-level tokens). Personal tokens or service account tokens are not supported.

## Configuration[â](#configuration "Direct link to Configuration")

When using this backend, you need to provide:

* The **integration installation ID** (`installationId`) - specifies which GitHub Ocean integration instance to use.
* The GitHub **organization** and **repository** where the workflow is located.
* The workflow **name**.
* The **integration action type** (`integrationActionType`) - must be set to `dispatch_workflow`.

Important notes:

* The workflow must reside in the repository's `.github/workflows/` directory.
* The workflow must use the [workflow\_dispatch](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) trigger.
  <br />
  <!-- -->
  For example, see the workflow implementation in [this guide](/guides/all/manage-pull-requests.md#guide).

### Automatic workflow status update[â](#automatic-workflow-status-update "Direct link to Automatic workflow status update")

Additionally, you can define whether or not Port should automatically use the workflow's end status (`SUCCESS`/`FAILURE`) to update the action/automation status in Port.

By default, this is set to `true`. To disable this option, set the `reportWorkflowStatus` field to `false` in the `invocationMethod` object, or turn the `Report workflow status` toggle off if using the UI.

Live events requirement

To enable automatic workflow status updates, the integration must have live events enabled. Workflow status is updated via webhook events from GitHub. Live events are automatically enabled for integrations hosted by Port, but must be manually configured for self-hosted installations.

### Organization auto-fill[â](#organization-auto-fill "Direct link to Organization auto-fill")

The `org` field behavior depends on the installation type:

* If the integration is **hosted by Port**, the `org` input field will be hidden and prefilled in the UI. Port automatically knows which organization you selected during installation.
* If the integration is **self-hosted**, you must always fill in the organization input, even if it is configured for a specific organization.
* When creating an action **through the API**, you must specify the organization even if the integration is hosted by Port.

### Specify a branch[â](#specify-a-branch "Direct link to Specify a branch")

By default, the integration will look for the workflow in the repository's default branch (usually `main`/`master`).

To use a different branch, simply pass the `ref` key in the `Configure the invocation payload` section (or `invocationMethod.workflowInputs` in the JSON object) with the desired branch name as the value:

```
{
  "ref": "my-branch-name"
}
```

Workflow file must exist in the default branch

Due to [GitHub's behavior](https://github.com/github/docs/issues/31007), to trigger a workflow that uses the `workflow_dispatch` event from a non-default branch using the `ref` key, the same workflow file must exist in the **default branch**.

TIP: If you prefer not to include the full workflow file in the **default branch**, placing a workflow file with the **same name** is enough for the correct workflow in the non-branch to run successfully.

## Limitations[â](#limitations "Direct link to Limitations")

### Input limit[â](#input-limit "Direct link to Input limit")

A GitHub workflow can have **up to 10** input parameters. Note this when defining your payloads.<br /><!-- -->If you need more than 10 inputs, you can use a JSON object as a single parameter.

### Workflow chains[â](#workflow-chains "Direct link to Workflow chains")

A workflow triggered using the `workflow_dispatch` trigger is self-contained. This means its actions and effects over the repository cannot trigger other automatic workflows.

For example, take the following scenario:

1. A developer executes a "Create a new microservice in a monorepo" workflow.
2. The workflow opens a new pull request in the target repository based on a pre-defined template.
3. The repository also has a workflow which is automatically triggered using the `on: pull_request: types: "opened"` trigger.
4. In this instance, the automatic PR workflow **will not** be triggered.
