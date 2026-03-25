# Source: https://docs.axonius.com/docs/creating-a-risk-score.md

# Creating a Risk Score

Learn how to create and manage risk scores for assets in Axonius, including setting parameters, assigning values, and defining risk levels.

The left navigation panel of the **Axonius Risk Score** page lists all assets to which you have created at least one Risk Score. Under each asset type, all Risk Scores defined for this asset are listed.

**To add new Risk Score:**

1. From the left navigation panel, click **+ Add Asset**.
2. Choose an asset type from the dropdown and click **Add Asset**. You can only add a single asset type at a time.
   If there are already Risk Scores defined for this asset type, the new Risk Score will be added under the relevant asset type in the left navigation panel.
   You can also click `+` next to the relevant asset type to add a new Risk Score to it.

   <Image alt="AddAssetRiskScore" border={false} src="https://files.readme.io/c556d7c753d548adb84f5d60e89e8b1c16b32d6221dfab474da1c4a01bd8d4df-image.png" />

   <br />
3. Under **Action Name**, enter a name for the Enforcement Action that runs when calculating this Risk Score. The name must be unique.

<Callout icon="📘" theme="info">
  Note

  At this point, the Risk Score's name is something generic such as "Calculate Risk Score 1". You can rename it after saving the Risk Score.
</Callout>

## Selecting Parameters

1. From the **Select Query** dropdown, select the specific assets this Risk Score applies to.
2. Under **Weighted Risk Score**, select whether to calculate Risk Score *per \[Asset Name]* or per *Security Finding per \[Asset Name]*.
   * *per Asset* - This Risk Score is calculated for the selected assets only, and is based on values from at least two parameters. The results are written into the **Axonius Risk Score** field on the relevant Assets Page.
   * *per Security Finding per Asset* - This Risk Score is calculated for a specific vulnerability in the context of a specific asset.

