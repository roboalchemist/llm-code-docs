# Source: https://docs.axonius.com/docs/using-the-dynamic-value-statement-wizard.md

# Using the Dynamic Value Statement Wizard

You can create Dynamic Value Statements using the following methods:

* The Wizard
* [Syntax](/docs/using-the-syntax-helper) - Includes Autocomplete feature and Syntax Helper.

This page explains how to create Dynamic Value Statements using the Wizard.

<Callout icon="📘" theme="info">
  Note

  Before configuring a Dynamic Value Statement, do the following:

  * From the **Module** dropdown, select the assets on which to run the query.

  * Fill in default values for the action fields that are below the statement. These will be the fallback values for the Dynamic Value Statement.
</Callout>

After completing the Dynamic Value Statement and saving the Enforcement Set, you can click **Simulate** to [debug the statement](/docs/using-the-simulator).

## Creating a Dynamic Value Statement Using the Wizard

### Adding an All Statement

This section describes how to construct an *All* statement using the Dynamic Value Statement wizard. Learn more about [All Statement syntax](/docs/all-statement-syntax).

**To construct an All statement**

1. Toggle on **Configure Dynamic Values** and then click **Wizard**. The Dynamic Value Statement Wizard for creating an *All* statement opens.

2. From the **Select form field** dropdown, select the action field to populate.

