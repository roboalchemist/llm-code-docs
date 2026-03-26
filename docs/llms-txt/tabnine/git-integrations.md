# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations.md

# Git Integrations

Run Tabnine CLI in your CI/CD pipeline to automate tasks on every pull request — code review, documentation generation, test scaffolding, and more.

### Overview

Tabnine CLI can run in [non-interactive (headless) mode](https://docs.tabnine.com/main/getting-started/getting-started/quickstart#non-interactive-mode) inside CI/CD pipelines, triggered automatically on pull requests and merge requests. The provided integrations install the CLI, authenticate, and execute a prompt against your codebase — the agent has full access to the diff, the repository, and the platform's API to post comments and results.

The behavior is entirely driven by the **prompt** you provide. The out-of-the-box configurations include a comprehensive code review prompt, but you can customize or replace it to automate any task.

### Prerequisites

Before setting up any integration, ensure you have:

* **Tabnine account** with Agents enabled for your team
* **`TABNINE_KEY`** — Tabnine [Personal Access Token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens). Obtain this from your Tabnine admin console.
* **Node.js 20** — Available in the CI runner (GotLab/Bibucket provided configurations use the `node:20` image)

{% hint style="info" %}
The `TABNINE_KEY` is a Personal Access Token used for non-interactive (headless) authentication. Store it as a secret/secured variable in your CI/CD platform - never commit it to your repository.
{% endhint %}

{% hint style="warning" %}
Tabnine use is limited to one user per seat under the license agreement. If you want to use Tabnine in a CI/CD pipeline, please contact our team.
{% endhint %}

### Supported Platforms

| Platform                                                                                                              | Integration Type | Trigger                        |
| --------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------ |
| [GitHub Actions](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/github-actions)           | Composite Action | `pull_request` event           |
| [GitLab CI/CD](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/gitlab-ci)                  | CI Job           | `merge_request_event` pipeline |
| [Bitbucket Pipelines](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/bitbucket-pipelines) | Pipeline Step    | Pull request pipelines         |

### How It Works

```
┌─────────────────────┐
│  Developer opens    │
│  a Pull Request     │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  CI/CD pipeline     │
│  triggers           │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Tabnine CLI installs│
│  and authenticates  │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Agent executes     │
│  your prompt        │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Results posted     │
│  on the PR/MR       │
└─────────────────────┘
```

The agent runs with access to:

* **The full repository** — it can read any file, not just the diff
* **Shell commands** — it can run build tools, test runners, linters, etc.
* **The platform API** — it can post comments, fetch PR metadata, and interact with the hosting platform
* **Tabnine's context engine** — it can search across your organization's repositories, fetch service summaries, and validate against coaching guidelines

### Example Use Cases

| Use Case                 | What the Agent Does                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Code Review**          | Audits the PR diff for bugs, security issues, performance, and posts inline comments (included out-of-the-box) |
| **Documentation**        | Generates or validates documentation for changed code and posts it as a PR comment                             |
| **Test Generation**      | Scaffolds unit tests for new or modified functions                                                             |
| **Coverage Analysis**    | Identifies untested code paths in the diff and suggests what to cover                                          |
| **Changelog Drafting**   | Summarizes PR changes into a changelog entry                                                                   |
| **Migration Validation** | Checks database migrations for safety and backward compatibility                                               |
| **Custom Policies**      | Enforces team-specific conventions, naming rules, or architectural constraints                                 |

Each of these is achieved by changing the prompt passed to `tabnine -y -p "..."` in your pipeline configuration.

### Customizing the Prompt

The core of every integration is a single call to the Tabnine CLI in non-interactive mode:

```bash
~/.local/bin/tabnine -y -p "YOUR PROMPT HERE"
```

The prompt defines what the agent does. The provided configurations include a detailed code review prompt, but you can replace it with any instructions. Your prompt can reference:

* **Environment variables** — CI/CD variables like PR number, commit SHAs, branch names
* **Platform APIs** — Instructions for the agent to call the GitHub/GitLab/Bitbucket API
* **Shell commands** — The agent can execute commands you describe in the prompt
* **Tabnine tools** — Remote code search, coaching guidelines, and other built-in capabilities

{% hint style="info" %}
The `-y` flag enables auto-accept mode, so the agent executes tool calls without waiting for confirmation — essential for non-interactive CI/CD environments.
{% endhint %}

### The Included Code Review Prompt

The out-of-the-box configurations include a comprehensive code review prompt that:

{% stepper %}
{% step %}

### Fetches the PR/MR diff

Uses the platform's API to obtain the diff for the pull/merge request.
{% endstep %}

{% step %}

### Classifies the change

Assigns a risk tier (Low, Standard, High) to the change.
{% endstep %}

{% step %}

### Audits the code

Checks for correctness, security, performance, and other issues.
{% endstep %}

{% step %}

### Analyzes cross-repo impact

Uses Tabnine's context engine to assess effects across repositories.
{% endstep %}

{% step %}

### Validates against coaching guidelines

Applies team-configured coaching guidelines to the change.
{% endstep %}

{% step %}

### Posts inline comments

Adds actionable suggestions on specific lines in the diff.
{% endstep %}

{% step %}

### Posts a summary comment

Provides an overall assessment in a summary comment on the PR/MR.
{% endstep %}
{% endstepper %}

The review evaluates code against these categories, in priority order:

| Priority | Category            | Examples                                           |
| -------- | ------------------- | -------------------------------------------------- |
| **P0**   | Correctness & Logic | Null dereferences, off-by-one errors, async issues |
| **P0**   | Data Integrity      | Missing transactions, idempotency problems         |
| **P1**   | Security            | SQL injection, hardcoded secrets, auth gaps        |
| **P1**   | API Contract Safety | Breaking changes, backward compatibility           |
| **P1**   | Error Handling      | Silent failures, missing cleanup                   |
| **P1**   | Performance         | N+1 queries, blocking I/O, resource leaks          |
| **P2**   | Deployment Safety   | Migration risks, missing feature flags             |
| **P2**   | Observability       | Missing logging, exposed sensitive data            |
| **P2**   | Maintainability     | Naming, conventions, documentation                 |

### Optional Configuration

All integrations support these optional settings:

| Setting          | Description                                                       | Default                           |
| ---------------- | ----------------------------------------------------------------- | --------------------------------- |
| **Tabnine Host** | URL of your Tabnine console (for self-hosted / EMT installations) | `https://console.tabnine.com`     |
| **Model ID**     | Override the AI model used by the agent                           | System default from admin console |

### Next Steps

Set up Tabnine CLI in your CI/CD pipeline:

* [**GitHub Actions**](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/github-actions) — Step-by-step setup for GitHub
* [**GitLab CI/CD**](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/gitlab-ci) — Step-by-step setup for GitLab
* [**Bitbucket Pipelines**](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/bitbucket-pipelines) — Step-by-step setup for Bitbucket

### See Also

* [Code Review (Interactive)](https://docs.tabnine.com/main/getting-started/tabnine-cli/examples/code-review) — Using Tabnine CLI for manual code reviews
* [Model Selection](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/model-selection) — Choosing the right model
