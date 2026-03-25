# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/faq.md

# FAQ

## Qodo Context Engine – Frequently Asked Questions

<details>

<summary>What is Qodo Context Engine?</summary>

Qodo Context Engine is the code intelligence engine behind the Qodo platform. It connects to your organization’s codebase, understands your architecture, and powers advanced AI agents to help you reason about code, systems, and dependencies.

</details>

<details>

<summary>What does Qodo Context Engine actually do?</summary>

Qodo Context Engine builds a deep understanding of your codebase:

* It **indexes code** across all your repositories, creating a structural and semantic map.
* It powers agents like **Ask Agent** and **Deep Research Agent** to provide context-aware help.
* It enables smarter answers in products like **Qodo Gen**, **Qodo Merge**, and external tools via **MCP**.

Think of it as an AI engineer that’s read all your code—and can explain it back to you, reason through changes, or surface important relationships.

</details>

<details>

<summary>Where can I use Qodo Context Engine?</summary>

Qodo Context Engine is available across the Qodo platform:

* **Qodo IDE plugin**: Brings codebase-wide understanding into your IDE.
* **Qodo Git plugin**: Enhances review, implement, and ask workflows with full-repo context.
* **As an MCP**: Can be integrated into **any tool that supports MCPs**.

</details>

<details>

<summary>What’s the difference between Ask Agent and Deep Research Agent?</summary>

| Agent                   | Best For                     | Strengths                          |
| ----------------------- | ---------------------------- | ---------------------------------- |
| **Ask Agent**           | Quick, scoped Q\&A           | Fast, grounded, context-aware      |
| **Deep Research Agent** | Complex, cross-repo analysis | Multi-step reasoning, deep insight |

Use **Ask** when you need quick understanding. Use **Deep Research** when you're planning refactors, architectural changes, or debugging across systems.

</details>

<details>

<summary>What kinds of questions can I ask Qodo Context Engine?</summary>

Some common examples:

* “Where is this function used across our repos?”
* “If I change this API response format, what breaks?”
* “How does session management work end-to-end?”
* “What services call this shared utility?”

Qodo Context Engine understands usage patterns, dependencies, and architectural intent—it’s more than just code search.

</details>

<details>

<summary>Is my code secure?</summary>

Yes. Qodo Context Engine only accesses the codebases you explicitly connect and tag. Data is handled in compliance with enterprise security standards, and never shared outside your organization.

</details>

<details>

<summary>How does this compare to AI code assistants?</summary>

Most assistants understand a file. Qodo Context Engine understands your **entire system**.\
It goes beyond autocomplete and one-off completions to help you:

* Understand how things work
* Refactor safely
* Make changes with full context

</details>

<details>

<summary>Why not just use RAG?</summary>

Traditional RAG systems retrieve a few snippets and then reason only over those. If the right context wasn’t pulled at the start, the answer can miss the mark.

Qodo Context Engine takes this further. It doesn’t just retrieve code — it **deeply indexes your entire codebase** (across thousands of repos and years of history) and applies **agentic reasoning** on top. That means:

* **Smarter retrieval**: Not just nearby code, but the right functions, commits, discussions, and docs.
* **Multi-agent reasoning**: Analyzes dependencies, intent, and tradeoffs like a senior engineer would.
* **Full-system view**: Scales to whole architectures, not just isolated files.

The result is an assistant that can handle both quick “what does this function do?” lookups and complex “what breaks if we refactor this?” research — without getting stuck on the wrong context.

</details>
