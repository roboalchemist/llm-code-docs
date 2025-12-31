# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/how-it-works.md

# How it Works?

{% embed url="<https://www.youtube.com/watch?v=RXMIkgozmwc>" %}

When you open a project in Visual Studio Code or JetBrains IDEs, Bito lets you enable the [**indexing**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of code files from that project’s folder. Basically, this indexing mechanism leverages our new [**AI Stack**](https://docs.bito.ai/help/bitos-ai-stack) that enables Bito to understand your entire codebase and answer any questions regarding it.&#x20;

The index is stored locally on your system to provide better performance while maintaining the security/privacy of your private code.

{% hint style="info" %}
It takes 12 minutes per each 10MB of code to understand your repo, as the index is being built locally.
{% endhint %}

## How to Ask Questions?

Once indexing is complete, you can ask any question in the Bito chatbox. Bito uses AI to determine if you are asking about something in your codebase. If Bito is confident, it grabs the relevant parts of your code from our [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) and feeds them to the [**Large Language Models (LLMs)**](https://docs.bito.ai/help/bitos-ai-stack/large-language-models-llm) for accurate answers. But if it's unsure, Bito will ask you to confirm before proceeding.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fum9m2Les997qz8ivTDLg%2Fscrnli_3_28_2024_7-05-52%20AM.png?alt=media&#x26;token=415c22f8-e92a-4fdf-bd79-b1affca7cdc5" alt=""><figcaption></figcaption></figure>

In case you ask a general question (not related to your codebase), then Bito will directly send your request to our LLM without first looking for the appropriate local context.

However, if you want to ask a question about your code no matter what, then you can use specific keywords such as **"my code", "my repo", "my project", "my workspace"**, etc., in your question.

The complete list of these keywords is given on our [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.

Once Bito sees any input containing these keywords, it will use the index to identify relevant portions of code or content in your folder and use it for processing your question, query, or task.

## Security of your code&#x20;

As usual, security is top of mind at Bito, especially when it comes to your code.  A fundamental approach we have taken is to keep all code on your machine, and not store any code, code snippets, indexes, or [**embedding vectors**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) on Bito’s servers or our API partners. All code remains on your machine, Bito does not store it. In addition, none of your code is used for AI model training.&#x20;

Learn more about [**Bito’s Privacy and Security Practices**](https://docs.bito.ai/privacy-and-security).&#x20;
