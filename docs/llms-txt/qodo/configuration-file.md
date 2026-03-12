# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/code-intelligence/context-engine/configuration-file.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file.md

# Configuration File

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

**The configuration file** allows you to adjust the various [tools and sub-tools](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list) used by Qodo.

### Configuration file example

An example configuration file can be found in our GitHub repository.&#x20;

**Avoid copying the entire configuration file**. **Only use the configurations you need.**

{% embed url="<https://github.com/qodo-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml>" %}

{% hint style="success" %}
**Tip: edit only what you need.**\
Keep your configuration file **minimal** by only editing the relevant settings.

**Avoid copying the entire configuration.** This could cause issues when defaults change over time.
{% endhint %}

### How to use the configuration file

The configuration file is a file named `.pr_agent.toml`, which can reside in several locations (see below).

Each [Qodo tool](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list) has its own specific configuration settings.

For example, the [review tool](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/review) uses parameters from [the `pr_reviewer` section of the configuration file](https://github.com/qodo-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L72):

```toml
...
[pr_reviewer] # /review #
# enable/disable features
require_score_review=false
require_tests_review=true
require_estimate_effort_to_review=true
...
```

If you set in `.pr_agent.toml`:

```toml
[pr_reviewer]
extra_instructions="""\
- instruction a
- instruction b
...
"""
```

Then you can give a list of extra instructions to the `review` tool, which it will follow when it runs.

See the [Tools Guide](https://qodo-merge-docs.qodo.ai/tools/) for a detailed description of the different tools and their configurations.

{% hint style="info" %}
**Show relevant configurations:**\
Set `config.output_relevant_configurations=true` to display the relevant configurations for each tool.

This can help with debugging or give you a better understanding of different configuration options.
{% endhint %}

## Possible Locations of Configuration Files <a href="#wiki-configuration-file" id="wiki-configuration-file"></a>

The possible locations of where can one place configuration files are ordered below by precedence (wiki being the highest precedence); if the same setting is defined in configuration files at two locations, the one with the higher precedence will **overwrite** the setting in the lower precedence.

### Wiki configuration file <a href="#wiki-configuration-file" id="wiki-configuration-file"></a>

{% hint style="info" %}
[Platforms supported: GitHub, GitLab, Bitbucket](#user-content-fn-1)[^1] Cloud, Azure DevOps
{% endhint %}

#### How to create a wiki configuration file

1. Enable wiki page (see [here](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/enabling-a-wiki) for instructions)
2. Edit a new page called `.pr_agent.toml`. and make sure it begins with three "\`" followed by: "toml"
3. Add any configuration parameters you'd like.
4. Save the page. Configuration takes effect immediately.

### Local configuration file <a href="#local-configuration-file" id="local-configuration-file"></a>

{% hint style="info" %}
[Platforms supported: GitHub, GitLab, Bitbucket](#user-content-fn-1)[^1], Azure DevOps
{% endhint %}

#### How to create a local configuration file

1. Create a file called `.pr_agent.toml`.
2. Edit any configuration parameter you'd like.
3. Upload the file to the root of the default branch in your repository.
4. The configuration will take effect after being merged into your repository.

### Global configuration file  <a href="#global-configuration-file" id="global-configuration-file"></a>

{% hint style="info" %}
[Platforms supported: GitHub, GitLab Cloud, Bitbucket](#user-content-fn-1)[^1] Cloud
{% endhint %}

#### How to create a global configuration file

1. Create a repository named `pr-agent-settings` in your organization.
2. In the repository `pr-agent-settings`, create a file called `.pr_agent.toml`.
3. Edit any configuration parameter you'd like.
4. Upload the file to the root of the default branch in the repository.
5. The configuration will take effect after being merged into your repository.

The `.pr_agent.toml` file in this repository will be used as the global configuration for all other repositories in the organization. Local configurations will always override global ones.

### Project/Group level configuration file <a href="#projectgroup-level-configuration-file" id="projectgroup-level-configuration-file"></a>

{% hint style="info" %}
Platforms supported: GitLab, Bitbucket Data Center, Azure DevOps
{% endhint %}

#### How to create a project/group configuration file

1. Create a repository named `pr-agent-settings` within a specific project (Bitbucket, Azure DevOps) or a group/subgroup (Gitlab).
2. In the repository `pr-agent-settings`, create a file called `.pr_agent.toml`.
3. Edit any configuration parameter you'd like.
4. Upload the file to the root of the default branch in the repository.
5. The configuration will take effect after being merged into your repository.

The configuration file in this repository will apply to all repositories directly under the same project/group/subgroup.

{% hint style="info" %}
For Gitlab, in case of a repository nested in several sub groups, the lookup for a pr-agent-settings repo will be only on one level above such repository.
{% endhint %}

### Organization level configuration file <a href="#organization-level-configuration-file" id="organization-level-configuration-file"></a>

{% hint style="info" %}
Platforms supported: Bitbucket Data Center, Azure DevOps
{% endhint %}

#### How to create an organization configuration file

**Setting up organization-level global configuration:**

1. For Bitbucket: Create a new **project** named `PR_AGENT_SETTINGS` with **project key** `PR_AGENT_SETTINGS` . For Azure DevOps: Create a new project named `pr-agent-settings`&#x20;
2. Inside this project, create a repository called `pr-agent-settings`.
3. Add a `.pr_agent.toml` configuration file to the repository (similar to the global configuration described above).
4. Optionally, you can add an organizational-level global best practices file.

All repositories across your organization will inherit configurations from this file.

{% hint style="info" %}
**Note:** If both organization-level and project-level settings are defined, the project-level settings take precedence.

A repository’s local `.pr_agent.toml` file will always override both global configurations.
{% endhint %}

[^1]:
