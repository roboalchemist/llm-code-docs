# Source: https://docs.aws.amazon.com/iot-device-defender/latest/devguide/llms.txt

# AWS IoT Device Defender AWS IoT Device Defender Developer Guide

- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html)
- [AWS IoT Device Defender troubleshooting guide](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-troubleshoot.html)
- [Document history](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/doc-history.html)

## [Getting started with AWS IoT Device Defender](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-tutorials.html)

- [Setting up](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-setting-up.html): Set up before using AWS IoT Device Defender's capabilities.
- [Audit guide](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-tutorial.html): Initialize AWS IoT Device Defender's auditing capabilities.
- [ML Detect guide](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-ml-getting-started.html): Get started with AWS IoT Device Defender ML Detect.
- [Customize when and how you view AWS IoT Device Defender audit results](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-suppressions-example.html): Use AWS IoT Device Defender audit finding suppressions to control when and how you view your audit results.


## [Audit](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-audit.html)

### [Audit checks](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-audit-checks.html)

Use the following audit checks for your data for AWS IoT Device Defender.

- [Intermediate CA revoked for active device certificates check](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-active-intermediary-device-revoked-CA.html): Use this check to identify all related device certificates that are still active despite revoking an intermediate CA.
- [Revoked CA certificate still active](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-revoked-ca-cert.html): Use this check to see if a CA certificate was revoked but is active for AWS IoT Device Defender.
- [Device certificate shared](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-device-cert-shared.html): Use this check for multiple connections for a shared certificate in AWS IoT Device Defender.
- [Device certificate key quality](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-device-cert-key-quality.html): Use this check for the device certificate key quality for AWS IoT Device Defender.
- [CA certificate key quality](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-ca-cert-key-quality.html): Use this check for CA certificates for AWS IoT Device Defender.
- [Unauthenticated Cognito role overly permissive](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-unauth-cognito-role-permissive.html): Use this check for overly permissive Amazon Cognito roles for AWS IoT Device Defender.
- [Authenticated Cognito role overly permissive](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-auth-cognito-role-permissive.html): Use this check for overly permissive Amazon Cognito roles.
- [AWS IoT policies overly permissive](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.html): Use this check for AWS IoT policies that grant more permissions than are necessary.
- [AWS IoT policy potentially misconfigured](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-iot-misconfigured-policies.html): Use this check for potentially misconfigured AWS IoT policies that contain MQTT wildcard characters and grant more permissions than necessary.
- [Role alias overly permissive](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-iot-role-alias-permissive.html): Use this check to identify role aliases that have associated policies that are too broad (e.g "iot:*").
- [Role alias allows access to unused services](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-role-alias-unused-svcs.html): Use this check to identify role aliases whose associated policies grant access to services that haven't been used in the past year.
- [CA certificate expiring](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-ca-cert-approaching-expiration.html): Use this check to identify CA certificates that will expire within the next 30 days (or that has already expired).
- [Conflicting MQTT client IDs](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-conflicting-client-ids.html): Use this check to identify when multiple connections are made to AWS IoT with the same client ID.
- [Device certificate expiring](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-device-cert-approaching-expiration.html): Use this check to identify when a device certificate is expiring within the configured threshold period or has already expired.
- [Device certificate age check](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-certificate-age-check.html): This audit check alerts you when a device certificate has been active for a number of days greater than or equal to the number you specify.
- [Revoked device certificate still active](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-revoked-device-cert.html): Use this check to identify when a device certificate that has been revoked is still active.
- [Logging disabled](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-logging-disabled.html): Use this check to identify when AWS IoT logging has been disabled.
- [Audit commands](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/AuditCommands.html)
- [Audit finding suppressions](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-finding-suppressions.html): Learn about AWS IoT Device Defender audit finding suppressions.


## [Detect](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-detect.html)

- [Security use cases](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-security-use-cases.html): Learn the use cases in which AWS IoT Device Defender Detect metrics can be used to monitor for security threats.
- [Concepts](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-concepts.html)
- [Behaviors](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-behaviors.html): A Security Profile contains a set of behaviors.
- [ML Detect](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-ml.html): Learn about getting started with AWS IoT Device Defender ML Detect.
- [Custom metrics](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-custom-metrics.html): Learn about using AWS IoT Device Defender custom metrics.
- [Device-side metrics](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-device-side-metrics.html): When creating a Security Profile, you can specify your IoT device's expected behavior by configuring behaviors and thresholds for metrics generated by IoT devices.
- [Cloud-side metrics](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-cloud-side-metrics.html): When creating a Security Profile, you can specify your IoT device's expected behavior by configuring behaviors and thresholds for metrics generated by IoT devices.

### [Detect metrics export](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-metrics-export.html)

With metrics export, you can export cloud-side, device-side, or custom metrics from AWS IoT Device Defender and publish them to an MQTT topic that you configure.

- [Metrics export schema](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/metrics-export-json-schema.html): See the following schema for batched metrics export data.
- [Detect metrics export pricing](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/metrics-export-pricing.html): When you publish cloud-side, device-side, or custom metrics to an MQTT topic that you configure, you will not incur charges for this step of the export process.
- [Permissions](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-metrics-export-permissions.html): This section contains information about how to set up the IAM roles and policies required to manage AWS IoT Device Defender Detect metrics export.
- [Scoping metrics in security profiles using dimensions](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/scoping-security-behavior.html): Dimensions are attributes that you can define to get more precise data about metrics and behaviors in your security profile.
- [Permissions](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-detect-permissions.html): This section contains information about how to set up the IAM roles and policies required to manage AWS IoT Device Defender Detect.
- [Detect commands](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-commands.html): Use the AWS IoT Device Defender Detect commands to identify unusual behavior for your devices.
- [How to use AWS IoT Device Defender detect](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-HowToHowTo.html)


## [Mitigation actions](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-mitigation-actions.html)

- [Mitigation action commands](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/mitigation-action-commands.html): You can use these mitigation action commands to define a set of actions for your AWS account that you can later apply to one or more sets of audit findings.


## [Using AWS IoT Device Defender with other AWS services](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-integration.html)

- [Security Hub CSPM integration](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/securityhub-integration.html): Learn how to use the AWS IoT Device Defender integration with AWS Security Hub CSPM.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Security best practices for device agents](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-DetectMetricsMessagesBestPract.html)


## [Security](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/security.html)

- [Data protection](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS IoT Device Defender.

### [Identity and access management](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/security-iam.html)

How to authenticate requests and manage access your AWS IoT Device Defender resources.

- [How AWS IoT Device Defender works with IAM](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS IoT Device Defender, learn what IAM features are available to use with AWS IoT Device Defender.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS IoT Device Defender resources.
- [Troubleshooting](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT Device Defender and IAM.
- [Compliance validation](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT Device Defender features for data resiliency.
