# Source: https://docs.agent.ai/actions/end_statement.md

# End If/Else/For Statement

Mark the end of If/Else blocks or For loops - required to close conditional logic or iteration blocks.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vG61oEyqDtQ?si=VA1yu9ouWYYhN7HD" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Mark the end of conditional blocks - closes For Loops, If Conditions, and other control flow actions.

**Common uses:**

* Close every For Loop
* Close every If Condition
* Close every If/Else block
* Define the boundary of conditional actions

**Action type:** `end_condition`

***

## What This Does (The Simple Version)

Think of this like a closing bracket or parenthesis. When you open a For Loop or If Condition, you need to close it. End Condition tells the workflow "this is where the conditional block ends."

**Real-world example:**
You have a For Loop that updates 50 deals. The End Condition marks where the loop ends, so the workflow knows to jump back to the top and process the next deal, or continue to the next action if all deals are done.

***

## How It Works

The End Condition action closes any conditional block (For Loop, If Condition, If/Else). When the workflow reaches this action:

**For Loops:**

1. Checks if there are more items to process
2. If yes → Jumps back to For Loop, updates current item, runs actions again
3. If no → Exits and continues with actions after End Condition

**If Conditions:**

1. Marks where the "if true" actions end
2. Workflow continues with actions after End Condition

**If/Else Blocks:**

1. Marks where the entire if/else block ends
2. Workflow continues with actions after End Condition

**It's required** - every For Loop, If Condition, or If/Else must have a matching End Condition.

***

## Setting It Up

### When to Add It

Add the End Condition action **after all the actions inside your conditional block**.

### For Loops

**Structure:**

```
1. For Loop (start)
   - Loop through: target_deals
   - Current item: current_deal

2. Update HubSpot Object (repeats for each item)
3. Create Timeline Event (repeats for each item)

4. End Condition (marks the end of loop)

5. Send Email (runs once after loop finishes)
```

### If Conditions

**Structure:**

```
1. If Condition (check if deal amount > 10000)

2. Update HubSpot Object (runs only if condition is true)
3. Send Email (runs only if condition is true)

4. End Condition (marks the end of if block)

5. Log to Console (runs regardless of condition)
```

### If/Else Blocks

**Structure:**

```
1. If Condition (check if contact has email)

2. Send Email (runs if condition is true)

3. Else Condition (if condition is false)

4. Log to Console (runs if condition is false)

5. End Condition (marks the end of entire if/else block)

6. Update Contact (runs regardless of condition)
```

### How to Add It

When building your workflow:

1. Add your conditional action (For Loop, If Condition, etc.)
2. Add all the actions that should be inside that block
3. Add the **End Condition** action
4. (Optional) Add actions after End Condition that should run after the block

**No configuration needed** - End Condition has no settings to configure. Just add it to your workflow.

***

## What Happens at End Condition

### In a For Loop

**Loop continues:**

* If more items exist, current item variable updates and workflow jumps back
* All actions between For Loop and End Condition run again

**Loop exits:**

* If no more items, workflow continues with action after End Condition
* Loop variables no longer exist

### In an If Condition

**After true actions:**

* End Condition marks where the "if true" actions end
* Workflow continues with actions after End Condition
* If condition was false, these actions were skipped entirely

### In an If/Else Block

**After entire block:**

* End Condition marks where the entire if/else block ends
* Either the "if true" or "else" actions ran (never both)
* Workflow continues with actions after End Condition

***

## Common Workflows

### For Loop with End Condition

**Goal:** Update multiple deals and send confirmation when done

1. **Search HubSpot (V2)**
   * Find deals
   * Output Variable: `target_deals`

2. **For Loop**
   * Loop through: `target_deals`
   * Current item: `current_deal`

3. **Update HubSpot Object** (inside loop)
   * Update the deal

4. **End Condition** ← Closes the For Loop

5. **Send Email** (after loop)
   * Confirmation that all deals were updated

### If Condition with End Condition

