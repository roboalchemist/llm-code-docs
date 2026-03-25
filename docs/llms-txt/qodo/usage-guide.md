# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/usage/usage-guide.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide.md

# Usage Guide

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

## Customization

You can use Qodo Git interface as is with its default configuration, or [customize it according to your specific organization needs using the configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

The configuration file enables you to:

* Customize your Git UI's look and feel.
* Automate PR reviews and tools usage.
* [Enforce your organization's best practices and policies](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices).
* Ignore unnecessary files, folders, or PRs.
* Provide custom instructions to Commands.

See the [configuration documentation](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/what-can-you-configure) to learn more.

## Tools and Commands

[Qodo Git plugin offers several tools](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools) to help developers save time, improve code quality, and make the PR review process quicker and hassle-free:

1. **Describe:** Generates PR descriptions with title, type, summary, and walkthrough
2. **Review:** Provides comprehensive PR feedback, security concerns, and review effort estimates
3. **Improve:** Suggests actionable code improvements with implementation options
4. **Ask:** Answers questions about the PR code changes
5. **Implement: C**onvert code review discussions into ready-to-commit code changes.

Other tools include documentation generation, test creation, component analysis, and code search.

***

## Usage

First, make sure you've [set up Qodo on your platform](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation).

### How to use Qodo

Once set up, there are two ways to use Qodo:

1. **Trigger tools manually with PR comments**

   Just comment on any pull request with a command like:

   ```bash
   /review  
   /describe  
   /ask "What's going on in this PR?"
   ```

   \
   The Qodo bot will react with an :eyes: emoji to indicate it has received your comment.\
   This method of using Qodo works immediately after setup.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F4Rkm3y3H3syWfqzfytSZ%2FScreenshot%202025-04-22%20at%2014.12.11.png?alt=media&#x26;token=96b9e092-4c9e-45f6-a6eb-9cda6a34b822" alt="" width="563"><figcaption></figcaption></figure>

2. **Run tools automatically on PRs**

   When a PR is opened or updated, you can have Qodo automatically run tools like `/review`, `/describe` and others.

   Scroll down to learn how to configure that.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fe1FnghanKPRwWyjsF376%2FScreenshot%202025-04-22%20at%2014.11.38.png?alt=media&#x26;token=81f28a47-4120-4499-9a10-aeb712429724" alt="" width="563"><figcaption></figcaption></figure>

### **Customize** Qodo **using the configuration file**

You can customize Qodo using the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

For example:

```toml
[pr_reviewer]
extra_instructions = "Answer in Japanese"
```

Now, when you run `/review`, Qodo will follow your custom instructions.

Learn more about different customization options in the [configuration file documentation](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

### Run tools automatically for new PRs

You can trigger any Qodo Merge Tool to run automatically when a PR is opened:

<pre class="language-toml"><code class="lang-toml">[github_app] # Or [gitlab], [bitbucket_app], etc
# settings for "pull_request" event
handle_pr_actions = ['opened', 'reopened', 'ready_for_review']
<strong>pr_commands = [
</strong>    "/describe --pr_description.final_update_message=false",
    "/review",
    "/improve",
]
</code></pre>

#### Parameters

* `handle_pr_actions`: Sets PR actions that will trigger Qodo Merge's automatic run.
* `pr_commands`: Defines the list of Tools that will be run automatically when a PR action happens.

In the example above, when a new PR is either opened, reopened or marked as `ready for review`, Qodo Merge will run the `describe`, `review` and `improve` tools.

{% hint style="info" %}
You can configure and customize different Tool parameters in the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).
{% endhint %}

### Run tools automatically fo**r open PRs**

You can trigger any Qodo Merge Tool to run automatically when a commit is pushed to an open PR:

```toml
[github_app] # Or [gitlab], [bitbucket_app], etc
handle_push_trigger = true
push_commands = [
    "/describe --pr_description.final_update_message=false",
    "/review",
]
```

#### Parameters

* `handle_push_trigger`: Enables Qodo Merge to run tools when a commit is pushed to an open PR.
* `push_commands`: Defines the list of tools that will be run automatically when a new commit is pushed to the PR.

In the example above, when new code is pushed to the PR, Qodo Merge will run the `describe` and `review` tools, with the specified parameters.

### Customize automatic tools

You can customize how Qodo Merge tools behave when they run automatically.

**How it works**

You can pass custom settings directly in the `pr_commands` or `push_commands` list by using `--<config_key>=<value>` right after the tool name.

Each tool has its own config keys. The available config keys for every tool can be found in [our configuration file example](https://github.com/qodo-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L183C1-L188C1).

For example, these are the config keys available for `/update_changelog`:&#x20;

```toml
[pr_update_changelog] # /update_changelog #
push_changelog_changes=false
extra_instructions = ""
add_pr_link=true
skip_ci_on_push=true
```

So if you'd like to configure `update_changelog` to automatically run with some extra instructions, your configuration file would look something like this:

```toml
[github_app] # Or [gitlab], [bitbucket_app], etc
...
pr_commands = [ # Or push_commands
    "/update_changelog --pr_update_changelog.extra_instructions='write changelog following the template...'",
    "/improve",
]
```

### **Draft PRs**

By default, draft PRs are not considered for automatic tools, but you can change this by setting the `feedback_on_draft_pr` parameter to `true` in the configuration file.

```toml
[github_app]
feedback_on_draft_pr = true
```

***

## GitHub Action <a href="#github-action" id="github-action"></a>

You can run Qodo Merge using GitHub Actions by setting environment variables in your workflow file `.github/workflows/pr_agent.yml`.

### Run tools automatically

Add these to the `env` section:

```yaml
env:
  OPENAI_KEY: ${{ secrets.OPENAI_KEY }} # Make sure to add your OpenAI key to your repo secrets
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # Make sure to add your GitHub token to your repo secrets
  
  github_action_config.auto_review: "true" # enable\disable auto review
  github_action_config.auto_describe: "true" # enable\disable auto describe
  github_action_config.auto_improve: "true" # enable\disable auto improve
  github_action_config.pr_actions: '["opened", "reopened", "ready_for_review", "review_requested"]'
```

* `github_action_config.auto_<toolname>`: Sets a tool to run automatically when a PR action happens.
  * If no tools are set, **all tools will run** by default when a PR action happens.
* `github_action_config.pr_actions`: Sets PR actions that will trigger Qodo Merge's automatic run.
  * If no PR actions are set, the default configuration is `["opened", "reopened", "ready_for_review", "review_requested"]`

### **Output Handling**

You can also configure Qodo Merge to output results (like review summaries) back into the [GitHub Actions step output](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions#outputs-for-docker-container-and-javascript-actions):

```yaml
github_action_config.enable_output: "true"
```

The review output will be in JSON format at:\
`steps.<step-id>.outputs.review`

The JSON structure matches what’s defined in [`pr_reviewer_prompts.toml`](https://github.com/qodo-ai/pr-agent/blob/main/pr_agent/settings/pr_reviewer_prompts.toml).

### Customize automatic tools

To change default tool behavior, you can either:

* Add more environment variables in your `.github/workflows/pr_agent.yml` file (e.g. `pr_description.publish_labels=false`)
* Or use a [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file) in the root of your repository.

**Example using the configuration file:**

```toml
[pr_description]
publish_labels = false
```

This prevents the `/describe` tool from posting PR labels.&#x20;

The available config keys for every tool can be found in [our configuration file example](https://github.com/qodo-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L183C1-L188C1).
