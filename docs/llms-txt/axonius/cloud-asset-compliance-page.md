# Source: https://docs.axonius.com/docs/cloud-asset-compliance-page.md

# Cloud Asset Compliance Page

Use the **Cloud Asset Compliance** page to compare cloud configuration and asset data against industry benchmarks and frameworks.
The following compliances are supported:

* CIS Amazon Web Services Foundations Benchmark v3.0
* CIS Amazon Web Services Foundations Benchmark v1.4
* CIS Amazon Web Services Foundations Benchmark v1.3
* CIS Amazon Web Services Foundations Benchmark v1.2
* CIS Microsoft Azure Foundations Benchmark v1.1
* CIS Microsoft Azure Foundations Benchmark v1.4
* CIS Microsoft Azure Foundations Benchmark v2.0
* CIS Oracle Cloud Infrastructure Foundations Benchmark v1.0
* CIS Google Cloud Platform Foundations Benchmark v1.1

Cloud Asset Compliance calculations are done as part of your discovery cycle using the  existing relevant adapter configuration.
The following adapters may need configuration of additional permissions or APIs:

* [Amazon Web Services](/docs/aws-adapter-configuration-for-cloud-asset-compliance)
* [Google Cloud Platform](/docs/gcp-configuration-for-cloud-asset-compliance)

To open the **Cloud Asset Compliance** page, click the Cloud Compliance icon on the left navigation panel.

<Image align="center" alt="CloudComplianceCenter3.png" border={false} width="900px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudComplianceCenter3.png" />

<br />

## Viewing Benchmark Results

To view benchmark results, first select the relevant benchmark from the **Compliance** dropdown. The following versions are available. You can select a different version as relevant from [Configure Benchmarks](/docs/cloud-asset-compliance-page#calculating-a-difference-benchmark-version).
You can select between:

* CIS Amazon Web Services Foundations Benchmark v3.0
* CIS Amazon Web Services Foundations Benchmark v1.4
* CIS Amazon Web Services Foundations Benchmark v1.3
* CIS Amazon Web Services Foundations Benchmark v1.2
* CIS Microsoft Azure Foundations Benchmark v1.1
* CIS Microsoft Azure Foundations Benchmark v2.0
* CIS Oracle Cloud Infrastructure Foundations benchmark v1.0
* CIS Google Cloud Platform Foundations Benchmark v1.1

The total number of recommendation controls for the benchmark is displayed on the top left side of the table:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Controls.png)

All benchmark controls (rules) are displayed for each account.
The following columns are displayed for each control:

* **Status** - contains the following values:

  * Passed ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(483\).png) - The account passed this benchmark control.

  * Excluded ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExcludeColor\(2\).png) - The account has an exclusion control.

  * Failed ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(484\).png) - The account failed this benchmark control.

  * Error ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(485\).png) - Unable to check the benchmark control, usually due to lack of permissions. Error details are displayed in the **Control Details Drawer** under the **Error** section.

  * Not Available ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/grey_dot\(1\).png) - The control didn't yet calculate.

* **Section** - The number of the control in the benchmark.

* **Comments or Exclusions** - If you exclude controls (rules) or make comments, an icon is displayed in this column. Hover over the icon to see the details about the exclusion or comment.

<Image alt="Rule_Exclusions" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rule_Exclusions.png" />

* **Control** - The name of the control in the benchmark.
* **Category** - The category of the control in the benchmark.
* **Profile Applicability** - Displays whether the CIS control is:

  * **Level 1** — base recommendation that can be implemented relatively quickly and with minimum performance impact

  OR

  * **Level 2** — higher level of security, but might have an adverse impact on your organization if incorrectly implemented
* **Account** - The account for which this control was checked.
* **Failed Results** and **Passed Results** - The number of checked entities for this control and the number of entities that failed/passed this control.

  * For example, in control **4.1 Ensure no security groups allow ingress from 0.0.0.0/0 to port 22** (part of the CIS AWS Foundations Benchmark v1.2), the AWS entity that is checked is Security Groups. If there are five Security Groups and two of them allow ingress from 0.0.0.0/0 to port 22, then the **Passed Results** column will display **2** and the **Failed Results** column will display **3**.
* **Noncompliant Assets** - The noncompliant assets related to the failed results that were identified.

### Calculating a Different Benchmark Version

By default, a new system displays the most recent version of the benchmark version. You can choose to work with a previous version.

<Callout icon="📘" theme="info">
  Note

  If you are upgrading from a previous Axonius version, the older existing compliance version is displayed by default when you upgrade to a new Axonius system. You can choose to work with a newer compliance version. When you move versions, any comments or exclusions you may have configured are not moved to the new version.
