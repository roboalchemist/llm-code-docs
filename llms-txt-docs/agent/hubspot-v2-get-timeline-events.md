# Source: https://docs.agent.ai/actions/hubspot-v2-get-timeline-events.md

# Get Timeline Events

Retrieve timeline events from any HubSpot record - see what happened and when.

**Common uses:**

* Get deal activity history for AI analysis
* Review contact engagement timeline
* Check recent events before taking action
* Gather context for decision-making
* Audit what happened on a record

**Action type:** `hubspot.v2.get_timeline_events`

***

## What This Does (The Simple Version)

Think of this like viewing someone's activity feed or history log. Every HubSpot record (contact, deal, company, etc.) has a timeline showing what's happened - emails sent, meetings scheduled, custom events logged. This action retrieves that timeline.

**Real-world example:**
Before calling a lead, you want to see their recent activity. This action gets their timeline showing: form submitted 3 days ago, whitepaper downloaded yesterday, demo requested today. Now you have context for the call.

***

## How It Works

This action retrieves timeline events from a HubSpot record. You specify:

1. **What type** of record (contact, deal, company, etc.)
2. **Which record** (the HubSpot ID)
3. **Filter options** (optional - specific event types, date ranges)
4. **How many events** to retrieve

The events are saved to a variable as a list you can use in later actions (like AI analysis or loops).

***

## Setting It Up

### Step 1: Choose Object Type

Select which type of HubSpot record to get events from:

* **Contacts** - Person timeline
* **Companies** - Organization timeline
* **Deals** - Deal timeline
* **Tickets** - Ticket timeline

**Choose the object type** from the dropdown.

### Step 2: Enter Object ID

In the **"Object ID"** field, enter the HubSpot ID of the record.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_deal` → `hs_object_id`
  * From a lookup: `contact_record` → `id`
  * From a webhook: `deal_id` (if provided)

**Example:** Click `{}` → select `deal_record` → `hs_object_id`

### Step 3: Filter by Event Type (Optional)

Want only specific types of events? Enter an event type in the **"Event Type Filter"** field.

**Leave blank** to get all event types (most common).

**Or enter a specific type:**

* `NOTE` - Only notes
* `MEETING` - Only meetings
* `EMAIL` - Only emails
* Custom event types you've created (e.g., `onboarding_completed`)

**Example:** Type `NOTE` to get only notes

### Step 4: Set Date Range (Optional)

Want events from a specific time period?

**Start Date field:**

* Enter start date (events after this date)
* Formats: `2025-01-01` or `01/01/2025`
* Or click `{}` to insert date variable

**End Date field:**

* Enter end date (events before this date)
* Same format options

**Leave both blank** to get events from all time.

**Example:** Start Date = `2025-01-01`, End Date = `2025-03-31` (Q1 2025 events only)

### Step 5: Set Result Limit (Optional)

Enter the maximum number of events to return.

**Default:** 100
**Maximum:** 500

**When to adjust:**

* **Testing?** Use 10-20 for faster results
* **AI analysis?** Use 50-100 (enough context, not overwhelming)
* **Complete history?** Use 500

### Step 6: Name Your Output Variable

Give the events list a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `deal_timeline`
* `contact_events`
* `recent_activity`
* `timeline_history`

This variable contains the list of events.

***

## What You Get Back

The action returns a **list of timeline events**, each containing event details.

**Example output saved to `deal_timeline`:**

```javascript  theme={null}
[
  {
    "id": "evt_12345",
    "eventType": "MEETING",
    "timestamp": "2025-01-15T14:00:00Z",
    "headline": "Product Demo",
    "details": "Demonstrated enterprise features, answered technical questions",
    "objectId": "987654"
  },
  {
    "id": "evt_67890",
    "eventType": "EMAIL",
    "timestamp": "2025-01-10T09:30:00Z",
    "headline": "Proposal Sent",
    "details": "Sent pricing proposal and implementation timeline",
    "objectId": "987654"
  },
  {
    "id": "evt_11111",
    "eventType": "NOTE",
    "timestamp": "2025-01-05T16:00:00Z",
    "headline": "Discovery Call",
    "details": "Discussed requirements, budget, timeline. Strong fit for enterprise plan.",
    "objectId": "987654"
  }
]
```

**Each event includes:**

* `id` - Event ID
* `eventType` - Type of event (MEETING, EMAIL, NOTE, custom types)
* `timestamp` - When it occurred
* `headline` - Event title/subject
* `details` - Event description/body
* `objectId` - The record it's associated with

***

## Using the Results

### Pass to AI for Analysis

The most common use - send timeline events to AI for context:

**In Invoke LLM action:**

* Prompt: Type "Analyze this deal timeline: " then click `{}` → select `deal_timeline`
  Example: `Analyze this deal timeline: {{deal_timeline}}`
* AI receives the full event list and can analyze patterns, identify risks, suggest next steps

### Loop Through Events

Process each event individually:

1. **For Loop**
   * Loop through: Click `{}` → select `deal_timeline`
   * Current item: `current_event`

2. **Inside loop:** Access event details
   * Click `{}` → `current_event` → `headline`
   * Click `{}` → `current_event` → `timestamp`

### Count Events

Want to know how many events there are?

**Add Set Variable action:**

* Use variable picker to count items in `deal_timeline` array

### Check for Recent Activity

**Add If Condition:**

* Check if `deal_timeline` list length > 0
* Check if most recent event timestamp is within last 7 days
* Take action based on activity level

***

## Common Workflows

### Deal Health Analysis

**Goal:** Analyze deal activity before updating

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal_record`

