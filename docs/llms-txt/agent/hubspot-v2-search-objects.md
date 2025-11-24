# Source: https://docs.agent.ai/actions/hubspot-v2-search-objects.md

# Search HubSpot

Find contacts, deals, companies, and other HubSpot records based on criteria you specify.

**Common uses:**

* Find all deals in a specific stage
* Get contacts matching certain criteria
* Search for companies by property values
* Pull records for bulk processing

**Action type:** `hubspot.v2.search_objects`

***

## How It Works

This action searches your HubSpot CRM and returns a list of matching records. You choose what type of object to search (contacts, deals, etc.), optionally add filters to narrow results, and select which properties to get back.

The results are saved to a variable you can use in later actions—usually in a loop to process each record.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Search HubSpot action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to search. For example, click **Deals** if you're searching for deals.

### Step 2: Add Search Filters (Optional)

After selecting the object type, you'll see a "Search Contact Properties" section (or "Search Deal Properties", etc. depending on your object type).

**Leave it empty** to get all records (up to your limit).

**To add filters:**

1. Click the **"+ Add Property"** button
2. This opens the property picker - select a property to filter by (e.g., "City", "Deal Stage", "Lifecycle Stage")
3. Click **Done**

**For each filter you add, you'll see:**

* **Property name** (e.g., "City")
* **Operator dropdown** - Choose how to compare:
  * **Equals** - Exact match
  * **Not Equals** - Doesn't match
  * **Contains** - Text contains this value
  * **Greater Than** - Number/date is greater
  * **Less Than** - Number/date is less
  * **Greater Than or Equal**
  * **Less Than or Equal**
  * **Has Property** - Property has any value
  * **Not Has Property** - Property is empty
* **Value field** - Enter the value or click `{}` to insert a variable

**Example filters:**

**Find closed-won deals:**

* Property: Deal Stage
* Operator: Equals
* Value: "closedwon"

**Find contacts in a specific city:**

* Property: City
* Operator: Equals
* Value: "San Francisco"

**Find deals over \$10,000:**

* Property: Amount
* Operator: Greater Than
* Value: "10000"

**Find contacts who haven't been contacted recently:**

* Property: Last Contact Date
* Operator: Less Than
* Value: Click `{}` → select `thirty_days_ago` variable

**Using variables in filter values:**

Click the `{}` button in the value field to insert a variable from previous actions or the trigger.

**Example:** Filter by a stage that was sent via webhook

* Property: Deal Stage
* Operator: Equals
* Value: Click `{}` → select `target_stage` (from webhook)

**Adding multiple filters:**
Each filter you add works with AND logic (records must match ALL filters).

**Tips:**

* Use the property picker to avoid typos in property names
* Operator choice matters: "Equals" requires exact match, "Contains" is more flexible
* Use Greater Than/Less Than for numbers and dates
* Values are case-sensitive for exact matches

### Step 3: Choose Properties to Retrieve

In the "Retrieve Contact Properties" section (or "Retrieve Deal Properties", etc.), click the **"+ Add Property"** button to select which HubSpot properties you want to get back in your search results.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**The properties you select will be included in each search result.**

**Note:** This is a separate section from the search filters. Search filters determine WHICH records to find. Retrieve properties determine WHAT data to get back from those records.

**Tips for choosing properties:**

* Only select what you'll actually use (faster searches)
* Always include `hs_object_id` if you'll update records or look up related data later
* Use the search bar to quickly find properties
* Common properties for contacts: `firstname`, `lastname`, `email`, `phone`
* Common properties for deals: `dealname`, `dealstage`, `amount`, `closedate`, `hs_object_id`

**Can't find a property?** It might not exist in your HubSpot. Check HubSpot → Settings → Properties to see all available properties.

### Step 4: Sort Results (Optional)

Choose how to order your results by entering a sort value.

**Examples:**

