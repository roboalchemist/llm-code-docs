# Source: https://biomejs.dev/guides/integrate-in-vcs/

# Integrate Biome with your VCS 

The VCS (Version Control System) integration is meant to take advantage of **additional** features that only a VCS can provide. At the moment, Biome only supports Git. The integration is **opt-in**. You have to enable `vcs.enabled` and set `vcs.clientKind` in the Biome configuration file:

<figure class="frame has-title not-content">
<pre data-language="json"><code>16}</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">biome.json</span></figcaption>
</figure>

This configuration doesn't do **anything per se**. You need to opt-in the features you want.

### Use the ignore file

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Use the ignore file"]](#use-the-ignore-file)

Enable `vcs.useIgnoreFile`, to allow Biome to ignore all the files and directories listed in the project's VCS ignore file as well as a `.ignore` file.

<figure class="frame has-title not-content">
<pre data-language="json"><code>17}</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">biome.json</span></figcaption>
</figure>

### Process only changed files

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Process only changed files"]](#process-only-changed-files)

This is a feature that is available only via CLI, and allows processing **only** the files that have **changed** from one revision to another.

First, you have to update your configuration file and tell Biome what's the default branch via the `vcs.defaultBranch` field:

<figure class="frame has-title not-content">
<pre data-language="json"><code>18}</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">biome.json</span></figcaption>
</figure>

