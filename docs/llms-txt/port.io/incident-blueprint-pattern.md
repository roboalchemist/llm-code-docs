# Source: https://docs.port.io/solutions/incident-management/incident-blueprint-pattern.md

# Incident blueprint pattern

The incident blueprint pattern is the recommended approach for managing self-healing incident workflows in Port. It separates workflow execution state from origin entities (like PagerDuty incidents or Datadog alerts), enabling AI agents to orchestrate incident response through clearly defined stages while keeping your existing alerting tools clean and focused.

This is a starting pattern, not a rigid template.

Adapt the stages, scorecards, and AI integrations to match your organization's incident management process.

## Why this pattern?[â](#why-this-pattern "Direct link to Why this pattern?")

**The problem:** When AI agents help triage, investigate, and resolve incidents, the intuitive approach is to add fields like `ai_suggested_severity` or `remediation_plan` directly to your origin entity. This creates tight coupling between your AI logic and external systems, limits the context available to agents, and lacks clear human approval gates.

**The solution:** The incident pattern separates workflow orchestration from origin entities, delivering:

* **Faster resolution times**: AI agents operate on incidents enriched with service context, deployment history, and on-call schedulesânot just raw alert data.
* **Cleaner origin systems**: PagerDuty/Datadog alerts stay focused on alerting. Workflow state lives in Port.
* **Staged AI integration**: Each workflow stage has a dedicated AI agent with clear responsibilities. Adapt stages, scorecards, and automations to match your SRE process.
* **Human governance**: AI suggests severity, root cause, and remediation. Humans review and approve before progressing.

## How the incident pattern solves this[â](#how-the-incident-pattern-solves-this "Direct link to How the incident pattern solves this")

The incident blueprint pattern creates a dedicated `incident` entity that maintains a relation to the origin alert while tracking its own execution state. This separation provides:

**A clean origin system** - The PagerDuty incident or Datadog alert stays focused on alerting. No workflow-specific fields are needed in the external system.

**Rich context aggregation** - The `incident` connects to related entities across your software catalog: the origin alert, the primary and affected services, the response team and incident commander, recent deployments for rollback analysis, and remediation PRs. These relations give AI agents access to the context needed for investigation.

**Staged AI agents** - Each workflow stage has a specialized AI agent with focused responsibility. Triage agents assess severity, investigator agents analyze root cause, and RCA agents generate postmortems.

**Human approval gates** - AI suggests severity, root cause, and remediation. Humans review and approve before progressing. This ensures governance without slowing down response.

**Customizable progression** - Scorecard rules enforce stage prerequisites without modifying the origin system. You control what criteria must be met before an incident advances.

## The six-stage workflow[â](#the-six-stage-workflow "Direct link to The six-stage workflow")

The incident blueprint uses scorecards to manage progression through six stages:

```
Alert â Triage & Response â Investigate â Remediate â Resolved â Completed with Postmortem
```

Each stage represents a distinct phase with specific requirements and AI integration points:

**Alert** - Incidents enter this stage when created from a PagerDuty alert or other monitoring source. They contain alert data and await triage. AI can analyze alert context and prepare initial categorization.

**Triage & Response** - AI analyzes the incident, suggests severity based on service tier and business impact, and drafts stakeholder communications. Requirements include severity assigned, owner and response team assigned, business impact documented, and triage timestamp recorded.

**Investigate** - AI examines recent deployments, service dependencies, and historical patterns to identify root cause. It generates a remediation plan for human review. Requirements include war room URL created, primary service identified, and investigation started timestamp.

**Remediate** - After the remediation plan is approved, the team executes the fix. This may include rolling back a deployment, merging a hotfix PR, or applying configuration changes. Requirements include root cause identified, remediation plan documented, and remediation started timestamp.

**Resolved** - The incident is marked resolved when the fix is verified and customer impact has ended. MTTR is calculated automatically. Requirements include resolution timestamp and status set to resolved.

**Completed with Postmortem** - The final stage generates a comprehensive postmortem document with timeline, root cause analysis, action items, and lessons learned. Requirements include postmortem content completed and postmortem completion timestamp.

## Why relations matter[â](#why-relations-matter "Direct link to Why relations matter")

The `incident` blueprint connects to entities across your software catalog: the origin PagerDuty incident, the primary and affected services, the response team and incident commander, recent deployments for rollback analysis, and remediation PRs.

