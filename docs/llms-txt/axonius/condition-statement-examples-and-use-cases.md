# Source: https://docs.axonius.com/docs/condition-statement-examples-and-use-cases.md

# Dynamic Value Statement Examples and Use Cases

## Tips for creating dynamic value statements (also referred to as "statements")

* Autocomplete and [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) show available options for action fields, operators, and functions.
* A list of exact names of both adapter fields and action fields, as well as their field types, is available from the Syntax Helper and [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard).
* Data from assets can be manipulated using functions. Multiple functions can be used when nested.
* When you create an Axonius custom field, the field name in the database is different depending on its type. For example, `form.field_date.specific` for type date and `form.field_number` for float. Use the Syntax Helper to select the correct field type.
* Our syntax (parser) is Lark based. To learn more, click [here](https://open.larksuite.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/get).

## Examples

Following are some examples of how statements can be used.

Learn more [useful tips and tricks for working with dynamic value statements](/docs/useful-tips-and-tricks).

### Example 1

**Enforcement Action used:** **[ServiceNow - Create Incident](/docs/create-servicenow-incident)** Action in the Category **Create Incident or Ticket**.

**Description**
This user wants each response team to get only the incidents related to them.
Each incident is tagged (in `device.labels`) with the name of the team.
In this example, this tag value is used to determine the value of the assignment group written on the Action Form.

* If the tag contains the string `Team:X`, the Action Field (`form.assignment_group`) on the Action Form is filled with the value `Team X ID`.
* If the tag contains the string `Team:Y`, the Action Field (`form.assignment_group`) on the Action Form is filled with the value `Team Y ID`.

After the Action Forms are filled, the tickets are distributed to the relevant response teams, according to the assignment group on the form. This allows them to streamline their process and save time as each response team gets only the tickets related to them.

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  Tags are called 'labels' in the adapters.
</Callout>

```text
switch device.labels 
case contains ("Team: X") then form.assignment_group set_value "Team X ID"
case contains ("Team: Y") then form.assignment_group set_value "Team Y ID"
```

### Example 2

**Enforcement Action used:** Any enforcement action in the **[Create Incident or Ticket](/docs/create-incident)** category that create tickets in supported ticketing systems.

**Description**
Axonius Exposures can detect known vulnerabilities (Aggregated Security Findings) on assets. Having a list of vulnerabilities in an incident ticket can speed the mitigation process.
This user decided to write a statement that does the following for each device:

* Converts the list of critical vulnerabilities found on the device to a string of vulnerabilities separated by a delimiter (in this example, a space followed by a comma ` ,`).
* Concatenates the joined string of critical vulnerabilities to the string `' critical vulnerabilities.'`
* Places the resulting concatenated string (`vulnerability1, vulnerability2, vulnerability3, vulnerability4 critical vulnerabilities.`) in the Incident Description field (`form.incident_description`) of the ticket.

```text
device all then form.incident_description set_value
concat (join ([device.adapters_data.rapid7_insightvm_adapter.critical_vulnerabilities], " ,")," critical vulnerabilities.")	
```

### Example 3

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** Action from the **Axonius Utilities** category.

**Description**
The worded description of the Rapid7 tag (`device.adapters_data.rapid7_criticality_tag`) includes a vulnerability level. As a number valued score makes it easier to quickly evaluate the vulnerability level of an asset, this user decided to create a custom field of type *integer* (`form.field_integer`) with a default value of 100.

* If the Rapid7 tag starts with the word 'low', the field is assigned a numerical value of 30.
* If the Rapid7 tag starts with the word 'medium', the field is assigned a numerical value of 60.

Now that there is a number value, instead of a word inside a description, it is possible to make quicker decisions on which vulnerabilities to work on first.

```text
switch [device.adapters_data.rapid7_criticality_tag] 
case starts_with ("high") then form.field_integer set_value 100 
case starts_with ("medium") then form.field_integer set_value 60 
case starts_with ("low") then form.field_integer set_value 30
```

### Example 4

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** Action from the **Axonius Utilities** category.

**Description**
Number values can often have more meaning than other types of measurements. This user wants to use a number value to indicate whether this asset possibly has one or more CVEs related to it. They wrote a statement that creates a custom field of type integer that represents a number-value score based on the Boolean value of the exploit field.

* Checks the Boolean value of the exploit field **device.adapters\_data.nexpose\_adapter.software\_cves.is\_exploit**.

  * If the Boolean value is 'true', a numeric score of 100 is written into the new `device.vulnerabilities_score` custom field.
  * If the Boolean value is 'false', a numeric score of 10 is written into the new `device.vulnerabilities_score` custom field.

```text
switch device.adapters_data.nexpose_adapter.software_cves.is_exploit
case field_equal (true) then device.vulnerabilities_score set_value 100
case field_equal (false) then device.vulnerabilities_score set_value 10
```

### Example 5

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** Action from the **Axonius Utilities** category.

**Description**
Creates a custom field of type float that represents a weighted score of five other custom fields.
This statement does the following for each device:

* Multiplies the value in each custom risk field (`device.custom.riskn`) by a percentage, giving a weighted risk score to each of the five risk fields.
* Adds the five weighted risk scores, and sets the value of **form.field\_number** to that sum.

```text
device all then form.field_number set_value add 
(multiply ([device.custom.risk1], 0.2), multiply ([device.custom.risk2], 0.3), multiply ([device.custom.risk3], 0.05), multiply ([device.custom.risk4], 0.2), multiply ([device.custom.risk5], 0.25))
```

### Example 6

**Enforcement Action used:** [**Axonius - Send Email**](/docs/send-email)

**Description**
Sends an email to recipients based on the value of the hostname. It aggregates all identical hostnames into a single email. The number of email messages is equal to the number of unique hostname values. As hostname is a list of values (array), 'contains' is true only if all values in the list are an exact match.
The values in the hostname list (**device.specific\_data.data.hostname**) determine the email recipient, as follows:

* Hostname values include 'xdept' sets the form email recipient field to `manager1@company.com`.
* Hostname values include 'ydept' sets the form email recipient field to `manager2@company.com`.

```text
switch device.specific_data.data.hostname 
case contains ("xdept") then form.emailList set_value "manager1@company.com"
case contains ("ydept") then form.emailList set_value "manager2@company.com"	
```

### Example 7

**Enforcement Action used:** [**Axonius - Send Email**](/docs/send-email)

**Description**
Sends an email to recipients based on the value of the asset name (name). It aggregates all identical asset names into a single email. The number of email messages is equal to the number of unique asset name values. As asset name is a single value field, 'contains' is true even if part of the asset name matches.

The value in the asset name (**device.specific\_data.data.name**) determines the email recipient, as follows:

* Asset name value includes 'xdept' sets the form email recipient field to `manager1@company.com`.
* Asset name value includes 'ydept' sets the form email recipient field to `manager2@company.com`.

```text
switch device.specific_data.data.name 
case contains ("xdept") then form.emailList set_value "manager1@company.com" 
case contains ("ydept") then form.emailList set_value "manager2@company.com" 
```

### Example 8

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)**

