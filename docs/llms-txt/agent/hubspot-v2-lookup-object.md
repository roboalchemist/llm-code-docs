# Source: https://docs.agent.ai/actions/hubspot-v2-lookup-object.md

# Look up HubSpot Object

Get detailed information about a specific HubSpot record when you know its ID, email, or domain.

**Common uses:**

* Get full details for a contact after searching
* Look up a deal triggered by a webhook
* Find a contact by their email address
* Fetch company information by domain
* Retrieve specific record properties

**Action type:** `hubspot.v2.lookup_object`

***

## What This Does (The Simple Version)

Think of this like looking up someone in a phone book. If you know their name (or in our case, their email, domain, or ID), you can find their full listing with all their details.

**Real-world example:**

Your website has a "Check your deal status" form. A customer enters their email. You use this action to look up their contact record in HubSpot by that email, then show them information about their deals.

**Another example:**

Someone fills out a contact form and you get their email address. Instead of creating a duplicate contact, you look them up by email first. If they exist, you update their info. If not, you create a new contact.

**The key difference from Search:**

* **Search** is like asking "Show me all contacts who work at Acme Corp" (might get many results)
* **Lookup** is like asking "Show me the contact with email [john@acme.com](mailto:john@acme.com)" (gets one specific record)

***

## How It Works

This action retrieves a single HubSpot record using a unique identifier. Depending on the object type, you can look up records in different ways:

* **Contacts:** By Object ID or Email address
* **Companies:** By Object ID or Domain name
* **All other objects (Deals, Tickets, etc.):** By Object ID only

You provide the identifier (usually from a webhook, search result, or previous action), and HubSpot returns the properties you request for that record.

**Why different lookup methods?**

Because different identifiers make sense for different object types:

* For **contacts**, email is unique - every contact has one email
* For **companies**, domain is unique - every company has one website domain
* For **deals/tickets/etc.**, you need the HubSpot ID since they don't have unique external identifiers

***

## When to Use Lookup vs. Search

**Use Lookup when:**

* You have a specific unique identifier (ID, email, or domain)
* You need exactly one record
* A webhook sent you an email or ID
* You know exactly which record you want

**Use Search when:**

* You don't have a unique identifier
* You need to find records matching criteria (like "all deals in this stage")
* You might get multiple results
* You're filtering by properties other than ID/email/domain

**Common pattern:** Search finds multiple records → Loop through results → Look up each one for complete details

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Look up HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - Person records (can lookup by ID or Email)
* **Companies** - Organization records (can lookup by ID or Domain)
* **Deals** - Sales opportunities (lookup by ID only)
* **Tickets** - Support tickets (lookup by ID only)
* **Calls** - Call engagement records (lookup by ID only)
* **Emails** - Email engagement records (lookup by ID only)
* **Meetings** - Meeting records (lookup by ID only)
* **Notes** - Note records (lookup by ID only)
* **Tasks** - Task records (lookup by ID only)

**Click the card** for the type of record you're looking up.

### Step 2: Choose Lookup Method (Contacts & Companies Only)

**For Contacts, you'll see a dropdown to choose:**

* **Lookup by Object ID** - Use the HubSpot record ID (e.g., "12345")
* **Lookup by Email** - Use the contact's email address (e.g., "[john@acme.com](mailto:john@acme.com)")

**For Companies, you'll see a dropdown to choose:**

* **Lookup by Object ID** - Use the HubSpot record ID (e.g., "67890")
* **Lookup by Domain** - Use the company's domain (e.g., "acme.com")

**For all other object types:**

* Only Object ID is available (no dropdown shown)

**Which should you choose?**

**Use Object ID when:**

* You got the ID from a search result
* You're looping through search results
* A webhook sent you the specific HubSpot record ID
* You have the ID from a previous action

**Use Email (for Contacts) when:**

* You have the contact's email but not their ID
* A form submission sends the email address
* You're enriching data from an external source that only has emails
* Example: "Look up the contact who just submitted our form using email [sarah@company.com](mailto:sarah@company.com)"

**Use Domain (for Companies) when:**

