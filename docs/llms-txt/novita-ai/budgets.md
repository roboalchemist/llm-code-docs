# Source: https://novita.ai/docs/guides/budgets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Budgets

The **Team Member Budgets** feature allows you to set flexible spending limits for each member,helping you effectively control overall costs.

> **Note**: This feature is only available for team accounts. Personal accounts or accounts not part of a team will see the menu but cannot access budget management functionalities. You can convert your personal account into a team account or join an existing team to collaborate with others.

## Permissions

* Only the **Team Owner**, **Admin**, and **Billing Roles** can check and manage team budgets.
* **Developer** and **Basic Roles** can only view their own budget type and budget limit, and cannot make changes.

## Budget Control Modes

For all team members, the system enforces budget execution and reset logic based on each member’s **Budget Type**.

### 1. Budget Type Description

| **Budget Type** | **Description** |         **Example**         |
| :-------------: | :-------------: | :-------------------------: |
|  **Unlimited**  |     No limit    |       Unlimited usage       |
|   **One-time**  | One-time budget | budget frozen once consumed |

### 2. Budget Type Switching

When an administrator changes a member’s budget type, the system applies the following transition rules:

| **Switch Path**      | **Processing Logic**                                                                                                     |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| Unlimited → One-time | The new budget will take effect immediately, with current spending reset to zero and tracked under the new budget cycle. |
| One-time → Unlimited | Current quota and restrictions are immediately discarded, and unlimited quota begins.                                    |

## Adjusting Member Budget Limits

Please follow the steps below to adjust a member’s budget:

1. Go to the [**Team Member Budgets**](https://novita.ai/billing/budgets) page.
2. Find the relevant member in the list, or use the search box to quickly locate them. Budgets can be configured for both current team members and invited members who are pending acceptance.

<img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/Budges01.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=c7df2a97caf5dfbe4a16cdaf30f4427b" alt="Budges01 Pn" width="1280" height="829" data-path="guides/images/Budges01.png" />

3. Click the "**Edit"** button and select the desired budget type.
   * New members are set to **Unlimited** by default, and this can be changed at any time.
   * The **One-time** budget type allows you to set a specific budget limit.

<img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/Budges02.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=05736cda09f305ecbe2d59cc4c0cc4ab" alt="Budges02 Pn" width="1280" height="827" data-path="guides/images/Budges02.png" />

4. Click the "**Refresh"** button to get the latest budget and consumption data.

<img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/Budges03.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=779bca0d1f3a71c0d73945756120b92e" alt="Budges03 Pn" width="1280" height="829" data-path="guides/images/Budges03.png" />

> **Note**: Budget changes take effect immediately. Once a member’s quota is exhausted, they will be unable to initiate new service calls.

## Budget Usage & Service Invocation Rules

* All API Keys created by a member share the same budget pool.
* Before any service is started, the system will automatically check both the wallet balance and the member’s remaining quota. If either is insufficient, the request will be denied.
* Upon reaching the budget limit, all related tasks will be automatically stopped.


Built with [Mintlify](https://mintlify.com).