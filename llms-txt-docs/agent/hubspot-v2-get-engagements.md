# Source: https://docs.agent.ai/actions/hubspot-v2-get-engagements.md

# Get Engagements

Retrieve calls, emails, meetings, notes, and tasks associated with any HubSpot record.

**Common uses:**

* Get call history for a contact
* Review all emails sent to a prospect
* Count meetings scheduled with a deal
* Analyze engagement patterns
* Gather relationship context

**Action type:** `hubspot.v2.get_engagements`

***

## What This Does (The Simple Version)

Think of this like pulling up someone's communication history. Every time your team calls, emails, or meets with a contact/company/deal, HubSpot logs it as an "engagement". This action retrieves those engagement records.

**Real-world example:**
You want to analyze how engaged a deal is. This action gets all calls, emails, and meetings associated with that deal - showing 15 calls, 32 emails, 4 meetings over 3 months. High engagement = healthy deal.

***

## How It Works

This action retrieves engagement records (calls, emails, meetings, notes, tasks) associated with a HubSpot record. You specify:

1. **What type of record** (contact, deal, company, ticket)
2. **Which record** (the HubSpot ID)
3. **Which engagement types** to get (calls, emails, meetings, notes, tasks)
4. **Date range** (optional)
5. **How many to retrieve**

The engagements are saved to a variable as a list you can analyze or loop through.

***

## Setting It Up

### Step 1: Choose Source Object Type

Select which type of HubSpot record to get engagements from:

* **Contacts** - Person's engagement history
* **Companies** - Organization's engagement history
* **Deals** - Deal's engagement history
* **Tickets** - Ticket's engagement history

**Choose the object type** from the dropdown.

### Step 2: Enter Object ID

In the **"Object ID"** field, enter the HubSpot ID of the record.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_contact` → `hs_object_id`
  * From a lookup: `deal_record` → `id`
  * From a webhook: `deal_id` (if provided)

**Example:** Click `{}` → select `contact_record` → `hs_object_id`

### Step 3: Select Engagement Types

Choose which types of engagements to retrieve. You can select multiple:

* **Calls** - Phone call records
* **Emails** - Email communications
* **Meetings** - Scheduled meetings
* **Notes** - Notes logged by your team
* **Tasks** - Tasks associated with this record

**Select all that apply** or choose specific types.

**Most common:** Select all types to get complete engagement history.

### Step 4: Set Date Range (Optional)

Want engagements from a specific time period?

**Start Date field:**

* Enter start date (engagements after this date)
* Formats: `2025-01-01` or `01/01/2025`
* Or click `{}` to insert date variable

**End Date field:**

* Enter end date (engagements before this date)
* Same format options

**Leave both blank** to get engagements from all time.

**Example:** Start Date = `2025-01-01` (get engagements from this year)

### Step 5: Set Result Limit (Optional)

Enter the maximum number of engagements to return.

**Default:** 100
**Maximum:** 500

**When to adjust:**

* **Testing?** Use 10-20
* **Recent activity?** Use 50
* **Complete history?** Use 500

### Step 6: Name Your Output Variable

Give the engagements list a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `deal_engagements`
* `contact_calls`
* `relationship_history`
* `recent_emails`

This variable contains the list of engagements.

***

## What You Get Back

The action returns a **list of engagement records**, each containing engagement details.

**Example output saved to `deal_engagements`:**

```javascript  theme={null}
[
  {
    "id": "123456",
    "type": "meeting",
    "createdAt": "2025-01-15T14:00:00Z",
    "properties": {
      "hs_meeting_title": "Product Demo",
      "hs_meeting_body": "Demonstrated enterprise features, answered technical questions about integrations",
      "hs_meeting_outcome": "Scheduled",
      "hs_meeting_start_time": "2025-01-15T14:00:00Z",
      "hs_meeting_duration": "3600000"
    }
  },
  {
    "id": "789012",
    "type": "call",
    "createdAt": "2025-01-10T10:30:00Z",
    "properties": {
      "hs_call_title": "Discovery Call",
      "hs_call_body": "Discussed requirements, budget, timeline. Strong interest in enterprise plan.",
      "hs_call_duration": "1800000",
      "hs_call_disposition": "Connected"
    }
  },
  {
    "id": "345678",
    "type": "email",
    "createdAt": "2025-01-08T09:00:00Z",
    "properties": {
      "hs_email_subject": "Proposal for Acme Corp",
      "hs_email_text": "Attached is our proposal...",
      "hs_email_status": "SENT"
    }
  },
  {
    "id": "901234",
    "type": "note",
    "createdAt": "2025-01-05T16:00:00Z",
    "properties": {
      "hs_note_body": "Follow-up from initial call. Need to connect with CTO about security requirements."
    }
  }
]
```

**Each engagement includes:**

* `id` - Engagement ID
* `type` - Type (meeting, call, email, note, task)
* `createdAt` - When it was created/logged
* `properties` - Type-specific details (subject, body, duration, outcome, etc.)

***

## Using the Results

### Pass to AI for Analysis

The most common use - send engagements to AI for relationship analysis:

**In Invoke LLM action:**

* Prompt: Type "Analyze this engagement history and assess relationship strength: " then click `{}` → select `deal_engagements`
  Example: `Analyze this engagement history: {{deal_engagements}}`
* AI receives all engagements and can identify patterns, frequency, quality

### Count Engagements

Want to know how many calls/emails/meetings?

**Add Set Variable action:**

* Use variable picker to count items in `deal_engagements` array
* Or count specific types: loop through and count where `type = "call"`

### Loop Through Engagements

Process each engagement individually:

1. **For Loop**
   * Loop through: Click `{}` → select `deal_engagements`
   * Current item: `current_engagement`

2. **Inside loop:** Access engagement details
   * Click `{}` → `current_engagement` → `type`
   * Click `{}` → `current_engagement` → `properties` → `hs_call_title`

### Check Recent Activity

**Add If Condition:**

* Check if `deal_engagements` list is not empty
* Check if first engagement (most recent) is within last 7 days
* Tag record based on engagement level

***

## Common Workflows

### Deal Engagement Analysis

**Goal:** Analyze all engagements for a deal to assess activity level

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal_record`