* You have the company website but not the HubSpot ID
* You're enriching company data from external sources
* A form captures the company website
* Example: "Look up the company with domain acme.com"

### Step 3: Enter the Lookup Value

In the lookup field (labeled based on your method selection), provide the identifier.

**If looking up by Object ID:**

Click into the field—the `{}` insert variable icon appears. Click it to select:

* From a webhook: The ID variable sent by the trigger (e.g., `contact_id`, `deal_id`)
* From a search/loop: `current_contact` → `hs_object_id`
* From a previous action: The output variable → `hs_object_id`

**Example:** Webhook sends `deal_id` → Click `{}` → select `deal_id`

**If looking up by Email (Contacts only):**

Click into the field and use the `{}` button to select:

* From a webhook: The email variable (e.g., `email`, `submitted_email`)
* From a form: The form submission email field
* From a search/loop: `current_contact` → `email`

**Example:** Form webhook sends `submitted_email` with value "[sarah@company.com](mailto:sarah@company.com)" → Click `{}` → select `submitted_email`

**If looking up by Domain (Companies only):**

Click into the field and use the `{}` button to select:

* From a webhook: The domain variable
* From a form: The company website/domain field
* From enrichment data: External data source with domain

**Example:** Webhook sends `company_website` with value "acme.com" → Click `{}` → select `company_website`

**Important for domains:** Use just the domain without "www" or "https\://"

* ✅ Good: `acme.com`
* ❌ Bad: `www.acme.com` or `https://acme.com`

**You can also type values directly** (less common):

* Object ID: `12345`
* Email: `john@acme.com`
* Domain: `acme.com`

### Step 4: Choose Properties to Retrieve (Optional)

Click the **"+ Add Property"** button to select which HubSpot properties you want to get back.

**This opens the property picker modal:**

* Search bar at the top to find properties quickly
* List of all available properties for that object type
* Click properties to select them (checkmark appears)
* Click **Done** when finished

**If you don't add any properties:**
The action will return a default set of basic properties for that object type.

**Tips:**

* Only select properties you'll actually use
* Use the search bar to quickly find specific properties
* Always include `hs_object_id` if you'll reference or update the record later

**Example properties to select:**

For **Contacts:**

* `firstname`
* `lastname`
* `email`
* `phone`
* `company`
* `lifecyclestage`
* `hs_object_id`

For **Companies:**

* `name`
* `domain`
* `industry`
* `city`
* `state`
* `numberofemployees`
* `hs_object_id`

For **Deals:**

* `dealname`
* `dealstage`
* `amount`
* `closedate`
* `pipeline`
* `hubspot_owner_id`
* `hs_object_id`

### Step 5: Get Associated Objects (Optional)

Want to also retrieve IDs of related records? Type the object types in the "Associated Object Types" field, separated by commas.

**Examples:**

```
contacts,companies
```

Returns IDs of contacts and companies associated with this record.

```
deals
```

Returns IDs of deals associated with this contact/company.

**What you get back:**
Just the IDs of associated records (not their full details). You can then look up those IDs if needed.

**Leave blank if:**
You don't need related record IDs.

### Step 6: Name Your Output Variable

In the "Output Variable Name" field, give this record a descriptive name.

**Good names:**

* `contact_details`
* `deal_info`
* `company_data`
* `retrieved_ticket`
* `found_contact`

This is how you'll reference the record's properties in later actions.

***

## What You Get Back

You get a single object containing the properties you selected.

**Example 1:** Looking up a contact by email with properties `firstname`, `lastname`, `email`

**Output saved to `contact_details`:**

```
{
  "firstname": "Sarah",
  "lastname": "Johnson",
  "email": "sarah@company.com",
  "hs_object_id": "12345"
}
```

**Example 2:** Looking up a company by domain with properties `name`, `domain`, `industry`

**Output saved to `company_info`:**

```
{
  "name": "Acme Corp",
  "domain": "acme.com",
  "industry": "Technology",
  "hs_object_id": "67890"
}
```

**Example 3:** With associations included

If you requested associated `deals`:

