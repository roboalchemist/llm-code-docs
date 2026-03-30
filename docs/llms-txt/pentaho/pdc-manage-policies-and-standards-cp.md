# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-policies-and-standards-cp.md

# Manage policies and standards

You can use the Pentaho Data Catalog policy manager to configure policies to set the expectations for your organization's behavior and decision-making, and to define standards for the tools and methods to achieve the intent of the policies.

## **Policy**

A policy is a statement of intent or guideline an organization wants to follow. It sets the overall direction and principles for how an organization operates in a specific area. For example, a data governance policy might state that all data must be classified and protected according to its sensitivity. A data lifecycle policy might state the intent around acquiring, storing and purging of data.

### Add a policy

Add a policy as a statement of intent or guideline your organization wants to follow.

Perform the following steps to add a policy:

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Click **Actions** > **Add New Policy**.

   The Create Policy window opens.
3. In the **Policy Name** field, enter a name for the policy.
4. (Optional) In the **Parent** field, select a parent policy.

   **Note:** The parent policy is automatically assigned if you have the policy selected before creating a new policy. You can choose a different policy if necessary.
5. Click **Create**.

   The policy is created and shown in the **Policy** navigation tree.
6. (Optional) Add information on the **Summary** tab as needed:

   **Note:** Fields with a pencil icon can be edited by clicking the pencil icon.

<table><thead><tr><th width="190.66668701171875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Definition</strong></td><td>Definition of the policy.</td></tr><tr><td><strong>Purpose</strong></td><td>Purpose of the policy.</td></tr><tr><td><strong>Scope</strong></td><td>Scope of the policy.</td></tr><tr><td><strong>Stakeholders</strong></td><td>People who are involved in or affected by a policy or policy action. Click the down arrow to view the list of users, then select or clear checkboxes to update the users that are stakeholders, and click <strong>Apply</strong>.</td></tr><tr><td>Rating</td><td>Rating for the policy.<br>To rate the policy, click one of the stars above the Properties pane.</td></tr></tbody></table>

In the Properties pane, you can add the following values:

<table><thead><tr><th width="191.7777099609375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Effective From-Until</strong></td><td><p>The date from which the policy is effective and the date until which the policy is effective.</p><ol><li>Click the field to open two calendars.</li><li>Click a day on the first calendar or enter a date to set the date that the policy goes into effect.</li><li>Click a day on the second calendar or enter a date to set the date that the policy expires.</li></ol></td></tr><tr><td><strong>Policy Review Date</strong></td><td><p>The date by which the policy should be reviewed.</p><ol><li>Click the field to open a calendar. </li><li>Click a day or enter a date to set a date to review the policy.</li></ol></td></tr><tr><td><strong>Policy Version</strong></td><td>Version of the policy.<br>Enter a version number.</td></tr><tr><td><strong>Domain</strong></td><td>Domain for the policy. Enter a domain value.</td></tr><tr><td><strong>Status</strong></td><td>Status of the policy. Select one of the following values: <strong>Draft</strong>, <strong>Review</strong>, <strong>Accepted</strong>, <strong>Deprecated</strong>.</td></tr><tr><td><strong>Custodian</strong></td><td>Custodian of the policy.<br>Click one of the users to assign as a custodian for the policy.</td></tr><tr><td><strong>Business Steward</strong></td><td>Business Steward for the policy. Click one of the users to assign as a business steward for the policy.</td></tr><tr><td><strong>Owners</strong></td><td>Owner of the policy.<br>Click one of the users to assign as an owner for the policy.</td></tr><tr><td><strong>Tags</strong></td><td>Label to associate with the policy.<br>To add a new tag, type a tag name and press <strong>Enter</strong>.</td></tr></tbody></table>

7\. Click **Save** to save your changes on the **Summary** tab.

