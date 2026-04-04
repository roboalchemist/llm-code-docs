# Source: https://docs.agent.ai/actions/hubspot-v2-create-engagement.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Engagement

Log calls, emails, meetings, notes, and tasks to HubSpot records - create engagement records programmatically.

**Common uses:**

* Log external calls to HubSpot
* Create notes from AI analysis
* Schedule follow-up tasks
* Record meetings from other systems
* Track email outreach

**Action type:** `hubspot.v2.create_engagement`

***

## What This Does (The Simple Version)

Think of this like adding an entry to someone's activity log. When your team calls, emails, or meets with someone, HubSpot tracks it as an "engagement". This action creates those engagement records from your workflows.

**Real-world example:**
After an AI analyzes a deal and generates insights, you want to log those insights as a note on the deal. This action creates a note engagement with the AI's analysis, visible in HubSpot's timeline.

***

## How It Works

This action creates engagement records (calls, emails, meetings, notes, tasks) in HubSpot. You specify:

1. **Engagement type** (call, email, meeting, note, task)
2. **Content** (body/description of the engagement)
3. **Who/what it's about** (associated contact, deal, company)
4. **Additional details** (title, duration, status, etc.)

The engagement appears in HubSpot on the associated record's timeline.

***

## Setting It Up

### Step 1: Choose Engagement Type

Select which type of engagement to create:

* **Note** - Add notes/comments
* **Call** - Log phone calls
* **Email** - Record email communications
* **Meeting** - Log meetings
* **Task** - Create tasks

**Choose from dropdown:** Engagement Type

### Step 2: Add Content (Required)

In the **"Content/Body"** field, enter the main content.

**This is the description/body of the engagement.**

**You can:**

* Type directly
* Click `{}` to insert variables
* Mix text and variables

**Examples:**

**For notes:**

```
AI Analysis: [insert deal_insights variable]
```

**For calls:**

```
Discussed [deal name] with [contact first name]. Next steps: [next actions]
```

**For tasks:**

```
Follow up on deal [deal name] - review proposal and schedule demo
```

### Step 3: Add Title/Subject (Optional)

In the **"Title/Subject"** field, add a title.

**Different engagement types use this differently:**

* **Note:** Note title
* **Call:** Call title
* **Email:** Email subject
* **Meeting:** Meeting title
* **Task:** Task subject

**Example:**

```
Discovery Call - [company_name]
```

### Step 4: Add Associations (Required)

In the **"Associations"** field, specify which records this engagement relates to.

**Format:** One per line: `object_type:object_id`

**Example:**

```
contact:[contact_id]
deal:[deal_record.id]
company:[company_id]
```

**Common patterns:**

**Associate with contact from lookup:**

```
contact:[contact_data.id]
```

**Associate with deal from search:**

```
deal:[current_deal.hs_object_id]
```

**Associate with multiple:**

```
contact:[contact_id]
deal:[deal_id]
```

### Step 5: Add Type-Specific Details (Optional)

Depending on engagement type, additional fields appear:

**For calls:**

* **Duration:** Call length in minutes (e.g., `30`)
* **Status:** Call outcome (e.g., `Connected`, `No Answer`, `Left Voicemail`)

**For meetings:**

* **Duration:** Meeting length in minutes (e.g., `60`)
* **Status:** Meeting outcome (e.g., `Scheduled`, `Completed`, `Rescheduled`)

**For tasks:**

* **Status:** Task status (e.g., `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`)
* **Priority:** Task priority (e.g., `HIGH`, `MEDIUM`, `LOW`)

**For emails:**

* **Status:** Email status (e.g., `SENT`, `SCHEDULED`)

### Step 6: Additional Properties (Optional)

In the **"Additional Properties"** field, add custom engagement properties.

**Format:** Key-value pairs, one per line:

```
property_name=value
another_property=another_value
```

**Or JSON:**

```json  theme={null}
{
  "custom_field": "value",
  "another_field": "[variable]"
}
```

### Step 7: Name Output Variable

In the **"Output Variable Name"** field, name the created engagement.

**Good names:**

* `created_note`
* `logged_call`
* `scheduled_task`
* `meeting_record`

**Default:** `created_engagement`

***

## What You Get Back

The action returns the created engagement record.

**Example output saved to `created_note`:**

```javascript  theme={null}
{
  "id": "123456789",
  "engagement_type": "note",
  "properties": {
    "hs_note_body": "AI Analysis: Deal shows strong engagement...",
    "hs_note_title": "Deal Health Analysis",
    "hs_timestamp": "2025-01-15T14:30:00Z",
    "hs_created_at": "2025-01-15T14:30:00Z"
  },
  "createdAt": "2025-01-15T14:30:00Z",
  "updatedAt": "2025-01-15T14:30:00Z"
}
```

**What's included:**

* `id` - Engagement ID
* `engagement_type` - Type you created
* `properties` - Engagement properties
* `createdAt` - When created

***

## Common Workflows

### Log AI Insights as Notes

**Goal:** Create notes with AI analysis results

1. **Lookup HubSpot Object (V2)**
   * Get deal
   * Output Variable: `deal_record`

2. **Get Timeline Events (V2)**
   * Get deal history
   * Output Variable: `deal_timeline`

3. **Invoke LLM**
   * Prompt: "Analyze \[deal\_record] and \[deal\_timeline]"
   * Output Variable: `insights`

4. **Create Engagement (V2)**
   * Engagement Type: Note
   * Content/Body: Click `{}` → `insights`
   * Title/Subject: "AI Deal Analysis"
   * Associations: `deal:[deal_record.id]`
   * Output Variable: `analysis_note`

### Log External Calls

**Goal:** Record calls from external phone system

