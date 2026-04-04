# Source: https://docs.envzero.com/guides/admin-guide/templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Overview

> Learn how env zero templates define reusable environment configurations for IaC deployments

## What is a Template?

In env zero, a template defines the type of environment that can be deployed. Environments are created based on templates. A template includes a name, a description, a valid set of configuration files that describe the deployment, and a set of [Variables and Secrets](/guides/admin-guide/variables).

## Why Templates are Important

* **Promote Reusability (DRY Architecture)**
  An IaC template can be reused across many environments, all pointing to the same code, supporting DRY (Don't Repeat Yourself) architecture. This ensures that your IaC configurations are consistent across all environments, reducing the risk of configuration drift and simplifying maintenance.
* **Enable Self-Service with Control**
  Templates allow engineers to deploy cloud resources easily while giving admins control over what can and cannot be configured. This ensures compliance with organizational standards and security policies.
* **Centralize Variable Management**
  Defining variables at the template level ensures they are automatically inherited by all environments created from that template. This centralized management keeps all environments up-to-date and simplifies configuration changes.

## Template Types

Templates reference specific IaC tools, and the type of template defines the required tool:

**Terraform/OpenTofu** Requires relevant `.tf` files in your Git repository. Depending on the template selected, either the `terraform`or `tofu` executable handles deployment.

**Terragrunt** Requires [Terragrunt configurations](https://terragrunt.gruntwork.io/docs/getting-started/configuration/) and the correct folder hierarchy with `.tf` files. The `terragrunt` executable manages deployment.

**Pulumi** Needs code that describes your environment in the repository. The `pulumi`executable handles deployment.

**CloudFormation** Requires JSON or YAML CloudFormation templates. Managed by `aws cloudformation` commands.

**Kubernetes** Needs YAML or JSON files describing cluster resources. `Kustomize` labels resources, and `kubectl` manages them.

**Helm** Configurable via a Helm Repo or Git repository with the chart's definition. The `helm` executable and `helm diff` plugin handle deployment.

## Create a Template

To create a new template, click CREATE NEW TEMPLATE on the top right in the Templates screen (Found in the Organization menu).
Enter the details for the Git repository containing the relevant configuration files: the repository, a branch or tag name, and the path for the root directory of the IaC files.

Please note that you can only create templates at the Organization level, not Project.

<Info>
  **If your VCS is not GitHub, GitLab, Bitbucket or Azure DevOps**

  Select the "Other VCS" option. You can either enter the details yourself, or copy the full URL of where your relevant configuration resides, and let env zero extract the values. Please note that extraction of values currently works for HTTP/S Git repositories only. If you use SSH, please enter your repository URL manually.

  To access a private repository you will need a Git access token. In the Select Token field, select a token from a list of predefined access tokens available to env zero. To define a Git access token in env zero, see [Manage Git Tokens](/guides/admin-guide/templates/#manage-git-connectivity).
</Info>

Once your template is created,  you can edit its [Variables](/guides/admin-guide/variables) by locating them in the template list, clicking on Settings and selecting the Variables tab. By default, your environment inherits variables set at the Organization level, but you can override these or create new ones. If your repository URL is in SSH format, the token field will be replaced by an SSH key field.

## Manage Templates

Templates can only be added, deleted, or edited at an Organization level. At a Project level, you can only associate or disassociate a template with the project.

You can view the Organization's templates in the Templates tab, see the template code, or create a new environment from the template.

If you have appropriate permissions, you can change the settings of an existing template. For example, you can refer it to another Terraform/Terragrunt configuration, in a different repo, branch, or tag,  or edit the variables.

You can also delete a template, in which case it can no longer be used to create new environments. It will have no effect on existing environments that are based on the deleted template.

<Note>
  Note

  Changes you make to your template will only affect new deployments based on the template. To update an active environment with the template changes you must redeploy the environment.
</Note>

## On-Premises Git Servers Support

Full git-ops support is available to Github Enterprise, Gitlab Enterprise and Bitbucket Server installations. Communication with these VCS will be done only through a self-hosted agent, which means you do not have to make the VCS available from outside your network.

IIf you'd like to use the "Other" VCS type to access a Git server that ison your private network, you need to enable port forwarding and grant public access using a public IP (and a high port number). It is strongly recommended that you open that port in your firewall for incoming traffic only from env zero's IPs (detailed below) in order to ensure proper and secure access to your Git server.

Current env zero outgoing IP addresses are listed under [Security Overview > IP Addresses](/guides/overview/security-overview/ip-addresses)

## Manage Git Connectivity

### Tokens (HTTP/S)

To access a private Git repository via HTTP/S, env zero needs a read-only access token.
Git access tokens are managed centrally in env zero and are referred to by templates.

Only users with an Organization Admin role can manage Git tokens in env zero.
To see the list of Git tokens, select the Credentials tab in the Organization Settings page. You can add or remove Git tokens.
To add a new Git token, click Add Token. Enter a name for the token, and the token value from your Git hosting service.
If your Git hosting service requires a username as well as a token (such as BitBucket or GitLab), enter the token value as `username:token`.

For details on how to generate an access token, refer to the documentation of your Git hosting service:

* [Personal access tokens (Github)](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
* [Personal access tokens (GitLab)](https://docs.gitlab.com/ee/user/profile/personal_access_tokens)
* [App Passwords (Bitbucket)](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html)
* [Personal access tokens (AzureDevOps)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)

### SSH Keys

To access a private Git repository via SSH, env zero needs a private SSH key that has been granted access to the Git repository.

SSH keys are managed much like tokens and can be configured on the Organization level by Admins.
To enable SSH connectivity to your Git repository, first [associate an SSH key with your template](/guides/admin-guide/variables/ssh-keys).

## Automatic Retry Policy

When running your IaC flow, you might want env zero to automatically retry in case of an error.

Automatic retries are configured per template and only retry the apply / destroy step

To enable automatic retry

* Find the Retry on failure section at the Advanced section of the template wizard, in the settings page.
* Choose if you would like your template to be retried on Deploy, Destroy, or both, and the number of times to retry.
* You can also define a Regex pattern so that env zero will only retry on certain errors. If you do not provide a Regex pattern, all errors will be retried.

## Finding My Template ID

Sometimes you may need your template ID for using it in env zero's [terraform provider](https://registry.terraform.io/providers/env0/env0/latest) or for some [API calls](/api-reference).

You can find it under the Template Card Templates tab.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/4bdc4bd-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=72441fab2e0f69b127bc4afad3bab249" alt="" width="1485" height="176" data-path="images/guides/admin-guide/4bdc4bd-image.png" />

Built with [Mintlify](https://mintlify.com).
