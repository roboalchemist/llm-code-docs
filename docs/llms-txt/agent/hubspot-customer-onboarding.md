# Source: https://docs.agent.ai/recipes/hubspot-customer-onboarding.md

# HubSpot Customer Onboarding

> Automatically kickoff customer onboarding when deals close - analyze relationship history, generate personalized onboarding plans, and create timeline events with next steps

Automatically kickoff customer onboarding when deals close - analyze relationship history, generate personalized onboarding plans, and create timeline events with next steps.

**What it does:** Triggered when a deal closes, looks up customer details and engagement history, uses AI to create onboarding plan, and logs next steps to HubSpot timeline.

**Common uses:**

* Automate onboarding kickoff
* Generate personalized welcome sequences
* Ensure consistent onboarding experience
* Provide context to success team
* Track onboarding milestones

**Complexity:** Advanced - Uses webhooks, lookups, associations, engagements, AI analysis, and multiple timeline events

***

## Overview

This workflow automates the transition from sales to customer success when a deal closes. It:

1. Receives webhook when deal reaches "Closed Won"
2. Looks up deal details with associated contacts and companies
3. Gets primary contact information
4. Retrieves engagement history (calls, emails, meetings)
5. Uses AI to analyze relationship and create onboarding plan
6. Creates timeline events with personalized next steps
7. (Optional) Notifies success team

**Result:** Customer success team gets complete context and AI-generated onboarding plan the moment a deal closes.

***

## What You'll Need

### HubSpot Setup

**HubSpot Workflow (to trigger onboarding):**

* Trigger: Deal stage changed to "Closed Won"
* Action: Send webhook to Agent.AI
* Payload includes: `deal_id`, `deal_name`, `deal_amount`, `close_date`

**Permissions:**

* Read Deals
* Read Contacts
* Read Companies
* Read Engagements
* Write Timeline Events

**Optional Properties:**

* Custom deal properties for onboarding tracking
* Onboarding status field
* Implementation timeline field

### Agent.AI Setup

**Actions needed:**

* Webhook Trigger
* Lookup HubSpot Object (V2) - Used multiple times
* Get Engagements (V2) - Used multiple times
* Invoke LLM
* Create Timeline Event (V2) - Used multiple times
* If Condition (optional, for conditional logic)

**Requirements:**

* LLM access (OpenAI, Anthropic, etc.)

***

## Step-by-Step Setup

### Step 1: Create the Agent.AI Workflow

**Add trigger:** Webhook

**Configuration:**