```
{
  "firstname": "Sarah",
  "lastname": "Johnson",
  "email": "sarah@company.com",
  "hs_object_id": "12345",
  "associations": {
    "deals": ["11111", "22222"]
  }
}
```

***

## Using the Retrieved Data

### Access Properties in Next Actions

For any field that needs a value, click the `{}` insert variable icon:

1. Select your output variable (e.g., `contact_details`)
2. Select the property you want (e.g., `email`, `firstname`)

**Example - Sending an email:**

* **To:** Click `{}` → select `contact_details` → select `email`
* **Subject:** Type "Hi " then click `{}` → select `contact_details` → select `firstname`

**Result:** Email goes to "[sarah@company.com](mailto:sarah@company.com)" with subject "Hi Sarah"

### Check If Property Has a Value

Some properties might be empty in HubSpot. Use an **If Condition** action to check first:

1. **Add If Condition** after the lookup
2. **Condition:** Check if `contact_details` → `phone` exists or is not empty
3. **If true:** Do something with the phone number
4. **If false:** Handle the missing data differently

### Use Associated Object IDs

If you retrieved associations, you can loop through them:

1. **Add For Loop** action
2. **Loop through:** Click to select `contact_details` → `associations` → `companies`
3. **Current item:** Name it `company_id`
4. Inside the loop, look up each company using that ID

***

## Common Workflows

### Form Submission → Lookup Contact by Email

**Goal:** When someone submits a form, find their existing contact record using their email.

**Real-world scenario:** You have a "Request a Demo" form. When Sarah fills it out, you want to check if she's already in your CRM before creating a new contact.

**Trigger:** Webhook receives `email` variable from form

1. **Look up HubSpot Object (V2)**
   * Object Type: Contacts
   * Lookup Method: **Lookup by Email**
   * Email: Click `{}` → select `email`
   * Add Properties: Select `firstname`, `lastname`, `email`, `company`, `hs_object_id`
   * Output Variable: `found_contact`

2. **If Condition** - Check if contact was found
   * If found: Update their info using `found_contact` → `hs_object_id`
   * If not found: Create new contact

3. **Send confirmation email**
   * To: `found_contact` → `email`
   * Subject: "Hi " + `found_contact` → `firstname` + ", thanks for your interest!"

### Enrich Company Data by Domain

**Goal:** External tool sends you a company domain, and you want to enrich it with HubSpot data.

**Real-world scenario:** Your sales team uses a Chrome extension that captures company domains from LinkedIn. You want to look up those companies in HubSpot to see if you already have them.

**Trigger:** Webhook with `company_domain` variable

1. **Look up HubSpot Object (V2)**
   * Object Type: Companies
   * Lookup Method: **Lookup by Domain**
   * Domain: Click `{}` → select `company_domain`
   * Add Properties: Select `name`, `industry`, `numberofemployees`, `city`, `hs_object_id`
   * Output Variable: `company_info`

2. **If Condition** - Check if company exists
   * If found: Display `company_info` → `name` and `company_info` → `industry`
   * If not found: Create new company with that domain

### Webhook → Lookup Deal by ID → Send Update

**Goal:** When a deal reaches a certain stage in HubSpot, send an email to the deal owner.

**Real-world scenario:** Your HubSpot workflow triggers when deals move to "Contract Sent" stage. You want to email the owner with deal details.

**Trigger:** HubSpot workflow sends webhook with `deal_id`

