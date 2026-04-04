# Source: https://docs.gitguardian.com/internal-monitoring/detect/secrets-incidents.md

# Secrets incidents

> Defines what a secret incident is in GitGuardian Internal Monitoring and explains why hardcoded secrets represent a security threat.

## What is a secret incident? What are its implications?

Secret incidents are open issues that need your attention to be resolved. They are created thanks to [our secrets detection engine](../../secrets-detection/home) that scans your internal sources for [hardcoded secrets](../../secrets-detection/core-concepts/what-is-a-secret.md) to display them in your dashboard.

Leaving a secret in plain text represents a threat for the security of the resources that are protected by that secret. To learn more about why hardcoded secrets are a vulnerability that needs your Application or Product Security teams' attention, read the related paragraph in our [Core Concepts](../../secrets-detection/core-concepts/what-is-a-secret) section.
