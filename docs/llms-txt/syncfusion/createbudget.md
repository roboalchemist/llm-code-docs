# Source: https://docs.syncfusion.com/code-studio/enterprise-server/createbudget.md

# Create Budget

The Budget feature in Code Studio enables administrators to allocate and monitor AI usage budgets for teams and individual users. This helps organizations manage costs effectively and optimize AI resource utilization.

> **Note**: Only admins can edit and assign budget for all.



## 1. Team Budget Setup

**Steps:**

- Open the **Code Studio** page and navigate to the **Budget** page from the left sidebar.

   <img src="./enterprise-images/budget.png" alt="budget"  />

- Click the **âBudgetâ** button on the top right of the page.
- Open the **Add Budget** dialog box.

   <img src="./enterprise-images/teambudget.png" alt="Team budget"  />

- Choose the desired **Team** in the team selection field.
- Set the **Maximum Budget** for the team.
- Choose the **Budget Period**:
  - Monthly
  - Quarterly
  - Half-Yearly
  - Annually
- (Optional) Enable **Auto-Renewal** and set the **Reset amount**. This will automatically reset the budget at the end of each period.
- Click the **âCreateâ** button to add the team budget.

## 2. Individual User Budget Allocation

**Steps:**

- Click **âManage All users budgetsâ** on the top right of the page.

   <img src="./enterprise-images/manageAllUserBudget.png" alt="Manage All User Budget"  />

- All users are listed in the table.
- For a user, open the **Context Menu** and click **âAdd Budgetâ**.

   <img src="./enterprise-images/userBudget.png" alt="User Budget"  />

- Now the **Budget Dialog Box** will be open:
  - Set the **Maximum Budget**.
  - Choose the **Budget Period**.
- Click the **âAddâ** button to assign the budget to the user.

   <img src="./enterprise-images/addUserBudget.png" alt="Add User budget"  />

## 3. Team Members Budget Setup

**Steps:**

- Click on the desired **Team** to go to its details page.

   <img src="./enterprise-images/teamDetailsBudget.png" alt="Team Details page"  />

- The selected team members are listed in the grid.
- Open the **Context Menu** and click **âAdd Budgetâ**.
- Now the **Budget Dialog Box** will be open:
  - Set the **Maximum Budget**.
  - Choose the **Budget Period**.
- Click the **âAddâ** button to assign the budget to the team member.

   <img src="./enterprise-images/addUserBudget.png" alt="team User budget"  />

## 4. Bulk Budget Setup for Users

**Steps:**

- Select multiple users by clicking the checkboxes in the users grid table.

   <img src="./enterprise-images/bulkBudget.png" alt="Bulk budget"  />

- Click **âAdd Budgetâ** (appears after selecting users).
- In the **Bulk Budget** dialog box:
  - Set the **Maximum Budget**.
  - Choose the **Budget Period**.
- Click the **âAddâ** button to assign budgets to all selected users.

   <img src="./enterprise-images/addBulkBudget.png" alt="add Bulk budget"  />

> **Note**: If selected users already have budgets, they will be **updated** with the new values.

## 5. Edit Budget

**Steps:**

- Click **âEdit Budgetâ** from the context menu of a team or user.
- Modify the **Maximum Budget**, **Budget Period**, or **Reset amount** (if applicable).
- Click **Update** to save the changes.

   <img src="./enterprise-images/editBudget.png" alt="Edit budget"  />

## 6. Delete Budget

### 6.1 Delete Team Budget

**Steps:**

- Click **âDeleteâ** in the context menu.
- In the **Delete Dialog Box**, click **âDeleteâ** to confirm.

   <img src="./enterprise-images/teamBudgetDelete.png" alt="delete Team budget"  />

### 6.2 Delete User Budget

**Steps:**

- Click **âEdit Budgetâ** from the userâs context menu.
- In the **Edit Budget** dialog, click **âDeleteâ**.
- In the **Delete Dialog Box**, click **âDeleteâ** to confirm.

   <img src="./enterprise-images/userBudgetDelete.png" alt="delete User budget"  />

## 7. Usage Alerts

Administrators can set up alerts for a team or a specific user to notify us when budget usage exceeds a defined threshold.

**Steps:**

- Click **âSet Alertâ** from the context menu to open the Alert dialog box.  
  *(If an alert is already set, click **âManage Alertâ** instead.)*

   <img src="./enterprise-images/setAlert.png" alt="set alert"  />

- Set the **Usage Threshold** (e.g., 50%).
- Enter the **Email Subject** (required).
- Specify the **Recipients** for the alert (e.g., team lead or manager). An alert email will be sent to these recipients.
- Click **Set** to activate the alert.

   <img src="./enterprise-images/setAlertDialog.png" alt="set alert dialog"  />

   ð Alerts help proactively manage budget overruns and ensure timely action.


