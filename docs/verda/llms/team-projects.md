# Source: https://docs.verda.com/welcome-to-verda/team-projects.md

# Team Projects

## Create New Project

There are two different ways to create a new cloud project: via the Project dashboard or the Project menu.

Create a new project from the **Project dashboard** by clicking the **Create new project** button on the top right corner of the screen.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-e02aecd85651e0fdb8d3e25be31609be54507f9b%2Fcreate%20project%201.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also use the **Project menu** found within the navigation sidebar by opening the drop down menu and clicking **Create new project** option.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-267df5e7970a9e807711fd9672e1e323332a6b1a%2FCreate%20project%202.png?alt=media" alt=""><figcaption></figcaption></figure>

Input the project name and any email addresses of team members you would like to invite, and click **Create project**. (See more about [inviting team members](#invite-team-members)).

***

## Delete a project

You can delete any project of which you are the **Owner**. On the project dashboard, open the settings menu on the project card and click **Delete**.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-b060abcf1a13c672909c101b156dfc3658ca8bcb%2FDelete%20Project.png?alt=media" alt=""><figcaption></figcaption></figure>

Any remaining balance within that project will be sent to your **Unallocated funds** in **My Account** page, [see Transfer Funds](#transfer-funds).

{% hint style="warning" %}
You must delete or transfer all instances and volumes from a project to enable deletion.
{% endhint %}

***

## Project billing

Project payment methods and billing information (including address, company name, and business ID) are always associated with the **Owner** of the project.

Billing information can only be edited by the project owner in their **My Account** page. Project admin can view this billing information in the **Billing & Settings** page.

Payment methods are added by the project owner. Both owner and admin can view the payment methods and choose which ones to use for topping up the account, including automatic top-up.

Project developers can create and manage resources, but do not have access to view or edit billing and payment details.

[View role permissions](#role-permissions)

***

## Transfer funds

When a project is deleted, any remaining funds from that project will be transferred to your **Unallocated balance** in the **My Account** page.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-1d5fdd12f0589d66a61090b68eb7c4281c18707f%2Funallocated%20balance.png?alt=media" alt=""><figcaption></figcaption></figure>

From the Unallocated balance, funds can be transferred to any other project you own.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-a9706c81a813026ab459b73464bc69b39c02f938%2FTransfer%20funds%20modal.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You must be the **Owner** of a project to transfer funds into it.
{% endhint %}

***

## Transfer resources

You can transfer active compute and storage between projects. In order to transfer resources, you must be the **Owner** of *both* the source and target projects.

{% hint style="info" %}
When transferring *Pay As You Go* resources, the target project must have enough balance to cover **at least 30 minutes** of the transferred resources.
{% endhint %}

### Transfer compute between projects

You can find **Transfer to new project** in the Actions menu on the compute cards or in their specific pages. Compute can remain running during the transfer. There is no need to shutdown instances, unless you want to detach storage first.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-a6b794f2715a02a3a4721921343d2ff9a56cb3a1%2Ftransfer%201.png?alt=media" alt=""><figcaption></figcaption></figure>

Choose which project the instance will be transferred to and click **Transfer compute**. All attached block volumes will be transferred with the instance.

### Transfer block volumes between projects

{% hint style="info" %}
Volumes must be detached before individual transfer is enabled. OS Volumes can only be detached by deleting the instance for which they are used as the main OS.
{% endhint %}

On the **Block volumes** screen, open the settings menu of the volume you would like to transfer. Click on **Transfer**, select the target project, and click **Transfer volume**.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-c8456521132b55839230d8d6bec15eeafc080917%2Ftransfer%20volume.png?alt=media" alt=""><figcaption></figcaption></figure>

### Transfer shared filesystems between projects

Currently, you cannot transfer shared filesystems between projects as they may be shared to other compute. We are working hard on improving this feature.

Feel free to reach out to us for assistance via the chat on the console or email <support@verda.com>.

***

## Invite team members

Invite team members from the **Team** page. Click the **invite** button on the top right of the screen.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-8ea4fb0eda6596da8845b055ffaac98759dd3230%2FTeam%20screen.png?alt=media" alt=""><figcaption></figcaption></figure>

Input email addresses of the team members you would like to add. Choose a role for them using the menu. View role permissions below.

They will receive an email invitation with a link to accept and join the project. You will see when they have accepted the invitation next to their information on the **Team** page.

***

## Roles

Team members are given different roles with various permissions:

* **Owner** is the user that created a project. Owners have all permissions.
* **Admin** have almost all permissions, except editing projects or editing billing information.
* **Developer** can only deploy instances, create volumes, and manage project resources.

### Role Permissions

<table><thead><tr><th width="401">Project Permissions</th><th data-type="checkbox">Owner</th><th data-type="checkbox">Admin</th><th data-type="checkbox">Developer</th></tr></thead><tbody><tr><td>Deploy and manage instances</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Create and manage volumes</td><td>true</td><td>true</td><td>true</td></tr><tr><td>View Auto top-up settings</td><td>true</td><td>true</td><td>true</td></tr><tr><td>Edit Auto top-up settings</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Top-up project balance</td><td>true</td><td>true</td><td>false</td></tr><tr><td>View billing information</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Invite team members</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Change team member roles</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Transfer resources between projects</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Rename project</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Change default payment card</td><td>true</td><td>true</td><td>false</td></tr><tr><td>Add/delete payment card</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Edit billing information</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Transfer funds between projects</td><td>true</td><td>false</td><td>false</td></tr><tr><td>Delete project</td><td>true</td><td>false</td><td>false</td></tr></tbody></table>

### Changing roles

Project **Owner** and **Admin** can change the roles of other team members using the menu in the **Team** page.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-3022e2983e1fda23c89ce9c9cbd07b9d12cd3152%2Frole%20change.png?alt=media" alt=""><figcaption><p>Change role or remove team members</p></figcaption></figure>

***

## Remove a team member

On the **Team** page, click on the role menu associated with the team member you would like to remove and click **Remove** (see image of menu above). You must confirm the removal of the team member.

For security purposes, all Cloud API keys the team member created will be deleted upon their removal. Contact us via chat or email <support@verda.com> if you need assistance.

***

## Leave a project

If you are a team member of a shared project, you can leave a project from your role menu on the **Team** page (see image above) or from the settings menu on the Project card.

For security purposes, all Cloud API keys you created will be deleted upon leaving. Contact us via chat or email <support@verda.com> if you need assistance.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-0eb8ce4126982cd84da1167df0f85c5f2a9bb134%2Fleave.png?alt=media" alt=""><figcaption></figcaption></figure>

***

## How to find the Project ID

Your Project ID is essential for troubleshooting, so please have it ready when reaching out to our support team. Project IDs can be found from the URL or copied from the **Project** card on the Project list screen.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-077088c0cfb5e1073cf782cabf94b8064747074e%2Fproject%20ID.png?alt=media" alt=""><figcaption></figcaption></figure>
