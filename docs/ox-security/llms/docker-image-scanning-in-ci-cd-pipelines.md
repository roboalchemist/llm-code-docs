# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/docker-image-scanning-in-ci-cd-pipelines.md

# Docker Image Scanning in CI/CD Pipelines

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

OX Security supports scanning container images immediately after they are built in your CI/CD pipeline. This allows you to detect vulnerabilities at the earliest possible stage, before the image is pushed to a registry or used in any runtime environment.

The scan is performed as a dedicated pipeline step, using an OX-provided scanner image and configuration.

The integration runs within CI/CD pipelines for repositories that are monitored in OX.

First, you need to configure the container scanning and then you can view the results, as follows:

1. [Pipeline Configuration (Outside OX)](#pipeline-configuration)
2. [Workflow Configuration (Inside OX)](#pipeline-workflow-configuration)
3. [Viewing Scan Results](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/understanding-pipeline-scan-results)

## Pipeline Configuration

To scan Docker images during pipeline execution, you must add a new step to your CI/CD configuration. OX provides a Docker image published on Docker Hub that runs the scanner.

### Prerequisites

* [OX CI/CD Integration key](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/creating-ci-cd-integration-key)
* Docker image name and tag to be scanned
* CI/CD environment that supports injecting these values
* CI/CD environment that supports mounting the host’s Docker socket into the container, OR providing remote access to the Docker daemon using TCP

| **Environment Variable** | **Description**                             | **Examples**                                                                                                                   |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `DOCKER_HOST`            | Specifies the address of the Docker daemon. | <p><code>unix:///var/run/docker.sock</code> (default for local)<br><code>tcp\://192.168.1.100:2375</code> (for remote TCP)</p> |

## System Requirements

| Requirement Type                | CPU       | Memory     |
| ------------------------------- | --------- | ---------- |
| Minimum System Requirements     | 1 core    | 512 MB RAM |
| Recommended System Requirements | 1–2 cores | 1 GB RAM   |

### Example: GitLab CI

```yaml
image_scan:
  stage: scan
  image: oxsecurity/ox-image-scanner:latest
  variables:
    OX_API_KEY: <your_api_key>
    OX_ARTIFACT_NAME: <image_name>
    OX_ARTIFACT_TAG:  <image_tag>
    DOCKER_HOST: <docker_host_url or path_to_socket, defaults to unix:///var/run/docker.sock>
  script:
    - scan-image
```

### Example: Azure

```
 - job: OX
        displayName: OX Security Image Scan
        steps:
          - script: |
              docker run \
                --rm \
                -e OX_API_KEY=<your_api_key> \
                -e OX_ARTIFACT_NAME=<image_name> \
                -e OX_ARTIFACT_TAG=<image_tag> \
                -e DOCKER_HOST=unix:///var/run/docker.sock \
                --env-file <(env | grep 'SYSTEM_\|BUILD_') \
                -v /var/run/docker.sock:/var/run/docker.sock \
                oxsecurity/ox-image-scanner:latest
```

## Pipeline Workflow Configuration

After configuring the pipeline, you must define how OX handles the scan results. This is done in the [Pipeline Workflows area of the OX platform.](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows)

**To configure the workflow:**

1. Go to **Pipeline Workflows** in the OX UI.
2. Drag the **Container Security** policy from the left panel into your active workflow.
3. Define actions based on issue severity or type (e.g., alert, block the pipeline).

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07c8e906b2b66ecbc7e4504616e241eb45f916a5%2FPipeline_Workflow%20(1).png?alt=media" alt="" width="317"><figcaption></figcaption></figure>

1. Save the updated workflow.

> **Note:** During early access, the **Container Security** policy is not part of the default workflow and must be added manually.
