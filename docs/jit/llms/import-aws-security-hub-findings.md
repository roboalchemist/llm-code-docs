# Source: https://docs.jit.io/docs/import-aws-security-hub-findings.md

# AWS Security Hub Integration

## Description

AWS `Security Hub` is a Cloud Security Posture Management (CSPM) service that performs security best practice checks, aggregates alerts, and enables automated remediation.

Jit imports the results from AWS Security Hub into the platform, enabling you to monitor and respond to threats in a proactive manner across multiple AWS accounts.

Jit specifically imports high and critical findings from AWS services, enabling you to focus on the most important security issues.

## Prerequisites

* [AWS integration](https://docs.jit.io/docs/integrating-with-aws) is required to activate this security control.
* `Security Hub` must be enabled on your AWS account.
* For instructions on excluding test accounts, see [Plan Resources Exclusion](https://docs.jit.io/docs/plan-resources-exclusion).

## Troubleshooting

**In the event that pipelines fail to display AWS findings:**

* Ensure that `Security Hub` is enabled on your AWS account.
* Make sure you exclude accounts without `Security Hub`. Follow the instructions at [Plan Resources Exclusion](https://docs.jit.io/docs/plan-resources-exclusion).
* Review the execution log within the pipeline. The execution log provides detailed information about each step in the pipeline, including any error messages or exceptions that occurred.\
  To view the execution log of a pipeline -\
  Go to the [Pipelines page](https://docs.jit.io/docs/pipelines-page), select the **pipeline**and select **View log** under the pipeline workflow.