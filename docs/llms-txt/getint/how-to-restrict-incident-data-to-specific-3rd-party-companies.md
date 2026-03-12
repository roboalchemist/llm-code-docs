# Source: https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/how-to-restrict-incident-data-to-specific-3rd-party-companies.md

# How to Restrict "Incident" Data to Specific 3rd Party Companies

### Who is this tutorial for? <a href="#who-is-this-tutorial-for" id="who-is-this-tutorial-for"></a>

This tutorial is for users integrating multiple 3rd parties (e.g., multiple companies using Jira) with ServiceNow, and you want to ensure that each company only sees their relevant data.

### Use Case <a href="#use-case" id="use-case"></a>

The examples here are based on the **Incident** type in ServiceNow. However, you can apply the same logic to other types like Change Request, Requested Item, Incident Task, etc.

If your ServiceNow instance is integrated with multiple 3rd party companies using Jira, this setup ensures that each company only sees the data associated with their **Assignment Group** in the Getint integration.

{% hint style="info" %}
**Important**: When creating an Incident in ServiceNow, always specify the **Assignment Group** field.
{% endhint %}

### How does it work? <a href="#how-does-it-work" id="how-does-it-work"></a>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjJjlquR4lhcfwyW2tQKd%2FJira%20ServiceNow%20integration%20main%20screen.png?alt=media&#x26;token=0b42e6da-0389-4f2b-a852-4212b2505a04" alt=""><figcaption><p>Example integration Incident ↔︎ Bug</p></figcaption></figure>

* **Incident 1** created in ServiceNow with **Assignment Group: company1** will result in Getint creating a Bug in **company1's Jira**.
* **Incident 2** created in ServiceNow with **Assignment Group: company2** will result in Getint creating a Bug in **company2's Jira**.
* **Incident 3** created in ServiceNow **without an Assignment Group** will not create any Bug in Jira, even if the integration is enabled.

When a **Bug is created in Jira** by company1 or company2:

* Getint automatically creates a corresponding Incident in ServiceNow with the appropriate **Assignment Group** matching the company (e.g., company1 or company2).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9bzsxpRaXDnpFA9Qc1Px%2FGetint%20White%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=bb914c97-78ab-4a91-89b4-2e42a5dc06a2" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>

#### Quick Steps

* **Create an Assignment Group** in ServiceNow (e.g., **company1**).
* **Create a user** with the username **company1** and assign the roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**.
* **Add Business Rules** for incidents (and other relevant types) to restrict access (Insert, Update, Read) based on the Assignment Group and username.
* **Add Business Rules** to ensure that each company only uses its own Assignment Group.

#### Step 1: Create an Assignment Group in ServiceNow

To ensure that each company only has access to its own Incidents and data, first create an **Assignment Group** in ServiceNow.

* Go to **User Administration > Groups**.
* Create a new Assignment Group.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBNvBP38gozNuUy9y71A6%2FCreating%20an%20Assignment%20Group.png?alt=media&#x26;token=309dbc77-6a28-4360-b5a8-5c8dfad32a1f" alt=""><figcaption><p>Create a new <strong>Assignment Group</strong></p></figcaption></figure>

* Name the group (e.g., **company1**).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbppaBRxeiYzELMaw2iEZ%2FCreate%20the%20Assignment%20Group.png?alt=media&#x26;token=33814dcf-48ee-4cee-b834-e187d645e55f" alt=""><figcaption><p>Create an <strong>Assignment Group</strong> with name company1</p></figcaption></figure>

#### Step 2: Create a ServiceNow User for Each Company

For tutorial purposes, the **Assignment Group name** should match the **username** for the integration user. Of course, it is possible to use any assignment group but, in such case, scripts defined below will have to be adjusted.

