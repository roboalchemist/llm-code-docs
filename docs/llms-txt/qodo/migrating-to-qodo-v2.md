# Source: https://docs.qodo.ai/qodo-documentation/code-review/migrating-to-qodo-v2.md

# Migrating to Qodo v2

{% hint style="warning" %}
Starting February 4, 2026, new Qodo accounts will not have access to the Qodo v1 code review experience.
{% endhint %}

This guide explains how customers using Qodo v1 can transition to Qodo v2’s new code review experience safely and incrementally.

The goal is to let you test and validate the new review behavior before enabling it broadly across your organization.

To use the new code review experience, you update your repository configuration and enable new review commands. During migration, you can run the new review alongside existing commands for testing purposes, then remove duplicates once validation is complete.

### Step 1: Update your repository configuration

Configuration for code review lives in your repository’s [configuration](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview). In the `.pr_agent.toml` you can see which review commands are enabled and how feedback is generated.

#### Add the new review commands

In the `git_provider` section (varies depending on your provider), add the new review commands (prefixed with `/agentic`):

{% code expandable="true" %}

```toml

⚠️ Select ONLY ONE section below — the one that matches your git provider.
# Do not include multiple provider sections in the same configuration file.

# GitHub App
[github_app]
pr_commands = [
  "/agentic_describe",
  "/agentic_review"
]

# GitLab
[gitlab]
pr_commands = [
  "/agentic_describe",
  "/agentic_review"
]

# Bitbucket Cloud / App
[bitbucket_app]
pr_commands = [
  "/agentic_describe",
  "/agentic_review"
]

# Bitbucket Server / Data Center
[bitbucket_server]
pr_commands = [
  "/agentic_describe",
  "/agentic_review"
]

# Azure DevOps Server
[azure_devops_server]
pr_commands = [
  "/agentic_describe",
  "/agentic_review"
]
```

{% endcode %}

The new commands combine and replace multiple legacy commands, including `/improve` `/review` `/describe` & `/compliance`

{% hint style="info" %}
During testing, both old and new review commands may run in parallel for comparison, but once migration is complete, older commands should be removed to avoid duplicate feedback and noise.
{% endhint %}

**Optional: Test the new review manually**

Manual testing is an optional way to preview the new code review experience before or during configuration.

In any pull request comment, enter:

```
/agentic_describe 
/agentic_review
```

This enables you to:

* Validate the new review output on real pull requests
* Compare results with existing review behavior
* Test without changing repository configuration

{% hint style="info" %}
Manual invocation is intended for testing and validation.
{% endhint %}

### Step 2: Enable on a pilot repository

Before rolling out the new code review experience across your organization, we recommend enabling it on a pilot repository.

This helps you:

* Evaluate signal quality and noise levels
* Confirm the new review behavior meets expectations
* Adjust configuration if needed
* Remove duplicate commands after validation

**Configuration details**

To learn how to configure options such as severity thresholds, display modes, verbosity levels, and ignore rules, see [Configuration](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) fundamentals.&#x20;

### Step 3: Enable on entire organization

After you’ve validated the new code review experience in a pilot repository, you can roll it out across your organization by applying the configuration at the organization level.

To enable the new review commands across all repositories, define them in the **global organization configuration**:

1. Create a repository in your organization named:\
   \&#xNAN;**`pr-agent-settings`**
2. Add a **`pr_agent.toml`** file to the root of that repository’s default branch.
3. In the `git_provider` section, set the new review commands:<br>

   <pre class="language-toml" data-expandable="true"><code class="lang-toml">⚠️ Select ONLY ONE section below — the one that matches your git provider.
   # Do not include multiple provider sections in the same configuration file.

   # GitHub App
   [github_app]
   pr_commands = [
     "/agentic_describe",
     "/agentic_review"
   ]

   # GitLab
   [gitlab]
   pr_commands = [
     "/agentic_describe",
     "/agentic_review"
   ]

   # Bitbucket Cloud / App
   [bitbucket_app]
   pr_commands = [
     "/agentic_describe",
     "/agentic_review"
   ]

   # Bitbucket Server / Data Center
   [bitbucket_server]
   pr_commands = [
     "/agentic_describe",
     "/agentic_review"
   ]

   # Azure DevOps Server
   [azure_devops_server]
   pr_commands = [
     "/agentic_describe",
     "/agentic_review"
   ]
   </code></pre>
4. Merge the change.

After this change is merged, the configuration applies as the default for all repositories in the organization (unless overridden by a repo-level or wiki configuration).

### Step 4: Remove Qodo v1 configuration

Once you enable the new commands broadly, remove older review commands from any configuration location where they are still defined (wiki, repo-level, or global).  See [Configuration](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview) fundamentals for more details.&#x20;

#### What you’ll notice in your PRs

After rollout, review output will be consolidated and more structured:

* Compliance and Code Suggestions will no longer appear as separate outputs (they are incorporated into the new review experience)
* Issues are grouped by priority (for example, Action Required vs Remediation Recommended)
* Findings include clearer explanations and direct references to relevant code
* Reviews include agent-assisted fix prompts to help resolve issues faster

These changes are expected and reflect a more coordinated and prioritized review flow.
