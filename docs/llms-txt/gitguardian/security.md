# Source: https://docs.gitguardian.com/platform/agent/security.md

# Data security and privacy

> :::warning[Alpha]
The GitGuardian Agent is currently in **private alpha**. Features and behavior may change. Contact us at [support@gitguardian.com](mailto:support@gitguardian.com) or reach out to your CSM or account manager to request access.
:::

:::warning[Alpha]
The GitGuardian Agent is currently in **private alpha**. Features and behavior may change. Contact us at [support@gitguardian.com](mailto:support@gitguardian.com) or reach out to your CSM or account manager to request access.
:::

The GitGuardian Agent is designed with security and privacy as core principles. This page explains how your data is handled when interacting with the Agent.

- **Secret values are always redacted** before any data reaches the AI model â only metadata (type, severity, location, status) is shared
- **Workspace boundaries respected** â the Agent operates with the user's own permissions, never exceeding their access level
- **No model-provider training** â prompts and responses are never shared with model providers; powered by Amazon Bedrock with strict data controls
- **Zero data retention** â data passes through for inference only, nothing is stored by Bedrock or the model provider

## Secret redaction

Sensitive values such as the secret itself are always **redacted** before being sent to the AI model. The Agent does not need to see the actual secret to provide threat analysis or remediation guidance. Only metadata about the incident (type, severity, locations, status) is shared with the model.

## AI infrastructure

The GitGuardian Agent is powered by [Amazon Bedrock](https://aws.amazon.com/bedrock/), a fully managed AI service provided by AWS. Amazon Bedrock allows GitGuardian to leverage large language models while maintaining strict control over your data.

### Your data is never used for model training

Inputs and outputs sent through Amazon Bedrock are **never used to train or improve** the underlying AI models. This is a core guarantee of the Amazon Bedrock service:

- No customer data is used to train, retrain, or improve base models.
- Model providers have no access to your data at any point.

See [Amazon Bedrock Data Protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) for details.

### Your data is not persisted by the model provider

Amazon Bedrock does not store or log your prompts and responses. Your data passes through the model for inference and is not retained by Amazon Bedrock or the model provider after the response is generated.

See [Security, Privacy, and Responsible AI â Amazon Bedrock](https://aws.amazon.com/bedrock/security-privacy-responsible-ai/) for details.

### Encryption

All data exchanged with Amazon Bedrock is encrypted:

- **In transit**: All communications between GitGuardian and Amazon Bedrock are encrypted using TLS.
- **At rest**: Any data stored on the GitGuardian side is encrypted at rest using industry-standard encryption. Amazon Bedrock supports customer-managed encryption keys through [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-at-rest.html).

See [Amazon Bedrock Data Protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) for details on encryption guarantees.

## What data is sent to the model

When you interact with the Agent, the following data may be sent to the AI model for processing:

- **Your message**: The question or request you type in the Agent interface.
- **Incident context**: Details about the incident you are viewing, such as the secret type, severity, locations, and status. This context allows the Agent to provide relevant and tailored responses.
- **Conversation history**: Previous messages in the current conversation, so the Agent can maintain context across follow-up questions.

As described in [Secret redaction](#secret-redaction) above, actual secret values are always redacted before being sent to the model.
