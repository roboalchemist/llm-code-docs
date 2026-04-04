# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/aws-secrets-manager.md

# AWS Secrets Manager

> Guide to configuring ggscout to collect and monitor secrets from AWS Secrets Manager, including authentication and region configuration.

# AWS Secrets Manager Integration

GGScout supports integration with AWS Secrets Manager to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Configuration

To configure GGScout to work with AWS Secrets Manager, add the following configuration to your `ggscout.toml` file:

```toml
[sources.aws-source-playground]
type = "awssecretsmanager"
fetch_all_versions = true
profile_name = "default"
regions = ["us-east-1"]
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.aws-source-playground.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.aws-source-playground.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### Configuration Parameters

| Parameter            | Description                                | Required | Default Value |
| -------------------- | ------------------------------------------ | -------- | ------------- |
| `type`               | Must be set to `"awssecretsmanager"`       | Yes      |             |
| `fetch_all_versions` | Whether to collect all versions of secrets | Yes      |             |
| `profile_name`       | AWS profile name to use                    | No       |             |
| `regions`            | AWS regions where secrets are stored       | No       |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write") | No       | "read"      |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team) | No       |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

### Authentication

GGScout uses the AWS Rust client for authentication, which follows the standard AWS credential resolution process. The authentication is handled automatically by the AWS SDK, and the TOML configuration file only allows specifying the `profile_name` parameter.

:::note
Authentication methods cannot be directly configured in the TOML file. Instead, you must provide the necessary AWS credentials through environment variables or AWS credential files.
:::

### AWS Credential Resolution

The AWS Rust client will attempt to load credentials in the following order:

1. Environment variables:

   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_SESSION_TOKEN` (if using temporary credentials)

2. AWS credential files:

   - `~/.aws/credentials`
   - `~/.aws/config`

3. IAM roles for Amazon EC2 or ECS tasks

4. IAM user federation

### Environment Variables

For direct authentication, you must set the following environment variables:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
- `AWS_SESSION_TOKEN`: Your AWS session token (if using temporary credentials)
- `AWS_REGION`: The AWS region where your secrets are stored

:::tip
For production environments, it's recommended to use IAM roles or instance profiles rather than hardcoding credentials in environment variables.
:::

## Required AWS Permissions

To fetch secrets from AWS Secrets Manager, the identity used by GGScout must have the appropriate IAM permissions. The minimum required permissions are:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:BatchGetSecretValue",
        "secretsmanager:DescribeSecret",
        "secretsmanager:ListSecretVersionIds"
      ],
      "Resource": "arn:aws:secretsmanager:*:*:secret:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:ListSecrets"
      ],
      "Resource": "*"
    }
  ]
}
```

As stated in [AWS documentation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecretsmanager.html), it is not possible to restrict the `"secretsmanager:ListSecrets"` permissions to a subset of secrets.

## Best Practices

1. Use IAM roles or instance profiles when running on AWS infrastructure
2. Follow the principle of least privilege for IAM permissions
3. Enable `fetch_all_versions` to track changes in your secrets over time
4. Regularly rotate access keys
5. Use separate AWS accounts or regions for different environments