</Callout>

**To work with a different version**

1. Select **Actions**.

<Image alt="CloudActions.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudActions.png" />

2. Select **Configure Benchmark**. The **Configure Benchmark** dialog opens.

<Image alt="BenchmarkDropdownN.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BenchmarkDropdownN.png" />

3. Select the Benchmark version you want, for instance  **CIS AWS Foundations Benchmark v1.4**. The system asks you to confirm your choice, as comments or exclusions that you have configured for a specific benchmark version aren't moved between benchmark versions and are only saved under the benchmark version where they were created.

4. Click **Change Benchmark Version** to implement your choice.

## Control Details Drawer

Click a control to open the **Control Details** drawer, which  displays more detailed information.

<Image align="center" alt="ControlDetailsDrawer2" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ControlDetailsDrawer2.png" />

The **Control Details** drawer contains all information in the table (mentioned above). In addition, it also contains  the following detailed information:

* **Description** - Detailed description on the control, what it means, and why it matters.
* **Remediation** - Full remediation instructions, which is useful if this control has failed the compliance check.
* **Failed Results** *(Relevant only for controls with Failed status)* - Detailed results on the failed entities. For example, in control 1.2 "Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password (part of the CIS AWS Foundations Benchmark v1.2)" - the Failed Results section will present the IAM Users that don't have MFA enabled.
* **Exclusions and Comments** - Exclusions and Comments  that were added to this control for the relevant accounts, and the capability to add, edit and delete Exclusions and Comments.
* **Error** *(Relevant only for controls with NoData status)* - Detailed error message why the control wasn't checked.
* **CIS Controls** - Matching CIS Controls for this benchmark control.

Each detailed information can be expanded or collapsed.

## Show Noncompliant Assets

For certain failed controls, the **Show Noncompliant Devices/Users** button is visible, showing the number of affected assets. When no affected devices or users are displayed because the system doesn`t currently support the failed control, the **Information** icon displays a message that the specific control doesn`t currently support noncompliant assets.

When clicking **Show Noncompliant Assets**, you are redirected to the Device/Users page, which displays all assets affected by this control.

For example, in control **4.1 Ensure no security groups allow ingress from 0.0.0.0/0 to port 22** (part of the CIS AWS Foundations Benchmark v1.2): If the control found that two Security Groups (AWS entities) failed, when clicking  **Show Affected Devices/Users**, it will display in the Devices page all EC2 machines (assets) that are part of security groups that allow ingress from 0.0.0.0/0 to port 22.

* For the **CIS Amazon Web Services Foundations Benchmark v3.0**:

  * The following controls (when failed) will contain **Show Affected Users**:

    * '1.4', '1.5', '1.6', '1.10', '1.12', '1.13', '1.14', '1.15'
  * The following controls (when failed) will contain **Show Affected Devices**:

    * '2.1.2', '2.1.4', '2.3.1', '3.4', '3.8', '3.9', '5.2', '5.4'

* For the **CIS Amazon Web Services Foundations Benchmark v1.4**:

  * The following controls (when failed) will contain **Show Affected Users**:

    * 1.4,  1.5, 1.6,  1.7, 1.10, 1.12, 1.13, 1.14, 1.15
  * * The following controls (when failed) will contain **Show Affected Devices**:
    * 2.1.3, 2.1.5, 2.3.1, 3.3, 3.6,  3.10, 3.11, 5.2, 5.3

* For the **CIS Amazon Web Services Foundations Benchmark v1.3**:

  * The following controls (when failed) will contain **Show Affected Users**:
    1.4, 1.5, 1.6, 1.7,  1.10, 1.12, 1.13, 1.14, 1.15,

  * The following controls (when failed) will contain **Show Affected Devices**:
    1.20, 3.3, 3.6, 3.11, 5.2, 5.3.

* For the **CIS Amazon Web Services Foundations Benchmark v1.2**:

  * The following controls (when failed) will contain **Show Affected Users** - 1.1, 1.2, 1.3, 1.4, 1.12, 1.13, 1.14, 1.16, 1.22

<Callout icon="📘" theme="info">
  Note

  In order to show affected IAM Users, **Fetch information about IAM Users** needs to be enabled in the **AWS Configuration** in the **Advanced Settings** for the AWS adapter. See [AWS Adapter Configuration for Cloud Asset Compliance](/docs/aws-adapter-configuration-for-cloud-asset-compliance).
</Callout>

* The following controls (when failed) will contain **Show Affected Devices** - 2.3, 2.6, 4.1, 4.2, 4.3

