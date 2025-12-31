# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.0/introducing-llamb.md

# Introducing LLaMB

The Avaamo Conversational AI Platform introduces a new product **`LLaMB - Large Language Model for Business`** in the `Atlas 8` release.

LLaMB is a new low-code framework for building powerful end-user generative AI agents in the enterprise safely, securely, and fast. LLaMB provides tools to eliminate hallucinations, integrate enterprise systems, and support any LLM ([Large Language Model](https://en.wikipedia.org/wiki/Large_language_model)) of your choice.

It utilizes LLM technology to offer inherently personalized and summarized results while maintaining the required level of security and compliance for enterprises. It is a practical and secure approach to deploying LLMs in the enterprise, thereby enhancing the knowledge search experience for both employees and customers.

Here's a quick sneak peek at LLaMB:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPRDS95k5pMVECaQPCweP%2F8.0-LLaMB.gif?alt=media&#x26;token=bcc50d02-4533-43dd-b891-ddbd75452d51" alt=""><figcaption></figcaption></figure>

This article outlines the key features of LLaMB and the next steps to leverage LLaMB product offering in the Avaamo Conversational AI Platform.&#x20;

{% hint style="info" %}
**Note**: LLaMB is enabled on demand. Contact your dedicated Customer Success Manager for further assistance.
{% endhint %}

## Key features

### Conversation completeness - Full Sentences and Complete Answers

The LLaMB responses are precise and complete sentences, a similar answer you might expect when communicating with another person in a regular conversation. The responses are not limited to simple one-word responses but can include detailed explanations, descriptions, or discussions, depending on the complexity of the question. It makes your agent more intuitive and user-friendly, simulating human-like interactions.

The following is an illustration to depict how LLaMB can generate natural language answers, close to a human conversation:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FozhGuhueINAlaoHaiyHO%2Fimage.png?alt=media\&token=66d40259-4e04-4a4f-be2f-8cd4831024d9)

* **Natural input:** Users can input queries, commands, or prompts in a conversational style, using natural language rather than adhering to a specific syntax or format. Similarly, LLaMB can understand the context of the conversation and provide complete answers in a way that mirrors natural human conversation.
* **Auto-waiting message:** While LLaMB is waiting to gather and collect information from verified sources, it informs users on the same and engages users in a conversation that feels comfortable and familiar.
* **Generated precise answer:** LLaMB excels in providing precise and context-specific answer summarization and comprehension. Leveraging on the vast amount of data that is already ingested and trained in the knowledge base, LLaMB can understand and grasp the meaning of the input provided to it and generate appropriate and relevant summarized responses.&#x20;
* **Source attribution**: All responses from LLaMB are provided with a source reference, indicating precisely the source from which the answers are derived. This means that only verified content references fed to LLaMB are used for providing responses, resulting in accurate, trustworthy, and secure inferred answers.

### Rich Rendering of Tabular Content

LLaMB provides the capability to comprehend information within intricate tables, deducing responses to user queries directly from the table's content. Unlike merely identifying and highlighting answers within the table, LLaMB goes beyond interpreting the user's query, extracting pertinent information, and providing a summarized response. This nuanced approach ensures that LLaMB not only locates answers within the table but also comprehends the user's query contextually, delivering a concise summary of the relevant information.

The following is an illustration to depict how LLaMB can generate nuanced city/role-based answers from tabular content:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fi1fXOrgulOQOJ2f0GgFC%2Fimage.png?alt=media&#x26;token=6fb2f916-9cf5-43a8-bbee-5036ce6c478b" alt=""><figcaption></figcaption></figure>

* Each response from the LLaMB content includes a link to `in-line source` from where the response is derived.
* LLaMB can auto-parse complex source tables.
* No configuration or training is required to parse tables in LLaMB.

### Fluid conversations - Natural language answers

"Fluid conversations" is a phrase to describe a conversation that flows easily and naturally. LLaMB generates natural language answers to user queries that are coherent, contextually appropriate, and that is easily understandable by a person. LLaMB engages users in dialogue that closely mimics human conversation, hence enhancing user experience by making interactions more intuitive and enjoyable.

The following is an illustration to depict how LLaMB can generate natural language answers, close to a human conversation:&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FnK5howX1QR4tOxklbA69%2Fimage.png?alt=media\&token=583c9e08-f3ce-477a-a867-226f6f2c2f0c)

* **Coreference resolution:** LLaMB can identify and link expressions in a text that refer to the same entity in a multi-turn conversation, hence, the responses are more accurate and coherent allowing the conversation to flow naturally.&#x20;
* **Human-like conversation**: LLaMB responses are not limited to simple one-word responses but can include detailed explanations, descriptions, or discussions, depending on the complexity of the question. It makes your agent more intuitive and user-friendly, simulating human-like interactions.
* **Deep semantic understanding**: LLaMB can comprehend the meaning of language beyond surface-level syntax by understanding the context, and relationships between words, and grasping the nuances of language semantics.
* **Conversational memory**: LLaMB can remember and maintain context throughout a conversation. This enables the system to understand references, callbacks, and evolving topics within the dialogue.

