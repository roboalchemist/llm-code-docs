# Source: https://docs.acceldata.io/documentation/data-policy-template.md

# Data Policy Template

> Data Policy Templates have been deprecated as part of a shift toward direct rule-based configurations. Users can continue to implement anomaly detection logic using **rulesets**, which provide equivalent and more flexible functionality.

A **Data Policy Template** is a reusable collection of **rule definitions** that can be applied to multiple Data Quality Policies. Instead of defining rules every time you create a policy, you can create a single template containing multiple rules. When you add this template to a policy, all the rules it contains are automatically evaluated.

**Benefits:**

- Saves time by reusing common rule definitions
- Ensures consistency across multiple policies
- Simplifies policy creation for new datasets

## Adding a Data Policy Template

Follow these steps to create a new Data Policy Template:

1. Navigate to: **Data Reliability &gt; Manage Policies &gt; Data Policy Templates tab**.
2. Click **Add Data Policy Template** to open the configuration page.
3. Enter the following details:
    - **Name:** Provide a descriptive name for the template (e.g., `Customer Table Quality Rules`).
    - **Description:** Explain why this template is being created.
    - **Select Rules:** Choose the rules to include in the template.

## Measurement Types and Rule Definitions

| Measurement Type | Description | Example | 
| ---- | ---- | ---- | 
| **Null Values** | Verifies whether selected columns contain null values | Customer email should not be null | 
| **Schema Match** | Checks if column data types match the expected type | Customer ID must be Integer | 
| **Pattern Match** | Ensures column values follow a regular expression | Emails must match `^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$` | 
| **Enumerations** | Validates values against a predefined list | Status must be `Active`, `Inactive`, or `Pending` | 
| **Tags Match** | Ensures values are present in a specified tag | Product category must match a defined tag | 
| **Range Match** | Validates values fall within a lower and upper bound | Order total between 0 and 10,000 | 
| **Uniqueness Check** | Ensures values in a column are unique | Customer ID column must be distinct | 
| **Duplicate Row Check** | Detects duplicate rows in a dataset | Ensure no repeated transaction records | 
| **Row Check** | Validates total number of rows falls within a range | Table must have 10,000–12,000 rows | 
| **Lookup** | Compares values with a reference table or column; optional SQL filter | Check IDs exist in a reference table where `is_active = 'Y'` | 


4. (Optional) Add **Labels** by clicking **Add Labels** and providing key-value pairs for easier categorization.
5. Click **Save** to create the template.

## Understanding the Data Policy Templates Table

The **Data Policy Templates table** provides an overview of all templates you have created. You can search for a template by its name.

| Column Name | Description | 
| ---- | ---- | 
| **Name** | Name of the data policy template | 
| **Description** | Description provided when the template was created | 
| **Data Dimensions** | Lists data dimensions defined in the template (e.g., Consistency, Uniqueness) | 
| **Labels** | Displays any labels associated with the template | 
| **Created At** | Date and time the template was created | 
| **Updated At** | Most recent date and time the template was updated | 
| **Vertical Ellipsis Icon** | Click to **edit** or **delete** the template | 


## Editing a Data Policy Template

1. Go to the **Data Policy Templates tab** in Manage Policies.
2. Click the **name** of the template you want to edit.
3. Update the rules, description, or labels as needed.
4. Click **Save** to apply the changes.

**Example:**

- You have a template `Customer Table Rules` with 5 rules.
- You add a new **Pattern Match** rule to check email formats.
- After saving, all policies using this template will now automatically include the new rule.