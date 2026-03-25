# Source: https://docs.tokens.studio/token-storage/remote/sync-server-generic.md

# Generic Versioned Storage - Server Sync Provider

## Generic Versioned sync setup guide

For projects requiring highly controlled and secure data-sharing environments, you can host your Design Token JSON files on your servers or storage solutions.

You can use the Tokens Studio plugin to keep your Design Tokens in sync with your code files ***without*** passing your design data through any Git or 3rd-party storage providers.

We support two-way sync, meaning you can use the plugin to:

* **push** JSON files of Design Tokens to your storage provider
* **pull** the Tokens stored in your storage provider into any Figma file

You can configure the permissions of your Generic Versioned sync to be:

* Read Only
* Read / Write
* Read / Write / Create

This means the Design Tokens living in code are the source of truth for our design decisions, which can be shared between design and development teams.

This doc outlines how to configure Generic Versioned storage and add it as a **Sync provider** in the plugin.

### How it works

* Once your Token JSON files are **stored on your server**, capture the **URL endpoint**.
* **Configure a new Generic Versioned sync provider** within the plugin.
* Use the plugin to **sync Design Token changes** between your server and Figma design files.

***

### Generic Versioned sync setup instructions

If you haven't already, store your Design Token JSON files on your server and create a storage endpoint.

→ [Here's an example implementation of token JSON files stored on a SQLite database on a local file if you need a reference.](https://github.com/tokens-studio/figma-tokens-generic-storage-example)

* [The swagger is available with the necessary schemas to roll your own endpoint.](https://github.com/tokens-studio/figma-tokens-generic-storage-example/blob/main/public/swagger.json)

→ [Here's a guide on using a JSON server as a simple way to use Generic Versioned storage created by Ian Lawton, a Tokens Studio Community member.](https://medium.com/@ian.lawton/a-simple-design-token-storage-server-for-figma-token-studio-3a9ba74aefb5)

#### 1. Storage URL

**Copy the URL** where your Token JSON files are stored.

* **Store it somewhere safe**, as it's needed for the plugin configuration.

#### 2. Capture header pairs

Headers are optional authentication instructions for the plugin set up as **key value pairs**.

* Refer to your server technical documentation for more details on headers.

For example, if you want to identify and track which users are accessing your Token files, you could set up a **user authorization** header:

* Name = `Authorization`
* Value = `username`

If your server requires authentication:

* **Copy and save the required header pair** somewhere safe, as it's needed for the plugin configuration.

***

### Configuring Tokens Studio Plugin

In Figma, open the Tokens Studio plugin and navigate to the **Settings** page.

* Under the **Sync providers** section, select the **Add new** button to see a list of all Token storage providers.
* Select **Generic Versioned**

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fl3jGFO0R3dcrsYlM4sDO%2Fsettings-page-genericversion-v2-0.png?alt=media&#x26;token=704c076c-1aaf-4777-9609-e5233924adc7" alt=""><figcaption></figcaption></figure>

#### Add credentials for Generic Versioned sync

You'll need the information saved from the steps above to complete the Tokens Studio sync configuration form.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FERiRo4kdAavRzl5U6HFq%2Fsync-generic-annotated-v2-0.png?alt=media&#x26;token=4f202438-d4c2-41b4-bdbc-fb18b10b25c3" alt=""><figcaption></figcaption></figure>

**1. Name**

This is a **nickname** that appears in the plugin settings page later on to identify this specific sync provider configuration.

* Choose something memorable to you and your project.
* Example: `Hyma brand exploration`

**2. URL**

Enter the complete **URL** you saved from [step 1 above.](#id-1.-storage-url)

**3. Flow type (permissions)**

The flow type sets the permissions between the plugin and your storage provider.

* **Read Only**
  * Token data is pulled into the plugin to be viewed but cannot be edited.
    * Read requests are sent via **GET** calls to the endpoint.
* **Read / Write**
  * Token data is pulled into the plugin to be viewed, and edits to those Tokens can be made and pushed back to storage.
  * New Tokens, sets, or themes can not be created.
    * Read/Write requests are sent via **PUT** requests to the endpoint.
* **Read / Write / Create**
  * New Tokens, sets, and themes can be created.
  * Token data can be pushed and pulled between the plugin and your storage provider for two-way sync.
    * Read/Write/Create requests are sent via **POST** requests to the endpoint.
    * The **POST** request is expected to return:
      * Validation that the endpoint has tracking setup (or not)
      * `updatedAt` field in the JSON, which can be used to set additional workflows on the storage side, like additional **GET** requests.

**4. Headers**

The optional authentication **headers** you saved from [step 2 above](#id-2.-capture-header-pairs).

#### Save and do the initial sync

Save to confirm your credentials, and follow the prompts in the plugin to finish setting up the sync to your Generic Versioned provider.

→ Read the Add New Sync Provider guide for more details.

{% content-ref url="../manage-sync-provider" %}
[manage-sync-provider](https://docs.tokens.studio/token-storage/manage-sync-provider)
{% endcontent-ref %}

***

### Shared source of truth

As you work in the plugin, push and pull indicators remind you to stay in sync.

Read the Sync Changes guide for more details

{% content-ref url="../remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

Once your Token JSON files are synced to your external storage, you have a shared source of truth between Designers and Engineers!

The various Token Types supported by Tokens Studio have unique transforms to be aware of.

{% content-ref url="../../manage-tokens/token-types" %}
[token-types](https://docs.tokens.studio/manage-tokens/token-types)
{% endcontent-ref %}

***

### Resources

Mentioned in this doc:

* GitHub - [Generic Versioned Example Repo from Tokens Studio](https://github.com/SorsOps/figma-tokens-generic-storage-example)
  * [Swagger example to roll your own endpoint.](https://github.com/SorsOps/figma-tokens-generic-storage-example/blob/main/public/swagger.json)
* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>

Community resources:

* Ian Lawson's Guide (Medium Article) - [A simple Design Token storage server for Figma Tokens Studio](https://medium.com/@ian.lawton/a-simple-design-token-storage-server-for-figma-token-studio-3a9ba74aefb5)

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