**Description**
For each asset, creates a custom field **form.field\_number** that contains the highest CVSS score recorded for that asset in the list field **device.specific\_data.data.software\_cves.cvss**.

```text
device all then form.field_number set_value max([device.specific_data.data.software_cves.cvss])
```

### Example 9

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)**

**Description**
Creates a custom field of type Date (`form.field_date.specific`) and sets its value to 20 November 2022 for all devices returned by the query.

```text
device all then form.field_date.specific set_value "20/11/22"
```

### Example 10

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)**

**Description**
Creates a custom field of type date (`form.field_date.specific`). Inserts in it the date and time from last\_seen in the CrowdStrike adapter, or, if empty, from Cisco Meraki, or if empty from AWS. If all three adapters are empty, the value falls back to the static value provided in the Action form field.

```text
device all then form.field_date.specific set_value 
[device.adapters_data.crowd_strike_adapter.last_seen] or 
[device.adapters_data.cisco_meraki_adapter.last_seen] or 
[device.adapters_data.aws_adapter.last_seen] 
```

### Example 11

**Enforcement Action used:** [**Axonius - Send Email**](/docs/send-email)

**Description**
For each device in my saved query, prepare an email for the device owner with specific information on the device that is out of compliance and steps for remediation.
Concatenate the following text and device field values to create the email content:

* The introductory text (string) of the email (`'We've noticed...secure updates can be installed:'`)
* Device manufacturer
* Device model
* `'laptop named'` followed by the device hostname
* `'Serial#'` followed by the device serial number
* Closing words to the email from the Axonius Help Desk (`'If you have any questions...Axonius Help Desk'`).

