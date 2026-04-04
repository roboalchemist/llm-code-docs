# Source: https://docs.envzero.com/guides/admin-guide/workflows/create-a-new-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating A New Workflow

> Step-by-step guide to creating a workflow using env0.workflow.yaml with dependencies and approval settings

To set up a Workflow, follow this simple guide:

env zero relies on a file named **env0.workflow\.yaml** (or **env0.workflow\.yml**) to describe the dependencies and configuration of the sub-environments in your workflow.

For the complete schema reference, see [Workflow File Reference](/guides/admin-guide/workflows/workflow-file-reference).

## Approval Priority Order

When multiple approval settings exist, approvals are evaluated in the following priority:

1. [ENV0\_REQUIRES\_APPROVAL](/guides/admin-guide/custom-flows/#forcing-manual-approvals) environment variable
2. Approval policy (always evaluated if defined)
3. Value from the UI or API request
4. Value from the workflow `requiresApproval` field

## Example Configuration

```yaml env0.workflow.yaml theme={null}
environments:
  vpc:
    name: "VPC and Network"
    templateName: "VPC"

  db:
    name: "Database"
    templateName: "DB"
    requiresApproval: true
    needs:
      - vpc

  eks:
    name: "EKS Cluster"
    templateName: "EKS"
    needs:
      - vpc

  billing-service:
    name: "Billing Service"
    vcs:
      type: terraform
      terraformVersion: "1.5.7"
      repository: "https://github.com/env0/templates"
      path: "aws/hello-world"
      githubInstallationId: 123456789
    disabled: ${DISABLE_BILLING_SERVICE}
    needs:
      - db
      - eks

  config-service:
    name: "Configuration Service"
    templateName: "Configuration Service"
    revision: feature-branch
    disabled: ${DISABLE_CONFIG_SERVICE}
    needs:
      - db
      - eks
```

### Using Environment Variables in Workflow Fields

You can use `${...}` syntax to interpolate environment variables into workflow fields.

In the example above:

* `DISABLE_BILLING_SERVICE` controls whether the `billing-service` environment is disabled.
* `DISABLE_CONFIG_SERVICE` controls whether the `config-service` environment is disabled.

When these variables are set to `true` (for example, in your environment or via env zero variables), the corresponding sub-environment is skipped during deployment.

## Environment Removal Strategy

By default, removing an environment from the workflow file leaves it detached but not destroyed.

To automatically run a "destroy" process on environments that were removed from the workflow file, add `environmentRemovalStrategy: destroy` to your `settings` section. For example:

```yaml env0.workflow.yaml theme={null}
settings:
  environmentRemovalStrategy: destroy

environments:
  vpc:
    name: "VPC and Network"
    templateName: "VPC"
```

| Value     | Behavior                                                                    |
| --------- | --------------------------------------------------------------------------- |
| `destroy` | Automatically destroy removed environments after deploying all environments |
| `detach`  | Detach removed environments without destroying them (default)               |

<Warning>
  **Template Naming**

  While not enforced, use unique template names. Otherwise, the Workflow will randomly choose one of the templates without considering permission restrictions.
</Warning>

## Creating a Workflow in the UI

1. Create a [new template](/guides/admin-guide/templates) and select **env zero Workflow** as the Template Type:

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/workflows/7e4b205-screen_shot_2022-06-08_at_16.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=031d94c14169550423c5a8488d1a42ad" alt="" width="2830" height="770" data-path="images/guides/admin-guide/workflows/7e4b205-screen_shot_2022-06-08_at_16.png" />

In the VCS step, fill in your VCS details and the directory that contains your **env0.workflow\.yaml** (or env0.workflow\.yaml\*\*) file:

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/workflows/bec911f-screen_shot_2022-06-08_at_16.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=6779901470b6abd60d4ddbd07963c412" alt="" width="2884" height="892" data-path="images/guides/admin-guide/workflows/bec911f-screen_shot_2022-06-08_at_16.png" />

1. Create an [Environment](/guides/admin-guide/environments/setting-up-a-new-environment) based on the Workflow template.
   You can choose any of the workflow environments from the dropdown menu in the top right corner.

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/workflows/9d4cf3b-screen_shot_2022-11-30_at_19.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=66e4e17f97aa5adb935589a49e42ed62" alt="" width="1660" height="708" data-path="images/guides/admin-guide/workflows/9d4cf3b-screen_shot_2022-11-30_at_19.png" />

After choosing one of the workflow sub-environments, you can modify its variables, workspace, revision and auto-approval settings.

<Note>
  Remote Backend

  The Remote Backend option will be applied to Terraform templates only. For further documentation about remote backend, [follow this guide](/guides/admin-guide/remote-backend).
</Note>

<Note>
  Overrides Note

  The values you set here for workspace and revision will override the ones you've defined in the workflow file for the corresponding environment.

  If you would like to set the whole workflow to the same workspace name value, you can do so by setting the workflow workspace name, and leaving the sub environments blank.

  Note that since Terragrunt uses a working directory instead of workspace name, the workspace name override won't apply to Terragrunt template type.

  When marking the workflow as remote backend, you must provide unique names for each of the sub environments workspaces.
</Note>

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/workflows/953934f-screen_shot_2022-12-21_at_11.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=f721bf284c6dfd90ceeed003a331e689" alt="" width="2922" height="2012" data-path="images/guides/admin-guide/workflows/953934f-screen_shot_2022-12-21_at_11.png" />

1. Deploy

   <img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/workflows/de95a1c-image.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=c69abe44cab5e61f66d5b055360ae659" alt="" width="1458" height="726" data-path="images/guides/admin-guide/workflows/de95a1c-image.png" />

Built with [Mintlify](https://mintlify.com).