<Callout icon="📘" theme="info">
  Note

  In order to show affected S3 Buckets, **Fetch information about S3** needs to be enabled in the **AWS Configuration** in the **Advanced Settings** for the AWS adapter. See [AWS Adapter Configuration for Cloud Asset Compliance](/docs/aws-adapter-configuration-for-cloud-asset-compliance).
</Callout>

* For the **CIS Google Cloud Platform Foundations Benchmark v1.1**:

  * The following controls (when failed) will contain **Show Affected Users** - 1.1, 1.5, 1.6
  * The following controls (when failed) will contain **Show Affected Devices** - 3.1, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.9, 5.1, 5.2, 6.1.2, 6.2.1, 6.2.2, 6.2.3, 6.2.4, 6.2.6, 6.2.7, 6.3.1, 6.3.2, 6.4, 6.5, 6.6, 6.7

* For the **CIS Microsoft Azure Foundations Benchmark v1.1**:

  * The following controls (when failed) will contain **Show Affected Users** - 1.3
  * The following controls (when failed) will contain **Show Affected Devices** - 6.1, 6.2, 7.1, 7.2

* For the **CIS Microsoft Azure Foundations Benchmark v1.4**:

  * The following controls (when failed) will contain **Show Affected Devices** - 6.1, 6.2, 6.6
  * The following controls (when failed) will contain **Show Affected Users** - 1.3

* For the **CIS Microsoft Azure Foundations Benchmark v2.0**:

  * The following controls (when failed) will contain **Show Affected Devices** - 6.1, 6.2, 7.2
  * The following controls (when failed) will contain **Show Affected Users** - None for Affected users

* For the **CIS Oracle Cloud Infrastructure Foundations Benchmark v1.0**:

  * The following rules (when failed) will contain **Show Affected Users** - 1.11, 1.13
  * The following rules (when failed) will contain **Show Affected Devices** - 2.1, 2.2, 2.5

### Noncompliant CIS AWS Foundations field

All affected assets (devices/Users) will contain a complex field.

* The field name for assets affected from the CIS Amazon Web Services Foundations Benchmark is named **Noncompliant CIS AWS Foundations**.
  This field will contain all failed benchmark rules for the specified asset.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(495\).png)

  This field can also be queried in the Query Wizard.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(496\).png)

### Noncompliant CIS Google Cloud Platform Foundations field

All affected assets (devices/users) contain a complex field.

* The field name for assets affected from the CIS Google Cloud Platform Foundations Benchmark is named **Noncompliant CIS Google Cloud Platform Foundations**.
  This field will contain all failed benchmark controls for the specified asset.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1797\).png)

  This field can also be queried in the Query Wizard.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1798\).png)

### Noncompliant CIS Azure Foundations field

All affected assets (devices/users) contain a complex field.

* The field name for assets affected from the CIS Microsoft Azure Foundations Benchmark is named **Noncompliant CIS Azure Foundations**.
  This field contains all failed benchmark controls for the specified asset.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1346\).png)

  This field can also be queried in the Query Wizard.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1347\).png)

### Noncompliant CIS Oracle Cloud Foundations field

All affected assets (devices/users) contain a complex field.

* The field name for assets affected from the CIS Microsoft Oracle Cloud Foundations Benchmark is named **Noncompliant CIS Oracle Cloud Foundations**.
  This field contains all failed benchmark controls for the specified asset.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1474\).png)

  This field can also be queried in the Query Wizard.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1475\).png)

## Adding Comments and Excluding Rules

Use the **Exclusions and Comments** pane to add comments and exclude rules.

[Excluding Controls](/docs/cloud-asset-compliance-page#Excluding-Controls)
[Adding Comments](/docs/cloud-asset-compliance-page#Adding-Comments)

### Excluding Controls

You can exclude controls from being included when cloud compliance runs. You can exclude a control on a single account, or on all accounts. Excluded controls won't be calculated on the selected accounts as part of the benchmark score.
**To exclude a control**

1. Click the relevant control. The Control Details drawer opens.

2. In the **Exclusion and Comments** pane, select **Exclusion**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewExlusionpane.png)

3. Specify a name or explanation for the exclusion.

4. From the **Select Account** dropdown, select a specific account you want to exclude, or select **All** to exclude this control from all accounts.

5. Click **Add**. If prompted to confirm, click **Yes**. The control is added to the **Exclusion and Comments** list in this section.  Each row displays when the list was last updated and by whom.

   <Image alt="ExclusionsAdded.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExclusionsAdded(1).png" />

* Editing an exclusion: Click   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1349\).png) (**Edit**) to edit an existing exclusion. When done, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1350\).png)  to save the changes.
* Deleting an exclusion: Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1351\).png) (**Delete**)   to delete an exclusion.

