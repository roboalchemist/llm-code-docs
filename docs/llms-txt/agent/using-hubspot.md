# Source: https://docs.agent.ai/builder/using-hubspot.md

# Using Agent.ai with HubSpot

> Start here to connect HubSpot, learn core patterns, and jump to actions, guides, and recipes.

The HubSpot integration connects Agent.ai directly to your CRM, enabling AI agents to read, analyze, and update your contacts, companies, deals, and custom objects in real time. Whether you're enriching lead data, automating deal updates, or building customer onboarding flows, this integration gives your agents native access to HubSpot's full data model.

**How it works**: Your agents can search for records, pull complete histories (including timeline events and engagements), process data with AI, then write back updates or create new records—all without leaving your workflow. Combine HubSpot actions with loops, conditionals, and LLM calls to build sophisticated automations that would normally require custom code or third-party tools.

### Why use HubSpot with Agent.ai

Your CRM is where revenue conversations live. Agent.ai turns that data into action:

* **Move deals forward, faster**: Pull a deal's full history (emails, meetings, notes), have AI assess momentum and risk, then update health fields or create next steps automatically.
* **Capture and convert more leads**: With features like Lead Magnet, visitors opt in before using your agent, and new contacts are synced to HubSpot automatically (no manual wiring).
* **Give ops superpowers**: Search, loop, and update at scale. Fix data hygiene, normalize stages, or tag segments across hundreds of records in minutes.
* **Create memorable experiences**: Personalize outreach, onboard customers with timely nudges, and keep teams aligned with concise AI summaries.

The result: less swivel-chair work, more time closing deals, and a CRM that stays up to date on its own.

***

## Quick start

This 3‑minute setup connects your CRM and gets you running your first Agent.ai flow.

| 1. Connect HubSpot                                                                                                                                                                                                        | 2. Run your first flow                                                                                                                                                                                                                                        | 3. Use a recipe                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connect your portal and verify permissions so Agent.ai can read/write CRM data.<br />[HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup) · [OAuth scopes](../integrations/hubspot-v2/reference/oauth-scopes) | Search deals → For Loop → Update stage to see end‑to‑end value fast.<br />Tip: use the `{}` button to insert variables.<br />[Search](../actions/hubspot-v2-search-objects) · [For Loop](../actions/for_loop) · [Update](../actions/hubspot-v2-update-object) | Start from a proven workflow, then customize for your team.<br />[Deal Analysis](../recipes/hubspot-deal-analysis) · [Onboarding](../recipes/hubspot-customer-onboarding) · [Contact Enrichment](../recipes/hubspot-contact-enrichment) |

***

## HubSpot actions (V2)

Use this as your action index—jump straight to the tool you need while building.

* [Search Objects](../actions/hubspot-v2-search-objects)
* [Lookup Object](../actions/hubspot-v2-lookup-object)
* [Create Object](../actions/hubspot-v2-create-object)
* [Update Object](../actions/hubspot-v2-update-object)
* [Get Timeline Events](../actions/hubspot-v2-get-timeline-events)
* [Create Timeline Event](../actions/hubspot-v2-create-timeline-event)
* [Get Engagements](../actions/hubspot-v2-get-engagements)
* [Create Engagement](../actions/hubspot-v2-create-engagement)

Related general actions:

* [Invoke LLM](../actions/use_genai)
* [For Loop](../actions/for_loop)
* [If Condition](../actions/if_else)
* [Set Variable](../actions/set-variable)

***

## HubSpot guides and references

Bookmark these essentials for setup, debugging, and deeper understanding.

* [Setup](../integrations/hubspot-v2/guides/hubspot-setup)
* [Triggers](../integrations/hubspot-v2/guides/webhook-triggers)
* [Variable System](../integrations/hubspot-v2/foundation/02-variable-system)
* [Troubleshooting](../integrations/hubspot-v2/guides/troubleshooting)
* [Error Messages](../integrations/hubspot-v2/reference/error-messages)

***

## Patterns you’ll use

Use these as blueprints—copy the shape, then swap in your objects and fields.

### Deal health analysis with AI

1. Lookup deal → 2. Get Timeline Events → 3. Invoke LLM (analyze) → 4. Update deal

### Engagement summary for contacts

1. Get Engagements → 2. Invoke LLM (summarize) → 3. Send notification or update property

### Bulk updates from searches

1. Search (e.g., deals in stage) → 2. For Loop → 3. Update each record

***

***

## Troubleshooting

Running into bumps? Start here before you dig into logs or support.

* Check OAuth scopes and reconnect if missing permissions
* Verify property internal names and value formats
* Use smaller limits while testing (10–20)
* Inspect execution logs to see data returned

***

## What to build next

A few great next steps to go from first success to repeatable impact.

* Explore recipes: [Deal Analysis](../recipes/hubspot-deal-analysis), [Customer Onboarding](../recipes/hubspot-customer-onboarding), [Contact Enrichment](../recipes/hubspot-contact-enrichment)
* Add a [Lead Magnet](./lead-magnet) to capture opt-ins and sync to HubSpot
