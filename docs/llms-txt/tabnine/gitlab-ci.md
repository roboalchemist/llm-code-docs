# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/gitlab-ci.md

# GitLab CI

Run Tabnine CLI on every GitLab merge request to automate code review, documentation, test generation, and more.

### Overview

The Tabnine GitLab CI job runs the Tabnine CLI Agent as a pipeline stage on merge request events. The included configuration provides a comprehensive code review prompt that analyzes the MR diff and posts a summary note and inline discussion comments directly on the merge request. You can customize the prompt to automate any task — see [Customizing the Prompt](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/..#customizing-the-prompt).

### Prerequisites

* A GitLab project with CI/CD pipelines enabled
* A Tabnine account with Agents enabled
* `TABNINE_KEY` - Tabnine [Personal access token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens)
* `GITLAB_API_TOKEN` - A GitLab personal or project access token with `api` scope

{% hint style="warning" %}
Tabnine use is limited to one user per seat under the license agreement. If you want to use Tabnine in a CI/CD pipeline, contact our team.
{% endhint %}

### Quick Setup

{% stepper %}
{% step %}
**Add CI/CD variables**

Go to your project's **Settings > CI/CD > Variables** and add:

| Variable           | Value                                | Options                             |
| ------------------ | ------------------------------------ | ----------------------------------- |
| `TABNINE_KEY`      | Tabnine Personal Access Token        | ✅ Mask variable, ✅ Protect variable |
| `GITLAB_API_TOKEN` | GitLab access token with `api` scope | ✅ Mask variable                     |
| {% endstep %}      |                                      |                                     |

{% step %}
**Add the CI job**

Copy the `.gitlab-ci.yml` from the [tabnine-pr-agent repository](https://github.com/codota/tabnine-pr-agent/tree/main/GitLab) to the root of your GitLab repository.

If you already have a `.gitlab-ci.yml`, merge the `review` stage and `tabnine-code-review` job into your existing configuration:

{% code title=".gitlab-ci.yml" %}

```yaml
stages:
  - review

tabnine-code-review:
  stage: review
  image: node:20
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    TABNINE_HOST: "https://console.tabnine.com"
    TABNINE_MODEL_ID: ""
  before_script:
    # Input validation
    - |
      if [ -z "$TABNINE_KEY" ]; then
        echo "Error: TABNINE_KEY not set"
        exit 1
      fi
      if [ -z "$GITLAB_API_TOKEN" ]; then
        echo "Error: GITLAB_API_TOKEN not set"
        exit 1
      fi

    - apt-get update -qq && apt-get install -y -qq curl git jq > /dev/null 2>&1

    # Install Tabnine CLI
    - |
      curl -fsSL "$TABNINE_HOST/update/cli/installer.mjs" -o installer.mjs
      node installer.mjs "$TABNINE_HOST"
      if [ ! -f ~/.local/bin/tabnine ]; then
        echo "Error: Tabnine CLI installation failed"
        exit 1
      fi

    # Configure git
    - git config user.name "Tabnine CLI Agent"
    - git config user.email "TabnineCLI@tabnine.com"

    # Configure Tabnine Auth & Settings
    - |
      mkdir -p ~/.tabnine/agent
      MODEL_BLOCK=""
      if [ -n "$TABNINE_MODEL_ID" ]; then
        MODEL_BLOCK=",\"model\":{\"name\":\"$TABNINE_MODEL_ID\"}"
      fi
      cat << EOF > ~/.tabnine/agent/settings.json
      {
        "general": { "tabnineHost": "$TABNINE_HOST" },
        "security": { "auth": { "selectedType": "tabnine-personal" } }${MODEL_BLOCK}
      }
      EOF
      chmod 600 ~/.tabnine/agent/settings.json

  script:
    # The agent reviews the MR diff and posts comments
    - TABNINE_TOKEN=$TABNINE_KEY ~/.local/bin/tabnine -y -p "<REVIEW_PROMPT>"
  allow_failure: true
```

{% endcode %}

See the [full configuration](https://github.com/codota/tabnine-pr-agent/blob/main/GitLab/.gitlab-ci.yml) for the complete review prompt.
{% endstep %}

{% step %}
**Open a merge request**

Push the configuration and open an MR. The Tabnine Code Review job will run automatically.
{% endstep %}
{% endstepper %}

### Configuration

#### Required CI/CD Variables

| Variable           | Description                                                                   |
| ------------------ | ----------------------------------------------------------------------------- |
| `TABNINE_KEY`      | Tabnine PAT. Mark as **Masked** and **Protected**.                            |
| `GITLAB_API_TOKEN` | GitLab personal or project access token with `api` scope. Mark as **Masked**. |

#### Optional CI/CD Variables

| Variable           | Default                       | Description                                                                          |
| ------------------ | ----------------------------- | ------------------------------------------------------------------------------------ |
| `TABNINE_HOST`     | `https://console.tabnine.com` | Tabnine host URL (for self-hosted / EMT installations)                               |
| `TABNINE_MODEL_ID` | —                             | Model ID for the AI agent. If empty, uses the system default from the admin console. |

### GitLab API Token

The `GITLAB_API_TOKEN` is used by the agent to interact with the GitLab API — fetching MR details, reading diffs, and posting comments.

**Creating a token:**

{% stepper %}
{% step %}
Go to **User Settings > Access Tokens** (personal) or **Project Settings > Access Tokens** (project-scoped)
{% endstep %}

{% step %}
Create a token with the `api` scope
{% endstep %}

{% step %}
Set an appropriate expiration date
{% endstep %}

{% step %}
Add it as a CI/CD variable named `GITLAB_API_TOKEN`
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Project access tokens** are preferred over personal tokens for CI/CD use, as they are scoped to a single project and can be managed independently.
{% endhint %}

### How It Works

{% stepper %}
{% step %}
Validates that `TABNINE_KEY` and `GITLAB_API_TOKEN` are set
{% endstep %}

{% step %}
Installs Tabnine CLI and dependencies (`curl`, `git`, `jq`)
{% endstep %}

{% step %}
Configures authentication and settings
{% endstep %}

{% step %}
Cleans up previous Tabnine PR Bot notes from the MR
{% endstep %}

{% step %}
Runs the review — the agent uses the GitLab API (`$CI_API_V4_URL`) to fetch MR changes, analyze the diff, and post notes and discussion comments
{% endstep %}
{% endstepper %}

The job uses these GitLab CI predefined variables automatically:

* `CI_API_V4_URL` — GitLab API base URL
* `CI_PROJECT_ID` — Project ID
* `CI_MERGE_REQUEST_IID` — MR internal ID
* `CI_MERGE_REQUEST_DIFF_HEAD_SHA` — Head commit SHA
* `CI_MERGE_REQUEST_DIFF_BASE_SHA` — Base commit SHA

### Important Notes

{% hint style="warning" %}
**`allow_failure: true`** is recommended so that a review failure does not block your CI pipeline. Code review is advisory — it should not prevent merges.
{% endhint %}

{% hint style="info" %}
The job only runs on merge request events (`$CI_PIPELINE_SOURCE == "merge_request_event"`). It will not trigger on regular branch pushes.
{% endhint %}

### Customization

#### Using a Specific Model

Set the `TABNINE_MODEL_ID` CI/CD variable in **Settings > CI/CD > Variables**, or override it in the job:

{% code title="Override model in job" %}

```yaml
tabnine-code-review:
  variables:
    TABNINE_MODEL_ID: "your-model-id"
```

{% endcode %}

#### Self-Hosted / EMT Installations

Set the `TABNINE_HOST` variable:

{% code title="Override host in job" %}

```yaml
tabnine-code-review:
  variables:
    TABNINE_HOST: "https://tabnine.your-company.com"
```

{% endcode %}

### Troubleshooting

<details>

<summary>"Error: TABNINE_KEY not set"</summary>

The CI/CD variable is missing or empty.

**Solution:** Add `TABNINE_KEY` in **Settings > CI/CD > Variables**. Mark it as **Masked** and **Protected**.

</details>

<details>

<summary>"Error: GITLAB_API_TOKEN not set"</summary>

The CI/CD variable is missing or empty.

**Solution:** Create a GitLab access token with `api` scope and add it as a CI/CD variable named `GITLAB_API_TOKEN`.

</details>

<details>

<summary>Job does not run on merge requests</summary>

The pipeline is not triggered by merge request events.

**Possible causes:**

* The `rules` block is missing or misconfigured
* The project does not have **Merge request pipelines** enabled
* Check that the rule is: `if: '$CI_PIPELINE_SOURCE == "merge_request_event"'`

</details>

<details>

<summary>No comments appear on the MR</summary>

**Possible causes:**

* The `GITLAB_API_TOKEN` lacks `api` scope
* The MR diff is empty or contains only low-risk changes
* Check the job logs for API errors

</details>

### See Also

* [Git Integrations Overview](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations) — Supported platforms and review capabilities
* [GitHub Actions](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/github-actions) — Setup for GitHub
* [Bitbucket Pipelines](https://docs.tabnine.com/main/getting-started/tabnine-cli/git-integrations/bitbucket-pipelines) — Setup for Bitbucket
