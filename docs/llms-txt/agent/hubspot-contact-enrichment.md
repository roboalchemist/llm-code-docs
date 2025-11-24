# Source: https://docs.agent.ai/recipes/hubspot-contact-enrichment.md

# HubSpot Contact Enrichment

> Automatically enrich contact records with company intelligence, news, and AI-powered insights whenever a contact is created or updated

Automatically enrich contact records with company intelligence, news, and AI-powered insights whenever a contact is created or updated.

**What it does:** Triggered by HubSpot, looks up contact details, searches the web for company info, generates AI insights, updates the contact, and logs the enrichment.

**Common uses:**

* Auto-research new leads
* Keep contact data current
* Provide sales context automatically
* Generate talking points for outreach
* Track enrichment history

**Complexity:** Intermediate - Uses webhooks, lookups, web search, AI analysis, and updates

***

## Overview

This workflow automatically enriches contacts the moment they're created or updated in HubSpot. It:

1. Receives webhook from HubSpot (contact created/updated)
2. Looks up full contact details
3. Searches web for company news and info
4. Uses AI to analyze and summarize intelligence
5. Updates contact with enrichment data
6. Creates timeline event to track enrichment

**Result:** Sales reps get instant context about new contacts without manual research.

***

## What You'll Need

### HubSpot Setup

**HubSpot Workflow (to trigger enrichment):**

* Trigger: Contact created OR Contact property changed
* Action: Send webhook to Agent.AI
* Payload includes: `contact_id`, `contact_email`, `contact_company`

**Custom Properties** (create in HubSpot → Settings → Properties → Contacts):

* `company_overview` (Multi-line text) - AI-generated company summary
* `recent_news` (Multi-line text) - News summary
* `talking_points` (Multi-line text) - Sales talking points
* `relevance_score` (Number) - 1-10 priority rating
* `outreach_approach` (Multi-line text) - Recommended approach
* `last_enriched` (Date) - Track when enriched

**Permissions:**

* Read Contacts
* Write Contacts
* Read Timeline Events
* Write Timeline Events

### Agent.AI Setup

**Actions needed:**

* Webhook Trigger
* Lookup HubSpot Object (V2)
* Get Search Results (web search)
* Invoke LLM
* Update HubSpot Object (V2)
* Create Timeline Event (V2)

**Requirements:**

* Web search API access (Google, Bing, or similar)
* LLM access (OpenAI, Anthropic, etc.)

***

## Step-by-Step Setup

### Step 1: Create the Agent.AI Workflow

**Add trigger:** Webhook

**Configuration:**

