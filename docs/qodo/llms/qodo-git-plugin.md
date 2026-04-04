# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/products-integrations/qodo-git-plugin.md

# Qodo Git plugin

{% hint style="success" %}
This article explains how to use Qodo Context Engine in Qodo Git plugi&#x6E;**.**

For a deeper dive on Qodo Git plugin, [**visit the dedicated Qodo Git plugin documentation portal**](https://docs.qodo.ai/qodo-documentation/qodo-merge)**.**
{% endhint %}

Qodo Context Engine integrates with Qodo Git plugin, giving your code review, implementation, and PR workflows deep, codebase-level intelligence.

It brings architectural understanding and full-repo context directly into your dev workflow, so every suggestion, insight, or generated change is grounded in how your system actually works.

### Why It Matters

Most pull request tools operate in a vacuum, limited to the diff or a single repo.

Qodo Context Engine opens the entire codebase to your merge workflow, making reviews smarter, implementations more reliable, and questions easier to answer.

***

### What This Enables

* **Smarter Reviews** with `/review`\
  Qodo Context Engine analyzes the PR in the context of your broader codebase.\
  The **Focus** section surfaces relevant context and architectural feedback.\
  The **References** section shows exactly which files or services influenced the feedback.
* **More Informed Implementations** with `/implement`\
  When generating code, Qodo Context Engine provides full-repo awareness—so suggestions align with your existing patterns, logic, and structure.\
  The **References** section shows which parts of the codebase informed the output.
* **Deeper Answers** with `/ask`\
  Go beyond the PR scope. Ask architectural or cross-repo questions, and get grounded answers based on the broader system—not just the current branch.
* Duplication Management with `/compliance`\
  The Compliance tool offers the *Codebase Code Duplication Compliance* section which contains feedback based on the RAG references. This section highlights possible code duplication issues in the PR, providing developers with insights into potential code quality concerns.

***

### How to Enable It

In your Qodo Git plugin configuration file, add:

```toml
enable_rag=true
```

***

### Get Started

To learn more and explore advanced options,  [see the full Qodo Context Engine in Qodo Git plugin documentation](https://qodo-merge-docs.qodo.ai/core-abilities/rag_context_enrichment/).
