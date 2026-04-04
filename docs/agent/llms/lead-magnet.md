# Source: https://docs.agent.ai/builder/lead-magnet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lead Magnet

> Require opt-in before running an agent and automatically add leads to your CRM.

## Why use a Lead Magnet

Use a Lead Magnet when you want visitors who run your public agent to first opt in to communications. This ensures you can follow up and automatically add the user to your CRM (e.g., HubSpot).

Common scenarios:

* Capture newsletter/demo opt-ins before running an assistant
* Gate premium agents behind a quick consent form
* Sync new leads directly to HubSpot contacts (optionally create deals)

***

## How it works (toggle-based)

1. In Builder settings, turn on **Lead Magnet** (after connecting HubSpot).
2. Agent.ai automatically displays a consent UI (email + opt-in) before the run.
3. On accept, Agent.ai automatically creates/updates the contact in HubSpot.
4. Your agent then runs as normal.

Notes:

* No custom prompt or consent form required — it’s built-in.
* No manual contact creation step — Agent.ai handles that for you.
* You can still enrich, associate, or update properties later in your workflow if you want.

***

## Configure your Lead Magnet

1. **Prepare HubSpot**

* Connect HubSpot: [HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup)
* Confirm write scopes for Contacts

2. **Toggle Lead Magnet on**

* Agent.ai will present the consent UI and collect email automatically

3. **Optional: create a deal or subscription**

* Create a deal associated with the contact
* Or add them to a specific list or workflow

4. **Proceed to the agent flow**

* After consent and contact sync, your agent executes its steps

***

## Best practices

* Keep the opt-in step short (email + one checkbox)
* Clearly explain value of opting in
* Set `lead_source` (e.g., "Agent Magnet") for reporting
* Respect user consent; don’t proceed without it
* Add an audit note via [Create Timeline Event](../actions/hubspot-v2-create-timeline-event)

***

## Troubleshooting

* Contact not created? Verify OAuth scopes and that Lead Magnet is enabled
* Unexpected duplicates? Contact creation is automatic; if you add manual creates, ensure you check first
* Not showing in lists? Confirm internal property names and values

***

## Related

* Start here: [Using Agent.ai with HubSpot](../builder/using-hubspot)
* Actions: [Lookup](../actions/hubspot-v2-lookup-object), [Create](../actions/hubspot-v2-create-object), [Update](../actions/hubspot-v2-update-object)
* Guides: [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers)

***

## Visual

<img src="https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=3517dab5a2cc74dd0c6b22da59b881bd" alt="Lead Magnet Flow" data-og-width="920" width="920" data-og-height="240" height="240" data-path="images/lead-magnet-hero.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=280&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=c540792eb205be3d28499bc8a74d2da5 280w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=560&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=97446eae5af18b507cc8e7d0cfe54608 560w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=840&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=aa20f5da15b550eb512fb69212d451c0 840w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=1100&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=4b3a47a5dcb067d5719e78fc0d5ab97c 1100w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=1650&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=985f732eb62e26eaf30ff9d55c6355c1 1650w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=2500&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=53e64063e8f48e9209767a05988c35c5 2500w" />