* Go to **User Administration > Users** and create a new user (e.g., **company1**).
* Set the **User ID** to **company1**.
* Set the password for the user.
* Assign the roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**. If the **getint** role doesn’t exist, create it as described earlier.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FWBYjXaOpoa7l5xyHOi7Z%2FCreate%20a%20ServiceNow%20User.png?alt=media&#x26;token=33918100-bec0-460c-ada8-289fa5e74a5e" alt=""><figcaption><p>Create new user</p></figcaption></figure>

{% hint style="info" %}
**Important note:**

[In this tutorial,](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)we created the **getint\_integration** user (and it applies for most cases where you have a single ServiceNow and single Jira to integrate), but we need to create another user (for each company) and assign roles: **getint**, **sn\_incident\_read**, **sn\_incident\_write**)
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUDwm3qmF7d13xf4T9bSp%2FUser%20records.png?alt=media&#x26;token=6c2e8c9a-8983-46cc-982b-945acf030c04" alt=""><figcaption><p>User ID is the most important (company1)</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FC3DqBTRr2bhBbYrgZpZE%2FAfter%20creating%20an%20user%2C%20edit%20the%20user%20password..png?alt=media&#x26;token=cb6366f9-847f-4c80-b835-a5a52a3b1973" alt=""><figcaption><p>After creating a user. Edit the user password.</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FGBl1SOnC7oDu9NUP0h02%2FGenerate%20the%20password..png?alt=media&#x26;token=2fba2ce9-da3b-425c-9180-35e05b783d0c" alt=""><figcaption><p>Generate and then copy the password</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F3CA6WaROlRHhhC61k463%2FUncheck%20and%20click%20Update.png?alt=media&#x26;token=0ed11200-77b3-483b-b650-d6607bbf5f38" alt=""><figcaption><p>Uncheck and click Update.</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FlKnQ7ZSxwNXDaotg3IFI%2FAssign%20roles%20to%20the%20user.png?alt=media&#x26;token=f4e8be9a-3d28-471a-aef1-32de8d38b183" alt=""><figcaption><p>Assign Roles to the user</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FhRrdhiTxlKGFFzhfFlH6%2FUser%20Role%20-%20Edit%20Users.png?alt=media&#x26;token=58d87015-b416-4f36-82b8-8a1678249548" alt=""><figcaption><p>Assign <strong>getint</strong>, <strong>sn_incident_read</strong>, <strong>sn_incident_write</strong>. If you don't see role <strong>getint</strong> then create it as described <a href="https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration"><strong>here</strong></a>.</p></figcaption></figure>

#### Step 3: Add a Business Rule to Restrict Access to Incidents by Assignment Group and Username

You need to create Business Rules to ensure that data visibility is restricted by **Assignment Group** and **username**.

**Requirements:**

