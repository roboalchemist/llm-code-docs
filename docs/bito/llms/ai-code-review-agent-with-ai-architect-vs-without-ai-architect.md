# Source: https://docs.bito.ai/ai-architect/ai-code-review-agent-with-ai-architect-vs-without-ai-architect.md

# AI Code Review Agent (with AI Architect vs without AI Architect)

The [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) becomes significantly more powerful when paired with [**AI Architect**](https://docs.bito.ai/ai-architect/overview).

Below is a clear explanation of how the agent behaves in each setup and why AI Architect unlocks much deeper, system-level insights.

## AI Code Review Agent without AI Architect

The standard AI Code Review Agent analyzes code at the **repository level**.

It creates a ***within-repo knowledge graph*** by building:

* Abstract Syntax Trees (ASTs)
* Symbol indexes
* Local dependency relationships

This allows it to perform strong, context-aware code reviews **within a single repository**, including:

* Identifying issues in the diff
* Understanding dependencies inside the repo
* Checking for consistency and correctness within that project
* Suggesting improvements based on local patterns

However, the agent’s visibility stops at the repository boundary. It cannot detect effects on other services or codebases.

## AI Code Review Agent powered by AI Architect

When **AI Architect** is enabled, the **AI Code Review Agent** gains a **complete view of your entire engineering ecosystem**.

AI Architect builds a **cross-repository knowledge graph** that maps:

* All services
* Shared libraries
* Modules and components
* Inter-service dependencies
* Upstream and downstream call chains

With this system-level understanding, the agent can perform much deeper analysis.

#### **Key capabilities unlocked by AI Architect**

**1. Cross-repository awareness**

The agent understands how code in one repo interacts with code in others — crucial for microservices and distributed systems.

**2. Cross-repo impact analysis**

During a pull request review, the agent can identify:

* What breaks downstream if you change an interface
* Which services call the function you updated
* Which teams or repos depend on your changes
* Whether the update introduces architecture-wide risks

**3. Architecture-level checks**

The agent evaluates your changes not just for correctness, but for their alignment with the overall system design.

**4. Early problem detection across the entire codebase**

Ripple effects, breaking changes, or dependency violations that traditionally appear only in staging or after deployment can now be flagged directly during review.

***

### **Side-by-side comparison**

| Capability                  | Without AI Architect | With AI Architect                 |
| --------------------------- | -------------------- | --------------------------------- |
| Scope                       | Single repository    | Entire system (multi-repo)        |
| Knowledge graph             | Repo-only            | Cross-repository, system-wide     |
| AST + symbol analysis       | ✅                    | ✅ (plus cross-repo linking)       |
| Dependency visibility       | Local to repo        | Full call chains across repos     |
| Impact analysis             | Local only           | Upstream + downstream, multi-repo |
| Architecture checks         | Limited              | System-level validation           |
| Ripple-effect detection     | ❌                    | ✅                                 |
| Multi-service understanding | ❌                    | ✅                                 |