8. (Optional) To add one or more custom properties, click the **Custom** tab.

   The **Custom** tab opens.

   1. Click **Add Custom Property**.

      The Add Custom Property window opens.
   2. Add information for the following fields:

      <table><thead><tr><th width="167.1112060546875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Field Label</strong></td><td>Field name that uniquely identifies the property.</td></tr><tr><td><strong>Field Type</strong></td><td><strong>Free text</strong> or <strong>Select Value</strong>.</td></tr><tr><td><strong>Available Values</strong></td><td>Field that appears and is required if you specify <strong>Select Value</strong> for <strong>Field Type</strong>. Enter comma-separated values that a user can choose when they add a property to a resource.</td></tr><tr><td><strong>Default Value</strong></td><td>(Optional) To set a default value, select one of the pre-existing values to display.</td></tr><tr><td><strong>Allow Blank</strong></td><td>(Optional) Select the checkbox to allow the property without any defined value.</td></tr></tbody></table>
   3. Click **Save**.

      A confirmation message is shown, and the custom property is added to the **Custom Properties** table.
   4. (Optional) If you want to add another custom property, repeat the steps.

   One or more custom properties are added.
9. (Optional) To add business terms, click the **Business Terms** tab.

   The **Business Terms** tab opens.

   A business term is a word or phrase that uses the vocabulary of a business function to describe the data it is associated with.

   1. Click **Add Terms**.

      The Business Terms window opens.
   2. Navigate to one or more terms to add and select their checkboxes.

      **Note:** The **Add** button shows the number of terms that are selected.
   3. Click **Add** to add the terms.

      The business terms are added.
10. (Optional) To add a comment, click the **Comment** tab.

    The **Comment** tab opens.

    1. In the **Enter comment** field, type your comment.

       You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.
    2. Click **Post** to add the comment.

    The comment is posted.

The policy is added.

### Update a policy

Update a policy to make changes like updating the policy language, assigning different users to one or more policy roles, or changing the effective dates of a policy.

Perform the following steps to update a policy:

1. In the left navigation menu, click **Policy**.

   The **Policy** page opens.
2. Select the policy that you want to update.

   The page for the policy opens.
3. (Optional) To update basic information, click the **Summary** tab:

   The **Summary** tab opens.

   **Note:** You can edit the fields by clicking the pencil icon.

<table><thead><tr><th width="141.77783203125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Policy</strong></td><td>Name for the policy.</td></tr><tr><td><strong>Definition</strong></td><td>Definition of the policy.</td></tr><tr><td><strong>Purpose</strong></td><td>Purpose of the policy.</td></tr><tr><td><strong>Scope</strong></td><td>Scope of the policy.</td></tr><tr><td><strong>Stakeholders</strong></td><td>People who are involved in or affected by a policy or policy action. Click the down arrow to view the list of users, then select or clear checkboxes to update the users that are stakeholders, and click <strong>Apply</strong>.</td></tr><tr><td>Rating</td><td>Rating for the policy. To rate the policy, click one of the stars above the Properties pane.</td></tr></tbody></table>

In the Properties pane, you can update the following values:

<table><thead><tr><th width="197.333251953125">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Effective From-Until</strong></td><td><p>Date that the policy is effective from and date that the policy is effective until.</p><p>1. Click the field to open two calendars.<br>2. Click a day on the first calendar or enter a date to set the date that the policy goes into effect.<br>3. Click a day on the second calendar or enter a date to set the date that the policy expires.</p></td></tr><tr><td><strong>Policy Review Date</strong></td><td>Date by which the policy should be reviewed.<br>1. Click the field to open a calendar.<br>2. Click a day or enter a date to set a date to review the policy.</td></tr><tr><td><strong>Policy Version</strong></td><td>Version of the policy.Enter or update the version number.</td></tr><tr><td><strong>Domain</strong></td><td>Domain for the policy. Enter or update the domain value.</td></tr><tr><td><strong>Status</strong></td><td>Status of the policy. Select one of the following values: <strong>Draft</strong>, <strong>Review</strong>, <strong>Accepted</strong>, <strong>Deprecated</strong>.</td></tr><tr><td><strong>Custodian</strong></td><td>Custodian of the policy.Click one of the users to assign as a custodian for the policy.</td></tr><tr><td><strong>Business Steward</strong></td><td>Business Steward for the policy. Click one of the users to assign as a business steward for the policy.</td></tr><tr><td><strong>Owners</strong></td><td>Owner of the policy.Click one of the users to assign as an owner for the policy.</td></tr><tr><td><strong>Tags</strong></td><td>Label to associate with the policy.To add a new tag, type a tag name and press <strong>Enter</strong>, or to remove a tag, click the <strong>X</strong> next to an existing tag.</td></tr></tbody></table>