**Goal:** Only update high-value deals

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal`

2. **If Condition**
   * Check if `deal.properties.amount` > 10000

3. **Update HubSpot Object** (only runs if true)
   * Update the deal stage

4. **Send Email** (only runs if true)
   * Notify sales team

5. **End Condition** ← Closes the If Condition

6. **Log to Console** (runs regardless)
   * Log that workflow completed

### If/Else with End Condition

**Goal:** Send email if contact has email address, otherwise log

1. **Lookup HubSpot Object (V2)**
   * Get contact
   * Output Variable: `contact`

2. **If Condition**
   * Check if `contact.properties.email` is not empty

3. **Send Email** (runs if true)
   * Send to contact's email

4. **Else Condition**

5. **Log to Console** (runs if false)
   * Log "No email address found"

6. **End Condition** ← Closes the entire if/else block

7. **Update Contact** (runs regardless)
   * Update last contacted date

***

## Real Examples

### Loop with Count Tracking

**Scenario:** Update deals and count how many were updated

1. **Set Variable**
   * `count` = `0`

2. **Search HubSpot (V2)**
   * Output Variable: `deals`

3. **For Loop**
   * Loop through: `deals`
   * Current item: `current_deal`

4. **Update HubSpot Object**
   * Update deal

5. **Set Variable**
   * Increment `count`

6. **End Condition** ← Closes For Loop

7. **Send Email**
   * Subject: "Updated \[count] deals"

### Conditional Update

**Scenario:** Update contact only if they're in a specific lifecycle stage

1. **Lookup HubSpot Object (V2)**
   * Get contact
   * Output Variable: `contact`

2. **If Condition**
   * Check if `contact.properties.lifecycle_stage` equals "lead"

3. **Update HubSpot Object**
   * Set lifecycle\_stage to "marketingqualifiedlead"

4. **Create Timeline Event**
   * Log stage change

5. **End Condition** ← Closes If Condition

6. **Log to Console**
   * "Workflow complete"

***

## Troubleshooting

### "Missing End Condition" Error

**Error:** Conditional block without End Condition

**How to fix:**

1. After all actions inside your conditional block, add an **End Condition** action
2. Make sure there's exactly one End Condition for each conditional block
3. Check that End Condition is after all the actions you want inside the block

### Actions After End Condition Don't Run

**Actions after End Condition are skipped**

**Possible causes:**

1. Error inside conditional block stops execution
2. For Loop timeout

**How to fix:**

1. Check execution log for errors
2. Fix errors in actions inside the block
3. For loops: reduce item count to test

### Wrong Actions Repeating

**Actions outside the block are repeating (For Loop)**

**Possible causes:**

1. End Condition is in the wrong place (too far down)

**How to fix:**

1. Move End Condition to immediately after the last action you want repeated
2. Actions after End Condition should only run once

### If/Else Not Working as Expected

**Wrong branch is executing**

**Possible causes:**

1. End Condition missing or in wrong place
2. Else Condition missing

**How to fix:**

1. Structure should be: If Condition → \[true actions] → Else Condition → \[false actions] → End Condition
2. Make sure End Condition is after both branches

***

## Tips & Best Practices

**✅ Do:**

* Always add End Condition after every conditional block
* Place End Condition after all actions you want inside the block
* Use one End Condition per conditional block (For Loop, If, If/Else)
* Check execution log to verify blocks executed correctly

**❌ Don't:**

* Forget to add End Condition (conditional blocks won't work)
* Put End Condition in the middle of actions you want in the block
* Add multiple End Conditions for one conditional block
* Try to access loop variables after End Condition (they're gone)

**Structure tips:**

* Conditional actions and End Condition are like opening and closing brackets
* Everything between them is inside the block
* Everything after End Condition runs after the block completes
* Keep blocks simple - complex nested conditions are harder to debug

***

## Related Actions

**Always used together:**

* [For Loop](./for_loop) - Starts a loop (requires End Condition)
* [If Condition](./if_else) - Conditional execution (requires End Condition)
* [Set Variable](./set-variable) - Save data from inside blocks

**Related guides:**

* [Variable System](./builder/template-variables) - Understanding variable scope

***

**Last Updated:** 2025-10-01
