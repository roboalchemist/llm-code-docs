# Source: https://docs.gitguardian.com/internal-monitoring/prevent/detect-secrets-on-workstations.md

# Detect secrets on developer workstations

> Use ggshield with git hooks to detect secrets on developer workstations before they reach shared repositories.

## Overview

Secrets detection can be integrated very early on in the development process. GitGuardian empowers developers, with [ggshield (our command-line interface application)](../../ggshield-docs/home.mdx) to scan their commits for hardcoded secrets before pushing them.

The cost of fixing hardcoded secrets is much lower at this stage than once they have reached the central/shared repository, hence the importance of shifting security left and providing developers with early and frequent feedback.

ggshield can be integrated into git hooks to automatically scan code before committing staged changes (pre-commit hook) or before pushing code to the shared repository (pre-push hook).

<details>
    <summary>What are git hooks?</summary>
    Like many Version Control Systems, git has a way to fire off custom scripts when certain actions are triggered. There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operations such as committing and merging, while server-side hooks run on network operations such as receiving pushed commits. The custom scripts running in git hooks can be used for a variety of purposes like linting, testing, and running security scans on your code.
</details>

## Getting started with ggshield

1. Set up [ggshield on your workstation](../../ggshield-docs/getting-started.md)
2. Configure the git hooks with ggshield:
   - [pre-commit hook](../../ggshield-docs/integrations/git-hooks/pre-commit.md)
   - [pre-push hook](../../ggshield-docs/integrations/git-hooks/pre-push.md)

## Additional resources

- [How To Use ggshield To Avoid Hardcoded Secrets [cheat sheet included]](https://blog.gitguardian.com/how-to-use-ggshield-to-avoid-hardcoded-secrets-cheat-sheet-included/)
- [Using ggshield Throughout The Software Development Lifecycle - A Developer's View of GitGuardian [video]](https://www.youtube.com/watch?v=diuBTBjx7Qc)
