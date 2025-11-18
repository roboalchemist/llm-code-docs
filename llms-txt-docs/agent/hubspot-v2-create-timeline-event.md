# Source: https://docs.agent.ai/actions/hubspot-v2-create-timeline-event.md

# Create Timeline Event

Add custom events to the timeline of any HubSpot record - perfect for tracking activities that happen outside HubSpot.

**Common uses:**

* Log customer actions from your app (logins, feature usage, purchases)
* Track external system events (support calls, shipping updates)
* Record custom milestones (onboarding completed, renewal date)
* Document important interactions (demo attended, contract signed)

**Action type:** `hubspot.v2.create_timeline_event`

***

## What This Does (The Simple Version)

Think of this like adding a note to someone's activity feed, but way more powerful. Instead of just text, you can log structured events that show up on contact, deal, or company timelines in HubSpot.

**Real-world example:**
A customer completes onboarding in your app. You create a timeline event on their contact record showing "Onboarding Completed" with details like completion date, steps finished, and time spent. Your sales team sees this in HubSpot and knows the customer is ready for upsell conversations.

***

## How It Works

This action creates a custom event that appears on the timeline of a HubSpot record. You choose:

1. **What record** to add the event to (contact, deal, company, etc.)
2. **Event type** identifier (you create this)
3. **Event details** (title, description, timestamp)
4. **Custom properties** (optional - any additional data you want to track)

The event appears on the record's timeline in HubSpot, just like emails, calls, and meetings.

***

## Setting It Up

### Step 1: Choose Target Object Type

Select which type of HubSpot record you want to add the timeline event to:

* **Contacts** - Add event to a person's timeline
* **Companies** - Add event to an organization's timeline
* **Deals** - Add event to a deal's timeline
* **Tickets** - Add event to a ticket's timeline

**Choose the object type** from the dropdown.

### Step 2: Enter Target Object ID

