# Source: https://docs.qodo.ai/qodo-documentation/qodo-aware/security-and-privacy.md

# Security and Privacy

Qodo Context Engine is built with enterprise-grade security and privacy in mind. It’s designed to provide intelligent, codebase-aware assistance—without compromising your data or control.

***

### Data Access & Scope

* **Code Access is Explicit**: Qodo Context Engine only analyzes the repositories you explicitly connect and tag. No code is accessed without user or admin configuration.
* **Context is Scoped**: Tagged repositories define the scope of what Qodo Context Engine can see and reason about. You remain in full control of what’s included.

***

### Data Handling

* **No Training on Customer Code**: Qodo Context Engine does not use your code for training any foundation models.
* **Temporary Retrieval Only**: Relevant code snippets are retrieved for context at query time and are not stored beyond session needs.
* **No Third-Party Sharing**: Your code and metadata are never shared with external parties.
* **You code never resides in Qodo servers.**

***

### Storage & Transmission

* **Encrypted at Rest and in Transit**: All data is encrypted using industry-standard protocols (TLS in transit, AES-256 at rest).
* **Isolated Indexing**: Each organization’s code index is isolated and never mixed with other tenants.

***

### Deployment & Integration

* **Flexible Deployment**: Available via cloud, hybrid, or MCP (Memory Code Provider) to support air-gapped or self-managed environments.
* **Audit-Ready**: All interactions with Qodo Context Engine can be logged and traced, enabling compliance with internal policies and external regulations.

***

### Trust & Control

* **You Own Your Data**: You choose what’s connected, indexed, and queried.
* **Enterprise Controls**: Role-based access, tagging, and scoping controls help you define how Qodo Context Engine is used across your team.
