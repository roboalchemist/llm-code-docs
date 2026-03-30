# Source: https://docs.jit.io/docs/gitlab-runners-are-disabled.md

# GitLab Runners are disabled

# Enabling GitLab Runners

Jit uses GitLab Runners to run its scans, both daily/weekly and PR scans. There are cases where, for organizatinal decisions, GitLab Runners are disabled. In this situation, Jit will not be able to run and GitLab Runners will need to be enabled. This guide explains how to enable GitLab Runners for your projects to automate CI/CD tasks.

***

## Prerequisites

1. A working GitLab account.
2. Access to the GitLab project where the runner will be registered.
3. Administrative rights to configure runners.

***

## Steps to Enable GitLab Runners

### 1. **Install GitLab Runner**

* Install GitLab Runner on your desired machine using the [official installation guide](https://docs.gitlab.com/runner/install/).
* Use one of the following commands for your platform:
  * **Debian/Ubuntu**:
    ```bash
    curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64
    chmod +x /usr/local/bin/gitlab-runner
    ```
  * **Windows**:\
    Download and install the binary from the [GitLab Runner Releases page](https://gitlab.com/gitlab-org/gitlab-runner/-/releases).

***

### 2. **Register the GitLab Runner**

* Run the registration command:
  ```bash
  gitlab-runner register
  ```
* Follow the prompts:
  * **GitLab URL**: Enter your GitLab instance URL (e.g., `https://gitlab.com`).
  * **Registration Token**: Obtain this token from `Settings > CI/CD > Runners` in your GitLab project.
  * **Description**: Provide a name for your runner (e.g., `My GitLab Runner`).
  * **Tags**: Add optional tags to categorize the runner.
  * **Executor**: Select an executor type (e.g., `shell`, `docker`, etc.).

***

### 3. **Configure the Runner**

* Edit the `config.toml` file located in the GitLab Runner installation directory to adjust settings such as cache, concurrency, or executor-specific options:
  ```toml
  [[runners]]
  name = "My GitLab Runner"
  url = "https://gitlab.com/"
  token = "YOUR_TOKEN"
  executor = "docker"
  [runners.docker]
    image = "alpine:latest"
  ```

***

### 4. **Verify the Runner**

* Go to `Settings > CI/CD > Runners` in your GitLab project.
* Ensure the new runner appears in the **Available Runners** section.

***

## Testing the Runner

1. Add a `.gitlab-ci.yml` file to your repository root with the following content:

   ```yaml
   stages:
     - test

   test-job:
     stage: test
     script:
       - echo "The runner is working!"
   ```