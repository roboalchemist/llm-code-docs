# Source: https://docs.avaamo.com/user-guide/llamb/llamb-faqs.md

# LLaMB FAQs

This article lists a few frequently asked questions about LLaMB:

### 1. How is LLaMB different from existing Answer skills?

At the surface level, although, both (LLaMB and Answers skill) appear to leverage and tap into the existing knowledge base and deliver answers sourced from enterprise content; however, unlike Answers, LLaMB extends much beyond the mere ingestion and delivery of answers from enterprise content.

LLaMB is an exclusive product offering from `Atlas 8` onwards in the Avaamo Conversational AI Platform to harness the power of enterprise content coupled with Generative AI in your agents.&#x20;

It is a full stack, low code toolset to build, deploy, and maintain LLM ([Large Language Model](https://en.wikipedia.org/wiki/Large_language_model))   applications at enterprise scale.

Many key features in LLaMB help in generating inherently personalized and summarized results while maintaining the required level of security and compliance for enterprises. It is a practical and secure approach to deploying LLMs in the enterprise, thereby enhancing the knowledge search experience for both employees and customers. See [Overview - Key features](https://docs.avaamo.com/user-guide/llamb/overview-key-features), for more information.

### 2. How does LLaMB handle hallucinations with Generative responses?

No Hallucination!&#x20;

By carefully managing the content sources and documents provided to LLaMB, you can leverage the "best of both worlds" approach. This means that only verified content references are fed to LLaMB, resulting in accurate, trustworthy, and secure inferred answers.

### 3. How to trust the answers from LLaMB?

The primary concern when it comes to enterprise applications is "Trust and Security". Raw Model APIs when piped directly into the enterprise are very vulnerable. Moreover, these models are subject to adversarial attacks such as prompt injection.&#x20;

With LLaMB, you have complete and absolute ownership of the data. This means that you own and control what data is ingested to LLaMB and this internally controls how the responses are presented to the users. LLaMB uses only the content ingested to generate answers.&#x20;

### 4. How secure is my content in LLaMB?

With LLaMB, all the content you feed and the agent you build and deploy is via the Avaamo Conversational AI Platform. The platform combines enterprise-grade security features with rigorous compliance with industry standards to ensure your data is always protected and secure. See [Security at Avaamo](https://avaamo.ai/conversational-ai-security/) for more information on the compliances and security regulations list. The trust and security layer

### 5. Does LLaMB auto-learn from the previous responses?

No, each interaction is treated as an independent prompt, and the LLaMB doesn't retain information from prior messages in the conversation. The answers are "generated" implying that LLaMB does not engage in learning from your usage. This enables you to have complete ownership and control on the responses provided to the user.

### 6. How to migrate from Answers to LLaMB?

* Create an LLaMB skill. See [Create LLaMB skill](https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill), for more information.
* Ingest the required content. See [Ingest enterprise content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content), for more information.
* For bulk ingestion, you can leverage [Content Ingestion API](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis). You can also upload multiple documents at a time from the UI. See [Upload content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content), for more information.
* Disable the Answers skill
* Test with the LLaMB skill. See [Test agent](https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent), for more information.

### 7. Can Answers and LLaMB co-exist?

It is not recommended to have Answers and LLaMB skills both enabled in the same agent as the knowledge-base content between Answers and LLaMB can overlap. Overlapping the same knowledge content can lead to confusion and unpleasant user experience.&#x20;

### 8. What are the types of files I can load in LLaMB? <a href="#id-1.-what-are-the-types-of-files-i-can-load-in-the-answers-skill" id="id-1.-what-are-the-types-of-files-i-can-load-in-the-answers-skill"></a>

You can ingest the following types of documents in the `LLaMB Content` skill:

* URL - Publicly accessible HTML content
* CSV (Comma-separated values)
* Microsoft Word document (docx)
* Microsft Powerpoint (pptx)
* Microsoft Excel (xlsx)
* HTML documents (html)

See [Upload content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content), for more information.

### 9. Can LLaMB parse tables?

Yes, it can parse and generate summarized, coherent, and contextually appropriate responses. See [Rich Rendering of Tabular Content](https://docs.avaamo.com/user-guide/overview-key-features#rich-rendering-of-tabular-content), for more information.&#x20;

### 10. What languages are supported in LLaMB? <a href="#id-1.-what-are-the-types-of-files-i-can-load-in-the-answers-skill" id="id-1.-what-are-the-types-of-files-i-can-load-in-the-answers-skill"></a>

Currently, you can ingest content only in the en-US language in the `LLaMB Content skill`. However, user inputs and agent responses can be in multiple languages. Refer [Supported language](https://docs.avaamo.com/user-guide/before-you-begin#id-4.-supported-language), for more information.

### 11. What should I do when the Generation quota is reached?

Contact Avaamo Support, for immediate assistance. It is recommended to contact Avaamo Support when the generation quota hits 75% of usage for prompt action. See [Usage analytics](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.

### 12. How long are the responses Cached?

For faster results and better efficiency, the responses generated by LLaMB are cached. Once a response is cached, it is always available for future use as per the [data retention policy ](https://docs.avaamo.com/user-guide/ref/data-retention)and not deleted from the cache until then. This helps in optimizing the generation cost. See [Usage analytics](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.

### 13. Can I configure cached response duration?

Currently, Once a response is cached, it is always available for future use as per the [data retention policy ](https://docs.avaamo.com/user-guide/ref/data-retention)and not deleted from the cache until then.&#x20;

### 14. Is there any limit on the number of URLs or PDF sizes? <a href="#id-2.-is-there-any-limit-on-the-number-of-urls-or-pdf-sizes" id="id-2.-is-there-any-limit-on-the-number-of-urls-or-pdf-sizes"></a>

There is no limit on the number of URLs that can be uploaded using the `LLaMB Content` skill. Further, you can upload multiple PDF documents and each PDF document can be more than 1000 pages. See [Upload Content](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content), for more information.

### 15. Will LLaMB search text present on images? <a href="#id-7.-will-answers-search-text-present-on-images" id="id-7.-will-answers-search-text-present-on-images"></a>

No. Currently, this feature is not supported.

### 16. How to improve the user experience with LLaMB ? <a href="#id-10.-how-to-improve-the-accuracy-of-the-answers-skill" id="id-10.-how-to-improve-the-accuracy-of-the-answers-skill"></a>

&#x20;Currently, there are two primary ways to analyze the user experience and further improve your agent:

* [Using user feedback ](https://docs.avaamo.com/user-guide/improve-user-experience-feedback-analytics#user-feedback)
* [Using Analytics](https://docs.avaamo.com/user-guide/improve-user-experience-feedback-analytics#insights-from-analytics)

### 17. Can I extract Usage analytics data from any API? <a href="#id-10.-how-to-improve-the-accuracy-of-the-answers-skill" id="id-10.-how-to-improve-the-accuracy-of-the-answers-skill"></a>

Currently, there is no API available to extract Usage analytics data. See [Usage](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage), for more information.

### 21. Can LLaMB perform computation operations? <a href="#id-10.-how-to-improve-the-accuracy-of-the-answers-skill" id="id-10.-how-to-improve-the-accuracy-of-the-answers-skill"></a>

&#x20;Currently, there is no support for any computation operations in LLaMB.&#x20;

### 22. Can you test LLaMB using Regression testing? <a href="#id-10.-how-to-improve-the-accuracy-of-the-answers-skill" id="id-10.-how-to-improve-the-accuracy-of-the-answers-skill"></a>

Yes, You can test LLaMB content using Regression testing. Refer [Regression Testing](https://docs.avaamo.com/user-guide/llamb/regression-testing), for more information.

### 23. What channels can LLaMB be deployed on? <a href="#id-10.-how-to-improve-the-accuracy-of-the-answers-skill" id="id-10.-how-to-improve-the-accuracy-of-the-answers-skill"></a>

LLaMB can be deployed in the following channels:

* [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel)
* [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps)
* [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps)&#x20;
* [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams)

**24. Are there any elements always shown in English, irrespective of the user’s language?**\
Yes. The following elements are expected to appear in English, regardless of the user’s language settings:

* Acronyms
* Digits
* Document name
* Citation links