4\. Click **Save** to save your changes on the **Summary** tab.

5. (Optional) To update custom properties associated with a policy, click the **Custom** tab:

   The **Custom** tab opens.

   * To add a custom property, click **Add Custom Property**, and enter the following values:

     <table><thead><tr><th width="156">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Field Label</strong></td><td>Field name that uniquely identifies the property.</td></tr><tr><td><strong>Field Type</strong></td><td><strong>Free text</strong> or <strong>Select Value</strong>.</td></tr><tr><td><strong>Available Values</strong></td><td>This field appears and is required if you specify <strong>Select Value</strong> for <strong>Field Type</strong>. Enter comma-separated values that a user can choose when they add a property to a resource.</td></tr><tr><td><strong>Default Value</strong></td><td>(Optional) To set a default value, select one of the pre-existing values to display.</td></tr><tr><td><strong>Allow Blank</strong></td><td>(Optional) Select the checkbox to allow the property without any defined value.</td></tr></tbody></table>

     1. Click **Save** to save the custom property.

        A confirmation message is shown and the custom property is added to the **Custom Properties** table.
     2. (Optional) If you want to add another custom property, repeat the steps.
   * To update a custom property value, click the **Property Value** field and update the value.\
     One or more custom properties are updated.
6. (Optional) To update business terms associated with a policy, click the **Business Terms** tab:

   The **Business Terms** tab opens.

   A business term is a word or phrase that uses the vocabulary of a business function to describe the data it is associated with.

   * To add business terms, use the following steps:
     1. Click **Add Terms**.

        The Business Terms window opens.
     2. Navigate to one or more terms to add and select their checkboxes.

        **Note:** The **Add** button displays the number of terms that are selected.
     3. Click **Add** to add the terms.
   * To remove a business term from a policy, click the trash can icon next to the term.

     **Note:** This action does not delete the business term but removes its association with the policy.

   The business terms are updated.
7. (Optional) To add, update, or delete a comment, click the **Comment** tab:

   The **Comment** tab opens.

   You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.

   * To add a new comment, use the following steps:
     1. Scroll to the bottom of the **Comment** tab and locate the **Enter comment** field.
     2. In the **Enter comment** field, type your comment.

        You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.
     3. Click **Post** to add the comment.\
        The comment is posted.
   * To edit a comment, use the following steps:

     **Note:** You can only edit comments that you made.

     1. Click the pencil icon and edit the comment.
     2. Click **Update**.\
        The comment is updated.
   * To delete a comment, use the following steps:

     **Note:** You can only delete comments that you made.

     1. Click the trash can icon next to the comment.

        A confirmation message opens.
     2. Click **Proceed** to delete the comment.\
        The comment is deleted.

   The policy is updated.

### Delete a policy

You can delete a policy that is no longer needed or is a duplicate of another policy.

Use the following steps to delete a policy:

**Note:** You cannot recover a deleted policy, so make sure this is what you want to do.

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Select the policy you want to delete.
3. Click the More actions icon (three vertical dots) next to the policy name and click **Delete**.

   A confirmation message opens.
4. Click **Confirm** to delete the policy.

The policy is deleted.

## **Standard**

A standard is more specific and detailed. It defines the criteria and requirements that must be met to comply with the policy. Standards provide the measurable benchmarks that are agreed upon pertaining to the parent policy. For instance, a data quality standard might require that a particular data field must always be completed and fall within a defined range.

For example, a policy governing the collection of customer data might have a standard with the following criteria:

