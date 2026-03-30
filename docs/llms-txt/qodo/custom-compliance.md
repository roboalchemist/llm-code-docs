# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/custom-compliance.md

# Custom Compliance

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

[The `compliance` tool](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/compliance) performs comprehensive compliance checks on PR code changes, validating them against security standards, ticket requirements, and custom organizational compliance checklists, thereby helping teams, enterprises, and agents maintain consistent code quality and security practices while ensuring that development work aligns with business requirements.

### Setting Up Custom Compliance <a href="#setting-up-custom-compliance" id="setting-up-custom-compliance"></a>

Each compliance is defined in a YAML file as follows:

* `title` (required): A clear, descriptive title that identifies what is being checked
* `compliance_label` (required): Determines whether this compliance generates labels for non-compliance issues (set to `true` or `false`)
* `objective` (required): A detailed description of the goal or purpose this compliance aims to achieve
* `success_criteria` and `failure_criteria` (at least one required; both recommended): Define the conditions for compliance

<details>

<summary>Example of a compliance checklist</summary>

```yaml
# pr_compliance_checklist.yaml
pr_compliances:
  - title: "Error Handling"
    compliance_label: true
    objective: "All external API calls must have proper error handling"
    success_criteria: "Try-catch blocks around external calls with appropriate logging"
    failure_criteria: "External API calls without error handling or logging"

...
```

</details>

<details>

<summary>Writing effective compliance checklists</summary>

* Avoid overly complex or subjective compliances that are hard to verify
* Keep compliances focused on security, business requirements, and critical standards
* Use clear, actionable language that developers can understand
* Focus on meaningful compliance requirements, not style preferences

</details>

<details>

<summary>Ready-to-use compliance templates</summary>

For production-ready compliance checklist templates organized by programming languages and technology stacks, check out the [PR Compliance Templates repository](https://github.com/qodo-ai/pr-compliance-templates).

</details>

### Local Compliance Checklists <a href="#local-compliance-checklists" id="local-compliance-checklists"></a>

For basic usage, create a `pr_compliance_checklist.yaml` file in your repository's root directory containing the compliance requirements specific to your repository.

The AI model will use this `pr_compliance_checklist.yaml` file as a reference, and if the PR code violates any of the compliance requirements, it will be shown in the compliance tool's comment.

### Global Hierarchical Compliance <a href="#global-hierarchical-compliance" id="global-hierarchical-compliance"></a>

Qodo supports hierarchical compliance checklists using a dedicated global configuration repository.

### **Setting up global hierarchical compliance**

1\. Create a new repository named `pr-agent-settings` in your organization or workspace.

2\. Build the folder hierarchy in your `pr-agent-settings` repository:

```
pr-agent-settings/
├── metadata.yaml                              # Maps repos/folders to compliance paths
└── codebase_standards/                        # Root for all compliance definitions
    ├── global/                                # Global compliance, inherited widely
    │   └── pr_compliance_checklist.yaml
    ├── groups/                                # For groups of repositories
    │   ├── frontend_repos/
    │   │   └── pr_compliance_checklist.yaml
    │   ├── backend_repos/
    │   │   └── pr_compliance_checklist.yaml
    │   ├── python_repos/
    │   │   └── pr_compliance_checklist.yaml
    │   ├── cpp_repos/
    │   │   └── pr_compliance_checklist.yaml
    │   └── ...
    ├── repo_a/                                # For standalone repositories
    │   └── pr_compliance_checklist.yaml
    ├── monorepo-name/                         # For monorepo-specific compliance
    │   ├── pr_compliance_checklist.yaml       # Root-level monorepo compliance
    │   ├── service-a/                         # Subproject compliance
    │   │   └── pr_compliance_checklist.yaml
    │   └── service-b/                         # Another subproject
    │       └── pr_compliance_checklist.yaml
    └── ...                                    # More repositories
```

{% hint style="info" %}
**Note:** In this structure, `pr-agent-settings`, `codebase_standards`, `global`, `groups`, `metadata.yaml`, and `pr_compliance_checklist.yaml` are hardcoded names that must be used exactly as shown.

All other names (such as `frontend_repos`, `backend_repos`, `repo_a`, `monorepo-name`, `service-a`, etc.) are examples and should be replaced with your actual repository and service names.
{% endhint %}

<details>

<summary>Grouping and categorizing compliance checklists</summary>

* Each folder (including the global folder) can contain a single `pr_compliance_checklist.yaml` file
* Organize repository compliance checklists by creating subfolders within the `groups` folder. Group them by purpose, programming languages, or other categories

</details>

3\. Define the metadata file `metadata.yaml` in the root of `pr-agent-settings`:

```yaml
# Standalone repos
qodo-merge:
  pr_compliance_checklist_paths:
    - "qodo-merge"

# Group-associated repos
repo_b:
  pr_compliance_checklist_paths:
    - "groups/backend_repos"

# Multi-group repos
repo_c:
  pr_compliance_checklist_paths:
    - "groups/frontend_repos"
    - "groups/backend_repos"

# Monorepo with subprojects
qodo-monorepo:
  pr_compliance_checklist_paths:
    - "qodo-monorepo"
  monorepo_subprojects:
    frontend:
      pr_compliance_checklist_paths:
        - "qodo-monorepo/qodo-github"
    backend:
      pr_compliance_checklist_paths:
        - "qodo-monorepo/qodo-gitlab"
```

4\. Set the following configuration:

```toml
[pr_compliance]
enable_global_pr_compliance = true
```

<details>

<summary>Compliance checklist loading strategy</summary>

1. **Global Checklists**: Hierarchical compliance from `pr-agent-settings` repository
   1. If the repository is mapped in `metadata.yaml`, it uses the specified paths and the global compliance checklist
   2. For monorepos, it automatically collects compliance checklists matching PR file paths
   3. If the repository is not mapped in `metadata.yaml`, global checklists are not loaded
2. **Local Repository Checklist**: `pr_compliance_checklist.yaml` file in the repository
   1. Loaded if present in the repository
   2. Content is merged with global checklists (if loaded) to create the final compliance checklist

</details>

***

## Configuration Options <a href="#configuration-options" id="configuration-options"></a>

<details>

<summary>General options</summary>

| Option                                  | Description                                                                                                                                                                |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `extra_instructions`                    | Optional extra instructions for the tool. For example: "Ensure that all error-handling paths in the code contain appropriate logging statements". Default is empty string. |
| `persistent_comment`                    | If set to true, the compliance comment will be persistent, meaning that every new compliance request will edit the previous one. Default is true.                          |
| `enable_user_defined_compliance_labels` | If set to true, the tool will add the label `Failed compliance check` for custom compliance violations. Default is true.                                                   |
| `enable_estimate_effort_to_review`      | If set to true, the tool will estimate the effort required to review the PR (1-5 scale) as a label. Default is true.                                                       |
| `enable_todo_scan`                      | If set to true, the tool will scan for TODO comments in the PR code. Default is false.                                                                                     |
| `enable_update_pr_compliance_checkbox`  | If set to true, the tool will add an update checkbox to refresh compliance status following push events. Default is true.                                                  |
| `enable_help_text`                      | If set to true, the tool will display help text in the comment. Default is false.                                                                                          |

</details>

<details>

<summary>Security compliance options</summary>

| Option                              | Description                                                                                                                                   |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `enable_security_compliance`        | If set to true, the tool will check for security vulnerabilities. Default is true.                                                            |
| `enable_compliance_labels_security` | If set to true, the tool will add a `Possible security concern` label to the PR when security-related concerns are detected. Default is true. |

</details>

<details>

<summary>Ticket compliance options</summary>

| Option                        | Description                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `enable_ticket_labels`        | If set to true, the tool will add ticket compliance labels to the PR. Default is false.                     |
| `enable_no_ticket_labels`     | If set to true, the tool will add a label when no ticket is found. Default is false.                        |
| `check_pr_additional_content` | If set to true, the tool will check if the PR contains content not related to the ticket. Default is false. |

</details>

## Usage Tips <a href="#usage-tips" id="usage-tips"></a>

#### Blocking PRs Based on Compliance <a href="#blocking-prs-based-on-compliance" id="blocking-prs-based-on-compliance"></a>

You can configure CI/CD Actions to prevent merging PRs with specific compliance labels:

* `Possible security concern` - Block PRs with potential security issues
* `Failed compliance check` - Block PRs that violate custom compliance checklists

Implement a dedicated [GitHub Action](https://medium.com/sequra-tech/quick-tip-block-pull-request-merge-using-labels-6cc326936221) to enforce these checklists.
