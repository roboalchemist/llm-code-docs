# Source: https://docs.acceldata.io/documentation/rules-and-rulesets.md

# Rules and Rule Sets

In ADOC, **Rules** and **Rule Sets** help ensure your datasets meet business data quality standards. Rules define specific checks on data, and Rule Sets group multiple rules for easy application, scheduling, and monitoring.

## What Are Rules?

A **Rule** is a **specific condition or check** that data must meet to be considered accurate, complete, and reliable. Each rule focuses on a particular aspect of data quality, such as null values, uniqueness, value ranges, patterns, or schema compliance.

**Key Points**:

- Rules are **tag-based**. They only apply to assets with matching tags.
- A rule **cannot be applied directly** to a data source; it must be part of a Rule Set.
- Rules can be created, edited, duplicated, or deleted.

**Example:**  A `Customer Email Validation` rule might include:

- **Rule Type**: Null Check
- **Description**: Ensure `customer_email` is not empty
- **Tag**: `CustomerData`

## What Are Rule Sets?

A **Rule Set** is a **collection of rules** that are applied together to a dataset or asset.

- Rule Sets allow multiple rules to run as a batch.
- Applying a Rule Set automatically **generates policies** for monitoring.
- Rule Sets can be scheduled for repeated execution.
- Rules inside a Rule Set are executed together; policies track which rules pass or fail.

**Example:** Rule Set: `Customer Data Quality Checks`

- Rules Included:
    - `Customer Email Validation` (Null Check)
    - `Customer ID Uniqueness` (Duplicate Row Check)
    - `Customer Phone Validation` (Pattern Match)

- The above rules are then applied to all assets tagged `CustomerData`.

## Creating a Rule

### Step 1: Start Rule Creation

1. Navigate to **Data** **Reliability -&gt; Manage Policies -&gt;** **Rules / RuleSets** from the left menu.
2. Click **Create Rule**.

Note Users with `view-only` permissions cannot create rules or rule sets.

### Step 2: Configure Rule Details

| **Field** | **Description** | **Example** | 
| ---- | ---- | ---- | 
| Name | Unique name for the rule | `Customer_Email_Validation` | 
| Description | Optional explanation | `Checks for missing or invalid emails` | 
| Rule Type | Type of check | Null Check, Enumeration, Schema Match | 
| Tags | Tags matching qualifying assets | `CustomerData` | 
| Tag Match Condition | How multiple tags are matched | All / Any | 


**Tag Match Example**:

- **All**: Only assets matching all tags are evaluated.
- **Any**: Assets matching at least one tag are evaluated.

### Step 3: Save the Rule

Click **Save**. 

The rule now appears in the **Rules Table**.

## Rules Table Overview

| **Column** | **Description** | 
| ---- | ---- | 
| Rule Name | Name of the rule | 
| Type | Type of rule | 
| Details | Tags used in the rule | 
| Last Updated | Date and time of last update | 
| Rule Sets | Number of rule sets containing this rule (clickable) | 
| Policies | Number of policies using this rule | 
| Created By | Email of the creator | 
| Delete / Ellipsis Menu | Options to Delete, Edit, Duplicate, Add to Rule Set, or View Rule Sets | 


## Creating a Rule Set

### Step 1: Start Rule Set Creation

1. Navigate to   **Data** **Reliability -&gt; Manage Policies -&gt;** **Rule/Rule Sets -&gt; Rule Sets** tab.
2. Click **Create Rule Set**.

### Step 2: Configure Rule Set Details

| Field | Description | Example | 
| ---- | ---- | ---- | 
| Name | Unique name for the Rule Set | `Customer Data Quality Checks` | 
| Category | Policy type for grouping | Customer Data | 
| Rules | Rules to be included in this set. Use the search bar to select rules that have already been included previously. | `Customer Email Validation`, `Customer ID Uniqueness` | 


### Step 3: Save the Rule Set

Click **Save**. 

The Rule Set now appears in the **Rule Sets Table**.

## Rule Sets Table Overview

| Column | Description | 
| ---- | ---- | 
| Rule Set Name | Name of the rule set | 
| Category | Policy type | 
| Last Updated | Date and time of last update | 
| Rules | Number of rules in the set | 
| Policies | Number of policies using the set | 
| # of Schedules | Number of schedules for this set | 
| Created By | User who created the set | 
| Delete / Ellipsis Menu | Options: Edit, Duplicate, Apply, Schedule, View Rules, View Schedules | 


## Importing a Rule Set

1. Click **Import Rule Set**.
2. Drag-and-drop a `.zip` or `.gz` file or browse your system.
3. Handle duplicates:
    - **Override**: Replace existing Rule Set
    - Do Not Import: Skip duplicates

4. Click **Next** and wait for import to complete.

Note If **Do Not Impor**t is selected, no duplicates are imported.

## Applying a Rule Set

1. Click the ellipsis icon next to a Rule Set.
2. Select **Apply Rule Set**.
3. Choose the **Source Type**: Data Source, Database, Schema, or BigQuery Dataset.
4. Select the asset(s).
5. Click **Apply**.

**Example:**

- Applying `Customer Data Quality Checks` to a database automatically creates policies for all included rules.
- Users without sufficient permissions may not see the created policies.

## Scheduling a Rule Set

1. Click the ellipsis and select **Schedule Rule Set**.
2. Enter a **Schedule Name**.
3. Select assets for application.
4. Enable **Automatic Policy Activation**.
5. Set frequency: Minute, Hour, Day, Week, Month, Year.
6. Click **Apply**.

## Viewing Rules and Schedules

- **View Rules:** Click ellipsis &gt; **View Rules**. Shows rule name, type, applied by, and creation date.
- **View Schedules:** Click ellipsis &gt; **View Schedules**. Shows schedule name, frequency, and enabled status.

## Example

**Scenario:** Monitor customer data quality.

**Step 1: Create Rules**

- `Customer Email Validation` (Null Check)
- `Customer ID Uniqueness` (Duplicate Row Check)
- `Customer Phone Validation` (Pattern Match)

**Step 2: Create a Rule Set**

- `Customer Data Quality Checks` (includes the 3 rules above)

**Step 3: Apply the Rule Set to Assets**

- Assets tagged `CustomerData`
- **Result:** Applying the Rule Set **automatically creates a Data Quality Policy** for each asset.

**Step 4: Schedule the Policy**

- Schedule the automatically created policy to run daily**.**
- The policy will execute all rules in the Rule Set, track pass/fail results, and generate alerts if necessary.

**Outcome:**

- The **Policy monitors customer data continuously**, not the Rule Set itself
- Reports and alerts indicate which rules passed or failed for each asset