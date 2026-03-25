# Source: https://help.aikido.dev/aikido-autofix/configure/autofix-pr-configuration.md

# AutoFix PR Configuration

## Pull Request Configuration <a href="#pull-request-configuration" id="pull-request-configuration"></a>

You can configure the AutoFix pull requests to your own needs with the ["PR Configuration" settings](https://app.aikido.dev/issues/fix/settings). It's possible to change the following fields:

* **Title Prefix:** Customize the title to match your internal processes
* **Labels:** Add specific labels to the PR for easier sorting and tracking
* **Branch name:** Customize the prefix of the branch Autofix creates
* **Commit Message:** Customize the prefix of the commit message in the PR
* **Summary:** Optionally include an additional message for each PR. For example add custom instructions for engineers or additional context.
* **Create Draft PR:** create draft PRs instead of ready for review.
* **Auto-Merge PR:** Aikido relies on built-in Github, Gitlab and Azure DevOps auto-merge features for this, learn more [here](https://help.aikido.dev/aikido-autofix/auto-merge-autofix-pull-requests).
* **Create Task for PR:** important for compliance reasons. This will automatically create a new task in your connected task tracker, linking to the created PR.

### Linking Pull Requests with Tasks

There are two ways to link your pull requests to tasks: <br>

1. **Automatic Task Creation**:&#x20;

Enable "Create task for PR" in your AutoFix configuration. This automatically generates a new task for every PR created by AutoFix.<br>

2. **Existing Task Linking**:

Task identifiers for fixed issues are automatically included in the branch name. If your workspace is integrated with a task tracker, the PR will automatically link to the corresponding task.

To ensure the link is created, include the task reference `$TASK_REF` placeholder in your PR title prefix and/or commit message. See [Pull Request Configuration](#pull-request-configuration)

<div data-full-width="false"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FjXhssVlJPAIBB6eDeqJG%2Fimage.png?alt=media&#x26;token=3376c407-5fbe-43d1-b5b4-5d41848aa18f" alt="" width="563"><figcaption></figcaption></figure></div>

## Repository-specific configuration

The settings in the Aikido UI are global settings, these are applied to all repos within the Aikido workspace.

**Branch prefixes** can be configured per repo by adding a `.aikido` file at the root level of the repo with the following contents:

```
autofix:
    branch_prefix: "prefix-for-branch-"
```

AutoFix will use the `branch_prefix` value when creating a branch for that specific repository.

The branch prefix defined in the `.aikido` file takes priority over the branch prefix configured in the UI.

#### Example

If your `.aikido` file contains:

```
autofix:
    branch_prefix: "security-fix-"
```

AutoFix will create branches like `security-fix-update-dependency-xyz`.

<br>
