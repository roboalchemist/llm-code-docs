# Source: https://docs.gitguardian.com/ggshield-docs/integrations/git-hooks/pre-push.md

# Pre-push

> Explains how to set up a ggshield pre-push git hook to scan commits for secrets before they are pushed to a remote repository.

## Prelude

A pre-push hook is a client-side git hook that runs right before a reference is pushed to a remote (`git push`). Please refer to [our learning center](https://www.gitguardian.com/glossary/git-hooks) for more information.

GitGuardian pre-push hook is performed through our CLI application: [`ggshield`](../../getting-started.md). `ggshield` is a wrapper around the GitGuardian API for secrets detection that requires an API key to work.

## Preview

![pre-push preview](/img/internal-monitoring/integrate-sources/vcs-integrations/git-hooks/git-hooks-pre-push-output.png)

:::info
Customize the remediation message and add your own to offer developers precise guidance for resolving their code issues and continuing their work.

**Read more here - GitGuardian CLI custom remediation message**
:::

## Installation

### The pre-commit framework

In order to use **GitGuardian CLI** with the [pre-commit](https://pre-commit.com/) framework, you need to perform the following steps.

1. Make sure you have the pre-commit framework installed:

```shell
$ pip install pre-commit
```

2. Create a `.pre-commit-config.yaml` file in your repository's root path:

```yaml
repos:
  - repo: https://github.com/gitguardian/ggshield
    rev: v1.48.0
    hooks:
      - id: ggshield-push
        language_version: python3
        stages: [pre-push]
```

3. Then install the hook with the command:

```shell
$ pre-commit install --hook-type pre-push
pre-commit installed at .git/hooks/pre-push
```

Now you're good to go!

> To avoid long delays, by default the pre-push hook will not scan pushes with more than 50 commits.
> This setting can be configured using the `max-commits-for-hook` key in ggshield configuration file.

### Global pre-push hook

To install pre-push globally (for all current and future repos):

1. Sign in to your GitGuardian workspace and create a Personal Access Token from your [personal settings](https://dashboard.gitguardian.com/api/personal-access-tokens).
2. Add this Personal Access Token (API key) to the `GITGUARDIAN_API_KEY` environment variable of your development environment.
3. Execute the following command:

```shell
$ ggshield install --mode global -t pre-push
```

It will:

- verify that if a global hook folder is defined in the global git configuration.
- create the `~/.git/hooks` folder (if needed).
- create a `pre-push` file which will be executed before every commit.
- give executable access to this file.

### Local pre-push hook

You can install the hook locally on desired repositories:

1. Sign in to your GitGuardian workspace and create a Personal Access Token from your [personal settings](https://dashboard.gitguardian.com/api/personal-access-tokens).
2. Add this Personal Access Token (API key) to the `GITGUARDIAN_API_KEY` environment variable in your repository.
3. Go in the repository and execute the following command:

```shell
$ ggshield install --mode local -t pre-push
```

Notes:

- If a pre-push executable file already exists, it will not be overridden. You can force override with the `--force` option:

```shell
$ ggshield install --mode local  -t pre-push --force
```
