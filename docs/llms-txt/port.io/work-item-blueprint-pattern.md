# Source: https://docs.port.io/solutions/autonomous-ticket-resolution/work-item-blueprint-pattern.md

# Work item blueprint pattern

The work item blueprint pattern is the recommended approach for managing autonomous development workflows in Port. It separates workflow execution state from origin entities (like Jira issues or GitHub issues), enabling AI agents to orchestrate work through clearly defined stages while keeping your existing tools clean and focused.

This is a starting pattern, not a rigid template.

Adapt the stages, scorecards, and AI integrations to match your organization's workflows.

## Why this pattern?[â](#why-this-pattern "Direct link to Why this pattern?")

**The problem:** When AI agents help triage, plan, and execute work, the intuitive approach is to add fields like `ai_suggested_priority` or `coding_agent_status` directly to origin entity. This creates tight coupling between your AI logic and external systems, clutters your ticketing UI, and limits the context available to agents.

**The solution:** The work item pattern separates workflow orchestration from origin entities, delivering:

* **Faster cycle times**: AI agents operate on work items enriched with service context, deployment history, and team ownership and not just raw entity data.
* **Cleaner origin systems**: Origin entities stay focused on requirements and workflow state lives in Port.
* **Flexible AI integration**: Each workflow stage has a dedicated AI agent with clear responsibilities and you can adapt stages, scorecards, and automations to match your team's process.
* **Better governance**: Scorecard rules enforce prerequisites without modifying external systems.

## How the work item pattern solves this[â](#how-the-work-item-pattern-solves-this "Direct link to How the work item pattern solves this")

The work item blueprint pattern creates a dedicated `work_item` entity that maintains a relation to the origin entity while tracking its own execution state. This separation provides:

**A clean origin system** - The Jira issue or GitHub issue stays focused on requirements. No workflow-specific fields are needed in the external system.

**Rich context aggregation** - The `work_item` connects to related entities across your software catalog: the origin ticket, the service being modified, the team and owner responsible, the repository and PR where code changes happen, and the deployment record. These relations give AI agents access to the context needed for decision making.

**Flexible AI integration** - Each workflow stage can have a specific AI agent with focused responsibility. Planning agents access service metadata, coding agents see repository patterns, deployment agents check dependencies.

**Customizable progression** - Scorecard rules enforce stage prerequisites without modifying the origin system. You control what criteria must be met before work advances.

## The five-stage workflow[â](#the-five-stage-workflow "Direct link to The five-stage workflow")

The work item blueprint uses scorecards to manage progression through five stages:

```
Draft â Plan â Develop â Deploy â Completed
```

Each stage represents a distinct phase with specific requirements and AI integration points:

**Draft** - Work items enter this stage when created from a Jira ticket or other source. They contain minimal information and await triage. AI can suggest initial categorization based on the ticket description.

**Plan** - During this stage, teams assign ownership, set priority, and determine the AI augmentation level. Requirements include assigned owner, set priority, and defined AI augmentation level. AI can analyze the ticket, suggest priority based on service tier and historical patterns, and draft a technical plan.

**Develop** - Code changes happen during this stage. Requirements include human-approved plan and created pull request. AI coding agents (Claude Code, Devin, GitHub Copilot) generate implementation while human developers review and refine the work.

**Deploy** - After the PR merges, the work item enters this stage. Teams can review blast radius and approve production deployment. Requirements include merged PR. AI can assess deployment risk based on service dependencies and suggest deployment timing.

**Completed** - The final stage records completion time and enables cycle time analysis. Requirements include successful deployment in production.

## Why relations matter[â](#why-relations-matter "Direct link to Why relations matter")

The `work_item` blueprint connects to entities across your software catalog: the origin Jira ticket, the service being modified, the team and owner responsible, the repository and PR where code changes happen, and the deployment record.

These relations matter because AI agents need context to make good decisions. When a planning agent suggests priority, it can check the service tier. When a deploy agent assesses risk, it can look at the service's dependencies and recent incidents. The work item doesn't store this data - it gets access to it through mirror properties, so everything stays in sync.

## How scorecards drive progression[â](#how-scorecards-drive-progression "Direct link to How scorecards drive progression")

Scorecards evaluate work item properties and relations to determine the current stage. Rules at each level act as gates:

* **Draft â Plan**: Requires owner assigned, priority set, and AI augmentation level defined
* **Plan â Develop**: Requires plan approved by human and PR created
* **Develop â Deploy**: Requires PR merged
* **Deploy â Completed**: Requires deployment successful and deployed to production

This approach keeps progression logic in Port, not hard-coded in external systems. Teams can adjust requirements without touching Jira workflows or GitHub actions.

## Customizing for your workflow[â](#customizing-for-your-workflow "Direct link to Customizing for your workflow")

The five-stage workflow works for most teams, but you can adapt it:

**Stage names** - Rename stages to match your terminology. "Plan" becomes "Refinement," "Develop" becomes "In Progress," "Deploy" becomes "Release."

**Progression rules** - Change what gates each transition. Require code review approval before Deploy. Add a "Testing" stage between Develop and Deploy. Remove Plan approval for low-priority items.

**Relations** - Connect to entities relevant to your workflow: design documents, testing environments, feature flags.

**AI augmentation levels** - Define what each level means for your team:

* **Human**: No AI involvement
* **AI-assisted**: AI suggests, human implements
* **AI-led**: AI implements, human reviews
* **Autonomous**: AI implements and deploys with monitoring

## Benefits[â](#benefits "Direct link to Benefits")

**Separation of concerns** - Requirements live in Jira. Workflow execution state lives in Port. Each system does what it does best.

**Context-aware AI** - Relations connect work items to services, repositories, PRs, and deployments. AI agents make better decisions with richer context.

**Flexible progression** - Scorecards drive stage transitions with configurable rules. No hard-coded workflows in external systems.

**Clean interfaces** - Origin entities stay focused. Workflow complexity doesn't leak into tools your team uses daily.

**Adaptable to your process** - Stages, rules, and AI integration points customize to your development workflow.

## Implementation[â](#implementation "Direct link to Implementation")

Ready to implement this pattern? The [work item blueprint implementation guide](/guides/all/work-item-blueprint.md) walks through the technical setup including:

* Blueprint configuration with properties and relations
* Scorecard rules for each stage transition
* Self-service actions for stage progression
* AI agent integration points
* Example JSON configurations

## Next steps[â](#next-steps "Direct link to Next steps")

* Review the [implementation guide](/guides/all/work-item-blueprint.md) for technical details
* Explore the [Autonomous Ticket Resolution demo](https://demo.getport.io/my_work_items) to see this pattern in action
* Explore all of our [Autonomous Ticket Resolution related guides](http://localhost:4000/guides?tags=Autonomous+Ticket+Resolution)
