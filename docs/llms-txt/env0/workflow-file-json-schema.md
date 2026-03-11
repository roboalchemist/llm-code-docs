# Source: https://docs.envzero.com/guides/admin-guide/workflows/workflow-file-json-schema.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow File JSON Schema

> JSON Schema definition for validating and auto-completing env0.workflow.yaml files in your IDE

Use this JSON Schema for IDE validation and auto-completion by referencing it in your editor configuration.

## JSON Schema

```json workflow-file.json theme={null}
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://docs.envzero.com/schemas/workflow-file.json",
  "title": "env0 Workflow File",
  "description": "Schema for env0 workflow files that define multi-environment deployments. A workflow file allows you to orchestrate the deployment of multiple environments with dependencies between them.",
  "type": "object",
  "additionalProperties": false,
  "required": ["environments"],
  "properties": {
    "environments": {
      "type": "object",
      "description": "A map of sub-environments in the workflow. Each key is a unique alias for the sub-environment, and the value defines its configuration.",
      "additionalProperties": {
        "$ref": "#/definitions/SubEnvironment"
      }
    },
    "settings": {
      "type": "object",
      "description": "Global workflow settings",
      "additionalProperties": false,
      "properties": {
        "environmentRemovalStrategy": {
          "type": "string",
          "description": "Determines what happens to sub-environments when they are removed from the workflow file. - destroy: The environment will be destroyed - detach: The environment will be detached but not destroyed",
          "enum": ["destroy", "detach"],
          "default": "destroy"
        }
      }
    }
  },
  "definitions": {
    "SubEnvironment": {
      "type": "object",
      "description": "Configuration for a sub-environment in the workflow",
      "additionalProperties": false,
      "required": ["name"],
      "properties": {
        "name": {
          "type": "string",
          "description": "The display name for this sub-environment. This name will be shown in the env0 UI."
        },
        "templateName": {
          "type": "string",
          "description": "The name of an existing env0 template to use for this sub-environment. Use this when referencing a pre-configured template in your organization. Note: Either 'templateName' OR 'vcs' must be specified, but not both."
        },
        "vcs": {
          "$ref": "#/definitions/VcsConfiguration",
          "description": "Inline VCS (Version Control System) configuration for this sub-environment. Use this to define the IaC source directly instead of referencing a template. Note: Either 'templateName' OR 'vcs' must be specified, but not both."
        },
        "revision": {
          "type": "string",
          "description": "The git revision (branch, tag, or commit SHA) to use. If not specified, the default branch will be used."
        },
        "workspace": {
          "type": "string",
          "description": "The Terraform/OpenTofu workspace name for this sub-environment. Useful for managing multiple instances of the same infrastructure."
        },
        "needs": {
          "type": "array",
          "description": "List of sub-environment aliases that must be deployed before this one. Creates a dependency graph for deployment ordering.",
          "items": {
            "type": "string"
          }
        },
        "requiresApproval": {
          "type": "boolean",
          "description": "If true, deployments of this sub-environment will require manual approval before proceeding. Useful for production environments.",
          "default": false
        },
        "disabled": {
          "oneOf": [{ "type": "boolean" }, { "type": "string" }],
          "description": "If set to true or 'true', this sub-environment will be skipped during deployment. Useful for temporarily disabling parts of the workflow."
        }
      }
    },
    "VcsConfiguration": {
      "type": "object",
      "description": "Inline VCS configuration for defining IaC source directly in the workflow file. This allows you to specify the repository, path, and IaC type without creating a separate template.",
      "additionalProperties": false,
      "required": ["repository", "type"],
      "properties": {
        "type": {
          "$ref": "#/definitions/IacType",
          "description": "The Infrastructure as Code type for this environment"
        },
        "repository": {
          "type": "string",
          "description": "The git repository URL containing the IaC code. Supports HTTPS and SSH URLs."
        },
        "revision": {
          "type": "string",
          "description": "The git revision (branch, tag, or commit) to use"
        },
        "path": {
          "type": "string",
          "description": "The path within the repository where the IaC code is located. Use '/' or leave empty for the repository root.",
          "default": ""
        },
        "terraformVersion": {
          "type": "string",
          "description": "The Terraform version to use. Can be: a specific version (e.g., '1.5.7') or 'RESOLVE_FROM_TERRAFORM_CODE' to auto-detect from required_version."
        },
        "opentofuVersion": {
          "type": "string",
          "description": "The OpenTofu version to use. Can be a specific version (e.g., '1.6.0')."
        },
        "terragruntVersion": {
          "type": "string",
          "description": "The Terragrunt version to use"
        },
        "terragruntTfBinary": {
          "type": "string",
          "description": "The underlying IaC binary for Terragrunt to use",
          "enum": ["terraform", "opentofu"],
          "default": "terraform"
        },
        "pulumiVersion": {
          "type": "string",
          "description": "The Pulumi version to use"
        },
        "ansibleVersion": {
          "type": "string",
          "description": "The Ansible version to use"
        },
        "fileName": {
          "type": "string",
          "description": "The CloudFormation template file name. Only used when type is 'cloudformation'."
        },
        "helmChartName": {
          "type": "string",
          "description": "The Helm chart name (when using a Helm repository)"
        },
        "isHelmRepository": {
          "type": "boolean",
          "description": "Set to true if the repository is a Helm chart repository",
          "default": false
        },
        "tokenId": {
          "type": "string",
          "description": "The ID of a stored VCS token for authentication. Use this for private repositories with token-based auth."
        },
        "tokenName": {
          "type": "string",
          "description": "The name of the VCS token (for reference)"
        },
        "sshKeys": {
          "type": "array",
          "description": "SSH keys for repository authentication. Required for SSH-based repository URLs.",
          "items": { "$ref": "#/definitions/SshKey" }
        },
        "githubInstallationId": {
          "oneOf": [{ "type": "number" }, { "type": "null" }],
          "description": "GitHub App installation ID for GitHub integration"
        },
        "bitbucketClientKey": {
          "oneOf": [{ "type": "string" }, { "type": "null" }],
          "description": "Bitbucket client key for Bitbucket Cloud integration"
        },
        "vcsConnectionId": {
          "oneOf": [{ "type": "string" }, { "type": "null" }],
          "description": "VCS connection ID for unified VCS integration"
        },
        "isGitLab": {
          "type": "boolean",
          "description": "Set to true for GitLab.com repositories",
          "default": false
        },
        "isGitLabEnterprise": {
          "type": "boolean",
          "description": "Set to true for GitLab Enterprise/self-hosted repositories",
          "default": false
        },
        "isGitHubEnterprise": {
          "type": "boolean",
          "description": "Set to true for GitHub Enterprise repositories",
          "default": false
        },
        "isBitbucketServer": {
          "type": "boolean",
          "description": "Set to true for Bitbucket Server/Data Center repositories",
          "default": false
        },
        "isAzureDevOps": {
          "type": "boolean",
          "description": "Set to true for Azure DevOps repositories",
          "default": false
        }
      }
    },
    "IacType": {
      "type": "string",
      "description": "Supported Infrastructure as Code types",
      "enum": [
        "terraform",
        "opentofu",
        "terragrunt",
        "pulumi",
        "k8s",
        "cloudformation",
        "helm",
        "ansible"
      ]
    },
    "SshKey": {
      "type": "object",
      "description": "SSH key reference for repository authentication",
      "additionalProperties": false,
      "required": ["id", "name"],
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1,
          "description": "The unique identifier of the SSH key stored in env0"
        },
        "name": {
          "type": "string",
          "description": "The display name of the SSH key"
        }
      }
    }
  },
  "examples": [
    {
      "environments": {
        "database": {
          "name": "PostgreSQL Database",
          "templateName": "aws-rds-postgres",
          "workspace": "production"
        },
        "api": {
          "name": "API Service",
          "templateName": "kubernetes-deployment",
          "needs": ["database"],
          "requiresApproval": true
        }
      }
    },
    {
      "environments": {
        "networking": {
          "name": "VPC and Networking",
          "vcs": {
            "type": "terraform",
            "repository": "https://github.com/myorg/infrastructure",
            "path": "terraform/networking",
            "terraformVersion": "1.5.7"
          }
        },
        "compute": {
          "name": "EC2 Instances",
          "vcs": {
            "type": "terraform",
            "repository": "git@github.com:myorg/infrastructure.git",
            "path": "terraform/compute",
            "terraformVersion": "RESOLVE_FROM_TERRAFORM_CODE",
            "sshKeys": [{ "id": "ssh-key-123", "name": "Deploy Key" }]
          },
          "needs": ["networking"]
        }
      }
    },
    {
      "settings": {
        "environmentRemovalStrategy": "detach"
      },
      "environments": {
        "infra": {
          "name": "Base Infrastructure",
          "templateName": "terraform-aws-base",
          "revision": "v2.0.0"
        },
        "app": {
          "name": "Application",
          "vcs": {
            "type": "helm",
            "repository": "https://github.com/myorg/helm-charts",
            "path": "charts/myapp"
          },
          "needs": ["infra"]
        },
        "monitoring": {
          "name": "Monitoring Stack",
          "templateName": "prometheus-grafana",
          "needs": ["infra"],
          "disabled": false
        }
      }
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
