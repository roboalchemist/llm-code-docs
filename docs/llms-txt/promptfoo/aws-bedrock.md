# Source: https://www.promptfoo.dev/docs/providers/aws-bedrock/

# AWS Bedrock | Promptfoo

## Setup

1. **Model Access**: Amazon Bedrock provides automatic access to serverless foundation models with no manual approval required.
   - **Most models**: Amazon, DeepSeek, Mistral, Meta, Qwen, and OpenAI models (including GPT-OSS and Qwen3) are available immediately - just start using them.
   - **Anthropic models**: Require one-time use case submission through the model catalog (access granted immediately after submission).
   - **AWS Marketplace models**: Some third-party models require IAM permissions with `aws-marketplace:Subscribe`.
   - **Access control**: Organizations maintain control through IAM roles and SSO profiles.
   - **Default credentials**: Use environment variables or IAM roles for default credentials.

2. **Install the package**: `npm install @aws-sdk/client-bedrock-runtime`.

3. **Configure the provider**: Add the provider ID to your configuration file.

   ```yaml
   providers:
     - id: bedrock:us.anthropic.claude-3-5-sonnet-20250929-v1:0
       config:
         region: us-east-1
         max_tokens: 256
         temperature: 0.7
         top_p: 0.9
         stopSequences: [END, STOP]
   ```

4. **Test**: Use the provided example to test the configuration.

## Application Inference Profiles

1. **Application Inference Profiles**: Use application inference profiles for inference.

   ```yaml
   providers:
     - id: bedrock:amazon.nova-sonic-v1:0
       config:
         region: us-east-1
         maxTokens: 256
   ```

2. **Tool Calling Support**: Support tool calling with OpenAI-compatible function definitions.

   ```yaml
   config:
     tools:
       - type: function
         function:
           name: code_analyzer
           description: Perform arithmetic calculations
           parameters:
             type: object
             properties:
               expression:
                 type: string
                 description: The mathematical expression to evaluate
           required: [expression]
     tool_choice: auto
   ```

3. **Model Variants**: For different model variants, use the appropriate model family.

   ```yaml
   config:
     tools:
       - type: function
         function:
           name: code_analyzer
           description: Perform arithmetic calculations
           parameters:
             type: object
             properties:
               expression:
                 type: string
                 description: The mathematical expression to evaluate
           required: [expression]
     tool_choice: auto
   ```

4. **Usage Example**: Use the provided example to test the configuration.

## Model-graded Tests

1. **Model-graded Tests**: Use Bedrock models to grade outputs. By default, model-graded tests use `gpt-5` and require the `OPENAI_API_KEY` environment variable to be set.

2. **Configuration**: Set the `defaultTest` property to configure the default test.

   ```yaml
   defaultTest:
     options:
       provider:
         id: provider:chat:modelname
         config:
           region: us-east-1
           temperature: 0
           max_new_tokens: 256
   ```

3. **Test**: Use the provided example to test the configuration.

## Multimodal Capabilities

1. **Multimodal Capabilities**: Support multimodal inputs including images and text.

   ```yaml
   providers:
     - id: bedrock:amazon.nova-pro-v1:0
       config:
         region: us-east-1
         inferenceConfig:
           temperature: 0.7
           max_new_tokens: 256
   ```

2. **Usage Example**: Use the provided example to test the configuration.

   ```yaml
   tests:
     - vars:
       - type: llm-rubric
         value: Do not mention that you are an AI or chat assistant
   ```

## Embeddings

1. **Embeddings**: Override the embeddings provider for all assertions that require embeddings.

   ```yaml
   providers:
     - id: bedrock:embeddings:amazon.titan-embed-text-v2:0
       config:
         region: us-east-1
   ```

## Guardrails

1. **Guardrails**: Use guardrails to ensure model access is granted in the AWS Bedrock console.

2. **Configuration**: Set the `guardrailIdentifier` and `guardrailVersion` in the provider config.

   ```yaml
   providers:
     - id: bedrock:us.anthropic.claude-3-5-sonnet-20241022-v2:0
       config:
         guardrailIdentifier: test-guardrail
         guardrailVersion: 1
   ```

## Environment Variables

1. **Environment Variables**: Configure the Bedrock provider using environment variables.

   ```bash
   export AWS_SDK_JS_LOG=1
   npx promptfoo eval
   ```

2. **Environment Variables**: Verify credentials and region configuration.

## Troubleshooting

### Authentication Issues

1. **"Unable to locate credentials" Error**: Check credential priority and verify AWS CLI setup.

2. **"AccessDenied" or "UnauthorizedOperation" Errors**: Verify IAM permissions and model access.

3. **"SSO session has expired"**: Run `aws sso login --profile YOUR_PROFILE`.

4. **"Profile not found"**: Check `~/.aws/config` and verify profile name matches exactly (case-sensitive).

### Model Configuration Issues

1. **Inference profile requires inferenceModelType**: If using an inference profile ARN, ensure the `inferenceModelType` is specified in the configuration.

2. **ValidationException: On-demand throughput isn't supported**: Update the provider configuration to include the regional prefix.

3. **AccessDeniedException: You don't have access to the model with the specified model ID**: Verify IAM permissions and region configuration.

## Knowledge Base

1. **Knowledge Base**: Provides Retrieval Augmented Generation (RAG) functionality.

2. **Prerequisites**: Install the `@aws-sdk/client-bedrock-agent-runtime` package.

3. **Configuration**: Configure the Knowledge Base provider by specifying `kb` in your provider ID.

   ```yaml
   providers:
     - id: bedrock:kb:us.anthropic.claude-3-5-sonnet-20250219-v1:0
       config:
         region: us-east-2
         knowledgeBaseId: YOUR_KNOWLEDGE_BASE_ID
         temperature: 0.0
         max_tokens: 1000
         numberOfResults: 5
   ```

4. **Usage Example**: Use the provided example to test the Knowledge Base with a few questions.

## See Also

- [Amazon SageMaker Provider](/docs/providers/sagemaker/)
- [RAG Evaluation Guide](/docs/guides/evaluate-rag/)
- [Context-based Assertions](/docs/configuration/expected-outputs/model-graded/)
- [Configuration Reference](/docs/configuration/reference/)
- [Command Line Interface](/docs/usage/command-line/)
- [Provider Options](/docs/providers/)
- [Amazon Bedrock Examples](https://github.com/promptfoo/promptfoo/tree/main/examples/amazon-bedrock)