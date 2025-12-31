# Source: https://biomejs.dev/recipes/git-hooks/

# Git Hooks 

Git allows executing scripts during the run of a git command using [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks). For example, you can format and lint the staged files before committing or pushing. Several tools exist to simplify the management of Git Hooks. In the following sections we introduce some of them and how they can be used with Biome.

## Lefthook

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Lefthook"]](#lefthook)

[Lefthook](https://github.com/evilmartians/lefthook) provides a fast, cross-platform, and dependency-free hook manager. It can be [installed via NPM](https://github.com/evilmartians/lefthook#install).

Add a file named `lefthook.yml` at the root of your Git repository. Some examples of *Lefthook* configurations:

-   Check formatting and lint before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="yaml"><code>1pre-commit:2  commands:3    check:4      glob: &quot;*.&quot;5      run: npx @biomejs/biome check --no-errors-on-unmatched --files-ignore-unknown=true --colors=off </code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">lefthook.yml</span></figcaption>
    </figure>
    :::

-   Format, lint, and apply safe code fixes before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="yaml"><code>1pre-commit:2  commands:3    check:4      glob: &quot;*.&quot;5      run: npx @biomejs/biome check --write --no-errors-on-unmatched --files-ignore-unknown=true --colors=off 6      stage_fixed: true</code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">lefthook.yml</span></figcaption>
    </figure>
    :::

    `stage_fixed: true` adds again the staged files.

-   Check formatting and lint before pushing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="yaml"><code>1pre-push:2  commands:3    check:4      glob: &quot;*.&quot;5      run: npx @biomejs/biome check --no-errors-on-unmatched --files-ignore-unknown=true --colors=off </code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">lefthook.yml</span></figcaption>
    </figure>
    :::

Note that you don't need to use both `glob` and `--files-ignore-unknown=true`. Using only `--files-ignore-unknown=true` allows handling files supported in the present and in the future by Biome. If you wish more control over which files are handled, you should use `glob`.

`--no-errors-on-unmatched` silents possible errors in case *no files are processed*.

Once configured, run `lefthook install` to set up the hooks.

## Husky

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Husky"]](#husky)

[Husky](https://github.com/typicode/husky) is a widely-used hook manager in the JavaScript ecosystem. Husky doesn't hide unstaged changes and is not able to provide the list of staged files. This is why it is often used in tandem with another tool such as *lint-staged* or *git-format-staged*.

If your project contains a `package.json`, you can automatically set up *husky* hooks upon package installation using `scripts.prepare`:

<figure class="frame has-title not-content">
<pre data-language="json"><code>15}</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">package.json</span></figcaption>
</figure>

### lint-staged

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "lint-staged"]](#lint-staged)

[lint-staged](https://github.com/lint-staged/lint-staged) is one of the most used tools in the JavaScript ecosystem.

Add the following husky configuration:

<figure class="frame has-title not-content">
<pre data-language="shell"><code>1lint-staged</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">.husky/pre-commit</span></figcaption>
</figure>

The configuration of lint-staged is directly embedded in `package.json`. Here's some example of commands that you could find useful when running the Git hooks:

<figure class="frame has-title not-content">
<pre data-language="jsonc"><code>1&quot;: [5      &quot;biome check --files-ignore-unknown=true&quot;, // Check formatting and lint6      &quot;biome check --write --no-errors-on-unmatched&quot;, // Format, sort imports, lint, and apply safe fixes7      &quot;biome check --write --organize-imports-enabled=false --no-errors-on-unmatched&quot;, // format and apply safe fixes8      &quot;biome check --write --unsafe --no-errors-on-unmatched&quot;, // Format, sort imports, lints, apply safe/unsafe fixes9      &quot;biome format --write --no-errors-on-unmatched&quot;, // Format10      &quot;biome lint --write --no-errors-on-unmatched&quot;, // Lint and apply safe fixes11    ],12    // Alternatively you can pass every files and ignore unknown extensions13    &quot;*&quot;: [14      &quot;biome check --no-errors-on-unmatched --files-ignore-unknown=true&quot;, // Check formatting and lint15    ]16  }17}</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">package.json</span></figcaption>
</figure>

Remember to use the CLI option `--no-errors-on-unmatched` in your command, to silent possible errors in case *no files are processed*.

### git-format-staged

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "git-format-staged"]](#git-format-staged)

In contrast to other tools such as *lefthook*, *pre-commit*, and *lint-staged*, [git-format-staged](https://github.com/hallettj/git-format-staged) doesn't use `git stash` internally. This avoids manual intervention when conflicts arise between unstaged changes and updated staged changes. See the [comparison of *git-format-staged* with other tools](https://github.com/hallettj/git-format-staged#comparisons-to-similar-utilities).

Some examples of configuration:

-   Check formatting and lint before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="shell"><code>1git-format-staged --formatter &#39;biome check --files-ignore-unknown=true --no-errors-on-unmatched \&quot;\&quot;&#39; .</code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">.husky/pre-commit</span></figcaption>
    </figure>
    :::

-   Format, lint, and apply safe code fixes before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="shell"><code>1git-format-staged --formatter &#39;biome check --write --files-ignore-unknown=true --no-errors-on-unmatched \&quot;\&quot;&#39; .</code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">.husky/pre-commit</span></figcaption>
    </figure>
    :::

## pre-commit

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "pre-commit"]](#pre-commit)

[pre-commit](https://pre-commit.com/) provides a multi-language hook manager. Biome provides four [pre-commit](https://pre-commit.com/) hooks via the [biomejs/pre-commit](https://github.com/biomejs/pre-commit) repository.

  hook `id`        description
  ---------------------------- -----------------------------------------------------------------------------
  `biome-ci`       Check formatting, check if imports are organized, and lints
  `biome-check`    Format, organize imports, lint, and apply safe fixes to the committed files
  `biome-format`   Format the committed files
  `biome-lint`     Lint and apply safe fixes to the committed files

In the following example, we assume that you [installed pre-commit](https://pre-commit.com/#install) and run `pre-commit install` in your repository. if you want to use the `biome-check` hook, add the following pre-commit configuration to the root of your project in a file named `.pre-commit-config.yaml`:

<figure class="frame has-title not-content">
<pre data-language="yaml"><code>1repos:2-   repo: https://github.com/biomejs/pre-commit3    rev: &quot;v2.0.6&quot;  # Use the sha / tag you want to point at4    hooks:5    -   id: biome-check6        additional_dependencies: [&quot;@biomejs/biome@2.1.1&quot;]</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">.pre-commit-config.yaml</span></figcaption>
</figure>

This will run `biome check --write` when you run `git commit`.

Note that you must specify which version of Biome to use thanks to the `additional_dependencies` option. [pre-commit](https://pre-commit.com/) separately installs tools and need to know which one to install.

If Biome is already installed as a `npm` package in your local repository, then it can be a burden to update both `package.json` and `.pre-commit-config.yaml` when you update Biome. Instead of using the provided Biome hooks, you can specify your own [local hook](https://pre-commit.com/#repository-local-hooks).

For example, if you use `npm`, you can write the following hook in `.pre-commit-config.yaml`:

<figure class="frame has-title not-content">
<pre data-language="yaml"><code>1repos:2  - repo: local3    hooks:4      - id: local-biome-check5        name: biome check6        entry: npx @biomejs/biome check --write --files-ignore-unknown=true --no-errors-on-unmatched7        language: system8        types: [text]9        files: &quot;\\.(jsx?|tsx?|c(js|ts)|m(js|ts)|d\\.(ts|cts|mts)|jsonc?)$&quot;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">.pre-commit-config.yaml</span></figcaption>
</figure>

The pre-commit option `files` is optional, because Biome is able to ignore unknown files (using the option `--files-ignore-unknown=true`).

## Shell script

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Shell script"]](#shell-script)

You can also use a custom shell script. Note that you can encounter cross-platform incompatibilities. We recommend the use of a dedicated tool as the one presented in the previous sections.

Some examples of shells scripts:

-   Check formatting and lint before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="shell"><code>1#!/bin/sh2set -eu3
    4npx @biomejs/biome check --staged --files-ignore-unknown=true --no-errors-on-unmatched</code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">.git/hooks/pre-commit</span></figcaption>
    </figure>
    :::

-   Format, lint, and apply safe code fixes before committing

    ::: expressive-code
    <figure class="frame has-title not-content">
    <pre data-language="shell"><code>1#!/bin/sh2set -eu3
    4if git status --short | grep --quiet &#39;^MM&#39;; then5  printf &#39;%s\n&#39; &quot;ERROR: Some staged files have unstaged changes&quot; &gt;&amp;26  exit 1;7fi8
    9npx @biomejs/biome check --write --staged --files-ignore-unknown=true --no-errors-on-unmatched10
    11git update-index --again</code></pre>
    <div class="copy">
    <div>

    </div>
    </div>
    <figcaption><span class="title">.git/hooks/pre-commit</span></figcaption>
    </figure>
    :::

    Note that we make the hook fail if staged files have unstaged changes.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/recipes/git-hooks.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Continuous Integration] ]](/recipes/continuous-integration) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Renovate] ]](/recipes/renovate)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.