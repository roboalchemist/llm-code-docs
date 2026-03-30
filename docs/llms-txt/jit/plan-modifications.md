# Source: https://docs.jit.io/docs/plan-modifications.md

# Plan Workflow Modifications

## Overview

> ⚠️ Note
>
> Security Plan configuration is managed directly in the Jit platform.\
> As-code configuration is no longer the source of truth and is considered redundant.\
> If you previously used as-code configuration, it has been automatically synced to Jit.\
> Please contact us if anything is unclear or behaves differently than expected.

Jit's Open DevSecOps platform offers plan workflow customizations, empowering security champions to tailor security plans according to their needs.

This feature enables you to address custom risks and align with your tech stack and development processes.

Modifications are currently supported with [Semgrep Python SAST scanning](https://docs.jit.io/docs/scan-code-for-vulnerabilities) and [KICS IaC Misconfigurations scaning](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations).

> 🚧 Contact Jit for assistance before using this feature.
>
> Contact us over a shared Slack channel, our platform chat, or [here](https://www.jit.io/contact).

## Instructions

At the end of your `jit-plan.yml` file in your Jit centralized repo, add an override section. The examples below show how to exclude running specific tests (checks) across your entire organization:

```yaml Semgrep example
override:
  workflows:
    sast:
      jobs:
        static-code-analysis-python-semgrep:
          steps:
          - name: Run semgrep python
            uses: registry.jit.io/control-semgrep-alpine:latest
            with:
              args: --json --config=/semgrep-python-config.yml --metrics=off --severity=ERROR --exclude-rule python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query ${WORK_DIR:-.}
```
```Text KICS example
override:
  workflows:
    iac-misconfiguration-detection:
      jobs:
        iac-misconfig-detection-terraform:
          steps:
          - name: Run KICS (terraform)
            uses: registry.jit.io/control-kics-alpine:latest
            with:
              args: scan -t Terraform -p ${WORK_DIR:-.} -o /code/jit-report/results.json -f json --config /terraform-config.yaml --disable-secrets --exclude-queries 6726dcc0-5ff5-459d-b473-a780bef7665c,4495bc5d-4d1e-4a26-ae92-152d18195648,42bb6b7f-6d54-4428-b707-666f669d94fb,90501b1b-cded-4cc1-9e8b-206b85cda317,3a1e94df-6847-4c0e-a3b6-6c6af4e128ef,c5b31ab9-0f26-4a49-b8aa-4cc064392f4d
    iac-misconfiguration-detection:
      jobs:
        iac-misconfig-detection-cloudformation:
          steps:
            - name: Run KICS (cloudformation)
              uses: registry.jit.io/control-kics-alpine:latest
              with:
                args: scan -t CloudFormation -p ${WORK_DIR:-.} -o $REPORT_FILE -f json --config /cloudformation-config.yaml --disable-secrets --exclude-queries c8dee387-a2e6-4a73-a942-183c975549ac
        iac-misconfig-detection-serverless:
          steps:
            - name: Run KICS (serverless)
              uses: registry.jit.io/control-kics-alpine:latest
              with:
                args: scan -t ServerlessFW -p ${WORK_DIR:-.} -o $REPORT_FILE -f json --config /serverless-config.yaml --disable-secrets --exclude-queries 165aae3b-a56a-48f3-b76d-d2b5083f5b8f
```

Replace the arguments shown in this example with the arguments that you intend to use. Arguments must be supported by the tool.

> 🚧 Important!
>
> Include all the arguments that were in the original arguments line, as it will be completely overridden by this change.
>
> Make sure you use the correct indentation!