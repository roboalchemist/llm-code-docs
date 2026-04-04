# Source: https://docs.envzero.com/guides/admin-guide/workflows/workflow-file-reference.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow File Reference

> Complete reference for the env0.workflow.yaml file schema including environments and settings configuration

This page provides a complete reference for the `env0.workflow.yaml` (or `.yml`) file used to define env zero Workflows.

## File Structure

The workflow file has two main sections:

* **`environments`** (required) - Defines the sub-environments in the workflow
* **`settings`** (optional) - Global workflow settings

Example:

```yaml env0.workflow.yaml theme={null}
settings:
  environmentRemovalStrategy: detach # or destroy

environments:
  my-environment:
    name: "My Environment"
    templateName: "my-template"
    # ... additional configuration
```

## Settings

Global settings that apply to the entire workflow.

`environmentRemovalStrategy` (string) controls what happens when a sub-environment is removed from the workflow file.

* Default: `detach`
* `detach` - The environment is detached but not destroyed.
* `destroy` - The environment is destroyed after you deploy the updated workflow.

## Sub-Environment Properties

Each sub-environment is defined as a key-value pair under `environments`. The key is a unique alias for the sub-environment.

### Core Properties

| Property       | Type     | Required | Description                                                       |
| -------------- | -------- | -------- | ----------------------------------------------------------------- |
| `name`         | `string` | Yes      | Display name shown in the env zero UI.                            |
| `templateName` | `string` | No\*     | Name of an existing env zero template. Cannot be used with `vcs`. |
| `vcs`          | `object` | No\*     | Inline VCS configuration. Cannot be used with `templateName`.     |

**\* Either `templateName` or `vcs` must be specified, but not both.**

### Optional Properties

| Property           | Type                  | Default | Description                                                                                                                       |
| ------------------ | --------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `needs`            | `array`               | `[]`    | List of sub-environment aliases that must deploy before this one.                                                                 |
| `revision`         | `string`              | -       | Git revision (branch, tag, or commit SHA) to use.                                                                                 |
| `workspace`        | `string`              | -       | For Terraform/OpenTofu, sets the workspace name. For Helm, sets the release name. For Pulumi/CloudFormation, sets the stack name. |
| `requiresApproval` | `boolean`             | `false` | If `true`, deployment requires manual approval before proceeding.                                                                 |
| `disabled`         | `boolean` or `string` | `false` | If `true` or `"true"`, this sub-environment is skipped during deployment. Supports variable interpolation.                        |

## VCS Configuration

If you want to use your code directly without creating a template for it first, you can use the `vcs` object with the following properties:

| Property     | Type     | Required | Default | Description                                                                                                     |
| ------------ | -------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| `type`       | `string` | Yes      | -       | IaC type. Options: `terraform`, `opentofu`, `terragrunt`, `pulumi`, `k8s`, `cloudformation`, `helm`, `ansible`. |
| `repository` | `string` | Yes      | -       | Git repository URL (HTTPS or SSH).                                                                              |
| `path`       | `string` | No       | `""`    | Path within the repository where IaC code is located.                                                           |
| `revision`   | `string` | No       | -       | Git revision (branch, tag, or commit) to use.                                                                   |

### VCS Authentication Properties

| Property               | Type     | Description                                                                 |
| ---------------------- | -------- | --------------------------------------------------------------------------- |
| `tokenId`              | `string` | ID of a stored VCS token for authentication.                                |
| `tokenName`            | `string` | Display name of the VCS token.                                              |
| `sshKeys`              | `array`  | SSH keys for repository authentication. Each item requires `id` and `name`. |
| `githubInstallationId` | `number` | GitHub App installation ID.                                                 |
| `bitbucketClientKey`   | `string` | Bitbucket client key for Bitbucket Cloud.                                   |
| `vcsConnectionId`      | `string` | VCS connection ID for unified VCS integration.                              |

### VCS Provider Flags

