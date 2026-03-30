# Source: https://docs.envzero.com/guides/admin-guide/templates/iac-binaries-versions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing IaC Binaries Versions

> Specify and manage IaC tool versions in env zero templates for Terraform, OpenTofu, Terragrunt, Pulumi, and Ansible

## Overview

When creating or editing a template, you can specify which version of Infrastructure as Code (IaC) tools to use for your deployments. env zero supports version management for Terraform, OpenTofu, Terragrunt, Pulumi, and Ansible.

## Version Resolution Order

When determining which version to use, env zero follows this priority order:

1. **Environment Variables** (`ENV0_TOOL_VERSION` Environment Variable)
2. **Version Files** (`.tool-version` repository file)
3. **Template Settings** (Specified in UI)

## Version Specification Methods

### 1. Environment Variables

You can override the template version setting using environment variables:

| IaC Tool   | Environment Variable      |
| ---------- | ------------------------- |
| Terraform  | `ENV0_TERRAFORM_VERSION`  |
| OpenTofu   | `ENV0_OPENTOFU_VERSION`   |
| Terragrunt | `ENV0_TERRAGRUNT_VERSION` |
| Pulumi     | `ENV0_PULUMI_VERSION`     |
| Ansible    | `ENV0_ANSIBLE_VERSION`    |

### 2. Version Files

env zero can automatically detect versions from standard version files located under the directory you configure in the template.
If you want to reuse the same version files for multiple folders, set the environment variable ENV0\_RESOLVE\_FILE\_VERSION\_RECURSIVELY=true.

| IaC Tool   | Version File          |
| ---------- | --------------------- |
| Terraform  | `.terraform-version`  |
| OpenTofu   | `.opentofu-version`   |
| Terragrunt | `.terragrunt-version` |
| Ansible    | `.ansiable-version`   |
| Pulumi     | `.pulumi-version`     |

### 3. Template Settings

To associate a specific IaC version with a template:

1. Open the relevant **Template**.
2. Go to the **Settings** tab and expand **Advanced Settings**.
3. Select the desired version from the `"Template Type" Version` dropdown.
4. Click **Save**.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/6e0ce13-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=1f5c2b84cbe0b8af9a7f35d5d99a2bed" alt="Interface screenshot showing configuration options" width="1287" height="883" data-path="images/guides/admin-guide/templates/6e0ce13-image.png" />
</Frame>

<Warning>
  Changing a version in an existing template might affect running environments.
</Warning>

### Special Version Values

#### Automatic Version Detection

When selecting a version in the template settings, you can choose special values:

* **Terraform**: "Resolve from code" - Automatically detects and uses the minimum required version specified in your Terraform code's `required_version` constraint
* **OpenTofu**: "Resolve from code" - Similar to Terraform, extracts required version from your code

<Note>
  The version value for automatic detection is `RESOLVE_FROM_CODE`.
</Note>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/8d0dc65-screen_shot_2021-04-25_at_12.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=e055a148c5aa382569575e189dd0cdce" alt="Screenshot showing Resolve from terraform code option" width="467" height="357" data-path="images/guides/admin-guide/templates/8d0dc65-screen_shot_2021-04-25_at_12.png" />
</Frame>

#### Latest Version

You can specify "latest" for supported IaC tools:

* Terraform: Latest version up to 1.5.x
* Pulumi: Latest available version
* OpenTofu: Latest available version
* Ansible: Latest available version

<Note>
  The version value for automatic detection is `latest`.
</Note>

<Warning>
  **Terraform versions ≥ 1.6.0 aren't supported**

  Terraform versions 1.6.0 and higher are under a BSL license and are not supported in env zero. Consider switching to [OpenTofu](https://opentofu.org/), the drop-in replacement for Terraform.
</Warning>

Built with [Mintlify](https://mintlify.com).
