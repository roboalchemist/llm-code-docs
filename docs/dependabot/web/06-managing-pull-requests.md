# Managing Dependabot Pull Requests

Source: https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates

## Overview

Dependabot pull requests are managed similarly to standard pull requests but include specialized features. The documentation emphasizes that users with **write access** can manage these PRs.

## Identifying Dependabot Pull Requests

Dependabot PRs are easily recognizable by two characteristics:

- The author is the `dependabot` or `dependabot[bot]` account
- They carry the `dependencies` label by default

## Rebase and Merge Strategy

### Automatic Rebasing

By default, Dependabot automatically rebases pull requests to resolve any conflicts. However, after 30 days without merging, Dependabot ceases automatic rebasing.

The `rebase-strategy` configuration option allows manual conflict handling if preferred:

```yaml
updates:
  - package-ecosystem: "npm"
    rebase-strategy: "disabled"  # Disable auto-rebase
```

### Force Push

To permit Dependabot to force-push over additional commits you've made, include one of these strings in your commit messages (case-insensitive):

- `[dependabot skip]`
- `[skip dependabot]`
- `[dependabot-skip]`
- `[skip-dependabot]`

Example commit message:

```
Add new tests [dependabot skip]
```

## Comment Commands

Dependabot responds to specific commands in PR comments. You can use these commands to manage updates:

### @dependabot merge

Automatically merges the pull request after CI passes.

```
@dependabot merge
```

### @dependabot rebase

Rebases the pull request to resolve conflicts.

```
@dependabot rebase
```

### @dependabot close

Closes the pull request and prevents Dependabot from recreating it for the same dependency update.

```
@dependabot close
```

### @dependabot ignore [dependency/version]

Prevents Dependabot from creating updates for this dependency/version combination. The dependency must be specified as a package name.

Examples:

```
@dependabot ignore express
@dependabot ignore lodash 4.17.0
```

You can still enable updates later by editing the `dependabot.yml` file.

### @dependabot squash and merge

Squashes commits before merging the PR.

```
@dependabot squash and merge
```

## Pull Request Configuration

### Commit Message Customization

Customize how commits are formatted:

```yaml
commit-message:
  prefix: "chore(deps):"
  include: "scope"
```

Options for `include`:
- `scope` - Add dependency name as scope
- `references` - Include issue/PR references
- `all` - Include both scope and references

### Branch Naming

Customize the branch naming convention:

```yaml
pull-request-branch-name:
  separator: "/"  # "dependabot/npm/lodash-4.17.20"
```

### Labels

Add custom labels to PRs:

```yaml
labels:
  - "dependencies"
  - "automated"
```

### Assignees

Automatically assign reviewers:

```yaml
assignees:
  - "alice"
  - "bob"
```

### Milestone

Associate with a project milestone:

```yaml
milestone: 1
```

## Repository Inactivity

Critical note: "If you don't interact with Dependabot pull requests for a repository during a 90-day time period, Dependabot considers your repository as inactive, and will automatically pause Dependabot updates."

### Reactivating a Paused Repository

To reactivate Dependabot after 90 days of inactivity:

1. Merge or close some existing Dependabot pull requests
2. Re-enable Dependabot in Settings > Security > Advanced Security > Dependabot
3. Dependabot will resume creating pull requests

## Best Practices

### 1. Use Labels for Organization

Organize PRs with consistent labels:

```yaml
labels:
  - "dependencies"
  - "npm"
```

### 2. Assign to Team

Automatically route PRs to appropriate team members:

```yaml
assignees:
  - "frontend-team"
```

### 3. Limit Concurrent PRs

Control volume with `open-pull-requests-limit`:

```yaml
open-pull-requests-limit: 5
```

### 4. Group Updates

Reduce notification noise by grouping related updates:

```yaml
groups:
  production-dependencies:
    dependency-type: "production"
```

### 5. Monitor Regularly

Check for Dependabot PRs at least weekly to prevent auto-deactivation.

### 6. Merge Security Updates First

Prioritize security update PRs over version updates.

### 7. Enable Auto-Merge for Safe Updates

Use GitHub's auto-merge feature for minor updates after CI passes:

1. Enable auto-merge on the PR
2. Select "Squash and merge"
3. PR merges automatically when CI passes

## Handling Conflicts

If a Dependabot PR has conflicts:

1. Comment with `@dependabot rebase` to attempt auto-rebase
2. If that fails, manually fix conflicts in the PR
3. Add `[dependabot skip]` to your commit message if adding commits
4. Request Dependabot to rebase again

## Security Updates

Security update PRs follow the same management rules but should be prioritized:

- Review and merge promptly
- Don't ignore/dismiss unless truly not applicable
- Automate merging when possible

## Notifications

You can filter notifications to focus on Dependabot PRs:

1. Go to Settings > Notifications
2. Create a custom filter for `is:pull-request author:dependabot`
3. Set up label-based filters in your workflow