* A customer's data must contain an active customer identifier with it.
* A customer's data must contain consent to use it for a given business purpose.
* A customer's data must be deleted upon request or at the end of a predefined period.

This standard might be linked to the SalesForce application.

You can link standards to specific data elements and applications, assign terms in business and governance vocabulary, and apply rule definitions. When you apply a rule definition to a standard, you can set actions to occur if the data meets or does not meet certain criteria.

**Note:** To add and delete policies and standards, you need the Business Steward role assigned to you. You need the Data Steward or Admin role assigned to you if you need to associate data elements or applications to a standard or manage those associations.

### Add a standard

Add a standard to define the data elements, applications, business terms, and rules used to achieve the intent of the associated policy.

Perform the following steps to add a standard:

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Navigate to the policy to which you want to add the standard.
3. Click **Actions** > **Add New Standard**.

   The Create Standard window opens.
4. In the **Standard Name** field, enter a name for the standard.
5. (Optional) In the **Parent** field, select a parent policy.

   **Note:** The parent policy is automatically assigned if you have the policy selected before adding a new standard. You can choose a different parent policy if necessary.
6. Click **Create**.

   The standard is created and shown in the **Policy** navigation tree.
7. (Optional) Add information on the **Summary** tab as needed:

   **Note:** Fields with a pencil icon can be edited by clicking the pencil icon.

<table><thead><tr><th width="149.55560302734375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Definition</strong></td><td>Definition of the standard.</td></tr><tr><td><strong>Purpose</strong></td><td>Purpose of the standard.</td></tr><tr><td><strong>Scope</strong></td><td>Scope of the standard.</td></tr><tr><td><strong>Stakeholders</strong></td><td>People who are involved in or affected by a standard or standard action. Click the down arrow to view the list of users, then select or clear checkboxes to update the users that are stakeholders, and click <strong>Apply</strong>.</td></tr><tr><td>Rating</td><td>Rating for the standard. To rate the standard, click one of the stars above the Properties pane.</td></tr></tbody></table>

In the Properties pane, you can update the following values:

<table><thead><tr><th width="207.3333740234375">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Effective From-Until</strong></td><td><p>Date that the standard is effective from and date that the standard is effective until.</p><p>1. Click the field to open two calendars.<br>2. Click a day on the first calendar or enter a date to set the date that the standard goes into effect.<br>3. Click a day on the second calendar or enter a date to set the date that the standard expires.</p></td></tr><tr><td><strong>Standard Review Date</strong></td><td><p>Date by which the standard should be reviewed.</p><p>1. Click the field to open a calendar.<br>2. Click a day or enter a date to set a date to review the standard.</p></td></tr><tr><td><strong>Standard Version</strong></td><td>Version of the standard.<br>Enter a version number.</td></tr><tr><td><strong>Domain</strong></td><td>Domain for the standard. Enter a domain value.</td></tr><tr><td><strong>Status</strong></td><td>Status of the standard. Select one of the following values: <strong>Draft</strong>, <strong>Review</strong>, <strong>Accepted</strong>, <strong>Deprecated</strong>.</td></tr><tr><td><strong>Custodian</strong></td><td>Custodian of the standard.<br>Click one of the users to assign as a custodian for the standard.</td></tr><tr><td><strong>Business Steward</strong></td><td>Business Steward for the standard. Click one of the users to assign as a business steward for the standard.</td></tr><tr><td><strong>Owners</strong></td><td>Owner of the standard.<br>Click one of the users to assign as an owner for the standard.</td></tr><tr><td><strong>Tags</strong></td><td>Label to associate with the standard.<br>To add a new tag, type a tag name and press <strong>Enter</strong>.</td></tr></tbody></table>

8\. Click **Save** to save your changes on the **Summary** tab.

