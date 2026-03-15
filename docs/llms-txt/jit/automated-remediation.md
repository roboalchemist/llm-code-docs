# Source: https://docs.jit.io/docs/automated-remediation.md

# Automated Remediation

## Overview

For some finding types, Jit provides *automated remediation* — an auto-generated code fix that resolves the finding. In those cases, the suggested code is displayed in the PR itself, and the developer can accept it by clicking **Commit suggestion**.

Jit displays suggested remediations in the PR comments. The developer can accept the suggestion to commit the changes.  Following this commit, Jit re-runs security tools on the fixed code.

## Example

The following misconfigured Terraform code is present in the pull request:

```text Misconfigured Terraform code
resource "aws_s3_bucket_object" "examplebucket_object" {
  key                    = "someobject"
  bucket                 = aws_s3_bucket.examplebucket.id
  source                 = "index.html"
}
```

Jit detects the misconfiguration and issues the following remediation suggestion:

![](https://files.readme.io/f5ada62-image_7.png)

Committing the suggestion fixes the misconfiguration. See below for the fixed code:

```Text Fixed Terraform code
resource "aws_s3_bucket_object" "examplebucket_object" {
  server_side_encryption = "AES256"
  key                    = "someobject"
  bucket                 = aws_s3_bucket.examplebucket.id
  source                 = "index.html"
}
```

Jit currently supports remediation for the [Scan IaC for Static Misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations) security requirement.

> 📘 Note
>
> If multiple findings are present in a single pull request, Jit recommends addressing them from the **Files changed** tab using the **Add suggestion to batch** option. This applies minimal code changes in a batch and prevents unnecessary re-running of Jit checks.