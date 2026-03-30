# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/ci-cd/github-workflow.md

# Source: https://docs.port.io/actions-and-automations/setup-backend/github-workflow.md

# GitHub workflow

The GitHub backend allows you to trigger GitHub workflows for your self-service actions and automations, using [Port's GitHub application](/build-your-software-catalog/sync-data-to-catalog/git/github/.md#setup).

GitHub app types

The GitHub backend is available for both the standard Port [GitHub app](/build-your-software-catalog/sync-data-to-catalog/git/github/.md), and the [self-hosted version](/build-your-software-catalog/sync-data-to-catalog/git/github/self-hosted-installation.md).

![](/img/self-service-actions/portGithubWorkflowArchitecture.png)

<br />

<br />

The steps shown in the image above are as follows:

1. Port publishes an invoked `action` message to a topic.
2. A secure topic (`ORG_ID.github.runs`) holds all the action invocations.
3. A listener implemented in Port's GitHub application receives the new topic message and runs the GitHub workflow defined by the creator of the self-service action/automation.

An example flow would be:

1. A developer asks to deploy a new version of an existing `Microservice`, using a self-service action.
2. The `create` action is sent to the `github.runs` topic.
3. Port's GitHub application event handler is triggered by this new action message.
4. Port's GitHub application triggers the GitHub workflow that deploys a new version of the service.
5. As part of the workflow, the new microservice `Deployment` is reported back to Port.
6. When the workflow is done, Port's GitHub application reports back to Port about the status of the action run (`SUCCESS` or `FAILURE`), according to workflow's status.

## Configuration[â](#configuration "Direct link to Configuration")

When using this backend, you need to provide the GitHub **organization** and **repository** where the workflow is located, as well as the workflow **name**.

Important notes:

* The workflow must reside in the repository's `.github/workflows/` directory.
* The workflow must use the [workflow\_dispatch](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) trigger.
  <br />
  <!-- -->
  For example, see the workflow implementation in [this guide](/guides/all/manage-pull-requests.md#guide).

### Specify a branch[â](#specify-a-branch "Direct link to Specify a branch")

By default, the integration will look for the workflow in the `main` branch of the repository.

To use a different branch, simply pass the `ref` key in the `Configure the invocation payload` section (or `invocationMethod.workflowInputs` in the JSON object) with the desired branch name as the value:

```
{
  "ref": "my-branch-name"
}
```

Workflow file must exist in the default branch

Due to [GitHub's behavior](https://github.com/github/docs/issues/31007), to trigger a workflow that uses the `workflow_dispatch` event from a non-default branch using the `ref` key, the same workflow file must exist in the **default branch**.

TIP: If you prefer not to include the full workflow file in the **default branch**, placing a workflow file with the **same name** is enough for the correct workflow in the non-branch to run successfully.

### Automatic workflow status update[â](#automatic-workflow-status-update "Direct link to Automatic workflow status update")

Additionally, you can define whether or not Port should automatically use the workflow's end status (`SUCCESS`/`FAILURE`) to update the action/automation status in Port.

By default, this is set to `true`. To disable this option, set the `reportWorkflowStatus` field to `false` in the `invocationMethod` object, or set the `Report workflow status` option to `No` if using the UI.

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

## Examples[â](#examples "Direct link to Examples")

For complete examples of self-service actions using a GitHub workflow as the backend, check out the [guides section](/guides/.md?tags=GitHub\&tags=Actions).
