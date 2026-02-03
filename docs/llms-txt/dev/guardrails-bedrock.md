# Source: https://dev.writer.com/home/guardrails-bedrock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up Bedrock guardrails

> Configure AWS Bedrock Guardrails for content filtering and sensitive data protection

This guide shows you how to configure [AWS Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with AI Studio. After completing this setup, AI Studio can use your Bedrock guardrails to filter content, detect PII, and enforce topic policies across your AI agents.

For an overview of how guardrails work in AI Studio, see [Configure guardrails](/home/guardrails).

## Prerequisites

Before configuring Bedrock guardrails in AI Studio, you need:

* An AWS account with access to Amazon Bedrock
* A Bedrock guardrail created in the AWS console
* AWS credentials with permission to invoke the guardrail
* Enterprise plan access to AI Studio

## Create a Bedrock guardrail in AWS

If you haven't created a Bedrock guardrail yet, follow these steps in the AWS console:

1. Navigate to **Amazon Bedrock > Guardrails** in the AWS console
2. Select **Create guardrail**
3. Configure your guardrail policies:
   * **Content filters**: Block harmful content categories (hate, insults, sexual, violence)
   * **Denied topics**: Define custom topics to block
   * **Word filters**: Block specific words or phrases
   * **Sensitive information filters**: Detect and block PII types
   * **Contextual grounding**: Check for hallucinations and relevance
4. Save your guardrail and note the **Guardrail ID** and **Version**

For detailed instructions, see [Create a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html) in the AWS documentation.

## Configuration parameters

Configure these parameters when adding a Bedrock guardrail in AI Studio:

### Required parameters

| Parameter               | Description                                                                                                                                                                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `guardrailIdentifier`   | The unique ID of your Bedrock guardrail (found in the AWS console)                                                                                                                                                                                                        |
| `guardrailVersion`      | The version of your guardrail (`DRAFT` or a version number like `1`, `2`)                                                                                                                                                                                                 |
| `aws_region_name`       | AWS region where your guardrail is deployed. Define the guardrail in the same region where your inference requests are made. See [supported regions](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html) in the AWS documentation. |
| `aws_access_key_id`     | AWS access key ID for authentication                                                                                                                                                                                                                                      |
| `aws_secret_access_key` | AWS secret access key for authentication                                                                                                                                                                                                                                  |

### Optional parameters

| Parameter                      | Description                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `disable_exception_on_block`   | When `true`, returns a modified response instead of raising an exception when content is blocked. Useful for chat interfaces where exceptions may disrupt the conversation flow. Default: `false` |
| `aws_session_token`            | Session token for temporary AWS credentials (required when using STS)                                                                                                                             |
| `aws_session_name`             | Name for the AWS session                                                                                                                                                                          |
| `aws_profile_name`             | AWS profile name for credential retrieval from `~/.aws/credentials`                                                                                                                               |
| `aws_role_name`                | IAM role name for cross-account access or role assumption                                                                                                                                         |
| `aws_web_identity_token`       | Web identity token for OIDC-based authentication                                                                                                                                                  |
| `aws_sts_endpoint`             | Custom AWS STS endpoint URL                                                                                                                                                                       |
| `aws_bedrock_runtime_endpoint` | Custom Bedrock runtime endpoint URL                                                                                                                                                               |

## AWS authentication options

AI Studio supports multiple [AWS authentication methods](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for Bedrock guardrails.

### Access keys (recommended for getting started)

Use IAM user access keys for straightforward authentication:

```
aws_access_key_id: AKIAIOSFODNN7EXAMPLE
aws_secret_access_key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_region_name: us-east-1
```

### Temporary credentials (STS)

Use temporary credentials from [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html):

```
aws_access_key_id: ASIAXXX...
aws_secret_access_key: xxx...
aws_session_token: FwoGZXIvYXdzEBY...
aws_region_name: us-east-1
```

### IAM role assumption

Assume an IAM role for cross-account access or elevated permissions:

```
aws_access_key_id: AKIAIOSFODNN7EXAMPLE
aws_secret_access_key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_role_name: bedrock-guardrail-role
aws_region_name: us-east-1
```

### Web identity (OIDC)

Use OIDC tokens for container-based or Kubernetes deployments:

```
aws_web_identity_token: eyJhbGciOiJSUzI1NiIs...
aws_role_name: bedrock-guardrail-role
aws_region_name: us-east-1
```

## Required IAM permissions

The AWS credentials you provide must have permission to invoke your Bedrock guardrail. Create an IAM policy with the following permissions:

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:ApplyGuardrail"
      ],
      "Resource": "arn:aws:bedrock:*:*:guardrail/*"
    }
  ]
}
```

For production environments, scope the resource ARN to your specific guardrail:

```json  theme={null}
{
  "Resource": "arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123def456"
}
```

## Guardrail versioning

Bedrock guardrails support versioning, allowing you to test changes before applying them to production:

| Version value  | Behavior                                     |
| -------------- | -------------------------------------------- |
| `DRAFT`        | Uses the current draft version (for testing) |
| `1`, `2`, etc. | Uses a specific published version            |

**Recommended workflow:**

1. Test guardrail changes using `DRAFT` version in a development environment
2. Publish a new version in the AWS console when satisfied
3. Update production AI Studio configuration to use the new version number

## Bedrock guardrail capabilities

AWS Bedrock Guardrails provide several content filtering capabilities:

### Content filters

Block content based on harmful categories with configurable thresholds:

* **Hate**: Discriminatory or prejudiced content
* **Insults**: Demeaning or offensive language
* **Sexual**: Sexually explicit content
* **Violence**: Violent or threatening content
* **Misconduct**: Content promoting illegal activities
* **Prompt attacks**: Attempts to manipulate the model

### Denied topics

Define custom topics that should be blocked. Useful for:

* Preventing discussion of competitors
* Blocking off-topic conversations
* Enforcing industry-specific restrictions

### Sensitive information filters

Detect and block PII types including:

* Names, addresses, phone numbers
* Email addresses, URLs
* Credit card numbers, bank accounts
* Social Security numbers (US)
* Driver's license numbers
* Passport numbers

### Word filters

Block specific words, phrases, or patterns. Supports:

* Exact word matching
* Profanity filters
* Custom blocked terms

## Error handling

When Bedrock blocks content, AI Studio returns an error to the agent. The default behavior raises an exception that halts the request.

Set `disable_exception_on_block: true` to return a modified response instead of raising an exception. This is useful for:

* Chat interfaces where exceptions disrupt the conversation
* Applications that need to handle blocks gracefully
* Scenarios where you want to show a custom message to users

## Troubleshooting

### Common errors

| Error                       | Cause                           | Solution                                                 |
| --------------------------- | ------------------------------- | -------------------------------------------------------- |
| `AccessDeniedException`     | Missing IAM permissions         | Verify your IAM policy includes `bedrock:ApplyGuardrail` |
| `ResourceNotFoundException` | Invalid guardrail ID or version | Check the guardrail ID and version in the AWS console    |
| `ValidationException`       | Invalid parameters              | Verify region name and other parameters are correct      |
| `ThrottlingException`       | Rate limit exceeded             | Implement retry logic or request a quota increase        |

### Verify your guardrail

Test your guardrail directly in the AWS console before configuring it in AI Studio:

1. Navigate to your guardrail in the AWS Bedrock console
2. Select **Test** to open the testing interface
3. Enter sample content that should trigger the guardrail
4. Verify the guardrail blocks or allows content as expected

## Next steps

* [Configure guardrails](/home/guardrails): Learn about guardrail modes and scoping
* [Track usage and spend](/home/observability): Monitor guardrail activity and usage
* [AWS Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html): Detailed AWS documentation
* [Create a guardrail in AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html): Step-by-step AWS console instructions
* [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/): Understand Bedrock guardrail costs
