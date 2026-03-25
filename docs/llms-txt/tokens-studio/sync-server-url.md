# Source: https://docs.tokens.studio/token-storage/remote/sync-server-url.md

# URL - Server Sync Provider

## URL sync setup guide

If your Design Token storage is set up on a local server, you can access your Token files (via their URL) in the plugin using the URL Sync option.

URL Sync operates in **read-only** mode.

* This means you can't use the Tokens Studio plugin to create or modify your design Tokens, but you can apply your Tokens to design elements in Figma.
* You'll need to modify the Token JSON files stored on your server and pull the updates into the plugin.

This means the Design Tokens living in code are the source of truth for our design decisions, which can be shared between design and development teams.

This guide outlines how to access your Token files stored on your local server using the **URL Sync provider** option in the plugin.

### How it works

* Once your Token JSON files are **stored on your server**, capture the URL.
* **Configure a new URL sync provider** within the plugin.
* Use the plugin to **sync Design Token changes** between your server and Figma design files.

***

### URL sync setup instructions

If you haven't already, store your Design Token JSON files on your server.

→ [Here's an example Token JSON file stored on a server URL.](https://raw.githubusercontent.com/Tokens-studio/plugin-example-css/main/Tokens.json)

#### 1. Server URL

**Copy the URL** on your server where your Token JSON files are stored. **Store the URL somewhere safe**, as it's needed for the plugin configuration.

#### 2. Check server headers

Headers are the server authentication instructions for the plugin.

* Refer to your server technical documentation for more details on headers.

If your server requires authentication:

* **Store the headers as a JSON object** in the headers field.
* **Access-Control-Allow-Origin** header must be `*`
* **Copy the required headers** and
  * **Store them somewhere safe**, as they are needed for the plugin configuration.

***

### Configure the Tokens Studio Plugin

In Figma, open the Tokens Studio plugin and navigate to the **Settings** page.

* Under the **Sync providers** section, select the **Add new** button to see a list of all Token storage providers.
* Select **URL**

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FY8zpuESkPKldFoG4qH13%2Fsettings-page-url-v2-0.png?alt=media&#x26;token=b187a404-f591-4ecf-ba04-c03de6d8f9d1" alt=""><figcaption></figcaption></figure>

#### Add credentials for URL sync

You'll need the information saved from the steps above to complete the Tokens Studio sync configuration form.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2FC19PxiiK1JNdgLNOo9%2Fsync-url-annotated-v2-0.png?alt=media&#x26;token=7e2d503d-928b-4c9f-8177-c5522b246e0d" alt=""><figcaption></figcaption></figure>

**1. Name**

This is a **nickname** that shows up in the **plugin settings page** later on to identify this specific sync provider configuration.

* Choose something memorable to you and your project.
* Example: `Hyma brand exploration`

**2. URL**

Enter the complete **URL** you saved from [step 1 above.](#id-1.-server-url)

#### **3. Headers**

The authentication **headers** you saved from [step 2 above](#id-2.-check-server-headers).

Example: `{"Some-Header-Key": "SomeHeaderValue"}`

#### Save and do the initial sync

Save to confirm your credentials, and follow the prompts in the plugin to finish setting up the sync to your server.

→ Read the Add New Sync Provider guide for more details.

{% content-ref url="../manage-sync-provider" %}
[manage-sync-provider](https://docs.tokens.studio/token-storage/manage-sync-provider)
{% endcontent-ref %}

***

### Shared source of truth

As you work in the plugin, pull indicators remind you to stay in sync with your URL storage.

Read the Sync Changes guide for more details

{% content-ref url="../remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

Once your Token JSON files are synced to your URL storage, you have a shared source of truth between Designers and Engineers!

The various Token Types supported by Tokens Studio have unique transforms to be aware of.

{% content-ref url="../../manage-tokens/token-types" %}
[token-types](https://docs.tokens.studio/manage-tokens/token-types)
{% endcontent-ref %}

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for URL sync](https://github.com/tokens-studio/figma-plugin/labels/sync%20url)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* 🧑‍💻 [Sync to external token storage enhancements - Feature Request](https://tokensstudio.featurebase.app/p/sync-external-storage-enhancements)
  * How might we improve the experience of working with sync providers in general?
* ↕️ [Git sync enhancements - push, pull, merge, branching - Feature Request](https://feedback.tokens.studio/p/git-sync-enhancements)
* 🔐 [Data security info request - Feature Request](https://feedback.tokens.studio/p/data-security-info)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
