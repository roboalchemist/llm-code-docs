# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/bitbucket-pipelines.md

# Bitbucket Pipelines

Run Tabnine CLI on every Bitbucket pull request to automate code review, documentation, test generation, and more.

### Overview

The Tabnine Bitbucket Pipeline step runs the Tabnine CLI Agent on pull request events. The included configuration provides a comprehensive code review prompt that analyzes the PR diff and posts a summary comment and inline comments directly on the pull request using the Bitbucket API. You can customize the prompt to automate any task — see [Customizing the Prompt](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/..#customizing-the-prompt).

### Prerequisites

* A Bitbucket repository with Pipelines enabled
* **A Tabnine account** with Agents enabled
* `TABNINE_KEY` - Tabnine [Personal access token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens)
* `BB_API_TOKEN` - A Bitbucket access token with `pullrequest:write` and `repository:read` scopes

{% hint style="warning" %}
Tabnine use is limited to one user per seat under the license agreement. If you want to use Tabnine in a CI/CD pipeline, contact our team.
{% endhint %}

### Quick Setup

{% stepper %}
{% step %}
**Add repository variables**

Go to your repository's **Repository Settings > Pipelines > Repository variables** and add:

| Variable       | Value                         | Options   |
| -------------- | ----------------------------- | --------- |
| `TABNINE_KEY`  | Tabnine Personal Access Token | ✅ Secured |
| `BB_API_TOKEN` | Bitbucket access token        | ✅ Secured |
| {% endstep %}  |                               |           |

{% step %}
**Add the pipeline configuration**

Copy the `bitbucket-pipelines.yml` from the [tabnine-pr-agent repository](https://github.com/codota/tabnine-pr-agent/tree/main/Bitbucket) to the root of your Bitbucket repository.

If you already have a `bitbucket-pipelines.yml`, merge the `pull-requests` section into your existing configuration:

{% code title="bitbucket-pipelines.yml" %}

```yaml
image: node:20

pipelines:
  pull-requests:
    '**':
      - step:
          name: Tabnine Code Review
          script:
            - export TABNINE_HOST="${TABNINE_HOST:-https://console.tabnine.com}"
            - export TABNINE_MODEL_ID="${TABNINE_MODEL_ID:-}"

            # Input validation
            - |
              if [ -z "$TABNINE_KEY" ]; then
                echo "Error: TABNINE_KEY not set"
                exit 1
              fi
              if [ -z "$BB_API_TOKEN" ]; then
                echo "Error: BB_API_TOKEN not set"
                exit 1
              fi

            # Install dependencies
            - apt-get update -qq && apt-get install -y -qq curl git jq > /dev/null 2>&1

            # Install Tabnine CLI
            - |
              curl -fsSL "$TABNINE_HOST/update/cli/installer.mjs" -o installer.mjs
              node installer.mjs "$TABNINE_HOST"

            # Configure and run review
            # ... (see full configuration link below)
```

{% endcode %}

See the [full configuration](https://github.com/codota/tabnine-pr-agent/blob/main/Bitbucket/bitbucket-pipelines.yml) for the complete pipeline including authentication setup and the review prompt.
{% endstep %}

{% step %}
**Open a pull request**

Push the configuration and open a PR. The Tabnine Code Review will run automatically.
{% endstep %}
{% endstepper %}

### Configuration

#### Required Repository Variables

| Variable       | Description                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------- |
| `TABNINE_KEY`  | Tabnine authentication credentials (PAT). Mark as **Secured**.                                     |
| `BB_API_TOKEN` | Bitbucket access token with `pullrequest:write` and `repository:read` scopes. Mark as **Secured**. |

#### Optional Repository Variables

| Variable           | Default                       | Description                                                                          |
| ------------------ | ----------------------------- | ------------------------------------------------------------------------------------ |
| `TABNINE_HOST`     | `https://console.tabnine.com` | Tabnine host URL (for self-hosted / Private installations)                           |
| `TABNINE_MODEL_ID` | —                             | Model ID for the AI agent. If empty, uses the system default from the admin console. |

### Bitbucket Access Token

The `BB_API_TOKEN` is used by the agent to interact with the Bitbucket REST API — fetching PR details, reading diffs, and posting comments.

**Creating an access token:**

{% stepper %}
{% step %}
Go to **Repository Settings > Access tokens** (repository-level) or your **Personal Settings > App passwords** (account-level)
{% endstep %}

{% step %}
Create a token with `pullrequest:write` and `repository:read` scopes
{% endstep %}

{% step %}
Add it as a repository variable named `BB_API_TOKEN` and mark it as **Secured**
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Repository access tokens** are preferred over personal app passwords for CI/CD use, as they are scoped to a single repository.
{% endhint %}

### How It Works

{% stepper %}
{% step %}

### Validate inputs

Checks that `TABNINE_KEY` and `BB_API_TOKEN` are set.
{% endstep %}

{% step %}

### Install dependencies

Installs Tabnine CLI and required tools (`curl`, `git`, `jq`).
{% endstep %}

{% step %}

### Configure authentication and settings

Sets up authentication and any pipeline-specific environment variables.
{% endstep %}

{% step %}

### Resolve destination commit SHA

Uses the Bitbucket API to resolve the destination branch commit SHA.
{% endstep %}

{% step %}

### Clean up previous comments

Removes previous Tabnine PR Bot comments from the PR.
{% endstep %}

{% step %}

### Run the review

Fetches the PR diff via the Bitbucket API (`api.bitbucket.org/2.0`), analyzes the code, and posts summary and inline comments.
{% endstep %}
{% endstepper %}

The pipeline uses these Bitbucket predefined variables automatically:

* `BITBUCKET_WORKSPACE` — Workspace slug
* `BITBUCKET_REPO_SLUG` — Repository slug
* `BITBUCKET_PR_ID` — Pull request ID
* `BITBUCKET_COMMIT` — Head commit SHA
* `BITBUCKET_PR_DESTINATION_BRANCH` — Destination branch name

### Important Notes

{% hint style="warning" %}
The `'**'` glob pattern in the `pull-requests` section means the review runs on PRs targeting **any branch**. Adjust the pattern to limit which branches trigger reviews (e.g., `'main'` or `'develop'`).
{% endhint %}

{% hint style="info" %}
Unlike GitHub Actions, Bitbucket Pipelines does not have a built-in `continue-on-error` equivalent at the step level. The pipeline step will fail if the review encounters an error. Consider wrapping the review command in a script that always exits 0 if you want advisory-only behavior.
{% endhint %}

### Customization

#### Reviewing Only Specific Branches

Change the glob pattern to match only PRs targeting specific branches:

```yaml
pipelines:
  pull-requests:
    'main':
      - step:
          name: Tabnine Code Review
          # ...
    'develop':
      - step:
          name: Tabnine Code Review
          # ...
```

#### Using a Specific Model

Set the `TABNINE_MODEL_ID` repository variable, or set a default directly in the pipeline:

```yaml
- export DEFAULT_MODEL_ID="your-model-id"
- export TABNINE_MODEL_ID="${TABNINE_MODEL_ID:-$DEFAULT_MODEL_ID}"
```

#### Self-Hosted / Private Installations

Set the `TABNINE_HOST` repository variable, or override it in the pipeline script:

```yaml
- export TABNINE_HOST="https://tabnine.your-company.com"
```

### Troubleshooting

<details>

<summary>"Error: TABNINE_KEY not set"</summary>

The repository variable is missing or empty.

Solution: Add `TABNINE_KEY` in **Repository Settings > Pipelines > Repository variables**. Mark it as **Secured**.

</details>

<details>

<summary>"Error: BB_API_TOKEN not set"</summary>

The repository variable is missing or empty.

Solution: Create a Bitbucket access token with `pullrequest:write` and `repository:read` scopes and add it as a repository variable named `BB_API_TOKEN`.

</details>

<details>

<summary>Pipeline does not run on pull requests</summary>

Possible causes:

* Pipelines are not enabled for the repository — go to **Repository Settings > Pipelines > Settings** and enable them
* The `pull-requests` section is missing or misconfigured in `bitbucket-pipelines.yml`
* The PR target branch does not match the glob pattern

</details>

<details>

<summary>No comments appear on the PR</summary>

Possible causes:

* The `BB_API_TOKEN` lacks `pullrequest:write` scope
* The PR diff is empty or contains only low-risk changes
* Check the pipeline logs for API errors

</details>

### See Also

* [Git Integrations Overview](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations) — Supported platforms and review capabilities
* [GitHub Actions](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/github-actions) — Setup for GitHub
* [GitLab CI/CD](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/gitlab-ci) — Setup for GitLab
