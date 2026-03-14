# Source: https://docs.tokens.studio/token-storage/remote-push-pull-changes.md

# Sync Changes to Remote Storage - Push and Pull

## Sync changes to remote Token storage

Once you have a sync provider connected, you can use the plugin to keep your tokens in sync.

{% content-ref url="remote" %}
[remote](https://docs.tokens.studio/token-storage/remote)
{% endcontent-ref %}

For sync providers that have **read** and/or **write** permissions, the plugin will identify when changes have been made and notify you to:

* **Push** to your sync provider.
  * **Write** access allows us to "send" changes made in the plugin to your code files.
* **Pull** from your sync provider.
  * **Read** access allows the plugin to "receive" changes to your code files.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FbfL00EZAmfloK5aBBoIq%2Ftokens-syncActions-pushPull-v2-0.png?alt=media&#x26;token=b2f8accf-2589-41ef-a9bd-cbfd4a091243" alt=""><figcaption></figcaption></figure>

### Push to sync provider

When you make changes in the plugin, it detects that your Token data is out of sync with the code files stored by your provider.

In the plugin, you will see the **push icon button** has a **notification indicator** visible to remind you to **push** (or send) your changes to your sync provider.

When you are ready to send those changes to your sync provider:

* **Select the push icon button** to open the **push modal**.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FEbNfrVA6xnThByiOLWBI%2Ftokens-push-modal-commitMsg-v2-0.png?alt=media&#x26;token=a46f7d28-730d-46c3-8c6e-8aaa11dabf16" alt=""><figcaption></figcaption></figure>

#### Push modal

The **Push modal** has three sections, accessible by selecting the tab in the plugin:

1. Commit
2. Diff
3. JSON

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FT9TbaH9aPse5wSpwCMGl%2Fsync-github-push-modal-annotated-v2-01.png?alt=media&#x26;token=55026edd-bb25-4a06-87b0-e2de39db4142" alt=""><figcaption></figcaption></figure>

**1. Commit**

By default, when the **Push modal** opens, you see the **commit form**.

This is where you add a **commit message** containing a short note about what you are **pushing** to the sync provider.

The **commit message** is:

* visible to engineers looking at your code files.
* required each time you **push** Token data to a sync provider.
  * The **Push Changes Button** will be inactive until the **commit form** is completed.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FhNA2WAKR0uQE87yuutpI%2Fsync-github-push-modal-commit-v2-01.png?alt=media&#x26;token=40c1728a-e9be-44d6-a496-eb691ee247c3" alt=""><figcaption></figcaption></figure>

**2. Diff view**

The **Diff** view shows the **difference** of what you are **pushing** to a sync provider and what is already at the source.

* Token data being added will appear highlighted in green.
* Token data being removed will appear highlighted in red.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPj1gn8M82ZKzzhBdWgVl%2Fsync-github-push-modal-diff-v2-01.png?alt=media&#x26;token=12613dc4-dd30-42b9-8ed4-bb46e1a99bbf" alt=""><figcaption></figcaption></figure>

**3. JSON view**

The **JSON** view shows the code in JSON, which will be sent to the sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FB0RWjxR9wOS24t0P2ag3%2Fsync-github-push-modal-json-v2-01.png?alt=media&#x26;token=82feb613-7227-4859-a2bc-8d98cdc39a3c" alt=""><figcaption></figcaption></figure>

#### Push Changes

Once you add a **Commit message**, you can select **Push changes**.

* The plugin will take some time to connect to your sync provider and update the Token data.

Once the **Push** has been completed and your **commit** has been added to the sync provider, the plugin may ask if you want to **Create a Pull Request**.

#### Pull Request

If your sync provider supports **Pull Requests**, sometimes called a **PR**, the plugin can initiate that process.

* A **Pull Request** signals to engineers and other folks consuming your code files that you've **pushed changes** to them and are requesting that they **pull** those changes to review them.
* The code review and merge processes are handled by the sync prover.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FrxuHdiqP5Ch4iImlKvIY%2Fsync-git-push-PR-modal-v2-0.png?alt=media&#x26;token=1397127e-1557-4791-9e1f-855e8a6490ad" alt=""><figcaption></figcaption></figure>

After you've **Pushed Changes** to your sync provider, you can **Create a Pull Request**.

* Selecting the **Create a Pull Request button** in the plugin will open a web browser to your sync provider, where you can complete the **PR** process.
  * The plugin will close the **Push Modal** and you can continue working in the plugin as desired.

**Delay the Pull Request**

Tapping outside the **Push modal** will close it without starting the **PR** process.

* This allows you to **push** more than one set of changes before you ask your team to review your changes.
* They will see each **commit message** you push from the plugin in the **PR** whenever you are ready.

## Pull from a sync provider

When the plugin detects that the Token data in your connected code files has changed, you will see the **pull button** with a notification indicator to remind you to **pull** (or update) the new data from your sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FCl4jUbL9vRkWTFX8OAXB%2Ftokens-pull-modal-metadata-v2-0.png?alt=media&#x26;token=2ab59671-c07a-4352-8c1d-33f23a2c8c56" alt=""><figcaption></figcaption></figure>

The **pull** action is also helpful if you've been working in the plugin and aren't happy with your changes.

* You can press the **pull button** at any time to 'reset' your Tokens to their original state in your code files.

When you are ready to receive changes from your sync provider:

* **Select the pull icon button** to open the **pull modal**.
* Review and accept the changes.
* The modal will close and the **pull indicator** will no longer be visible.

### Pull modal

The **Pull modal** separates the changes the plugin identifies so you can review them:

* **Token Sets** where changes are detected are in collapsable headings
  * **Tokens** deleted are identified with a **removed** label
  * **Token Values** that are changed are identified with the
    * Previous value on the left
    * New value on the right
* Metadata changes
  * When Token sets are removed/added
* Themes changes
  * All changes to the theme configuration.

Select the **Pull changes button** once you are ready to accept the changes.

You will lose all Tokens in the plugin, and they can not be recovered!

If you want to keep the Tokens as they are currently in the plugin, you can select **cancel.**

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FOHizR9DAgEZAfKZdodxV%2Fsync-github-pull-modal-annotated-v2-01.png?alt=media&#x26;token=518d6acc-c66f-4b2d-9e3c-61b78e1e4b31" alt=""><figcaption></figcaption></figure>

***

### Resources

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - Open issues for [Sync Indicators](https://github.com/tokens-studio/figma-plugin/labels/sync%20indicators)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
