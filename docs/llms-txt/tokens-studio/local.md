# Source: https://docs.tokens.studio/token-storage/local.md

# Local Document - Figma File Token Storage

## Local Figma Document Token Storage

By default, Tokens Studio will store your Design Tokens locally in the Figma file you are working in.

This limits your ability to share your Tokens across multiple Figma files. A **sync provider** is required for a [multi-file workflow in Figma](https://docs.tokens.studio/figma/non-local-files).

{% content-ref url="remote" %}
[remote](https://docs.tokens.studio/token-storage/remote)
{% endcontent-ref %}

Once you have added one or more Sync Providers to Tokens Studio, you can temporarily store your tokens locally in the Figma file. This is helpful for offline work, saving backups of your Figma files, or prepping a file to share with other people who won't have access to your sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FLOGHTpLHPLffpy5qI8sc%2Fsettings-page-sync-localOnly-v2-01.png?alt=media&#x26;token=c565ed2b-77e2-4ca7-ab59-a10e99eee2e0" alt=""><figcaption></figcaption></figure>

### Steps in the plugin for Figma

Open the Tokens Studio plugin and navigate to the **settings** page.

* Navigate to the **sync provider** section.
* Select the **local document** option.
* A confirmation dialog appears asking you to **confirm this change**
  * If you select **cancel**
    * The modal will close, and your current sync provider settings will remain.
  * If you select **yes**
    * Tokens currently in the plugin will be stored in the current Figma file
    * The **push** and **pull** actions from the bottom of the plugin won't be available.
      * Changes made to tokens will remain in the current Figma and can't be shared in other Figma files.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FF3wbXgM0OTOIZkpNFeUa%2Fsetting-sync-switch-local-annotated-v2-01.png?alt=media&#x26;token=69546b02-c492-4a9b-a379-3248779ebd47" alt=""><figcaption></figcaption></figure>

### Your Tokens are now being stored locally

The **Local document** option will show as **active** on the plugin's settings page.

* You can switch back to using a **Sync provider** to store your Tokens remotely at anytime.

{% content-ref url="manage-sync-provider/change" %}
[change](https://docs.tokens.studio/token-storage/manage-sync-provider/change)
{% endcontent-ref %}

***

### Resources

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Sync Local Storage](https://github.com/tokens-studio/figma-plugin/labels/sync%20local%20storage)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None yet

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