* `createdate` - Oldest first
* `-createdate` - Newest first (the minus sign means descending)
* `amount` - Smallest to largest
* `-amount` - Largest to smallest

**Leave blank** for HubSpot's default order (usually by creation date).

### Step 5: Set Result Limit (Optional)

Enter the maximum number of results to return.

**Default:** 100
**Maximum:** 1000

**When to adjust:**

* **Testing?** Use 10-20 to run faster
* **Production?** Set based on how many you expect (100-500 is common)
* **Processing in a loop?** Remember that 1000 records takes time!

### Step 6: Name Your Output Variable

Give the search results a descriptive name in the "Output Variable Name" field.

**Good names:**

* `qualified_deals`
* `inactive_contacts`
* `target_companies`
* `recent_tickets`

This is the variable name you'll use to access the results in later actions.

***

## What You Get Back

The search returns a **list** of objects. Each object contains the properties you selected in Step 3.

**Example:** If you searched for deals and selected properties `dealname`, `amount`, `hs_object_id`:

**Output saved to `qualified_deals`:**

```
[
  {
    "dealname": "Acme Corp - Enterprise",
    "amount": "50000",
    "hs_object_id": "12345"
  },
  {
    "dealname": "TechCo Deal",
    "amount": "25000",
    "hs_object_id": "67890"
  }
]
```

***

## Using the Results

### In a For Loop (Most Common)

After your search action, add a **For Loop** action:

1. **Loop through:** Click to select your search results variable (e.g., `qualified_deals`)
2. **Current item variable:** Give each item a name (e.g., `current_deal`)

**Inside the loop, access properties:**

For any field that needs a value, click the **Insert Variable** button (the `{}` icon) and navigate:

* Select `current_deal`
* Then select the property you want (e.g., `dealname`, `amount`, `hs_object_id`)

**Example:** In an Update HubSpot Object action inside the loop:

* **Object ID:** Insert variable → `current_deal` → `hs_object_id`
* **Property to update:** Insert variable → `current_deal` → `dealname`

### Count How Many Results

Want to know how many records matched?

Add a **Set Variable** action after the search and use the variable picker to count the items in your results array.

### Get Just the First Result

To grab only the first record, use the variable picker to select the first item from your results array in any subsequent action.

***

## Common Workflows

### Find and Update Pattern

