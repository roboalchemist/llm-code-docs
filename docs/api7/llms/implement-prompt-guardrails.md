# Source: https://docs.api7.ai/apisix/how-to-guide/ai-gateway/implement-prompt-guardrails.md

# Implement Prompt Guardrails

Prompt guardrails provide additional safeguards to protect user privacy, prevent unintended or harmful model behaviors, discourage hallucinated responses, and stay compliant with responsible AI ethical standards when working with [large language models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model).

In this document, you will learn a few recommended practices for implementing prompt guardrails, including defining allow and deny patterns, moderating content for toxicity, redacting sensitive information, and discouraging undesired outputs and hallucinations.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Understand how to [proxy requests to LLM services](https://docs.api7.ai/apisix/how-to-guide/ai-gateway/proxy-openai-requests.md).

## Implement Allow and Deny Patterns[â](#implement-allow-and-deny-patterns "Direct link to Implement Allow and Deny Patterns")

During LLM integration, implementing allow and deny patterns is a practice for enhancing security and controlling the quality of user interactions. By defining explicit rules that permit or block specific types of input, organizations can prevent confidential or inappropriate content from reaching the model. This approach not only protects against potential misuse and harmful outputs but also ensures compliance with regulatory standards and internal policies. Such guardrails are crucial for maintaining the integrity and reliability of AI systems, especially when handling sensitive data or user-generated content.

The [`ai-prompt-guard`](https://docs.api7.ai/hub/ai-prompt-guard.md) plugin helps enforce these guardrails by inspecting and validating incoming prompt messages at the gateway. It checks the content of requests against user-defined allowed and denied patterns to ensure that only approved inputs are forwarded to upstream LLM. Based on its configuration, the plugin can either examine just the latest message or the entire conversation history, and it can be set to check prompts from all roles or only from end users.

## Moderate Content for Toxicity[â](#moderate-content-for-toxicity "Direct link to Moderate Content for Toxicity")

Content moderation for toxicity in user prompts helps ensure a safe and respectful environment for users. Given that LLMs can generate responses based on user input, it is crucial to correctly handle and filter out harmful content such as profanity, hate speech, insults, harassment, violence, and threats, before they are processed by the model.

The [`ai-aws-content-moderation`](https://docs.api7.ai/hub/ai-aws-content-moderation.md) and [`ai-aliyun-content-moderation`](https://docs.api7.ai/hub/ai-aliyun-content-moderation.md) plugins enforce these guardrails by analyzing input prompts for toxic or unsafe content and evaluating them against configurable thresholds for each moderation category. If a request exceeds any configured threshold, it is rejected at the gateway before being forwarded to the upstream LLM.

## Discourage Hallucinations and Undesired Output[â](#discourage-hallucinations-and-undesired-output "Direct link to Discourage Hallucinations and Undesired Output")

Hallucinations refer to instances where the model generates information that is factually incorrect, misleading, or entirely fabricated, even though it may sound plausible or confident. There are different approaches to mitigate hallucinations, one of which is to pre-engineer system prompts. For example, you can configure the following system prompt:

```
Before you respond to the user message, on a scale of 0 to 10, how confident are you with your response? If your confidence level is lower than 8/10, respond with "Sorry I do not have an answer that I am confident with" and explain the reasoning. If your confidence level is higher or equal to 8/10, you may return the response to the user.
```

You can also pre-engineer system prompts to discourage undesired output. For example, you may want all responses to not quote information from copyrighted content, or reference any controversial sources. You can configure the following system prompt:

```
Provide all responses based on factual information, avoiding any quotes from copyrighted materials. Do not reference or include information from controversial or unreliable sources. Ensure that all content is original, non-derivative, and based on widely accepted, publicly available information.
```

See [Configure Prompt Decorators](https://docs.api7.ai/apisix/how-to-guide/ai-gateway/configure-prompt-decorators.md) to learn how you can configure these pre-engineered prompts.

## Redact Sensitive Information (PII)[â](#redact-sensitive-information-pii "Direct link to Redact Sensitive Information (PII)")

Redacting sensitive information is a key aspect of prompt guardrails, especially when handling user-generated content. By detecting and masking Personally Identifiable Information (PII) in prompts, you can reduce the risk of accidental data exposure, support compliance with privacy regulations, and prevent sensitive data from being sent to upstream LLMs.

API7 Enterprise will soon provide support for integration with external guardrail solutions, such as [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/).

Additionally, API7 Enterprise provides the [`data-mask`](https://docs.api7.ai/hub/data-mask.md) plugin, which masks sensitive information in request headers, bodies, and URL query parameters when requests are logged by logging plugins. Note that this plugin does not modify the actual request or response traffic. The plugin is not available in APISIX.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned a few recommended practices for implementing prompt guardrails to provide additional safeguards when integrating with LLM service providers.

Other types of guardrailsâsuch as denied topics, content filters, and alternative implementation strategiesâalso exist. Reviewing additional resources and exploring different approaches can help determine the strategies that best align with your organizationâs requirements.
