# Source: https://docs.logrocket.com/docs/logrocket-galileo-ai-privacy-faq.md

# LogRocket Galileo AI Privacy & FAQ

LogRocket Galileo uses multiple AI models in tandem to generate relevant and actionable insights. LogRocket has taken numerous measures to ensure that customer and user data is kept safe at all times.

We make calls to OpenAI and Google’s API for certain Galileo functions. OpenAI and Google do not use data sent via its API to train their models, which our team has determined is a secure approach to keeping customer and user data safe. More information about how OpenAI treats data sent to its API can be found [here](https://openai.com/enterprise-privacy) and how Google treats data sent to their API [here](https://cloud.google.com/gemini/docs/discover/data-governance) .

# FAQ

**Does LogRocket comply with GDPR, CCPA, and other relevant data protection regulations?**

Yes, both we and our downstream providers (OpenAI, GCP) are [compliant with common data protection regulations](https://docs.logrocket.com/docs/gdpr).

**Does LogRocket use or plan to use customer information to improve and/or train future AI models?**

We use commercial off-the-shelf model providers with specific prompting techniques to yield accurate output. We don't currently train any models using customer data or have any plans to do so.

**Which AI models and services does LogRocket use? What types of AI model does LogRocket use?**

We have vendor relationships with both GCP and OpenAI and may use their commercial models, or open-source models, in the future. Most of the models used are LLMs or multimodal transformer models.

Please see additional details about the vendors we use in our Vendor Management Policy.

**What measures are in place to ensure the AI’s outputs are fair, unbiased, accurate, and truthful? How does LogRocket handle AI bias?**

OpenAI provides extensive safety documentation: [https://openai.com/safety](https://openai.com/safety)

We use AI to describe and summarize user experiences. We do not use AI to make recommendations on individuals. The potential for harm is minimal even with malicious inputs.

**Is there a possibility of LogRocket’s AI making uncontrolled or unsupervised decisions that could impact other systems or people?**

No.