Then, add the `--changed` option to your command, to process only those files that your VCS acknowledged as "changed". Biome, with the help of the VCS, will determine the changed file from the branch `main` and your current revision:

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --changed</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0ic3RhcmxpZ2h0LWFzaWRlX19pY29uIj48cGF0aCBkPSJNMTIgMTZDMTEuODAyMiAxNiAxMS42MDg5IDE2LjA1ODcgMTEuNDQ0NCAxNi4xNjg2QzExLjI4IDE2LjI3ODQgMTEuMTUxOCAxNi40MzQ2IDExLjA3NjEgMTYuNjE3M0MxMS4wMDA0IDE2LjgwMDEgMTAuOTgwNiAxNy4wMDExIDExLjAxOTIgMTcuMTk1MUMxMS4wNTc4IDE3LjM4OTEgMTEuMTUzIDE3LjU2NzMgMTEuMjkyOSAxNy43MDcxQzExLjQzMjcgMTcuODQ3IDExLjYxMDkgMTcuOTQyMiAxMS44MDQ5IDE3Ljk4MDhDMTEuOTk4OSAxOC4wMTk0IDEyLjIgMTcuOTk5NiAxMi4zODI3IDE3LjkyMzlDMTIuNTY1NCAxNy44NDgyIDEyLjcyMTYgMTcuNzIgMTIuODMxNSAxNy41NTU2QzEyLjk0MTMgMTcuMzkxMSAxMyAxNy4xOTc4IDEzIDE3QzEzIDE2LjczNDggMTIuODk0NiAxNi40ODA1IDEyLjcwNzEgMTYuMjkyOUMxMi41MTk2IDE2LjEwNTQgMTIuMjY1MiAxNiAxMiAxNlpNMjIuNjcgMTcuNDdMMTQuNjIgMy40NzAwM0MxNC4zNTk4IDMuMDAzNTQgMTMuOTc5OCAyLjYxNDk4IDEzLjUxOTIgMi4zNDQ1QzEzLjA1ODYgMi4wNzQwMSAxMi41MzQxIDEuOTMxNCAxMiAxLjkzMTRDMTEuNDY1OSAxLjkzMTQgMTAuOTQxNCAyLjA3NDAxIDEwLjQ4MDggMi4zNDQ1QzEwLjAyMDIgMi42MTQ5OCA5LjY0MDE5IDMuMDAzNTQgOS4zOCAzLjQ3MDAzTDEuMzggMTcuNDdDMS4xMTA3OSAxNy45MjQgMC45NjYxNDEgMTguNDQxIDAuOTYwNjQzIDE4Ljk2ODhDMC45NTUxNDQgMTkuNDk2NiAxLjA4OSAyMC4wMTY2IDEuMzQ4NjggMjAuNDc2MUMxLjYwODM3IDIwLjkzNTYgMS45ODQ3IDIxLjMxODUgMi40Mzk2OCAyMS41ODYxQzIuODk0NjYgMjEuODUzNiAzLjQxMjE4IDIxLjk5NjQgMy45NCAyMkgyMC4wNkMyMC41OTIxIDIyLjAwNTMgMjEuMTE1OSAyMS44Njg5IDIxLjU3NzkgMjEuNjA0OUMyMi4wMzk5IDIxLjM0MSAyMi40MjM0IDIwLjk1ODkgMjIuNjg5IDIwLjQ5NzhDMjIuOTU0NiAyMC4wMzY4IDIzLjA5MjggMTkuNTEzNCAyMy4wODk1IDE4Ljk4MTRDMjMuMDg2MiAxOC40NDkzIDIyLjk0MTQgMTcuOTI3NyAyMi42NyAxNy40N1pNMjAuOTQgMTkuNDdDMjAuODUyMyAxOS42MjYgMjAuNzI0NSAxOS43NTU2IDIwLjU2OTcgMTkuODQ1M0MyMC40MTQ5IDE5LjkzNSAyMC4yMzg5IDE5Ljk4MTUgMjAuMDYgMTkuOThIMy45NEMzLjc2MTExIDE5Ljk4MTUgMy41ODUxIDE5LjkzNSAzLjQzMDMyIDE5Ljg0NTNDMy4yNzU1MyAxOS43NTU2IDMuMTQ3NjUgMTkuNjI2IDMuMDYgMTkuNDdDMi45NzIyMyAxOS4zMTggMi45MjYwMiAxOS4xNDU2IDIuOTI2MDIgMTguOTdDMi45MjYwMiAxOC43OTQ1IDIuOTcyMjMgMTguNjIyIDMuMDYgMTguNDdMMTEuMDYgNC40NzAwM0MxMS4xNDM5IDQuMzA2MjMgMTEuMjcxNCA0LjE2ODc2IDExLjQyODQgNC4wNzI3N0MxMS41ODU1IDMuOTc2NzggMTEuNzY2IDMuOTI1OTkgMTEuOTUgMy45MjU5OUMxMi4xMzQgMy45MjU5OSAxMi4zMTQ1IDMuOTc2NzggMTIuNDcxNiA0LjA3Mjc3QzEyLjYyODYgNC4xNjg3NiAxMi43NTYxIDQuMzA2MjMgMTIuODQgNC40NzAwM0wyMC44OSAxOC40N0MyMC45ODkyIDE4LjYxOTkgMjEuMDQ2MiAxOC43OTM3IDIxLjA1NSAxOC45NzMyQzIxLjA2MzggMTkuMTUyNyAyMS4wMjQxIDE5LjMzMTIgMjAuOTQgMTkuNDlWMTkuNDdaTTEyIDguMDAwMDNDMTEuNzM0OCA4LjAwMDAzIDExLjQ4MDQgOC4xMDUzOCAxMS4yOTI5IDguMjkyOTJDMTEuMTA1NCA4LjQ4MDQ2IDExIDguNzM0ODEgMTEgOS4wMDAwM1YxM0MxMSAxMy4yNjUyIDExLjEwNTQgMTMuNTE5NiAxMS4yOTI5IDEzLjcwNzFDMTEuNDgwNCAxMy44OTQ3IDExLjczNDggMTQgMTIgMTRDMTIuMjY1MiAxNCAxMi41MTk2IDEzLjg5NDcgMTIuNzA3MSAxMy43MDcxQzEyLjg5NDYgMTMuNTE5NiAxMyAxMy4yNjUyIDEzIDEzVjkuMDAwMDNDMTMgOC43MzQ4MSAxMi44OTQ2IDguNDgwNDYgMTIuNzA3MSA4LjI5MjkyQzEyLjUxOTYgOC4xMDUzOCAxMi4yNjUyIDguMDAwMDMgMTIgOC4wMDAwM1oiPjwvcGF0aD48L3N2Zz4=)Caution

Biome doesn't check what's changed, this means that even adding spaces or newlines to a file, will mark this file as "changed"

Alternatively, you can use the option `--since` to specify an arbitrary branch. This option **takes precedence** over the option `vcs.defaultBranch`. For example, you might want to check your changes against the `next` branch:

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --changed --since=next</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

### Process only staged files

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Process only staged files"]](#process-only-staged-files)

Before committing your changes, you may want to check formatting and linting for files added to the index (also known as staged files) without running Biome on the entire project. To limit Biome to only processing files slated for committing, pass the `--staged` option to the command:

<figure class="frame is-terminal not-content">
<pre data-language="shell"><code>1biome check --staged</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title"></span><span class="sr-only">Terminal window</span></figcaption>
</figure>

The `--staged` option is not available in the `ci` command, as you are usually not expected to commit changes during CI.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/guides/integrate-in-vcs.mdx)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Integrate Biome in an editor extension] ]](/guides/editors/create-an-extension) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Migrate from ESLint & Prettier] ]](/guides/migrate-eslint-prettier)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.