2. **Get Engagements (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → `deal_record` → `id`
   * Engagement Types: Select all (Calls, Emails, Meetings, Notes)
   * Limit: 100
   * Output Variable: `deal_engagements`

3. **Invoke LLM**
   * Prompt: "Analyze this deal's engagement history. Assess: engagement frequency, quality, gaps, and health score." + `deal_engagements` variable
   * Output Variable: `engagement_analysis`

4. **Update HubSpot Object (V2)**
   * Update deal with engagement score

### Contact Communication History

**Goal:** Get all emails sent to a contact before sending another

1. **Get Engagements (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `contact_id`
   * Engagement Types: Select "Emails"
   * Start Date: Click `{}` → `thirty_days_ago`
   * Limit: 50
   * Output Variable: `recent_emails`

2. **If Condition**
   * Check if `recent_emails` count \< 3 (not over-emailing)

3. **Send Email** (inside if block)
   * Only sends if they haven't received too many emails

4. **End Condition**

### Meeting Count Report

**Goal:** Count meetings scheduled with each deal in a list

1. **Search HubSpot (V2)**
   * Find target deals
   * Output Variable: `target_deals`

2. **For Loop**
   * Loop through: `target_deals`
   * Current item: `current_deal`

3. **Get Engagements (V2)** (inside loop)
   * Object Type: Deals
   * Object ID: Click `{}` → `current_deal` → `hs_object_id`
   * Engagement Types: Select "Meetings"
   * Output Variable: `deal_meetings`

4. **Set Variable** (inside loop)
   * Count meetings and store

5. **End Loop**

***

## Real Examples

### Prospect Research

**Scenario:** Before calling a prospect, see all previous interactions.

**Trigger:** Manual

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** (enter contact ID or use search first)
* **Engagement Types:** Select all
* **Start Date:** Leave blank (all time)
* **Limit:** 100
* **Output Variable:** `contact_history`

**Next steps:** AI summarizes history, identifies last touchpoint, suggests talking points.

### Sales Velocity Tracking

**Scenario:** Measure how many touchpoints it takes to close deals.

**Trigger:** When deal closes (webhook)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `deal_id` (from webhook)
* **Engagement Types:** Select Calls, Emails, Meetings
* **Limit:** 500 (complete history)
* **Output Variable:** `sales_cycle_engagements`

**Next steps:** Count total engagements, calculate velocity, log metrics.

***

## Troubleshooting

### No Engagements Returned

**Action returns empty list `[]`**

**Possible causes:**

1. Record has no engagements
2. Wrong engagement types selected
3. Date range excludes all engagements
4. Object ID doesn't exist

**How to fix:**

1. Check HubSpot - does this record have logged calls/emails/meetings?
2. Select all engagement types to test
3. Remove date range filters
4. Verify object ID is correct
5. Check if engagements are actually associated with this record

### Missing Expected Engagements

**Some engagements you know exist aren't showing up**

**Possible causes:**

1. Engagements not associated with this specific record
2. Hit the limit before reaching those engagements
3. Date range excluding them

**How to fix:**

1. Check in HubSpot - are these engagements actually associated with this record?
2. Increase limit to 500
3. Expand date range or remove it
4. Engagements might be associated with related records (contact vs. company)

### Different Object Has Different Engagements

**Contact has different engagements than associated company**

**This is normal** - engagements are object-specific:

* Contact engagements: logged directly on the contact
* Company engagements: logged directly on the company
* Deal engagements: logged directly on the deal

**To get complete picture:**

1. Get engagements for contact
2. Get engagements for associated company
3. Get engagements for associated deal
4. Combine all three for full relationship history

### Properties Missing

**Engagements returned but missing details**

**Possible causes:**

1. Engagement was logged without details
2. Specific properties not filled in

**This is normal** - not all engagements have all properties:

* Quick notes might only have `hs_note_body`
* Some calls might not have duration logged
* Old emails might have limited data

**How to handle:**

* Check which properties exist before using them
* Use default values for missing properties
* Focus on properties that are consistently filled

***

## Tips & Best Practices

**✅ Do:**

* Select all engagement types unless you need specific ones
* Use result limit to control volume
* Pass engagements to AI for pattern analysis
* Check execution log to see what was returned
* Use date range for "recent activity" checks
* Consider getting engagements from related records too (contact + company + deal)

**❌ Don't:**

* Forget that engagements are object-specific (contact ≠ company ≠ deal)
* Assume all engagements have full details
* Request engagements without checking if record exists first
* Exceed 500 limit (HubSpot maximum)
* Expect engagements to include associations to other records (this action gets the engagements only)

**Performance tips:**

* Getting 100 engagements takes \~2-3 seconds
* More engagement types = slightly slower
* Date range filters can speed up retrieval
* Limit keeps results manageable

**Analysis ideas:**

* **Engagement frequency:** Count engagements per month
* **Engagement quality:** Analyze call notes and meeting outcomes
* **Response time:** Time between emails and responses
* **Engagement gaps:** Long periods with no activity
* **Activity patterns:** Which days/times have most engagement

***

## Difference from Get Timeline Events

**Get Engagements vs. Get Timeline Events - what's the difference?**

**Get Engagements (this action):**

* Retrieves: Calls, emails, meetings, notes, tasks
* These are standard HubSpot activity records
* Logged by your team
* Used for: Relationship analysis, activity tracking, communication history

**Get Timeline Events:**

* Retrieves: All timeline events (including custom events)
* Includes: Standard events + custom events you create
* Used for: Complete timeline history, custom milestone tracking

**When to use which:**

* **Get Engagements:** When you need sales/service activity (calls, emails, meetings)
* **Get Timeline Events:** When you need complete timeline including custom events

**You can use both** in the same workflow for complete context!

***

## Related Actions

**What to do with engagements:**

* [For Loop](./for_loop) - Process each engagement
* [If Condition](./if_else) - Check engagement patterns
* [Invoke LLM](./use_genai) - Analyze engagement quality

**Related actions:**

* [Get Timeline Events (V2)](./hubspot-v2-get-timeline-events) - Get timeline events (includes custom events)
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get object before retrieving engagements

**Related workflows:**

* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagement history for onboarding context
* [HubSpot Deal Analysis](../recipes/hubspot-deal-analysis) - Uses timeline events (similar pattern)

***

**Last Updated:** 2025-10-01