* Copy the webhook URL (you'll need this for HubSpot)
* Expected variables from HubSpot:
  * `_hubspot_portal` (automatically included)
  * `deal_id` (deal's HubSpot ID)
  * `deal_name` (deal name for context)
  * `deal_amount` (contract value)
  * `close_date` (when deal closed)

### Step 2: Setup HubSpot Workflow

**In HubSpot:**

1. Go to Automation → Workflows
2. Create workflow
3. **Trigger:** Deal stage changed to "Closed Won"
4. **Add action:** Send webhook
5. **Webhook URL:** Paste Agent.AI webhook URL from Step 1
6. **Method:** POST
7. **Payload:**

```json  theme={null}
{
  "_hubspot_portal": "{{portal.id}}",
  "deal_id": "{{deal.hs_object_id}}",
  "deal_name": "{{deal.dealname}}",
  "deal_amount": "{{deal.amount}}",
  "close_date": "{{deal.closedate}}"
}
```

8. Save and activate

**Now when deals reach "Closed Won", this webhook fires.**

### Step 3: Lookup Deal with Associations

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Deals
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → select `deal_id` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `pipeline`
  * `deal_type`
  * `contract_start_date`
  * `hs_object_id`
* **Retrieve Associations:** Select "Contacts" and "Companies"
* **Output Variable:** `deal_data`

**What this does:** Gets complete deal info plus IDs of associated contacts and companies.

### Step 4: Lookup Primary Contact

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → `deal_data` → `associations` → `contacts` → `[0]` → `id`
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `phone`
  * `jobtitle`
  * `department`
  * `hs_object_id`
* **Output Variable:** `primary_contact`

**What this does:** Gets detailed info about the primary contact (first associated contact).

**Note:** `[0]` gets the first contact from the associations array. You could add an If Condition to find a specific contact role instead.

### Step 5: Get Deal Engagement History

**Add action:** Get Engagements (V2)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → select `deal_id` (from webhook)
* **Engagement Types:** Select "Calls", "Emails", "Meetings", "Notes"
* **Limit:** 50
* **Output Variable:** `deal_engagements`

**What this does:** Retrieves all sales interactions (calls, emails, meetings, notes) associated with this deal.

### Step 6: Get Contact Engagement History

**Add action:** Get Engagements (V2)

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** Click `{}` → `primary_contact` → `id`
* **Engagement Types:** Select "Calls", "Emails", "Meetings", "Notes"
* **Limit:** 50
* **Output Variable:** `contact_engagements`

**What this does:** Gets engagement history for the primary contact (might include interactions beyond this deal).

### Step 7: AI Onboarding Analysis

**Add action:** Invoke LLM

**Configuration:**

* **Prompt:**

```
Create a personalized customer onboarding plan based on this context:

DEAL INFORMATION:
- Deal: {{deal_data.properties.dealname}}
- Amount: ${{deal_data.properties.amount}}
- Close Date: {{deal_data.properties.closedate}}
- Contract Start: {{deal_data.properties.contract_start_date}}

PRIMARY CONTACT:
- Name: {{primary_contact.properties.firstname}} {{primary_contact.properties.lastname}}
- Title: {{primary_contact.properties.jobtitle}}
- Email: {{primary_contact.properties.email}}
- Department: {{primary_contact.properties.department}}

RELATIONSHIP HISTORY:
Deal Engagements: {{deal_engagements}}
Contact Engagements: {{contact_engagements}}

Based on this context, provide:

1. Onboarding complexity (Low/Medium/High)
2. Key stakeholders identified from engagements
3. Technical requirements mentioned in sales conversations
4. Recommended onboarding timeline (in days)
5. First 3 onboarding milestones with specific actions
6. Potential risks or concerns to watch for
7. Personalized welcome message for customer success team

Format as JSON with keys: complexity, stakeholders, technical_requirements, timeline_days, milestones, risks, welcome_message
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `onboarding_plan`

**What this does:** AI analyzes all context and creates a detailed, personalized onboarding plan.

### Step 8: Create Kickoff Timeline Event

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `deal_id`
* **Event Type:** `onboarding_kickoff`
* **Event Title:** "Onboarding Plan Generated"
* **Event Description:** Click `{}` → `onboarding_plan` → `welcome_message`
* **Event Properties:**
  ```
  complexity={{onboarding_plan.complexity}}
  timeline_days={{onboarding_plan.timeline_days}}
  ```
* **Output Variable:** `kickoff_event`

**What this does:** Logs that onboarding started with AI-generated plan details.

### Step 9: Create Milestone Events (Loop Optional)

**Add action:** Create Timeline Event (V2) - Repeat for each milestone

**Milestone 1:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `deal_id`
* **Event Type:** `onboarding_milestone`
* **Event Title:** "Milestone 1: " then click `{}` → `onboarding_plan` → `milestones` → `[0]`
* **Event Description:** Type "First milestone for customer onboarding"
* **Output Variable:** `milestone_1_event`

**Milestone 2:**

* Same pattern, using `milestones[1]`

**Milestone 3:**

* Same pattern, using `milestones[2]`

**What this does:** Creates separate timeline events for each onboarding milestone so success team can track progress.

### Step 10: Create Contact Timeline Event

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → `primary_contact` → `id`
* **Event Type:** `customer_onboarding_start`
* **Event Title:** "Customer Onboarding Started"
* **Event Description:** Type "Onboarding kickoff for " then click `{}` → `deal_data` → `properties` → `dealname`
* **Event Properties:**
  ```
  deal_id={{deal_id}}
  complexity={{onboarding_plan.complexity}}
  ```
* **Output Variable:** `contact_event`

**What this does:** Logs onboarding start on the contact record too (visible in contact timeline).

### Step 11 (Optional): Send Notification

**Add action:** Send Email

**Configuration:**

* **To:** [success-team@yourcompany.com](mailto:success-team@yourcompany.com)
* **Subject:** Type "New Customer Onboarding: " then click `{}` → select `deal_name`
* **Body:**

```
New customer onboarding ready!

Deal: {{deal_name}}
Amount: ${{deal_amount}}
Primary Contact: {{primary_contact.properties.firstname}} {{primary_contact.properties.lastname}}

Onboarding Complexity: {{onboarding_plan.complexity}}
Timeline: {{onboarding_plan.timeline_days}} days

Key Stakeholders:
{{onboarding_plan.stakeholders}}

Technical Requirements:
{{onboarding_plan.technical_requirements}}

Milestones:
{{onboarding_plan.milestones}}

Risks to Watch:
{{onboarding_plan.risks}}

View in HubSpot: [link to deal]
```

**What this does:** Notifies customer success team with full onboarding plan.

***

## How It Works

**Execution flow:**

1. **Deal closes** in HubSpot → reaches "Closed Won" stage
2. **HubSpot workflow fires webhook** to Agent.AI with deal ID
3. **Lookup Deal** gets full deal details + associated contact/company IDs → `deal_data`
4. **Lookup Primary Contact** gets contact details → `primary_contact`
5. **Get Deal Engagements** retrieves sales history → `deal_engagements`
6. **Get Contact Engagements** retrieves contact history → `contact_engagements`
7. **AI Analysis** combines all context → generates onboarding plan → `onboarding_plan`
8. **Create Timeline Events** logs kickoff + milestones to deal and contact
9. **Send Email** (optional) notifies success team

**Timeline:** \~15-20 seconds from deal close to complete onboarding plan

***

## Example Output

### What the AI Generates

**For "Acme Corp - Enterprise License" deal:**

```json  theme={null}
{
  "complexity": "High",

  "stakeholders": "VP of Engineering (John Doe - primary), CTO (mentioned in demo call), IT Manager (security discussions), 3 engineering team members attended technical deep-dive",

  "technical_requirements": "SSO integration required, custom API endpoints for internal tools, data migration from legacy system, dedicated environment for testing, compliance review for data handling",

  "timeline_days": 90,

  "milestones": [
    "Week 1-2: Kickoff call, technical discovery, SSO setup",
    "Week 3-6: Core implementation, API integration, data migration planning",
    "Week 7-12: Testing, training sessions, compliance review, go-live preparation"
  ],

  "risks": "Complex SSO requirements may delay timeline. Data migration complexity not fully scoped. Multiple stakeholders need alignment. Customer mentioned tight deadline for Q1 launch.",

  "welcome_message": "Welcome to Acme Corp! This is a high-value enterprise customer with sophisticated technical requirements. VP of Engineering John Doe is your primary contact and has been very engaged throughout the sales process. Key focus: deliver SSO and API integration within 90 days to meet their Q1 launch deadline. Multiple stakeholders need coordination - schedule kickoff call with all parties ASAP."
}
```

### What Appears in HubSpot

**On the Deal timeline:**

* **Event:** "Onboarding Plan Generated"
* **Description:** "Welcome to Acme Corp! This is a high-value enterprise customer..."
* **Properties:** complexity=High, timeline\_days=90

**Three milestone events:**

* "Milestone 1: Week 1-2: Kickoff call, technical discovery, SSO setup"
* "Milestone 2: Week 3-6: Core implementation, API integration..."
* "Milestone 3: Week 7-12: Testing, training sessions..."

**On the Contact timeline:**

* **Event:** "Customer Onboarding Started"
* **Description:** "Onboarding kickoff for Acme Corp - Enterprise License"

**Email to success team:**
Subject: "New Customer Onboarding: Acme Corp - Enterprise License"
Body contains full onboarding plan with all details

***

## Customization Ideas

### Different Trigger Conditions

**In HubSpot workflow:**

* Trigger on specific deal types only (enterprise vs. standard)
* Trigger when ticket type = "New Customer Onboarding"
* Trigger when deal reaches "Implementation" stage

### Conditional Onboarding Paths

**Add If Condition after AI analysis:**

* If complexity = "High" → Assign to senior success manager
* If complexity = "Low" → Use automated onboarding sequence
* If deal amount > \$100k → Create dedicated Slack channel

### Company-Level Analysis

**Add step to lookup company:**

* Get company details from `deal_data.associations.companies[0].id`
* Include company size, industry, tech stack in AI analysis
* Adjust onboarding based on company profile

### Integration with Other Systems

**After onboarding plan:**

* Create Jira tickets for technical milestones
* Add tasks to project management tool
* Create Slack channel for customer
* Send calendar invites for milestone meetings

### Multi-Contact Analysis

**Instead of just primary contact:**

* Loop through all associated contacts
* Get engagements for each
* Identify decision makers, technical champions, end users
* Create onboarding plan for each role

***

## Troubleshooting

### No Associated Contacts

**Deal has no contacts associated**

**Causes:**

1. Deal created without contact association
2. Contact association removed

**Fix:**

1. Add If Condition after Step 3 to check if `deal_data.associations.contacts` exists
2. If empty, skip contact lookup and use deal-only onboarding
3. Or create timeline event flagging missing contact

### Engagement History Empty

**No engagements returned**

**Causes:**

1. Deal/contact has no logged engagements
2. Permissions issue

**Fix:**

1. Check "Read Engagements" permission
2. Add fallback message: "No engagement history available"
3. AI can still create onboarding plan without history
4. Log note to manually research customer

### AI Response Too Generic

**Onboarding plan lacks specifics**

**Causes:**

1. Limited engagement history
2. Prompt not specific enough
3. Missing key context

**Fix:**

1. Add more specific prompts about what to look for
2. Include additional data sources (timeline events, notes)
3. Ask AI to highlight unknowns or gaps
4. Request specific questions for kickoff call

### Timeline Events Not Creating

**Events fail to create**

**Causes:**

1. Missing permissions
2. Event type name invalid
3. Target object ID wrong

**Fix:**

1. Verify "Write Timeline Events" permission
2. Use lowercase with underscores for event type
3. Check execution log for exact error
4. Verify object IDs are correct

***

## Tips & Best Practices

**✅ Do:**

* Test with closed-won test deals first
* Include engagement limit (50 is reasonable)
* Create distinct event types for each milestone
* Log events to both deal and contact
* Include complexity assessment
* Provide success team with full context
* Track which engagements matter most (demos, technical calls)

**❌ Don't:**

* Assume primary contact is always first in array (add validation)
* Skip error handling for missing associations
* Create generic onboarding plans (use specific context)
* Forget to notify success team
* Overwhelm with too many timeline events
* Include sensitive sales notes in onboarding plan

**Performance tips:**

* Engagement retrieval is fast (under 2 seconds)
* LLM analysis takes 5-10 seconds with full context
* Consider limiting engagement count for very old deals
* Cache onboarding templates for common scenarios

**Success metrics to track:**

* Time from deal close to onboarding kickoff
* Onboarding completion rate by complexity level
* Accuracy of AI timeline predictions
* Success team satisfaction with plan quality

***

## Related Resources

**Actions used:**

* [Lookup HubSpot Object (V2)](../actions/hubspot-v2-lookup-object)
* [Get Engagements (V2)](../actions/hubspot-v2-get-engagements)
* [Create Timeline Event (V2)](../actions/hubspot-v2-create-timeline-event)

**Related workflows:**

* [HubSpot Deal Analysis](./hubspot-deal-analysis) - Similar AI analysis with loops
* [HubSpot Contact Enrichment](./hubspot-contact-enrichment) - Webhook-triggered automation

***

**Last Updated:** 2025-10-01
