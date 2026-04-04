# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/idp-sync.md

# IdP Sync

IdP Sync in Tabnine implements automatic user provisioning and de-provisioning, replacing manual user management.

Tabnine offers an IdP sync functionality based on the SCIM 2.0 protocol. IdP Sync uses the SCIM Users API to manage new users and existing users. Changes made in the IdP (add/remove users) are reflected in Tabnine automatically.

IdP sync is available for Enterprise customers using either self-hosted (private) installations or Enterprise SaaS users (console.tabnine.com).

### User Types

All users are either “*registered*” (active) or “*deactivated*” (inactive). There are no hard deletes in the Tabnine system, so admins must deactivate a user (not delete).

{% hint style="info" %}
Tabnine plans to implement the SCIM Groups API in the near future for role and team management.
{% endhint %}

Newly synced users (users that have never been registered before) will receive an email upon registration, By default, they will be designated *registered users*.

Existing users will be synced by email match and given the status of synced users. Once they are synced, they can only be managed by the IdP and not manually.

{% hint style="danger" %}
Unrecognized users are those users that already exist in Tabnine but for some reason aren’t found in the IdP. This could be due to a misconfiguration in the IdP itself. These users continue to be managed manually.
{% endhint %}

### Team and Role Assignment

Team and role management is currently manual. Whenever a user is added to the system, that user has a default status of “member.”

Admins would assign new roles to users, such as “admin,” by changing the “member” status.

Team assignments are critical in Tabnine IdP Sync. Without a team assignment, the user *cannot* work.

Admins have the option to automatically assign new users to a default team so they can work immediately (and move them to a different team manually), or to leave them unassigned.

Admins may choose to leave users unassigned for different reasons, but an unassigned member still counts toward the number of licenses your organization uses with Tabnine.

{% hint style="warning" %}
We advise these team-less users not to be left that way in the long-term (if a member user is not active for the long-term, set that user to “deactivated”).
{% endhint %}

{% hint style="danger" %}
*Unsynced Users:* An error may occur where users not recognized by the IdP remain unchanged unless manually updated.
{% endhint %}

### Test Mode and Live Mode

IdP Sync can be set to either Test Mode or Live Mode. Live Mode will apply IdP updates in real time with sync happening continuously.

To push updates, ensure the IDP is properly configured. The first sync can take up to an hour.

It is a *best practice* to start with Test Mode. Ensure that your SCIM configuration is set properly.

Test Mode will simulate and preview changes in IdP Sync, but not apply them. If admins are satisfied with the preview, they can push the changes live.

### How to Set Up IdP Sync

Users must request activation from an account manager or Tabnine Support, as IdP Sync is not available by default.

Once given access, admins must follow the three following steps:

First, enable **IdP Sync** in the Admin Console, choosing **Test** or **Live**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c26684880ee809446e961d00ae35ce8b67859992%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, generate SCIM API key.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9bd861774cf8d03dccbb88e4a82ced882b032807%2FSCIM%20API%20key%20(1).gif?alt=media" alt=""><figcaption></figcaption></figure>

### Configuring your Identity Provider for IdP Sync

Back in your IDP (Okta, Entra ID, etc.), add the 1) Tabnine SCIM URL and 2) API key.

#### Azure Entra ID <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9288c7921771207cbb2c42cb9b757df708a0e4fa%2Fazure%20logo.svg?alt=media" alt="" data-size="line">

{% hint style="info" %}
*If you do not already have* an existing Tabnine application in Azure Entra ID, follow these instructions:

1. Set up an enterprise application. Navigate from:\
   **Enterprise Applications > New Application > Create your own application**
2. Next, name it Tabnine and choose "**Integrate any other application you don't find in the gallery**."
   {% endhint %}

Navigate to your Tabnine application.

Click on **Get Started** and then choose **Automatic**.

At this point, add a) the *Tabnine SCIM URL* ***and*** b) the *Tabnine-generated API key*.

Select **Test the connection**.

In the **Provisioning** section, select "**Sync only assigned users and groups."**

Once in place, hit **Start**.

**Provisioning**

Enter your [Azure Portal](https://azure.microsoft.com/en-us/get-started/azure-portal) and press **Sign In**.

Next, under Azure Services, click the icon for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-153f0bd4000178122e8e8a1a89b385614027788d%2FMicrosoft_Entra_ID_color_icon.svg.png?alt=media" alt="" data-size="line"> Microsoft Entra ID:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-768c216095b028af2a0b4431ff1fa828dedecb1a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

On the lefthand side menu, click on the **Manage** dropdown and select **Enterprise applications**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-48f74a2660b5195d47a09df4f36cd70e5e2a15fa%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Next, choose **Tabnine Self Hosted.**

Within that application, go to the lefthand side menu and choose the **Manage** dropdown. Select **Provisioning**:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9b117563b7d5b5d4af8f88a471d2d69c4d7c09be%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

After that, go to New Configuration. Once there, enter your Tenant URL with the following format:

`baseUrl/scim/v2`

For example:

```
https://idp.tabnine.io/scim/v2
```

Retrieve a secret token by entering the following URL formula for creating it:

`baseUrl/organization/idp/scim-key`

Next, run **Test Connection**.

Then run **Create**.

Under this <mark style="color:blue;">new provisioning configuration</mark>, go to **Manage** and again to **Provisioning**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0707a9b042df4dfb164da9b8932c96a1617e6024%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Open **Mappings** and select <mark style="color:blue;">Provision Microsoft Entra ID Groups</mark>:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fcccfc921f53188dafca42b7afc93a3a7583e88b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Set the **Enabled** column to **No** and hit **Save**.

Then select <mark style="color:blue;">Provision Microsoft Entra ID Users</mark>, where you will delete any mappings until you are left with the following configuration:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-722753613610d0ef13560f992ad636836d8a4fc3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Click Save.

Finally, go back to <mark style="color:blue;">ⓘ</mark> **Overview** and click <mark style="color:blue;">**▷**</mark> Start provisioning:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-dc8f97b217049795f23828cb092cc66927f048e2%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Okta <picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5e007ad462944a955a0a5cdeb108fec4f05fbdd4%2FOkta_Aura_White_L.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-498d994363f704ce6b160eee04153dd8ca5128bb%2Fokta-logo.png?alt=media" alt="" data-size="line"></picture>

Head over to Okta. On the lefthand side menu, select **Applications**, then select your Tabnine app.

Next, navigate from **General > App Settings > Edit**. Then, check off **Enable SCIM Provisioning** and hit **Save**.

Proceed to **Provisioning**.

Add your *Tabnine SCIM URL* under **SCIM connector base URL**.

Under **Authentication Mode**, Select "HTTP Header."

Now add your *Tabnine-generated API key* under **HTTP Header - Authorization**.

Once in place, hit **Save**.

{% hint style="info" %}
The sync cycle only starts when the IdP initiates it and the Tabnine SCIM service is running with a valid token. Syncs (e.g., from Entra ID) may take up to an hour.
{% endhint %}

### **Disabling IdP Sync**

When disabling IdP sync, admins can choose to convert all synced users to unsynced users, ***or*** deactivate all synced users.\\
