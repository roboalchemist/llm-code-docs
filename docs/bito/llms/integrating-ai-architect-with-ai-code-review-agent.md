# Source: https://docs.bito.ai/ai-architect/integrating-ai-architect-with-ai-code-review-agent.md

# Integrating AI Architect with AI Code Review Agent

Enhance your code reviews with deeper codebase intelligence by connecting Bito's [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) to [AI Architect](https://docs.bito.ai/ai-architect/overview). This integration enables significantly more accurate and context-aware reviews by leveraging the comprehensive knowledge graph that AI Architect builds from your codebase.

### What this integration provides

When AI Code Review Agent accesses AI Architect's knowledge graph, it gains a complete understanding of your codebase architecture — including microservices, modules, APIs, dependencies, and design patterns.

This enhanced context allows the AI Code Review Agent to:

* **Provide system-aware code reviews** - Understand how changes in one service or module impact other parts of your system
* **Catch architectural inconsistencies** - Identify when new code doesn't align with your established patterns and conventions
* **Detect cross-repository issues** - Spot problems that span multiple repositories or services
* **Deliver more accurate suggestions** - Generate fixes that are grounded in your actual codebase structure and usage patterns
* **Reduce false positives** - Better understand context to avoid flagging valid code as problematic

### Setup instructions

Follow these steps to connect AI Architect with AI Code Review Agent:

1. Log in to [**Bito Cloud**](https://alpha.bito.ai/home/welcome)
2. Open the [**AI Architect Settings**](https://alpha.bito.ai/home/ai-architect/settings?mode=self-hosted) dashboard.
3. In the **Server URL** field, enter your **Bito MCP URL**
4. In the **Auth token** field, enter your **Bito MCP Access Token**

### Need help?

Contact our team at [**support@bito.ai**](mailto:support@bito.ai) to request a trial. We'll help you configure the integration and get your team up and running quickly.
