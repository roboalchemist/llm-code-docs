# Source: https://fly.io/docs/elixir/advanced-guides/github-actions-elixir-ci-cd/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# GitHub Actions for Elixir CI/CD 

You want the benefits of modern CI/CD for your Elixir projects? You're in the right place!

## [](#continuous-integration-ci)[Continuous Integration (CI)] 

Continuous integration is a software development practice where developers frequently merge code changes into a central repository. Automated builds and tests are run to assert the new code's correctness before integrating the changes into the main development branch. The goal is to find and correct bugs faster, improve software quality and enable software releases to happen faster.

To get started with GitHub Actions in your project, let's create a "test" workflow. To do this, create this path and file in the root of your project:

`.github/workflows/elixir.yaml`

Let's look at a sample file. Comments are included to explain and document what we're doing and why.

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
name: Elixir CI

# Define workflow that runs when changes are pushed to the
# `main` branch or pushed to a PR branch that targets the `main`
# branch. Change the branch name if your project uses a
# different name for the main branch like "master" or "production".
on:
  push:
    branches: [ "main" ]  # adapt branch for project
  pull_request:
    branches: [ "main" ]  # adapt branch for project

# Sets the ENV `MIX_ENV` to `test` for running tests
env:
  MIX_ENV: test

permissions:
  contents: read

jobs:
  test:
    # Set up a Postgres DB service. By default, Phoenix applications
    # use Postgres. This creates a database for running tests.
    # Additional services can be defined here if required.
    services:
      db:
        image: postgres:12
        ports: ['5432:5432']
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    runs-on: ubuntu-latest
    name: Test on OTP $} / Elixir $}
    strategy:
      # Specify the OTP and Elixir versions to use when building
      # and running the workflow steps.
      matrix:
        otp: ['25.0.4']       # Define the OTP version [required]
        elixir: ['1.14.1']    # Define the elixir version [required]
    steps:
    # Step: Setup Elixir + Erlang image as the base.
    - name: Set up Elixir
      uses: erlef/setup-beam@v1
      with:
        otp-version: $}
        elixir-version: $}

    # Step: Check out the code.
    - name: Checkout code
      uses: actions/checkout@v3

    # Step: Define how to cache deps. Restores existing cache if present.
    - name: Cache deps
      id: cache-deps
      uses: actions/cache@v3
      env:
        cache-name: cache-elixir-deps
      with:
        path: deps
        key: $}-mix-$}-$}
        restore-keys: |
          $}-mix-$}-

    # Step: Define how to cache the `_build` directory. After the first run,
    # this speeds up tests runs a lot. This includes not re-compiling our
    # project's downloaded deps every run.
    - name: Cache compiled build
      id: cache-build
      uses: actions/cache@v3
      env:
        cache-name: cache-compiled-build
      with:
        path: _build
        key: $}-mix-$}-$}
        restore-keys: |
          $}-mix-$}-
          $}-mix-

    # Step: Conditionally bust the cache when job is re-run.
    # Sometimes, we may have issues with incremental builds that are fixed by
    # doing a full recompile. In order to not waste dev time on such trivial
    # issues (while also reaping the time savings of incremental builds for
    # *most* day-to-day development), force a full recompile only on builds
    # that are retried.
    - name: Clean to rule out incremental build as a source of flakiness
      if: github.run_attempt != '1'
      run: |
        mix deps.clean --all
        mix clean
      shell: sh

    # Step: Download project dependencies. If unchanged, uses
    # the cached version.
    - name: Install dependencies
      run: mix deps.get

    # Step: Compile the project treating any warnings as errors.
    # Customize this step if a different behavior is desired.
    - name: Compiles without warnings
      run: mix compile --warnings-as-errors

    # Step: Check that the checked in code has already been formatted.
    # This step fails if something was found unformatted.
    # Customize this step as desired.
    - name: Check Formatting
      run: mix format --check-formatted

    # Step: Execute the tests.
    - name: Run tests
      run: mix test