In the **"Target Object ID"** field, enter the HubSpot ID of the record you want to add the event to.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_contact` → `hs_object_id`
  * From a lookup: `found_deal` → `id`
  * From a webhook: `contact_id` (if provided)

**Example:** Click `{}` → select `contact_record` → `id`

### Step 3: Enter Event Type

The **"Event Type"** is a unique identifier for this kind of event. This helps HubSpot group similar events together.

**Format:** Use lowercase with underscores, like:

* `onboarding_completed`
* `feature_activated`
* `purchase_made`
* `support_call_completed`
* `renewal_reminder`

**Type directly** in the field or click `{}` to insert a variable.

**Note:** Use the same event type for similar events. For example, all "Feature Activated" events should use `feature_activated` so they're grouped together on the timeline.

### Step 4: Enter Event Title

The **"Event Title"** is the headline that appears on the timeline - like a subject line.

**Examples:**

* "Onboarding Completed"
* "Feature Activated: Advanced Reporting"
* "Purchase: Enterprise Plan"
* "Support Call: Billing Question"

Type directly or click `{}` to insert variables. You can combine text and variables:

* Type "Purchase: " then click `{}` → select `plan_name`
* Type "Feature Activated: " then click `{}` → select `feature_name`

### Step 5: Enter Event Description (Optional)

The **"Event Description"** provides additional details that appear when someone clicks the event on the timeline.

**Examples:**

* "Customer completed all 5 onboarding steps in 3 days"
* "Activated Advanced Reporting feature on 2025-10-01"
* "Upgraded from Starter to Enterprise plan, annual billing"

Type directly or click `{}` to insert variables with details.

**Leave blank** if you don't need additional description.

### Step 6: Add Event Properties (Optional)

Click **"+ Add Property"** if you want to attach custom data to this event.

**This is different from HubSpot properties.** These are custom key-value pairs specific to this event.

**Format:** Each property is `key=value`, one per line:

```
steps_completed=5
time_spent_minutes=45
completion_date=2025-10-01
```

Or use variables by clicking `{}` in the value field.

**Leave blank** if you don't need custom properties.

### Step 7: Set Event Timestamp (Optional)

The **"Event Timestamp"** controls when the event appears on the timeline.

**Default:** If you leave this blank, it uses the current time (right now).

**Formats supported:**

* ISO 8601: `2025-10-01T14:30:00Z`
* Date only: `2025-10-01` (assumes midnight)
* US format: `10/01/2025`
* Timestamp in milliseconds: `1727790600000` (13 digits)
* Timestamp in seconds: `1727790600` (10 digits)

**Usually you'll:**

* Leave blank to use "now"
* Click `{}` to insert a date variable from your trigger or previous action
* Type a specific date if logging a past event

### Step 8: Name Your Output Variable

Give the event result a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `onboarding_event`
* `purchase_event`
* `timeline_event`
* `logged_activity`

This variable contains the event ID and confirmation details.

***

## What You Get Back

The action returns confirmation that the event was created, including the event ID.

**Example output saved to `onboarding_event`:**

```
{
  "id": "evt_12345",
  "event_type": "onboarding_completed",
  "event_title": "Onboarding Completed",
  "event_description": "Customer completed all steps",
  "timestamp": 1727790600000,
  "object_id": "67890",
  "object_type": "contacts",
  "created_at": "2025-10-01T14:30:00Z",
  "properties": {
    "steps_completed": "5",
    "time_spent_minutes": "45"
  }
}
```

***

## Using the Results

### Confirm Event Was Created

The event either succeeds (returns event ID) or throws an error. The output variable contains the event ID, which you can use to verify creation succeeded.

### Access Event Details

Use the output variable to access event information in later actions:

* Click `{}` → `onboarding_event` → `id` (the event ID)
* Click `{}` → `onboarding_event` → `timestamp`
* Click `{}` → `onboarding_event` → `properties` → `steps_completed`

***

## Common Workflows

### Log App Activity

**Goal:** When a user completes onboarding in your app, log it on their HubSpot contact

**Trigger:** Webhook from your app

**Webhook receives:** `contact_id`, `steps_completed`, `completion_time` variables

1. **Create Timeline Event (V2)**
   * Object Type: Contacts
   * Target Object ID: Click `{}` → select `contact_id`
   * Event Type: `onboarding_completed`
   * Event Title: "Onboarding Completed Successfully"
   * Event Description: Type "Completed " then click `{}` → select `steps_completed` → type " steps"
   * Event Properties:
     ```
     steps_completed={{steps_completed}}
     time_spent_minutes={{completion_time}}
     ```
   * Event Timestamp: Leave blank (use current time)
   * Output Variable: `onboarding_event`

2. **Update contact** or send notification...

### Track Purchase on Company Timeline

**Goal:** When a company makes a purchase, log it on their company record

**Trigger:** Webhook from payment processor

**Webhook receives:** `company_domain`, `plan_name`, `amount`, `purchase_date`

1. **Lookup HubSpot Object (V2)**
   * Object Type: Companies
   * Lookup by: Domain
   * Domain: Click `{}` → select `company_domain`
   * Output Variable: `company_record`

2. **Create Timeline Event (V2)**
   * Object Type: Companies
   * Target Object ID: Click `{}` → `company_record` → `id`
   * Event Type: `purchase_made`
   * Event Title: Type "Purchase: " then click `{}` → select `plan_name`
   * Event Description: Type "Purchased " then click `{}` → select `plan_name` → type " for \$" → click `{}` → select `amount`
   * Event Properties:
     ```
     plan_name={{plan_name}}
     amount={{amount}}
     billing_frequency=annual
     ```
   * Event Timestamp: Click `{}` → select `purchase_date`
   * Output Variable: `purchase_event`

### Log Support Call on Deal

**Goal:** After a support call, log it on the related deal's timeline

1. **Search HubSpot (V2)**
   * Find the deal associated with the customer
   * Output Variable: `customer_deal`

2. **Create Timeline Event (V2)**
   * Object Type: Deals
   * Target Object ID: Click `{}` → `customer_deal` → `hs_object_id`
   * Event Type: `support_call_completed`
   * Event Title: Type "Support Call: " then click `{}` → select `call_topic`
   * Event Description: Click `{}` → select `call_notes`
   * Event Properties:
     ```
     duration_minutes={{call_duration}}
     resolution={{resolution_status}}
     agent={{support_agent_name}}
     ```
   * Event Timestamp: Click `{}` → select `call_time`
   * Output Variable: `support_event`

***

## Real Examples

### Feature Activation Tracking

**Scenario:** Track when customers activate premium features in your SaaS app.

**Webhook receives:** `user_email`, `feature_name`, `activation_date`

**Timeline Event Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → select `contact_id` (from lookup action)
* **Event Type:** `feature_activated`
* **Event Title:** Type "Feature Activated: " then click `{}` → select `feature_name`
* **Event Description:** Type "Customer activated " then click `{}` → select `feature_name` → type " on " → click `{}` → select `activation_date`
* **Event Properties:**
  ```
  feature_name={{feature_name}}
  plan_tier={{user_plan}}
  activation_date={{activation_date}}
  ```
* **Event Timestamp:** Click `{}` → select `activation_date`
* **Output Variable:** `feature_event`

**Next steps:** Check if they've activated 3+ features and update lifecycle stage.

### Renewal Reminder Logging

**Scenario:** Log when renewal reminders are sent to customers.

**Trigger:** Scheduled (runs daily)

**Timeline Event Configuration:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `current_deal` → `hs_object_id` (from loop)
* **Event Type:** `renewal_reminder_sent`
* **Event Title:** "Renewal Reminder Sent"
* **Event Description:** Type "Renewal reminder sent for contract ending " then click `{}` → select `contract_end_date`
* **Event Properties:**
  ```
  contract_value={{deal_amount}}
  days_until_renewal={{days_remaining}}
  reminder_number={{reminder_count}}
  ```
* **Event Timestamp:** Leave blank (current time)
* **Output Variable:** `reminder_event`

***

## Troubleshooting

### "Target Object Not Found" Error

**Error:** Can't find the object to add event to

**Possible causes:**

1. Object ID is wrong or doesn't exist
2. Variable containing ID is empty
3. Using wrong object type for that ID

**How to fix:**

1. Check the execution log - what ID was used?
2. Verify the object exists in HubSpot (search by ID)
3. Make sure previous action (lookup/search) found the record successfully
4. Check that object type matches the ID (contact ID needs object type = Contacts)

### "Invalid Event Type" Error

**Error:** Event type format is incorrect

**Possible causes:**

1. Event type contains spaces or special characters
2. Event type is empty

**How to fix:**

1. Use lowercase with underscores only: `onboarding_completed` not "Onboarding Completed"
2. No spaces, no special characters except underscore
3. Make sure the field isn't empty

### Events Not Showing on Timeline

**Events created but don't appear in HubSpot**

**Possible causes:**

1. Looking at wrong record
2. Timeline filtered to hide custom events
3. Timestamp is far in past/future

**How to fix:**

1. Verify you're looking at the correct contact/company/deal in HubSpot
2. In HubSpot timeline, click "Filter" and make sure custom events are enabled
3. Check the timestamp - events in the far future or distant past might not show by default
4. Refresh the HubSpot page

### Timestamp Not Parsing

**Timestamp field showing current time instead of expected date**

**Possible causes:**

1. Date format not recognized
2. Variable is empty or has invalid value

**How to fix:**

1. Use one of the supported formats (ISO 8601 is most reliable: `2025-10-01T14:30:00Z`)
2. Check execution log to see what value was sent
3. If using a variable, verify it contains a valid date
4. Leave blank to use current time

***

## Tips & Best Practices

**✅ Do:**

* Use consistent event types across workflows (helps with reporting)
* Include meaningful descriptions that provide context
* Set custom properties for data you'll want to filter/report on later
* Use descriptive event titles that make sense at a glance
* Test with a single record before running on multiple records
* Use past timestamps to backfill historical events

**❌ Don't:**

* Use spaces or special characters in event type (breaks filtering)
* Create events without checking if target object exists first
* Log too many events (clutters timeline) - be selective
* Forget to include key context in description or properties
* Use vague event types like "event1" or "update" (not helpful later)

**Performance tips:**

* Creating timeline events is fast (under 1 second typically)
* You can create many events in a loop without issues
* Consider batching if creating thousands of events

***

## Related Actions

**What to do next:**

* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Find object ID before creating event
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find multiple records to log events on
* [Get Timeline Events](./hubspot-v2-get-timeline-events) - Retrieve events from a record's timeline
* [For Loop](./for_loop) - Create events on multiple records

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in event properties
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Triggering workflows from HubSpot

***

**Last Updated:** 2025-10-01
