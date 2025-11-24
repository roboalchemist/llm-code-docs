# Source: https://docs.agent.ai/builder/template-variables.md

# Template Variables

> Use the variable syntax and curly braces button to insert data from previous actions into your workflow

Use the \{\{variable}} syntax and `{}` button to insert data from previous actions into your workflow.

**Common uses:**

* Insert search results into AI prompts
* Use deal amount in update actions
* Reference contact email in conditions
* Access nested properties like `contact.properties.firstname`
* Build text with multiple variables

***

## What This Does (The Simple Version)

Think of variables like passing notes between actions. One action finds data (like a contact record) and saves it with a name. Later actions can reference that name to use the data.

**Real-world example:**
A search action finds deals and saves them as `target_deals`. A loop action references `target_deals` to process each one. Inside the loop, you reference `current_deal.properties.amount` to get each deal's amount.

***

## The `{}` Button

**The easiest way to insert variables:**

1. **Hover** over any input field
2. **`{}` button appears** on the right
3. **Click it** to open variable picker
4. **Select the variable** you want
5. **Variable is inserted** in correct syntax

**Where you'll see it:**

* All action input fields
* Condition fields
* Update value fields
* Prompt fields
* Email body fields

***

## Variable Syntax

### Basic Variable

**Format:** \{\{variable\_name}}

**Example:**

```
\{\{contact\_email\}}
\{\{deal\_amount\}}
\{\{search\_results\}}
```

### Accessing Properties

**Format:** \{\{variable.properties.property\_name}}

**Example:**

```
\{\{contact\_data.properties.email\}}
\{\{deal\_record.properties.amount\}}
\{\{company\_info.properties.domain\}}
```

### Accessing Nested Data

**Format:** \{\{variable.path.to.data}}

**Example:**

```
\{\{contact\_data.properties.firstname\}}
\{\{deal\_record.associations.contacts\}}
\{\{current\_item.id\}}
```

### Accessing Array Items

**Format:** \{\{variable\[0]}} (first item)

**Example:**

```
\{\{search\_results[0]\}}
\{\{contact\_data.associations.companies[0].id\}}
\{\{deals[0].properties.dealname\}}
```

***

## Common Patterns

### From Search Action

**After Search HubSpot (V2):**

**Output variable:** `target_deals`

**Access in later actions:**

* Whole list: \{\{target\_deals}}
* First deal: \{\{target\_deals\[0]}}
* First deal's name: \{\{target\_deals\[0].properties.dealname}}

### From Lookup Action

**After Lookup HubSpot Object (V2):**

**Output variable:** `contact_record`

**Access properties:**

* Email: \{\{contact\_record.properties.email}}
* First name: \{\{contact\_record.properties.firstname}}
* Company: \{\{contact\_record.properties.company}}
* Object ID: \{\{contact\_record.id}} or \{\{contact\_record.hs\_object\_id}}

### From Loop

**Inside For Loop:**

**Current item variable:** `current_deal`

**Access current item:**

* Whole object: \{\{current\_deal}}
* Deal name: \{\{current\_deal.properties.dealname}}
* Deal amount: \{\{current\_deal.properties.amount}}
* Object ID: \{\{current\_deal.hs\_object\_id}}

### From Webhook

**After webhook trigger:**

**Webhook variables available immediately:**

* \{\{contact\_id}}
* \{\{deal\_name}}
* \{\{\_hubspot\_portal}}
* Whatever you included in HubSpot webhook payload

### From Set Variable

**After Set Variable action:**

**Variable name:** `total_count`

**Access anywhere after:**

* \{\{total\_count}}

**Can use in:**

* Conditions: \{\{total\_count}} > 10
* Updates: Set property to \{\{total\_count}}
* Math: \{\{total\_count}} + 1

***

## Using Variables in Different Actions

### In Update Actions

**Update HubSpot Object (V2):**

1. Select property to update
2. In value field, hover and click `{}`
3. Select variable
4. Or mix text + variables: "Total: \$\{\{deal\_amount}}"

**Example:**

* Update `hs_lead_status` with: \{\{enrichment\_result}}
* Update `notes` with: "Score: \{\{lead\_score}} - Company: \{\{company\_name}}"

### In Conditions

**If Condition:**

1. Type condition naturally
2. Click `{}` to insert variables
3. AI evaluates the condition

**Example:**

```
\{\{deal\_record.properties.amount\}} > 50000
\{\{contact\_data.properties.email\}} is not empty
\{\{lifecycle\_stage\}} equals "salesqualifiedlead"
```

### In AI Prompts

**Invoke LLM:**

1. Type prompt text
2. Click `{}` to insert variables
3. AI receives the data

**Example:**

```
Analyze this deal: \{\{deal\_record\}}

Based on this timeline: \{\{deal\_timeline\}}

Provide insights about \{\{contact\_data.properties.firstname\}}'s engagement.
```

### In Loops

**For Loop:**

1. "Loop through" field: Click `{}` → select list variable
2. "Current item" field: Type name like `current_contact`

**Inside loop, access:**

* \{\{current\_contact.properties.email}}
* \{\{current\_contact.properties.firstname}}

### In Search Filters

**Search HubSpot (V2):**

1. Add filter
2. In value field: Click `{}`
3. Insert variable for dynamic search

**Example:**