**Goal:** Search for records, then update each one

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Click "+ Add Property" and select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_update`

2. **For Loop**
   * Loop through: `deals_to_update`
   * Current item: `current_deal`

3. **Update HubSpot Object (V2)** - inside loop
   * Object ID: Insert variable → `current_deal` → `hs_object_id`
   * Update whatever properties you need

4. **End Loop**

### Search Using Trigger Data

**Goal:** Use data from a webhook to filter your search

**Webhook receives:** `target_stage` variable

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: Click `{}` → select `target_stage` (from webhook)
   * Output Variable: `matching_deals`

2. Process the results...

### Daily Report

**Goal:** Count records and send an email

1. **Search HubSpot (V2)**
   * Object Type: Tickets
   * Search Filters: Click "+ Add Property"
     * Property: Ticket Pipeline Stage
     * Operator: Equals
     * Value: "open"
   * Limit: 1000
   * Output Variable: `open_tickets`

2. **Set Variable**
   * Variable name: `ticket_count`
   * Value: Use variable picker to count `open_tickets`

3. **Send Email**
   * Subject: Type "You have " then insert `ticket_count` variable

***

## Real Examples

### Daily Deal Health Check

**Scenario:** Every morning at 9 AM, find all deals in "Presentation Scheduled" stage.

**Trigger:** Schedule (daily at 9:00 AM)

**Search Configuration:**

* **Object Type:** Deals
* **Search Filters:** Click "+ Add Property"
  * Property: Deal Stage
  * Operator: Equals
  * Value: "presentationscheduled"
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `hs_object_id`
  * `hubspot_owner_id`
* **Sort:** Select "Create Date" descending (newest first)
* **Limit:** 50
* **Output Variable:** `active_deals`

**Next steps:** Loop through `active_deals` and analyze each one.

### Find Contacts from Form Submission

**Scenario:** When someone submits a form, find their contact record.

**Webhook receives:** `email` variable from HubSpot form

**Search Configuration:**

* **Object Type:** Contacts
* **Search Filters:** Click "+ Add Property"
  * Property: Email
  * Operator: Equals
  * Value: Click `{}` → select `email` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `hs_object_id`
* **Limit:** 1 (expecting only one match)
* **Output Variable:** `found_contact`

**Next steps:** Check if contact was found, then enrich their data.

***

## Troubleshooting

### No Results Found

**The search returns an empty list `[]`**

**Possible causes:**

1. No records actually match your filters
2. Property name is misspelled in filters
3. Property value doesn't match exactly

**How to fix:**

1. Go to HubSpot and manually search using the same criteria—do records exist?
2. Double-check property names (they're case-sensitive!)
3. Look at an actual HubSpot record to see the exact value format
4. Try removing filters one by one to see which is excluding results

### Missing Properties in Results

**Records come back but properties you selected aren't showing up**

**Possible causes:**

1. You didn't add that property using "+ Add Property"
2. The property is actually empty in HubSpot
3. Property was added but not saved before running

**How to fix:**

1. Make sure you clicked "+ Add Property" and selected all properties you need
2. Check an actual HubSpot record—does it have values for those properties?
3. Re-add the property and save the action
4. Check the execution log to see exactly what was returned

### "Missing OAuth Scope" Error

**You don't have permission to access that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize access to that object type
4. Save and try the search again

**Required permissions by object:**

* **Contacts:** "Read Contacts"
* **Companies:** "Read Companies"
* **Deals:** "Read Deals"
* **Tickets:** "Read Tickets"

### Search is Slow (Takes 10+ Seconds)

**Possible causes:**

1. Returning too many results
2. Requesting too many properties
3. HubSpot account has millions of records

**How to fix:**

1. **Add filters** to narrow the search scope
2. **Lower the limit** (100 instead of 1000)
3. **Request fewer properties** (only what you need)
4. **Add specific filters** like date ranges instead of searching everything

***

## Tips & Best Practices

**✅ Do:**

* Always include `hs_object_id` in your properties if you'll update or reference records later
* Use the "+ Add Property" button to browse and select from your actual HubSpot properties
* Start with small limits while testing (10-20), then increase for production
* Test your filters in HubSpot's UI first to verify they return the right records
* Use descriptive output variable names
* Add filters to narrow results whenever possible

**❌ Don't:**

* Search for all records without filters (could return thousands!)
* Request every property when you only need a few
* Forget to set a limit (defaults to 100 but be explicit)
* Assume all properties have values—some might be empty
* Use misspelled property names in filters

**Performance tips:**

* Filters make searches faster—use them!
* Limit results to what you need (don't fetch 1000 if you'll only process 50)
* If looping through results, remember each iteration takes time
* The fewer properties you request, the faster the search

***

## Advanced Filtering

The simple `property=value` format works for exact matches. For more complex scenarios like:

* "Greater than" or "less than" comparisons
* Date range filtering
* OR logic between filters
* "Contains" text searches

See the **[Advanced Variable Usage](../builder/template-variables)** guide for JSON filter syntax.

***

## Related Actions

**What to do next:**

* [For Loop](./for_loop) - Process search results one by one
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update records you found
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get full details for specific records
* [If Condition](./if_else) - Filter results based on conditions

**Related guides:**

* [Variable System](../builder/template-variables) - Using search results in other actions
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Use webhook payloads to drive searches
* [Deal Analysis Workflow](../recipes/hubspot-deal-analysis) - Complete example

***

**Last Updated:** 2025-10-01
