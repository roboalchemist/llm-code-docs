# Source: https://docs.safetycli.com/safety-docs/administration/project-policies.md

# Project Policies

{% hint style="info" %}
Project policies are similar to Safety Policy Files, but take precedence over policy files in cases where a codebase has been onboarded as a Safety Project.
{% endhint %}

## Creating a Project Policy

To create a policy for a project, visit <https://platform.safetycli.com> and complete these steps:

1. Select your project.
2. Click **Project Settings**.
3. Click **Policies**.
4. Select your policy and click **Edit**.
5. Build your policy using the guided policy builder, or alternatively click **Advanced Configuration** to build your policy using JSON.
6. Click **Save**.

## Migrating your Safety Policy File to a Project Policy

{% hint style="info" %}
We plan to introduce a feature that will automatically detect a local policy file during project creation and replicate this in the Project Policy. Until then, please follow these instructions.
{% endhint %}

To migrate a local policy file to a Project Policy, visit [https://platform.safetycli.com](https://platform.safetycli.com/) and complete these steps:

1. Click **Project Settings**.
2. Click **Policies**.
3. Select your policy and click **Edit**.
4. Scroll down and click **Advanced Configuration**.
5. Copy the contents of your local policy file.
6. Paste the policy file contents into the advanced configuration.
7. Click **Update Policy**.

## Modifying your Default Organization Policy

All Organizations in Safety Platform are initialized with a default Project Policy. When a new project is created, this organization policy is applied. You can modify your default organization policy by visiting [https://platform.safetycli.com](https://platform.safetycli.com/) and following these steps:<br>

1. From the top navigation items, click **Organization**.
2. From the left-hand navigation, click **Policies**.
3. Select your policy and click **Edit**.
4. Build your policy using the guided policy builder, or alternatively click **Advanced Configuration** to build your policy using JSON.
5. Click **Save**.<br>

Note that updated organization policies will not apply retrospectively to existing project policies, but instead will apply to any newly created projects.