* Find deals where `amount` Greater Than \{\{minimum\_threshold}}
* Find contacts where `company` Equals \{\{target\_company}}

***

## Real Examples

### Deal Analysis with Variables

**Step 1: Lookup Deal**

* Output Variable: `deal_data`

**Step 2: Get Timeline**

* Object ID: \{\{deal\_data.id}}
* Output Variable: `deal_timeline`

**Step 3: AI Analysis**

* Prompt: "Analyze deal \{\{deal\_data.properties.dealname}} with timeline \{\{deal\_timeline}}"
* Output Variable: `insights`

**Step 4: Update Deal**

* Update `deal_health_score` with: \{\{insights.health\_score}}

### Contact Enrichment with Variables

**Step 1: Webhook receives**

* Variables: `contact_id`, `contact_email`, `contact_company`

**Step 2: Lookup Contact**

* Object ID: `\{\{contact\_id\}\}`
* Output Variable: `contact_data`

**Step 3: Web Search**

* Query: "\{\{contact\_data.properties.company}} \{\{contact\_data.properties.jobtitle}}"
* Output Variable: `web_results`

**Step 4: AI Enrichment**

* Prompt: "Enrich \{\{contact\_data.properties.firstname}} from \{\{web\_results}}"
* Output Variable: `enrichment`

**Step 5: Update Contact**

* Update `hs_lead_status` with: `\{\{enrichment.lead\_category\}\}`

### Loop with Counter

**Step 1: Set Variable**

* Variable Name: `high_value_count`
* Value: `0`

**Step 2: For Loop**

* Loop through: \{\{all\_deals}}
* Current item: `current_deal`

**Step 3: If Condition (inside loop)**

* Condition: \{\{current\_deal.properties.amount}} > 100000

**Step 4: Set Variable (inside if)**

* Variable Name: `high_value_count`
* Value: \{\{high\_value\_count}} + 1

**Step 5: End Condition**

**Step 6: End Loop**

**After loop:** Use `\{\{high\_value\_count\}\}`

***

## Accessing Associations

**After Lookup with Associations:**

**Output variable:** `deal_data` (with contacts and companies retrieved)

**Access associated contact ID:**

```
\{\{deal\_data.associations.contacts[0].id\}\}
```

**Access associated company ID:**

```
\{\{deal\_data.associations.companies[0].id\}\}
```

**Use in another Lookup:**

* Object Type: Contacts
* Object ID: `\{\{deal\_data.associations.contacts[0].id\}\}`

***

## Troubleshooting

### Variable Not Found

**Can't select variable in `{}` picker**

**Possible causes:**

1. Variable not created yet (action hasn't run)
2. Variable only exists inside loop/if block
3. Action that creates it failed

**How to fix:**

1. Check action order - variable must be created before use
2. Create variable outside loop if needed after loop
3. Check execution log - did creating action succeed?

### Empty Value

**Variable exists but has no value**

**Possible causes:**

1. Previous action returned empty result
2. Property doesn't exist on object
3. Search/lookup found nothing

**How to fix:**

1. Check execution log - what did previous action return?
2. Verify property name is correct
3. Add If Condition to check if variable is empty first

### Wrong Syntax

**Variable doesn't insert correctly**

**Common mistakes:**

* ❌ `{variable}` (single braces)
* ❌ `\{\{variable.property\_name\}\}` (should be `properties.property_name`)
* ❌ `\{\{variable.0\}\}` (should be `variable[0]`)

**Correct:**

* ✅ \{\{variable}}
* ✅ \{\{variable.properties.property\_name}}
* ✅ \{\{variable\[0]}}

### Can't Access Nested Property

**Error accessing `contact.properties.email`**

**Possible causes:**

1. Using `.email` instead of `.properties.email`
2. Property doesn't exist on this object type
3. Property name wrong

**How to fix:**

1. HubSpot properties are always under `.properties.`
2. Check property exists: Look at object in execution log
3. Use exact internal property name (lowercase, no spaces)

***

## Tips & Best Practices

**✅ Do:**

* Use `{}` button instead of typing manually
* Use descriptive variable names (`contact_data` not `c`)
* Check execution log to see variable values
* Test with If Condition to check if variable exists
* Use variables to make workflows dynamic
* Access properties through `.properties.` for HubSpot objects

**❌ Don't:**

* Type `{{}}` manually (typo-prone)
* Assume variables always have values
* Use variables before they're created
* Reference loop variables outside the loop
* Forget `.properties.` when accessing HubSpot properties

**Common HubSpot property paths:**

* Contact email: `.properties.email`
* Contact name: `.properties.firstname` and `.properties.lastname`
* Deal amount: `.properties.amount`
* Deal stage: `.properties.dealstage`
* Company domain: `.properties.domain`
* Object ID: `.id` or `.hs_object_id`

***

## Related Actions

**Foundation:**

* [Variable System](../builder/template-variables) - How variables work
* [Action Execution](../builder/overview) - Variable scope and lifecycle

**Actions that create variables:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Creates list of results
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Creates object variable
* [Set Variable](../actions/set-variable) - Creates custom variables
* [For Loop](./for_loop) - Creates current item variable

**Actions that use variables:**

* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Insert in update values
* [If Condition](./if_else) - Use in conditions
* [Invoke LLM](./use_genai) - Insert in prompts

***

**Last Updated:** 2025-10-01
