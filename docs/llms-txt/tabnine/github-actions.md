# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/github-actions.md

# GitHub Actions

Run Tabnine CLI on every GitHub pull request to automate code review, documentation, test generation, and more.

### Overview

The Tabnine GitHub Action is a [composite action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action) that installs the Tabnine CLI, authenticates, and runs the agent in non-interactive mode on every pull request. The included configuration provides a comprehensive code review prompt, but you can customize the prompt to automate any task — documentation generation, test scaffolding, changelog drafting, and more.

#### Composite Action vs. Standalone Workflow

There are two ways to use Tabnine with GitHub Actions:

| Approach                           | Best For                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Composite Action** (recommended) | Most users - minimal setup, automatic updates when you bump the action version                                          |
| **Standalone Workflow**            | Users who want full control over every step, need to customize the setup, or prefer not to depend on an external action |

The **Quick Setup** below uses the composite action. If you prefer the standalone approach, copy `GitHub/tabnine-review.yml` from [this repository](https://github.com/codota/tabnine-pr-agent/tree/main/GitHub) into your project at `.github/workflows/tabnine-review.yml`. The standalone workflow contains all the same steps (CLI installation, authentication, cleanup, and the code review prompt) inlined directly, so you can modify any part of it.

{% hint style="info" %}
The standalone workflow uses GitHub **repository variables** (`vars.TABNINE_HOST`, `vars.TABNINE_MODEL_ID`) for optional configuration instead of action inputs. Set them in **Settings > Secrets and variables > Actions > Variables tab > New repository variable**.
{% endhint %}

### Prerequisites

* A GitHub repository with Actions enabled
* A Tabnine account with Agents enabled
* `TABNINE_KEY` - Tabnine [Personal access token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens)

{% hint style="warning" %}
Tabnine use is limited to one user per seat under the license agreement. If you want to use Tabnine in a CI/CD pipeline, contact our team.
{% endhint %}

### Quick Setup

{% stepper %}
{% step %}
**Add the `TABNINE_KEY` secret**

Go to your repository's **Settings > Secrets and variables > Actions** and add a new repository secret named `TABNINE_KEY` with your Tabnine PAT.
{% endstep %}

{% step %}
**Create the workflow file**

Create `.github/workflows/tabnine-review.yml` in your repository:

{% code title=".github/workflows/tabnine-review\.yml" %}

```yaml
name: "Tabnine PR Review Agent"

on:
  pull_request:
    branches:
      - main

permissions:
  contents: read
  pull-requests: write

jobs:
  review_pr:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Review PR
        uses: codota/tabnine-pr-agent@v2
        continue-on-error: true
        with:
          TABNINE_KEY: ${{ secrets.TABNINE_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          repository: ${{ github.repository }}
          pull_request_number: ${{ github.event.pull_request.number }}
          head_sha: ${{ github.event.pull_request.head.sha }}
          base_sha: ${{ github.event.pull_request.base.sha }}
```

{% endcode %}
{% endstep %}

{% step %}
**Open a pull request**

Push the workflow file and open a PR. The Tabnine Code Review will run automatically and post its findings as comments.
{% endstep %}
{% endstepper %}

### Configuration

#### Required Inputs

| Input                 | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| `TABNINE_KEY`         | Tabnine Personal access token. Store as a **repository secret**.            |
| `github_token`        | GitHub token for posting comments. Use the built-in `secrets.GITHUB_TOKEN`. |
| `repository`          | Repository in `owner/repo` format. Use `${{ github.repository }}`.          |
| `pull_request_number` | PR number. Use `${{ github.event.pull_request.number }}`.                   |
| `head_sha`            | PR head commit SHA. Use `${{ github.event.pull_request.head.sha }}`.        |
| `base_sha`            | PR base commit SHA. Use `${{ github.event.pull_request.base.sha }}`.        |

#### Optional Inputs

| Input          | Default                       | Description                                                              |
| -------------- | ----------------------------- | ------------------------------------------------------------------------ |
| `tabnine_host` | `https://console.tabnine.com` | Tabnine host URL (for self-hosted / EMT installations)                   |
| `model_id`     | —                             | Model ID for the AI agent. Overrides the default from the admin console. |

### Important Notes

{% hint style="warning" %}
**Full git history required.** The checkout step must use `fetch-depth: 0` so the agent can access the full diff between the PR branch and the base branch.
{% endhint %}

{% hint style="info" %}
**`continue-on-error: true`** is recommended so that a review failure does not block your CI pipeline. Code review is advisory - it should not prevent merges.
{% endhint %}

### Permissions

The workflow requires these GitHub token permissions:

| Permission      | Level   | Why                            |
| --------------- | ------- | ------------------------------ |
| `contents`      | `read`  | Read repository files and diff |
| `pull-requests` | `write` | Post review comments on the PR |

### How It Works

{% stepper %}
{% step %}

### Install the CLI

Installs Tabnine CLI from your Tabnine host.
{% endstep %}

{% step %}

### Configure authentication

Configures authentication using the `TABNINE_KEY` secret.
{% endstep %}

{% step %}

### Clean up previous comments

Cleans up any previous Tabnine PR Bot comments (to avoid duplicates on re-runs).
{% endstep %}

{% step %}

### Run the agent

Runs the agent with the configured prompt — the agent has access to the repository, the PR diff (via `gh pr diff`), shell commands, and the GitHub API.
{% endstep %}
{% endstepper %}

The agent uses the pre-authenticated `gh` CLI, so no additional API tokens are needed beyond `GITHUB_TOKEN`.

With the included code review prompt, the agent fetches the diff, classifies risk, audits the code, and posts inline comments and a summary. You can replace or extend the prompt to perform other tasks.

### Customization

#### Reviewing Only Specific Branches

Update the `on` trigger to limit which branches get reviewed:

{% code title="workflow trigger" %}

```yaml
on:
  pull_request:
    branches:
      - main
      - develop
      - 'release/**'
```

{% endcode %}

#### Using a Specific Model

Pass a `model_id` to override the default AI model:

{% code title="Using a specific model" %}

```yaml
- name: Review PR
  uses: codota/tabnine-pr-agent@v2
  continue-on-error: true
  with:
    TABNINE_KEY: ${{ secrets.TABNINE_KEY }}
    github_token: ${{ secrets.GITHUB_TOKEN }}
    repository: ${{ github.repository }}
    pull_request_number: ${{ github.event.pull_request.number }}
    head_sha: ${{ github.event.pull_request.head.sha }}
    base_sha: ${{ github.event.pull_request.base.sha }}
    model_id: "your-model-id"
```

{% endcode %}

#### Self-Hosted / Private Installations

If you run a self-hosted Tabnine instance, set the `tabnine_host` input:

{% code title="Self-hosted Tabnine host" %}

```yaml
- name: Review PR
  uses: codota/tabnine-pr-agent@v2
  continue-on-error: true
  with:
    TABNINE_KEY: ${{ secrets.TABNINE_KEY }}
    github_token: ${{ secrets.GITHUB_TOKEN }}
    repository: ${{ github.repository }}
    pull_request_number: ${{ github.event.pull_request.number }}
    head_sha: ${{ github.event.pull_request.head.sha }}
    base_sha: ${{ github.event.pull_request.base.sha }}
    tabnine_host: "https://tabnine.your-company.com"
```

{% endcode %}

### Troubleshooting

<details>

<summary>"Error: TABNINE_KEY is required"</summary>

The `TABNINE_KEY` secret is not set or is empty.

**Solution:** Add the secret in **Settings > Secrets and variables > Actions > New repository secret**. The value should be the [Personal Access Token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens) from your Tabnine admin console.

</details>

<details>

<summary>"Error: Tabnine CLI installation failed"</summary>

The CLI installer could not be downloaded or executed.

**Solution:**

* Verify the `tabnine_host` URL is reachable from GitHub Actions runners
* If using a self-hosted runner, ensure it has internet access and Node.js 20+
* Check if your corporate firewall blocks the Tabnine host

</details>

<details>

<summary>No comments appear on the PR</summary>

The action ran but no review comments were posted.

**Possible causes:**

* The PR diff is empty or contains only low-risk changes (Tier 1 reviews may post only a summary)
* The `pull-requests: write` permission is missing from the workflow
* Check the GitHub Actions logs for errors in the "Code Review" step

</details>

<details>

<summary>Duplicate comments on re-runs</summary>

The action automatically cleans up previous Tabnine PR Bot comments before posting new ones. If duplicates appear:

**Solution:** Ensure the `github_token` has `pull-requests: write` permission, which is required for deleting old comments.

</details>

### See Also

* [Git Integrations Overview](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations) — Supported platforms and review capabilities
* [GitLab CI/CD](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/gitlab-ci) — Setup for GitLab
* [Bitbucket Pipelines](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/bitbucket-pipelines) — Setup for Bitbucket
