# Source: https://docs.agent.ai/actions/hubspot-v2-create-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create HubSpot Object

Create new contacts, deals, companies, and other HubSpot records from your workflows.

**Common uses:**

* Create contacts from form submissions
* Generate deals when opportunities arise
* Add companies from enrichment data
* Create tickets from customer requests

**Action type:** `hubspot.v2.create_object`

***

## What This Does (The Simple Version)

Think of this like adding a new contact to your phone. You choose what type of record to create (contact, company, deal, etc.), fill in the details, and save it to HubSpot.

**Real-world example:**
Someone fills out a "Request Demo" form on your website. You use this action to create a new contact in HubSpot with their name, email, company, and set their lifecycle stage to "Lead". You can even link them to an existing company record.

***

## How It Works

This action creates a brand new record in your HubSpot CRM. You choose:

1. **What type** of record to create (contact, deal, company, etc.)
2. **Which properties** to set
3. **What values** to use (typed values or variables from previous actions)

The new record is saved to a variable containing the HubSpot ID and all properties you set.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Create HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to create.

### Step 2: Add Properties

In the **"Contacts Object Properties"** section (or "Deals Object Properties", etc.), click the **"+ Add Property"** button to select which properties you want to set on the new record.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**After closing the modal**, you'll see individual input fields for each property you selected.

**For each property:**

* The field is labeled with the property name (e.g., "First Name", "Email", "Company Name")
* Type the value directly, OR
* Hover over the field to see the `{}` button, then click it to insert a variable

**Example - Creating a contact:**

1. Click "+ Add Property"
2. Select `firstname`, `lastname`, `email`, `company`, `lifecycle_stage`
3. Click Done
4. Now you see five fields:
   * **First Name**: Click `{}` → select `first_name` (from webhook)
   * **Last Name**: Click `{}` → select `last_name` (from webhook)
   * **Email**: Click `{}` → select `email` (from webhook)
   * **Company**: Click `{}` → select `company_name` (from webhook)
   * **Lifecycle Stage**: Type "lead"

**Required properties:**
Different object types require different properties. Common requirements:

* **Contacts:** Usually just `email` (but best to include `firstname` and `lastname` too)
* **Companies:** Usually just `name` or `domain`
* **Deals:** Usually `dealname` and `pipeline` and `dealstage`
* **Tickets:** Usually `subject` and `hs_pipeline` and `hs_pipeline_stage`

**Tips:**

* Use the property picker to see all available properties and avoid typos
* Click `{}` to insert variables from triggers or previous actions
* HubSpot will use default values for properties you don't set

### Step 3: Name Your Output Variable

Give the created record a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `created_contact`
* `new_deal`
* `new_ticket`
* `contact_record`

This variable contains the new record with its HubSpot ID and all properties.

***

## What You Get Back

The action returns the **complete created object** with all its properties, including the HubSpot-generated ID.

**Example:** If you created a contact with `firstname`, `lastname`, `email`:

**Output saved to `created_contact`:**

```
{
  "id": "67890",
  "properties": {
    "firstname": "Jane",
    "lastname": "Smith",
    "email": "jane@example.com",
    "createdate": "2025-10-01T14:30:00Z",
    "hs_object_id": "67890"
  },
  "createdAt": "2025-10-01T14:30:00Z",
  "archived": false
}
```

**The `id` field is the HubSpot Object ID** - save this if you need to update or reference this record later.

***

## Using the Results

### Access the New Record's ID

The most common use is getting the HubSpot ID to use in later actions:

**In any field that accepts variables:**

