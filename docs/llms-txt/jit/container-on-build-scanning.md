# Source: https://docs.jit.io/docs/container-on-build-scanning.md

# Container On-Build Scanning

# Container Scanning in Jit

## Overview

Jit's container scanning feature helps detect vulnerabilities in container images during the CI/CD process. The scanning process focuses on two key stages:

* **On-Build Scanning**: The scan is performed during the CI/CD pipeline execution, before deployment.
* **Findings Analysis & PR Feedback**: Security issues are reported directly in pull requests and optionally added to the findings backlog.

Jit integrates with existing CI/CD workflows, allowing security checks to run as independent steps without interfering with core build processes.

> **Note:** Jit supports build-time container scanning only. Scanning images directly from a registry (e.g., Docker Hub, ECR) is not supported.

***

# Configuring Organization-Level Secrets for Jit CLI in CI/CD Workflows

This guide helps you securely configure and run the **Jit CLI** to scan container images within your CI/CD pipelines. Before you start, ensure you've set the required secrets at your organization level.

To configure this please navigate to Settings -> Users & Permissions -> API Tokens -> Generate Token -> Select Role - CLI Agent, set description and expiration and you will get the Client ID and Secret Key.

## Required Secrets

| Secret Name      | Description                 |
| ---------------- | --------------------------- |
| `JIT_CLIENT_ID`  | Your Jit client identifier. |
| `JIT_SECRET_KEY` | Your Jit secret key.        |

***

## Choose the Correct CLI Version

Ensure you select the Jit CLI binary matching your CI/CD runner's OS and CPU architecture:

| Runner OS     | CPU Architecture    | Dependency Install                              | Jit CLI Download URL   |
| ------------- | ------------------- | ----------------------------------------------- | ---------------------- |
| Debian/Ubuntu | `amd64` (Intel/AMD) | `apt-get update && apt-get install -y curl git` | `jit-cli-amd64-slim`   |
| Alpine Linux  | `amd64`             | `apk update && apk add curl git`                | `jit-cli-amd64-alpine` |

**Example URL pattern:**

```
https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-<slim|alpine>
```

## Platform Configuration Instructions

### GitHub Actions

Setting up in GitHub is straightforward:

1. **Access Organization Settings**
   * Navigate to your GitHub organization
   * Select **Settings** from the top navigation

2. **Configure Secrets**
   * In the left sidebar, find **Security** → **Secrets and variables** → **Actions**
   * Click **New organization secret**
   * Add each credential separately:
     * Name: `JIT_CLIENT_ID` with its corresponding value
     * Name: `JIT_SECRET_KEY` with its corresponding value
   * Select which repositories should have access
   * Save each secret

