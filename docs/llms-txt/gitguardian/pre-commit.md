# Source: https://docs.gitguardian.com/ggshield-docs/integrations/git-hooks/pre-commit.md

# Pre-commit

> Set up ggshield as a pre-commit git hook to detect secrets before they are committed.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/IAQjwlQtRB0?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

## Prelude

A pre-commit hook is a client-side git hook that runs right before the commit is created. Please refer to [our learning center](https://www.gitguardian.com/glossary/git-hooks) for more information.

GitGuardian pre-commit hook is performed through our CLI application: [`ggshield`](../../getting-started.md). `ggshield` is a wrapper around GitGuardian API for secrets detection that requires an API key to work.

## Preview

![pre-commit preview](/img/internal-monitoring/integrate-sources/vcs-integrations/git-hooks/git-hooks-pre-commit-output.png)

:::info
Customize the remediation message and add your own to offer developers precise guidance for resolving their code issues and continuing their work.

**Read more here - GitGuardian CLI custom remediation message**
:::

## Installation

### The pre-commit framework

In order to use `ggshield` with the [pre-commit](https://pre-commit.com/) framework, you need to perform the following steps.

1. Make sure you have pre-commit installed:

```shell
$ pip install pre-commit
```

2. Create a `.pre-commit-config.yaml` file in your repository's root path with the following content:

```yaml
repos:
  - repo: https://github.com/gitguardian/ggshield
    rev: v1.48.0
    hooks:
      - id: ggshield
        language_version: python3
        stages: [pre-commit]
```

3. Then install the hook with the command:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

Now you're good to go!

> Note: If you want to skip all the pre-commit checks, you can add the `-n` parameter as follows:

```shell
$ git commit -m "commit message" -n
```

> Alternatively if you only want to skip ggshield, you can use SKIP=ggshield before the command:

```shell
$ SKIP=ggshield git commit -m "commit message"
```

### Global pre-commit hook

To install pre-commit globally (for all current and future repos):

1. Sign in to your GitGuardian workspace and create a Personal Access Token from your [personal settings](https://dashboard.gitguardian.com/api/personal-access-tokens).
2. Add this Personal Access Token (API key) to the `GITGUARDIAN_API_KEY` environment variable of your development environment.
3. Execute the following command:

```shell
$ ggshield install --mode global
```

It will:

- verify if a global hook folder is defined in the global git configuration.
- create the `~/.git/hooks` folder (if needed).
- create a `pre-commit` file which will be executed before every commit.
- give executable access to this file.

### Local pre-commit hook

You can install the hook locally on desired repositories:

1. Sign in to your GitGuardian workspace and create a Personal Access Token from your [personal settings](https://dashboard.gitguardian.com/api/personal-access-tokens).
2. Add this Personal Access Token (API key) to the `GITGUARDIAN_API_KEY` environment variable in your repository.
3. Go in the repository and execute the following command:

```shell
$ ggshield install --mode local
```

Notes:

- If a pre-commit executable file already exists, it will not be overridden. You can force overriding with the `--force` option:

```shell
$ ggshield install --mode local --force
```

- If you already have a pre-commit executable file and you want to use ggshield,
  all you need to do is to add this line in the file:

```shell
$ ggshield secret scan pre-commit
```

- If you want to try pre-commit scanning through the docker image:

```shell
$ docker run -e GITGUARDIAN_API_KEY -v $(pwd):/data --rm gitguardian/ggshield ggshield secret scan pre-commit
```
