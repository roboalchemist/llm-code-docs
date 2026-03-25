# Source: https://docs.tokens.studio/token-storage/manage-sync-provider.md

# Manage Sync Providers

## Manage sync providers

By default, Design Tokens created with Tokens Studio are stored locally in each Figma file, accessed by opening the plugin.

If you want to share your Tokens across multiple Figma files or store them externally (not in Figma), you can set up remote Token storage with one of our integration partners and add them as a **sync provider** in the plugin.

### Steps in the plugin for Figma

Open the Tokens Studio plugin and navigate to the **settings** page.

* Tap the **Add new sync provider**
* A **modal** will open with **a list of providers** to choose from.
* Tap the **Choose** button next to the provider you want to add

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FOdhqxEaFm37SlxMbIHkZ%2Fsettings-page-addNewSyncProvider-v2-0.png?alt=media&#x26;token=4ec5817c-5947-4b63-9234-0044d9718443" alt=""><figcaption></figcaption></figure>

### Sync provider credentials

Once you select your sync provider, a **modal** will open with a form to **add the necessary credentials**.

\
Each provider's form will look slightly different. If you need help on how to fill out the form, make sure to check out their specific documentation for detailed instructions.&#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>GitHub</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPQX5WYH7zZUsIvcoDu3S%2Fgithub-card-header-sync-provider.png?alt=media&#x26;token=1bd8963c-cabf-4bc9-9409-040d28adab40">github-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-github">sync-git-github</a></td></tr><tr><td>Gitlab</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FpRqNTyIaZapd1SqRohSz%2Fgitlab-card-header-sync-provider.png?alt=media&#x26;token=4cc49ccd-8a17-48cb-9167-093cd60287d0">gitlab-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-gitlab">sync-git-gitlab</a></td></tr><tr><td>Azure DevOps</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2OYQvS12rKDRw2RxZeos%2Fado-card-header-sync-provider.png?alt=media&#x26;token=568ad820-6e59-4db3-b16e-479e4ad7a6d0">ado-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-azure-devops">sync-git-azure-devops</a></td></tr><tr><td>Bitbucket</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FewmX1Q0F9XnNSRbYyksO%2Fbitbucket-card-header-sync-provider.png?alt=media&#x26;token=23434d72-e1b1-49d2-824a-7ea31deb1aaf">bitbucket-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-bitbucket">sync-git-bitbucket</a></td></tr><tr><td>JSONBin</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FASrFKEtxsqtYlq5xX2NL%2FJSONBIN-card-header-sync-provider.png?alt=media&#x26;token=731d0f95-1c37-4f6b-9ce3-9b13834bba92">JSONBIN-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-jsonbin">sync-cloud-jsonbin</a></td></tr><tr><td>Supernova</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FsbhdiY2yFHg9Dgv20a1c%2FSUPERNOVA-card-header-sync-provider.png?alt=media&#x26;token=e162c759-26d8-4165-8f14-0e5c10e41e63">SUPERNOVA-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-supernova">sync-cloud-supernova</a></td></tr><tr><td>Token Studio Platform</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDlVTT6lCDHtCxHltCRwZ%2FSTUDIO-card-header-sync-provider.png?alt=media&#x26;token=ca22b02a-4e2a-4293-a1b1-7453ed22990b">STUDIO-card-header-sync-provider.png</a></td><td><a href="remote/sync-cloud-studio-platform">sync-cloud-studio-platform</a></td></tr><tr><td>URL</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F4i5dEQKmUjLeSAYIUi2M%2FURL-card-header-sync-provider.png?alt=media&#x26;token=3a7d114e-6f2e-4d87-8e19-1ffb3935a661">URL-card-header-sync-provider.png</a></td><td><a href="remote/sync-server-url">sync-server-url</a></td></tr><tr><td>Generic Versioned </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FvOdY6AksQcUtuMUY42AT%2FGENERICVERSION-card-header-sync-provider.png?alt=media&#x26;token=ec54fe57-e05b-4690-8567-dbd45b97e675">GENERICVERSION-card-header-sync-provider.png</a></td><td><a href="remote/sync-server-generic">sync-server-generic</a></td></tr></tbody></table>

Select **Save** to continue. Sometimes you have to scroll the form to see the **save** button.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FqowGOyHpqu21lJcT5T0Z%2Fsync-save-button-cutoff-annotated-v2-0.png?alt=media&#x26;token=5b9198fb-6b42-4d86-8fd9-263de80cbcf4" alt=""><figcaption></figcaption></figure>

### Save and do the initial sync

Once you **Save** your credentials, the plugin will compare your Tokens with whats in your repository.

You'll see a modal asking you to **push** or **pull** to 'sync' the plugin data with your storage provider, depending on the type of provider, permissions, and the Tokens you have in the plugin.