| Property             | Type      | Default | Description                                      |
| -------------------- | --------- | ------- | ------------------------------------------------ |
| `isGitLab`           | `boolean` | `false` | Set to `true` for GitLab.com repositories.       |
| `isGitLabEnterprise` | `boolean` | `false` | Set to `true` for GitLab Enterprise/self-hosted. |
| `isGitHubEnterprise` | `boolean` | `false` | Set to `true` for GitHub Enterprise.             |
| `isBitbucketServer`  | `boolean` | `false` | Set to `true` for Bitbucket Server/Data Center.  |
| `isAzureDevOps`      | `boolean` | `false` | Set to `true` for Azure DevOps.                  |

### IaC Version Properties

| Property             | Type     | Description                                                                                 |
| -------------------- | -------- | ------------------------------------------------------------------------------------------- |
| `terraformVersion`   | `string` | Terraform version. Use a specific version (e.g., `1.5.7`) or `RESOLVE_FROM_TERRAFORM_CODE`. |
| `opentofuVersion`    | `string` | OpenTofu version. Use a specific version (e.g., `1.6.0`).                                   |
| `terragruntVersion`  | `string` | Terragrunt version (e.g., `0.54.0`).                                                        |
| `terragruntTfBinary` | `string` | Underlying binary for Terragrunt: `terraform` (default) or `opentofu`.                      |
| `pulumiVersion`      | `string` | Pulumi version (e.g., `3.100.0`).                                                           |
| `ansibleVersion`     | `string` | Ansible version (e.g., `2.15.0`).                                                           |

### CloudFormation Properties

| Property           | Type      | Default | Description                                                 |
| ------------------ | --------- | ------- | ----------------------------------------------------------- |
| `helmChartName`    | `string`  | -       | Helm chart name when using a Helm repository.               |
| `isHelmRepository` | `boolean` | `false` | Set to `true` if the repository is a Helm chart repository. |

### Helm Properties

| Property           | Type      | Default | Description                                                 |
| ------------------ | --------- | ------- | ----------------------------------------------------------- |
| `helmChartName`    | `string`  | -       | Helm chart name when using a Helm repository.               |
| `isHelmRepository` | `boolean` | `false` | Set to `true` if the repository is a Helm chart repository. |

## Examples

### Simple Workflow with Template References

A basic workflow using pre-defined templates with dependencies.

```yaml env0.workflow.yaml theme={null}
environments:
  database:
    name: "PostgreSQL Database"
    templateName: "aws-rds-postgres"
    workspace: "production"

  api:
    name: "API Service"
    templateName: "kubernetes-deployment"
    needs:
      - database
    requiresApproval: true
```

### Workflow with Inline VCS Configuration

Define IaC source directly without creating separate templates:

```yaml env0.workflow.yaml theme={null}
environments:
  networking:
    name: "VPC and Networking"
    vcs:
      type: terraform
      repository: "https://github.com/myorg/infrastructure"
      path: "terraform/networking"
      terraformVersion: "1.5.7"

  compute:
    name: "EC2 Instances"
    vcs:
      type: terraform
      repository: "git@github.com:myorg/infrastructure.git"
      path: "terraform/compute"
      terraformVersion: "RESOLVE_FROM_TERRAFORM_CODE"
      sshKeys:
        - id: "ssh-key-123"
          name: "Deploy Key"
    needs:
      - networking
```

### Mixed Workflow with Settings

Combine template references and inline VCS with global settings.

```yaml env0.workflow.yaml theme={null}
settings:
  environmentRemovalStrategy: remove

environments:
  infra:
    name: "Base Infrastructure"
    templateName: "terraform-aws-base"
    revision: "v2.0.0"

  app:
    name: "Application"
    vcs:
      type: helm
      repository: "https://github.com/myorg/helm-charts"
      path: "charts/myapp"
    needs:
      - infra

  monitoring:
    name: "Monitoring Stack"
    templateName: "prometheus-grafana"
    needs:
      - infra
    disabled: false
```

### Workflow with Variable Interpolation

Use environment variables to conditionally disable sub-environments.

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
    templateName: "Billing Service"
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

<Tip>
  Use variable interpolation with the `disabled` property to enable partial
  workflow deployments based on environment variables.
</Tip>

Learn more: [Workflow File JSON Schema](/guides/admin-guide/workflows/workflow-file-json-schema)

Built with [Mintlify](https://mintlify.com).
