# Source: https://jam.dev/docs/administration/members-and-roles.md

# Members and Roles

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FqDWnIMOIDB2eFFPdaBsA%2FSetting_%20Members%20and%20Roles.png?alt=media&#x26;token=70447e13-e64a-47ac-8a29-6f4d7ae3c622" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Available to workspaces on our [Team](https://jam.dev/pricing) or [Enterprise](https://jam.dev/pricing) plans.
{% endhint %}

### **Overview**

Jam currently offers two seat types: **Viewer** (free) and **Creator/Admin** (paid). Each seat type provides different levels of access and functionality within your team workspace. Your workspace’s plan, along with the number and type of paid seats, determines your subscription cost.

Here’s how these seat types work:

<details>

<summary>Viewer (free)</summary>

The **Viewer** seat is a free role that makes collaboration easy. Viewers can access and comment on Jams but cannot create or manage them in team workspaces.

Viewers can self-upgrade to a **paid Creator seat** by taking certain actions within your team workspace, such as:

* Creating a Jam
* Creating a recording link
* Sending a Jam to an integration
* Moving a Jam into a paid team via any integration

{% hint style="info" %}
**Note:** Viewer seats are not available on pro and business legacy plans.
{% endhint %}

</details>

<details>

<summary>Creator (paid) <code>default</code></summary>

The **Creator** seat is a paid role designed for team members who actively create and manage content within your team’s workspace. Creators have full capabilities, including:

* Creating, moving, and deleting Jams and recording links
* Moving content between teams and integrations
* Actively collaborating within a paid team workspace

Creators impact your workspace’s billing, as each Creator occupies a paid seat.

{% hint style="info" %}
**Note:** By default, all new users join your workspace as creators.
{% endhint %}

</details>

<details>

<summary>Admin (paid)</summary>

The **Admin** seat is a paid, permanent role intended for managing workspace settings and members. Admins have all Creator capabilities, plus additional management privileges, including:

* Managing workspace settings and member roles
* Controlling billing and subscription details
* Upgrading or downgrading members between Viewer, Creator, and Admin roles

Admins also occupy a paid seat and directly impact your billing.

</details>

### **Examples of seat combinations and billing impact**

Since your team workspace’s cost depends on seat types, here are common scenarios:

1. **Only free seats:**
   * **Alex** is invited to view Jams, give feedback, and comment occasionally but does not create new Jams. Alex uses a **Viewer seat** and remains free, not impacting your team’s workspace billing.
2. **Free and paid seats:**
   * **Riley** is a product manager who creates Jams regularly. Riley uses a **Creator seat** and is a paid member of the workspace.
   * **Joe** is a developer and uses a **viewer seat** to view and comment on Jams created by Riley. Joe’s viewer seat is a free member of your workspace.
   * **Jordan** frequently manages team members and workspace settings. Jordan has an **Admin seat** and is also a paid member.
3. **All paid seats:**
   * **Taylor** actively creates recording links, collaborates on integrations, and manages the workspace. Taylor holds both Creator and Admin capabilities under an **Admin seat**, impacting your billing.

{% hint style="info" %}
**Note:** On legacy Pro and Business plans, workspaces have a included seat amount

* **Pro:** 2 seats included
* **Business:** 10 seats included

If your workspace exceeds this seat quota, additional creator and admin seats are billed at an extra per-seat rate ($8 per additional seat). Viewer seats are not available on pro and business legacy plans.
{% endhint %}

### **How do people get a paid seat?**

1. **Self-upgrade (Viewer → Creator)**

   Viewers can automatically upgrade themselves to a paid Creator seat by performing specific actions:

   * **Create** a new Jam
   * **Create** a new recording link
   * **Move** or copy a Jam into a paid team via an integration
   * **Send** content to an integration, triggering active collaboration
2. **Upgrade via Admin**

   Admins can manually upgrade a Viewer to a Creator or Admin seat anytime. They can also downgrade Creators back to Viewers (free) or switch Creator roles to Admin roles.

   * On Pro and Team plans, workspace Admins fully manage seat types and billing adjustments.
   * Admins receive notifications each time someone upgrades their seat automatically or manually, helping maintain control of your workspace billing.

{% hint style="info" %}
**Example:** Casey is initially assigned a Viewer seat. Casey creates a new Jam to collaborate actively with their team. By creating that Jam, Casey automatically upgrades from a Viewer seat to a Creator seat, which updates the workspace billing
{% endhint %}

### **Managing Seats**

#### **Manage seats on Team plan**

On Team plan, workspace Admins control seat management directly. Here’s how Admins can manage user seats:

1. Go to your workspace settings page.
2. Select the **Team** tab.
3. Choose the member whose seat you want to manage.
4. Click their seat type (**Viewer**, **Creator**, or **Admin**) and select a new seat type from the available options.

#### **Manage seats on Enterprise plans**

If your workspace uses Single Sign-On (SSO) and Active Directory sync, you’ll need to manage member roles directly through your Identity Provider (IdP) and Active Directory. You won’t be able to manage these roles directly in Jam.

{% hint style="info" %}
**Note:** You cannot downgrade someone to a Viewer seat if you want to prevent future self-upgrades. (If desired, contact support to explore advanced restrictions.)
{% endhint %}

#### **Manage seats on Legacy Plans**

On Pro and Business plans, workspace Admins control seat management directly. Here’s how Admins can manage user seats:

1. Go to your workspace settings page.
2. Select the **Team** tab.
3. Choose the member whose seat you want to manage.
4. Click their seat type (**Creator**, or **Admin**) and select a new seat type from the available options.