1. **Look up HubSpot Object (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → select `deal_id`
   * Add Properties: Select `dealname`, `amount`, `dealstage`, `closedate`, `hubspot_owner_id`
   * Output Variable: `deal_details`

2. **Send Email**
   * To: Look up owner email using `deal_details` → `hubspot_owner_id`
   * Subject: "Contract sent for " + `deal_details` → `dealname`
   * Body: Include `deal_details` → `amount` and `deal_details` → `closedate`

### Search → Loop → Lookup Pattern

**Goal:** Find all contacts in a certain lifecycle stage, then get complete details for each.

**Real-world scenario:** You want to find all "Lead" contacts and send them a nurture email with personalized details.

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Filters: `lifecyclestage=lead`
   * Properties: Just get `hs_object_id` (basic info)
   * Output: `lead_contacts`

2. **For Loop**
   * Loop through: `lead_contacts`
   * Current item: `current_contact`

3. **Look up HubSpot Object (V2)** - inside loop
   * Object Type: Contacts
   * Lookup Method: Lookup by Object ID
   * Object ID: Click `{}` → select `current_contact` → `hs_object_id`
   * Add Properties: Select all the properties you need for the email
   * Output Variable: `full_contact`

4. **Send Email** - inside loop
   * To: `full_contact` → `email`
   * Personalized with their data

5. **End Loop**

***

## Real Examples

### Example 1: Form Submission with Email

**Scenario:** "Contact Us" form sends email address. Look up the contact to personalize the response.

**Webhook receives:** `submitted_email` = "[sarah@company.com](mailto:sarah@company.com)"

**Configuration:**

* **Object Type:** Contacts
* **Lookup Method:** Lookup by Email
* **Email:** Click `{}` → select `submitted_email`
* **Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `company`
  * `lifecyclestage`
  * `hs_object_id`
* **Output Variable:** `contact_info`

**What happens:**

* Action finds Sarah's contact record
* Returns: `{"firstname": "Sarah", "lastname": "Johnson", "email": "sarah@company.com", ...}`

**Next step:** Send email: "Hi Sarah, thanks for reaching out!"

### Example 2: Company Enrichment

**Scenario:** Sales rep enters a company domain in your tool. Get HubSpot company data.

**Variable:** `company_domain` = "acme.com"

**Configuration:**

* **Object Type:** Companies
* **Lookup Method:** Lookup by Domain
* **Domain:** Click `{}` → select `company_domain`
* **Properties:** Select `name`, `industry`, `numberofemployees`, `city`, `state`, `hs_object_id`
* **Associated Object Types:** `contacts` (get contact IDs at this company)
* **Output Variable:** `company_data`

**What happens:**

* Action finds Acme Corp company record
* Returns company details plus IDs of contacts at that company
* `company_data` → `associations` → `contacts` = \["123", "456", "789"]

**Next step:** Loop through contact IDs and email each person at the company

### Example 3: Deal Update Notification

**Scenario:** HubSpot workflow fires when deal stage changes to "Closed Won". Send celebration email to owner.

**Webhook receives:** `deal_id` = "12345"

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → select `deal_id`
* **Properties:** Select `dealname`, `dealstage`, `amount`, `closedate`, `hubspot_owner_id`
* **Output Variable:** `won_deal`

**What happens:**

* Retrieves: `{"dealname": "Acme Corp - Enterprise", "amount": "50000", ...}`

**Next step:**

* Email owner: "Congrats! " + `won_deal` → `dealname` + " closed for \$" + `won_deal` → `amount`

***

## Troubleshooting

### "Object not found" Error

**The record doesn't exist with that identifier**

**Possible causes:**

1. Wrong ID, email, or domain was provided
2. Record was deleted from HubSpot
3. Email/domain doesn't match exactly
4. Variable is empty or undefined

**How to fix:**

1. **Check the execution log** - See exactly what value was sent to the action
2. **Verify in HubSpot** - Does a record with that ID/email/domain actually exist?
3. **For email lookups:** Check for typos, extra spaces, or wrong capitalization
4. **For domain lookups:** Make sure it's just the domain (e.g., "acme.com" not "[https://www.acme.com](https://www.acme.com)")
5. **Add safety check:** Use an If Condition before the lookup to verify the variable has a value

**Example fix:**

```
If Condition: Check if {email} is not empty
  If true: Look up contact by email
  If false: Skip lookup or create new contact
```

### No Record Found by Email

**Looked up contact by email but got "not found"**

**Possible causes:**

1. Contact doesn't exist in HubSpot with that email
2. Email has typo or formatting issue
3. Email has extra whitespace

**How to fix:**

1. **Search HubSpot manually** - Does a contact with that email exist?
2. **Trim whitespace** - Strip spaces before/after the email
3. **Check format** - Emails should be lowercase typically
4. **Create if not found** - Use If Condition to create contact if lookup fails

**Pattern:**

```
1. Look up contact by email
2. If Condition: Check if contact was found
   - If found: Update contact
   - If not found: Create new contact
```

### No Company Found by Domain

**Looked up company by domain but got "not found"**

**Possible causes:**

1. Domain format is incorrect
2. Company doesn't exist in HubSpot
3. Domain includes "www" or "https\://" prefix
4. Domain has path or query parameters

**How to fix:**

1. **Use clean domain only:** Just `acme.com` (not `www.acme.com` or `https://acme.com/about`)
2. **Strip prefixes:** Remove "[www](http://www).", "http\://", "https\://"
3. **Remove paths:** Remove everything after the domain ("/about", "?page=1")
4. **Check HubSpot** - Verify the company exists with that exact domain

**Example:** If webhook sends `https://www.acme.com/products`

* Strip to just: `acme.com`
* Then do the lookup

### Properties Are Empty Even Though Record Found

**Record was found but specific properties are blank**

**Possible causes:**

1. Those properties are actually empty in HubSpot (not filled out)
2. Property names don't match exactly
3. Didn't select those properties in the property picker

**How to fix:**

1. **Check HubSpot record** - Open the actual record in HubSpot and see if those fields have values
2. **Use property picker** - Don't type property names, use the "+ Add Property" button
3. **Handle empty values** - Use If Condition to check if property has a value before using it

**Example:**

```
Look up contact by email
If Condition: Check if contact_details → phone is not empty
  - If has phone: Send SMS
  - If no phone: Send email instead
```

### "Missing OAuth Scope" Error

**Don't have permission to access that object type**

**How to fix:**

1. Go to **Settings → Integrations**
2. Find HubSpot and click **"Reconnect"**
3. Make sure you check the box for that object type's read permission
4. Save and try the workflow again

**Required permissions:**

* Contacts: "Read Contacts"
* Companies: "Read Companies"
* Deals: "Read Deals"
* Tickets: "Read Tickets"

***

## Tips & Best Practices

**✅ Do:**

* **Use Lookup by Email** for contacts when you only have the email (super common with forms!)
* **Use Lookup by Domain** for companies when enriching external data
* **Use the `{}` button** to insert variables instead of typing
* **Always handle "not found"** - Use If Condition to check if the lookup succeeded
* **Clean domains** - Strip "www" and "https\://" before looking up by domain
* **Use descriptive variable names** - `found_contact` is better than `c`
* **Include `hs_object_id`** in properties if you'll update/reference the record later

**❌ Don't:**

* Hard-code specific IDs, emails, or domains (they change between portals)
* Assume the record exists - always handle the not-found case
* Include URL prefixes in domain lookups ("[https://acme.com](https://acme.com)" won't work)
* Forget to select properties - you'll only get defaults
* Use the wrong lookup method (can't look up deals by email!)

**Performance tips:**

* Lookups are very fast - don't worry about using them in loops
* Lookup by email/domain is just as fast as by ID
* Only select properties you need (though lookup is fast regardless)
* If you're looking up many records, Search might be more efficient than individual lookups

***

## Lookup Methods Quick Reference

| Object Type   | Can Lookup By         |
| ------------- | --------------------- |
| **Contacts**  | Object ID, **Email**  |
| **Companies** | Object ID, **Domain** |
| **Deals**     | Object ID only        |
| **Tickets**   | Object ID only        |
| **Calls**     | Object ID only        |
| **Emails**    | Object ID only        |
| **Meetings**  | Object ID only        |
| **Notes**     | Object ID only        |
| **Tasks**     | Object ID only        |

**Bold** = Special lookup methods (beyond just ID)

***

## Related Actions

**Use with Lookup:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records before looking them up
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update the record after looking it up
* [Create HubSpot Object (V2)](./hubspot-v2-create-object) - Create record if lookup fails (common pattern!)
* [If Condition](./if_else) - Check if lookup succeeded
* [For Loop](./for_loop) - Loop through associated record IDs

**Related guides:**

* [Variable System](../builder/template-variables) - Using retrieved data in actions
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Getting IDs/emails from HubSpot workflows

***

**Last Updated:** 2025-10-01
