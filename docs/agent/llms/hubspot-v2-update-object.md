# Source: https://docs.agent.ai/actions/hubspot-v2-update-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update HubSpot Object

Update contacts, deals, companies, and other HubSpot records with new information.

**Common uses:**

* Update deal stages when deals progress
* Change contact properties based on form submissions
* Update company information from webhook data
* Modify ticket status and priority

**Action type:** `hubspot.v2.update_object`

***

## What This Does (The Simple Version)

Think of this like editing a contact card in your phone. You find the person (by their name, email, or phone number), then update whatever details changed.

**Real-world example:**
A customer fills out a "Request Enterprise Demo" form. You use this action to find their contact record by email and update their `lifecycle_stage` to "Sales Qualified Lead" and set `demo_requested` to "Yes".

***

## How It Works

This action finds a HubSpot record and updates it with new property values. You choose:

1. **What type** of record to update (contact, deal, company, etc.)
2. **How to find it** (by ID, email, or domain)
3. **Which properties** to update
4. **What values** to set

The updated record is saved to a variable you can use in later actions.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Update HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to update.

### Step 2: Choose How to Find the Record

After selecting the object type, you'll see a **"Identify by"** dropdown with different lookup methods:

**For Contacts:**

* **Lookup by Object ID** - If you have the HubSpot ID
* **Lookup by Email** - Find by email address

**For Companies:**

* **Lookup by Object ID** - If you have the HubSpot ID
* **Lookup by Domain** - Find by company domain (e.g., "acme.com")

**For all other objects (Deals, Tickets, etc.):**

* **Lookup by Object ID** - Only option (must have the HubSpot ID)

**Choose your method** from the dropdown.

### Step 3: Enter the Identifier

In the **identifier field** below the dropdown, enter the value to find the record:

**Examples:**

* If you chose "Lookup by Email": Enter `jane@example.com` or click `{}` to insert an email variable
* If you chose "Lookup by Domain": Enter `acme.com` or click `{}` to insert a domain variable
* If you chose "Lookup by Object ID": Enter `12345` or click `{}` to insert an ID variable from a previous action

**Using variables:**
Click the `{}` button to insert a variable from previous actions. Common patterns:

* Email from webhook: Click `{}` → select `contact_email` (from your trigger)
* ID from search: Click `{}` → select `current_deal` → `hs_object_id` (from a loop)

### Step 4: Add Properties to Update

In the **"Update Contact Properties"** section (or "Update Deal Properties", etc.), click the **"+ Add Property"** button to select which properties you want to update.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**After closing the modal**, you'll see individual input fields for each property you selected.

**For each property:**

* The field is labeled with the property name (e.g., "Lifecycle Stage", "Deal Stage", "City")
* Type the new value directly, OR
* Hover over the field to see the `{}` button, then click it to insert a variable

**Example - Updating a contact:**

1. Click "+ Add Property"
2. Select `lifecycle_stage`, `deal_stage_requested`, `city`
3. Click Done
4. Now you see three fields:
   * **Lifecycle Stage**: Type "Sales Qualified Lead"
   * **Deal Stage Requested**: Type "Yes"
   * **City**: Click `{}` → select `form_city` (from webhook)

**Tips:**

* Only add properties you actually want to change (you don't need to include properties that aren't changing)
* Use the property picker to avoid typos
* Click `{}` to insert variables from triggers, previous actions, or loop items

### Step 5: Name Your Output Variable

Give the updated record a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `updated_contact`
* `updated_deal`
* `modified_ticket`
* `current_record`

This variable contains the full record with all its properties after the update.

***

## What You Get Back

The action returns the **complete updated object** with all its properties (not just the ones you changed).

**Example:** If you updated a contact's `lifecycle_stage` and selected properties `firstname`, `email`, `lifecycle_stage`:

**Output saved to `updated_contact`:**

```
{
  "id": "12345",
  "properties": {
    "firstname": "Jane",
    "email": "jane@example.com",
    "lifecycle_stage": "salesqualifiedlead"
  },
  "createdAt": "2025-01-15T10:30:00Z",
  "updatedAt": "2025-10-01T14:22:00Z"
}
```

**Note:** The full record is returned, but you control which properties are visible by what you selected in the property picker.

***

## Using the Results

### Access Updated Properties

After the update action, use the output variable to access the updated record:

**In any field that accepts variables:**

* Click the **Insert Variable** button (`{}` icon)
* Navigate to your output variable (e.g., `updated_contact`)
* Select the property you want (e.g., `id`, `properties` → `email`)

### In a Loop

If you're updating multiple records in a loop:

**Example workflow:**

1. **Search HubSpot (V2)** - Find contacts matching criteria, save to `contacts_to_update`
2. **For Loop** - Loop through `contacts_to_update`, current item: `current_contact`
3. **Update HubSpot Object (V2)** - Inside the loop:
   * Object Type: Contacts
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_contact` → `hs_object_id`
   * Update properties (e.g., set `last_contacted` to today)
   * Output Variable: `updated_contact`
4. **End Loop**

### Check If Update Succeeded

The update either succeeds (returns the full record) or throws an error. If the record isn't found or credentials are wrong, the workflow stops with an error message.

***

## Common Workflows

### Update from Form Submission

**Goal:** When someone fills out a form, update their contact record

**Trigger:** Webhook from HubSpot form

**Webhook receives:** `email`, `requested_demo` variables

1. **Update HubSpot Object (V2)**
   * Object Type: Contacts
   * Identify by: Lookup by Email
   * Identifier: Click `{}` → select `email` (from webhook)
   * Update Properties: Click "+ Add Property" and select:
     * `demo_requested`: Set to "Yes"
     * `lifecycle_stage`: Set to "Sales Qualified Lead"
   * Output Variable: `updated_contact`

2. **Send notification** or continue workflow\...

### Update Deal Stage in Loop

**Goal:** Move multiple deals to the next stage

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_progress`

