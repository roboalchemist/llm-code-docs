# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-teams.md

# Managing Tabnine Teams

## Logging into Admin Console <a href="#logging-into-admin-console" id="logging-into-admin-console"></a>

Once installed, your instance already has your first admin user set up.

The first admin's user name is set according to the email provided in the installation process (referred to as "first admin user" during setup).

To retrieve the initial password for the first admin user, run the following command on your Kubernetes cluster:

```bash
kubectl -n default get secret default-password --template=‘{{.data.password | base64decode }}
```

Once you get the initial password:

1. Enter your Tabnine instance URL in your browser.
2. Login to Tabnine using your username and password:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c876bb72e866dad95bdafa5a92b99108eaaa989f%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Make sure you change the first admin user password, since the initial password can be viewed by anyone using the above command.

\
To change your password, click the **Forgot your password?** link.
{% endhint %}

![image.png](https://cdn.document360.io/bad30e15-930b-48d6-8f2e-c94ca3858c20/Images/Documentation/image\(13\).png)

## **Setting up your organization**

To achieve the full potential of your Tabnine Enterprise Server, we recommend reviewing the following documentation:

1. [Tabnine teams](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-teams)
2. [Roles in an enterprise](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/roles-in-an-enterprise)
3. [Inviting users to your organization](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/inviting-users-to-your-team)

After installing the Tabnine Enterprise Server, the next step will be to onboard your colleagues and teammates so they can start using Tabnine.

## Tabnine Teams <a href="#tabnine-teams" id="tabnine-teams"></a>

Tabnine's authorization system is based on different teams within your organization. A team is a group of users who are using Tabnine.

On installation, your organization will already have one default team, but you can create multiple teams according to your organizational structure.

#### **Why use different teams?**

1. The team structure makes it easier to manage Tabnine authorization within your organization. We recommend creating the teams according to your organizational structure to allow for better control.
2. A team is also a unit of measure for monitoring Tabnine's performance within your organization.
3. Access and connections are managed at the team level, where each user only has access to repos that are connected to their specific team.

### **Onboarding a Team**

To permit teammates to access Tabnine, they must receive an invitation to become authorized users. This approach is designed to prevent unauthorized usage of Tabnine and enables administrators to ensure it reaches the intended audience.

**There are 2 ways to onboard new users to Tabnine:**

1. Via the link in an email invitation
2. Via an invitation link

As mentioned previously, Tabnine's default installation already contains your default team. If you don't require additional teams, you can skip the next section (Managing teams) and skip straight to the [Inviting users to your organization](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/inviting-users-to-your-team) article where both invitation options are covered at length.

### **Managing Teams**

**Creating a team**\
To create a new team (Admin or Manager role):

1. Navigate to **Team Members**
   1. Click **Create new team** on the top right-hand corner of the screen
2. Alternatively, at the bottom of the **All Teams** dropdown menu, click **Create new team**
3. Finally, on the **Teams** page, you can select the <mark style="background-color:blue;">+</mark><mark style="background-color:blue;">**Create a new team**</mark>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6c727a2c4e57b230014e2ed0194701f670f1a409%2FTeams%20screenshot.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-57aa5cfa98fe10155396055d1306d832ce5bcb4c%2FCreate%20New%20Team.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Edit a Team Name or Delete a Team**

To edit or delete/remove a team, click the **edit**/**trash bin icon** next to the team's name in the <mark style="background-color:blue;">**All Teams**</mark> dropdown.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6dca0a7c19cca35aaeec3c5b5418d5494c85da7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Important note about team deletion

1. Only Admins can delete teams.
2. Deleting a team will remove the team and disband all the current team users.

For users of the removed team to continue using Tabnine, they'll have to receive and accept another invitation and select their team to join.

For more details on how to invite users to a team, see [Inviting users to your organization](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/inviting-users-to-your-team).
{% endhint %}

### Viewing users who are not assigned to a team

Some users are not assigned to a team, which can happen after a team admin removes a user from a team or deletes a team.

Users who aren't part of a team can't work with Tabnine until they join a new team.

To view these users, go to the Teams page and select the **Not assigned to a team** option in the Team dropdown:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-14beda3fba2c9db4d1ab2d9b36c7801854ccd2f3%2FSH%20Unassigned%20to%20a%20team.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Adjusting Teams' Permissions

On the separate Teams page, you can see *how many* members and repos that particular team has.

Additionally, you can grant access to individual teams for Code Review under "Review" or Agent by checking or unchecking that option, as seen below:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-154930afb34c0b71c45f4bc2b0bbf8503bcaed59%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