3. From the second dropdown, assign a value or function to the action field. See [Selecting Action Field](#selecting-action-field) below.

4. To assign additional adapter fields or relations to an action field, click **+ Add Alternative** for each one to add. An **OR** clause is added to the statement for each one. The screen below shows an *All* statement with several **OR** clauses.

5. Click **+ Also** to configure an additional action field in the statement, and repeat this procedure from the second step.

<Image alt="AllStatementExample(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AllStatementExample(1).png" />

When done, you can click **Syntax** to view the syntax of the statement created by the Wizard. Learn more about converting from [Wizard to Syntax](#converting-from-wizard-to-syntax).

<Image alt="AllStatementExampleValidate(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AllStatementExampleValidate(1).png" />

After saving the Enforcement Set, you can click **Simulate** from either above the **Wizard** or **Syntax** statement to [debug the statement](/docs/using-the-simulator). The following screen shows the results of hovering over a component in the statement.

<Image alt="SimulateAllExample(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateAllExample(1).png" />

### Adding a Switch/Case Statement

This section describes how to construct a *Switch/Case* statement using the Dynamic Value Statement wizard.
Learn more about [Switch/Case Statement syntax](/docs/switchcase-statements-syntax).

<Callout icon="📘" theme="info">
  Note

  The Dynamic Value Statement wizard supports all operators and the following functions in a *Switch/Case* statement: **To upper**, **To lower**, **Substring**, **Relation**, **Concat**, and **Concat (Relation)**)
</Callout>

**To construct a Switch/Case statement**

1. Toggle on **Configure Dynamic Values**, click **Wizard**, and then click **Switch to value by condition**. The Dynamic Value Statement Wizard for creating a *Switch/Case* statement opens.

2. Configure the *Switch* part of the statement:
   1. From the **Adapter** and **Select Adapter Field** dropdowns, select the adapter and adapter field. Learn [how to select an adapter and adapter field](#selecting-an-adapter-and-adapter-field).
   2. From the **Select operator** dropdown, select the operator to use on the adapter field value, and in **Write**, type the value to compare to the field value using the operator.
      ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OperatorDropdown.png)

3. Configure the *Case* part of the statement:
   1. From the **Select form field** dropdown, select the action field that you want to populate.
   2. From the second dropdown, select a value or function to assign to the action field, when the condition in the *Switch* part of the statement is met. See [Selecting Action Field](#selecting-action-field) below.

4. Click **+ Also** to populate an additional action field in the Switch part of the statement. Proceed as in the previous step.

5. Repeat the previous step for each action field that you want to populate for this *IF* condition.

6. Click **Add Condition** to add an **ELSE IF** clause to the statement and repeat the previous three steps.

<Callout icon="📘" theme="info">
  Note

  * The adapter and adapter field cannot be changed in the ELSE IF clauses.

  * You can click **Remove Condition** to remove any condition except the first. This button appears from the second condition onward.
</Callout>

7. Repeat the previous step for each **ELSE IF** clause to add to the statement.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WizardSwitchCaseAlsoJira.png)

You can click **Syntax** to view the syntax of the statement created by the Wizard. Learn more about converting from [WIzard to Syntax](#converting-from-wizard-to-syntax).

<Image alt="SyntaxJira" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxJira.png" />

After saving the Enforcement Set, you can click **Simulate** from either above the **Wizard** or **Syntax** statement to [debug the statement](/docs/using-the-simulator). The following screen shows the results of hovering over a component in the statement.

<Image alt="SimulateJira" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateJira.png" />

### Selecting an Adapter and Adapter Field

<Callout icon="📘" theme="info">
  Note

  You must select a module (asset type) before selecting an adapter and adapter field.
</Callout>

* The **Adapter** dropdown contains a list of all adapters that fetched data for assets. The adapter that you select from this dropdown controls the list of fields displayed in the **Adapter Field** dropdown.

  * The first entry and default selection in this dropdown is **Aggregated** represented by the  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(213\).png) icon.

* The **Select Adapter Field** dropdown contains a list of all the fields on that adapter.
  * In the case of the **Aggregated** selection in the Adapter dropdown, this is a list of all fields whose data is aggregated (i.e., collated) from all of the data that was fetched from all adapters. These are considered common fields.

### Selecting Action Field

You can use the Wizard to construct a simple *set-value* statement to set the value of an action field to one of the following. This can be used in both *All* and *Switch/Case* statements.

* **Adapter field** - The value of the adapter field. In this case,[select an adapter and adapter field](#selecting-an-adapter-and-adapter-field).

* **Custom input** - The value that you enter in the Value (**Write**) box.

* **Concat** - The concatenation of adapter fields, relation fields, and/or custom inputs. See [Using the Concat Function in the Wizard](#using-the-concat-function-in-the-wizard) below.

* **To upper** - The uppercase value of an adapter field or custom input. This is equivalent to the **to\_upper** function in the Syntax statement.

* **To lower** - The lowercase value of an adapter field or custom input. This is equivalent to the **to\_lower** function in the Syntax statement.

* **Substring** - The substring of an adapter field or custom input. Learn [how to use the Substring Function in the Wizard](#using-the-substring-function-in-the-wizard).

* **Relation** - The value of an adapter field in a related asset, i.e., an asset related to the asset on which the Enforcement Action runs. Learn [how to use the Relation Function in the Wizard](#using-the-relation-function-in-the-wizard).

<Image alt="ActionFieldDropdown" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionFieldDropdown.png" />

### Using the Concat Function in the Wizard

The **Concat** function combines the text from multiple field values.

* No delimiters are added between the combined values.
* The values can be any valid expression as long as they resolve to strings.
* You can use the **Concat** function to assign to an action field the concatenation of one or more adapter fields, one or more custom inputs, one or more Relation fields, or a combination of adapter fields, Relation fields, and custom inputs.
* The **Concat** function requires at least two items to be joined.
* You can create a statement that nests the **Relation** function inside the **Concat** function.

**To use the Concat function in the Wizard**

1. In the dropdown that opens to the right of **Concat**, select at least two of the following to concatenate to each other:
   * **Adapter field** - For this choice, from the **Adapter** and **Select Adapter Field** dropdowns, select the adapter and adapter field to be used in the concatenation.
   * **Custom Input** - For this choice, type a string value in the Value (**Write**) box. It is possible to manually enlarge the area for writing the string and then use the vertical scroll bar to view the entire string.
   * **Relation** - For this choice, select the asset, Relationship, and Relationship adapter and field. See these field descriptions in [the Relation function description](#using-the-relation-function-in-the-wizard) below.

<Image alt="ConcatDropdown.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConcatDropdown.png" />

2. Click `+` for each additional custom input, adapter field, or relation for the concatenation.
3. To delete an item included in the concatenation configuration, click the **X** to the right of the item. It is possible to delete any or all of the items, from the third item onward. This is because a concatenation requires at least two items.

The following is an example of using the Wizard to create a statement using the **Concat** function.

<Image alt="ConcatRelationExample.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConcatRelationExample.png" />

### Using the Substring Function in the Wizard

The **Substring** function returns a substring of an adapter field or custom input, beginning from the specified start position in the string for the length specified. The values can be any valid expression as long as they resolve to strings.

**To use the Substring function in the Wizard**

1. In the dropdown that opens to the right of **Substring**, select one of the following from which to extract a substring:
   * **Adapter field** - For this choice, from the **Adapter** and **Select Adapter Field** dropdowns, select the adapter and adapter field.
   * **Custom Input** - For this choice, type a string value in the Value (**Write**) box. It is possible to manually enlarge the area for writing the string and then use the vertical scroll bar to view the entire string.
2. In **From**, type the start position in the adapter field  / custom input from which to extract the substring.
3. In **Length**, type the length of the substring to extract.

<Image alt="SubstringExample" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SubstringExample.png" />

### Using the Relation Function in the Wizard

The **relation** function in a Dynamic Value Statement fetches data from a related asset (i.e., an asset that is related to the Enforcement Center action asset via a [Relationship](/docs/exploring-connections-and-asset-relationships)) and populates Enforcement Action configuration fields (form fields) with it. This cross-asset data retrieval enhances Enforcement Actions with more context and precision.
For example, when you run an Enforcement Action on a user, you can use the **relation** function to retrieve data from an associated device based on a user-device relationship defined by a Relationship.

<Callout icon="📘" theme="info">
  Note

  The Dynamic Value Statement wizard supports using the **relation** function within the **concat** function. See [Using the Concat Function in the Wizard](#using-the-concat-function-in-the-wizard) above.
</Callout>

**To use the Relation function in the Wizard**

1. From the **Asset Type** dropdown, select the related asset type from which to pull data.
2. From the **Relationship** dropdown, select the Relationship name.
3. From the adapter dropdown, select the adapter from which to pull the field in the related asset type.
4. From the **Select field** dropdown, select the field from the related asset to be used in the Dynamic Value Statement.

<Image alt="RelationWizard" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RelationWizard.png" />

## Converting from Wizard to Syntax

You can construct a statement in the Wizard screen and then convert and view its Syntax.
Click the **Syntax** button to convert Wizard to Syntax.

<Callout icon="📘" theme="info">
  Note

  The **Syntax** button is disabled when not all fields have been filled in the Wizard. This occurs when you don't complete a statement, including the case where you didn't yet choose a module in the Enforcement Set query and therefore cannot choose an adapter field.

  <Image alt="SyntaxButtonDisabled" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxButtonDisabled.png" />

  When you save the Enforcement Set, the incomplete Dynamic Value statement is not saved.
</Callout>

## Converting from Syntax to Wizard

You can construct a statement in the Syntax screen and then convert and view it in the Wizard.
Click the **Wizard** button to convert Syntax to Wizard.

<Callout icon="📘" theme="info">
  Note

  The **Wizard** button is disabled in the following cases and a tooltip is displayed::

  * The statement is too complex to display in the Wizard.

  * The statement includes functions not supported by the Wizard.

  * Syntax was not validated successfully.

  * The statement is incomplete. For example, you did not choose a module and therefore cannot choose an adapter and adapter field.
</Callout>

## Examples

### All Statement Example

The following screen shows an *All* statement example built in the Wizard.

The **Axonius - Add Tag to Assets** action runs on Aggregated Security Finding assets that match the critical vulns query.

<Image border={false} src="https://files.readme.io/fd7ba305e643271f67764a00b7e6cfe48da949653720967fa93e2cf728919ae6-image.png" />

For each vulnerability that matches the query, the statement assigns the action field **Tag names** the first non-empty value of the following adapter fields:

* **CVE Impact Score**
* **CVSS V2 Score**
* **CVSS V3 Score**

<Image alt="ExampleAllStatement" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleAllStatement.png" />

You can click the **Syntax** button to translate the statement constructed in the Wizard to Syntax.

<Image alt="ExampleAllStatementSyntax" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleAllStatementSyntax.png" />

After saving the Enforcement Set, you can click **Simulate** from either above the **Wizard** or **Syntax** statement to [debug the statement](/docs/using-the-simulator).

### Switch/Case Statement Example 1

The following screen shows a *Switch/Case* statement example built in the Wizard.
For each vulnerability that matches the query, it checks if the **CVSS V2 Score** field in the Aggregated adapter is greater than **2** (the first condition).
If yes, the action field **Tag names** is assigned the value of the **CVSS V2 Score** adapter field.
If not, it checks if the **CVSS V2 Score** field in the Aggregated adapter is less than **2** (the second condition). If yes, the action field **Tag names** is assigned the value **0**.
If none of the conditions are met, the action field **Tag names** is assigned the value **fallback**, defined as the default value in the action configuration form.

<Image alt="ExampleSwitchStatementWizard" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleSwitchStatementWizard.png" />

You can click the **Syntax** button to translate the statement constructed in the Wizard to Syntax and validate it.

<Image alt="ExampleSwitchStatementSyntax" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleSwitchStatementSyntax.png" />

After saving the Enforcement Set, you can click **Simulate** from either above the **Wizard** or **Syntax** statement to [debug the statement](/docs/using-the-simulator).

### Switch/Case Statement Example 2

The following screen shows a *Switch/Case* example built in the Wizard.
For each device that matches the query, it checks if the **Asset Name** field in the Aggregated adapter meets the criteria listed in the first condition. If it does, the action field is assigned the value of the adapter field. If not, the next condition is checked. Once the **Asset Name** field value meets the criteria, the remaining ELSE IF conditions are not processed.

<Image alt="ExampleSwitchStatement2a" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleSwitchStatement2a.png" />

You can click the **Syntax** button to translate the statement constructed in the Wizard to Syntax and validate it.

<Image alt="ExampleSwitchStatement2aSyntax" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleSwitchStatement2aSyntax.png" />

After saving the Enforcement Set, you can click **Simulate** from either above the **Wizard** or **Syntax** statement to [debug the statement](/docs/using-the-simulator).