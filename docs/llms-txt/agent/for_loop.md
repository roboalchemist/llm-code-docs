# Source: https://docs.agent.ai/actions/for_loop.md

# For Loop

Repeat actions for each item in a list or a specific number of times - automate repetitive tasks efficiently.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3J3TKMJ4pXI?si=vFycP1JMoowvaJqe" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Process multiple items one at a time - perfect for updating, analyzing, or taking action on lists of records.

**Common uses:**

* Loop through search results and update each record
* Process each contact in a list
* Analyze multiple deals one by one
* Send emails to a list of people

**Action type:** `for_condition`

***

## What This Does (The Simple Version)

Think of this like going through a stack of papers on your desk, one at a time. You pick up the first paper, do something with it, put it down, then pick up the next one. The loop continues until you've gone through the entire stack.

**Real-world example:**
You search HubSpot and find 50 deals in "Presentation Scheduled" stage. You want to update each one to the next stage. The For Loop lets you go through all 50 deals, one by one, and update each one.

***

## How It Works

This action repeats the actions inside the loop for each item in a list. You provide:

1. **What to loop through** (usually a list from a search action)
2. **What to call each item** (the variable name for the current item)

The loop automatically:

* Starts at the first item
* Runs all actions inside the loop
* Moves to the next item
* Repeats until all items are processed

***

## Setting It Up

### Step 1: Add a For Loop Action

When you add a For Loop action to your workflow, you'll see two main fields.

### Step 2: Choose What to Loop Through

In the **"Loop through"** field, click the `{}` button to select the list you want to process.

**Usually this is:**

* Search results from a **Search HubSpot (V2)** action
* A list from a previous action
* An array variable from your trigger

**Example:**

1. Earlier in your workflow, you ran **Search HubSpot (V2)** and saved results to `target_deals`
2. In the For Loop, click `{}` → select `target_deals`

**You can also type a number** to loop a specific number of times:

* Type `5` to loop 5 times
* Type `10` to loop 10 times
* Click `{}` to insert a variable containing a number

### Step 3: Name the Current Item

In the **"Current item variable"** field, type a name for the variable that will hold each item as you loop through.

**Good names:**

* If looping through deals: `current_deal`
* If looping through contacts: `current_contact`
* If looping through companies: `current_company`
* If looping through tickets: `current_ticket`

**This variable will change on each iteration** - first it's the 1st item, then the 2nd, then the 3rd, etc.

### Step 4: Add Actions Inside the Loop

After the For Loop action, add the actions you want to run for each item. These actions will execute once per item.

**Common actions inside loops:**

* **Update HubSpot Object (V2)** - Update the current record
* **Create Timeline Event (V2)** - Log an event on each record
* **If Condition** - Check something about the current item
* **Set Variable** - Calculate or store data

**Inside these actions**, use the current item variable by clicking `{}` and selecting it.

**Example:** Inside an Update HubSpot Object action:

* Object ID: Click `{}` → select `current_deal` → `hs_object_id`
* Properties: Update based on `current_deal` data

### Step 5: End the Loop

After all the actions you want repeated, add an **End Loop** action. This tells the workflow where the loop ends.

**The workflow structure looks like:**

1. Search HubSpot (V2) → saves to `target_deals`
2. **For Loop** → loop through `target_deals`, current item: `current_deal`
3. Update HubSpot Object (V2) → update `current_deal`
4. Create Timeline Event (V2) → log event on `current_deal`
5. **End Loop**
6. (Actions here run after the loop finishes)

***

## How Variables Work in Loops

### Current Item Variable

Each time through the loop, the current item variable gets updated with the next item.

**Example:** Looping through 3 deals saved to `target_deals`

**Iteration 1:**

```
current_deal = {
  "dealname": "Acme Corp Deal",
  "hs_object_id": "12345",
  "amount": "50000"
}
```

**Iteration 2:**

```
current_deal = {
  "dealname": "TechCo Deal",
  "hs_object_id": "67890",
  "amount": "25000"
}
```

**Iteration 3:**

```
current_deal = {
  "dealname": "BigBiz Deal",
  "hs_object_id": "11111",
  "amount": "100000"
}
```

