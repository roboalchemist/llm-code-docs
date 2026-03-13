# Source: https://docs.gitguardian.com/internal-monitoring/prevent/block-secrets-from-entering-vcs.md

# Block secrets from the VCS

> Use ggshield with pre-receive git hooks to block secrets from reaching shared repositories on self-hosted GitHub or GitLab instances.

## Overview

Secrets can be blocked from reaching shared repositories with the help of ggshield, the GitGuardian CLI, and through the setup of pre-receive git hooks.

This is only applicable for organizations running their own GitHub, GitHub Enterprise Server, or GitLab instances. If this is your case, the VCS site administrator can create and remove pre-receive hooks for your entire organization and its associated repositories.

<details>
    <summary>What is a pre-receive hook?</summary>
    Pre-receive hooks run tests on code pushed to a repository to ensure contributions meet repository or organization policy.
    If the commit contents pass the tests, the push will be accepted into the repository.
    If the commit contents contain any secrets, the push will not be accepted.
    If your push isnât accepted, you will see an error message corresponding to the failed pre- receive hook.
</details>

### Advantages

Pre-receive hooks are configured once for the VCS instance and are the most effective tool to prevent secrets from reaching your codebase.

### Integrate ggshield with a pre-receive hook

1. [Create a service account](../../api-docs/service-accounts.md) for the GitGuardian API
2. Set up a [pre-receive hook with ggshield](../../ggshield-docs/integrations/git-hooks/pre-receive.md)