2. **Get Timeline Events (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → `deal_record` → `id`
   * Limit: 50
   * Output Variable: `deal_timeline`

3. **Invoke LLM**
   * Prompt: "Analyze this deal timeline and assess health: " + `deal_timeline` variable
   * Output Variable: `health_assessment`

4. **Update HubSpot Object (V2)**
   * Update deal with health score

### Check Recent Contact Activity

**Goal:** Only send email if contact hasn't been contacted recently

1. **Get Timeline Events (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `contact_id`
   * Event Type Filter: `EMAIL`
   * Start Date: Click `{}` → `seven_days_ago` (system variable)
   * Output Variable: `recent_emails`

2. **If Condition**
   * Check if `recent_emails` is empty (no emails in last 7 days)

3. **Send Email** (inside if block)
   * Only runs if no recent emails

4. **End Condition**

### Gather Context for Sales Call

**Goal:** Get complete activity history before calling prospect

1. **Search HubSpot (V2)**
   * Find target contact
   * Output Variable: `target_contact`

2. **Get Timeline Events (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `target_contact` → `hs_object_id`
   * Limit: 100
   * Output Variable: `contact_history`

3. **Invoke LLM**
   * Prompt: "Summarize this contact's history and suggest talking points: " + `contact_history` variable
   * Output Variable: `call_prep`

***

## Real Examples

### Pre-Call Research

**Scenario:** Sales rep clicks "Run" before calling a lead to get instant context.

**Trigger:** Manual

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** (manually enter contact ID or use search first)
* **Event Type Filter:** Leave blank (get all events)
* **Start Date:** Leave blank
* **End Date:** Leave blank
* **Limit:** 100
* **Output Variable:** `contact_timeline`

**Next steps:** AI summarizes timeline, identifies recent activity, suggests talking points.

### Deal Stall Detection

**Scenario:** Every morning, check deals for inactivity.

**Trigger:** Scheduled (daily at 9:00 AM)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `current_deal` → `hs_object_id` (from loop)
* **Event Type Filter:** Leave blank
* **Start Date:** Click `{}` → `thirty_days_ago`
* **End Date:** Leave blank
* **Limit:** 10 (just need to know if ANY activity exists)
* **Output Variable:** `recent_activity`

**Next steps:** If `recent_activity` is empty, flag deal as stalled.

***

## Troubleshooting

### No Events Returned

**Action returns empty list `[]`**

**Possible causes:**

1. Record has no timeline events
2. Event type filter doesn't match any events
3. Date range excludes all events
4. Object ID doesn't exist

**How to fix:**

1. Check HubSpot - does this record have timeline events?
2. Remove event type filter (leave blank to get all types)
3. Remove date range filters
4. Verify object ID is correct (check execution log)
5. Try with a record you know has events

### Wrong Event Type

**Filter returns no results but events exist**

**Possible causes:**

1. Event type name is case-sensitive or misspelled
2. Using wrong event type identifier

**How to fix:**

1. Event types are usually UPPERCASE: `EMAIL`, `MEETING`, `NOTE`
2. For custom events, check exact event type identifier
3. Leave filter blank first to see all event types, then filter

### Too Many Events

**Returns 500 events but there are more**

**Possible causes:**

1. HubSpot maximum limit is 500
2. Record has thousands of events

**How to fix:**

1. Use date range to focus on recent events
2. Use start\_date to get last 30/60/90 days only
3. Use event type filter to narrow down
4. If you need all events, make multiple calls with different date ranges

### Events Missing Details

**Events returned but `details` field is empty**

**This is normal** - not all event types have details. Some only have headlines.

**How to handle:**

1. Check `headline` field (always present)
2. Some events just track "this happened" without description
3. Use `eventType` to understand what kind of event it was

***

## Tips & Best Practices

**✅ Do:**

* Use result limit to control how many events you get
* Pass timeline to AI for analysis (great context)
* Filter by date range for recent activity checks
* Use in loops to analyze multiple records
* Leave event type filter blank unless you need specific types
* Check execution log to see what events were returned

**❌ Don't:**

* Request all events for records with thousands (use date range)
* Forget that event types are case-sensitive
* Assume all events have detailed descriptions
* Use without object ID (it's required)
* Expect events from the future (end\_date should be past or present)

**Performance tips:**

* Getting 100 events takes \~1-2 seconds
* Fewer events = faster response
* Date range filters speed up retrieval
* Event type filters reduce result size

**Use cases by event type:**

* **All events:** Complete history for AI analysis
* **EMAIL only:** Check email frequency/timing
* **MEETING only:** Count of meetings scheduled
* **NOTE only:** Sales notes and context
* **Custom events:** Track specific milestones

***

## Related Actions

**What to do with events:**

* [For Loop](./for_loop) - Process each event
* [If Condition](./if_else) - Check if events exist
* [Create Timeline Event (V2)](./hubspot-v2-create-timeline-event) - Add new events
* [Invoke LLM](./use_genai) - Analyze events with AI

**Related actions:**

* [Get Engagements (V2)](./hubspot-v2-get-engagements) - Similar but for engagements (calls, emails, meetings, notes)
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get object before retrieving timeline

**Related workflows:**

* [HubSpot Deal Analysis](../recipes/hubspot-deal-analysis) - Uses timeline events for AI analysis
* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagement history

***

**Last Updated:** 2025-10-01
