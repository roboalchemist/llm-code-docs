# Source: https://docs.agent.ai/actions/set-variable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Variable

Create or update variables during workflow execution - store values, build counters, calculate totals, or save results for later actions.

<img src="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=7b7eb43e684aeb09dc2dcbec1f2c055d" alt="Set Variable Pn" data-og-width="1194" width="1194" data-og-height="1148" height="1148" data-path="images/set_variable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=280&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=dc714a20e0020bb27efce40ed8fadda7 280w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=560&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=2f14286f91b09bccc6ba1493548f7e8f 560w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=840&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=0b6ce0c1b590a3fb33749806a0eb9681 840w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=1100&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=58fffd19d8edf62b8d4bc84f274d0bd4 1100w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=1650&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=9e4010787ea8b5794f8af5803b27f6af 1650w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=2500&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=092b65ef7234c0d728a3775fb1a49e82 2500w" />

**Common uses:**

* Create counters in loops
* Store calculated values
* Build text from multiple sources
* Save API responses
* Track totals across iterations
* Set default values

**Action type:** `set_variable`

***

## What This Does (The Simple Version)

Think of this like creating a sticky note during your workflow. You can write down a value and give it a name - then use that name in later actions. It's useful for calculations, counters, or storing data you'll need again.

**Real-world example:**
You're looping through 50 deals and want to count how many are high-value. Create a counter variable set to `0`, then inside the loop, increase it by 1 each time you find a high-value deal. After the loop, you know exactly how many there are.

***

## How It Works

The Set Variable action creates or updates a variable. You specify:

1. **Variable name** - What to call it
2. **Value** - What to store (text, number, or data from other variables)

**If the variable exists:** It updates it
**If it doesn't exist:** It creates it

The variable persists through the rest of the workflow and can be referenced in any later action.

***

## Setting It Up

### Step 1: Add Set Variable Action

Add the **Set Variable** action to your workflow.

### Step 2: Name Your Variable

In the **"Variable Name"** field, type a name for your variable.

**Good names:**

* `deal_count`
* `total_amount`
* `high_priority_deals`
* `enrichment_result`
* `calculated_score`

**Naming rules:**

* Use lowercase letters, numbers, underscores
* No spaces or special characters
* Make it descriptive

### Step 3: Set the Value

In the **"Value"** field, enter what you want to store.

**Three ways to set values:**

**Option 1: Type directly**

* Type text or numbers directly
* Example: `0` (for a counter)
* Example: `High Priority` (for a status)

**Option 2: Insert variables**

* Hover to see `{}` button
* Click to select variable from previous action
* Example: Click `{}` → `deal_record` → `properties` → `amount`

**Option 3: Combine text and variables**

* Mix typed text with variables
* Example: Type "Total: \$" then click `{}` → select `total_amount`
* Result: "Total: \$50000"

***

## Common Patterns

### Create a Counter

**Goal:** Count items in a loop

**Setup:**

1. **Before loop** - Set Variable
   * Variable Name: `counter`
   * Value: `0`

2. **Inside loop** - Set Variable
   * Variable Name: `counter`
   * Value: Click `{}` → `counter`, then type ` + 1` (AI evaluates math)

**Result:** After loop, `counter` contains total count

### Calculate a Total

**Goal:** Add up deal amounts

**Setup:**

1. **Before loop** - Set Variable
   * Variable Name: `total_amount`
   * Value: `0`

2. **Inside loop** - Set Variable
   * Variable Name: `total_amount`
   * Value: \{\{total\_amount}} + \{\{current\_deal.properties.amount}}

**Result:** After loop, `total_amount` is the sum

### Store a Calculation

**Goal:** Calculate a percentage

**Setup:**

* **Set Variable**
  * Variable Name: `win_rate`
  * Value: \{\{won\_deals}} / \{\{total\_deals}} \* 100

**Result:** `win_rate` contains the percentage

### Build Text from Multiple Parts

**Goal:** Create a summary message

**Setup:**

* **Set Variable**
  * Variable Name: `summary`
  * Value: Type "Deal " then click `{}` → `deal_name`, type " worth \$" then click `{}` → `deal_amount`, type " closed on " then click `{}` → `close_date`

**Result:** `summary` = "Deal Acme Corp worth \$50000 closed on 2025-01-15"

### Set a Default Value

**Goal:** Provide fallback if data is missing

**Setup:**

* **Set Variable**
  * Variable Name: `contact_name`
  * Value: \{\{contact.properties.firstname}} \{\{contact.properties.lastname}} or if empty `Unknown Contact`

**Result:** `contact_name` has name or "Unknown Contact"

***

## Common Workflows

### Count High-Value Deals

**Goal:** Count how many deals exceed threshold

1. **Set Variable** (before loop)
   * Variable Name: `high_value_count`
   * Value: `0`