### Trust and Secure

LLM APIs are readily available for everyone's use. The primary concern when it comes to enterprise applications is "Trust and Security". Raw Model LLM APIs when piped directly into the enterprise are vulnerable to adversarial attacks.

LLaMB comes with all the key building blocks required to build and deploy enterprise LLM applications safely and securely. The following are key focus areas that help in building trust and security within enterprises when using LLaMB:

**Ownership and Control**: With LLaMB, you have the complete and absolute ownership of the data. This means that you own and control what data is ingested to LLaMB and this internally controls how the responses are presented to the users. LLaMB uses only the content ingested to generate answers. The answers are "generated" implying that LLaMB does not engage in learning from your usage. Each interaction is treated as an independent prompt, and the LLaMB doesn't retain information from prior messages in the conversation.

**Security**: With LLaMB, all the content you feed and the agent you build and deploy is via the Avaamo Conversational AI Platform. The platform combines enterprise-grade security features with rigorous compliance with industry standards to ensure your data is always protected and secure. See [Security at Avaamo](https://avaamo.ai/conversational-ai-security/) for more information on the compliances and security regulations list. The trust and security layer.

### Easy ingestion pipeline: No more parsing templates!

LLaMB can process PDF files seamlessly, eliminating the need for any preprocessing or parsing templates. For HTML content, the requirement for parsing templates has been drastically simplified.

This implies that the sole prerequisite before utilizing LLaMB is to have the content readily available. Once the content is prepared, the straightforward process involves enabling LLaMB, ingesting the content, and witnessing the seamless transformation without any additional complexities.

The following is an illustration to depict how LLaMB can generate nuanced city/role-based answers from multiple tabular content:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWUVf9dB2nE37NjEJ7j8r%2Fimage.png?alt=media&#x26;token=792db0c1-965a-4841-a610-7cc79747afe7" alt=""><figcaption></figcaption></figure>

* **Multi-source summarization**: LLaMB can infer and summarize the content from multiple sources, say, for example, from multiple tables by understanding the context of the user's query, infer, and summarize precisely with appropriate contextual responses.
* **Deep coreference resolution:** LLaMB can map context and co-reference from multiple sources based on the context in the user's query, summarize the results, and provide a comprehensive response to the user.
* LLaMB can parse complex tables without the need for any pre-processing utility&#x20;
* **Multiple source attribution**:  All responses from LLaMB are provided with a source reference, indicating precisely the source from which the answers are derived. If multiple sources of content are used for inferring answers, then multiple source attribution is provided. This means that only verified content references fed to LLaMB are used for providing responses, resulting in accurate, trustworthy, and secure inferred answers.

See [Parsing templates](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/parsing-templates), for more information.

### Soft unhandled (Active redirect)

LLaMB provides the capability to gracefully redirect users when faced with unhandled responses, a feature known as `Soft Unhandled`.&#x20;

In instances where the agent fails to comprehend a user query, it defaults to an unhandled intent response, stating, "*I am sorry. I don't have an answer for that.*" The `Soft Unhandled` feature maintains the acknowledgment of the agent's inability to provide an answer but does so with a courteous and polished response. This feature aims to enhance user interaction by:

* Creating a pleasant user experience during interactions.&#x20;
* Establishing a soft and reassuring tone in the agent's response.
* Conveying the impression that, although unable to address certain queries, the agent is still actively assisting with those it can answer.

|                                                                                                    Soft Unhandled                                                                                                   |                                                                                                      Unhandled                                                                                                      |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7LvpKk9x6XAxq7EMzKta%2Fimage.png?alt=media\&token=2ed81bd5-b35f-4ebe-8911-921c0b7ef2a0) | ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FgVsuWrJHNvwsBcwhTkmH%2Fimage.png?alt=media\&token=e72b5db7-6f28-4d7f-a166-11c687a469c9) |

See [Soft unhandled](https://docs.avaamo.com/user-guide/llamb/soft-unhandled-active-redirect), for more information.

## Next steps

1. Start by understanding [key terms](https://docs.avaamo.com/user-guide/llamb/key-terms) in the LLaMB product.
2. Understand what is required in the [Before you begin](https://docs.avaamo.com/user-guide/llamb/before-you-begin) section.
3. You are now ready to [get started](https://docs.avaamo.com/user-guide/llamb/get-started) by exploring LLaMB in the Avaamo Conversational AI Platform.
