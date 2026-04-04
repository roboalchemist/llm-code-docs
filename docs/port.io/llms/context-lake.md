# Source: https://docs.port.io/ai-interfaces/context-lake.md

# Context lake

Port's Context Lake is your unified engineering knowledge layerâconnecting data from across your entire toolchain into a single, semantically-rich source of truth. It's not a separate feature, but rather the powerful result of Port's core capabilities working together to provide organizational context that AI agents, developers, and workflows can understand and act upon.

## What comprises the context lake[â](#what-comprises-the-context-lake "Direct link to What comprises the context lake")

The context lake transforms scattered data across your engineering tools into unified organizational knowledge. It is built from four core components:

### Software catalog - your data[â](#software-catalog---your-data "Direct link to Software catalog - your data")

The [software catalog](/build-your-software-catalog/overview.md) is where you define YOUR organization's data model using blueprints (services, environments, teams, deployments, incidents, etc.) and populate it with entities from all your tools. This catalog becomes your organizational semantic layerâteaching Port what "service," "deployment," or "incident" means specifically in your context, providing the schema and structure that gives meaning to your data.

### Business context - holistic view[â](#business-context---holistic-view "Direct link to Business context - holistic view")

Beyond technical metadata, the Context Lake enriches your software catalog with **business context**âthe organizational, financial, and operational signals that help prioritize work, assess risk, and align engineering decisions with business objectives. This business layer transforms technical catalogs into decision-making platforms by answering: *"What matters most to the business?"*

Business context in Port can include:

#### Cost & financial context[â](#cost--financial-context "Direct link to Cost & financial context")

* **Cost center attribution** - Track which department or budget owns each resource via [AWS Cost integration](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/.md) or [Kubecost](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost/.md)
* **Revenue impact** - Tag services that directly generate revenue or support revenue-generating features
* **Cloud spending patterns** - Understand resource costs to inform optimization and prioritization decisions

#### Criticality & risk context[â](#criticality--risk-context "Direct link to Criticality & risk context")

