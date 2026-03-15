# Source: https://docs.firehydrant.com/docs/servicenow-business-rules.md

# ServiceNow Business Rules

> ℹ️ Need to install in the ServiceNow integration?
>
> [Learn how](https://docs.firehydrant.com/docs/servicenow-copy).

## Setting Up ServiceNow Business Rules for FireHydrant Integration

Business rules in ServiceNow automate actions based on database operations (create, update, delete). In this case, we're using business rules to automatically sync ServiceNow incidents with FireHydrant, which:

* Eliminates manual double-entry of incident data
* Ensures your incidents in FireHydrant stay in sync with ServiceNow
* Allows teams to work in their preferred tool while maintaining data consistency
* Automates communication between systems based on specific conditions you define

> 📘 Note:
>
> You can technically create separate Business Rules for creating vs. updating FireHydrant incidents from ServiceNow activity if desired.
>
> Both Rules would share all the same settings except for **Name** (highly suggest different rule names to differentiate, **When to run** (one would be only **Insert** checked, the other **Update** checked), and any **Filter conditions** you configure differently for each. Both Rules should be able to use the same code.

## Business Rule: Create/update FireHydrant Incidents

1. Navigate to System Definition > Business Rules
2. Click "New" to create a business rule
3. Configure the following settings in your business rule:
   1. **Name**: Anything is fine as long as it clarifies what the rule does. We recommend something like `FireHydrant - Create/Update Incidents`
   2. **Table**: `Incident [incident]` (or custom table, if you want to link other tables to FireHydrant incidents)
   3. **Active**: ✓
   4. **Advanced**:  ✓
   5. **When to run** tab:
      1. **When**: `after`
      2. **Order**: Default `100` should be fine, but this depends on how you have SNOW business rules configured
      3. **Insert**: ✓
      4. **Update**: ✓
      5. **Delete**: *(unchecked)*
      6. **Query**: *(unchecked)*
   6. **Filter Conditions** *(optional)*
      1. Add any specific conditions you'd like for creating FireHydrant incidents from SNOW records
      2. **Example**: Priority is Critical, or Category equals Production Issue, etc.
   7. **Advanced** tab: Copy the following code below into the **Script** portion of the Advanced tab.
      1. `fhWebhookUrl`: Remember to insert the webhook to FireHydrant on line 4. You can find this in FireHydrant in **Settings** > **Integration list** > **ServiceNow** > **Webhook URL**.
      2. `syncedFields`: List the ServiceNow ticket fields you want to sync with FireHydrant. Modify this array to match your field mapping configuration

> 📘 Note:
>
> Ensure your field names in `syncedFields` match those configured in your FireHydrant field mapping settings.

### Script

```javascript
(function executeRule(current, previous) {
    var fhWebhookUrl = 'Enter the webhook URL from your FireHydrant ServiceNow integration settings';

	var request = new sn_ws.RESTMessageV2();
	request.setEndpoint(fhWebhookUrl);
    request.setHttpMethod('POST');

	var requestBody = {};
	
	Object.keys(current).forEach(function (field) {
		requestBody[field] = current.getValue(field);
	});

	// FH Required fields Do Not Remove!!
	requestBody['sys_id'] = current.getValue('sys_id');
	requestBody['number'] = current.getValue('number');
	requestBody['state'] = current.getValue('state');
	requestBody['sn_user'] = gs.getUserName();
	requestBody['sn_user_email'] = gs.getUser().getEmail();
	requestBody['sn_table'] = current.getTableName();
	requestBody['fh_type'] = 'ticket';

    request.setRequestHeader('Accept', 'application/json');
    request.setRequestHeader('Content-Type', 'application/json');
	request.setRequestBody(JSON.stringify(requestBody));
	gs.info("FireHydrant - Request body: {0}", JSON.stringify(requestBody));

    var response = request.execute();
	if (response.getStatusCode() !== 200) {
		gs.info("FireHydrant - {0}: {1}", response.getStatusCode(), response.getBody());
	}
})(current, previous);
```

<div style={{ backgroundColor: "#018FF4" }} id="68635bc239a60b00116b3c81">
  🦉<a href="https://docs.firehydrant.com/v1.2.0/recipes/servicenow-business-rule" slug="servicenow-business-rule" title="ServiceNow Business Rule">ServiceNow Business Rule</a>
</div>

## Business Rule: Add work notes to Firehydrant incident

When managing incidents across ServiceNow and FireHydrant, keeping communication in sync between platforms is crucial for effective incident response. By setting up a business rule to sync ServiceNow work notes to FireHydrant, you ensure that all team updates, progress notes, and important communications are automatically shared between systems. This eliminates the need for manual copy-pasting, reduces the risk of missed updates, and allows team members to collaborate effectively regardless of which platform they're using. Support teams can continue working in ServiceNow while incident responders track progress in FireHydrant, maintaining a single source of truth for incident communications.

1. Navigate to System Definition > Business Rules
2. Click "New" to create a business rule
3. Configure the following items in the business rule:
   1. **Name**: Pick a name that clarifies what it's doing. We recommend something like `FireHydrant - Work Notes` or something similar
   2. **Table**: `Journal Entry [sys_journal_field]`
   3. **Active**: ✓
   4. **Advanced**: ✓
   5. **When to run** tab:
      1. **When**: `after`
      2. **Order**: Default `100` should be fine, but this depends on how you have SNOW business rules configured
      3. **Insert**: ✓
      4. **Update**: *(unchecked)*
      5. **Delete**: *(unchecked)*
      6. **Query**: *(unchecked)*
      7. **Filter Conditions**
         1. `Element` `is` `work_notes`
         2. `Name` `is` `incident`
         3. Any other conditions you want to filter/add
   6. **Advanced** tab: Copy the code block below into the Script on the Advanced tab.
      1. `fhWebhookUrl`: Remember to insert the webhook to FireHydrant on line 4. You can find this in FireHydrant in **Settings** > **Integration list** > **ServiceNow** > **Webhook URL**.

### Script

```javascript
(function executeRule(current, previous /*null when async*/ ) {
  try {
    var fireHydrantPrefix = "FireHydrant WorkNotes - ";
    var fhWebhookUrl = 'Enter the webhook URL from your FireHydrant ServiceNow integration settings';
    // Prepare the payload
    var payload = {
      fh_type: "generic_chat_message",
      sn_user: gs.getUser().getEmail(),
      parent_sys_id: current.getValue("element_id"),
      value: current.getValue("value"),
      table: current.getValue("name")
    };

    // Prepare request
    var request = new sn_ws.RESTMessageV2();
    request.setEndpoint(fhWebhookUrl);
    request.setHttpMethod('POST');
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestBody(JSON.stringify(payload));

    var response = request.execute();
    gs.info(fireHydrantPrefix + "Request sent, status code: " + response.getStatusCode());
    if (response.getStatusCode() !== 200) {
      gs.info(fireHydrantPrefix + "Bad request: {0}", response.getBody());
    }
  } catch (ex) {
    gs.error('Error in Work Note Notification Business Rule: ' + ex.message);
  }
})(current, previous);
```

<div style={{ backgroundColor: "#018FF4" }} id="68635bc239a60b00116b3c82">
  🦉<a href="https://docs.firehydrant.com/v1.2.0/recipes/servicenow-business-rule-for-work-notes" slug="servicenow-business-rule-for-work-notes" title="ServiceNow Business Rule for Work Notes">ServiceNow Business Rule for Work Notes</a>
</div>