<Accordion title="Guidelines for calculating per Security Finding per Asset Risk Score" icon="fa-info-circle">
  <Callout icon="💡" theme="warn">
    When calculating a *per Security Finding per Asset* Risk Score:

    * The query selected must include at least one asset that has an associated vulnerability.

    * We strongly recommend to include at least one Axonius field from the Security Findings module and not from the asset itself. Otherwise, the calculation might fail or provide false results.
      * The Security Findings field should include attributes related to the vulnerability itself - CVE Severity, CVSS Score, etc.

    * The Risk Score result is written simultaneously into the following pages and fields:
      * On the Assets page, the Risk Score appears under the **Security Findings Instances: Axonius Risk Score** field, available from the Security Findings Instances table.
      * On the Security Findings page, the Risk Score appears under the **Axonius Risk Score** field. This refers to the risk score of the asset itself, and since each Security Finding represents a specific vulnerability on a specific asset, it is the same as the *per Security Finding per Asse* Risk Score.

    See [Viewing Risk Score Results](https://docs.axonius.com/axonius-help-docs/docs/viewing-risk-score-results) for detailed instructions on how to view the calculation results from each Assets page.
  </Callout>
</Accordion>

3. Under **Score Calculation**, select the parameters you want to include in the score calculation. Click `+` to add more parameters. You can include an unlimited number of parameters (two is the minimum), provided that the sum of their weights (**Total Percentage**) is exactly 100. The more parameters included, the more factors the Risk Score takes into consideration. There are two possible types of parameters:
   * **Asset Field** - Select a specific Axonius field to use in the calculation. For example (for Devices): Host Name, Last Seen, Total CVE Count, etc. Then, from the **Adapter** dropdown, select the adapter from which to fetch the field value.
   * **Query Condition** - This parameter is calculated based on the existence or absence of the asset from a specific query. The logic is as follows: If the asset exists in the selected query, assign Value A; Else, assign Value B. Select a query from the dropdown or click **+ Add Query** to create a new query.
4. For each parameter, under the **Weight** column, type or use the Up/Down arrows to set the percentage of this parameter in the Risk Score calculation.

<Callout icon="📘" theme="info">
  Note

  The Total % appearing under the Weight % column must be 100. If it's above or below 100, the system warns you accordingly.
</Callout>

The following example shows a Risk Score per Security Finding per Device, calculated by the weights of three different Axonius fields: CMDB Business Applications: Crown Jewel (fetched from the ServiceNow adapter); Public IPs; and Plugins Information: VPR Score (fetched from the Tenable.io adapter).

<Image align="center" alt="RiskScorePerSFPerDeviceExample" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/RiskScore_per%20sf%20per%20device_example.png" />

## Assigning Alternative Values to Parameters

All parameters added to the Risk Score require defining the following:

* At least one alternative value, that will be assigned to them as a Risk Score in case their values meet or do not meet specific conditions. For example, fields with non-numeric values must be assigned at least one numeric value.
* At least one fallback value - a default value to be assigned in case none of the conditions are met.

To complete this process, click **Add Alternative Value** (see previous image) under the field row **or** the Edit icon ![EditIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MTYHUDUH.png).

The process of assigning alternative values to parameters differs between numeric and non-numeric fields.

### If the field has a non-numeric value:

1. Fill in the IF row (the first condition) to assign a numeric value to the field.
2. Optionally, click `+` to add more ELSE IF conditions.
3. In the bottom ELSE section, enter a fallback value.
4. Click **Apply**.

For example, if we add the CVE Severity field, we can define the following alternative values:

* If this field's value is either CRITICAL or URGENT, the Risk Score will be 10.
* If this field's value is HIGH, the Risk Score will be 8.
* If this field's value is anything else, the Risk Score will be 5.

<Image alt="AlternativeValue" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1AGOGZSA.png" />

<Callout icon="📘" theme="info">
  Notes

  1. Defining the conditions is done using standard Axonius query operators. The available operators change according to the field type - string, boolean, enum, etc. For example, if the selected field is Software Name, the condition row contains additional operators such as "starts" and "ends".
  2. In case a single field has multiple values, the calculation assigns the numeric values according to the order in which the conditions were set. Therefore, based on the previous example, if we have a Severity field that contains both CRITICAL and HIGH severities, its numeric value will be 10, because the CRITICAL condition appears first.
</Callout>

This logic also applies to **Query Conditions**: assign numeric values to use in the calculation in case the asset exists or doesn't exist in the query. Then, click **Apply**.

<Image align="center" alt="query condition" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/RiskScore_QueryCond.png" />

### If the field has a numeric value:

<Callout icon="📘" theme="info">
  Note

  This section does **not** apply to Query Conditions.
</Callout>

When the field has a numeric value (for example - CVSS Score, Device Count, etc.), an additional section titled **Choose Value** appears in the Alternative Value wizard. In this section, fill in the following fields:

1. **In case of multiple values, choose which one you want to display** - Some fields might have multiple values, for example, if their values are fetched from multiple adapters. In this case, choose which value you want to use in the calculation: the Maximum (default) or Minimum.
2. **(Optional) Select an operator (× or ÷) and enter a value to adjust the Risk Score** - Select an operator (Multiply or Divide) and enter a value to adjust the Risk Score by it. For example - divide the value by 10. This is useful when fields have very high values (100, 1000, etc.) or non-integer values, which might complicate the calculation. In these cases, you might prefer to normalize the data and work with more convenient numbers.

<Accordion title="Example - Normalizing Numeric Values" icon="fa-info-circle">
  1) Assume we want to normalize the Not Fetched Count field as follows: display the maximum value in case of multiple values, and divide the value by 10:

  <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-O359ESMV.png" width="600px" alt="DataNormalization" />

  2. Assume that the Not Fetched Count field has the following values: 20, 30, and 50. According to what was defined under **Choose Value**, the assigned Risk Score will be 5: the calculation mechanism takes the maximum value (50) and divides it by 10.
  3. After normalizing the data, proceed to the **Alternative Value** section of the wizard and define conditions and a fallback value, as explained previously.

     * For example: define that if the normalized value is smaller than 10, the Field Value will be used as the Risk Score. In any other case - when the value equals to or larger than 10 - an alternative Risk Score of 7 will be assigned.

     <br />

     <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-AX6KYV7P.png" width="650px" alt="FullWizard" />
  4. Since 5 is smaller than 10, the Field Value 5 will indeed be the Risk Score.

  Note that the conditions defined in this section are checked against the values defined in the previous step. For each condition, select whether to use the Field Value (as defined under **Choose Value**), or set a different value.
</Accordion>

### Field-Based Fallback Conditions

<Callout icon="📘" theme="info">
  Note

  This section does **not** apply to Query Conditions.
</Callout>

The previous examples demonstrated how to configure numeric fallback values - **Value**-type fallbacks. However, you can also configure up to 2 **Field**-type fallbacks. The system will check these two fields sequentially, until it reaches the correct field value to use. If none of the fields matches the condition, a final **Value**-type fallback must be assigned.

<Callout icon="📘" theme="info">
  Note

  While you can configure up to 2 field-based fallbacks, you can only configure a single numeric fallback value for each condition.
</Callout>

To summarize the two possible flows:

<Tabs>
  <Tab title="Flow 1 - Value-type Fallback">
    1. The system checks the value of the calculation field defined.
    2. If the value doesn't match the required condition(s), the system assigns this field a defined numeric value.
  </Tab>

  <Tab title="Flow 2 - Field-type Fallback">
    1. The system checks the value of the calculation field defined.
    2. (Optional) If the value doesn't match the required condition(s), the system checks **the value of a second field**.
    3. (Optional) If the value doesn't match the required condition(s), the system checks **the value of a third field**.
    4. If the value doesn't match the required condition(s), the system assigns this field a defined numeric value.
  </Tab>
</Tabs>

**Example for Flow 2 - Field-type Fallback**

We want to use a Security Finding's **CVSS V4 Score** field value in the Risk Score calculation. However, this field doesn't necessarily have values for all Security Findings. Instead of setting a numeric fallback value straight away, we can set the system to move on and check the value of the **CVSS V3 Score** field. This field also doesn't necessarily have values for all Security Findings, so we can set the system to move on and check the value of the **CVSS V2 Score** field.
In case none of these fields have appropriate values, we will set a final, numeric fallback value to use in the calculation.

