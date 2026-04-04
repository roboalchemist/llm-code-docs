# Source: https://docs.port.io/solutions/engineering-intelligence/why-port.md

# Why Port?

Port goes beyond measurement and reporting by combining engineering intelligence with orchestration on a unified software catalog. Instead of stopping at dashboards that show what happened, Port closes the end-to-end feedback loop from insight to execution and back to measurable impact. Insights are tied to the right service and owner in the Context Lake, turned into an executable next step, and tracked back to measurable impact.

Example

A production-readiness scorecard for the critical `checkout` service drops to red â mean time to recovery (MTTR) has doubled. Port links the spike to the owning team and correlates it with recent releases and incidents. An AI agent identifies the root cause and recommends a fix. The service owner reviews the findings and triggers an agentic workflow that creates a Jira ticket with the agent's improvement steps. After the fix, MTTR recovers and the scorecard turns green â measured on the same platform that surfaced the problem.

## The pillars of Port's approach[â](#the-pillars-of-ports-approach "Direct link to The pillars of Port's approach")

| Pillar                        | What it does                                                                                                                                                                                                                                                                                                                                           | Common industry gap it addresses                                                                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Context Lake**              | Port maintains a live software catalog of every service, API, team, repository, dependency, deployment, and incident. When metrics change, you see exactly which entities are affected and why.                                                                                                                                                        | Standalone metrics tools aggregate data but don't maintain a catalog. You can see deployment frequency dropped, but not which services, which teams, or what dependencies are involved.     |
| **Governance and Scorecards** | Scorecards define standards as rules evaluated continuously against the catalog. Track production readiness, security compliance, AI adoption, test coverage - standards become automated checks, not manual audits. AI agents can recommend governance policies based on industry best practices.                                                     | Metrics-only tools show data as-is. They can't enforce that services must have owners, that production services require 80% test coverage, or that all APIs must have documentation.        |
| **Workflow Orchestration**    | When standards violations are detected or metrics degrade, Port workflows can notify owners, create tickets, trigger remediation, block deployments, or provide developers with self-service actions to fix issues.                                                                                                                                    | Without orchestration, humans must notice dashboard changes and manually follow up. Seeing a problem doesn't automatically create a ticket, notify an owner, or prevent a risky deployment. |
| **AI agents & MCP**           | AI agents run on top of the catalog to surface insights, explain what's driving metric changes, and recommend next best actions. Through MCP integration, agents connect to external tools and data sources, generating consistent outputs like bottleneck reports, prioritized user stories, and implementation plans grounded in your org's context. | Without the catalog, governance, and orchestration foundation, AI agents can't reliably connect insights to owners, standards, and concrete actions across services.                        |

## AI agents and MCP: the intelligence layer[â](#ai-agents-and-mcp-the-intelligence-layer "Direct link to AI agents and MCP: the intelligence layer")

Port's AI agents are context-aware intelligence that operates on your entire software catalog. Through MCP, agents can:

* **Connect to external MCPs:** Interact with tools such as GitHub, Jira, Slack, PagerDuty, and any other tool in your stack.
* **Take autonomous actions:** Create tickets, update documentation, trigger workflows, and enforce policies.
* **Provide contextual recommendations:** Agents know which services are affected, who owns them, and what standards apply.
* **Learn from your organization:** Use your historical data, patterns, and governance rules to provide personalized recommendations.

## Port's architectural approach[â](#ports-architectural-approach "Direct link to Port's architectural approach")

Port is built on a software catalog that models your entire engineering estate. Metrics, standards, and workflows all operate on the same unified data model.

* **Metrics connected to context:** When deployment frequency drops, you immediately see which services, which teams, which dependencies. Scorecards continuously enforce standards. Workflows automatically act on insights.
* **One catalog, many use cases:** The catalog you build for DevEx metrics becomes your platform foundation. When you need self-service workflows, API catalogs, or developer portals, you activate features on the same platform - no re-cataloging, no migration.
* **Single platform, no duplication:** Engineering intelligence and your developer portal share the same catalog and data model. No separate tools to maintain, no duplicated data, no integration overhead.

## Summary - what sets Port apart[â](#summary---what-sets-port-apart "Direct link to Summary - what sets Port apart")

### Measurement + action[â](#measurement--action "Direct link to Measurement + action")

* Track DORA metrics, custom KPIs, and developer surveys on the same catalog.
* Scorecards continuously evaluate standards across services and teams.
* Workflows automatically remediate when metrics degrade or standards are violated.

### DevEx + Agentic Developer Portal (ADP)[â](#devex--agentic-developer-portal-adp "Direct link to DevEx + Agentic Developer Portal (ADP)")

* Build your catalog once for both engineering intelligence and self-service developer workflows.
* Developers scaffold services, provision resources, and resolve issues without leaving the portal.
* No second tool, no re-cataloging, no migration.

### Context-rich[â](#context-rich "Direct link to Context-rich")

* Every metric is linked to services, teams, dependencies, and owners.
* When deployment frequency drops, you see exactly which services and teams are affected.
* Understand why something changed, not just what.

### AI agents with MCP[â](#ai-agents-with-mcp "Direct link to AI agents with MCP")

* Agents analyze trends and explain what's driving metric changes across your catalog.
* MCP connects agents to GitHub, Jira, Slack, PagerDuty, and the rest of your toolchain.
* Agents generate bottleneck reports, prioritized stories, and implementation plans grounded in your data.

The bottom line

Build your software catalog once with Port and get engineering intelligence, AI agents with MCP integration, and Agentic Developer Portal capabilities from the same unified foundation. Your DevEx investment becomes your Agentic Developer Portal infrastructure, powered by AI agents that can take action across your entire toolchain.

## Next steps[â](#next-steps "Direct link to Next steps")

Explore how Port's engineering intelligence works in practice:

* [Engineering intelligence overview](/solutions/engineering-intelligence/overview.md) - The journey from surveys to advanced metrics.
* [Surveys](/solutions/engineering-intelligence/surveys.md) - Use qualitative data as a catalyst for change.
* [Measure DORA metrics](/solutions/engineering-intelligence/measure-dora-metrics.md) - Track deployment frequency, lead time, change failure rate, and MTTR.
* [More engineering metrics](/solutions/engineering-intelligence/more-engineering-metrics.md) - Go beyond DORA with custom metrics tied to your catalog.
* [Improve lead time](/solutions/engineering-intelligence/improve-lead-time.md) - Actionable workflows to reduce time from commit to production.
* [Reduce MTTR](/solutions/engineering-intelligence/reduce-mttr.md) - Automate incident response and recovery.