* **Business criticality levels** - Classify services (e.g., mission-critical, customer-facing, internal tooling) to drive different [SLA requirements](/guides/all/track-slos-and-slis-for-services.md), triage workflows, and [automation policies](/solutions/security/prioritise-vulnerabilities.md#policy-as-code)
* **Disaster recovery tier** - Define RTO/RPO requirements based on business impact to inform backup strategies and incident response priorities
* **Data sensitivity** - Mark resources handling PII, financial data, or regulated information to enforce compliance controls
* **Compliance scope** - Tag services subject to SOC 2, GDPR, HIPAA, or PCI-DSS to ensure audit readiness

#### Operational context[â](#operational-context "Direct link to Operational context")

* **SLAs & SLOs** - Define service-level agreements and objectives to measure reliability, track [MTTR](/guides/all/track-and-show-mtbf-for-services.md), and ensure [SLA compliance](/solutions/security/prioritise-vulnerabilities.md#sla-visibility)
* **On-call ownership** - Integrate [PagerDuty schedules](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md) to understand who's responsible right now for incident response
* **Escalation policies** - Define who to notify and when for different severity levels based on business impact
* **Incident captain & responder roles** - Track who's currently leading incidents or available for triage

#### Organizational context[â](#organizational-context "Direct link to Organizational context")

* **Team affiliation** - Connect services to teams via [GitHub CODEOWNERS](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) or [Jira project mappings](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/examples.md) for clear ownership
* **Reporting hierarchy** - Map organizational structure (team â department â division) for escalation paths
* **Business unit alignment** - Associate services with product lines or business units to understand impact radius

#### Customer & product context[â](#customer--product-context "Direct link to Customer & product context")

* **Customer tier** - Identify which customer segments are affected (e.g., enterprise, gold-tier, freemium) to prioritize incidents and features affecting high-value customers
* **Product lifecycle stage** - Tag services by maturity (closed beta, open beta, GA, deprecated) to set appropriate expectations and SLAsâa closed beta feature with 10 freemium users has different urgency than a GA feature serving enterprise customers

**Why business context matters:**

When AI agents and workflows understand business context, they can:

* **Prioritize vulnerabilities** affecting revenue-generating production services over internal dev tools
* **Route incidents** to the right on-call engineer based on service ownership and escalation policies
* **Estimate blast radius** of a deployment by understanding dependent services and their business criticality
* **Automatically enforce policies** like "critical services must have SLOs defined" or "PII-handling services require SOC 2 compliance checks"
* **Calculate risk scores** that combine technical severity (CVSS) with business impact (criticality + revenue + SLA + customer tier)
* **Adjust incident response** based on affected customer tierâa P1 incident affecting enterprise customers triggers immediate executive notification, while the same issue in closed beta may follow standard on-call procedures

**Example use cases:**

* Risk-based vulnerability triage
* Context-aware incident routing
* Disaster recovery policy enforcement

**Scenario:** A critical CVE is discovered in a library used by multiple services.

**Without business context:** Security team gets hundreds of alertsâno clear way to prioritize which services to patch first.

**With Port's business context:**

1. Port enriches each vulnerability with:

   * Service **business criticality** (mission-critical vs. internal)
   * **Revenue impact** (directly revenue-generating or not)
   * **SLA requirements** (99.99% uptime vs. best-effort)
   * **Data sensitivity** (handles customer PII or not)
   * **Compliance scope** (subject to SOC 2 audit)
   * **Customer tier** (enterprise vs. freemium)

2. AI agent or automation calculates **risk score**:

   ```
   Risk = CVE Severity Ã (Business Criticality + Revenue Impact + SLA Weight + Compliance Factor + Customer Tier)
   ```

3. Results in prioritized triage queue:

   * **Fix immediately**: Payment service (mission-critical, revenue-generating, 99.99% SLA, PCI-DSS scope, enterprise customers)
   * **Fix this sprint**: Customer portal (customer-facing, revenue-supporting, 99.5% SLA, gold-tier customers)
   * **Backlog**: Internal dev tools (low criticality, no SLA, internal users only)

*Learn more:* [Prioritize vulnerabilities with business context](/solutions/security/prioritise-vulnerabilities.md)

**Scenario:** Production API starts returning 500 errors during business hours.

**Without business context:** Generic "production down" alert â manual escalation â wasted time finding the right owner.

**With Port's business context:**

1. Port's incident automation queries Context Lake for:

   * Service **on-call schedule** from PagerDuty
   * Service **business criticality** and **SLA** (99.99% uptime)
   * **Revenue impact** (payment processing = revenue-blocking)
   * **Customer tier affected** (enterprise customers experiencing errors)
   * **Product lifecycle stage** (GA with 10,000+ active users)
   * **Recent deployments** (was there a recent change?)
   * **Dependent services** (what else might be affected?)

2. Automation takes action based on context:

   * **Closed beta, freemium users**: Page on-call engineer via standard PagerDuty workflow
   * **GA, enterprise customers**: Immediate P1 escalation â page incident captain + notify VP Engineering â create executive war room

3. Result: **Faster MTTR and appropriate response** because both responders and escalation paths match business impact

*Learn more:* [Generate incident updates with n8n and Port](/guides/all/generate-incident-updates-with-n8n-and-port.md)

**Scenario:** Platform team needs to ensure all mission-critical services have disaster recovery plans.

**Without business context:** Manual spreadsheet tracking â inconsistent enforcement â audit findings.

**With Port's business context:**

1. Services are tagged with:

   * **Business criticality** (mission-critical, high, medium, low)
   * **Disaster recovery tier** (Tier 1: RTO < 1hr, Tier 2: RTO < 4hr, Tier 3: RTO < 24hr)
   * **Backup schedule** (daily, weekly, none)
   * **Customer tier impact** (affects enterprise vs. freemium)
   * **Product lifecycle** (GA services have stricter DR requirements than beta)

2. Port automation enforcement policy (AEP):

   ```
   IF service.businessCriticality == "mission-critical"
   AND service.productLifecycle == "GA"
   AND service.disasterRecoveryTier != "Tier 1"
   THEN fail_scorecard("Missing DR Plan")
   AND create_jira_ticket(owner, "Define DR plan with RTO < 1hr for GA mission-critical service")
   ```

3. Scorecard dashboard shows:

   * 12/15 mission-critical GA services have Tier 1 DR plans
   * 3 services out of compliance â auto-created tickets assigned to owners
   * Beta services excluded from strict DR requirements until GA launch

*Learn more:* [Compliance as code](/solutions/security/compliance-as-code.md)

**Ingesting business context into Port:**

Business context comes from many sources:

* **Cloud providers** (cost data via [AWS Cost](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/.md), [Kubecost](/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost/.md))
* **Incident management** (on-call schedules via [PagerDuty](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md), [ServiceNow](/build-your-software-catalog/sync-data-to-catalog/incident-management/servicenow.md))
* **Source control** (team ownership via [GitHub CODEOWNERS](/build-your-software-catalog/sync-data-to-catalog/git/github/.md), [GitLab](/build-your-software-catalog/sync-data-to-catalog/git/gitlab/.md))
* **Project management** (business unit, stakeholders via [Jira](/build-your-software-catalog/sync-data-to-catalog/project-management/jira/examples.md))
* **Manual enrichment** (business criticality, revenue impact, SLAs, customer tier, product lifecycle added as blueprint properties and updated via [self-service actions](/actions-and-automations/setup-backend/github-workflow/.md) or [API](/api-reference/port-api.md))

The Context Lake unifies all these sources so AI agents, workflows, and dashboards can make business-aware decisions.

### Access controls - data governance[â](#access-controls---data-governance "Direct link to Access controls - data governance")

[RBAC and permissions](/sso-rbac/rbac-overview/.md) ensure that the right people and systems see the right data. Teams, roles, and policies control who can view, edit, or act on catalog data, maintaining security while enabling collaboration and providing governed access to your organizational knowledge.

### Scorecards - your standards[â](#scorecards---your-standards "Direct link to Scorecards - your standards")

[Scorecards](/scorecards/overview.md) define and track your engineering standards, KPIs, and quality metrics. They encode organizational expectationsâproduction readiness requirements, security compliance rules, operational best practicesâas measurable criteria within the Context Lake, providing the organizational standards and quality signals that inform decisions.

### Interface layer - how you access it[â](#interface-layer---how-you-access-it "Direct link to Interface layer - how you access it")

Context Lake data becomes actionable through multiple interfaces: **[AI Interfaces](/ai-interfaces/overview.md)** where AI agents and assistants query through [Port MCP Server](/ai-interfaces/port-mcp-server/overview-and-installation.md) to understand your organization, **[API](/api-reference/port-api.md)** for programmatic access, and **[Interface Designer](/customize-pages-dashboards-and-plugins/dashboards/overview.md)** with dashboards and visualizations that surface insights to your teamsâproviding multiple ways to query, visualize, and act on your organizational context.

### External data via MCP Connectors[â](#external-data-via-mcp-connectors "Direct link to External data via MCP Connectors")

While the Context Lake provides structured organizational knowledge, [MCP Connectors](/ai-interfaces/mcp-connectors.md) complement it by giving Port AI access to external tools like Notion, Linear, Jira, and other MCP servers. The Context Lake provides the modeled data (blueprints, entities, scorecards), while MCP Connectors provide real-time access to external data you wouldn't typically model like documentation, tickets, logs, and other just-in-time information. Together, they give AI agents both structured context and dynamic external data for more accurate responses.

## Why the context lake matters[â](#why-the-context-lake-matters "Direct link to Why the context lake matters")

* For AI agents
* For developers
* For platform teams

Generic AI doesn't understand what "production-ready" means in YOUR organization, who owns which services, or how your deployment pipeline works. Context Lake provides this semantic understanding, enabling AI agents to:

* Answer ownership questions with definitive data (not guesses from code comments).
* Understand dependencies and relationships between services.
* Follow your organization's standards and guardrails when taking actions.
* Make decisions based on real-time operational context.

Instead of hunting across 10 different tools to understand a service's dependencies, ownership, deployment history, or incident timeline, developers get unified context in one place. The Context Lake connects the dots automatically.

**Benefits:**

* Quick access to service ownership and team information.
* Understand dependencies without switching between tools.
* See complete deployment and incident history in context.
* Get AI-powered insights based on your organization's actual data.

Define your organizational semantics onceâservice definitions, environment types, team structures, standardsâand every tool, workflow, and AI agent can consume this shared knowledge. No more syncing configurations across systems.

**Benefits:**

* Single source of truth for organizational definitions.
* Consistent standards across all tools and automations.
* Reduced maintenance overhead from duplicate configurations.
* Enable self-service while maintaining governance.

## Context lake in action[â](#context-lake-in-action "Direct link to Context lake in action")

* AI agent understanding ownership
* Autonomous service provisioning
* Incident response

**Developer asks:** "Who owns the payments service?"

* **Without Context Lake:** AI guesses based on code comments or recent contributors.
* **With Context Lake:** AI queries the catalog â sees Team relation â returns the owning team with Slack channel and on-call schedule.

**AI agent needs to provision a dev environment:**

* **Without Context Lake:** Agent doesn't know company's cloud standards, naming conventions, or cost limits.
* **With Context Lake:** Agent queries blueprints â understands allowed regions, naming patterns, tagging requirements â provisions correctly within organizational guardrails.

**Alert fires:** "payments-api pod crashing"

* **Without Context Lake:** Engineer hunts through Slack, wiki, runbooks across multiple tools.
* **With Context Lake:** Port surfaces: recent deployments, related PRs, dependent services, ownership, SLOs, past incidentsâall in unified context for faster resolution.

## External agents and AI workflows[â](#external-agents-and-ai-workflows "Direct link to External agents and AI workflows")

External AI agents and automation workflows can leverage Port's Context Lake to make intelligent, context-aware decisions without needing direct access to your entire toolchain. Instead of building custom integrations for each tool, external systems can query Port's unified knowledge layer to understand your organization's structure, relationships, and standards.

### n8n integration[â](#n8n-integration "Direct link to n8n integration")

Port provides a custom n8n node that simplifies integration with Port's AI agents and Context Lake. To get started:

1. **[Set up Port's n8n custom node](/ai-interfaces/port-n8n-node.md)** â Install and configure the Port node in your n8n instance
2. **[Build automation workflows](/guides/all/remediate-vulnerability-with-n8n-and-port.md)** â See an example of using Port as a context lake for vulnerability management workflows

## Getting started[â](#getting-started "Direct link to Getting started")

Building your Context Lake is a natural part of setting up Port:

1. **[Define your data model](/build-your-software-catalog/overview.md)** - Create blueprints that represent your organization's entities.
2. **[Connect your tools](/build-your-software-catalog/sync-data-to-catalog/.md)** - Ingest data from GitHub, Kubernetes, PagerDuty, and 100+ other integrations.
3. **[Set up relationships](/build-your-software-catalog/customize-integrations/configure-mapping.md#relations)** - Define how entities connect to each other.
4. **[Configure access controls](/sso-rbac/rbac-overview/.md)** - Ensure proper data governance.
5. **[Define standards](/scorecards/overview.md)** - Create scorecards that encode your quality requirements.

As you build your catalog, you're simultaneously building your Context Lakeâthe unified knowledge layer that powers intelligent automation and AI-driven workflows.
