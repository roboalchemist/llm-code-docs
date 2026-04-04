# Source: https://docs.bito.ai/help/account-and-settings/managing-workspace-members.md

# Managing  workspace members

In Bito, collaboration happens within a **Workspace**, where team members are assigned roles and access based on their responsibilities. In most cases, every organization would create one Workspace. Anyone can [**sign up on Bito**](https://alpha.bito.ai/), create a workspace for their team, and invite their coworkers to join the Workspace.&#x20;

The [**Manage Users → Members**](https://alpha.bito.ai/home/members) dashboard introduces a clear, flexible interface for managing user access and feature seats across your team.

## Seat management overview

At the top of the **Members** dashboard, you’ll see a summary of your seat usage and assignment status:

* **Seats purchased**: Displays the total number of seats your workspace has purchased and the total billing amount.
* **Seats assigned**: Shows how many of those seats are assigned for:
  * **IDE Code Reviews**
  * **Git Code Reviews**
* **Seat assignment mode**:
  * **Auto (Assign & Buy):** In this mode, available seats will be automatically assigned to developers (marked as [Eligible](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If all seats are assigned, new seat is purchased and assigned automatically.
    * ***Note:** This mode is useful for dynamic teams where new contributors are added frequently.*
    * ***Note:** This is the default mode for all new workspaces.*
  * **Auto (Assign only):** In this mode, available seats will be automatically assigned to developers (marked as [Eligible](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats)) when they join the workspace or when they submit their first pull request reviewed by Bito. If no seats are available, Bito will not purchase additional seats, and the developer will not gain access to Bito features.
  * **Manual:** In this mode, workspace admins need to manually purchase seats and [assign them to developers](https://docs.bito.ai/billing-and-plans/overview#assigning-code-review-agent-seats) as needed. Bito will review pull requests only for submitters who have an assigned seat.
    * ***Note:** This mode is ideal for teams that want tighter control over who gets access and when billing occurs.*

You can switch between these modes based on your team's seat allocation preferences.

<a href="../../billing-and-plans/overview#seat-management" class="button primary">Learn more</a>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fk892sPlZPXvsMUJJQD8O%2Fscrnli_jE3Uiba03IjHl3.png?alt=media&#x26;token=0357c01b-3100-48d6-acb9-6222200ce6ef" alt=""><figcaption></figcaption></figure>

## Managing members by feature

Below the seat overview, you'll find three tabs to manage different types of access:

#### 1. **Git Code Review tab**

Assign or unassign seats to members specifically for the Git based Code Review Agent feature. Each member listed here can be toggled on or off depending on whether you want to allocate a seat for this feature.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FtyTtpwy7rcDF5gS0eiCo%2Fscrnli_4XpAlWqsuim28d.png?alt=media&#x26;token=fb85bf93-c45c-453c-bed1-92ea4dad2251" alt=""><figcaption></figcaption></figure>

#### 2. **IDE Code Review tab**

Similar to the Git Code Review tab, this tab lets you assign or remove access to Bito's AI Chat and code review feature in supported IDEs. You can also [invite new members](#inviting-coworkers-to-the-workspace) to join the workspace.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkCCdW3bit3FaCDFXdZUa%2Fscrnli_0JzrS8S3Gip93M_1.png?alt=media&#x26;token=d96f858a-ed59-48c2-aebb-8ca7f66a9917" alt=""><figcaption></figcaption></figure>

#### 3. **Admin tab**

This tab is dedicated to managing administrative roles within the workspace. Only members with elevated permissions are shown here.

This tab displays a table with the following information:

* **Name**: Displays the full name and email address of the member.
* **Role**: A dropdown that allows you to set or update the user’s administrative role:
  * **Owner**: Full control over the workspace.
  * **Admin**: Access to most workspace management functions.
  * **+ Billing contact**: (Checkbox) Receives billing-related communications.
  * **Billing only**: (Button) Limits the member to billing management tasks.

**Additional options:**

Each admin row has a three-dot menu offering:

* **Remove from Admin members**: Revoke administrative privileges.
* **Remove from workspace**: Completely remove the user from the workspace.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FjvjwFLEt9xotsiKVcX3j%2Fscrnli_hRg3q01U3ivPsa.png?alt=media&#x26;token=62ef6fce-4d55-4ee1-a8b1-00d7c1997e96" alt=""><figcaption></figcaption></figure>

## Inviting coworkers to the Workspace

You can use Bito in a single-player mode for all the use cases. However, it works best when your coworkers join the Workspace to collaborate with Bito. There are three ways you can invite your coworkers.&#x20;

**Option 1** - Allow your work e-mail domain for the Workspace. This setting is turned on by default, and all users with the same e-mail domain as yours will automatically see the Workspace under "Pending Invitations" when signing up in Bito. You can manage this setting after you create the Workspace through the "Settings" page in your Bito account.&#x20;

{% hint style="info" %}
You may still need to notify your coworkers about Bito and share Bito workspace URL. We don't send e-mails to your coworkers unless you invite them to the Workspace.&#x20;
{% endhint %}

**Option 2** - Invite your coworkers via e-mail when you create your Workspace or later from your workspace setting.&#x20;

**Option 3**- Share a web link specific to your Workspace via the channel of your choice: e-mail, Slack, or Teams. The link is automatically created and shown when creating a workspace or on the workspace settings page.

## Adding Admin members

To add a new admin:

1. Click the **“Add members”** button at the top of the Admin tab.
2. In the popup:
   * Select an existing user from your workspace, **or**
   * Invite a new member by entering their email address.
3. Assign the appropriate role and permissions as needed.