```text
device all then form.mail_content
set_value concat(
"We've noticed that your Axonius issued laptop has been out of compliance. Your action is necessary to ensure that your device is secure and you have a smooth experience the next time you use it to access firm applications.

 **Please leave the following machine plugged-in, powered on, and connected to the internet overnight so that secure updates can be installed:***",
[device.specific_data.data.device_manufacturer_preferred], 
" ",
[device.specific_data.data.device_model_preferred],
" laptop named ",
[device.specific_data.data.hostname_preferred],
" (Serial#",
[device.specific_data.data.serial_number_preferred],
")* 

If you have any questions, no longer have this laptop or no longer need this laptop, please reply to this email.

Thank you!

HelpDesk
*Axonius Help Desk*")
```

### Example 12

**Enforcement Action used:**  Any

**Description**
Determine through which node to deploy a file based on the prefix of the asset name.
If the asset name (`device.specific_data.data.name`) begins with:
pro - Set `form.instance` to 'pro-axonctlr1'
dev - Set `form.instance` to 'dev-axonctlr1'
tes - Set `form.instance` to 'tes-axonctlr1'

```text
switch device.specific_data.data.name 
case starts_with ("pro") then form.instance set_value "pro-axonctlr1" 
case starts_with ("dev") then form.instance set_value "dev-axonctlr1" 
case starts_with ("tes") then form.instance set_value "tes-axoncltr1"
```

### Example 13

**Enforcement Action used:** [**Axonius - Add Tag to Assets**](/docs/add-remove-tag)

**Description**
For each asset, the following statement compares the values of its two custom fields **intest** and **intest2**, both of type Integer. If the value of **intest** is greater than the value of **intest2**, the value of the tag name field (`form.tag_name`) is set to 'success'.

```text
switch device.adapters_data.gui.custom_intest
case gt ([device.adapters_data.gui.custom_intest2]) then form.tag_name set_value "success"
```

### Example 14

**Enforcement Action used:** [**Jira Service Management - Create Ticket per Asset**](/docs/create-jira-service-desk-incident-per-entity)

**Description**
For each device in my saved query, open a ticket and set its **Ticket description** to a concatenation of the following strings and field values.

* `'This computer is out of compliance. Please make sure all security agents are installed: '`
* Preferred Device Manufacturer name followed by a space
* Preferred Device Model name
* `'Hostname '` followed by the Preferred Hostname (FQDN)
* `'Serial#'` followed by the Preferred Serial Number
* `'IP Address: '` followed by the Preferred IPv4 address.
* `'MAC Address: '` followed by the Preferred MAC Address.
* `'If you have any questions, no longer have this laptop, or no longer need this laptop, please reply to this email. Thank you! Axonius Help Desk'.`

The output is displayed in the Ticket description of each ticket.

```text
device all then form.incident_description
set_value concat(
"This computer is out of compliance. Please make sure all security agents are installed: ",
[device.specific_data.data.device_manufacturer_preferred], 
" ",
[device.specific_data.data.device_model_preferred],
" Hostname ",
[device.specific_data.data.hostname_fqdn_preferred],
" Serial#",
[device.specific_data.data.serial_number_preferred],
" IP Address:",
[device.specific_data.data.network_interfaces.ips_v4_preferred],
" MAC Address:",
[device.specific_data.data.network_interfaces.mac_preferred],
"If you have any questions, no longer have this laptop or no longer need this laptop, please reply to this email. Thank you! Axonius Help Desk")
```

### Example 15

**Enforcement Action used:** [**Jira Service Management - Create Ticket per Asset**](/docs/create-jira-service-desk-incident-per-entity)

**Description**
This example demonstrates how to automatically create a Jira ticket for each device resulting from a saved query. The **ticket description** will include key asset information, formatted for readability using the following conventions:

* `_ text/field_` italicizes the enclosed text/field.
* `＊text＊` boldens the field value following the enclosed text.
* `\n` inserts a line break (carriage return).

For each device, the **Ticket description** field will be populated by concatenating (joining) the following static text and dynamic asset field value:

