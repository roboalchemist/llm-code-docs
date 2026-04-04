# Source: https://docs.socket.dev/docs/socket-for-azure-devops-yaml.md

# Socket for Azure DevOps (Yaml)

This guide shows how to use [Socket CLI](https://pypi.org/project/socketsecurity/) in a **YAML-defined pipeline** that runs on every commit across all branches.

## Prerequisites

* Azure Repos with YAML pipeline support
* Python and `pip` installed on the build agent
* A variable group named `socket_security` with a variable `api_key`
* Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))
* Create Variable Group Key for ADO ([Directions](https://docs.socket.dev/docs/create-variable-group-key-for-azure-devops))

## Full Example

Save the following as `azure-pipelines.yml` in your repository:

```yaml
trigger:
  branches:
    include:
      - '*'

pool: your_agent_pool

variables:
  - group: socket_security
  - name: SOCKET_SECURITY_API_KEY
    value: $[variables.api_key]

steps:
- script: |
    pip install socketsecurity --upgrade
  displayName: Install Socket CLI

- script: |
    PR="${SYSTEM_PULLREQUEST_PULLREQUESTNUMBER:-0}"
    DISABLE_BLOCKING=""

    if [[ "$BUILD_SOURCEBRANCHNAME" == "main" || "$BUILD_SOURCEBRANCHNAME" == "master" ]]; then
      DEFAULT_BRANCH="--default-branch"
      DISABLE_BLOCKING="--disable-blocking"
    fi

    socketcli \
      --target-path "$BUILD_REPOSITORY_LOCALPATH" \
      --branch "$BUILD_SOURCEBRANCHNAME" \
      --pr-number "$PR" \
      --commit-sha "$BUILD_SOURCEVERSION" \
      --commit-message "$BUILD_SOURCEVERSIONMESSAGE" \
      --enable-diff \
      $DEFAULT_BRANCH \
      $DISABLE_BLOCKING
  displayName: Run Socket CLI
```

## Behavior

* The pipeline runs on **every commit** to **any branch**.
* Blocking is **enabled** for PRs.
* Blocking is **disabled** for main/master using `--disable-blocking`.

## Optional

To also run the pipeline when a pull request is opened/updated:

```yaml
pr:
  branches:
    include:
      - '*'
```

## Summary

* The CLI is automatically installed and invoked with full context (branch, commit, PR).
* Blocking logic is handled based on branch type.
* Credentials are securely pulled from a variable group.

For CLI reference, see: [Socketsecurity on PyPI](https://pypi.org/project/socketsecurity/)