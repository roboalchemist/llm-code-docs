# Source: https://docs.ox.security/admin-settings/settings.md

# Settings

{% hint style="success" %}
**At a glance:** Manage organization-wide and personal settings so that OX works best for you and your organization.
{% endhint %}

## Overview

As its name suggests, the **Settings** page is the place to manage the settings that affect how you and your organization work with OX. View and manage different categories of settings by switching among the tabs at the top of the page:

* [Organization](#organization)
* [Usability](#usability)
* [Scan](#scan)
* [Applications](#applications)
* [Notifications](#notifications)
* [Login](#login)
* [API keys](#api-keys)
* [Secrets](#secrets)

![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6244307eb6f38c7d8eb5bf804728699548321851%2Fsettings_page.png?alt=media)

<details>

<summary>Organization</summary>

In the **Organization** tab, you can:

* View and edit the name of your organization (as it appears in the OX interface)
* View and copy the organization ID
* Delete the organization

**Deleting an organization**

**Caution!** Deleting an organization removes all its data from the OX system (including scan history and audit logs). Once the organization is deleted, it can't be recovered. Be very certain this is what you want to do before you proceed.

**To delete an organization:**

1. In the **Delete organization** section, click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-09e273022b9240efdcca424cc9c931faf13ae031%2Fdelete_button.png?alt=media" alt="" data-size="line"> button.
2. In the dialog, confirm your action by typing the verification text and clicking **Delete.** \\

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-03e23a2a3e165f0889d7fb3fd90bef90904f172d%2Fdelete_organization_dialog.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

</details>

<details>

<summary>Usability</summary>

</details>

<details>

<summary>Scan</summary>

</details>

<details>

<summary>Applications</summary>

</details>

<details>

<summary>Notifications</summary>

</details>

<details>

<summary>Login</summary>

In the login settings section you can manage your OX Security login options.

<img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8821908262abe6b3fe4a5e0814e63b58656c84ce%2Fimage.png?alt=media" alt="Login settings" data-size="original">

The green icon on the login options indicates that the respective login option is configured and approved.

You can revoke the configured login option by clicking on the respective option and selecting the revoke option.

<img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cb12a54224108e02cf52f5daa86879a71555859c%2Fimage.png?alt=media" alt="Revoke login" data-size="original">

This will remove this login option from the options the user sees when he logs into OX.

**Configure login**

You can configure the new login option by clicking on it and providing the required details.

<img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a112ffd09e0b11c7b918ac2a452d9a3b1846c22d%2Fimage.png?alt=media" alt="Configure login" data-size="original">

Every login option has its own configuration e.g to configure Azure AD SSO, you need to specify the Azure domain, client ID, and client secret. You can follow the list of instructions provided by us for configuration.

</details>

<details>

<summary>API keys</summary>

The OX API supports authentication via API key, passed in an HTTP header.

**Create an API key**

**To create an API key for use with the OX API:**

1. Click the **CREATE API KEY** button.

   Click to zoom
2. In the **Create API Key** dialog:
   1. Enter a name that will help you identify your API key later.
   2. Under **API Key Type,** select the **API Integration** option.

      Click to zoom
   3. \[optional] Change the expiration date of the API key.
      * By default, the expiration date is set to one year from the time you created it.
   4. Click the **CREATE** button.
   5. The **API Key Secret** will be displayed. This is what you’ll use in the [authorization header](https://www.notion.so/Working-with-the-OX-API-62f91e59c1104a20b37f6a969dfceb01?pvs=21) of your API calls.

      \*\*Important:\*\* Be sure to copy the \*\*API Key Secret\*\* to your clipboard before closing the dialog; then, paste it immediately into a secure location, such as a password manager. Once you close the \*\*Create API Key\*\* dialog, you won’t be able to access the \*\*API Key Secret\*\* again. (So, if you haven’t copied it, you’ll need to create a new key.)

      Click to zoom
   6. Click the **DONE** button to close the dialog.
3. The API key you created is now displayed in the table.

   Click to zoom

</details>

<details>

<summary>Secrets</summary>

</details>