* '\`*This computer is out of compliance. Please make sure all security agents are installed.* \n'
* '`IP Address:＊`' followed by the device's Preferred IPv4 address.
* '`MAC Address:＊`' followed by the device's Preferred MAC Address.
* '`\nIf you have any questions, no longer have this laptop, or no longer need this laptop, please reply to this email. Thank you!\n _Axonius Help Desk _`'.

```text
device all then form.incident_description
set_value concat("_This computer is out of compliance. Please make sure all security agents are installed._ \n",
"IP Address:*",
[device.specific_data.data.network_interfaces.ips_v4_preferred],
"*\nMAC Address:*",
[device.specific_data.data.network_interfaces.mac_preferred],
"*\nIf you have any questions, no longer have this laptop or no longer need this laptop, please reply to this email. Thank you! \n_Axonius Help Desk_")
```

The following shows an example of the output displayed in the Ticket description.

<Image alt="StatementExampleOutput" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/StatementExampleOutput.png" />

### Example 16

**Enforcement Action used:** [**Axonius - Add Tag to Assets**](/docs/add-remove-tag)

**Description**
For all devices with name (`device.specific_data.data.name`) containing `TEAM1`, set the tag name to the email value (`device.adapters_data.gui.custom_team1_email`) if it exists on the device. If it doesn`t exist, set the tag name to the owner value (`device.adapters\_data.gui.custom\_team1\_owner\`) if it exists on the device.
If both those values don't exist on the device, set the tag name to 'TEAM1'.

```text
switch [device.specific_data.data.name]
case contains("TEAM1") then form.tag_name set_value  [device.adapters_data.gui.custom_team1_email] or [device.adapters_data.gui.custom_team1_owner] or "TEAM1"
```

### Example 17

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)**

**Description**
This statement fills in both action fields (custom fields) **Field name** (`form.field_name`) and **Field value** (`form.field_number`) at once, according to the preferred hostname (`device.specific_data.data.hostname_preferred`) value, provided that it exists in the returned query results:

* If the preferred hostname contains 'a', set 'Field name' to 'a' and 'Field value' to '1'.
* If the preferred hostname contains 'b', set 'Field name' to 'b' and 'Field value' to '2'.
* If the preferred hostname contains 'c', set 'Field name' to 'c' and 'Field value' to '3'.

```text
switch [device.specific_data.data.hostname_preferred]
case contains ("a") then form.field_name set_value "a" also form.field_number set_value 1
case contains ("b") then form.field_name set_value "b" also form.field_number set_value 2
case contains ("c") then form.field_name set_value "c" also form.field_number set_value 3
```

### Example 18

**Based on Predefined Enforcement Set:** **[Calculate combined Risk Score per device with multiple criteria](/docs/using-predefined-enforcement-sets)** runs five **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** actions, where each action calculates a different custom field. Following these precalculations, the final **[Axonius - Calculate Risk Score](/docs/risk-score)** action calculates the risk score per device based on these five custom fields and Axonius fields (**Total CVE Count**, **Total Critical CVE Count**, and **Total High CVE Count**), each with a defined weight percentage.

**Description**
In this example, you create an Enforcement Set based on the predefined Enforcement Set and change how to calculate the value of the **Axonius\_epp** custom field in the second Post Action score **by epp**.

You begin by opening the predefined template, typing a meaningful **Enforcement Set name** and optionally a **Description**, defining the assets and query on which to run the Enforcement Set (**Run this Enforcement Set on assets matching the following query**), and then clicking **Save as New**. This creates a new Enforcement Set in the Shared Enforcement Sets folder with all the Enforcement Action definitions as in the predefined set.

<Image alt="EPP_PostAction" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EPP_PostAction.png" />

You can then open the second Post Action **score by epp** (open in the above screen), and modify its Dynamic Value statement to the below.

```text
switch device.specific_data.data.adapter_properties
case contains ("Endpoint_Protection_Platform") then form.field_number set_value "0"
```

For each asset, this statement sets the custom field **Axonius\_epp** to **0** if any of the adapter properties (**device.specific\_data.data.adapter\_properties** list field) contains the string 'Endpoint\_Protection\_Platform'. Otherwise, the value of the custom field **Axonius\_epp** is set to **100**, as defined by the default **Field value**.

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  You can remove precalculations defined by the other **Axonius - Add Custom Data to Assets** actions, if they are not relevant to the risk score calculation, and also remove those fields from the final **Calculate Risk Score** action.

  You can open the final post action **Axonius - Calculate Risk Score** that includes in its calculation the five custom fields calculated in the previous five actions, as well as the three Axonius fields on the device assets: **Total CVE Count**, **Total Critical CVE Count**, and **Total High CVE Count**. You can change the **Weight %** of these fields, provided that they add up to 100%. When done, you click **Save and Run** to calculate and add the calculated risk score to each device that matches the query.

  <Image alt="CalcCombinedRiskScore" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CalcCombinedRiskScore.png" />
</Callout>

### Example 19

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** to add to each user in the query results, a field **lastlogonnum**, which represents the number of days since the user last logged on.

**Description**
For each user returned in the query results, the following statement calculates the number of days since the user last logged on and places the value in the added custom field **lastlogonnum** (Field type: Single Value, Value type: Float).

* The **max** function returns the latest date (highest value) in **Last Logon Date** (**user.specific\_data.data.last\_logon**, which is a list (array) of logon dates and NOT a single value field).

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  It is necessary to use the **max** or **min** function to return a single last logon date, as the **subtract** function works on single value fields only and NOT on list fields.

  * The **subtract** function subtracts from the **now()** date (the current day's date) the value returned from the **max** function and places the value (the number of days since the last logon) in **lastlogonnum**. If there are no Logon dates registered for a user, **lastlogonnum** is assigned the fallback value - **0**.

  ```text
  user all
  then form.field_number
  set_value subtract(now(), max([user.specific_data.data.last_logon]))
  ```
</Callout>

The following screen shows the Enforcement Set configuration.

<Image alt="ECExampleLastLogon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECExampleLastLogon.png" />

The following screen shows the run results.

<Image alt="AssetsLastLogon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetsLastLogon.png" />

### Example 20

**Enforcement Action used:** **[Axonius - Add Custom Data to Assets](/docs/add-custom-data)** to add to each Security Finding in the query results, a custom field **VulnActiveDays**, which is the number of days that the vulnerability has been active before it has been mitigated.

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  The Security team can then use the **VulnActiveDays** values in a stat module to calculate the average age in days that a vulnerability for devices in a specific division and adapter have been active.
</Callout>

**Description**
For each Security Finding returned in the query results, the following statement calculates the number of days that the vulnerability was active by subtracting the date that it was first seen from the date that it was last seen.

* The **max** function returns the latest date (highest value) in the **vulnerability.specific\_data.data.first\_seen\_by\_source**, which is an aggregated list (array) of dates that the vulnerability was first seen. Similarly, for the **vulnerability.specific\_data.data.last\_seen** list.

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  It is necessary to use the **max** function to return one last seen date and one first seen date, as the **subtract** function works on single value fields only and NOT on list fields.
</Callout>

* The **subtract** function subtracts the maximum first seen value returned from the **max** function from the maximum last seen value returned from the **max** function and places the value (the number of days that the vulnerability was active) in the **VulnActiveDays** custom field. If there are no first seen or last seen dates registered for a vulnerability, **VulnActiveDays** is assigned the fallback value.

```text
vulnerability all 
then form.field_integer
set_value subtract (max([vulnerability.specific_data.data.last_seen]), max([vulnerability.specific_data.data.first_seen_by_source]))
```

***

### Example 21

**Enforcement Action used:** [**Jira - Create Ticket per Asset**](/docs/create-jira-issue-per-entity)

**Description**
For each asset that matches the query, the following statement concatenates the following:

* "Please make sure to include this device in the upcoming patch cycle, as it was found to have "
* The value in **device.specific\_data.data.software\_cves.cve\_id\_count**. This is the number of vulnerabilities found on the asset.
* " vulnerabilities, of which "
* The value in **device.specific\_data.data.software\_cves.cve\_severity.critical\_count**. This is the number of critical vulnerabilities found on the asset.
* " are considered critical."

It places the resulting concatenated string in **form.incident\_description** — the **Description** field of the ticket.

<Callout icon="📘" theme="info">
  <strong>Note</strong>

  If one or more fields are missing a value, the function fails and the action field in the asset is set to the fallback static value.
</Callout>

```text
device all then form.incident_description set_value concat ("Please make sure to include this device in the upcoming patch cycle, as it was found to have ", [device.specific_data.data.software_cves.cve_id_count], " vulnerabilities, of which ", [device.specific_data.data.software_cves.cve_severity.critical_count], " are considered critical.")
```