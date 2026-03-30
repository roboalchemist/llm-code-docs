# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/help-docs.md

# Help Docs

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `help_docs` tool can answer a free-text question based on your git documentation folder.

## How to use the `help_docs` tool

**Manual usage**

Comment on the PR:

```
/help_docs "..."
```

**Automatic usage**

To run the tool automatically when a new issue is opened, add it to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[github_app]
pr_commands = [
    "/help_docs",
    ...
]

[pr_help_docs]
repo_url = ""
...
```

The tool assumes by default that the documentation is located in the root of the repository, at the `/docs` folder.

However, this can be customized by setting the `docs_path` configuration option:

```toml
[pr_help_docs]
repo_url = ""                 # The repository to use as context
docs_path = "docs"            # The documentation folder
repo_default_branch = "main"  # The branch to use in case repo_url overwritten
```

[Learn more about automatic usage of tools.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide)

### Run automatically when a new issue is opened <a href="#run-automatically-when-a-new-issue-is-opened" id="run-automatically-when-a-new-issue-is-opened"></a>

You can configure Qodo to run `help_docs` automatically on any newly created issue. This can be useful for providing immediate feedback to users who open issues with questions on open-source projects with extensive documentation.

1. [Create a GitHub action](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/setup-and-installation/github), such as:`.github/workflows/help_docs.yml`:
2. Add to your `YAML` file:

```yaml
name: Run Qodo on every opened issue, respond to user comments on an issue

#When the action is triggered
on:
  issues:
    types: [opened] #New issue

# Read env. variables
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  GITHUB_API_URL: ${{ github.api_url }}
  GIT_REPO_URL: ${{ github.event.repository.clone_url }}
  ISSUE_URL: ${{ github.event.issue.html_url || github.event.comment.html_url }}
  ISSUE_BODY: ${{ github.event.issue.body || github.event.comment.body }}
  OPENAI_KEY: ${{ secrets.OPENAI_KEY }}

# The actual set of actions
jobs:
  issue_agent:
    runs-on: ubuntu-latest
    if: ${{ github.event.sender.type != 'Bot' }} #Do not respond to bots

    # Set required permissions
    permissions:
      contents: read    # For reading repository contents
      issues: write     # For commenting on issues

    steps:
      - name: Run PR Agent on Issues
        if: ${{ env.ISSUE_URL != '' }}
        uses: docker://codiumai/pr-agent:latest
        with:
          entrypoint: /bin/bash #Replace invoking cli.py directly with a shell
          args: |
            -c "cd /app && \
            echo 'Running Issue Agent action step on ISSUE_URL=$ISSUE_URL' && \
            export config__git_provider='github' && \
            export github__user_token=$GITHUB_TOKEN && \            
            export github__base_url=$GITHUB_API_URL && \
            export openai__key=$OPENAI_KEY && \
            python -m pr_agent.cli --issue_url=$ISSUE_URL --pr_help_docs.repo_url="..." --pr_help_docs.docs_path="..." --pr_help_docs.openai_key=$OPENAI_KEY && \help_docs \"$ISSUE_BODY\""
```

3. Continue adding secrets and relevant configurations, such as `repo_url` and `docs_path.`&#x20;
4. Merge the changes to your main branch.
5. Done! When a new issue related to the repository's documentation is opened in your repository, you will see a comment from the  `github-actions` bot with an auto response.

***

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `help_docs` tool by setting configurations under the `pr_help_docs` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="257.36328125">Possible configurations</th><th width="222.34765625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>repo_url</code></td><td>The URL for the repository where the issue or PR reside</td><td>The repository's URL</td></tr><tr><td><code>repo_default_branch</code></td><td>none</td><td><p>The branch to use in case <code>repo_url</code> overwritten.</p><p>If repo_url was not overwritten this parameter has no effect.</p></td></tr><tr><td><code>docs_path</code></td><td><code>./docs</code></td><td>Relative path to the docs folder from the root of repository.</td></tr><tr><td><code>exclude_root_readme</code></td><td><code>false</code></td><td>Whether to exclude the root <code>README</code> file from Qodo's context.</td></tr><tr><td><code>supported_doc_exts</code></td><td><code>[".md", ".mdx", ".rst"]</code></td><td>Which file extensions should be included for <code>help_docs</code>'s action.</td></tr></tbody></table>

## Example usage <a href="#example-usage" id="example-usage"></a>

Asking a question about another repository:

<figure><img src="https://codium.ai/images/pr_agent/help_docs_comment_explicit_git.png" alt="" width="563"><figcaption></figcaption></figure>

Response:

<figure><img src="https://codium.ai/images/pr_agent/help_docs_response.png" alt="" width="563"><figcaption></figcaption></figure>