9. (Optional) To add one or more custom properties, click the **Custom** tab.

   The **Custom** tab opens.

   1. Click **Add Custom Property**.

      The Add Custom Property window opens.
   2. Add information for the following fields:

      <table><thead><tr><th width="168.22216796875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Field Label</strong></td><td>Field name that uniquely identifies the property.</td></tr><tr><td><strong>Field Type</strong></td><td><strong>Free text</strong> or <strong>Select Value</strong>.</td></tr><tr><td><strong>Available Values</strong></td><td>Field that appears and is required if you specify <strong>Select Value</strong> for <strong>Field Type</strong>. Enter comma-separated values that a user can choose when they add a property to a resource.</td></tr><tr><td><strong>Default Value</strong></td><td>(Optional) To set a default value, select one of the pre-existing values to display.</td></tr><tr><td><strong>Allow Blank</strong></td><td>(Optional) Select the checkbox to allow the property without any defined value.</td></tr></tbody></table>
   3. Click **Save**.
   4. (Optional) If you want to add another custom property, repeat the steps.

   One or more custom properties are added.
10. (Optional) To add business terms, click the **Business Terms** tab.

    The **Business Terms** tab opens.

    1. Click **Add Terms**.

       The Business Terms window opens.
    2. Navigate to one or more terms to add and select their checkboxes.

       **Note:** The **Add** button displays the number of terms that are selected.
    3. Click **Add** to add the terms.

    The business terms are added.
11. (Optional) To add one or more data elements to a standard, click the **Data Elements** tab.

    The **Data Elements** tab opens.

    **Note:** You need to have the Data Steward or Admin role to add or update data elements for a standard.

    1. Click **Add Data Element**.

       The Add Entities window opens.
    2. Navigate to the data elements you want to add.
    3. Select the checkboxes for the data elements.

       **Note:** The **Add** button displays the number of data elements that are selected.
    4. Click **Add**.

    The data elements are added.
12. (Optional) To add a comment, click the **Comment** tab.

    The **Comment** tab opens.

    1. In the **Enter comment** field, type your comment.

       You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.
    2. Click **Post** to add the comment.

    The comment is posted.
13. (Optional) To add one or more applications, click the **Applications** tab.

    The **Applications** tab opens.

    **Note:** You need to have the Data Steward or Admin role to add applications to a standard.

    1. Click **Add Applications**.

       The Add Applications window opens.
    2. Navigate to the applications you want to add.
    3. Select the checkboxes for the applications.

       **Note:** The **Add** button displays the number of applications that are selected.
    4. Click **Add**.

       The applications are added.
14. (Optional) To add one or more rule definitions, click the **Rules** tab.

    The **Rules** tab opens.

    1. Click **Add Rule definition(s)**.

       The Select rule definition(s) window opens.
    2. Select checkboxes for rule definitions to associate with the standard.

       **Note:** The **Add** button displays the number of rule definitions being added.
    3. For **Relationship type**, select either **Enforced By** or **Measured By**.

    One or more rule definitions are added.

The standard is added.

### Update a standard

Update a standard to update the data elements, applications, business terms, and rules associated with a standard.

Perform the following steps to update a standard:

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Select the standard that you want to update.

   The page for the standard opens.
3. (Optional) To update basic information, click the **Summary** tab:

   The **Summary** tab opens.

   **Note:** You can edit the fields by clicking the pencil icon.

<table><thead><tr><th width="155.11102294921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Standard</strong></td><td>Name for the standard.</td></tr><tr><td><strong>Definition</strong></td><td>Definition of the standard.</td></tr><tr><td><strong>Purpose</strong></td><td>Purpose of the standard.</td></tr><tr><td><strong>Scope</strong></td><td>Scope of the standard.</td></tr><tr><td><strong>Stakeholders</strong></td><td>People that are involved in or affected by a standard or standard action.Click the down arrow to view the list of users, then select or clear checkboxes to update the users that are stakeholders, and click <strong>Apply</strong>.</td></tr><tr><td>Rating</td><td>Rating for the standard.To rate the standard, click one of the stars above the Properties pane.</td></tr></tbody></table>

In the Properties pane, you can update the following values:

