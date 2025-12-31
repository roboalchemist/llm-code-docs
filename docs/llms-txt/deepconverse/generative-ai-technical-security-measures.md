# Source: https://docs.deepconverse.com/product-docs/security/generative-ai-technical-security-measures.md

# Generative AI - Technical Security Measures

{% hint style="info" %}
This document applies to our Generative AI features used in the platform
{% endhint %}

The following document builds on the technical and organizational security measures that are in place and addresses specific questions relating to use of Generative AI in our products:

### Data Processors

DeepConverse has a process for vetting data processors to ensure that any customer data that is processed by an external entity adheres to the standards of maintaining data security and privacy. We make use of the following platforms to serve Generative AI models.

* Azure OpenAI
* AWS&#x20;
* Google Cloud (Future)

#### Azure Open AI

* Azure data centers are located in the US
* GPT-3.5 & GPT-4 used dependent on use cases
* Safeguards in place
  * Data is not used to train other models
  * Compliance in place ([Azure Trust Center](https://www.microsoft.com/en-us/trust-center/product-overview))
  * Retention
    * Microsoft may store data for up to 30 days to detect abuse. DeepConverse is currently in the process of adding an option to reduce this time as well.
* Difference between OpenAI and Azure OpenAI

Azure OpenAI is a fully managed service offered by Microsoft Azure. It comes with SLAs, security and reliability to support enterprise use cases.\ <br>

| <p><br></p>            | ChatGPT WebApp      | Microsoft Azure OpenAI ChatGPT APIs |
| ---------------------- | ------------------- | ----------------------------------- |
| Access method          | WebApp / IPhone App | API only                            |
| Data retention         | Undefined           | 30 days for Moderation only         |
| Data used for Training | Yes                 | No                                  |
| Control over PII data  | None                | PII can be filtered out             |

\
Data Flow diagram for Azure OpenAI

<figure><img src="https://lh5.googleusercontent.com/h1vda7GSKjSfTeIED2ICbrVZymrNVVwop3qAhaqdXFcAtdiIaL4nOyrisiOboqbTJ9propD7r5Zf-p3Pwz6OhkZGZcgXgr3AQb7QF2qq1u5z7B0Oqz9cSD5nwvzdP-EkON25qZabHhlk2jS-jNkVS9g" alt=""><figcaption></figcaption></figure>

### PII and PHI Handling

DeepConverse does not make use of PII to provide answers and capabilities in the platform. PII and PHI are removed from the information being sent to Generative models.&#x20;

* PII is retained only till needed for the conversation, for:
  * Case creation
  * API lookups that need PII
    * Configurable duration
    * Minimum 15 days\ <br>
* Post Conversation
  * PII is removed
  * Non-PII Data is retained for analytics and DeepConverse model improvement\ <br>
* PII Processed for Flow Execution
  * User messages
  * Problem Specification:
* PII (mostly during case creation)
  * Name
  * Email
  * Zip code, Order Number etc

### Hallucinations

Generative AI models due to their generative nature can hallucinate i.e. give textual output that is most probable based on the input being provided. The models are outputting the content word by word on the likelihood of it being most probable.&#x20;

* DeepConverse makes use of Retrieval Augmented Question Answering to provide ground truth data to the models and reason out the answer. This approach reduces the risk of hallucination as we do not allow the model to use its memory.&#x20;
* DeepConverse also checks for sources of the information being generated. If we cannot determine the source we understand that the likelihood of the content being a hallucination is higher.
* We make us of reasoning capabilities of LLMs to reduce hallucinations&#x20;
* All Generative AI actions are logged and available for review for our team to identify potential hallucinations and place more safeguards as we iterate on improving the models.

<br>
