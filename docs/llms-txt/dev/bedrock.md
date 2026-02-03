# Source: https://dev.writer.com/home/integrations/bedrock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoke Palmyra models on Amazon Bedrock

Palmyra X5 and Palmyra X4 are available on [Amazon Bedrock](https://aws.amazon.com/bedrock/).

Amazon Bedrock is a fully managed service from AWS that enables developers to build and scale generative AI applications using foundation models from leading AI companies. This integration allows you to use Palmyra X5 and X4 in Amazon's serverless environment.

This guide covers how to:

* Install and configure the AWS CLI, which you need to connect to Bedrock
* List available Writer models on Bedrock
* Use the AWS `boto3` Python SDK to invoke Palmyra models on Bedrock

## Prerequisites

Before interacting with Palmyra models on Bedrock, you need an [AWS account](https://aws.amazon.com/) with access to Bedrock.

## Install and configure the AWS CLI

1. [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. Configure the AWS CLI with your AWS credentials. You can configure the CLI using the following command and providing your AWS account credentials:

```bash  theme={null}
aws configure sso
```

Alternatively, you can configure the CLI with environment variables or a credentials file. See the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html#getting-started-quickstart-config) for more details.

3. Test that your AWS CLI is configured correctly by running the following command:

```bash  theme={null}
aws sts get-caller-identity
```

You should see output similar to the following:

```bash  theme={null}
{
    "UserId": "A123456789012",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

## Install the AWS boto3 SDK for Python

To invoke Palmyra models on Bedrock using Python, you can use the AWS `boto3` SDK.

Install the `boto3` SDK using the following command:

```bash  theme={null}
pip install boto3
```

## Subscribe to Bedrock Models

<Warning>
  Writer Palmyra X5 and X4 models are available in Amazon Bedrock in the US West (Oregon) AWS Region with [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). For the most up-to-date information on model support by Region, refer to the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html).
</Warning>

To subscribe to the Palmyra X5 and Palmyra X4 models on Bedrock, go to the [Bedrock console](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to the Writer models you want to use.

You can also list the available models from Writer using the following command:

<CodeGroup>
  ```bash AWS CLI theme={null}
  aws bedrock list-foundation-models --region=us-west-2 --by-provider writer --query "modelSummaries[*].modelId"
  ```

  ```python boto3 (Python SDK) theme={null}
  import boto3

  bedrock = boto3.client(service_name="bedrock", region_name="us-west-2")
  response = bedrock.list_foundation_models(byProvider="writer")

  for summary in response["modelSummaries"]:
      print(summary["modelId"])
  ```
</CodeGroup>

## Use Palmyra X5 and Palmyra X4 on with the AWS Python SDK

<Warning>
  Palmyra X5 and Palmyra X4 are only available in the US West (Oregon) region but can be accessed through cross-Region inference. Cross-Region inference allows you to distribute traffic across multiple AWS Regions. To learn more about cross-Region inference for Bedrock, see [Increase throughput with cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) and [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html).
</Warning>

The following example uses the `boto3` Python SDK to create a chat completion with the Palmyra X5 model on Bedrock. The `modelId` is `us.writer.palmyra-x5-v1:0`, which is the ID for the [cross-region inference profile for Palmyra X5](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html).

```python boto3 (Python SDK) theme={null}
import boto3

client = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")
response = client.converse(
    modelId="us.writer.palmyra-x5-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Write a one sentence product description for a cozy, stylish sweater suitable for both casual and formal occasions"
                }
            ],
        }
    ],
)
print(response["output"]["message"]["content"][0]["text"])
```

Learn more about the `converse` method in the [boto3 Python SDK documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html).

## Example: Summarize a meeting transcript

The following example uses Palmyra X5 to summarize a meeting transcript and provide a list of action items from the transcript.

It takes a meeting transcript text file, passes it to Palmyra X5 with instructions to provide a summary of the meeting and a list of action items, and prints the response.

```python boto3 (Python SDK) theme={null}
import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-west-2")

# Set the model ID, e.g. Palmyra X5.
# This is the ID for the cross-region inference profile for Palmyra X5.
# See https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html.
model_id = "us.writer.palmyra-x5-v1:0"

transcript_file_path = "call-transcript.txt"
transcript_format = "txt"

# Load the document
with open(transcript_file_path, "rb") as file:
    document_bytes = file.read()

# Start a conversation with a user message and the document
conversation = [
    {
        "role": "user",
        "content": [
            {
                "text": "Create a summary of the meeting notes and provide a list of action items."
            },
            {
                "document": {
                    # Available formats: html, md, pdf, doc/docx, xls/xlsx, csv, and txt
                    "format": transcript_format,
                    "name": "Meeting Notes",
                    "source": {"bytes": document_bytes},
                }
            },
        ],
    }
]

try:
    # Send the message to the model.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 500, "temperature": 0.3},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```

## Additional resources

See more information and examples below:

* [AWS blog post](https://aws.amazon.com/blogs/aws/writer-palmyra-x5-and-x4-foundation-models-are-now-available-in-amazon-bedrock/) about Palmyra X5 and X4 on Bedrock
* [Additional code examples for Amazon Bedrock](https://github.com/writer/aws-examples/tree/main/bedrock-examples)
