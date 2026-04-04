# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/code-intelligence/best-practices.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices.md

# Best Practices

Best Practices lets Qodo learn from accepted code suggestions and continuously adapt to your team's coding patterns.

***

## Auto Best Practices

{% hint style="info" %}
**Platforms supported:** GitHub
{% endhint %}

{% hint style="warning" %}
You must [enable a Wiki](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/enabling-a-wiki) to use this feature.
{% endhint %}

Auto best practices is a Qodo capability that:

1. Identifies recurring patterns from accepted suggestions.
2. **Automatically** generates [best practices page](https://github.com/qodo-ai/pr-agent/wiki/.pr_agent_auto_best_practices) based on what your team consistently values.
3. Applies these learned patterns to future code reviews.

This creates an automatic feedback loop where the system continuously learns from your team's choices to provide increasingly relevant suggestions.&#x20;

### How to enable Auto Best Practices <a href="#relevant-configurations" id="relevant-configurations"></a>

To enable auto best practices, add the following to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[auto_best_practices]
# Disable all auto best practices usage or generation
enable_auto_best_practices = true  

# Disable usage of auto best practices file in the 'improve' tool
utilize_auto_best_practices = true 

# Extra instructions to the auto best practices generation prompt
extra_instructions = ""            

# Max number of patterns to be detected
max_patterns = 5
```

### Example

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FUcPWXfR5XMpYJht7TZC4%2FScreenshot%202025-06-22%20at%2015.02.07.png?alt=media&#x26;token=428441fd-f0a7-48db-8431-d5dec1d8b937" alt="" width="375"><figcaption></figcaption></figure>

***

## Custom Best Practices <a href="#auto-best-practices-vs-custom-best-practices" id="auto-best-practices-vs-custom-best-practices"></a>

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

### Local best practices file

For basic usage, create a `best_practices.md` file in your repository's root directory containing a list of best practices, coding standards, and guidelines specific to your repository. Qodo will use this `best_practices.md` file as a reference.

In case the PR code violates any of the best practices guidelines, Qodo will create additional suggestions, with a dedicated label: `Organization best practices`.

### Writing effective best practices files

The following guidelines apply to all best practices files:

* Write clearly and concisely.
* Include brief code examples when helpful with before/after patterns.
* Focus on project-specific guidelines that will result in relevant suggestions you actually want to get.
* Keep each file relatively short, under 800 lines, since:
  * AI models may not process effectively very long documents.
  * Long files tend to contain generic guidelines already known to AI.
* Use pattern-based structure rather than simple bullet points for better clarity.

### Example `best_practices.md`

#### Error handling

You can create a `best_practices.md` file in your repository root with content like:

```markdown
Add proper error handling with try-except blocks around external function calls.
```

Example code before:

```python
# Some code that might raise an exception
return process_pr_data(data)
```

Example code after:

```python
try:
    # Some code that might raise an exception
    return process_pr_data(data)
except Exception as e:
    logger.exception("Failed to process request", extra={"error": e})
```

#### Null checks

You can create a `best_practices.md` file in your repository root with content like:

```markdown
Add defensive null/empty checks before accessing object properties.
```

Example code before:

```python
def get_pr_code(pr_data):
    if "changed_code" in pr_data:
        return pr_data.get("changed_code", "")
    return ""
```

Example code after:

```python
def get_pr_code(pr_data):
    if pr_data is None:
        return ""
    if "changed_code" in pr_data:
        return pr_data.get("changed_code", "")
    return ""
```

***

### **Global hierarchical best practices**

For organizations managing multiple repositories with different requirements, Qodo supports a hierarchical best practices system using a dedicated global configuration repository.

**Supported scenarios:**

1. **Standalone repositories**: Individual repositories can have their own specific best practices tailored to their unique requirements
2. **Groups of repositories**: Repositories can be mapped to shared group-level best practices for consistent standards across similar projects
3. **Monorepos with subprojects**: Large monorepos can have both repository-level and subproject-level best practices, with automatic path-based matching

**Setting up global hierarchical best practices**

1\. Create a new repository named `pr-agent-settings` in your organization/workspace.

2\. Build the folder hierarchy in your `pr-agent-settings` repository. For example:

```
pr-agent-settings/
├── metadata.yaml                    # Maps repos/folders to best practice paths
└── codebase_standards/              # Root for all best practice definitions
    ├── global/                      # Global rules, inherited widely
    │   └── best_practices.md
    ├── groups/                      # For groups of repositories
    │   ├── frontend_repos/
    │   │   └── best_practices.md
    │   ├── backend_repos/
    │   │   └── best_practices.md
    │   ├── python_repos/
    │   │   └── best_practices.md
    │   ├── cpp_repos/
    │   │   └── best_practices.md
    │   └── ...
    ├── repo_a/                      # For standalone repositories
    │   └── best_practices.md
    ├── monorepo-name/               # For monorepo-specific rules 
    │   ├── best_practices.md        # Root level monorepo rules
    │   ├── service-a/               # Subproject best practices
    │   │   └── best_practices.md
    │   └── service-b/               # Another subproject
    │       └── best_practices.md
    └── ...                          # More repositories
```

{% hint style="info" %}
**Note:** In this structure, `pr-agent-settings`, `codebase_standards`, `global`, `groups`, `metadata.yaml`, and `best_practices.md` are hardcoded names that must be used exactly as shown.

All other names (such as `frontend_repos`, `backend_repos`, `repo_a`, `monorepo-name`, `service-a`, etc.) are examples and should be replaced with your actual repository and service names.
{% endhint %}

{% hint style="success" %}

### Grouping and categorizing best practices

* Each folder (including the global folder) can contain a single `best_practices.md` file.
* Organize repository best practices by creating subfolders within the `groups` folder.\
  Group them by purpose, programming languages, or other categories
  {% endhint %}

3\. Define the metadata file `metadata.yaml` that maps your repositories to their relevant best practices paths. For example:

```yaml
# Standalone repos
repo_a:
  best_practices_paths:
    - "repo_a"

# Group-associated repos
repo_b:
  best_practices_paths:
    - "groups/backend_repos"

# Multi-group repos
repo_c:
  best_practices_paths:
    - "groups/frontend_repos"
    - "groups/backend_repos"

# Monorepo with subprojects
monorepo-name:
  best_practices_paths:
    - "monorepo-name"
  monorepo_subprojects:
    service-a:
      best_practices_paths:
        - "monorepo-name/service-a"
    service-b:
      best_practices_paths:
        - "monorepo-name/service-b"
```

4\. Set the following configuration in your global configuration file:

```toml
[best_practices]
enable_global_best_practices = true
```

#### Best practices priority

When global best practices are enabled, Qodo follows this priority order:

1\. **Primary**: Global hierarchical best practices from `pr-agent-settings` repository:

```
1.1 If the repository is mapped in `metadata.yaml`, it uses the specified paths

1.2 For monorepos, it automatically collects best practices matching PR file paths

1.3 If no mapping exists, it falls back to the global best practices
```

2\. **Fallback**: Local repository `best_practices.md` file:

```
2.1 Used when global best practices are not found or configured

2.2 Acts as a safety net for repositories not yet configured in the global system

2.3 Local best practices are completely ignored when global best practices are successfully loaded
```

#### Edge cases and behavior

* **Missing paths**: If specified paths in `metadata.yaml` don't exist in the file system, those paths are skipped
* **Monorepo subproject matching**: For monorepos, Qodo automatically matches PR file paths against subproject paths to apply relevant best practices
* **Multiple group inheritance**: Repositories can inherit from multiple groups, and all applicable best practices are combined

#### Best practices suggestions label

Best practice suggestions are labeled as `Organization best practice` by default.

To customize this label, modify it in your configuration file:

```toml
[best_practices]
organization_name = "..."
```

And the label will be: `{organization_name} best practice`.

<figure><img src="https://codium.ai/images/pr_agent/org_best_practice.png" alt="" width="375"><figcaption></figcaption></figure>

***

## How It Works

#### 1. **Exploration Phase** – Finding Code Issues

The `improve` tool scans PR code changes for potential issues—not minor formatting errors, but real problems like bugs, logic flaws, or anti-patterns.\
This phase is **exploratory by design**, helping surface meaningful suggestions beyond predefined categories.

#### 2. **Tracking Implemented Suggestions**

Qodo automatically tracks accepted AI-generated suggestions. When PR authors apply a suggestion, it’s logged in the `.pr_agent_accepted_suggestions` Wiki page.

This tracking provides the foundation for learning what works.

#### 3. **Learning from Accepted Patterns**

Once a month, Qodo analyzes accepted suggestions to generate a custom `.pr_agent_auto_best_practices` Wiki file.\
These patterns represent practices that your team implicitly approves through repeated adoption.

#### 4. **Applying Best Practices in Reviews**

During the next use of the `improve` tool:

* The tool checks code changes against these learned patterns.
* If a suggestion matches a learned best practice, it’s clearly labeled with **“Learned best practice.”**
* This creates a **two-phase analysis**:
  * **Exploratory**: Surfaces general issues without restrictions
  * **Targeted**: Checks for violations of established, successful patterns

Keeping both phases separate allows Qodo to stay innovative while building on your team’s real-world feedback.
