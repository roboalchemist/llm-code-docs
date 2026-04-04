# Source: https://docs.envzero.com/guides/admin-guide/env-zero-templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using env zero Templates

> Define reusable infrastructure blueprints with templates for consistent environment deployments in env zero

## What are Templates?

Templates in env zero define the type of environment that can be deployed. They serve as blueprints for your infrastructure deployments, including a name, description, valid configuration files, and a set of [Variables and Secrets](/guides/admin-guide/variables).

Environments are created based on templates, making them the foundation of your Infrastructure-as-Code (IaC) workflow in env zero.

## Why Templates are Important

### Promote Reusability (DRY Architecture)

Templates enable you to reuse IaC configurations across many environments, all pointing to the same code. This supports DRY (Don't Repeat Yourself) architecture, ensuring consistent configurations across all environments while reducing configuration drift and simplifying maintenance.

### Enable Self-Service with Control

Templates allow engineers to deploy cloud resources easily while giving administrators control over what can and cannot be configured. This ensures compliance with organizational standards and security policies.

### Centralize Variable Management

Defining variables at the template level ensures they are automatically inherited by all environments created from that template. This centralized management keeps all environments up-to-date and simplifies configuration changes.

## Template Types

Templates reference specific IaC tools, and the type of template defines the required tool:

### Terraform/OpenTofu

* **Requirements:** Relevant `.tf` files in your Git repository
* **Execution:** Either `terraform` or `tofu` executable handles deployment
* **Use Case:** Most common IaC framework for cloud infrastructure

### Terragrunt

* **Requirements:** [Terragrunt configurations](https://terragrunt.gruntwork.io/docs/getting-started/configuration/) and correct folder hierarchy with `.tf` files
* **Execution:** `terragrunt` executable manages deployment
* **Use Case:** Terraform wrapper for DRY configurations

### Pulumi

* **Requirements:** Code that describes your environment in the repository
* **Execution:** `pulumi` executable handles deployment
* **Use Case:** Infrastructure as code using general-purpose programming languages

### CloudFormation

* **Requirements:** JSON or YAML CloudFormation templates
* **Execution:** `aws cloudformation` commands
* **Use Case:** AWS-native infrastructure definitions

### Kubernetes

* **Requirements:** YAML or JSON files describing cluster resources
* **Execution:** `Kustomize` labels resources, `kubectl` manages them
* **Use Case:** Container orchestration and cluster management

### Helm

* **Requirements:** Helm Repo or Git repository with chart definitions
* **Execution:** `helm` executable and `helm diff` plugin
* **Use Case:** Kubernetes package management and templating

## Creating Templates

### Basic Template Creation

To create a new template:

1. Navigate to the Templates screen (found in the Organization menu)
2. Click "CREATE NEW TEMPLATE" in the top right
3. Enter Git repository details:
   * Repository URL
   * Branch or tag name
   * Path for the root directory of IaC files

<Note>
  **Organization Level Only**
  Templates can only be created at the Organization level, not at the Project level.
</Note>

### VCS Integration Options

**Supported VCS Platforms:**

* GitHub
* GitLab
* Bitbucket
* Azure DevOps

**Other VCS Support:**

* Select "Other VCS" option for custom Git servers
* Enter repository details manually or copy full URL for auto-extraction
* Auto-extraction works for HTTP/S Git repositories only
* SSH repositories require manual URL entry

### Private Repository Access

**HTTP/S Access:**

* Requires Git access token
* Select from predefined access tokens in env zero
* Configure tokens in [Manage Git Tokens](/guides/admin-guide/templates/#manage-git-connectivity)

**SSH Access:**

* Requires private SSH key with repository access
* Configure SSH keys at the Organization level
* Associate SSH key with template in Variables section

## Template Management

### Organization-Level Operations

Templates can only be added, deleted, or edited at the Organization level. At the Project level, you can only associate or disassociate templates with the project.

### Template Operations

* **View Templates:** See all organization templates in the Templates tab
* **View Code:** Access template source code and configurations
* **Create Environments:** Deploy new environments from templates
* **Edit Settings:** Modify repository references, branches, tags, or variables
* **Delete Templates:** Remove templates (existing environments remain unaffected)

<Note>
  **Template Changes Impact**
  Changes to templates only affect new deployments. To update active environments with template changes, you must redeploy the environment.
</Note>

## Git Connectivity Management

### Access Tokens (HTTP/S)

For private Git repository access via HTTP/S:

**Token Management:**

* Only Organization Admins can manage Git tokens
* Access through Credentials tab in Organization Settings
* Add or remove tokens as needed

**Token Configuration:**

* Enter token name and value from your Git hosting service
* For services requiring username (BitBucket, GitLab): use format `username:token`
* Supports GitHub, GitLab, Bitbucket, and Azure DevOps tokens

**Token Generation References:**

* [GitHub Personal Access Tokens](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
* [GitLab Personal Access Tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens)
* [Bitbucket App Passwords](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html)
* [Azure DevOps Personal Access Tokens](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)

### SSH Keys

For private Git repository access via SSH:

**SSH Key Management:**

* Configured at Organization level by Admins
* Associate SSH key with template in Variables section
* Provides secure access to private repositories

## On-Premises Git Servers

### Enterprise VCS Support

Full git-ops support available for:

* GitHub Enterprise
* GitLab Enterprise
* Bitbucket Server

**Communication:** Done only through self-hosted agent - no need to expose VCS to external networks.

### Private Network Access

For Git servers on private networks:

* Use "Other" VCS type
* Enable port forwarding with public IP and high port number
* **Security Recommendation:** Open firewall for incoming traffic only from env zero IPs

**Current env zero IP addresses:** Listed under [Security Overview > IP Addresses](/guides/overview/security-overview/ip-addresses)

## Advanced Template Features

### Automatic Retry Policy

Configure automatic retries for failed deployments:

**Configuration:**

* Find "Retry on failure" section in Advanced template settings
* Choose retry triggers: Deploy, Destroy, or both
* Set number of retry attempts
* Optional: Define regex pattern for specific error types

**Behavior:**

* Only retries the apply/destroy step
* All errors retried if no regex pattern provided
* Helps handle transient infrastructure issues

### Template Variables

Manage template-specific variables:

* **Inheritance:** Environments inherit organization-level variables by default
* **Override:** Override inherited variables at template level
* **Custom Variables:** Create new template-specific variables
* **Centralized Management:** All environments from template inherit these variables

## Finding Template Information

### Template ID

Locate template identifiers for:

* **Terraform Provider:** Use in env zero resource definitions
* **API Calls:** Reference in REST API requests
* **Integration:** Connect with external tools

Find the ID in the Template Card under the Templates tab.

## Best Practices

### Template Design

* **Reusability:** Design templates for multiple environment use
* **Consistency:** Use consistent naming and structure across templates
* **Documentation:** Include clear descriptions and variable documentation

### Variable Management

* **Centralization:** Define common variables at organization level
* **Template-Specific:** Override only when necessary
* **Security:** Use secrets for sensitive configuration
* **Validation:** Implement proper variable validation

### Access Control

* **Permissions:** Grant appropriate template access to team members
* **Token Management:** Regularly rotate Git access tokens
* **SSH Keys:** Use strong SSH keys and rotate regularly
* **Audit:** Monitor template usage and changes

This comprehensive template system gives you the foundation for consistent, reusable, and manageable infrastructure deployments across your organization.

Built with [Mintlify](https://mintlify.com).
