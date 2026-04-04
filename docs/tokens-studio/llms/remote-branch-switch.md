# Source: https://docs.tokens.studio/token-storage/remote-branch-switch.md

# Branch Switching (pro) - Version Control

## Branch switching (pro)

> The **Multi-file sync to remote storage** feature requires a [Pro Licence](https://tokens.studio/pricing) for Tokens Studio. Read the guide for more details.&#x20;

If you are working with one of these Git sync providers and have a Pro Licence for Tokens Studio, you can use the plugin native integration to take advantage of **branch** workflows to version control changes to your Tokens:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>GitHub </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPQX5WYH7zZUsIvcoDu3S%2Fgithub-card-header-sync-provider.png?alt=media&#x26;token=1bd8963c-cabf-4bc9-9409-040d28adab40">github-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-github">sync-git-github</a></td></tr><tr><td>Gitlab</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FpRqNTyIaZapd1SqRohSz%2Fgitlab-card-header-sync-provider.png?alt=media&#x26;token=4cc49ccd-8a17-48cb-9167-093cd60287d0">gitlab-card-header-sync-provider.png</a></td><td><a href="remote/sync-git-gitlab">sync-git-gitlab</a></td></tr><tr><td>Azure DevOps</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2OYQvS12rKDRw2RxZeos%2Fado-card-header-sync-provider.png?alt=media&#x26;token=568ad820-6e59-4db3-b16e-479e4ad7a6d0">ado-card-header-sync-provider.png</a></td><td></td></tr><tr><td>Bitbucket </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FewmX1Q0F9XnNSRbYyksO%2Fbitbucket-card-header-sync-provider.png?alt=media&#x26;token=23434d72-e1b1-49d2-824a-7ea31deb1aaf">bitbucket-card-header-sync-provider.png</a></td><td></td></tr></tbody></table>

{% hint style="info" %}
In this guide we will show a GitHub sync provider, but the steps are similar for all other Git sync providers.&#x20;
{% endhint %}

### Default branch settings

By default, Tokens Studio will connect to the **branch** you identified in your **sync provider settings.** You can adjust your Default Branch at anytime from the Settings page of the Plugin.&#x20;

→ [Read the guide on editing sync providers here](https://docs.tokens.studio/token-storage/manage-sync-provider/edit)

The image below shows an example of a Github sync provider with the setting for `branch` set to `main` (number 4).&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F8CYbG5HRgQwSHrgn5lKq%2Fsync-github-annotated-v2-0.png?alt=media&#x26;token=b33464ea-a7b2-4a17-bac9-4ff3582c6f6b" alt=""><figcaption></figcaption></figure>

To support proper version control of your Token Changes, you can **create a new branch** or **switch branches** using the plugin.

### Branch indicator

When you are connected to **Sync Provider** that supports branching, the **Sync Actions** at the bottom of the plugin will be visible.&#x20;

The **Branch Button** is on the left, displaying the current branch you are working on.

For example, in the image below, the `main` branch is active.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FNekgLAShpNgDdFszzTKI%2Fsync-actions-none-v2-0.png?alt=media&#x26;token=ad56e95a-35b6-499e-a71f-92fb5dad34d6" alt=""><figcaption></figcaption></figure>

### View available branches

**Selecting the branch name** from the **Sync Actions** at the bottom of the plugin will open the **Branch menu** which displays:

1. An option to **Create a new branch**.
2. Available branches from your sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FkciIJpPthsNxEW7yKiz8%2Ftokens-sync-branch-menus-annotated-V2-01.png?alt=media&#x26;token=491a3ed6-d2e7-4f27-911a-7dba467391e8" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The branches visible in the plugin come from your sync provider.

The plugin can't remove any branches from the list; you have to log into your sync provider to delete branches.
{% endhint %}

#### 1. Create a new branch

**Select the branch name** from the **Sync Actions** at the bottom of the plugin to open the **Branch menu**.

* Select the **Create a new branch from** option.
* You'll see a list of current branches from your Sync provider.
* **Select the branch** you want to make your new branch from.
  * Choosing an existing branch (like `main`) will:
    * Ignore any local changes you have made to your Tokens in the plugin.
    * Pull in the Tokens from the branch you selected as the starting place for your new branch.
  * Choosing **Current changes** will:
    * Take the Tokens exactly as you have them in the plugin as the starting place for your new branch.
* Follow the prompts in the plugin to finish creating your new branch.
  * If you have unsaved changes in the plugin (blue push notification is visible), you will be prompted to **push** your changes to the **Sync Provider** before creating the new branch so they aren't lost.
* Once the new branch is created, the plugin will open the **Push Modal** to sync your Tokens to your new branch.

→ [Read the Keep Your Tokens in Sync guide for more details on the Push modal. ](https://docs.tokens.studio/remote-push-pull-changes#push-modal)

#### 2. Switch branches

**Select the branch name** from the **Sync Actions** at the bottom of the plugin to see the available branches you can switch between.

* **Select a new branch name** to switch to that branch.
* The plugin will open the **Pull modal** to see if you want to replace your existing tokens with the Tokens in the new branch you've selected.

→ [Read the Keep Your Tokens in Sync guide for more details on the Pull modal. ](https://docs.tokens.studio/remote-push-pull-changes#pull-modal)

### Limitations of branch switching

Sometimes, when you open the plugin, it reverts to the default branch in your **Sync Provider** configuration, for example, `main`.

Other times, new branches created in a local file are automatically applied in all files sharing the same sync provider, which is not always desired.

{% hint style="info" %}
it's important to double-check which branch you are working on each time you open the plugin.

* The **name of the branch you are working on** appears at the bottom of the plugin for easy reference.
* You can switch branches by following the steps above at any time.
  {% endhint %}

***

### Resources

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Sync Brancing](https://github.com/tokens-studio/figma-plugin/labels/sync%20branch)

* Add error when TS plugin is not able to push changes [#2487](https://github.com/tokens-studio/figma-plugin/issues/2487)
  * Currently no error is shown when you try to push changes to a branch where you don't have permissions for.
* Branch switching conflicts over multiple files <https://github.com/tokens-studio/figma-plugin/issues/2476>
  * Branch settings in the plugin follow you across Figma files.

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None yet

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
