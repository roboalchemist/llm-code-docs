# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/how-does-bito-understand-my-code.md

# How does Bito Understand My Code?

Bito deploys a [**Vector Database**](https://docs.bito.ai/help/bitos-ai-stack/vector-databases) locally on the user’s machine, bundled as part of the Bito IDE plug-in. This database uses [**Embeddings**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) (a vector with over 1,000 dimensions) to retrieve text, function names, objects, etc. from the codebase and then transform them into multi-dimensional vector space.&#x20;

Then when you give it a function name or ask it a question, that query is converted into a vector and is compared to other vectors nearby. This returns the relevant search results. So, it's a way to perform search not on keywords, but on meaning. Vector Databases are able to do this kind of search very quickly.

{% hint style="info" %}
Learn more about [**how Bito indexes your code**](https://docs.bito.ai/help/bitos-ai-stack/indexing) so that it can understand it.
{% endhint %}

Bito also uses an **Agent Selection Framework** that acts like an autonomous entity capable of perceiving its environment, making decisions, and taking actions to achieve certain goals. It figures out if it’s necessary to do an embeddings comparison on your codebase, do we need to perform an action against Jira, or do we do something else.&#x20;

Finally, Bito utilizes [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) from Open AI, Anthropic, and others that actually provide the answer to the question by leveraging the context provided by the Agent Selection Framework and the embeddings.&#x20;

This is what makes us stand out from other AI tools like ChatGPT, GitHub Copilot, etc. that do not understand your entire codebase.&#x20;

We’re making significant innovations in our [**AI Stack**](https://docs.bito.ai/help/bitos-ai-stack) to simplify coding for everyone. To learn more about this head over to [**Bito’s AI Stack documentation**](https://docs.bito.ai/help/bitos-ai-stack).