* The Assignment Group (e.g., **company1**) is created.
* The user with the matching username (e.g., **company1**) and with the roles assigned: (**getint**, **sn\_incident\_read**, **sn\_incident\_write**

{% hint style="info" %}
**Important:** The username and Assignment Group must be identical (case-sensitive).
{% endhint %}

**Steps:**

* Go to **Administration > Business Rule**.
* And follow the steps shown in the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvmGz4DzaO1ZzZk67wzrm%2FAdding%20a%20business%20rule.png?alt=media&#x26;token=9d9b2705-9cbe-46c2-88b0-a2b68dd08e74" alt=""><figcaption><p>Create a new Business Rule</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FW8vbKCdp348ZaCxeE1xm%2FBusiness%20rule%20configuration.png?alt=media&#x26;token=e3764bdd-2fff-4f9a-abda-f7ff8644c356" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fj5Q7g1TDXxrKgL9ZBO1e%2FAdding%20the%20business%20rule%20script.png?alt=media&#x26;token=f2970db5-6496-4197-8304-46fbdfeb98a9" alt=""><figcaption><p>Go to Advanced tab and paste script shown below.</p></figcaption></figure>

* Create a new Business Rule with the following script:

```
(function executeRule(current, previous) {
    var userName = gs.getUserName();  // Get the current user's username

 // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        gs.info("Admin user, bypassing group restriction.");
        return; // Allow admins to proceed
    }

    // Handle querying incidents where assignment group matches the username
    if (!current.isNewRecord()) {  // Only add this condition for non-insert actions
        current.addQuery('assignment_group.name', userName);  // Compare assignment group's name with the username
        gs.info("Querying incidents where assignment group matches username: " + userName);
    }

    // Handle inserts - set the assignment group based on the username
    if (current.isNewRecord()) {  // If this is an insert operation
        var userGr = new GlideRecord('sys_user_group');
        userGr.addQuery('name', userName);  // Find the group by username
        userGr.query();
        
        if (userGr.next()) {
            current.assignment_group = userGr.sys_id;  // Set the assignment group to the group found
            gs.info("Set assignment group to: " + userGr.name + " for user: " + userName);
        } else {
            gs.error("No matching assignment group found for username: " + userName);
        }
    }

    // Handle updates - restrict changes if assignment_group doesn't match the username
    if (!current.isNewRecord() && current.assignment_group.changes()) {  // If it's an update and assignment_group has changed
        var newAssignmentGroup = current.assignment_group.getDisplayValue().toLowerCase();
        
        // Check if the new assignment group matches the current user's group
        if (newAssignmentGroup !== userName.toLowerCase()) {
            gs.addErrorMessage("You cannot change the assignment group to one that does not match your username.");
            gs.error("Update blocked: Attempt to change assignment group to: " + newAssignmentGroup + " by user: " + userName);
            current.setAbortAction(true);  // Prevent the update from completing
        }
    }
})(current, previous);
```

This script ensures that users only see Incidents assigned to their group, and it sets the **Assignment Group** automatically for new records.

#### Step 4: (Optional) Add Business Rule to Hide Other Assignment Groups

This step is **optional** and only serves to hide other Assignment Groups, ensuring that 3rd parties will only see their own Assignment Group (which matches their username) in the integration configuration.

{% hint style="info" %}
**Important**: Even if a 3rd party company attempts to use an Assignment Group other than their own, Getint will ignore it and still enforce the use of the username as the Assignment Group.
{% endhint %}

**Purpose:**

This Business Rule ensures that each company only sees its own Assignment Group and hides others. This is useful for preventing 3rd parties from seeing Assignment Groups that do not belong to them.

**Steps:**

* Go to **Administration > Business Rule**.
* Create a new Business Rule following the steps shown in the images below.
* Set the fields as shown in the image.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPYYRTHwbfXlR1p3mOOu3%2FChecking%20assignment%20groups%20in%20getint%20integration.png?alt=media&#x26;token=d4b3c746-fd0d-4d9c-a682-09b81701347b" alt=""><figcaption><p>You can also hide all groups and leave group created specifically for 3rd party (ex. “company1”)</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FBfhYaAZ5vonuTQwtRGLG%2FNew%20Business%20Rule.png?alt=media&#x26;token=7106406c-575f-4638-a4c2-e424ff30a088" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fkev7RLBvOumXpvZi6mWk%2FBusiness%20rule%20setup.png?alt=media&#x26;token=5c0cb54f-6e35-47d3-9f79-e6612cde6bc0" alt=""><figcaption><p>Everything should be set as in the picture above</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPSWorAInvkxsnDeuWFEP%2FBusiness%20rule%20script%20for%20SNOW%20integration.png?alt=media&#x26;token=e2711d9f-dc48-4794-8c8d-633b9809be18" alt=""><figcaption><p>Go to Advanced tab and paste script shown below</p></figcaption></figure>

* Script: In the Advanced tab, paste the following script to restrict the visibility of Assignment Groups based on the current user's username:

```
(function executeRule(current, previous /*null when async*/) {
    // Get the current user's username
    var userName = gs.getUserName();
    // Bypass restriction for admin users
    if (gs.hasRole('admin')) {
        gs.info("Admin user, bypassing group restriction.");
        return; // Allow admins to proceed
    }
    // Get the group name of the current group being queried or interacted with
    var groupName = current.name.getDisplayValue();
    // Log values for debugging (optional)
    gs.info("User: " + userName + " | Group: " + groupName);
 // Restrict the query to return only groups where the group name matches the username
    current.addQuery('name', userName);
})(current, previous);
```

This rule ensures that only the group matching the username will be visible to each company during the integration process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FPzdBwHnoDwTXtyDvQelC%2FChecking%20Assignment%20Group%20in%20Getint.png?alt=media&#x26;token=4e5fca5e-c59b-40e6-bc8c-d391dce38247" alt=""><figcaption><p>Example for user "allegro." Only one Assignment Group is visible because username is allegro.</p></figcaption></figure>

#### Step 5: Add Business Rule to Restrict Access to Comments from Incidents

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FdQCHllEEQsIZ9nlYFf9q%2FAdd%20Business%20Rule%20to%20Restrict%20Access%20to%20Comments%20from%20Incidents.png?alt=media&#x26;token=3e53c704-bb07-4507-9600-b255bbedc7a0" alt=""><figcaption><p>Make sure to select sys_journal_field table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FsXhZtQS9gMtXd2OOAEor%2FAdvance%20tab%20for%20the%20business%20rule.png?alt=media&#x26;token=298c7280-0d74-41c1-b0eb-c785e325345b" alt=""><figcaption><p>Go to Advanced tab and paste script shown below</p></figcaption></figure>

* Create a new Business Rule with the following script

```
(function executeRule(current, previous /*null when async*/) {
 var username = gs.getUserName();

    // Filter records where the 'name' field is 'incident'
    current.addQuery('sys_class_name', 'incident'); // Ensure we are working with incidents only

    // Create a new GlideRecord for incidents
    var gr = new GlideRecord('incident');
    gr.addQuery('sys_class_name', 'incident'); // Ensure we are filtering incidents
    gr.query();

    var incidentSysIds = [];
    while (gr.next()) {
        var assignmentGroupId = gr.getValue('assignment_group'); // Get the sys_id of the assignment group
        var groupRecord = new GlideRecord('sys_user_group');
        if (groupRecord.get(assignmentGroupId)) { // Fetch group record
            var groupName = groupRecord.getValue('name'); // Get the group name
            if (groupName === username) {
                incidentSysIds.push(gr.getValue('sys_id')); // Add the incident's sys_id if it matches
            }
        }
    }

    // Now add the query to 'current' to return only the incidents with the collected sys_ids
    if (incidentSysIds.length > 0) {
        current.addQuery('element_id', 'IN', incidentSysIds); // Filter current to only include these sys_ids
    } else {
        current.addQuery('element_id', 'IN', ['-1']); // No matching incidents, return an empty set
    }

})(current, previous);
```

#### Step 6: Add Two Business Rules to Restrict Access to Attachments from Incidents

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

In the first step you will restrict access to the **sys\_attachment** table, and in the second step you will restrict access to the **sys\_attachment\_doc** table (which holds the data for each attachment).

* Restrict access to **sys\_attachment** table

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FiXYhQWQwe4m9xNTXwr9Y%2Fsys%20attachment%20table.png?alt=media&#x26;token=4e889fed-6872-4e45-92cc-732a9c5b5dba" alt=""><figcaption><p>Make sure to select sys_attachment table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FMuijH3N1aL5pdLw0UJpl%2FBusiness%20rule%20for%20step%206.png?alt=media&#x26;token=7acdb3b7-a7b8-47de-905b-75acb6ada7f2" alt=""><figcaption><p>Go to Advanced tab and paste script shown below:</p></figcaption></figure>

* Create a new Business Rule with the following script

```
(function executeRule(current, previous /*null when async*/) {
    var username = gs.getUserName();

    // Filter attachments that are linked to incidents
    current.addQuery('table_name', 'incident'); // Filter only attachments related to incidents

    // Create a new GlideRecord to query incidents
    var gr = new GlideRecord('incident');
    gr.addQuery('sys_class_name', 'incident'); // Ensure we are filtering incidents
    gr.query();

    var incidentSysIds = [];
    while (gr.next()) {
        var assignmentGroupId = gr.getValue('assignment_group'); // Get the sys_id of the assignment group
        var groupRecord = new GlideRecord('sys_user_group');
        if (groupRecord.get(assignmentGroupId)) { // Fetch group record
            var groupName = groupRecord.getValue('name'); // Get the group name
            if (groupName === username) { // Compare assignment group with the username
                incidentSysIds.push(gr.getValue('sys_id')); // Add the incident's sys_id if it matches
            }
        }
    }

    // Now add the query to 'current' to return only the attachments linked to the incidents with the matching assignment group
    if (incidentSysIds.length > 0) {
        gs.error("Matching incident sys_ids: " + incidentSysIds.join(", "));
        current.addQuery('table_sys_id', 'IN', incidentSysIds); // Filter current to only include attachments linked to these incidents
    } else {
        gs.error("No matching incidents found for user: " + username);
        current.addQuery('table_sys_id', 'IN', ['-1']); // No matching incidents, return an empty set
    }

})(current, previous);
```

* Restrict access to **sys\_attachment\_doc** table

**Steps:**

* Go to **Administration > Business Rule**.
* And follow steps shown on the pictures below:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FNQttSMtRPn3411FO9gyH%2Fsys%20attachment%20doc.png?alt=media&#x26;token=68d7bc75-72e1-4a4a-ba4f-6c4a5facd0d8" alt=""><figcaption><p>Make sure to select sys_attachment_doc table</p></figcaption></figure>

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fw1UOOXGMD2qocpUGKgBz%2FBusiness%20rule%20script%20for%20SNOW%20step%206.png?alt=media&#x26;token=e41fd0be-4efd-42ad-bfed-94daa0f270d4" alt=""><figcaption><p>Go to Advanced tab and paste script shown below:</p></figcaption></figure>

* Create a new Business Rule with the following script
*

```
(function executeRule(current, previous /*null when async*/) {
    var username = gs.getUserName();

    // Create a new GlideRecord for attachments related to incidents
    var attachmentGR = new GlideRecord('sys_attachment');
    attachmentGR.addQuery('table_name', 'incident'); // Filter for attachments related to incidents
    attachmentGR.query();

    var attachmentSysIds = [];
    while (attachmentGR.next()) {
        var incidentId = attachmentGR.getValue('table_sys_id'); // Get the sys_id of the related incident
        
        // Query the incident to get the assignment group
        var incidentGR = new GlideRecord('incident');
        if (incidentGR.get(incidentId)) {
            var assignmentGroupId = incidentGR.getValue('assignment_group'); // Get assignment group id
            var groupRecord = new GlideRecord('sys_user_group');
            if (groupRecord.get(assignmentGroupId)) { // Fetch group record
                var groupName = groupRecord.getValue('name'); // Get the group name
                if (groupName === username) {
                    attachmentSysIds.push(attachmentGR.getValue('sys_id')); // Add the attachment sys_id if it matches
                }
            }
        }
    }

    // Now add the query to 'current' to return only the documents linked to the attachments with the collected sys_ids
    if (attachmentSysIds.length > 0) {
        gs.error("Matching attachment sys_ids for user: " + username + " - " + attachmentSysIds.join(", "));
        current.addQuery('sys_attachment', 'IN', attachmentSysIds); // Filter current to only include attachment docs linked to these attachments
    } else {
        gs.error("No matching attachments found for user: " + username);
        current.addQuery('sys_attachment', 'IN', ['-1']); // No matching attachments, return an empty set
    }

})(current, previous);
```

### Summary

We have now restricted data access for each company to the Incidents associated with their Assignment Group. You can apply similar logic to other tables, such as Change Request, to restrict full access.

If you need any further help or if you are experiencing issues with your integration, feel free to open a support ticket at our [Support Portal.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