These images show the **push** and **pull** modals for a new GitHub sync, but it will look similar for most providers.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fciz3wA0SQRb3Av91RhjC%2Fsync-git-push-pull-modal-v2-0.png?alt=media&#x26;token=6d840795-d0cc-44ba-a81a-4c707c216b1e" alt=""><figcaption></figcaption></figure>

**Pull from provider**

If your sync provider already has Design Tokens, you'll see a dialogue asking if you want to **pull** your Tokens in.

* If you select **yes**
  * Tokens in your remote storage will be **pulled** into the plugin.
  * Any Tokens currently in the plugin will be replaced with the Tokens in your remote storage, and they can not be recovered.
  * Once the pull is complete, the modal will close and you'll be returned to the **Settings** page of the plugin.
* If you select **cancel**
  * Tokens currently in the plugin will remain, and you can choose to push them to your sync provider later.
  * The modal will close and you'll be returned to the **Settings** page of the plugin.
* If you close the modal without making a selection
  * Tokens currently in the plugin will remain, and you can choose to push them to your sync provider later.
  * Closing the modal returns you to the **Settings** page of the plugin.

Read the Sync Changes guide for more details

{% content-ref url="remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

**Push from local**

If your sync provider does not have code files with Design Tokens, you'll see a modal asking if you want to **push**.

This would **push** or "send" the current Tokens in the plugin to your sync provider.

* If you select **Push changes**
  * The **commit message** is required.
    * You can think of it as a short note to your engineers about what you are **pushing**, such as "initial token load."
  * Tokens in the plugin will be **pushed** to your remote storage.
  * Once the pull is complete, the modal will close and you'll be returned to the **Settings** page of the plugin.
* If you select **cancel**
  * Tokens currently in the plugin will remain, and you can choose to push them to your sync provider later.
  * The modal will close and you'll be returned to the **Settings** page of the plugin.
* If you close the modal without making a selection
  * Tokens currently in the plugin will remain, and you can choose to push them to your sync provider later.
  * Closing the modal returns you to the **Settings** page of the plugin.

### Sync provider is active

Once your sync provider is connected, it appears on the **settings page** as **Active**. The plugin will tell you which **Token Format** your JSON files are being written in.

{% content-ref url="../manage-settings/token-format" %}
[token-format](https://docs.tokens.studio/manage-settings/token-format)
{% endcontent-ref %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FbPpjQb9sxGHTzQi9WTru%2Fsettings-page-sync-actions-push-v2-0.png?alt=media&#x26;token=4f7e731e-7971-4ba4-83f6-8dee43c23220" alt=""><figcaption></figcaption></figure>

You'll notice the **sync actions** at the bottom of the plugin are now visible. These actions indicate when the plugin is out of sync with the Tokens in remote storage.

* **Push** indicator:
  * Visible when changes you've made in the plugin need to be sent to the code files stored by your sync provider.
* **Pull** indicator:
  * Visible when the plugin needs to "receive" changes made to the code files stored by your sync provider.

Read the Sync Changes guide for more details

{% content-ref url="remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FNekgLAShpNgDdFszzTKI%2Fsync-actions-none-v2-0.png?alt=media&#x26;token=ad56e95a-35b6-499e-a71f-92fb5dad34d6" alt=""><figcaption></figcaption></figure>

### Pro tips for working with Sync providers

Once your sync provider is active, here are some workflow tips from the Tokens Studio team and community.

#### Save a copy of your sync provider credentials

Capture a copy of the credentials you filled in the form and store them somewhere for safekeeping.

* If you need to re-add the sync provider to the plugin, you'll have a record of what you put in each section of the form as a reference.

#### Share Tokens between Figma files

Once the sync provider is added, Tokens stored by your sync provider are easily accessed in any Figma file without needing to add the credentials again.

Once you open the Tokens Studio plugin in any Figma file:

1. Navigate to the **settings** page of the plugin
2. Navigate to the **sync provider** of your choice in the list and select **apply**
3. The **pull from provider** modal will open, asking if you want to **pull** in the Tokens being stored externally.
   * Follow the **Pull** steps above.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDq4QvYXPHhm1tDXGmv0o%2Fsync-pull-modal-v2-01.png?alt=media&#x26;token=e43b196d-772b-4bf4-943f-59cce4c66d48" alt=""><figcaption></figcaption></figure>

Once you've completed the **Pull** from your sync provider, your Tokens will be available in your new Figma file.

* If your sync provider has **write** permissions, changes you make in the new Figma file can be **Pushed** back to the sync provider and then **Pulled** into other Figma files.

***

### Resources

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - Open issues for [Sync Providers Manage](https://github.com/tokens-studio/figma-plugin/labels/sync%20providers%20manage)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None yet

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
