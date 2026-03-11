# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/jenkins.md

# Jenkins

OX Security integrates with Jenkins to scan Docker-based builds for security issues.

To scan pull requests before they are merged, you must configure Jenkins to provide source and target branch information in the pipeline.

### Prerequisites

* **Docker support:** Jenkins must be able to run Docker containers.
* **Git information:** Jenkins must use the Git plugin or be manually configured to provide commit and branch details.

### Required environment variables

| Variable      | Description                                                                                                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `OX_API_KEY`  | [The OX Security integration key.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/broken-reference) |
| `OX_HOST_URL` | The OX platform URL (only if using an on-premise installation).                                                                                                                                                          |
| `GIT_URL`     | The repository URL. Provided by the Git plugin or entered manually.                                                                                                                                                      |
| `GIT_COMMIT`  | The commit SHA. Provided by the Git plugin or replaced with `OX_COMMIT_SHA`.                                                                                                                                             |
| `GIT_BRANCH`  | The branch name. Provided by the Git plugin or replaced with `OX_SOURCE_BRANCH`.                                                                                                                                         |

### Optional environment variables

| Variable               | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `OX_TARGET_BRANCH`     | The target branch name. Recommended when running scans before merging pull requests. |
| `OX_OVERRIDE_BLOCKING` | Set to `true` to override stage failure caused by blocking issues.                   |
| `OX_TIMEOUT`           | Maximum duration of the scan, in minutes.                                            |
| `OX_FAIL_ON_TIMEOUT`   | Set to `true` to fail the stage if a scan times out.                                 |
| `OX_FAIL_ON_ERROR`     | Set to `true` to fail the stage if a system or network error occurs.                 |

### Advanced environment variables

| Variable                    | Description                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `OX_DISABLE_SSL_VALIDATION` | Set to `true` to disable SSL certificate validation for self-signed certificates in on-premise environments. |

### Integration example (`Jenkinsfile`)

```groovy
pipeline {
    agent any

    stages {
        stage('OX Security Scan') {
            agent {
                docker {
                    alwaysPull true
                    image 'oxsecurity/ox-block-mode:latest'
                }
            }

            environment {
                OX_API_KEY = credentials('ox-api-key')
                // OX_COMMIT_SHA = 6f3f6a038baa67b40f12d0692e75c40ad49a986e
                // OX_SOURCE_BRANCH = development
                // OX_TARGET_BRANCH = main
                // OX_OVERRIDE_BLOCKING = false
                // OX_TIMEOUT = 20
                // OX_FAIL_ON_TIMEOUT = false
                // OX_FAIL_ON_ERROR = false
            }

            steps {
                script {
                    sh 'ox-block-mode'
                }
            }
        }
    }
}
```