**After the loop ends,** `current_deal` no longer exists (it's scoped to the loop only).

### Loop Index (Optional)

You can also track which iteration you're on with an index variable. This is automatic - you don't need to set it up.

**Usage:** In advanced scenarios, you might reference the loop index to know "I'm on item 5 of 50".

***

## Common Workflows

### Update All Deals in a Stage

**Goal:** Find all deals in a specific stage and move them to the next stage

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_update`

2. **For Loop**
   * Loop through: Click `{}` → select `deals_to_update`
   * Current item variable: `current_deal`

3. **Update HubSpot Object (V2)** (inside loop)
   * Object Type: Deals
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_deal` → `hs_object_id`
   * Update Properties:
     * `dealstage`: "decisionmakerboughtin"
   * Output Variable: `updated_deal`

4. **End Loop**

### Send Email to Each Contact

**Goal:** Loop through a list of contacts and send each one a personalized email

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Search Filters: (your criteria)
   * Retrieve Properties: Select `firstname`, `email`, `company`
   * Output Variable: `target_contacts`

2. **For Loop**
   * Loop through: Click `{}` → select `target_contacts`
   * Current item variable: `current_contact`

3. **Send Email** (inside loop)
   * To: Click `{}` → `current_contact` → `properties` → `email`
   * Subject: Type "Hi " then click `{}` → `current_contact` → `properties` → `firstname`
   * Body: Use personalized content with variables from `current_contact`

4. **End Loop**

### Log Timeline Events on Multiple Records

**Goal:** Create a timeline event on each deal in a list

1. **Search HubSpot (V2)**
   * Find your target deals
   * Output Variable: `opportunity_deals`

2. **For Loop**
   * Loop through: Click `{}` → select `opportunity_deals`
   * Current item variable: `deal`

3. **Create Timeline Event (V2)** (inside loop)
   * Object Type: Deals
   * Target Object ID: Click `{}` → `deal` → `hs_object_id`
   * Event Type: `opportunity_reviewed`
   * Event Title: Type "Deal Reviewed: " then click `{}` → `deal` → `properties` → `dealname`
   * Output Variable: `event_result`

4. **End Loop**

***

## Real Examples

### Deal Health Check Loop

**Scenario:** Every morning, find all deals in "Presentation Scheduled" stage and analyze each one.

**Trigger:** Scheduled (daily at 9:00 AM)

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters:
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: `dealname`, `hs_object_id`, `amount`, `closedate`
   * Output Variable: `active_deals`

2. **For Loop**
   * Loop through: `active_deals`
   * Current item variable: `current_deal`

3. **Get Timeline Events (V2)** (inside loop)
   * Object Type: Deals
   * Object ID: Click `{}` → `current_deal` → `hs_object_id`
   * Output Variable: `deal_events`

4. **If Condition** (inside loop)
   * Condition: Check if `deal_events` is empty (no recent activity)
   * If true: Update deal stage to "stalled"

5. **End Loop**

**Result:** All active deals are checked, and deals with no activity are flagged.

### Contact Enrichment Loop

**Scenario:** Enrich all new contacts with external data.

**Trigger:** Scheduled (daily at midnight)

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Search Filters:
     * Property: Lifecycle Stage
     * Operator: Equals
     * Value: "lead"
   * Retrieve Properties: `email`, `firstname`, `lastname`, `hs_object_id`
   * Limit: 100
   * Output Variable: `new_leads`

2. **For Loop**
   * Loop through: `new_leads`
   * Current item variable: `lead`

3. **External API Call** (inside loop)
   * Lookup company data using `lead.properties.email`
   * Output Variable: `enrichment_data`

4. **Update HubSpot Object (V2)** (inside loop)
   * Object Type: Contacts
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `lead` → `hs_object_id`
   * Update Properties with enrichment data

5. **End Loop**

***

## Troubleshooting

### Loop Doesn't Run

**The loop actions are skipped completely**

**Possible causes:**

1. The list you're looping through is empty
2. Variable doesn't exist or is not a list
3. Loop count is 0

**How to fix:**

1. Check the execution log - what was the loop count?
2. Verify the search action returned results (check its output in the log)
3. Make sure you're using the correct variable name (the one from the search action's output variable)
4. Test your search manually in HubSpot to confirm records exist

### Loop Only Runs Once

**Loop processes only the first item then stops**

**Possible causes:**

1. Missing **End Loop** action
2. Error inside the loop on the 2nd iteration
3. Break condition triggered

**How to fix:**

1. Make sure you added an **End Loop** action after all loop body actions
2. Check execution log - did an error occur on iteration 2?
3. Fix any errors in actions inside the loop (they might work for some items but fail for others)

### Can't Access Loop Variable After Loop

**Error:** Variable `current_deal` not found (outside the loop)

**This is expected behavior** - loop variables only exist inside the loop.

**How to fix:**

1. If you need data from the loop later, use **Set Variable** inside the loop to save it
2. Save results to a list variable that persists after the loop

**Example:**
Inside loop:

* **Set Variable** → `all_updated_ids` → append `current_deal.hs_object_id`

After loop:

* Access `all_updated_ids` (still available)

### Loop Running Too Long

**Loop takes forever or times out**

**Possible causes:**

1. Looping through too many items (1000+)
2. Slow actions inside the loop (external API calls)
3. Nested loops (loop inside a loop)

**How to fix:**

1. Limit search results to smaller batches (100-500)
2. Optimize actions inside loop - remove unnecessary steps
3. Consider breaking into multiple workflows
4. Use result limits on your search action

***

## Tips & Best Practices

**✅ Do:**

* Always use **End Loop** to close the loop
* Use descriptive current item variable names (`current_deal` not `item`)
* Limit search results while testing (10-20 items to start)
* Check loop variable in execution log to see what's being processed
* Use **If Condition** inside loops to skip items that don't meet criteria

**❌ Don't:**

* Forget to add **End Loop** (loop won't work)
* Loop through thousands of items at once (use batches)
* Create variables inside loops without understanding scope (they'll be overwritten each iteration)
* Put slow external API calls inside loops without considering total time
* Access loop variables outside the loop (they won't exist)

**Performance tips:**

* Loops can handle 100-500 items comfortably
* Each action inside the loop adds to total time (5 actions × 100 items = 500 action executions)
* For large lists (1000+), consider splitting into multiple workflow runs
* Use search result limits to control loop size

***

## Related Actions

**What to use with loops:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Get lists to loop through
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update each record in loop
* [End Loop](./end_statement) - Required to close the loop
* [If Condition](./if_else) - Conditionally process items in loop

**Related guides:**

* [Variable System](./builder/template-variables) - Understanding variable scope in loops
* [Deal Analysis Workflow](./recipes/hubspot-deal-analysis) - Complete example with loops

***

**Last Updated:** 2025-10-01
