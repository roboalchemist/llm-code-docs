# Source: https://docs.qodo.ai/qodo-documentation/on-prem/context-engine/setup-context-engine/gitlab.md

# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/getting-started/enterprise-self-hosted/3.-index-your-codebase/gitlab.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/install/gitlab.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/gitlab.md

# GitLab

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

Learn more on how to setup Qodo on GitLab.

## Before you start <a href="#github-cloud" id="github-cloud"></a>

Installing Qodo on GitLab allows you to enhance your merge requests with automated insights and improvements.

You can configure it for a single repository or roll it out to multiple projects or groups.

Setup time is usually a few minutes, depending on whether you’re using a webhook or CI pipeline approach.

After setup, Qodo will monitor merge requests, process their content, and publish outputs like descriptions, reviews, or improvement suggestions directly to your MRs.

***

## 1. Log In to Qodo Portal <a href="#github-cloud" id="github-cloud"></a>

Before setting up Qodo, make sure to [create a Qodo account and sign in](https://app.qodo.ai/signin).

Once you've signed in to the Qodo Portal, you can follow the [Qodo Git plugin installation guide](https://app.qodo.ai/qodo-merge/installation) straight from the portal, or continue reading here.

## 2. Setup Qodo

Once you've signed in to your [Qodo account](https://app.qodo.ai/signin), follow the instructions in the [Qodo Portal](https://app.qodo.ai/qodo-merge/installation) or below to setup Qodo on GitLab.

### GitLab Repository <a href="#gitlab-cloud" id="gitlab-cloud"></a>

{% hint style="success" %}
**This installation method is available to subscribed users only.**

Visit [Qodo's Plans page](https://www.qodo.ai/pricing/) to learn more.
{% endhint %}

1. **Generate a GitLab access token:** Generate either a personal, project or group level access token, and store the token in a safe place.
   * **Make sure to enable the "api" scope** in order to allow Qodo to read pull requests, comment and respond to requests.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fkt6ecKovwYIQBMnenybk%2FScreenshot%202025-04-20%20at%2015.17.22.png?alt=media&#x26;token=078fb6e0-772f-41a4-b146-6b88b48ad252" alt=""><figcaption></figcaption></figure>

2. **Generate a shared secret through Qodo registration page:**
   1. Go to [https://register.gitlab.pr-agent.codium.ai](https://register.gitlab.pr-agent.codium.ai/?__hstc=232934721.e3c03c2c582e511ab7ec66e5818cd519.1727274486526.1744298083607.1744704531758.50&__hssc=232934721.6.1744704531758&__hsfp=4022204572).
   2. Fill in your generated GitLab token and your company or personal name in the appropriate fields and click **Submit**.
   3. A shared secret will be generated. Store it in a safe place.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FvFoUa3VuZg2Z97PWo3Re%2FScreenshot%202025-04-21%20at%2011.35.31.png?alt=media&#x26;token=9da644dd-42df-4ace-9e11-773f9cd8d917" alt="" width="473"><figcaption></figcaption></figure>

2. **Install a GitLab webhook:**
   1. Go to the settings menu in your repository or groups, and click W**ebhooks.**
   2. Click **Add new webhook**.
   3. In the webhook definition form, fill in the following fields:
      1. **URL:** <https://pro.gitlab.pr-agent.codium.ai/webhook>
      2. **Secret token:** Your Qodo key
      3. **Trigger:** Check the **Comments** and **Merge request events** boxes.
      4. **SSL Verification:** Check the **Enable SSL verification** box.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FL9bf53J4l1dziwKTrcv7%2Fgitlab_pro_webhooks.webp?alt=media&#x26;token=acf64b28-f16a-45c8-88d3-d15be5f4f218" alt="" width="563"><figcaption></figcaption></figure>

**You’re all set!** Start using Qodo

{% hint style="info" %}
[Visit our usage guide](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide) for next steps.
{% endhint %}

### GitLab Pipeline <a href="#run-as-a-gitlab-pipeline" id="run-as-a-gitlab-pipeline"></a>

1. **Create a CI file:** Create a new file named `.gitlab-ci.yml` with the content below:

```yaml
stages:
  - pr_agent

pr_agent_job:
  stage: pr_agent
  image:
    name: codiumai/pr-agent:latest
    entrypoint: [""]
  script:
    - cd /app
    - echo "Running PR Agent action step"
    - export MR_URL="$CI_MERGE_REQUEST_PROJECT_URL/merge_requests/$CI_MERGE_REQUEST_IID"
    - echo "MR_URL=$MR_URL"
    - export gitlab__url=$CI_SERVER_PROTOCOL://$CI_SERVER_FQDN
    - export gitlab__PERSONAL_ACCESS_TOKEN=$GITLAB_PERSONAL_ACCESS_TOKEN
    - export config__git_provider="gitlab"
    - export openai__key=$OPENAI_KEY
    - python -m pr_agent.cli --pr_url="$MR_URL" describe
    - python -m pr_agent.cli --pr_url="$MR_URL" review
    - python -m pr_agent.cli --pr_url="$MR_URL" improve
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

* This script will run Qodo Merge on every new merge request.
  * You can modify the `rules` section to run Qodo Merge on different events.
  * You can also modify the `script` section to run different Qodo Merge commands, or with different parameters by exporting different environment variable&#x73;**.**

{% hint style="info" %}
**Note**: The `$CI_SERVER_FQDN` variable is available only from GitLab version 16.10.

If you're using an earlier version, you can combine the variables `$CI_SERVER_HOST` and `$CI_SERVER_PORT` to achieve the same result.
{% endhint %}

2. **Add masked vairables:** Go to **CI/CD**, then choose **Variables**. In the masked variables section, add the following masked variables to your GitLab repository:

   * `GITLAB_PERSONAL_ACCESS_TOKEN`: Your GitLab personal access token.
   * `OPENAI_KEY`: Your OpenAI key.

   Don't set the variables as `protected`, or the pipeline will not have access to them.

**You’re all set!** Start using Qodo

{% hint style="info" %}
[Visit our usage guide](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide) for next steps.
{% endhint %}

### GitLab Webhook Server <a href="#run-a-gitlab-webhook-server" id="run-a-gitlab-webhook-server"></a>

1. **Create a new GitLab user:** In the group or project where you'd like to add Qodo Merge, create a new user and give it the **Reporter** role.
2. **Generate token:** Generate a `personal_access_token` with `api` access.
3. **Obtain secret:** Generate a random secret for your app, and save it for later (`shared_secret`). For example, you can use:

```
SHARED_SECRET=$(python -c "import secrets; print(secrets.token_hex(10))")
```

4. **Clone this repository**:

```
git clone https://github.com/qodo-ai/pr-agent.git
```

5. **Prepare variables and secrets:**&#x20;
   1. In the [Qodo Merge configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):
      * Set `config.git_provider` to "gitlab"
   2. In the secrets file/variables:
      * Set your AI model key in the respective section
      * In the `[gitlab]` section:
        * Set `personal_access_token` with the token from step 2.
        * Set `shared_secret` with the random secret from step 3.
6. **Build Docker image:** Build a Docker image for the app.\
   For example using Dockerhub:

   ```
   docker build . -t gitlab_pr_agent --target gitlab_webhook -f docker/Dockerfile
   docker push codiumai/pr-agent:gitlab_webhook  # Push to your Docker repository
   ```
7. **Set the environmente variables in the Docker image:**

```
CONFIG__GIT_PROVIDER=gitlab
GITLAB__PERSONAL_ACCESS_TOKEN=<personal_access_token>
GITLAB__SHARED_SECRET=<shared_secret>
GITLAB__URL=https://gitlab.com
OPENAI__KEY=<your_openai_api_key>
```

8. **Create webhook:** Create a webhook in your GitLab project. Make sure to:
   * Set the URL to `http[s]://<PR_AGENT_HOSTNAME>/webhook`
   * Set the secret token to the generated secret from step 3.
   * Enable the triggers `push`, `comments` and `merge request events`.

**You’re all set!** Start using Qodo

{% hint style="info" %}
[Visit our usage guide](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide) for next steps.
{% endhint %}
