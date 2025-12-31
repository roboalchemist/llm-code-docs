# Source: https://docs.bito.ai/ai-code-reviews-in-git/chat-with-ai-code-review-agent.md

# Chat with AI Code Review Agent

Ask questions directly to the AI Code Review Agent regarding its code review feedback. You can inquire about highlighted issues, request alternative solutions, or seek clarifications on suggested fixes.

Real-time collaboration with the AI Code Review Agent accelerates your development cycle. By delivering immediate, actionable insights, it eliminates the delays typically experienced with human reviews. Developers can engage directly with the Agent to clarify recommendations on the spot, ensuring that any issues are addressed swiftly and accurately.

Bito supports over 20 languages—including English, Hindi, Chinese, and Spanish—so you can interact with the AI in the language you’re most comfortable with.

## How to chat?

To start a conversation, type your question directly as a reply to the Agent’s code review comment.&#x20;

The AI Code Review Agent will **analyze your comment and determine** if it’s a valid and relevant question.&#x20;

* If the agent decides it’s a valid question, it will respond with helpful insights.
* If the agent determines it’s unclear, off-topic, or not related to its feedback, it will **not respond**.

To help the agent recognize your question faster, you can also **tag your comment** with **@bitoagent** or **@askbito**. Tagging informs the Agent that your message is intended as a question. However, **tagging does not guarantee a reply**. The agent will still **analyze your comment and decide** whether it is a valid question worth responding to.

Bito usually responds within about 10 seconds.

* On **GitHub** and **Bitbucket**, you may need to manually refresh the page to see the response.
* On **GitLab**, updates happen automatically.

{% hint style="info" %}
**Note:** The AI Code Review Agent will only respond to questions posted as a reply to its own comments.\
It will not reply to questions added on threads that it didn’t start.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhvDrQ1DMSqIECpvjdstX%2Fscrnli_fUCdzJyMPFpLu9_2.jpg?alt=media&#x26;token=89b64664-0bea-4835-afba-5e85372338d2" alt="" width="563"><figcaption></figcaption></figure>

### What you can ask about

When chatting with the AI Code Review Agent, you can ask questions to better understand or improve the code feedback it provided. Here are examples of what you can ask:

* **Clarifications about a highlighted issue**\
  Ask the AI to explain why it flagged a certain line of code or why something might cause a problem.
* **Request for alternative solutions**\
  Request different ways to fix or improve the code beyond what was originally suggested.
* **Deeper explanations**\
  If you want to understand the technical reasoning behind a suggestion (e.g., security concerns, performance impacts, best practices), you can ask for more detailed explanations.
* **Request for examples**\
  Ask the AI to provide an example snippet showing the corrected or improved code.
* **Trade-off discussions**\
  Ask the AI about pros and cons of different approaches it may have suggested (e.g., performance vs. readability).
* **Best practices guidance**\
  Request advice on best practices related to the specific code snippet — such as naming conventions, error handling, optimization tips, or design patterns.
* **Language-specific advice**\
  If you’re working in a particular language (e.g., JavaScript, Python, Java), you can ask for language-specific guidance related to the comment.
* **Request for more context**\
  If the suggestion feels too "short" or "surface level," you can ask the AI to explain more about the broader coding or architectural concept behind its feedback.
* **Security and safety questions**\
  If a suggestion touches on security (like input validation, authentication, or encryption), you can ask for further security-related advice.
* **Testing and validation**\
  Ask the AI if it recommends writing any tests based on its code suggestions and what those tests might look like.

{% hint style="info" %}
**Tip:** Feel free to ask your question in your preferred language! Bito supports over 20 languages, including English, Hindi, Chinese, and Spanish.
{% endhint %}

### What you cannot ask about

The AI can only answer questions related to its **own code review comments**.

* **You cannot** ask general questions about the repository or unrelated topics.
* **You cannot** start a new thread independently — your question must be a reply to a comment made by Bito’s AI Code Review Agent.

If your comment is not linked to a Bito review comment, the AI will **not respond**.