2. **Search HubSpot (V2)**
   * Find all deals
   * Output Variable: `all_deals`

3. **For Loop**
   * Loop through: `all_deals`
   * Current item: `current_deal`

4. **If Condition** (inside loop)
   * Condition: \{\{current\_deal.properties.amount}} > 50000

5. **Set Variable** (inside if block)
   * Variable Name: `high_value_count`
   * Value: \{\{high\_value\_count}} + 1

6. **End Condition**

7. **End Loop**

**Result:** `high_value_count` contains the total

### Build a Report Summary

**Goal:** Create text summary from multiple sources

1. **Search HubSpot (V2)**
   * Find deals
   * Output Variable: `deals`

2. **Get Timeline Events**
   * Get activity
   * Output Variable: `events`

3. **Set Variable**
   * Variable Name: `report`
   * Value: "Found \{\{deals}} deals with \{\{events}} total activities"

4. **Send Email**
   * Body: Click `{}` → select `report`

### Track Running Total

**Goal:** Sum deal amounts across multiple stages

1. **Set Variable**
   * Variable Name: `total_pipeline`
   * Value: `0`

2. **For Loop** through deals

3. **Set Variable** (inside loop)
   * Variable Name: `total_pipeline`
   * Value: \{\{total\_pipeline}} + \{\{current\_deal.properties.amount}}

4. **End Loop**

5. **Update HubSpot Object**
   * Update custom property with `total_pipeline`

***

## Real Examples

### Deal Stage Counter

**Scenario:** Count deals in each stage

**Before loop:**

* Set `proposal_count` = `0`
* Set `negotiation_count` = `0`
* Set `closed_won_count` = `0`

**Inside loop:**

* If stage = "proposal" → Increment `proposal_count`
* If stage = "negotiation" → Increment `negotiation_count`
* If stage = "closedwon" → Increment `closed_won_count`

**After loop:** Use counts in report or dashboard update

### Enrichment Scoring

**Scenario:** Build a lead score from multiple factors

**Setup:**

* Set `score` = `0`
* If company exists → Set `score` = \{\{score}} + 10
* If job title contains "VP" → Set `score` = \{\{score}} + 15
* If email domain is corporate → Set `score` = \{\{score}} + 5
* If LinkedIn profile found → Set `score` = \{\{score}} + 10

**Result:** `score` contains total lead score

***

## Troubleshooting

### Variable Not Updating

**Value stays the same despite Set Variable**

**Possible causes:**

1. Set Variable action not running (inside skipped if block)
2. Variable name misspelled
3. Value formula incorrect

**How to fix:**

1. Check execution log - did action run?
2. Verify exact variable name (case-sensitive)
3. Test formula with simple values first
4. Check if variable exists before trying to update

### Math Not Working

**Calculation returns wrong value**

**Possible causes:**

1. Variables are text, not numbers
2. Formula syntax incorrect
3. Empty/null values in calculation

**How to fix:**

1. AI evaluates math - write it naturally: `5 + 3` or \{\{count}} + 1
2. Check execution log for actual values
3. Handle empty values: use If Condition to check first
4. Convert text to numbers if needed

### Variable Not Available Later

**Can't select variable in later action**

**Possible causes:**

1. Variable created inside loop (only exists inside loop)
2. Variable created inside if block (only exists in that block)
3. Set Variable action failed

**How to fix:**

1. Create variable BEFORE loop/if block if you need it after
2. Check execution log - did Set Variable succeed?
3. Variables created inside loops/if blocks have limited scope

### Wrong Variable Used

**Selected wrong variable from picker**

**Possible causes:**

1. Similar variable names
2. Variable from different loop iteration

**How to fix:**

1. Use descriptive names: `deal_count` not `count`
2. Check variable picker shows correct source
3. Review execution log to verify values

***

## Tips & Best Practices

**✅ Do:**

* Use descriptive variable names (`high_value_count` not `x`)
* Initialize counters to `0` before loops
* Initialize totals to `0` before calculations
* Use Set Variable for values you'll reference multiple times
* Create variables outside loops if you need them after
* Check execution log to verify values

**❌ Don't:**

* Use variable names that are too similar (`count1`, `count2`)
* Forget to initialize counters (leads to errors)
* Try to use variables before creating them
* Assume variables from loops persist after loop
* Overcomplicate formulas (break into multiple Set Variable actions)

**Performance tips:**

* Set Variable is instant (less than 0.1 seconds)
* No limit on number of variables
* Variables are lightweight (don't impact performance)

**Naming conventions:**

* **Counters:** `item_count`, `total_deals`, `high_priority_count`
* **Totals:** `total_amount`, `sum_value`, `pipeline_total`
* **Calculations:** `win_rate`, `average_score`, `conversion_rate`
* **Text:** `summary`, `message`, `report_text`
* **Status:** `processing_status`, `result_code`

***

**Last Updated:** 2025-10-01
