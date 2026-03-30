# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/capabilities/deep-research.md

# /deep-research

The `deep_research` endpoint is an intelligent code analysis agent that goes beyond simple search to provide comprehensive understanding of your codebase. Think of it as having a senior architect who has thoroughly studied every line of your code and can answer complex questions about architecture, patterns, and implementation strategies.<br>

**Key Features:**

* **Code Understanding**: Comprehends code logic, architecture, and design patterns.
* **Cross-Repository Analysis**: Can analyze relationships between different parts of your codebase.
* **Implementation Planning**: Helps plan new features based on existing code patterns.
* **Best Practice Recommendations**: Suggests improvements based on codebase analysis.
* **Architecture Insights**: Provides high-level understanding of system design.

***

### API/MCP Reference

#### Request Format

```json
{
  "tool": "deep_research",
  "parameters": {
    "input": "How does the authentication flow work across our microservices? What security measures are in place?",
    "repositories": ["backend/api", "frontend/app"],  // Repos to analyze
    "session_id": "analysis-123"                      // Track conversation context
  }
}
```

#### Parameters

<table><thead><tr><th width="139.515625">Parameter</th><th width="93.83984375">Type</th><th width="113.328125">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>input</code></td><td>string</td><td>Yes</td><td>Your question or research query. Be specific and detailed for best results.</td></tr><tr><td><code>repositories</code></td><td>array</td><td>No</td><td>List of repository identifiers to scope the search. Format: <code>org/repo</code> </td></tr><tr><td><code>session_id</code></td><td>string</td><td>No</td><td>Unique identifier to maintain context across multiple queries in a conversation.</td></tr></tbody></table>

***

### Best Practices

#### :rocket: Recommended Query Strategies

* **Be specific and detailed** - "How does user authentication work across our microservices?" provides richer insights than general queries
* **Include context about your goals** - Mentioning why you need the information helps Deep Research tailor its analysis
* **Leverage session\_id for complex investigations** - Build on previous queries to dive deeper into specific areas
* **Specify repositories for focused analysis** - When you know which repos are relevant, include them for more targeted results
* **Ask 'why' and 'how' questions** - Deep Research excels at explaining design decisions and implementation reasoning

#### :imp: Avoid

* Asking for simple keyword searches, use `get_context` instead
* Asking the agent to modify your code, deep-research analyzes, and suggest code, it will not modify files
* Asking about external services not in your codebase\s
* Don't use for real-time data - it analyzes code structure, not runtime behavior

***

<details>

<summary>Usage Patterns</summary>

#### Pattern 1: Architecture Discovery

**When to use**: Understanding how your system works

```json
{
  "input": "Explain our payment processing architecture. How do orders flow from the frontend through our services to the payment gateway?",
  "repositories": ["acme/frontend", "acme/api-gateway", "acme/payment-service"]
}
```

**Returns**: Complete flow diagram in text, service interactions, data transformations, error handling paths

#### Pattern 2: Security Audit

**When to use**: Evaluating security implementation

```json
{
  "input": "Analyze our JWT authentication implementation. Are we following security best practices? What vulnerabilities might exist?",
  "repositories": ["acme/auth-service", "acme/api-gateway"]
}
```

**Returns**: Security analysis, best practice violations, specific vulnerabilities, improvement recommendations

#### Pattern 3: Feature Planning

**When to use**: Before implementing new features

```json
{
  "input": "We need to add real-time notifications. Based on our current architecture, where should this be implemented and what patterns should we follow?",
  "repositories": ["acme/backend", "acme/frontend", "acme/websocket-service"]
}
```

**Returns**: Implementation strategy, integration points, consistent patterns to follow, potential challenges

#### Pattern 4: Performance Analysis

**When to use**: Identifying bottlenecks and optimization opportunities

```json
{
  "input": "What are the performance bottlenecks in our data processing pipeline? Focus on database queries and data transformations.",
  "repositories": ["acme/data-service", "acme/analytics-engine"]
}
```

**Returns**: Bottleneck identification, N+1 queries, inefficient algorithms, caching opportunities

#### Pattern 5: Dependency Impact

**When to use**: Before upgrading dependencies or making breaking changes

```json
{
  "input": "If we upgrade from Express 4 to Express 5, what parts of our codebase would be affected? What breaking changes should we prepare for?",
  "repositories": ["acme/api", "acme/admin-portal", "acme/webhook-service"]
}
```

**Returns**: Affected code sections, breaking changes, migration strategy, risk assessment

#### Pattern 6: Onboarding New Developers

**When to use**: Explaining complex parts of the codebase

```json
{
  "input": "Explain how our multi-tenant isolation works. How do we ensure data separation between clients?",
  "repositories": ["acme/core", "acme/tenant-service"]
}
```

**Returns**: Conceptual explanation, implementation details, key files and functions, potential gotchas

#### Pattern 7: Best Practice Validation

**When to use**: Ensuring code quality and consistency

```json
{
  "input": "Are we following React best practices in our component architecture? Identify anti-patterns and suggest improvements.",
  "repositories": ["acme/web-app", "acme/mobile-web"]
}
```

**Returns**: Pattern analysis, anti-pattern identification, specific improvement suggestions, refactoring priorities

</details>