* Copy the webhook URL (you'll need this for HubSpot)
* Expected variables from HubSpot:
  * `_hubspot_portal` (automatically included)
  * `contact_id` (contact's HubSpot ID)
  * `contact_email` (contact's email)
  * `contact_company` (contact's company name)

### Step 2: Setup HubSpot Workflow

**In HubSpot:**

1. Go to Automation → Workflows
2. Create workflow
3. **Trigger:** Contact created OR Contact property "Email" is known
4. **Add action:** Send webhook
5. **Webhook URL:** Paste Agent.AI webhook URL from Step 1
6. **Method:** POST
7. **Payload:**

```json  theme={null}
{
  "_hubspot_portal": "[portal.id]",
  "contact_id": "[contact.hs_object_id]",
  "contact_email": "[contact.email]",
  "contact_company": "[contact.company]"
}
```

8. Save and activate

**Now when contacts are created in HubSpot, this webhook fires.**

### Step 3: Lookup Full Contact Details

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → select `contact_id` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `company`
  * `jobtitle`
  * `phone`
  * `city`
  * `state`
  * `country`
  * `industry`
  * `hs_object_id`
* **Retrieve Associations:** Select "Companies" (get associated company records)
* **Output Variable:** `contact_data`

**What this does:** Gets complete contact profile with all details for enrichment.

### Step 4: Web Search for Company Info

**Add action:** Get Search Results (or Web Search)

**Configuration:**

* **Query:** Type text and insert variables:
  * Click `{}` → `contact_data` → `properties` → `company`
  * Type " news funding products recent"
* **Number of Results:** 5
* **Output Variable:** `web_research`

**Example query:** "Acme Corp news funding products recent"

**What this does:** Finds recent news, funding announcements, product launches, and company updates.

### Step 5: AI Enrichment Analysis

**Add action:** Invoke LLM

**Configuration:**

* **Prompt:**

```
Analyze this contact and create an enrichment summary:

Contact Information:
- Name: [contact first name] [contact last name]
- Title: [contact job title]
- Company: [contact company]
- Industry: [contact industry]
- Location: [contact city], [contact state]

Recent Company News & Information:
[web research results]

Please provide:
1. Company overview (2-3 sentences describing the company)
2. Recent news summary (key highlights from search results)
3. Talking points for sales (3-5 specific conversation starters)
4. Contact relevance score (1-10, where 10 is highest priority)
5. Recommended outreach approach (1-2 sentences)

Return as JSON with keys: company_overview, news_summary, talking_points, relevance_score, outreach_approach
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `enrichment_insights`

**What this does:** AI analyzes all gathered data and creates actionable sales intelligence.

### Step 6: Update Contact with Enrichment

**Add action:** Update HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → select `contact_id` (from webhook)
* **Update Properties:** Click "+ Add Property" and select custom properties:
  * `company_overview`: Click `{}` → `enrichment_insights` → `company_overview`
  * `recent_news`: Click `{}` → `enrichment_insights` → `news_summary`
  * `talking_points`: Click `{}` → `enrichment_insights` → `talking_points`
  * `relevance_score`: Click `{}` → `enrichment_insights` → `relevance_score`
  * `outreach_approach`: Click `{}` → `enrichment_insights` → `outreach_approach`
  * `last_enriched`: Type `[now]` or use current date variable
* **Output Variable:** `updated_contact`

**What this does:** Writes all enrichment data back to HubSpot contact record.

### Step 7: Log Enrichment Activity

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → select `contact_id`
* **Event Type:** `contact_enriched`
* **Event Title:** "Contact Enriched with AI Insights"
* **Event Description:** Type "Enriched contact with company research and AI analysis. Relevance score: " then click `{}` → `enrichment_insights` → `relevance_score`
* **Event Properties:** (optional)
  ```
  sources=[web_research]
  ai_model=gpt-4
  ```
* **Event Timestamp:** Leave blank (uses current time)
* **Output Variable:** `enrichment_event`

**What this does:** Creates audit trail showing when and how contact was enriched.

***

## How It Works

**Execution flow:**

1. **Contact created in HubSpot** (e.g., from form submission)
2. **HubSpot workflow fires webhook** to Agent.AI with contact ID
3. **Lookup** gets full contact profile from HubSpot → `contact_data`
4. **Web Search** finds recent company news → `web_research`
5. **AI Analysis** combines contact + news → generates insights → `enrichment_insights`
6. **Update** writes enrichment data to contact record in HubSpot
7. **Timeline Event** logs that enrichment occurred

**Timeline:** \~10-15 seconds from contact creation to enriched profile

***

## Example Output

### What the AI Generates

**For contact "John Doe, VP Engineering at Acme Corp":**

```json  theme={null}
{
  "company_overview": "Acme Corp is a fast-growing enterprise AI platform company based in San Francisco. Recently raised $50M Series B led by Sequoia Capital, indicating strong investor confidence and expansion plans. Focus on enterprise machine learning solutions.",

  "news_summary": "Recent $50M Series B funding announced. New enterprise features launched including advanced analytics and custom model training. Expanding engineering team by 50% in next 6 months. Featured in TechCrunch for innovative AI approach.",

  "talking_points": "1. Congratulate on recent $50M Series B funding\n2. Discuss new enterprise features and how they align with engineering priorities\n3. Reference expansion plans and potential partnership opportunities\n4. Mention TechCrunch feature and industry recognition\n5. Connect on engineering team growth and talent needs",

  "relevance_score": 9,

  "outreach_approach": "High-priority contact. VP of Engineering at well-funded, rapidly growing company. Lead with technical value proposition and enterprise case studies. Timing is ideal given their product launch and team expansion."
}
```

### What Appears in HubSpot

In the contact record, sales reps see:

**Company Overview:**
"Acme Corp is a fast-growing enterprise AI platform company..."

**Recent News:**
"Recent \$50M Series B funding announced. New enterprise features..."

**Talking Points:**
"1. Congratulate on recent \$50M Series B funding
2\. Discuss new enterprise features..."

**Relevance Score:** 9

**Outreach Approach:**
"High-priority contact. VP of Engineering at well-funded..."

**Timeline Event:**
"Contact Enriched with AI Insights - Relevance score: 9"

***

## Customization Ideas

### Different Trigger Conditions

**In HubSpot workflow:**

* Trigger on specific forms (only enrich demo requests)
* Trigger on lifecycle stage change (enrich when MQL)
* Trigger on company property change (re-enrich when company changes)

### Industry-Specific Research

**Customize web search query:**

* Tech companies: "\[company] funding product launch tech news"
* Manufacturing: "\[company] acquisitions capacity expansion news"
* Healthcare: "\[company] FDA approvals clinical trials news"

### Different Enrichment Focus

**Adjust AI prompt for different goals:**

**For sales:**

```
Focus on: buying signals, budget indicators, decision maker access, competitive landscape
```

**For recruiting:**

```
Focus on: company culture, growth trajectory, engineering team size, tech stack
```

**For partnerships:**

```
Focus on: strategic initiatives, market positioning, partner ecosystem, expansion plans
```

### Conditional Enrichment

**Add If Condition after lookup:**

* Only enrich if `jobtitle` contains "VP", "Director", "C-level"
* Only enrich if `relevance_score` > 7
* Only enrich if company size > 100 employees

### Multi-Language Support

**For international contacts:**

* Detect `country` from contact data
* Adjust web search language
* Request AI response in appropriate language

***

## Troubleshooting

### Webhook Not Firing

**Agent.AI workflow doesn't run when contact created**

**Causes:**

1. HubSpot workflow not active
2. Webhook URL incorrect
3. Contact doesn't meet trigger criteria

**Fix:**

1. Check HubSpot workflow status (Automation → Workflows)
2. Verify webhook URL matches Agent.AI URL exactly
3. Test with a contact that definitely meets trigger conditions
4. Check HubSpot workflow execution history

### No Web Results

**Web search returns empty or irrelevant results**

**Causes:**

1. Company name is generic or missing
2. Search API limit reached
3. Company is very small/new

**Fix:**

1. Check `contact_data.properties.company` has a value
2. Add fallback: If no company, skip web search
3. Broaden search query (remove specific terms)
4. Add If Condition to skip search if company is empty

### AI Response Not Formatted

**Enrichment insights malformed or not JSON**

**Causes:**

1. LLM didn't follow format instructions
2. Web results overwhelming token limit

**Fix:**

1. Make prompt more explicit: "Return ONLY valid JSON"
2. Reduce web search results from 5 to 3
3. Try GPT-4 instead of GPT-3.5 (better at structured output)
4. Add error handling with Set Variable action

### Properties Not Updating

**Contact updated but enrichment fields empty**

**Causes:**

1. Custom properties not created in HubSpot
2. AI returned unexpected format
3. Variable path wrong

**Fix:**

1. Create all custom properties in HubSpot first
2. Check execution log - what did AI return?
3. Verify variable paths: `enrichment_insights.company_overview` not `company_overview`

### Enrichment Too Slow

**Workflow takes 30+ seconds**

**Causes:**

1. Web search slow
2. LLM processing large context
3. Multiple API calls stacking

**Fix:**

1. Reduce web search results (5 → 3)
2. Simplify AI prompt
3. Use faster LLM model (GPT-3.5 instead of GPT-4)
4. Consider async processing

***

## Tips & Best Practices

**✅ Do:**

* Test with a few contacts before activating for all
* Create all custom properties in HubSpot first
* Use specific, relevant web search queries
* Monitor LLM costs (each contact = 1 LLM call)
* Review AI-generated insights for accuracy
* Add timestamp to track when enriched
* Log enrichment to timeline for audit trail

**❌ Don't:**

* Enrich every contact (filter for quality leads only)
* Use vague search queries (be specific)
* Forget to handle missing company names
* Skip error handling for web search failures
* Enrich contacts without email or company data
* Re-enrich same contact multiple times per day

**Cost optimization:**

* Only enrich contacts above certain score threshold
* Use cheaper LLM for simple enrichment
* Limit web search to 3 results
* Add cooldown period (don't re-enrich within 30 days)

**Privacy considerations:**

* Web search is public data only
* Don't store sensitive info in custom properties
* Follow GDPR/privacy regulations
* Allow contacts to opt out of enrichment

***

## Related Resources

**Actions used:**

* [Lookup HubSpot Object (V2)](../actions/hubspot-v2-lookup-object)
* [Update HubSpot Object (V2)](../actions/hubspot-v2-update-object)
* [Create Timeline Event (V2)](../actions/hubspot-v2-create-timeline-event)

**Related workflows:**

* [HubSpot Deal Analysis](./hubspot-deal-analysis) - Similar AI analysis pattern
* [HubSpot Customer Onboarding](./hubspot-customer-onboarding) - Multi-step automation example

***

**Last Updated:** 2025-10-01
