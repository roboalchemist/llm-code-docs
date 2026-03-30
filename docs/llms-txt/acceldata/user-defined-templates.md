# Source: https://docs.acceldata.io/documentation/user-defined-templates.md

# User Defined Templates

User Defined Templates (UDTs) let you define custom functions once and reuse them across multiple Data Quality policies in ADOC. This avoids duplicating the same logic in different places and ensures consistency.

UDTs are a key part of **Policy Management** because they extend the platform with reusable, business-specific rules that can be centrally managed.

## Why Use UDTs?

- **Reusable logic**: Write once, use across many policies.
- **Flexibility**: Build in SQL, Scala, Java, Python, JavaScript, or Expressions.
- **Consistency**: Standardize business rules across datasets.
- **Maintainability**: Update logic in one place instead of many.

## Types of UDTs

1. **Transform UDT** – Extracts or transforms values from records in a dataset.

- _Example_: Standardizing phone numbers before validation.

2. **Validation UDT** – Applies rules to validate records in a dataset.

- _Example_: Ensuring no transaction has a negative amount.

## Creating a UDT

1. Navigate to **Data Reliability &gt; Manage Policies &gt; User Defined Templates**.
2. Click **Create New**.
3. Choose either **Transform UDT** or **Validation UDT**.
4. Enter details (Name, Description, Language, Code, Reference Variables).
5. (Optional) Add Labels or Metadata.
6. **Validate** your code (see below).
7. Click **Save**.

## Validation Methods

Before saving, you should test your UDT code to ensure it works correctly. ADOC provides two ways to validate:

### 1. Manual Validation

Use sample data that you enter yourself.

1. Select **Manual** from the Validate button.
2. Enter your test data.
3. Choose an analytics pipeline to run it.
4. Provide values for any reference variables in your code.
5. Click **Validate**.

This is useful for quick checks during development.

### 2. Asset Validation

Use real data from one of your connected assets.

1. Select **With Assets** from the Validate button.
2. Choose an asset using the search bar or navigation.
3. Click **Next** to define values for reference variables.
4. Click **Validate**.

This method is recommended for confirming that the UDT works with production-like datasets.

## Managing UDTs

All created templates are listed in the **User Defined Templates table**, which shows:

- Name
- UDT Type (Transform or Validation)
- Language
- Labels
- Created/Updated timestamps

For each UDT, you can:

- **Edit**: Update logic (linked policies may be impacted).
- **View**: See full details.
- **Linked Policies**: Check which policies use it.
- **Delete**: Remove if no longer needed.

## Example Scenario

Your company needs to validate tax calculations across multiple datasets.

- Create a **Transform UDT** to calculate tax for each record.
- Create a **Validation UDT** to ensure the tax follows country rules.
- Apply these templates across multiple policies instead of rewriting the logic each time.

This ensures consistency and makes ongoing maintenance far simpler.