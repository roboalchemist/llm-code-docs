# Source: https://docs.agent.ai/recipes/hubspot-deal-analysis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# HubSpot Deal Analysis

> Automatically analyze deals using AI, review timeline history, and update records with health scores and next-step recommendations

Automatically analyze deals using AI, review timeline history, and update records with health scores and next-step recommendations.

**What it does:** Finds deals in a specific stage, analyzes each one using AI and historical data, then updates the deal with insights.

**Common uses:**

* Daily deal health checks
* Pipeline review automation
* Identify at-risk deals
* Generate AI-powered next steps
* Scale deal analysis across entire pipeline

**Complexity:** Intermediate - Uses search, loops, AI analysis, and updates

***

## Overview

This workflow combines HubSpot data with AI analysis to automatically assess deal health. For each deal in your target stage, it:

1. Searches for deals in a specific stage
2. Loops through each deal
3. Gets timeline events for historical context
4. Sends deal data + timeline to AI for analysis
5. Updates the deal with AI-generated insights

**Result:** Every deal gets a health score, risk assessment, and recommended next steps automatically.

***

## What You'll Need

### HubSpot Setup

**Custom Properties** (create these in HubSpot → Settings → Properties → Deals):

* `ai_health_score` (Number) - Stores 1-10 health rating
* `ai_risks` (Multi-line text) - Stores identified risks
* `ai_next_steps` (Multi-line text) - Stores recommended actions
* `ai_close_likelihood` (Single-line text) - Stores probability assessment

**Permissions:**

* Read Deals
* Write Deals
* Read Timeline Events

### Agent.AI Setup

**Actions needed:**

* Search HubSpot (V2)
* For Loop
* Get Timeline Events (V2)
* Invoke LLM (or Generate Content)
* Update HubSpot Object (V2)
* End Loop

**LLM Access:**

* OpenAI, Anthropic, or other LLM provider configured

***

## Step-by-Step Setup

### Step 1: Add a Trigger

Choose how to run this workflow:

**Option A: Scheduled (Recommended)**

* Trigger: Schedule
* Frequency: Daily at 9:00 AM
* Use for: Regular pipeline health checks

**Option B: Manual**

* Trigger: Manual
* Use for: On-demand analysis

### Step 2: Search for Target Deals

**Add action:** Search HubSpot (V2)

**Configuration:**

* **Object Type:** Deals
* **Search Filters:** Click "+ Add Property"
  * Property: Deal Stage
  * Operator: Equals
  * Value: "presentationscheduled" (or your target stage)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `hs_object_id`
  * `pipeline`
  * `hubspot_owner_id`
* **Sort:** `-createdate` (newest first)
* **Limit:** 50 (adjust based on your needs)
* **Output Variable:** `target_deals`

**What this does:** Finds all deals in "Presentation Scheduled" stage (or whatever stage you chose), gets their key details.

### Step 3: Start Loop

**Add action:** For Loop

**Configuration:**

* **Loop through:** Click `{}` → select `target_deals`
* **Current item variable:** `current_deal`

**What this does:** Processes each deal one at a time.

### Step 4: Get Timeline Events

**Add action:** Get Timeline Events (V2)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `current_deal` → `hs_object_id`
* **Event Type Filter:** Leave blank (get all events)
* **Output Variable:** `deal_timeline`

**What this does:** Gets the complete timeline history for the current deal (emails, calls, meetings, notes, custom events).

### Step 5: AI Analysis

**Add action:** Invoke LLM (or Generate Content)

**Configuration:**

* **Prompt:**

