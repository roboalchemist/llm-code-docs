# Source: https://braintrust.dev/docs/integrations/ai-providers/bedrock.md

# AWS Bedrock

> Configure AWS Bedrock to access Amazon's foundation models

Configure AWS Bedrock to access Amazon's foundation models through Braintrust.

## Authentication

**Access token**: Use AWS credentials to authenticate with Bedrock

## Configuration

| Field                         | Description                                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Region**<br />String        | Required. The AWS region where your Bedrock models are hosted. [Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)                       |
| **Access key**<br />String    | Required. Your AWS access key ID for authentication. [Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)                                          |
| **Secret**<br />String        | Required. Your AWS secret access key (entered separately in the secret field). [Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)                |
| **Session token**<br />String | Optional. Temporary session token for AWS STS (Security Token Service) authentication. [Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) |
| **API base**<br />URL String  | Optional. Custom API endpoint URL if using a different Bedrock endpoint. Default uses AWS Bedrock default endpoints.                                                                            |

## Models

Popular AWS Bedrock models include:

* Claude 3.5 Sonnet `anthropic.claude-3-5-sonnet-20241022-v2:0`
* Claude 3 Haiku `anthropic.claude-3-haiku-20240307-v1:0`
* Llama 3.1 70B `meta.llama3-1-70b-instruct-v1:0`
* Titan Text `amazon.titan-text-express-v1`

## Additional resources

* [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
* [Bedrock Model IDs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)
* [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt