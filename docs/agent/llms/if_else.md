# Source: https://docs.agent.ai/actions/if_else.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# If/Else Statement

Run actions only when certain conditions are met - perfect for conditional logic and branching workflows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SICac2Zw9kQ?si=q3q2WjgUBd74pvlk" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Run actions only when certain conditions are met - perfect for conditional logic and branching workflows.

**Common uses:**

* Only update high-value deals
* Skip contacts without email addresses
* Route based on deal stage
* Check if variables exist before using them
* Different actions for different scenarios

**Action type:** `if_condition`

***

## What This Does (The Simple Version)

Think of this like an "if this, then that" rule. You set a condition, and actions inside the if block only run when that condition is true. If it's false, they're skipped.

**Real-world example:**
You're sending follow-up emails to leads. You only want to email contacts who haven't been contacted in the last 7 days. Add an If Condition that checks "last contact date > 7 days ago" - the email action inside only runs if true.

***

## How It Works

The If Condition action evaluates a condition you provide. Based on the result:

**If TRUE:**

* Actions immediately after the If Condition run
* Continues until it reaches an Else Condition or End Condition

**If FALSE:**

* Actions after the If Condition are skipped
* Jumps to Else Condition (if present) or End Condition

**You must end every If Condition with an End Condition action.**

***

## Setting It Up

### Step 1: Add If Condition Action

When you add an If Condition action to your workflow, you'll see a query/condition field.

### Step 2: Write Your Condition

In the **"Condition"** field, describe what you want to check in plain English.

**The condition is evaluated by AI** - you can write it naturally:

**Examples:**

**Check if a value is above a threshold:**

```
The deal amount is greater than 10000
```

**Check if a field has a value:**

```
The contact email is not empty
```

**Check if a date is recent:**

```
The last contact date was within the last 7 days
```

**Check if a variable exists:**

```
The search results variable is not empty
```

**Compare values:**

```
The contact lifecycle stage equals "salesqualifiedlead"
```

**You can use variables** by clicking `{}` or typing them:

```
[deal amount] > 50000
```

### Step 3: Add Actions to Run If True

After the If Condition, add the actions that should run when the condition is TRUE.

**Example:**

1. **If Condition** - Check if deal amount greater than 10000
2. **Update HubSpot Object** - Update to VIP status (runs if TRUE)
3. **Send Email** - Notify sales director (runs if TRUE)
4. **End Condition** - Marks end of if block

### Step 4: Add Else Condition (Optional)

Want different actions if the condition is FALSE?

**Add an Else Condition action** after your "if true" actions:

1. **If Condition** - Check if contact has email
2. **Send Email** - (runs if TRUE)
3. **Else Condition**
4. **Create Task** - Manually find email (runs if FALSE)
5. **End Condition**

### Step 5: Close with End Condition

**Always add End Condition** at the end to close the if/else block.

***

## Condition Examples

### Numeric Comparisons

```
[deal amount] > 10000
[relevance_score] >= 8
[contact_count] < 5
```

### String Comparisons

```
[contact lifecycle_stage] equals "lead"
[deal stage] is "closedwon"
[company industry] contains "technology"
```

### Empty/Exists Checks

```
[contact email] is not empty
[search_results] has items
[timeline_events] is empty
The contact has a phone number
```

### Date Comparisons

```
[deal closedate] is in the future
[contact lastmodifieddate] is within last 30 days
The last activity was more than 7 days ago
```

### Boolean Checks

```
[enrichment_complete] is true
[contact emailoptout] equals false
The contact has not unsubscribed
```

### Complex Conditions

```
The deal amount is greater than 50000 AND the deal stage is "presentationscheduled"
The contact has an email OR a phone number
The lifecycle stage is "lead" or "marketingqualifiedlead"
```

***

## Common Workflows

### Only Update High-Value Deals

**Goal:** Update deal priority only if amount exceeds threshold

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal`

2. **If Condition**
   * Condition: `[deal amount] > 50000`

3. **Update HubSpot Object (V2)** (inside if block)
   * Update `priority` to "High"

4. **End Condition**

### Skip Contacts Without Email

**Goal:** Send email only if contact has email address

1. **Search HubSpot (V2)**
   * Find contacts
   * Output Variable: `contacts`

2. **For Loop**
   * Loop through: `contacts`
   * Current item: `current_contact`

3. **If Condition** (inside loop)
   * Condition: `[current contact email] is not empty`

4. **Send Email** (inside if block)
   * Send to: `[current contact email]`

5. **End Condition**

6. **End Loop**

### Route by Deal Stage

**Goal:** Different actions based on deal stage

1. **Lookup HubSpot Object (V2)**
   * Get deal
   * Output Variable: `deal`

2. **If Condition**
   * Condition: `[deal stage] equals "closedwon"`

3. **Create Timeline Event** (if won)
   * Log onboarding kickoff

4. **Else Condition**

5. **Update HubSpot Object** (if not won)
   * Update follow-up date

6. **End Condition**

### Check Before Using Variable

**Goal:** Only process if search found results

1. **Search HubSpot (V2)**
   * Search for deals
   * Output Variable: `deals`

2. **If Condition**
   * Condition: `[deals] is not empty`

3. **For Loop** (inside if block)
   * Loop through deals

4. **Process each deal...**

5. **End Loop**

6. **End Condition**

***

## Real Examples

### Lead Qualification

**Scenario:** Auto-qualify leads based on criteria

**Trigger:** Contact created webhook

**Condition:**

```
[contact company] is not empty AND [contact jobtitle] contains "Director" or "VP" or "C-level"
```

**If TRUE:**

* Update lifecycle stage to "salesqualifiedlead"
* Assign to senior sales rep
* Send immediate notification

**If FALSE:**

* Keep as "lead"
* Add to nurture sequence

### Deal Health Check

**Scenario:** Flag stale deals

**Trigger:** Scheduled (daily)

**Inside loop for each deal:**

**If Condition:**

```
The last activity was more than 14 days ago
```

**If TRUE:**

* Update deal property `status` to "stale"
* Create task for owner to follow up

**End Condition**

### Conditional Enrichment

**Scenario:** Only enrich important contacts

**Trigger:** Contact updated webhook

**Condition:**

```
[contact company] is not empty AND [contact lifecycle_stage] equals "salesqualifiedlead"
```

**If TRUE:**

* Run web search for company
* AI enrichment analysis
* Update contact with insights

**Else:**

* Log that contact wasn't enriched
* Add to later enrichment queue

**End Condition**

***

## If/Else Patterns

### Simple If (No Else)

```
1. If Condition
2. Action (runs if true)
3. Action (runs if true)
4. End Condition
5. Action (always runs)
```

### If/Else

```
1. If Condition
2. Action (runs if true)
3. Else Condition
4. Action (runs if false)
5. End Condition
6. Action (always runs)
```

### Multiple Conditions (Nested)

```
1. If Condition - Check A
2.   If Condition - Check B (nested)
3.     Action (runs if both A and B are true)
4.   End Condition
5. End Condition
```

### Sequential Checks

```
1. If Condition - Check if deal > 10000
2.   Update to "High Priority"
3. End Condition

4. If Condition - Check if deal > 50000
5.   Notify VP Sales
6. End Condition
```

***

## Troubleshooting

### Condition Always TRUE (or Always FALSE)

**Actions always run (or never run)**

**Possible causes:**

1. Condition is written incorrectly
2. Variable doesn't exist
3. Variable has unexpected value

**How to fix:**

1. Check execution log - what did the AI evaluate?
2. Test condition with known values first
3. Use simple conditions initially (e.g., `5 > 3` should always be true)
4. Make sure variables exist before referencing them
5. Check variable values in execution log

### Can't Access Variables

**Variable in condition shows as empty**

**Possible causes:**

1. Variable doesn't exist (action before if condition failed)
2. Variable name spelled wrong
3. Wrong path to nested property

**How to fix:**

1. Check execution log - does the variable exist?
2. Verify variable name matches output from previous action
3. For nested properties: `[contact email]` not `[contact.email]`

### Actions After If Condition Not Running

**Expected actions are skipped**

**Possible causes:**

1. Condition evaluated to FALSE
2. Missing End Condition
3. Error inside if block

**How to fix:**

1. Check execution log - what was the condition result (true/false)?
2. Add End Condition after if block
3. Look for errors in actions inside the if block

### Else Block Not Running

**Else actions don't execute when condition is false**

**Possible causes:**

1. Missing Else Condition action
2. Else Condition in wrong place
3. Missing End Condition

**How to fix:**

1. Structure must be: If Condition → \[true actions] → Else Condition → \[false actions] → End Condition
2. Make sure Else Condition is before End Condition
3. Check execution log to see execution path

***

## Tips & Best Practices

**✅ Do:**

* Write conditions in plain English (AI evaluates them)
* Use clear, simple conditions when possible
* Always add End Condition to close if blocks
* Test conditions with known values first
* Check execution log to see true/false result
* Use variables by clicking `{}` button for accuracy
* Add Else Condition for "if false" actions

**❌ Don't:**

* Forget to add End Condition (required)
* Reference variables that might not exist without checking first
* Write overly complex conditions (break into multiple if statements)
* Assume condition will always evaluate as expected (test it)
* Nest too many if conditions (hard to debug)

**Writing good conditions:**

* **Clear:** "The deal amount is greater than 10000"
* **Specific:** "The contact lifecycle stage equals 'salesqualifiedlead'"
* **Testable:** Use values you can verify
* **Safe:** Check if variable exists first if unsure

**Performance tips:**

* Conditions evaluate quickly (less than 1 second)
* Simple conditions faster than complex
* Avoid unnecessary nesting

***

## Related Actions

**Always used together:**

* [End Condition](./end_statement) - Required to close if blocks (can close If, For, or If/Else)
* [Set Variable](./set-variable) - Often used inside if blocks

**Common patterns:**

* Use inside [For Loop](./for_loop) to conditionally process items
* Use with [Update HubSpot Object (V2)](./hubspot-v2-update-object) to conditionally update

**Related guides:**

* [Variable System](./builder/template-variables) - Using variables in conditions

***

**Last Updated:** 2025-10-01