```

### [](#when-the-workflow-runs)[When the Workflow Runs...] 

When code is pushed to the `main` branch, this workflow is run. This happens either from directly pushing to the `main` branch or after merging a PR into the `main` branch.

This workflow is also configured to run checks on PR branches that target the `main` branch. This is where it is most helpful. We can work on a fix or a new feature in a branch and as we work and push our code up, it automatically runs the full gamut of checks we want.

When all steps in the workflow succeed, the workflow "passes" and the automated checks say it can be merged. When a step fails, the workflow halts at that point and "fails", potentially blocking a merge.

### [](#customizing-the-workflow-steps)[Customizing the Workflow Steps] 

This workflow is a starting point for a team. Every project is unique and every team values different things. Is this missing something your team wants? Check out some additional steps that can be added to your workflow.

-   Add a step to run [Credo](https://github.com/rrrene/credo) checks.
-   Add a step to run [Sobelow](https://github.com/nccgroup/sobelow) for security focused static analysis.
-   Add a step to run [dialyxir](https://github.com/jeremyjh/dialyxir). This runs [Dialyzer](https://www.erlang.org/doc/man/dialyzer.html) static code analysis on the project. Refer to the project for tips on caching the PLT.
-   Customize the `mix test` command to include [code coverage](https://hexdocs.pm/mix/main/Mix.Tasks.Test.html#module-coverage) checks.
-   Add Node setup and caching if `npm` assets are part of the project's test suite.
-   Add a step to run [mix_audit](https://github.com/mirego/mix_audit). This provides a `mix deps.audit` task to scan a project's Mix dependencies for known Elixir security vulnerabilities
-   Add a step to run [`mix hex.audit`](https://hexdocs.pm/hex/Mix.Tasks.Hex.Audit.html). This shows all Hex dependencies that have been marked as retired, which the package maintainers no longer recommended using.
-   Add a set to run [`mix deps.unlock --check-unused`](https://hexdocs.pm/mix/Mix.Tasks.Deps.Unlock.html). This checks that the `mix.lock` file has no unused dependencies. This is useful if you want to reject contributions with extra dependencies.

### [](#benefits-of-caching)[Benefits of Caching] 

It's worth spending time tweaking your caches. Why? A lot of effort has been put into speeding up Elixir build times. If we don't cache the build artifacts, then we don't reap any of those benefits!

Of course, faster build times means you spend less money running your CI workflow. But that's not the reason to do it! Better caches mean the checks are performed faster and that means faster feedback. Faster feedback means that, as a team, you save time and can move faster. No waiting 20 minutes for the checks to complete so a PR can be merged. (Yes, I have felt that pain!)

This starting template builds in two caching steps. If `node_modules` factor into your project's tests, then caching there makes a lot of sense too.

Just keep in mind that the reason we cache is to reduce drag on the speed of our team.

If our caches ever cause a problem, and sometimes they can, it's good to know how to clear them. In our project, go to Actions \> (Sidebar) Management \> Caches. This is the list of caches saved for the project. We can use our naming format to identify which cache file is for what.

### [](#retrying-failed-builds)[Retrying Failed Builds] 

We cache aggressively because we want the productivity benefits that incremental compiles bring the team. However, on occasion, incremental builds can fail. The quick fix is to perform a full recompile.

The following step from our CI pipeline does this for us.

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` highlight
    # Step: Conditionally bust the cache when job is re-run.
    # Sometimes, we may have issues with incremental builds that are fixed by
    # doing a full recompile. In order to not waste dev time on such trivial
    # issues (while also reaping the time savings of incremental builds for
    # *most* day-to-day development), force a full recompile only on builds
    # that are retried.
    - name: Clean to rule out incremental build as a source of flakiness
      if: github.run_attempt != '1'
      run: |
        mix deps.clean --all
        mix clean
      shell: sh
```

If this is not the first run attempt, meaning we are re-running the job, then it busts our cache by cleaning out the `deps` and `_build` directories.

This compromise works well. Most of the time, we get fast checks and, where there is a problem, we only need to retry the failed task to force a clean build.

### [](#additional-resources)[Additional Resources] 

-   [Documentation: Caching dependencies to speed up workflows](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
    -   [Managing Caches](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#managing-caches)
-   [erlef/setup-beam](https://github.com/erlef/setup-beam) - Set up your BEAM-based GitHub Actions workflow (Erlang, Elixir, and more)
    -   See project for settings and ENV options
    -   [Elixir setup action - Archived](https://github.com/actions/setup-elixir#phoenix-example) - Includes helpful examples like setting up the Postgres service database.
-   [Felt blog: Taking Hashrocket's "Ultimate Elixir CI" to the Next Level](https://felt.com/blog/hashrocket-ultimate-elixir-to-the-next-level)
    -   [felt/ultimate-elixir-ci](https://github.com/felt/ultimate-elixir-ci) - Good examples on CI setup with explanations.
    -   [Source for cleaning out incremental builds on retry](https://github.com/felt/ultimate-elixir-ci/blob/main/.github/actions/elixir-setup/action.yml#L97)

## [](#continuous-deployment-cd)[Continuous Deployment (CD)] 

Continuous deployment is a software development practice that automatically builds and releases the project into production when new changes pass automated checks and are merged to the main branch. Using this practice, it is common to release new versions of the applications multiple times a day, ideally, without users even being aware of the process.

### [](#auto-deploying-our-elixir-applications)[Auto-Deploying our Elixir Applications] 

We can easily auto-deploy our Elixir applications on Fly.io. There is nothing specific to Elixir about this process, so please refer to this guide for the details.

[Continuous Deployment with Fly.io and GitHub Actions](/docs/app-guides/continuous-deployment-with-github-actions/)

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Felixir%2Fadvanced-guides%2Fgithub-actions-elixir-ci-cd.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+GitHub+Actions+for+Elixir+CI%2FCD%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Felixir%2Fadvanced-guides%2Fgithub-actions-elixir-ci-cd%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Felixir%2Fadvanced-guides%2Fgithub-actions-elixir-ci-cd.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22GitHub+Actions+for+Elixir+CI%2FCD%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/elixir/advanced-guides/github-actions-elixir-ci-cd.html.md)