* Click the **Insert Variable** button (`{}` icon)
* Navigate to your output variable (e.g., `created_contact`)
* Select `id` or `properties` → `hs_object_id` (they're the same)

**Example:** Create a deal associated with the new contact

1. **Create HubSpot Object (V2)** - Create contact, output: `created_contact`
2. **Create HubSpot Object (V2)** - Create deal:
   * Set deal properties (dealname, dealstage, etc.)
   * In associations field: Type `contact:` then click `{}` → `created_contact` → `id`

### Access Other Properties

You can access any property from the created record:

* Click `{}` → `created_contact` → `properties` → `email`
* Click `{}` → `created_contact` → `properties` → `createdate`

### Check If Creation Succeeded

The creation either succeeds (returns the full record) or throws an error. If required properties are missing or credentials are wrong, the workflow stops with an error message.

***

## Common Workflows

### Create Contact from Form

**Goal:** When someone submits a form, create a contact in HubSpot

**Trigger:** Webhook from website form

**Webhook receives:** `first_name`, `last_name`, `email`, `company` variables

1. **Create HubSpot Object (V2)**
   * Object Type: Contacts
   * Properties: Click "+ Add Property" and select:
     * `firstname`: Click `{}` → select `first_name`
     * `lastname`: Click `{}` → select `last_name`
     * `email`: Click `{}` → select `email`
     * `company`: Click `{}` → select `company`
     * `lifecycle_stage`: Type "lead"
   * Output Variable: `created_contact`

2. **Send confirmation email** using `created_contact` data...

### Create Deal for New Contact

**Goal:** After creating a contact, automatically create a deal for them

1. **Create HubSpot Object (V2)** - Create contact
   * Object Type: Contacts
   * Properties: Set `firstname`, `lastname`, `email`
   * Output Variable: `new_contact`

2. **Create HubSpot Object (V2)** - Create deal
   * Object Type: Deals
   * Properties: Click "+ Add Property" and select:
     * `dealname`: Type "New Opportunity - " then click `{}` → `new_contact` → `properties` → `firstname`
     * `dealstage`: Type "appointmentscheduled"
     * `pipeline`: Type "default"
     * `amount`: Type "5000"
   * Output Variable: `new_deal`

3. **Associate them** (if needed) using Update or Association action...

### Create Company from Enrichment

**Goal:** Look up company data and create a company record

**Trigger:** Manual or webhook with company domain

1. **Enrich Company Data** (external API action)
   * Domain: `acme.com`
   * Output Variable: `company_data`

2. **Create HubSpot Object (V2)**
   * Object Type: Companies
   * Properties: Click "+ Add Property" and select:
     * `name`: Click `{}` → `company_data` → `name`
     * `domain`: Click `{}` → `company_data` → `domain`
     * `industry`: Click `{}` → `company_data` → `industry`
     * `numberofemployees`: Click `{}` → `company_data` → `employee_count`
   * Output Variable: `created_company`

***

## Real Examples

### Lead Capture Workflow

**Scenario:** Website visitor submits "Download Whitepaper" form, create contact and mark as MQL.

**Webhook receives:** `email`, `first_name`, `last_name`, `phone` variables

**Create Configuration:**

* **Object Type:** Contacts
* **Properties:** Click "+ Add Property" and select:
  * `email`: Click `{}` → select `email`
  * `firstname`: Click `{}` → select `first_name`
  * `lastname`: Click `{}` → select `last_name`
  * `phone`: Click `{}` → select `phone`
  * `lifecycle_stage`: "marketingqualifiedlead"
  * `lead_source`: "Whitepaper Download"
* **Output Variable:** `new_lead`

**Next steps:** Send whitepaper download link to `new_lead.properties.email`.

### New Deal from Opportunity

**Scenario:** Sales rep fills out "New Opportunity" form, create deal with their info.

**Webhook receives:** `deal_name`, `contact_email`, `amount`, `close_date` variables

**Create Configuration:**

* **Object Type:** Deals
* **Properties:** Click "+ Add Property" and select:
  * `dealname`: Click `{}` → select `deal_name`
  * `amount`: Click `{}` → select `amount`
  * `closedate`: Click `{}` → select `close_date`
  * `dealstage`: "qualifiedtobuy"
  * `pipeline`: "default"
  * `deal_source`: "Sales Generated"
* **Output Variable:** `new_deal`

**Next steps:** Look up contact by `contact_email` and associate with `new_deal`.

***

## Troubleshooting

### "Missing Required Property" Error

**Error:** "Property 'email' is required" or similar

**Possible causes:**

1. Required property not selected in property picker
2. Required property field left empty
3. Variable inserted but it has no value

**How to fix:**

1. Click "+ Add Property" and select all required properties for that object type
2. Fill in values for all required fields
3. Check that variables you inserted actually have values (check execution log)
4. For contacts: always include `email`
5. For companies: always include `name` or `domain`
6. For deals: always include `dealname`, `pipeline`, `dealstage`

### "Property Does Not Exist" Error

**Error:** "Property 'custom\_field' does not exist"

**Possible causes:**

1. Property name is misspelled
2. Property doesn't exist in your HubSpot account
3. Property exists but not for that object type

**How to fix:**

1. Always use the "+ Add Property" button (shows only valid properties)
2. Go to HubSpot → Settings → Properties to verify the property exists
3. Make sure you're creating the right object type for that property
4. Custom properties must be created in HubSpot first

### "Missing OAuth Scope" Error

**You don't have permission to create that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize **WRITE** access to that object type
4. Save and try creating again

**Required permissions by object:**

* **Contacts:** "Write Contacts"
* **Companies:** "Write Companies"
* **Deals:** "Write Deals"
* **Tickets:** "Write Tickets"

### Duplicate Records Created

**Multiple records created instead of one**

**Possible causes:**

1. Workflow running multiple times
2. No duplicate checking (HubSpot allows duplicate emails if not prevented)

**How to fix:**

1. Check trigger settings - is it triggering multiple times?
2. Before creating, use **Search HubSpot (V2)** to check if record exists:
   * Search by email (for contacts) or domain (for companies)
   * Use **If Condition** to only create if search returns empty
3. Enable duplicate prevention in HubSpot settings (contacts only)

***

## Tips & Best Practices

**✅ Do:**

* Always use the "+ Add Property" button to select from actual HubSpot properties
* Include all required properties for that object type
* Use descriptive `dealname`, `firstname`/`lastname`, or `name` values
* Set `lifecycle_stage` for contacts to track their journey
* Save the output variable to use the HubSpot ID later
* Test with one record before running in a loop

**❌ Don't:**

* Create contacts without email addresses (HubSpot requires it)
* Forget to set `pipeline` and `dealstage` for deals (required)
* Create duplicate records - search first if unsure
* Forget to check permissions (need WRITE access, not just READ)
* Set properties that don't exist in your HubSpot account

**Performance tips:**

* Creating records is fast (usually under 1 second)
* If creating many records in a loop, consider batching (100-500 at a time)
* Use variables from previous actions instead of hardcoded values

***

## Related Actions

**What to do next:**

* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update records you created
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Check if record exists before creating
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get full details on created record
* [If Condition](./if_else) - Only create if certain conditions are met

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in property values
* [HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup) - Getting write permissions

***

**Last Updated:** 2025-10-01
