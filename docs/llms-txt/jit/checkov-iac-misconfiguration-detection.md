# Source: https://docs.jit.io/docs/checkov-iac-misconfiguration-detection.md

# Checkov IaC Misconfiguration Detection

## Overview

Checkov is a static analysis tool that scans cloud infrastructure configurations to detect security and compliance issues. This integration leverages Checkov to run misconfiguration framework scanning across multiple IaC frameworks, helping you identify potential security vulnerabilities in your infrastructure code before deployment.\
Jit uses **KICS** by default as the Infrastructure as Code (IaC) scanning tool to detect misconfigurations and security issues. However, this page explains how customers can use **Checkov** as an alternative if they prefer.

## Supported Frameworks

Checkov supports scanning the following IaC frameworks:

* Terraform
* CloudFormation
* Kubernetes
* Serverless
* Helm
* OpenAPI

## Requirements

Before using the Checkov IaC integration, ensure that:

* You have a `jit-plan.yml` file in your repository
* Your CI/CD pipeline is configured to run Jit scans
* Your repository contains IaC files in one of the supported formats

## Configuration

### Enabling the Scan

To enable Checkov IaC scanning, you need to update the `jit-plan.yml` file which is located in the Jit repository.\
The `jit-plan.yml` file defines the user's security plan as code and supports the ability to configure additional security tools beyond the default ones provided by Jit, giving customers the flexibility to choose the tools that best fit their security needs.\
To enable Checkov IaC scanning, update the `jit-plan.yml` file in your repository with the following configuration:

```yaml
override:
  workflows:
    iac-misconfiguration-detection:
      jobs:
        checkov-iac-misconfig-detection:
          enabled: true
        iac-misconfig-detection-cloudformation:
          enabled: false
        iac-misconfig-detection-kubernetes:
          enabled: false
        iac-misconfig-detection-pulumi:
          enabled: false
        iac-misconfig-detection-serverless:
          enabled: false
        iac-misconfig-detection-terraform:
          enabled: false
```

This configuration enables the generic Checkov scanner while disabling the framework-specific scanners, which are no longer needed when using the comprehensive scanner.

### Severity Filtering

By default, Checkov will only report findings with HIGH severity. You can customize the severity threshold using the `SEVERITY_THRESHOLD` environment variable.

Available severity options:

* `HIGH` (default) - Only show high severity issues
* `MEDIUM` - Show high and medium severity issues
* `LOW` - Show all detected issues (high, medium, and low)

#### Example Configuration with Custom Severity

```yaml
override:
  workflows:
    iac-misconfiguration-detection:
      jobs:
        checkov-iac-misconfig-detection:
          enabled: true
          steps:
            - name: Run Checkov
                with:
                env:
                    SEVERITY_THRESHOLD: MEDIUM
```

## Examples

### Basic Configuration

Here's an example of a minimal configuration to enable Checkov scanning:

```yaml
override:
  workflows:
    iac-misconfiguration-detection:
      jobs:
        checkov-iac-misconfig-detection:
          enabled: true
```

### Configuration with Low Severity Threshold

To catch all issues, including those with low severity:

```yaml
override:
  workflows:
    iac-misconfiguration-detection:
      jobs:
        checkov-iac-misconfig-detection:
          enabled: true
          steps:
            - name: Run Checkov
                with:
                env:
                    SEVERITY_THRESHOLD: LOW
```