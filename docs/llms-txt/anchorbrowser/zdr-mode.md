# Source: https://docs.anchorbrowser.io/security/zdr-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Zero Data Retention (ZDR) Mode

> Enhanced security mode that disables all video and log recordings to prevent sensitive data retention

Zero Data Retention (ZDR) Mode is an enhanced security feature that completely disables video recordings and log recordings for your Anchor account. This mode is designed for organizations handling highly sensitive data that require absolute assurance that no session artifacts are retained on the Anchor platform.

## What is ZDR Mode?

When ZDR Mode is enabled, Anchor disables all recording capabilities for your account, including:

* **Video recordings**: No screen recordings or visual captures of browser sessions
* **Log recordings**: No session logs or activity records

This ensures that no sensitive data from your browser sessions is retained on the Anchor platform, providing an additional layer of data protection beyond our standard ephemeral architecture.

## When to use ZDR Mode

ZDR Mode is recommended for organizations that:

* Handle highly regulated or classified information
* Require strict data residency and retention policies
* Work with sensitive customer data that must not be recorded
* Need to comply with specific industry regulations prohibiting data retention
* Operate in environments where even temporary recording poses compliance risks

## How ZDR Mode works

Once enabled, ZDR Mode:

1. Disables all video recording functionality for browser sessions
2. Prevents session logs from being captured or stored
3. Maintains all other Anchor security features, including ephemeral VMs and tenant isolation
4. Applies to all browser sessions created under your account

Note that ZDR Mode does not affect the core functionality of Anchor Browser. All browser automation, authentication, and networking capabilities remain fully operational.

## Enabling ZDR Mode

ZDR Mode is enabled manually by the Anchor team. To request ZDR Mode for your account:

1. Contact your Anchor account representative or reach out to [support@anchorbrowser.io](mailto:support@anchorbrowser.io)
2. Provide your account details and business justification for requiring ZDR Mode
3. The Anchor team will review your request and enable ZDR Mode for your account
4. You will receive confirmation once ZDR Mode has been activated

## Important considerations

* **Debugging limitations**: With ZDR Mode enabled, you will not have access to video recordings or logs for troubleshooting session issues. Ensure your application has adequate logging and monitoring in place.
* **Permanent setting**: Once enabled, ZDR Mode typically remains active for the duration of your service agreement. Contact the Anchor team if you need to modify this setting.
* **No self-service**: ZDR Mode cannot be toggled on or off by customers. All changes must be requested through the Anchor team.

## Compliance and security

ZDR Mode complements Anchor's existing security architecture, which includes:

* Ephemeral virtual machines that are destroyed after each session
* Strict tenant isolation
* Encryption in transit and at rest
* SOC 2 Type II, ISO 27001, HIPAA, and GDPR compliance

For more information about Anchor's security framework, see our [Trust & Security](/security) documentation or visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/).
