# Source: https://docs.axonius.com/docs/risk-score.md

# Axonius - Calculate Risk Score

**Axonius - Calculate Risk Score** calculates the Risk Score of an asset and writes the calculated value into the relevant Axonius Risk Score field for:

* Assets returned by the selected query or assets selected on the relevant asset page.

A major use case of the **Axonius - Calculate Risk Score** action is to calculate Risk Score **across assets and security findings**, namely, to calculate the Risk Score of a specific vulnerability in the context of a specific asset ("per Security Finding per Asset"). For example, you can compare the risk level of specific CVEs on a laptop with the risk level of the same CVEs on a desktop or a mobile device..

### Calculation Logic

When you run the Enforcement Action, for each asset that matches the query, the Enforcement action takes the values from the selected numeric (alternative) fields, multiplies them by their respective weight values, and completes the process by adding all the values to get a score. Similar to conditional statement behavior, when one of the fields is missing or has no value, the calculation fails entirely and that asset gets the Axonius-assigned default value 0.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Enforcement Set name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Weighted Risk Score** - The type of weighted risk score to calculate. You can choose between the following options:
  * **per Security Finding per \[Asset Name]** - This risk score calculation is based on values from either the Asset or the Security Findings fields. You must enter at least one Asset field value and one Security Finding field value.
  * **per \[Asset Name]** - This risk score is calculated on values from at least two Asset fields.
* **Score Calculation** - in this section, do the following:
  1. Click the `+` button for each additional field value that you want to include in the risk score calculation. You can include an unlimited amount of components, provided that the sum of their weights (**Total %**) is exactly 100. More selected fields means that the risk score takes more factors into consideration.
  2. Select the Axonius field whose value is used in the risk score calculation.
  3. For each risk score component, in the Adapter dropdown,  select the adapter from which to fetch the field value.
  4. Type or use the Up/Down arrows to input the **Weight %** of the selected Axonius field.

<Callout icon="📘" theme="info">
  Note

  The Total % appearing under the Weight % column must be 100. If it's above or below 100, the system warns you accordingly.
</Callout>

The following example shows a Risk Score per Security Finding per Device, calculated by the weights of three different fields: CMDB Business Applications: Crown Jewel (fetched from the ServiceNow adapter); Public IPs; and Plugins Information: VPR Score (fetched from the Tenable.io adapter).

<Image alt="RiskScoreExample" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-J2TLV55W.png" />

The field configuration from here is the same as in the main [Axonius Risk Score page](/docs/risk-score-settings). It involves assigning alternative values to fields and data normalization.[Read the full documentation about these procedures](/docs/creating-a-risk-score#assigning-alternative-values-to-fields).

## Viewing Risk Score Results

### Per Asset

1. When the Enforcement Set finishes running, view its [run history](/docs/view-ec-set-history) and click the most recent Enforcement Set run (row) to open its Run drawer.

<Image alt="CompletedActionRiskScore.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CompletedActionRiskScore.png" />

3. Click the green **Successful** link. The relevant Assets page opens, listing the assets matching the query for which the Enforcement Action succeeded to calculate the Risk Score. For each asset, the **EC: Result Details** field shows ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC-result-details-field.png)

When there are assets for which the Enforcement Action failed to calculate the Risk Score, you can click the red **Failed** link to view the assets, and see the complete error message for each one by hovering over the **EC: Result Details** field.

4. Add the calculated Risk Score column to the table on the Assets page: select **Edit Table `>` Edit Columns**, and from the fields that appear, add the **Axonius Risk Score** field (refer to [ Changing Columns Display](/docs/setting-page-columns-display#changing-columns-displayed) to learn more).

<Image alt="AddRiskScoreField.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddRiskScoreField(1).png" />

The table on the Assets page now displays  the **Axonius Risk Score** column.

<Image alt="RiskScoreResults.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RiskScoreResults(1).png" />

### Per Security Finding per Asset

1. Repeat steps 1-2 as explained [above](/docs/risk-score#per-asset).
2. On the relevant Assets page, select an asset.
3. On the Asset's Profile page, from the left navigation panel, expand the **Tables** section and select **Security Finding Instances**.
4. The Security Finding Instances table opens, displaying the **Axonius Risk Score** field for each vulnerability detected on the asset.

<Image alt="Results" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VMBDN8KH.png" />

<Callout icon="📘" theme="info">
  Note

  The results for *per Security Finding per Device* Risk Score are also available from the **Security Finding** table on the Device's Profile page. This option is only available for Device assets.
</Callout>

## Editing Enforcement Actions in a Risk Score

After creating Risk Score Enforcement Sets, you can edit them and add more actions and advanced configurations as in any Enforcement Set.[See detailed explanation here](/docs/editing-enforcement-actions-in-a-risk-score).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).