1. Click **Edit Risk Score** next to the field's row to start the process:

   <Image alt="EditRiskScoreButton" border={false} src="https://files.readme.io/8c9cd73625177bdfaccd075186902251ef8a9a7f2db54be1cbe07666a58f5ea9-image.png" />

   <br />
2. Set one or more conditions for the **CVSS V4 Score** field:

<Image alt="Fallback2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Z5D5VXAI.png" />

3. From the **ELSE** dropdown, select **Field**:

<Image alt="Fallback3" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VLEGSOM7.png" />

4. Select the **CVSS V3 Score** field and set a condition for it:

<Image alt="Fallback4" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-HNFMZD2Z.png" />

5. From the next **ELSE** dropdown, select **Field**. Then, select the **CVSS V2 Score** field and set a condition for it:

<Image alt="Fallback5" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MZYZZV13.png" />

6. You've reached the maximum number of fields that can be set. The final **ELSE** dropdown only allows you to select **Value** and set a numeric value. This step is mandatory to complete the process.

<Image alt="Fallback6" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-0KTUYGLR.png" />

7. Click **Apply** to save your changes.

**Important notes:**

* Each step can contain multiple conditions. Click `+` to add expressions for each step.

<Image alt="Fallback7" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-YIAH2SLE.png" />

* To have the system use the field value instead of a custom value, click **Reset score value**.

<Image alt="Fallback8" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MK3PDO5N.png" />

* If the field has a numeric value, you can normalize its data using operators, as demonstrated [previously](/docs/creating-a-risk-score#if-the-field-has-a-numeric-value). Click **Normalize risk score** to display the **Choose Value** dialog.

<Image alt="Fallback9" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-9QON0DFS.png" />

<Image alt="Fallback10" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DOJT19ZO.png" />

* If the field has a non-numeric value, the **Normalize risk score** won't be available, and you will only need to assign it a custom numeric value.

<Image alt="Fallback11" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-32LGVU09.png" />

You can come back to each calculation field and edit its Alternative Value configurations by clicking the Edit ![EditIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MB6Y4L4H.png) icon.

## Defining Risk Levels

Axonius divides ranges of Risk Scores into levels. A **Risk Level** is a translation of a Risk Score's numeric value to one of the following strings: Low, Medium, High, or Critical. For example, Axonius' default settings are that Risk Scores between 0.01 and 3.99 are **Low** level; Risk Scores between 4 and 6.99 are **Medium** level; and so on.

The **Risk Level** section is available at the bottom of the Risk Score page, right after selecting parameters.

Each Risk Level row contains two fields. The left field represents the lowest number in the range and the right field represents the highest number in the range. The ranges are set to the Axonius default, but you can change them according to your needs.

<Callout icon="🚧" theme="warn">
  **Note**

  The **Risk Level** field is **not** automatically populated for old Risk Scores (created before the introduction of Risk Levels). To apply Risk Levels on these Risk Scores, you must open, save, and run each of them at least once. Alternatively, you can [save your custom Risk Levels as default](https://docs.axonius.com/docs/creating-a-risk-score#/saving-custom-risk-levels-as-default) and apply them on both existing and new Risk Scores from the **Risk Score Settings** page.
</Callout>

<Image alt="risk levels1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/risk%20levels1.png" />

### Guidelines for Defining Risk Levels

* The left field of the **Low** level row always has the value 0.1 and can't be edited.
* Each left field automatically receives its value from the right field on the previous row, so no gap between the ranges is possible.
  * For example, if the value of the right **Low** field is 4.5, then the value of the left **Medium** field is set to 4.51; if you change the value of the right **Low** field to be 4.51, then the value of the left **Medium** field changes to 4.52.

<Image alt="risk levels4" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/risk%20levels4.png" />

* The right field of the **Critical** level row always has the value *infinity*; so, in fact, the range of the **Critical** level is driven by the ranges of the former levels and doesn't need to be manually set.
* To return to the Axonius default settings, click **Reset to Levels Default**.
* To save the custom Risk Score ranges you defined, you must save your changes before exiting the page. Otherwise, the ranges and levels will be reset to the Axonius default.

<br />

<Callout icon="📘" theme="info">
  **Note**

  When the Risk Score Level results in 0 in the final calculation, the value of **Axonius Risk Level** is None.
</Callout>

### Saving Custom Risk Levels as Default

To avoid defining custom Risk Levels for every new Risk Score created, you can save the custom ranges you defined as default.

1. Click **Risk Score Settings** from the top right corner of the page.

<Image alt="risk levels5" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/risk%20levels5.png" />

2. Edit the default ranges according to the [guidelines](https://docs.axonius.com/docs/creating-a-risk-score#/guidelines-for-defining-risk-levels).
3. Select whether to apply this default only on future Risk Scores, **or** on both existing and new Risk Scores.
4. Click **Save**.