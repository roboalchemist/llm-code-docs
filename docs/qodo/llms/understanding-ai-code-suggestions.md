# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/learn-more/understanding-ai-code-suggestions.md

# Understanding AI Code Suggestions

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

### **AI Limitations**

AI models for code are getting better and better, but they are not flawless. Not all the suggestions will be perfect, and a user should not accept all of them automatically. Critical reading and judgment are required. Mistakes of the AI are rare but can happen, and it is usually quite easy for a human to spot them.

### **Purpose of Suggestions**

* **Self-reflection:** The suggestions aim to enable developers to *self-reflect* and improve their pull requests. This process can help to identify blind spots, uncover missed edge cases, and enhance code readability and coherency. Even when a specific code suggestion isn't suitable, the underlying issue it highlights often reveals something important that might deserve attention.
* **Bug detection:** The suggestions also alert on any *critical bugs* that may have been identified during the analysis. This provides an additional safety net to catch potential issues before they make it into production. It's perfectly acceptable to implement only the suggestions you find valuable for your specific context.
* **Hierarchy:** Presenting the suggestions in a structured hierarchical table enables the user to *quickly* understand them, and to decide which ones are relevant and which are not.
* **Customization:** To guide the model to suggestions that are more relevant to the specific needs of your project, we recommend to use the [`extra_instructions`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file) and [`best practices`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices) fields.
* **Interactive usage:** The interactive [PR chat](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/integrations/chrome-extension) also provides an easy way to get more tailored suggestions and feedback from the AI model.
