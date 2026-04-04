# Source: https://docs.socket.dev/docs/socket-for-azure-devops.md

# Socket for Azure DevOps (ADO Classic)

This guide walks you through integrating [Socket CLI](https://pypi.org/project/socketsecurity/) into a **Classic Azure DevOps pipeline** using the UI-based editor.

## Prerequisites

* Azure DevOps project using Classic pipelines
* Python and `pip` available on the build agent
* Access to modify pipeline definitions
* Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))
* Create Variable Group Key for ADO ([Directions](https://docs.socket.dev/docs/create-variable-group-key-for-azure-devops))

## Setup Steps

1. Go to **Pipelines > New Pipeline > Use the Classic Editor**.
2. Select your repo and default settings.
3. In the pipeline editor, add the following tasks:

### Task 1: Install Socket CLI

* **Task type**: Command Line
* **Display name**: `Install Socket CLI`
* **Script**:
  ```bash
  pip install socketsecurity --upgrade
  ```

### Task 2: Run Socket CLI

* **Task type**: Command Line
* **Display name**: `Run Socket CLI`
* **Script**:

  ```bash
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
    $DEFAULT_BRANCH \
    $DISABLE_BLOCKING
  ```

## Behavior

* **Pull Requests**: Blocking mode is **enabled by default**.
* **Commits to main/master**: Blocking mode is **disabled** using `--disable-blocking`.

## Notes

* The Socket CLI will analyze dependencies based on commit and branch metadata.
* Make sure the agent has permissions and environment to run Python and shell scripts.

For CLI reference, see: [Socketsecurity on PyPI](https://pypi.org/project/socketsecurity/)