<table><thead><tr><th width="212.888916015625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Effective From-Until</strong></td><td><p>Date that the standard is effective from and date that the standard is effective until.</p><p>1. Click the field to open two calendars.<br>2. Click a day on the first calendar or enter a date to set the date that the standard goes into effect.<br>3. Click a day on the second calendar or enter a date to set the date that the standard expires.</p></td></tr><tr><td><strong>Standard Review Date</strong></td><td><p>Date by which the standard should be reviewed.</p><p>1. Click the field to open a calendar.<br>2. Click a day or enter a date to set a date to review the standard.</p></td></tr><tr><td><strong>Standard Version</strong></td><td>Version of the standard. Enter a version number.</td></tr><tr><td><strong>Domain</strong></td><td>Domain for the standard. Enter or update the domain value.</td></tr><tr><td><strong>Status</strong></td><td>Status of the standard. Select one of the following values: <strong>Draft</strong>, <strong>Review</strong>, <strong>Accepted</strong>, <strong>Deprecated</strong>.</td></tr><tr><td><strong>Custodian</strong></td><td>Custodian of the standard.Click one of the users to assign as a custodian for the standard.</td></tr><tr><td><strong>Business Steward</strong></td><td>Business Steward for the standard. Click one of the users to assign as a business steward for the standard.</td></tr><tr><td><strong>Owners</strong></td><td>Owner of the standard.Click one of the users to assign as an owner for the standard.</td></tr><tr><td><strong>Tags</strong></td><td>Label to associate with the standard.To add a new tag, type a tag name and press <strong>Enter</strong>, or to remove a tag, click the <strong>X</strong> next to an existing tag.</td></tr></tbody></table>

4\. Click **Save** to save your changes on the **Summary** tab.

5. (Optional) To update custom properties, click the **Custom** tab:

   The **Custom** tab opens.

   * To add a custom property, click **Add Custom Property**, and enter the following values:

     <table><thead><tr><th width="176">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Field Label</strong></td><td>Field name that uniquely identifies the property.</td></tr><tr><td><strong>Field Type</strong></td><td><strong>Free text</strong> or <strong>Select Value</strong>.</td></tr><tr><td><strong>Available Values</strong></td><td>This field appears and is required if you specify <strong>Select Value</strong> for <strong>Field Type</strong>. Enter comma-separated values that a user can choose when they add a property to a resource.</td></tr><tr><td><strong>Default Value</strong></td><td>(Optional) To set a default value, select one of the pre-existing values to display.</td></tr><tr><td><strong>Allow Blank</strong></td><td>(Optional) Select the checkbox to allow the property without any defined value.</td></tr></tbody></table>

     1. Click **Save** to save the custom property.

        A confirmation message is shown and the custom property is added to the **Custom Properties** table.
     2. (Optional) If you want to add another custom property, repeat the steps.
   * To update a custom property value, click the **Property Value** field and update the value.\
     One or more custom properties are updated.
6. (Optional) To update business terms associated with a standard, click the **Business Terms** tab:

   The **Business Terms** tab opens.

   A business term is a word or phrase that uses the vocabulary of a business function to describe the data it is associated with.

   * To add business terms, use the following steps:
     1. Click **Add Terms**.

        The Business Terms window opens.
     2. Navigate to one or more terms to add and select their checkboxes.

        **Note:** The **Add** button displays the number of terms that are selected.
     3. Click **Add** to add the terms.
   * To remove a business term from a standard, click the trash can icon next to the term.

     **Note:** This action does not delete the business term but removes its association with the standard.

   The business terms are updated.
7. (Optional) To add or update one or more data elements, click the **Data Elements** tab:

   The **Data Elements** tab opens.

   **Note:** You need to have the Data Steward or Admin role to add or update data elements for a standard.

   * To add data elements, use the following steps:
     1. Click **Add Data Element**. The Add Entities window opens.
     2. Navigate to one or more data elements that you want to add.
     3. Select the checkboxes for the data elements.

        **Note:** The **Add** button displays the number of data elements you are adding.
     4. Click **Add**. The data elements are added.
   * To remove a data element, click the trash can icon next to the data element in the list.

     **Note:** This action does not delete the data element but removes its association with the standard.
