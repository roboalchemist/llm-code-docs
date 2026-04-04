# Source: https://docs.gitguardian.com/platform/deployment-model/self-hosted.md

# Source: https://docs.gitguardian.com/honeytoken/self-hosted.md

# Honeytoken for self-hosted installations

> Enable and configure the Honeytoken feature on self-hosted GitGuardian installations.

## Enabling Honeytoken on self-hosted environments

:::info
Honeytoken is available to self-hosted installations as an add-on on top of the Secret Detection license.
:::

To enable Honeytoken in your self-hosted GitGuardian instance, please contact support@gitguardian.com.

Please note that this feature is not compatible with self-hosted installations in an airgapped environment as it requires access to AWS.

After your request, we'll enable the feature, establish your dedicated AWS infrastructure for Honeytokens, and reach out to finalize the setup.

### Synchronize license

After receiving confirmation from your GitGuardian contact regarding the feature activation for your instance(s), it is crucial to ensure that the GitGuardian application's [license is synchronized accordingly](/self-hosting/license-management).

Once this task is completed, Honeytoken will appear on your GitGuardian dashboard within a few minutes. However, note that you won't be able to create any honeytokens until you complete the next step.

### Set up the AWS integration

To configure the AWS integration required for the AWS honeytokens, your GitGuardian contact will share a download link for the json file (`aws_honeytoken_config.json`). Follow these steps to complete the configuration:

1. Access the Admin area of your GitGuardian dashboard (administrative rights are necessary).
2. Navigate to Settings > Honeytoken and upload the provided JSON file.
3. This action triggers the configuration process, which establishes users and keys within your dedicated AWS organization.
4. While the full setup may take some time, you can start using available honeytokens immediately.
5. Monitor the dashboard to observe the honeytoken count increasing as the setup progresses.

Navigate to the Admin area in your GitGuardian dashboard (admin rights required). Go to Settings > Honeytoken and upload the provided JSON file. This triggers the configuration process, setting up users and keys within your dedicated AWS organization.

Full setup may take some time, but you can begin using available honeytokens immediately. Monitor the dashboard to see your honeytoken count rise as the setup progresses.

## Health checks

The Health Checks page in the Admin area contains a Honeytoken section, showing the AWS integration statuses.

### AWS integration health checks

There are two types of health checks:

- "Access to AWS resources":
    - This health check verifies whether the instance can successfully create AWS users and keys intended for use as honeytokens.
    - Additionally, it ensures that access to the S3 bucket containing logs is operational.
    - If any issues arise during this check, it can be manually restarted by clicking the "Check again" button.
- âReception of eventsâ:
    - This health check monitors the seamless functioning of the various methods we employ to collect honeytoken events.
    - Unlike the previous check, this one is scheduled to run at regular intervals and cannot be manually restarted.

      ![Healthchecks](/img/honeytoken/healthchecks.png)

## Network requirements

### Inbound rules

| Port | Source | Destination | Description |
|------|--------|-------------|-------------|
| 443  | AWS<sup>*</sup> | All K8S nodes | Non real-time events webhook |
| 443  | AWS<sup>*</sup> | All K8S nodes | Real-time events webhook |

\* [AWS IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html)

### Outbound rules

Outbound requests include the creation of AWS tokens, and retrieving the logs with events.
Every outbound communications between your GitGuardian instance and AWS are HTTPS protocol on port 443.

| Port | Source |                                         Destination |                            Description |
|:----:|-------:|----------------------------------------------------:|---------------------------------------:|
| 443  |    All K8S nodes |                       `sts.amazonaws.com` |                 Authentication AWS API |
| 443  |    All K8S nodes |             `sts.us-west-2.amazonaws.com` |        Regional Authentication AWS API |
| 443  |    All K8S nodes |                       `iam.amazonaws.com` | AWS Identity and Access Management API |
| 443  |    All K8S nodes |  `s3-accesspoint.us-west-2.amazonaws.com` |                    Regional S3 AWS API |
| 443  |    All K8S nodes |   `organizations.us-east-1.amazonaws.com` |                  Organizations AWS API |