### Adding Comments

Use the Comments section in the drawer to add comments on benchmark results so anybody looking at the results can understand the full context. You can add a comment to a single account or to all accounts.

**To add a comment**

1. Click the control. The Control Details drawer opens.
2. In the **Exclusion and Comments** section, select **Comment**.

<Image alt="AddingaComment.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddingaComment.png" />

4. Enter a comment.

5. From the **Select Account** dropdown, select the accounts you want to add the comment to. Click **All** to add the comment to all accounts, making it a general comment for this control. Comments are only visible for the relevant filtered accounts.

<Image alt="comment 2.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/comment%202.png" />

6. Click **Add**. The rule is added to the **Exclusion and Comments** list in this drawer.  The list shows who last updated this exclusion and when.

   * Editing a comment: Click  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1349\).png) (**Edit**) to edit an existing comment. After making the required changes, click the check icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1350\).png)  to save the changes.
   * Deleting a comment: Click  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1351\).png) (**Delete**) to delete a comment. If a Confirm prompt appears, click **Yes**.

     <Image align="center" alt="editing and deleting.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/editing%20and%20deleting.png" />

## CIS Benchmark Scoring

A benchmark score is displayed according to the results. The score can be for all connected cloud provider accounts, or for one or more accounts.

<Image alt="CISBenchmarkScore.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CISBenchmarkScore.png" />

The CIS Benchmark score is calculated as the percentage of passed controls out of all controls selected in the Configure Benchmark dialog. The score is calculated and aggregated on all accounts currently filtered. Other filters will not affect the CIS benchmark score.

The score component also has an option to exclude controls from the benchmark score by clicking **Actions** `>` **Configure Benchmark**, located on the top right of the score component.
You can select/clear controls for the benchmark. These controls aren't subsequently shown in the table and aren't taken into account when calculating the benchmark score.

<Image alt="Configure_Benchmark2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Configure_Benchmark2.png" />

The color of the score is defined as follows:

* Score less than 50 - red
* Score  greater than 50 and less than 70 - orange
* Score greater than 70 - green
* No score - ‘Not Available’ in gray

Hover over the clock icon to see the time last updated. This is displayed when the fetching stage is complete and all data from all the rules is calculated. This score is displayed until the next fetch cycle and calculation are complete.
When adapters aren't connected, or the first fetch or calculation is in progress, the Benchmark score is shown as ‘Not Available’ in gray.

## Filtering

* You can filter on the values to be displayed in the table. All filters apply on the CSV when exporting or when sending compliance result by email.
* The following filters are available:

  * **Account** - When you have multiple AWS, GCP, Azure or Oracle accounts, you can filter and select one or more accounts. All rules will be displayed for each of the selected accounts.

    <Image alt="AccountsDropDown.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AccountsDropDown.png" />

  * **Control** - Display only certain benchmark controls.

    <Image alt="CloudControls" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudControls.png" />

  * **Category** - Display only selected categories.

    <Image alt="CloudCat.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudCat.png" />

  * **Status** - Display  controls by Status: Excluded, Failed, Not Available or Passed.

  * **Profile Applicability** - Display CIS benchmarks by Profile Applicability level: Level 1 (basic security requirements) or Level 2 (enhanced security requirements).

  * **Display by Date** - Show the benchmark for a specific date.

## Aggregated View

* You can view all results in an aggregated view by enabling the **Aggregated View** switch.

* When **Aggregated View** is enabled, it shows aggregates results and affected assets across all accounts currently filtered and displays the aggregated results per control.

* When **Aggregated View** is disabled, results and affected assets are shown per each account per control.

## Exporting Benchmark Results to CSV

You can export the benchmark results table data to a CSV file.
**To export the results to a CSV file**

* In the **Cloud Asset Compliance** page, click **Export CSV** on the right side of the page just above the table.
  The CSV file is automatically downloaded.

  * Name format: *axonius-data*\< date >T\< time >UTC.csv\_
  * For example: *axonius-data\_2020-04-13T07-18-41UTC.csv*

## Enforce

The **Enforce** menu lets you take various actions on the benchmark results table data.
For more details on the various actions, see [Cloud Asset Compliance - Enforcement Actions](/docs/cloud-asset-compliance-enforcement-actions-overview).

<Callout icon="📘" theme="info">
  Note

  **[Axonius Security Policy Enforcement Center](/docs/ec-overview)** is required to enforce actions for cloud assets.
</Callout>

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).