These relations matter because AI agents need context to make good decisions. When a triage agent suggests severity, it can check the service tier and on-call schedule. When an investigator agent analyzes root cause, it can examine recent deployments and service dependencies. The incident doesn't store this data - it gets access to it through mirror properties, so everything stays in sync.

## How scorecards drive progression[â](#how-scorecards-drive-progression "Direct link to How scorecards drive progression")

Scorecards evaluate incident properties and relations to determine the current stage. Rules at each level act as gates:

* **Alert â Triage & Response**: Requires severity, owner, response team, business impact, and triage timestamp.
* **Triage & Response â Investigate**: Requires war room URL, primary service identified, and investigation started timestamp.
* **Investigate â Remediate**: Requires root cause identified, remediation plan documented, and remediation started timestamp.
* **Remediate â Resolved**: Requires resolution timestamp and status set to resolved.
* **Resolved â Completed with Postmortem**: Requires postmortem content completed and postmortem completion timestamp.

This approach keeps progression logic in Port, not hard-coded in external systems. Teams can adjust requirements without touching PagerDuty workflows or alerting rules.

## AI agents in the incident workflow[â](#ai-agents-in-the-incident-workflow "Direct link to AI agents in the incident workflow")

The incident workflow uses three specialized AI agents, each with focused responsibilities:

* **Triage Agent** (Alert â Triage): Severity assessment, business impact calculation, affected service identification, communication drafting, owner/team recommendation.
* **Investigator Agent** (Investigate): Root cause analysis, deployment correlation, rollback suggestion, remediation plan generation, similar incident detection.
* **RCA Agent** (Postmortem): Postmortem generation, timeline construction, action item creation, lessons learned extraction.

Each agent has access to Port's catalog through read-only tools, enabling queries across services, deployments, PRs, and historical incidents. Agents call update actions to store their findings, which humans then review and approve.

## Postmortem templates[â](#postmortem-templates "Direct link to Postmortem templates")

The incident blueprint includes a `postmortem_template` relation that points to a separate `postmortem_template` blueprint. This allows the RCA Agent to select the appropriate template structure based on incident type or severity. Configure templates for Google SRE format, Atlassian format, Five Whys, or custom formats. The AI agent reads the template structure to generate consistent, well-organized postmortems.

## Customizing for your workflow[â](#customizing-for-your-workflow "Direct link to Customizing for your workflow")

The six-stage workflow works for most SRE teams, but you can adapt it:

**Stage names** - Rename stages to match your terminology. "Triage & Response" becomes "Assessment," "Remediate" becomes "Mitigation," "Completed with Postmortem" becomes "Closed."

**Progression rules** - Change what gates each transition. Require manager approval for sev1 incidents. Add a "Validation" stage between Remediate and Resolved. Skip postmortem for sev4 incidents.

**Relations** - Connect to entities relevant to your workflow: runbook documents, Slack channels, Jira follow-up tickets.

**SLA thresholds** - Define SLA breach calculations based on your commitments:

* **Sev1**: Response within 15 minutes, resolution within 1 hour.
* **Sev2**: Response within 30 minutes, resolution within 4 hours.
* **Sev3**: Response within 2 hours, resolution within 24 hours.
* **Sev4**: Response within 1 business day.

## Benefits[â](#benefits "Direct link to Benefits")

**Separation of concerns** - Alert data lives in PagerDuty/Datadog. Workflow execution state lives in Port. Each system does what it does best.

**Context-aware AI** - Relations connect incidents to services, deployments, PRs, and on-call schedules. AI agents make better decisions with richer context.

**Flexible progression** - Scorecards drive stage transitions with configurable rules. No hard-coded workflows in external systems.

**Human governance** - AI suggests, humans approve. Severity, remediation plans, and postmortems require review before progressing.

**Adaptable to your process** - Stages, rules, SLA thresholds, and AI integration points customize to your incident management workflow.

## Implementation[â](#implementation "Direct link to Implementation")

Ready to implement this pattern? The [incident blueprint implementation guide](/guides/all/incident-blueprint.md) walks through the technical setup including:

* Blueprint configuration with properties and relations
* Scorecard rules for each stage transition
* Self-service actions for stage progression
* AI agent integration points
* Example JSON configurations

## Next steps[â](#next-steps "Direct link to Next steps")

* Review the [implementation guide](/guides/all/incident-blueprint.md) for technical details.
* Explore the [Self-Healing Incidents demo](https://demo.port.io/incidents_workflow) to see this pattern in action.
