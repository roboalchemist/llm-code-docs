# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/generic-ci.md

# Generic CI

You can integrate OX with any CI/CD system that supports running Docker images, even if it’s not listed among the officially supported integrations. This method, called Generic CI Integration, lets you trigger pipeline scans by running the OX Docker image and providing the required environment variables manually.

Use this method for CI/CD systems such as Bamboo, TeamCity, or any other platform that can execute Docker containers.

Use this integration when:

* Your CI/CD system isn’t one of the officially supported platforms.
* You need a temporary solution before a native integration is developed.
* You’re running OX scans locally or in custom build environments.

### How It Works

The Generic CI method runs the same Docker image used for standard pipeline integrations (`oxsecurity/ox-block-mode`), but does not rely on any built-in detection logic for a specific CI system.\
Instead, you provide a small set of environment variables that describe the repository, branch, and commit being scanned.

When the scan runs, OX treats it exactly like any other pipeline scan. The results appear in the platform under CI/CD Type: Generic, with the same blocking behavior, vulnerability display, and scan details as native integrations.

### Prerequisites

Before you begin:

1. Ensure your CI/CD system can run Docker images.
2. [Obtain an OX API key from your organization’s settings.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/broken-reference)
3. Make sure the repository you want to scan is already connected to OX.

### Required Environment Variables

| Variable           | Description                                                                      |
| ------------------ | -------------------------------------------------------------------------------- |
| `OX_GENERIC_CI`    | Must be set to `true` to indicate a generic CI execution.                        |
| `OX_API_KEY`       | Your OX API key for authentication.                                              |
| `OX_GIT_URL`       | The repository URL. Provided by the Git plugin or entered manually.              |
| `OX_SOURCE_BRANCH` | <p>The name of the branch being scanned, for example:<br><code>master</code></p> |
| `OX_COMMIT_SHA`    | The commit SHA, for example: `842cb296ed26a6fd2c59ebdf129d265649877448`          |

### Optional Environment Variables

| Variable            | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `OX_TARGET_BRANCH`  | The target branch in case of a pull request, for example: `feature-a` |
| `OX_JOB_ID`         | The identifier of the CI job. Displayed in OX under the scan details. |
| `OX_JOB_URL`        | A link to the job run in your CI system. Appears in the OX UI.        |
| `OX_JOB_USER`       | The user or system that triggered the scan.                           |
| `OX_JOB_USER_EMAIL` | The email of the user that triggered the scan.                        |

### Example

The following example shows how to execute a Generic CI scan from any CI/CD system or even locally:

```bash
docker run --rm \
  -e OX_GENERIC_CI=true \
  -e OX_API_KEY=<your_api_key> \
  -e OX_GIT_URL=https://github.com/example/repo.git \
  -e OX_SOURCE_BRANCH=main \
  -e OX_COMMIT_SHA=abc123def \
  oxsecurity/ox-pipeline-scan:latest
```

You can add optional parameters to include job metadata:

```bash
  -e OX_JOB_ID=123 \
  -e OX_JOB_URL=https://ci.example.com/job/123 \
  -e OX_JOB_USER_EMAIL=developer@example.com
```
