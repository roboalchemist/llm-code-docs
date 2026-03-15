# Source: https://docs.firehydrant.com/docs/firehydrant-ai-security-practices.md

# AI Security Practices

How we are ensuring the security of your data in our AI product

# Data Access

## How will my data be used?

We only send data in the prompt. Your data will never be used to train our models and cannot be used to train the models of our upstream providers. You will additionally have control over whether AI is available in your tenant, and for which features.

## Who has access to AI-generated data in the platform?

Our AI functionality is bound by the same rules as our platform security and privacy. You control user access to incident data and we have implemented tenancy at the lowest level. Users will only be able to view AI-generated content for incidents that they have access to.

# Vendor Security

## Which providers are in use?

[OpenAI](https://openai.com/security)

[Anthropic](https://trust.anthropic.com/)

[Recall.ai](https://security.recall.ai/)

[AssemblyAI](https://www.assemblyai.com/security)

## How have you vetted supporting vendors?

All vendors that were onboarded to support our AI features have had the following materials reviewed and vetted by our security team:

* SOC 2 Type II or ISO 27001 report where available
* Customer-facing and internal policy documents
* Penetration test reports

We further review their corporate, application, and infrastructure security practices against curated criteria that we evaluate all of our onboarded vendors against. These details factor into our risk assessment and decision-making process into whether to incorporate them into our offering.