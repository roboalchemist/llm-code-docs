# Source: https://docs.qodo.ai/qodo-documentation/management-portal/teams.md

# Teams

The Teams page is used to organize users into teams and manage team-level settings.

### Who can access this page?

* **Enterprise**
  * Organization admins can view and manage all teams.
  * Team admins can manage their own teams.
* **Team and Free plans**
  * Team admins can manage the single available team.
  * Team members can view team information only.

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2FvKtSVBqJHLZJXXECb1tW%2FChatGPT%20Image%20Feb%2011%2C%202026%2C%2011_23_16%20AM.png?alt=media&#x26;token=a9ffeb0b-d370-4ffb-86cb-3c301ea341e5" alt=""><figcaption></figcaption></figure>

#### Teams table columns

| Column     | Description                      |
| ---------- | -------------------------------- |
| Team       | The team name.                   |
| Created on | Date the team was created.       |
| Owner      | Email address of the team admin. |
| Members    | Number of users in the team.     |
| Actions    | Available team actions.          |

#### Create a team&#x20;

To create a team:

1. Open the **Teams** page.
2. Select **Create team**.
3. Enter a **team name** and select a **team owner** (search by user email).
4. Click **Create team** to finish.

The new team appears in the teams list and can be managed immediately.

#### View team members

From the team’s Actions menu, select **View team members** to see all users assigned to the team.

#### Rename a team

{% hint style="info" %}
Team owners and organization admins can perform this action.&#x20;
{% endhint %}

1. From the team’s Actions menu, select **Rename team**.
2. Enter the new team name.
3. Click **Save.**

### Delete a Team

{% hint style="info" %}
This action cannot be undone.
{% endhint %}

#### To delete a team:

1. Open the team’s **Actions** menu.
2. Select **Delete team**.
3. Confirm the action.

#### What happens when a team is deleted?

The result depends on the account type:

**Team in an Enterprise plan**

* Team members are removed from the team.
* They remain in the organization.
* Removed members can still be found on the **Users** page.
* Other teams and subscriptions are not affected.

**Team in a Teams plan**&#x20;

* Deleting the team terminates the active Teams subscription immediately.
* The account is downgraded from **paid** to **free**.
* No refund is issued.
* Removes the user account from the database.\
  If a user wants to stop renewing but keep access until the end of the billing cycle, they should use **Cancel subscription** instead. This keeps the plan active until the billing period ends, after which the account is downgraded to free.