[Learn more about GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

***

### GitLab CI/CD

For GitLab environments:

1. **Access Group Settings**
   * Navigate to your GitLab group
   * Go to **Settings** → **CI/CD**

2. **Add Variables**
   * Expand the **Variables** section
   * Click **Add variable** for each credential:
     * Key: `JIT_CLIENT_ID` with its value
     * Key: `JIT_SECRET_KEY` with its value
   * Set type to **Variable** (or **File** if appropriate)
   * Uncheck **Protect variable** (to enable the variables when running on non-protected branch scanning)
   * Save each variable

[Learn more about GitLab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/)

***

### CircleCI

CircleCI uses Contexts for organization-level configuration:

1. **Access Organization Settings**
   * Go to your CircleCI organization
   * Select **Organization Settings**

2. **Create and Configure Context**
   * Select **Contexts** from the sidebar
   * Click **Create Context** (e.g., "Jit Security")
   * Add each environment variable:
     * Name: `JIT_CLIENT_ID` with its value
     * Name: `JIT_SECRET_KEY` with its value

3. **Use in Workflows**
   * Reference this context in your CircleCI configuration files

[Learn more about CircleCI Contexts](https://circleci.com/docs/2.0/contexts/)

***

### Jenkins

For Jenkins environments:

1. **Access Credentials**
   * Navigate to **Manage Jenkins** → **Manage Credentials**
   * Select the appropriate credentials domain

2. **Add Credentials**
   * Click **Add Credentials**
   * Choose **Secret text** type
   * Create separate entries for:
     * `JIT_CLIENT_ID` with its value
     * `JIT_SECRET_KEY` with its value
   * Provide descriptive IDs and descriptions
   * Save each credential

[Learn more about Jenkins Credentials](https://www.jenkins.io/doc/book/using/using-credentials/)

***

### Bitbucket Pipelines

For Bitbucket Pipelines:

1. **Access Workspace Settings**
   * Navigate to your Bitbucket workspace
   * Click on **Settings** in the left sidebar
   * Select **Workspace settings**

2. **Configure Workspace-Level Variables (Recommended)**
   * Select **Pipelines** → **Workspace variables**
   * Click **Add** for each credential:
     * Name: `JIT_CLIENT_ID` with its value
     * Name: `JIT_SECRET_KEY` with its value
   * Enable **Secured** option to encrypt sensitive values
   * Save each variable

3. **Alternatively, For Repository-Level Variables**
   * Navigate to your specific repository
   * Go to **Repository settings** → **Pipelines** → **Repository variables**
   * Add the same variables following the same process as above

[Learn more about Bitbucket Pipelines variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/)

## Workflow Examples Overview

Each CI/CD workflow below includes these steps:

1. **Install dependencies** (curl, git).
2. **Download and install Jit CLI**.
3. **Build container image**.
4. **Run Jit CLI scan**.
   > **Note:** The examples below use `[OPTIONS]` as a placeholder. See the [Command Options](#command-options)  section for available arguments.

## Running a Container Scan

### CD scan (production image build case)

```yaml GitHub
name: Jit Security Scan

on:
  push:
    branches:
      - main

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Dependencies & Jit CLI
        run: |
          sudo apt-get update && sudo apt-get install -y curl git
          curl -L https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim -o jit-cli
          chmod +x jit-cli

      - name: Build Container Image
        run: docker build -t <image>

      - name: Run Jit CLI Scan
        env:
          # Needed for communicating Jit BE
          JIT_CLIENT_ID: ${{ secrets.JIT_CLIENT_ID }}
          JIT_SECRET_KEY: ${{ secrets.JIT_SECRET_KEY }}
        run: |
          ./jit-cli container \
            --image <image> \
            --tracking-name <example-registry.io/image-name> \
            --fail-on-findings \
            --add-to-backlog
```
```yaml GitLab
container-scan:
  script:
    - echo "Build and scan container"
		- docker build -t <image>
    - sudo apt-get update && sudo apt-get install -y curl git
    - curl -O https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim
    - chmod +x jit-cli-amd64-slim
    - |
      JIT_CLIENT_ID=$JIT_CLIENT_ID \
      JIT_SECRET_KEY=$JIT_SECRET_KEY \
      ./jit-cli-amd64-slim container \
        --image <image> \
        --tracking-name <example-registry.io/image-name> \
        --fail-on-findings \
        --add-to-backlog
```
```yaml Bitbucket
image: atlassian/default-image:latest

pipelines:
  default:
    - step:
        name: Build and Scan
        services:
          - docker
        script:
          - apt-get update && apt-get install -y curl git
          - curl -L https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim -o jit-cli
          - chmod +x jit-cli
          - docker build -t <image>
          - >
            ./jit-cli container --image <image> --tracking-name <example-registry.io/image-name> [OPTIONS]
```
```yaml CircleCI
version: 2.1

jobs:
  security_scan:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - setup_remote_docker
      - run:
          name: Install Dependencies and Jit CLI
          command: |
            sudo apt-get update && sudo apt-get install -y curl git
            curl -L https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim -o jit-cli
            chmod +x jit-cli
      - run:
          name: Build Container Image
          command: docker build -t <image>
      - run:
          name: Run Jit CLI Scan
          command: ./jit-cli container --image <image> --tracking-name <example-registry.io/image-name> [OPTIONS]

workflows:
  security_scan_workflow:
    jobs:
      - security_scan:
          context:
            - Jit
            - AdditionalContextIfNeeded
```
```groovy Jenkins
pipeline {
    environment {
        JIT_CLIENT_ID = credentials('JIT_CLIENT_ID')
        JIT_CLIENT_SECRET = credentials('JIT_CLIENT_SECRET')
    }
    stages {
        stage('Build and Scan Image') {
            steps {
                sh '''
                apt-get update && apt-get install -y curl git
                curl -L https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim -o jit-cli
                chmod +x jit-cli
                docker build -t <image>
                ./jit-cli container --image <image> --tracking-name <example-registry.io/image-name> [OPTIONS]
                '''
            }
        }
    }
}
```

### PR/MR scan

```yaml GitHub
name: Jit Security Scan

on:
  pull_request:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Dependencies & Jit CLI
        run: |
          sudo apt-get update && sudo apt-get install -y curl git
          curl -L https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim -o jit-cli
          chmod +x jit-cli

      - name: Build Container Image
        run: docker build -t <image>

      - name: Run Jit CLI Scan
        env:
          # Data relevant for creating a PR reivew
          GITHUB_REPOSITORY_OWNER: ${{ github.repository_owner }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
          COMMIT_ID: ${{ github.event.pull_request.head.sha }}
          # Needed for communicating Jit BE
          JIT_CLIENT_ID: ${{ secrets.JIT_CLIENT_ID }}
          JIT_SECRET_KEY: ${{ secrets.JIT_SECRET_KEY }}
        run: |
          ./jit-cli container \
            --image <image> \
            --tracking-name <example-registry.io/image-name> \
            --organization "$GITHUB_REPOSITORY_OWNER" \
            --repo "${GITHUB_REPOSITORY#*/}" \
            --pull-request "${PR_NUMBER}" \
            --commit-id "${COMMIT_ID}" \
            --fail-on-findings \
            --new-findings-only
```
```yaml GitLab
container-scan:
  script:
    - echo "Build and scan container"
		- docker build -t <image>
    - sudo apt-get update && sudo apt-get install -y curl git
    - curl -O https://jit-cli.s3.us-east-1.amazonaws.com/jit-cli/latest/jit-cli-amd64-slim
    - chmod +x jit-cli-amd64-slim
    - |
      JIT_CLIENT_ID=$JIT_CLIENT_ID \
      JIT_SECRET_KEY=$JIT_SECRET_KEY \
      ./jit-cli-amd64-slim container \
        --image <image> \
        --tracking-name <example-registry.io/image-name> \
        --organization "$CI_PROJECT_NAMESPACE" \
        --repo "$CI_PROJECT_NAME" \
        --pull-request "$CI_MERGE_REQUEST_IID" \
        --commit-id "$CI_COMMIT_SHA" \
        --fail-on-findings \
        --new-findings-only
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      when: on_success
```

### Important Notes

* Adjust the CLI URL to match your runner's OS and CPU architecture according to the provided table.
* Ensure your container image build step clearly tags the image (your-image-name).
* When building the image with Podman/Kaniko or other non-"docker" building system, you should save the image as "image.tar" and pass the tar file to the `--image` option.

## Command Options

### Core Options (All Workflows)

[block:parameters]
{
  "data": {
    "h-0": "Option",
    "h-1": "Default",
    "h-2": "Description",
    "0-0": "`--image`",
    "0-1": "Required",
    "0-2": "The container image to scan. This should be the same image you built with `docker build -t <image>`. Can be a local image or a full registry path (e.g., `myapp:latest` or `registry.example.com/myapp:1.0`).",
    "1-0": "`--tracking-name <production-name>`",
    "1-1": "Required",
    "1-2": "The canonical name of the image without tags, used for tracking findings across different scans.  \nShould match the image name in your registry (e.g., `registry.example.com/myapp`).  \nThis ensures findings are properly tracked when scanning the same image from different sources.",
    "2-0": "`--new-findings-only`",
    "2-1": "`false`",
    "2-2": "Only alert on new findings.",
    "3-0": "`--severity <LOW,MEDIUM,HIGH,CRITICAL>`",
    "3-1": "`HIGH,CRITICAL`",
    "3-2": "Severity levels to report.",
    "4-0": "`--fail-on-findings`",
    "4-1": "`false`",
    "4-2": "Fail the workflow if vulnerabilities are found."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

### PR/MR Workflow Options

| Option           | Default | Description                                                                   |
| :--------------- | :------ | :---------------------------------------------------------------------------- |
| `--organization` | None    | SCM organization name for associating findings with the correct organization. |
| `--repo`         | None    | Repository identifier name.                                                   |
| `--pull-request` | None    | PR/MR number identifier.                                                      |
| `--commit-id`    | None    | Commit ID for associating findings with the correct commit.                   |

### CD Workflow Options (Production Builds)

| Option             | Default | Description                                                                    |
| ------------------ | ------- | ------------------------------------------------------------------------------ |
| `--add-to-backlog` | `false` | Add findings to Jit's backlog. **Only use in CD workflows, not PR workflows**. |

## Managing Findings & PR Comments

* **Findings are displayed as PR comments** with severity-based filtering.
* **Threshold Configuration**: Users can define what severity level is required to surface findings.
* **Findings View**: Once a PR is merged, unresolved findings are added to the findings backlog for future review.
* **Blocking PRs**: The user can enforce merge blocking based on findings severity.

## Troubleshooting

### Common Issues

**1. CLI Authentication Failure**\
Ensure that `JIT_CLIENT_ID` and `JIT_SECRET_KEY` are correctly set in your environment.

**2. No Findings Are Reported**\
Check if the `--new-findings-only` flag is enabled. If set, only new vulnerabilities are surfaced.

**3. Workflow Fails on Scan Execution**\
If `--fail-on-findings` is enabled, ensure that no critical vulnerabilities are present, or adjust the severity threshold.