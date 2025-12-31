# Source: https://docs.bito.ai/ai-code-reviews-in-git/agent-settings/repo-level-settings.md

# Repo level settings

Repo-level Agent settings let you control how the [**AI Code Review Agent**](https://docs.bito.ai/ai-code-reviews-in-git/overview) behaves for each repository.&#x20;

By placing a **`.bito.yaml`** file in the root of your repository, you can define custom review preferences that apply only to that repository.&#x20;

Bito automatically detects the presence of a `.bito.yaml` file in a repository and applies its configuration to override the global Agent settings defined by admins in the Bito Cloud UI.

This gives developers fine-grained control while admins maintain global oversight and billing management.

## Why use repo-level settings&#x20;

Large organizations often have different review needs across projects.&#x20;

Centralized (agent-level) settings don’t scale well — especially when each repo has its own coding standards, branch structure, or tooling.&#x20;

**Repo-level configuration helps by:**&#x20;

* Enabling custom review behavior per repository.
* Allowing custom guidelines flexibility at the repo level.&#x20;
* Keeping settings version-controlled and transparent.

## How it works&#x20;

1. Add a `.bito.yaml` file to the root of your repository. To get started, [download a sample `.bito.yaml` file](https://github.com/gitbito/repo-level-settings-file).
2. Add the [supported configuration fields](#supported-settings-in-.bito.yaml-file) (key-value pairs) to specify how the Code Review Agent should behave for that repository.
3. When the Code Review Agent runs, Bito automatically detects the file and applies those settings for that repository.

{% hint style="info" %}
**Note:** Repo-level overrides are applied only if your workspace admin has enabled **“Allow config file settings”** in [Agent Settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance). This option is **required** for repo-level overrides to take effect and is **turned on by default**.
{% endhint %}

## Enabling repo-level overrides&#x20;

Admins can manage this from the [Agent Settings](https://docs.bito.ai/ai-code-reviews-in-git/install-run-using-bito-cloud/create-or-customize-an-agent-instance) panel.&#x20;

* **Setting name:** Allow config file settings&#x20;
* **Description:** Enabling this allows repositories to override Agent Settings by placing a `.bito.yaml` file in the repo root.

{% hint style="info" %}
**Note:** Only workspace admins can toggle this setting from the Bito dashboard (cannot be changed via `.bito.yaml` file).
{% endhint %}

## Supported settings in `.bito.yaml` file

You can override the following Code Review Agent settings:&#x20;

<table data-header-hidden><thead><tr><th width="257.99993896484375">Setting</th><th>Description</th></tr></thead><tbody><tr><td><strong>suggestion_mode</strong> </td><td><p>Controls how detailed the review comments are.<br><br>Choose between <strong>Essential</strong> and <strong>Comprehensive</strong> review modes:</p><ul><li>In <strong>Essential</strong> mode, only critical issues are posted as inline comments, and other issues appear in the main review summary under "Additional issues".</li><li>In <strong>Comprehensive</strong> mode, Bito also includes minor suggestion and potential nitpicks as inline comments.</li></ul><p><br><strong>Valid values:</strong> <code>essential</code> or <code>comprehensive</code></p></td></tr><tr><td><strong>post_description</strong> </td><td>Automatically create summary of changes and append to your existing pull request summary.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>post_changelist</strong></td><td>Adds a walkthrough section to pull request comments.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>include_source_branches</strong></td><td>Source branches defined using comma-separated GLOB or regex patterns for which Bito automatically reviews pull requests.<br><br><strong>Example:</strong> <code>"feature/*, release/*, main"</code>    </td></tr><tr><td><strong>include_target_branches</strong></td><td>Target branches defined using comma-separated GLOB or regex patterns for which Bito automatically reviews pull requests.<br><br><strong>Example:</strong> <code>"feature/*, release/*, main"</code></td></tr><tr><td><strong>exclude_files</strong></td><td>Comma-separated file path GLOB patterns to exclude from code reviews.<br><br><strong>Example:</strong> <code>"*.md, *.yaml, config/*"</code></td></tr><tr><td><strong>exclude_draft_pr</strong></td><td>Excludes draft pull requests from automatic reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>secret_scanner_feedback</strong></td><td>Enables or disables secret scanning feedback. Bito detects and reports secrets left in code changes.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>linters_feedback</strong></td><td>Run Linting tools during code reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>custom_guidelines</strong></td><td><p>Adds repo-defined coding guidelines, supporting both general and language-specific configurations.<br><br>Provide the <strong>name</strong> and <strong>path</strong> to review guidelines that you want bito to follow. These files must exist in your <strong>source branch</strong> at review time.<br><br>We accept up to 3 general guidelines and 1 language specific guideline per language.<br><br><strong>Example:</strong></p><pre class="language-yaml"><code class="lang-yaml">custom_guidelines:
  general:
    - name: "Global Checks"
      path: "./guidelines/global_checks.txt"
    - name: "Security Rules"
      path: "./guidelines/security.txt"
    - name: "Legacy Style Guide"
      path: "./guidelines/legacy.txt"
    - name: "Performance Checks"
      path: "./guidelines/perf.txt"
    - name: "Code Style"
      path: "./guidelines/style.txt"
  per_language:
    python:
      name: "Python Best Practices"
      path: "./guidelines/py.txt"
    javascript:
      name: "JS Style Guide"
      path: "./guidelines/js.txt"
    typescript:
      name: "TS Checks"
      path: "./guidelines/ts.txt"
    java:
      name: "Java Coding Standards"  
      Path: "./guidelines/java.txt"
</code></pre></td></tr><tr><td><strong>dependency_check.enabled</strong></td><td><p>Run Dependency Check analysis during code reviews.<br></p><p><strong>Valid values:</strong> <code>true</code> or <code>false</code></p></td></tr><tr><td><strong>repo_level_guidelines_enabled</strong></td><td>When enabled, Bito will automatically detect and use best-practice guidelines from agent configuration files such as <code>CLAUDE.md</code>, <code>AGENTS.md</code>, <code>GEMINI.md</code>, <code>.cursor/rules</code>, or <code>.windsurf/rules</code> during code reviews.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>sequence_diagram_enabled</strong></td><td>When enabled, Bito will generate interaction diagrams during code reviews to visualize the architecture and impacted components in the submitted changes.<br>Currently, it is supported for GitHub and GitLab.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>static_analysis.fb_infer.enabled</strong></td><td>Run Static Analysis tools during code reviews for providing better feedback.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code></td></tr><tr><td><strong>labels_excluded</strong></td><td>Comma-separated list of labels that, if present on a pull request or merge request, skip automatic review.<br><br>This is case-sensitive by default. For example, if we mention "Bug" in the repo-level <code>.bito.yaml</code> file and the tagged label is "bug", we won't match it. Users can use regex to make it case-insensitive, e.g., <code>(?i)^bug$</code> or <code>(?i)bug</code>.<br><br><strong>Example:</strong> <code>"wip, do-not-review, chore, size/*"</code></td></tr><tr><td><strong>post_as_request_changes</strong></td><td>Enable this option to get Bito feedback as "Request changes" review comments. Depending on your Git provider settings, you may need to resolve all comments before merging.<br><br>For GitHub, this will automatically enable auto-approve for resolved PRs.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code> </td></tr><tr><td><strong>functional_validation_enabled</strong></td><td>Enable this option to automatically validate pull requests against Jira ticket referenced in PR description, title, or branch name.<br><br>Jira Integration must be completed from <a href="https://alpha.bito.ai/">Bito dashboard</a> for this to work.<br><br><strong>Valid values:</strong> <code>true</code> or <code>false</code> </td></tr></tbody></table>

&#x20;

## Sample `.bito.yaml` file

```yaml
suggestion_mode: comprehensive       # 'essential' = only major issues, 'comprehensive' = everything
post_description: true                # Include summary description in PR comment
post_changelist: true                 # Include walkthrough of changes

include_source_branches: feature/**,bugfix/**
include_target_branches: main,develop
exclude_files: docs/**,README.md

exclude_draft_pr: true            # Don't review draft PRs
secret_scanner_feedback: true      # Enable secret scanning feedback
linters_feedback: true             # Enable linting / static analysis

custom_guidelines:
  general:
    - name: "Global Checks"
      path: "./guidelines/global_checks.txt"
    - name: "Security Rules"
      path: "./guidelines/security.txt"
    - name: "Legacy Style Guide"
      path: "./guidelines/legacy.txt"
    - name: "Performance Checks"
      path: "./guidelines/perf.txt"
    - name: "Code Style"
      path: "./guidelines/style.txt"
  per_language:
    python:
      name: "Python Best Practices"
      path: "./guidelines/py.txt"
    javascript:
      name: "JS Style Guide"
      path: "./guidelines/js.txt"
    typescript:
      name: "TS Checks"
      path: "./guidelines/ts.txt"
    java:
      name: "Java Coding Standards"  
      Path: "./guidelines/java.txt"  

```

## Download `.bito.yaml` file&#x20;

### From GitHub:

You can download a sample `.bito.yaml` configuration file directly from Bito’s official GitHub repository.&#x20;

This file includes all supported configuration fields with example values to help you get started quickly.&#x20;

1. Go to the [Bito GitHub repository](https://github.com/gitbito/repo-level-settings-file).&#x20;
2. Open the `.bito.yaml` file.&#x20;
3. Click the **Download raw file** button to download it.

### From Bito Cloud UI:

You can also download the sample `.bito.yaml` configuration file from the Bito Cloud UI.&#x20;

* Go to [Repositories](https://alpha.bito.ai/home/ai-agents/code-review-agent) dashboard.&#x20;
* Click the **Download settings file** button given in the Agent panel.&#x20;

{% hint style="info" %}
**Note:** Web browsers such as Google Chrome do not allow downloading files that begin with a dot `.`. As a result, when you download the sample settings file, it will be saved with a different name (for example, `agent.yaml` or `bito.yaml`). To use it correctly, rename the file to `.bito.yaml` before adding it to your repository.
{% endhint %}

{% hint style="info" %}
**Note:** By default, files that start with a dot `.` are hidden in most file explorers.

To view hidden files:&#x20;

* **Windows:** In File Explorer, go to the top menu bar, click **View**, then enable **Hidden items**.&#x20;
* **macOS:** Press `Command + Shift + .` in Finder.
* **Linux:** Run `ls -a` in your terminal.
  {% endhint %}

{% hint style="info" %}
**Note:** On macOS, the Finder app may not allow naming a file starting with a dot (e.g., `.bito.yaml`). In that case, open Terminal and use the following command to rename the file (replace `filename.yaml` with your actual file name):

`mv filename.yaml .bito.yaml`&#x20;
{% endhint %}

## Rules and limits

* The `.bito.yaml` file is read from the **source branch** of the pull request.&#x20;
* If a repo defines custom guidelines, agent-level guidelines are ignored for that repository.&#x20;
* If any property in the `.bito.yaml` file contains an invalid value, the entire configuration file will be rejected and default Agent Settings will be used instead.&#x20;
* If a property is missing in the `.bito.yaml` file, the corresponding value from the global Agent Settings will be used instead.
