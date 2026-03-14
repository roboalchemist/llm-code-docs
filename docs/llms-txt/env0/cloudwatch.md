# Source: https://docs.envzero.com/guides/integrations/logs-forwarding/cloudwatch.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon Cloudwatch

> Forward env zero deployment and audit logs to AWS CloudWatch log groups using OIDC authentication

[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) is AWS's service for monitoring and observing your applications and resources. This integration allows you to forward your deployment and audit logs from env zero directly to CloudWatch log groups.

## Prerequisites

Before you begin, make sure you have:

1. [Enabled OIDC](/guides/integrations/oidc-integrations/#enabling-oidc-token-availability) in your env zero organization.
2. Configured an Identity provider as explained in [Set up an AWS OIDC authentication Guide](/guides/integrations/oidc-integrations/oidc-with-aws).

## Setup

To allow env zero to send logs to CloudWatch, you need an IAM policy with the necessary permissions. This policy will be [attached to an IAM Role](/guides/integrations/oidc-integrations/oidc-with-aws/#assign-an-iam-role) you use for OIDC authentication.\
The policy allows env zero to create and write to two log groups: `env0-deployments` and `env0-audits`.

```json Log Transporter Policy theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:PutLogEvents"
      ],
      "Resource": [
        "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:env0-deployments",
        "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:env0-deployments:*",
        "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:env0-audits",
        "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:env0-audits:*"
      ]
    }
  ]
}
```

<Info>
  **Optional: Using a Log Group Prefix**

  If you manage multiple env zero organizations that log to the same AWS account, you can use a prefix to keep the logs separate. For example, a prefix like `prod/` would create log groups named `prod/env0-deployments` and `prod/env0-audits`.

  To use a prefix, modify the Resource ARNs in the policy. For a prefix of `prod/`, your resource list would look like this:

  ```json  theme={null}
  "Resource": [
    "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:prod/env0-deployments",
    "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:prod/env0-deployments:*",
    "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:prod/env0-audits",
    "arn:aws:logs:<AWS_REGION>:<AWS_ACCOUNT_ID>:log-group:prod/env0-audits:*"
  ]
  ```

</Info>

## Self Configuration of CloudWatch Transporter

There are two ways to configure the integrations:

1. ### In the env zero app

In the organization's integrations page, click on CloudWatch and fill the form's fields:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/logs-forwarding/e4c5dbf676cbd0bc2065a625e490e3d975be1e6d9e47e4cd7a60268b4bad93de-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=f39dd5e0809a1b88e71ffc0cd7082705" alt="Log forwarding integration configuration form showing setup fields" width="1120" height="1436" data-path="images/guides/integrations/logs-forwarding/e4c5dbf676cbd0bc2065a625e490e3d975be1e6d9e47e4cd7a60268b4bad93de-image.png" />
</Frame>

1. ### Using environment variables

   In the env zero platform you will need to configure the following environment variables in [any scope](/guides/admin-guide/variables/#variables-and-scopes-in-env0) to forward the **deployment logs**. These are the relevant environment variables:

   | Environment variable name               | Description                                                                                | Mandatory |
   | :-------------------------------------- | :----------------------------------------------------------------------------------------- | :-------- |
   | `ENV0_CLOUDWATCH_ROLE_ARN`              | The ARN of the IAM role associated with your OIDC provider                                 | Yes       |
   | `ENV0_CLOUDWATCH_AWS_REGION`            | The AWS region where your log groups will reside                                           | Yes       |
   | `ENV0_CLOUDWATCH_SESSION_DURATION`      | The OIDC token session duration in seconds. Defaults to 3600 (1 hour) if not set.          | No        |
   | `ENV0_CLOUDWATCH_LOG_GROUP_NAME_PREFIX` | An optional prefix for your log group names. Must match the prefix used in your IAM policy | No        |

env zero sets the log group name according to the log type:

1. ### Audit Logs

   * `logGroupName` - `env0-audits`

2. ### Deployment Logs

   * `logGroupName` - `env0-deployments`

Built with [Mintlify](https://mintlify.com).
