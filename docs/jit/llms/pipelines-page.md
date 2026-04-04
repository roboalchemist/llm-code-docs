# Source: https://docs.jit.io/docs/pipelines-page.md

# Pipelines

## Overview

Jit security pipelines are a live representation of Jit continuous security (CS) implementation that provides the following benefits:

1. Confirming Jit security controls are running properly.
2. Viewing ongoing and past security scans.
3. Reviewing individual security scans, their results and execution logs.

## Pipelines Architecture

Pipelines include the security workflows and constituent jobs (typically [security tools](https://docs.jit.io/docs/security-tools)) that Jit executes. These pipelines have a fixed lifecycle that progresses through a *Queued* and then *Running* state, before terminating in either *Success* or *Failed*. Failure of a single job is sufficient to fail the entire pipeline. Pipelines are associated with a scanned resource (either a repo, service, cloud infrastructure account, etc.) and a trigger (such as a pull request creation).

![](https://files.readme.io/e416ed9-Screenshot_2022-11-29_11.50.04_AM.png)

> 📘 Note
>
> For code-centric security, pipelines trigger when a change is pushed to a project. Pipelines can also be scheduled, as is the case for non-code-centric security.

## Anatomy of a Pipeline

Pipeline information is organized into the following columns—

| Resource                                                                                                                                                                                                                                                                                 | Runner                                                                                  | Workflows                                                    | Pipeline Status                                                                                                                                                                                     |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Each pipeline is defined by its associated resource— such as a GitHub repo or AWS account. This column also shows when how long ago the pipeline was created, how long it took to run, and who the initiator was. The initiator can either be a human developer or an automated process. | The infrastructure used to run the pipeline— such as GitHub Actions or Jit's own cloud. | The specific security workflows implemented by the pipeline. | This column shows the present state of the pipeline. Additional information (for instance, a note on *why* the pipeline failed, which may include specific security findings) may also be included. |

![](https://files.readme.io/9d99a91-individualpipeline.png)

## Pipeline Details

The pipeline details page contains additional information that varies depending on the triggering event type. This includes, but is not limited to, the *scope* of the pipeline and any uncovered security findings. The *scope* of the pipeline defines the breadth of the security scan— for example, if only new code was scanned, rather than the entire code base.

To view the pipeline detail page, click on the pipeline.

### Viewing finding details

*Findings* is the final section of the pipeline details view. Each individual finding is presented as a vertical list item that includes the finding name, date and time of detection, severity, and status. Select the finding to open the *Finding Details* panel, which displays the following additional information—

| Field                       | Definition                                                                                    |
| :-------------------------- | :-------------------------------------------------------------------------------------------- |
| First Detected              | The date and time when this finding was detected.                                             |
| Vulnerability Type          | Stack layer associated with the finding.                                                      |
| Security Tool               | The tool (specified at the security requirement-level) that Jit used to uncover this finding. |
| Details                     | This contains additional information describing the finding.                                  |
| Learn more about this issue | This may contain an external link to security tool documentation.                             |
| File Name                   | The file associated with this security vulnerability.                                         |

## Testing Newly-Activated Security Requirements

If you selected the **Test me** option when you activated a security requirement from the [Security Plans](https://docs.jit.io/docs/my-plan-tab) page, you were redirected to the Pipelines page to view the test pipeline, which demonstrates that your newly-activated security requirement is functional.

If you would like to verify this security requirement's detection accuracy, select the test pipeline and select **Introduce a \[issue type]** to create a test pull request that contains a detectable issue.