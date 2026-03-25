# Source: https://docs.axonius.com/docs/exception-management.md

# Exception Management

Learn about managing exceptions for security findings, including workflows, approval processes, and admin settings.

## Overview

In the context of risk management, Exceptions are permissions to leave certain vulnerabilities unresolved. This is typically done when immediate remediation is difficult due to business, technical, or operational reasons. Exceptions require justification and risk acknowledgement.

**Axonius Exception Management** provides a centralized, auditable interface for defining and managing Exception Rules at the Security Finding (specific vulnerability on a specific asset) level. This solution empowers security teams to:

* Filter Exceptions from dashboards and workflows across all integrated scanners.
* Configure structured approval workflows, track and manage them in one place.
* Balance security needs with real-world constraints while maintaining oversight.
* Uphold compliance and operational integrity while reducing manual effort.

**Exception Management** is the main operational space used by requestors and approvers to submit, view, approve, deny, and track Exception requests. To access this page, click **Exception Management** from the **Security Findings** page.

![ExceptionManagementNavigationButton](https://files.readme.io/a95effe54d9541b48edf6addc1ce14e5bd0930351784326cea8d7982f4a74bd2-image.png)

The Exception Management workflow is as follows:

1. [An admin defines](https://docs.axonius.com/docs/exception-management#/admin-settings---exception-rules) which user roles can request Exceptions, whether they need approval, and who can approve them.
2. A user with the appropriate permissions [creates an Exception request](https://docs.axonius.com/docs/exception-management#/creating-an-exception).
3. The approver(s) defined in the Exception Rule for this user role review the request.
4. The approver(s) decide whether to [approve or deny](https://docs.axonius.com/docs/exception-management#/approving-exceptions) this Exception.
5. If the Exception is approved, it becomes active, and takes effect until its expiration date (if set).

The main page of the Exception Management page displays the Exception Table.

## Exception Table

The table of Security Findings Exceptions displays the following information:

* **Exception Name**
* **Query** - The query this Exception applies to.
* **Security Findings** - The Security Findings this Exception applies to.
* **Status** - Contains one of the following values:
  * **Active** - Exception is currently in effect.
  * **Deactivated** - Exception was approved previously but was [deactivated](https://docs.axonius.com/docs/exception-management#/deactivating-exceptions) by an approver.
  * **Pending Approval** - Exception is waiting for all the approvers to approve it.
  * **Denied** - Exception is not approved.
  * **Expired** - The expiration date of this Exception has passed.
* **Expiration Date** and **Applied since** - Information on the date range in which this Exception should be active.
* **Requested By** and **Request Date** - Who requested this Exception and when.
* **Approvers** - The users that need to approve this Exception.
* **Waiting for** - The user who needs to approve this Exception so it can move to the next step (another approver or final approval).

Select an Exception from the table to view its details: general details, approval info (which step the Exception reached in the approval workflow), and a list of all the Security Findings included in the Exception. You also have the option to open this list in the Security Findings Assets page.

Note that this list is dynamic and prone to changes based on the assets included in the query.

<Image align="center" alt="Asset List" width="600px" src="https://files.readme.io/24b6b5af2f46b9b835a6ffdefb28710ec527e6eddf8c047caaa8382cb9c7d741-image.png" />

## Admin Settings - Exception Rules

<Callout icon="📘" theme="info">
  **Notes**

  1. Only users with Admin privileges can access this page. If you are not an admin, you can skip this section.
  2. Admins must have the Manage Security Findings Exceptions permission to create and edit Exception Rules.
</Callout>

Exception Rules provide a consistent, controlled Exception management by tailoring the process to specific user attributes. Use the **Admin Settings** page to create Exception Rules based on user roles and permissions. Define the following:

* Which user roles can request Exceptions
* Whether their requests require approval
* If their requests require approval - how many approval steps are required, and who are the approvers in each step.
* Additional instructions for the requester, if needed.

To access these settings, click **Admin Settings** from the **Exception Management** page.

To create an Exception Rule:

1. Click **Create Rule**.
2. Select the user role this rule applies to.
3. Set the approval workflow for this user's Exception requests. The options are:

   * **Auto Pilot** - Any request by this user role will be approved automatically.
   * **Approvers** - Select who should approve requests from this user role. You can select multiple approvers per step, as well as add multiple approval steps. When adding multiple approvers per step, **either** of them can approve the request in this step - the requester selects the approver for each step.. Click the trash bin icon next to each step to remove it from the workflow.

     <Callout icon="📘" theme="info">
       **Notes**

       * The approval workflow will follow the order in which you add the steps.
       * You can select approvers from all user roles.
     </Callout>
4. *(Optional)* Add specific instructions you want the user to follow when requesting an Exception. These instructions will appear on the requester's **Create Exception** form.
5. Click **Create Rule**. The new Exception Rule is added to the Rules table.

### Editing an Exception Rule

To edit rule details, select the relevant rule from the table. Changes to a rule apply only to future Exceptions and don't affect existing ones.

<Callout icon="🚧" theme="warn">
  **Attention**

  Exception Rules cannot be deleted, they can only be edited.
</Callout>

### Enabling Email Notifications (Optional)

As an admin, you have the option to to enable email notifications for Exception requests for easy management and tracking. From the Admin Settings page, toggle on **Enable Email notifications** (enabled by default; disable it to stop all email notifications).

A summary of the email notification flow:

1. A user creates a new Exception request. The system sets the request status to **Pending Approval** and notifies both the first approver via email.
2. If the approver doesn't take any action after 48 hours, the system sends them another email reminder. If the approver still fails to act, the request status remains **Pending Approval** until its expiration date.
3. The requester receives an email notification for every decision made on their request throughout the process. If there are multiple approvers, the system passes the request to the next approver on the list to repeat the cycle.
4. For active Exceptions: the system sends the requester an email notification 7 days prior to, 24 hours prior to, and on the day of expiration, and prompts them to submit a new request if needed.

<Card title="View a detailed email notification flow" icon="fa-diagram-project">
  [View the full flowchart here →](https://mermaid.ink/svg/pako:eNqVVWtv0zAU_SuWEQKkdkrTR9oggWAdDAmqqZuEIJ2Qm9y01tK42M62UvW_c23ntbEKyJfEzj3nPnzu9Z7GIgEa0pVk2zX5PF_kBJ_nz8lpobTYkFORCUmu1rAB5f7FGVNqCilRmulCzSEhKc-y8FmaDpJB0lFaihsIn00mHj7lsnvHE70O_e19JzaMxjp9_SThRwmQl5Q-xHHQqyl7yyH4_0WZC83TXckGvXSYQs3m9YbBZIkIh7nUTOqX0QzuyBx-FqA0OZXANCTXr0i3-4Z8yrk-2zCeRTPH-m67leIW5HUYhs6RY6oNLWwOtxzuKi-qWLpSOzDLflxIEYNSJKp2SLlz7RDmSbiEWHORk6v3za5j3ldhkHfW5O2BNCbNFx7phVBc81sgHzJx95gGY60SsmG7HDGUVZVuWRWQoanVCirz5HH-5mnglu1LkWm-_yJkjZLKEmJiydvDkYBnsGI24Aum108FPIV8Z_nxg0Py8tIqKCyXrzCuWqRHXJypmGXMlvaYk5koK2s9fWVcD8aReZHBmJyLQrZPyv0uD37D8wRk5LRQLYkWR5XjHJd2huNSo3Jnwvnf21UTT7tuDwxN1AtqQyxy_EHO7rdc7hbUctpFq1jl-ki1_iAuv67YDeQPBG6sIU8qpWNx59CVotA8XxG9BvLiG6gXZItlJksW35hCmG2O7cJR9rYQPHaHsRT3jsYqx_hFML5E010tRzifyHvJExTlIxQWq9s1UZqwb6FO2i2bnO3Ucdia9QPPWeaUXIZVjkAHtslbGyf2J_rEMdSN_VGyXP_ZL06tlY53D2ZMi8yZtcF1pNjZultG1TR3KzZLbqx-OKt2pvVIav0nUZvyQQn-OpamQRSQKdspHGQc5zKp9F9m8pTop4GN8NwfRP7ANdV_oBHWHEbkiu4k_09wB2i1ht34h_5AtdMOXp08oaGWBXToBiT6wyXdG5MF1ebmXNAQPxNIGcpyQRf5AWFbln8XYlMhsVFWaxqmLFO4KrYJ3jxTzvBkNvWuBDMYTgU2NQ2Ho2BoWWi4p_c07Pb6nn8y7vujwO_3_fHQ63fozu6fTEY-XnbesD8Zet5kcOjQX9a1f-KNe95o1A88r-f1g9HhNydIkT0)
</Card>

## Creating an Exception

To request a new Exception, click **Create Exception**. After your request is approved, the Exception is synced with the system correlation every 12 hours.

There are two ways to select Security Findings to include in the Exception:

* **Selecting a Security Findings query** - see step 2 in the procedure described below.
* **Manually Selecting Security Findings** - Go to the Security Findings Assets page and:
  * To create an Exception for one Security Finding, hover over the asset's row, and from the icons that appear on the right, click **Create Exception**.
  * To create an Exception for multiple Security Findings (up to 1000), mark the checkboxes of the assets you want to include, and click the **Create Exception** button above the table.

    ![ManualSelectException](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/ManualSelectException.png)

    The **Create Exception** drawer opens. Follow the steps detailed below to complete the request. Note that the section of selecting assets from a query is disabled at this stage.

In the **Create Exception** drawer, follow these steps:

1. In the **Exception Setup** tab, provide general Exception details, such as a title (name) and a justification reason for requesting this Exception. For example, *"These vulnerabilities exist in a legacy system that is protected from external access by strict firewall rules"*. Some fields are optional, like the Evidence Link supporting this justification.
2. Select a Security Findings query that contains the assets you want this Exception to apply to. For example - "All Low-Risk Security Findings".

   1. Any query you select is duplicated and becomes a **managed query** after submitting the request. This managed query cannot be edited, renamed, moved, or deleted. Such queries are centrally managed by Axonius and are used to ensure the integrity of exception scopes.

      <Callout icon="📘" theme="info">
        **Notes**

        * The query is dynamic, as the Security Findings included in it change according to changes in your data.
        * The managed query is a **duplication** of the original query. The original query is **not** managed, and you can edit, rename, move, or delete it as needed.
      </Callout>
   2. To access managed queries, navigate to the **Queries** page and select the **Security Finding Exception Queries** folder.

      <Image align="center" alt="ExceptionQueriesFolder" width="200px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/exposures/SF%20Exception%20Queries.png" />
3. After you select a query, you can view all the assets it includes in the **Security Findings List** tab.
4. If there are multiple approvers configured for your role, select one approver whom you want to approve this request. It is recommended to choose the approver that is most relevant to you (for example, your team leader) or to this specific Exception. If automatic approval was configured, the system informs you of that.

   <Callout icon="📘" theme="info">
     **Notes**

     1. The approval workflow (automatic or requires approvers) and the list of available approvers is preconfigured for each user role in the [**Admin Settings**](https://docs.axonius.com/docs/exception-management#/admin-settings---exception-rules).
     2. In case there are multiple approval steps and multiple approvers in each step, you need to select **one approver per step**.
   </Callout>
5. Set an expiration date for the Exception - either it never expires, or expires within a set number of days, or on a specific date.
6. After you populate all the required fields, click **Create Exception**. The new Exception appears as a new row in the Exception Table with a "Pending Approval" status, unless it is automatically approved, and then its status is "Approved".\
   If you created an Exception request by selecting assets directly from the Security Findings Assets page, navigate to **Exception Management** to see your request listed there.

## Approving Exceptions

Users who were selected as approvers for Exception requests can see the list of requests in the [Exception Table](https://docs.axonius.com/docs/exception-management#/exception-table). If any requests are pending your approval, select the relevant request to review it. Use the table’s filters such as **Status** or **Requested by** to easily navigate through the requests.

In the Exception Details drawer that opens, review the details of this Exception, the Security Findings included in it, whether there are any other approvers, and if so, what is their status.

After reviewing the request, select whether to **Deny Exception** or **Approve Exception**.

<Callout icon="🚧" theme="warn">
  **Attention**

  While you can't change your selection (denying or approving), admins and approvers can still [deactivate the Exception](https://docs.axonius.com/docs/exception-management#/deactivating-exceptions) **after** it was approved.
</Callout>

<Callout icon="📘" theme="info">
  **Note**

  Since the approval workflow follows the order of the approval steps, approvers can approve or deny Exceptions only when their assigned step is in effect. For example, an approver who was assigned Approval Step 2 will see these the **Deny Exception** and **Approve Exception** buttons in the Exception Details drawer **only after Approval Step 1 was complete.**
</Callout>

<Accordion title="Approval Workflow - Example" icon="fa-info-circle">
  According to the Exception Rule, users with the role X require 3 approval steps for their Exceptions, and the following approvers are assigned to each step:

  * **Approval Step 1:** User A, User B
  * **Approval Step 2:** User C, User D, User E
  * **Approval Step 3:** User F

  When a user with the role X creates an Exception, they need to select the following approvers for each step:

  * **Approval Step 1:** User A **or** User B
  * **Approval Step 2:** User C **or** User D **or** User E
  * **Approval Step 3:** User F

  Assume that the user selected the following approvers:

  * **Approval Step 1:** User B
  * **Approval Step 2:** User D
  * **Approval Step 3:** User F

  User D will only be able to approve or deny the Exception after User B approved it; and User F will only be able to approve or deny the Exception after User D approved it.
</Accordion>

## Additional Actions on Exceptions

### Deactivating Exceptions

An Exception can be deactivated after it was approved by either:

* Its creator
* An admin
* A user who had already approved the request

To deactivate an Exception, select it from the Exceptions table and click **Deactivate**. This action cannot be undone.

### Duplicating Exceptions

If you want to create multiple Exception requests with similar details, **or** submit a request identical to an existing request that was expired; instead of creating a new request from scratch, you can duplicate an existing request and edit the relevant details there. Thus, to extend an expired request, you only need to change the expiration date.

To duplicate an Exception:

1. Select it from the Exceptions table and click **Duplicate**. A new Create Exception drawer opens.
2. Edit the relevant details and click **Create Exception**.

<Image align="center" alt="ExceptionActionsDeactivateDuplicate" width="300px" src="https://files.readme.io/bec36f9ebc619f363d70dc9291dbbcf0c73ee702c728b3f5191ae0a758b4c519-image.png" />

<br />