2. **For Loop**
   * Loop through: `deals_to_progress`
   * Current item: `current_deal`

3. **Update HubSpot Object (V2)** - inside loop
   * Object Type: Deals
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_deal` → `hs_object_id`
   * Update Properties: Click "+ Add Property"
     * `dealstage`: Set to "decisionmakerboughtin"
   * Output Variable: `updated_deal`

4. **End Loop**

### Update Company by Domain

**Goal:** Update a company's information when you know their domain

**Trigger:** Manual or webhook with company domain

1. **Update HubSpot Object (V2)**
   * Object Type: Companies
   * Identify by: Lookup by Domain
   * Identifier: Type "acme.com" or click `{}` to insert domain variable
   * Update Properties: Click "+ Add Property"
     * `industry`: Set to "Technology"
     * `company_size`: Set to "500+"
   * Output Variable: `updated_company`

***

## Real Examples

### Contact Lifecycle Update

**Scenario:** When a contact downloads a whitepaper, update their lifecycle stage.

**Webhook receives:** `email` variable from form

**Update Configuration:**

* **Object Type:** Contacts
* **Identify by:** Lookup by Email
* **Identifier:** Click `{}` → select `email` (from webhook)
* **Update Properties:** Click "+ Add Property" and select:
  * `lifecycle_stage`: "marketingqualifiedlead"
  * `last_engagement_date`: Click `{}` → select `today` (system variable)
  * `content_downloads`: Click `{}` → select `download_count` (from previous action)
* **Output Variable:** `updated_contact`

**Next steps:** Send confirmation email using updated contact data.

### Deal Amount Update

**Scenario:** When a deal reaches "Contract Sent" stage, update the expected close date.

**Trigger:** Manual or scheduled

**Update Configuration:**

* **Object Type:** Deals
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → select `deal_id` (from search or webhook)
* **Update Properties:** Click "+ Add Property" and select:
  * `closedate`: Click `{}` → select `thirty_days_from_now` (calculated variable)
  * `dealstage`: "contractsent"
* **Output Variable:** `updated_deal`

***

## Troubleshooting

### Record Not Found

**Error:** "Object not found" or "No record with that email/domain"

**Possible causes:**

1. The email/domain/ID doesn't exist in HubSpot
2. Typo in the identifier value
3. Using wrong identification method

**How to fix:**

1. Check HubSpot manually - does the record exist?
2. Verify the identifier value (email is case-insensitive, but check for typos)
3. For email lookup, make sure you selected "Contacts" (not Companies or Deals)
4. For domain lookup, make sure you selected "Companies" (not Contacts)
5. Check the execution log to see the exact value that was used

### "Missing OAuth Scope" Error

**You don't have permission to update that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize **WRITE** access to that object type
4. Save and try the update again

**Required permissions by object:**

* **Contacts:** "Write Contacts" (not just "Read Contacts")
* **Companies:** "Write Companies"
* **Deals:** "Write Deals"
* **Tickets:** "Write Tickets"

### Properties Not Updating

**The action succeeds but properties don't change**

**Possible causes:**

1. Property name is misspelled
2. Property value format is wrong (e.g., date format)
3. Property is read-only in HubSpot
4. Property doesn't exist for that object type

**How to fix:**

1. Use the "+ Add Property" button to select from actual HubSpot properties (avoids typos)
2. Check HubSpot → Settings → Properties to see valid values for that property
3. Look at a HubSpot record to see the expected format (dates, picklists, etc.)
4. Try updating the property manually in HubSpot to verify it's editable
5. Check the execution log - the response shows which properties were actually updated

### No Properties Selected

**Error:** "At least one property is required to update an object"

**How to fix:**

1. Click the "+ Add Property" button
2. Select at least one property to update
3. Enter a value for that property
4. Make sure you clicked "Done" in the property picker modal

***

## Tips & Best Practices

**✅ Do:**

* Use the "+ Add Property" button to browse and select from your actual HubSpot properties
* Use "Lookup by Email" for contacts when you have their email (more reliable than searching)
* Use "Lookup by Domain" for companies when you know the domain
* Always use `hs_object_id` when you have it (fastest, most reliable)
* Test with a single record before running in a loop on hundreds of records
* Use descriptive output variable names

**❌ Don't:**

* Try to update properties that don't exist for that object type
* Forget to check permissions (need WRITE access, not just READ)
* Assume email/domain lookup works for all object types (Contacts/Companies only)
* Update properties that are managed by HubSpot workflows (may get overwritten)

**Performance tips:**

* Updating by Object ID is fastest (no extra lookup required)
* Only update properties that actually changed (don't update everything)
* If updating many records, use a loop with reasonable batch sizes (100-500)

***

## Related Actions

**What to do next:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records to update
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get record details before updating
* [For Loop](./for_loop) - Update multiple records one by one
* [If Condition](./if_else) - Conditionally update based on property values

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in update values
* [HubSpot Setup](../user/integrations) - Getting write permissions

***

**Last Updated:** 2025-10-01