8. (Optional) To add update or delete a comment, click the **Comment** tab:

   The **Comment** tab opens.

   You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.

   * To add a new comment, use the following steps:
     1. Scroll to the bottom of the **Comment** tab and locate the **Enter comment** field.
     2. In the **Enter comment** field, type your comment.

        You can add comments, share suggestions, or ask questions directly in the comment, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the **Mentions** card on the Home page (if enabled), prompting them to respond if necessary.
     3. Click **Post** to add the comment.\
        The comment is posted.
   * To edit a comment, use the following steps:

     **Note:** You can only edit comments that you made.

     1. Click the pencil icon and edit the comment.
     2. Click **Update**.\
        The comment is updated.
   * To delete a comment, use the following steps:

     **Note:** You can only delete comments that you made.

     1. Click the trash can icon next to the comment.

        You see a confirmation message.
     2. Click **Proceed** to delete the comment.\
        The comment is deleted.
9. (Optional) Click the **Applications** tab to add or remove one or more applications associated with the standard.

   The **Applications** tab opens.

   **Note:** You need to have the Data Steward or Admin role to add applications to or remove them from a standard.

   * To add one or more applications, use the following steps:
     1. Click **Add Applications**.

        The Applications window opens.
     2. Navigate to one or more applications you want to add.
     3. Select the checkboxes for the applications.

        **Note:** The **Add** button displays the number of applications that are selected.
     4. Click **Add**.\
        The applications are added.
   * To remove an application, click the trash can icon next to the application.

     **Note:** This action does not remove the application but removes its association with the standard.

     The application is removed.
10. (Optional) To add or update one or more rule definitions, click the **Rules** tab.

    The **Rules** tab opens.

    * To add one or more rule definitions, use the following steps:
      1. Click **Add Rule definition(s)**.

         The Select rule definition(s) window opens.
      2. Select checkboxes for rule definitions to associate with the standard.

         **Note:** The **Add** button displays the number of rule definitions that are selected.
      3. For **Relationship Type**, select either **Enforced By** or **Measured By**.
      4. Click **Add**.\
         One or more rule definitions are added.
    * To remove a rule definition, click the trash can icon next to the rule definition.

      **Note:** This action does not remove the rule definition but removes its association with the standard.

    The rule definitions are updated.

The standard is updated.

### Delete a standard

You can delete a standard that is no longer needed or is a duplicate of another standard.

Use the following steps to delete a standard:

**Note:** You cannot recover a deleted standard, so make sure this is what you want to do.

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Select the standard you want to delete.
3. Click the **More** actions icon (three vertical dots) next to the standard name and click **Delete**.

   A confirmation message opens.
4. Click **Confirm** to delete the standard.

The standard is deleted.

### Import policies and standards

You can import policies and standards from outside of Pentaho Data Catalog with a file in one of the following file types:

* JSON Lines (see <https://jsonlines.org/> for more information)
* Comma Separated Values (text/csv)

Use the following steps to import a policy or standard:

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Navigate to the location where you want to import the policy or standard.

   The page for the policy or standard opens.
3. Click **Actions** > **Import**.

   The Import Assets window opens.
4. Click inside the box to select a JSON Lines or CSV file for the policy or standard.

   The file name and its size are shown below the dotted line box.
5. Click **Submit**.

The file is imported and is shown in the Policy navigation tree.

### Export policies and standards

You can export policies and standards from Data Catalog.

Use the following steps to export a policy or standard:

1. In the left navigation menu, click **Policy**.

   The Policy page opens.
2. Select the policy or standard you want to export.

   The page for the policy or standard opens.
3. Click **Actions** > **Export**.

   The **Export Assets** dialog box opens.
4. Select the polocy and standard, you want to export. Select individual polocies and standards, or choose **Select all.**\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
5. Select the file type (**CSV** or **JSON**), you want to export the polocies and standards to and click **Submit**.

   This downloads the file containing the glossary polocies and standards in the selected format.

The file is exported to your default download location, such as the `Downloads` folder.