```
Analyze this deal and provide insights:

Deal Name: {{current_deal.dealname}}
Stage: {{current_deal.dealstage}}
Amount: ${{current_deal.amount}}
Close Date: {{current_deal.closedate}}

Timeline History:
{{deal_timeline}}

Please provide:
1. Deal health score (1-10, where 10 is healthiest)
2. Key risks or concerns
3. Recommended next steps (3-5 specific actions)
4. Likelihood to close (percentage or descriptive)

Return as JSON with keys: health_score, risks, next_steps, close_likelihood
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `deal_insights`

**What this does:** AI analyzes the deal using all available context and generates actionable insights.

**Tip:** Adjust the prompt to match your sales process. Ask about specific things that matter to your team.

### Step 6: Update Deal with Insights

**Add action:** Update HubSpot Object (V2)

**Configuration:**

* **Object Type:** Deals
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → `current_deal` → `hs_object_id`
* **Update Properties:** Click "+ Add Property" and select your custom properties:
  * `ai_health_score`: Click `{}` → `deal_insights` → `health_score`
  * `ai_risks`: Click `{}` → `deal_insights` → `risks`
  * `ai_next_steps`: Click `{}` → `deal_insights` → `next_steps`
  * `ai_close_likelihood`: Click `{}` → `deal_insights` → `close_likelihood`
* **Output Variable:** `updated_deal`

**What this does:** Saves AI insights back to the deal record so your team can see them in HubSpot.

### Step 7: Close the Loop

**Add action:** End Loop

**What this does:** Marks the end of the loop. Workflow jumps back to Step 3 and processes the next deal.

### Step 8 (Optional): Send Summary

**Add action:** Send Email (after the loop)

**Configuration:**

* **To:** Your email or sales team email
* **Subject:** "Deal Analysis Complete"
* **Body:** "Analyzed and updated insights for all deals in Presentation Scheduled stage."

**What this does:** Notifies you when the workflow finishes.

***

## How It Works

**Execution flow:**

1. **Search** finds 50 deals in "Presentation Scheduled" stage → saves to `target_deals`
2. **For Loop** starts with first deal → `current_deal` = Deal #1
3. **Get Timeline Events** retrieves history for Deal #1 → saves to `deal_timeline`
4. **Invoke LLM** analyzes Deal #1 + timeline → saves insights to `deal_insights`
5. **Update** writes insights back to Deal #1 in HubSpot
6. **End Loop** → Jump back to step 2, `current_deal` = Deal #2
7. Repeat until all 50 deals are analyzed
8. **Send Email** (optional) notifies team

**Example timeline:** 50 deals × \~5 seconds per deal = \~4 minutes total

***

## Example Output

### What the AI Generates

**For a deal named "Acme Corp - Enterprise License":**

```json  theme={null}
{
  "health_score": 7,
  "risks": "Customer has not responded to follow-up in 5 days. Technical questions from demo suggest potential integration concerns. Close date is 30 days away but no next meeting scheduled.",
  "next_steps": "1. Send follow-up email addressing technical questions\n2. Offer integration consultation call with solutions engineer\n3. Share case study from similar customer in manufacturing industry\n4. Schedule technical deep-dive meeting\n5. Create custom proposal addressing integration concerns",
  "close_likelihood": "Medium-High (65%)"
}
```

### What Appears in HubSpot

In the deal record, you'll see:

* **AI Health Score:** 7
* **AI Risks:** "Customer has not responded to follow-up in 5 days..."
* **AI Next Steps:** "1. Send follow-up email... 2. Offer integration consultation..."
* **AI Close Likelihood:** "Medium-High (65%)"

Sales reps can see these insights directly on the deal record and take action.

***

## Customization Ideas

### Different Target Stages

Change which stage to analyze:

* **Search Filter Value:** Change from "presentationscheduled" to:
  * "qualifiedtobuy" - Recently qualified deals
  * "decisionmakerboughtin" - Deals nearing close
  * "contractsent" - Contracts waiting for signature

### Multiple Stages

Run separate workflows for different stages, or add an If Condition inside the loop to handle different stages differently.

### Different AI Focus

Customize the LLM prompt for different analysis types:

**For early-stage deals:**

```
Focus on: qualification quality, budget alignment, decision maker access
```

**For late-stage deals:**

```
Focus on: contract negotiation status, closing risks, urgency signals
```

**For stalled deals:**

```
Focus on: reasons for stall, re-engagement strategies, win-back probability
```

### Add Filters

Only analyze deals meeting certain criteria:

**After Get Timeline Events, add If Condition:**

* Condition: Check if timeline has any events in last 7 days
* If no recent activity → Tag as "stalled"
* If has activity → Run AI analysis

### Segment by Owner

**After Search, add another loop:**

* Group deals by `hubspot_owner_id`
* Send each owner a summary of their deals

***

## Troubleshooting

### No Deals Found

**Search returns empty array**

**Causes:**

1. No deals in that stage
2. Wrong stage name (check exact value in HubSpot)
3. Missing permissions

**Fix:**

1. Check HubSpot - do deals exist in that stage?
2. Get exact stage value: Go to HubSpot → Deal → Check "Deal Stage" property
3. Verify "Read Deals" permission

### AI Insights Not Formatted Correctly

**Deal properties contain raw JSON or malformed text**

**Causes:**

1. LLM didn't follow JSON format instruction
2. Template variable rendering issue

**Fix:**

1. Make prompt more explicit: "Return ONLY valid JSON, nothing else"
2. Test with a single deal first
3. Try different LLM model (GPT-4 better at structured output than GPT-3.5)
4. Parse JSON in a Set Variable action before updating

### Custom Properties Not Found

**Error: "Property 'ai\_health\_score' does not exist"**

**Causes:**

1. Custom properties not created in HubSpot
2. Properties created but not for Deals object

**Fix:**

1. Go to HubSpot → Settings → Properties → Deals
2. Create custom properties:
   * `ai_health_score` (Number, 0-10)
   * `ai_risks` (Multi-line text)
   * `ai_next_steps` (Multi-line text)
   * `ai_close_likelihood` (Single-line text)
3. Save and try again

### Timeline Too Long

**LLM times out or returns incomplete response**

**Causes:**

1. Timeline has hundreds of events
2. Exceeding token limit

**Fix:**

1. Add result limit to Get Timeline Events action
2. Filter by date range (last 30 days)
3. Filter by event type (only important events)
4. Use LLM with larger context window

### Loop Takes Too Long

**Workflow times out**

**Causes:**

1. Too many deals (1000+)
2. LLM calls are slow

**Fix:**

1. Reduce search limit to 50-100 deals
2. Run multiple smaller workflows instead of one large one
3. Filter deals by date (only deals from last 30 days)

***

## Tips & Best Practices

**✅ Do:**

* Start with small search limit (10-20 deals) to test
* Review AI-generated insights for a few deals before scaling
* Adjust prompt based on what your team actually needs
* Create custom properties in HubSpot before running workflow
* Use scheduled trigger for daily automated analysis
* Monitor execution logs to see how long each deal takes

**❌ Don't:**

* Analyze thousands of deals at once (splits into batches)
* Forget to create custom properties in HubSpot first
* Use vague prompts (be specific about what you want)
* Skip testing with a few deals first
* Analyze the same stage multiple times a day (redundant)

**Cost optimization:**

* LLM calls cost money - monitor usage
* Use cheaper models (GPT-3.5) for simple analysis
* Limit timeline events to reduce tokens
* Only analyze deals that changed recently (add date filter)

***

## Related Resources

**Actions used:**

* [Search HubSpot (V2)](../actions/hubspot-v2-search-objects)
* [For Loop](../actions/for_loop)
* [Get Timeline Events (V2)](../actions/hubspot-v2-get-timeline-events)
* [Update HubSpot Object (V2)](../actions/hubspot-v2-update-object)
* [End Loop](../actions/end_statement)

**Related workflows:**

* [HubSpot Contact Enrichment](./hubspot-contact-enrichment) - Similar pattern for contacts
* [HubSpot Customer Onboarding](./hubspot-customer-onboarding) - Multi-stage workflow example

***

**Last Updated:** 2025-10-01
