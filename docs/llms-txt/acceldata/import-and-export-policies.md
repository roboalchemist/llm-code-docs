# Source: https://docs.acceldata.io/documentation/import-and-export-policies.md

# Import and Export Policies

Policies in ADOC capture your organization’s rules for **data quality, freshness, drift, anomalies, and more**. Often, teams want to reuse these rules across different environments (e.g., staging to production) or share them across business units. To make this easier, ADOC allows you to **import and export policies**.

- **Exporting a policy**: Think of it like packaging your rules into a file so they can be shared or backed up.
- **Importing a policy**: It means bringing in rules from another ADOC environment (another tenant), so you don’t have to start from scratch.

This saves time, ensures consistency, and reduces human error.

> - You can **only import from another tenant** (not your own).> - Policy packages are shared as `.zip` or `.gz` files.> - Whether you can see or edit imported policies depends on your **permissions** (RBAC).

## Import Policies

You use **Import Policies** when you want to bring rules into your environment that were already created elsewhere. You import policies to:

- Standardize policies across departments or regions.
- Avoid re-creating policies for the same rules (e.g., “Customer Email must not be null”).
- Reuse tested and approved rules quickly.

## How to Import

1. Navigate to **Data Reliability -&gt; Manage Policies -&gt; Import Policies**.
2. Click **Import Policies**.
3. Upload the `.zip` or `.gz` file you received.
4. ADOC will:
    - Check if the data sources match.
    - Tell you if there are name conflicts.
    - Ask whether you want to override existing policies or skip them.

5. Once complete, ADOC applies the imported policies.

Recommendation If a policy import fails, it doesn’t mean the data is lost. It usually means the policy depends on something that isn’t set up yet (like a missing data source).

## What You’ll See

After importing, you’ll see a table that tells you:

- When the import started and finished.
- Whether it was successful or errored.
- How many new policies were created or updated.

## Export Policies

You use **Export Policies** when you want to share your rules with another environment or team. You must export policies to:

- Move policies from **development to production** safely.
- Share best-practice rules with other teams.
- Keep a backup of your policies for compliance or audits.

## How to Export

1. Navigate to **Manage Policies -&gt; Policies tab**.
2. Use filters to find the policies you want (or leave blank to export all).
3. Select the  checkbox on the left of the policies table.
4. Click **Export**. The **Export Policies dialog box** is displayed allowing you to:
    1. Choose whether to include tags (metadata).
    2. Provide a filename (optional).
    3. Click the **Export Policy** button to download the `.zip` file.

Think of the exported `.zip` file as a “policy package” that someone else can import into their ADOC.

## Things to Keep in Mind

- Some features (like SQL templates) are exported automatically even if not in use.
- If you don’t have the right permissions, you may not see the policies after importing (even if they were technically created).
- Exported files include the **ADOC version** to make tracking easier.