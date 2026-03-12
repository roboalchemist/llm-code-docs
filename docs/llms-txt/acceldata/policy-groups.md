# Source: https://docs.acceldata.io/documentation/policy-groups.md

# Policy Groups

In ADOC, a **Policy Group** is a way to organize multiple policies together. Instead of managing individual rules one by one, you can bundle them into groups that reflect a project, a data domain, or a business goal. For example:

- A **Customer Data Group** might include rules for email validity, address completeness, and duplicate checks.
- A **Finance Data Group** could hold rules for reconciliation, daily freshness, and anomaly detection.

This makes it easier to apply, monitor, and maintain related policies as a set.

## Why Use Policy Groups?

- **Organization**: Keep policies structured by team, domain, or use case.
- **Efficiency**: Manage and review multiple rules at once.
- **Clarity**: Business users can quickly see which rules apply to which area of the business.

## Creating a Policy Group

To create a new Policy Group:

1. Navigate to **Data Reliability &gt; Manage Policies &gt; Policy Groups**.
2. Click **Create**.
3. Enter a **name** for the group (e.g., “Customer Data Quality”).
4. (Optional) Add a **description** to explain its purpose.
5. Select the policies you want to include.
6. Click **Create**.

Once created, the group will appear in the **Policy Groups table**.

## Understanding the Policy Groups Table

The table gives you a quick view of all existing groups:

| Column | What It Shows | 
| ---- | ---- | 
| **Policy Group Name** | The name of the group. Click it to view or edit the group’s details. | 
| **Created At** | When the group was first created. | 
| **Updated At** | The most recent time the group was edited. | 
| **Linked Policies** | The number of policies inside the group. Clicking the number shows which policies are included. | 
| **Actions** | Lets you delete the group. | 


Think of Policy Groups like **folders of rules**. Instead of managing 10 different policies separately, you can manage them as one logical set.