1. **Webhook receives:**
   * `contact_id`
   * `call_duration`
   * `call_notes`
   * `call_outcome`

2. **Create Engagement (V2)**
   * Engagement Type: Call
   * Content/Body: Click `{}` → `call_notes`
   * Title/Subject: Type "Outbound Sales Call"
   * Duration: Click `{}` → `call_duration`
   * Status: Click `{}` → `call_outcome`
   * Associations: `contact:[contact_id]`

### Create Follow-Up Tasks

**Goal:** Create tasks after enrichment

1. **Search HubSpot (V2)**
   * Find high-priority leads
   * Output Variable: `priority_leads`

2. **For Loop**
   * Loop through: `priority_leads`
   * Current item: `current_lead`

3. **Create Engagement (V2)** (inside loop)
   * Engagement Type: Task
   * Content/Body: Type "Review enrichment data and reach out to " then click `{}` → `current_lead` → `properties` → `firstname`
   * Title/Subject: "Follow-up: High Priority Lead"
   * Status: `NOT_STARTED`
   * Priority: `HIGH`
   * Associations: `contact:[current_lead.hs_object_id]`

4. **End Loop**

***

## Real Examples

### Post-Analysis Note

**Scenario:** After AI analyzes deal health, log insights

**Configuration:**

* **Engagement Type:** Note
* **Content/Body:** `[deal_health_analysis]`
* **Title/Subject:** "Automated Health Check"
* **Associations:** `deal:[deal_id]`

**Result:** Note appears on deal timeline with AI insights

### External Call Logging

**Scenario:** Phone system sends webhook after calls

**Webhook payload:**

```json  theme={null}
{
  "contact_id": "123456",
  "duration_minutes": "15",
  "outcome": "Connected",
  "notes": "Discussed pricing, sending proposal"
}
```

**Configuration:**

* **Engagement Type:** Call
* **Content/Body:** `[notes]`
* **Title/Subject:** "Sales Call"
* **Duration:** `[duration_minutes]`
* **Status:** `[outcome]`
* **Associations:** `contact:[contact_id]`

**Result:** Call logged to contact with all details

### Automated Task Creation

**Scenario:** Create task when deal reaches certain stage

**Trigger:** Webhook when deal stage = "Decision Stage"

**Configuration:**

* **Engagement Type:** Task
* **Content/Body:** "Review decision criteria with \[contact\_name] and address any concerns"
* **Title/Subject:** "Decision Stage Follow-up"
* **Status:** `NOT_STARTED`
* **Priority:** `HIGH`
* **Associations:** `deal:[deal_id]\ncontact:[primary_contact_id]`

**Result:** High-priority task created for sales rep

***

## Troubleshooting

### Missing Associations Error

**"Associations are required" error**

**Possible causes:**

1. Associations field empty
2. Wrong format
3. Invalid object ID

**How to fix:**

1. Add at least one association: `contact:[contact_id]`
2. Use format: `object_type:object_id` (one per line)
3. Verify object IDs are valid HubSpot IDs
4. Check execution log for exact error

### Engagement Not Appearing

**Created but can't find in HubSpot**

**Possible causes:**

1. Associated with wrong record
2. Looking at wrong record type
3. Timeline filter hiding it

**How to fix:**

1. Check associations - verify correct record ID
2. Check execution log - see which ID was used
3. In HubSpot timeline, clear filters
4. Search for engagement by ID in execution log

### Duration Not Saving

**Duration field ignored**

**Possible causes:**

1. Wrong format (needs minutes)
2. Non-numeric value
3. Only applies to calls/meetings

**How to fix:**

1. Use number of minutes: `30` not `30 minutes`
2. Ensure numeric value: `[duration]` must resolve to number
3. Duration only works for calls and meetings

### Status Invalid

**Status value rejected**

**Possible causes:**

1. Invalid status for engagement type
2. Custom status not recognized

**How to fix:**

1. Use standard values:
   * Calls: `Connected`, `No Answer`, `Left Voicemail`, `Busy`
   * Meetings: `Scheduled`, `Completed`, `Rescheduled`, `Canceled`
   * Tasks: `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `WAITING`, `DEFERRED`
   * Emails: `SENT`, `SCHEDULED`, `BOUNCED`, `FAILED`
2. Check HubSpot settings for custom values

***

## Tips & Best Practices

**✅ Do:**

* Always include meaningful content/body
* Associate with relevant records (contact, deal, company)
* Use descriptive titles/subjects
* Include duration for calls and meetings (helps reporting)
* Set task priority for action items
* Use variables to make content dynamic
* Log AI insights as notes for context

**❌ Don't:**

* Create engagements without associations (required)
* Leave content/body empty
* Use invalid status values
* Forget duration is in minutes (not seconds/hours)
* Create duplicate engagements (check if exists first)
* Log sensitive information in engagements

**Performance tips:**

* Creating engagement takes \~1-2 seconds
* No limit on engagements created
* Bulk creation: use loops with rate limiting

**Engagement type selection:**

* **Notes:** AI insights, analysis results, internal comments
* **Calls:** Phone conversations (manual or from phone system)
* **Emails:** Email outreach (if not using HubSpot email)
* **Meetings:** Meeting records from external calendars
* **Tasks:** Follow-up actions, reminders, to-dos

***

## Related Actions

**Before creating engagement:**

* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get record to associate
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records to log engagements on

**After creating engagement:**

* [Get Engagements (V2)](./hubspot-v2-get-engagements) - Retrieve engagements later
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update associated record

**Related actions:**

* [Create Timeline Event (V2)](./hubspot-v2-create-timeline-event) - Custom timeline events (different from engagements)
* [For Loop](./for_loop) - Create multiple engagements

**Related workflows:**

* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagements for context

***

**Last Updated:** 2025-10-01
