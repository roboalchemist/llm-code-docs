# Source: https://docs.tokens.studio/manage-settings/token-format.md

# Token Format - W3C DTCG vs Legacy

## Token formats W3C DTCG vs Legacy

In support of moving towards the [W3C Specifications for Design Tokens](https://tr.designtokens.org/format/), as managed by the Design Tokens Community Group (DTCG), you can choose a Design Token Format (how tokens are written in their JSON files) from within the Tokens Studio Plugin.

* Current Tokens Studio "legacy" format
* W3C DTCG spec format

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FVy3w6934p9RQi6Y1oMby%2FtokenJSON-format-compare-colorSimple-V2-03.png?alt=media&#x26;token=e6b020d7-91fb-4de6-9120-a9b1883527bb" alt=""><figcaption><p>From the Tokens Page of the plugin, the JSON view is selected and annotated to show the difference between Token Formatting. The image on the left shows "legacy" Token Format. The image on the right shows "W3C DTCG" Token Formatting.  </p></figcaption></figure>

### What's the difference?

The DTCG format prefixes the properties of a design token in the JSON file with the dollar sign (`$`)

* `$value`
* `$type`
* `$description`

Restrictions of special characters in token names are introduced to support this:

* `{`
* `}`
* `$`

When creating Token names with these characters, an error message appears, and the action is blocked.

→ [Learn more about Token Names based on their Technical Specifications.](https://docs.tokens.studio/manage-tokens/token-names/technical-specs)

{% hint style="info" %}
The DTCG [specifies additional token types](https://tr.designtokens.org/format/#types) and their accepted values, which we will support in future releases.
{% endhint %}

***

### In the plugin

The choice of Token Format can be defined for Tokens stored in the local file or remote via a sync provider. For Git sync providers, different branches can have different Token Formats.

You can select a token format in two locations:

1. Plugin settings > sync/storage providers.
2. Sync actions at the bottom of the plugin when a remote storage provider is active.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FuvCJztR89an0LnRiSPNG%2Fsettings-dtcg-convert-bothLocations-V2-03.png?alt=media&#x26;token=bcc53281-67bc-4948-9023-9ff9e8e61dc2" alt=""><figcaption><p>In the Plugin, you can initiate the Token Format conversion process from the Settings Page by selecting the Format for the current Token Project or the Sync Provider Actions at the bottom of the Plugin. </p></figcaption></figure>

{% hint style="info" %}
You can change between the W3C DTCG and Legacy token formats at any time by following the steps below.
{% endhint %}

### 1. Settings page

On the plugin's settings page, you can see the **Token Format** being used in your file next to your token storage provider.

* The default is `legacy format`
* When you make the switch, you'll see `W3C DTCG format`

**Tokens stored on the local document**

If your tokens are stored locally in the Figma file (no external storage or sync providers), the **Token format action** is to the right of the **local document** option.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXpMsuS8uucgO7JXoM51G%2FSETTINGS2B-tokenFormat-both-v2-0.png?alt=media&#x26;token=cbe821d8-dfec-4218-b60f-c347327073e7" alt=""><figcaption><p>The Settings page of the Plugin is shown with the Token project data stored locally. The image on the left shows the Token Format as "legacy". The image on the right shows the Token Format as "W3C DTCG". </p></figcaption></figure>

**Tokens stored externally**

When your tokens are stored externally via **Sync providers** the **token format** for the active sync provider will show.

The **token format** for other sync providers will be hidden.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F3tsItLSy6ScNWcQbUuNC%2Fsettings-format-sync-V2-03.png?alt=media&#x26;token=94c50d5f-2871-4082-93f7-64310d55bd6c" alt=""><figcaption><p>The Settings page of the Plugin is shown with the Token project data synced to Github. The image on the left shows the Token Format as "legacy". The image on the right shows the Token Format as "W3C</p></figcaption></figure>

### 2. Sync actions

When synced to external storage, the current **token format** also appears at the bottom of the plugin alongside the other **Sync provider actions**.

It's possible for different branches of a sync provider to have different token formats, so you can **select** the **Token format icon button** to switch formats if needed.

→ [Learn more about the Branch Switching (pro) feature ](https://docs.tokens.studio/token-storage/remote-branch-switch)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fu91CoMhmxIdym3J7l4yi%2FtokenJSON-format-compare-V2-03.png?alt=media&#x26;token=f10ce24c-5c83-488c-8905-b99a55e9b33d" alt=""><figcaption><p>The Tokens page of the Plugin displays several Color Tokens in the JSON view. The image on the left shows the Token Format as "legacy" indicated by the icon next to the branch called "main.  The image on the right shows the Token Format as "W3C DTCG" indicated by the icon next to the branch called "w3c-dtcg-conversion".  </p></figcaption></figure>

### **Convert between Token Formats**

Select the **Token format indicator** to start the process of changing formats (from the settings page or sync actions):

* A **Token format modal** appears to explain the process.
* **Confirm** your decision to switch formats.
* The plugin will convert your token JSON files to the format of your choice.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F9AgWmTtNkeDO0WZdvUnG%2Fsettings-dtcg-convert-local-V2-03.png?alt=media&#x26;token=957bec37-8ae7-4d01-bd9b-cd712af06900" alt=""><figcaption><p>From the Settings page of the Plugin, select the current Token Format next to the active sync provider to start the conversion process. The images above show the flow of local document storage of Token data. </p></figcaption></figure>

The plugin will convert your token JSON files to the format of your choice without any further action from you.&#x20;

#### Push changes to remote storage&#x20;

If you have unsaved changes that need to be synced to a remote storage provider that requires it, the plugin will prompt you to **push changes** so you don't lose your work.

* A **new branch** is automatically created for you with updated JSON files.
* The **push changes** modal will open.
* A pre-filled **commit message** is added to help your engineers know what to do when they receive your changes.
* Follow the prompts in the plugin to **push changes** to your sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F6g28WHUqUFwSdyJNK11q%2Fsettings-dtcg-convert-sync1-V2-03.png?alt=media&#x26;token=accc6304-f859-423b-9c9d-3d4113cc1e47" alt=""><figcaption><p>From the Settings page of the Plugin, select the current Token Format next to the active sync provider to start the conversion process. The images above show the flow of remote storage of Token data using Github as the sync provider. </p></figcaption></figure>

Once you've synced your changes, the plugin will automatically have you working in the newly created branch. You'll see the W3C DTCG Token Format indicators next to the branch name at the bottom of the plugin.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F7Nz9aRwrjsHrDNqAoRVa%2Fsettings-dtcg-convert-sync2-V2-03.png?alt=media&#x26;token=1665d1b1-7e4b-464f-b641-1daa7a096b53" alt=""><figcaption><p>After completing the sync to remote Token storage provider process, the sync provider actions at the bottom of the plugin show a newly created branch called "w3c-dtcg-conversion" next to the icon for W3C DTCG Token Format. Select the JSON View from the Tokens page to see the newly formatted JSON files. </p></figcaption></figure>

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When your design token format is set to `W3C DTCG Format` using the steps above, you'll need to configure Style Dictionary to support this.

→ [Style Dictionary V4 Utils - convertToDTCG](https://v4.styledictionary.com/reference/utils/dtcg/)

For each Token Type the SD-Transforms package will automatically convert the Tokens Studio specific Token Type to align with the DTCG Format Token Type where necessary.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

{% content-ref url="../manage-tokens/token-types" %}
[token-types](https://docs.tokens.studio/manage-tokens/token-types)
{% endcontent-ref %}

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - [convertToDTCG](https://v4.styledictionary.com/reference/utils/dtcg/)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known Issues and Bugs

Tokens Studio Plugin GitHub - [Open issues for Token Format](https://github.com/tokens-studio/figma-plugin/labels/Token%20Format)

* Add empty line when writing to files (sync providers + local export) [#2970](https://github.com/tokens-studio/figma-plugin/issues/2970)

Tokens Studio Plugin Github - [Open issues for W3C DTCG](https://github.com/tokens-studio/figma-plugin/labels/W3C%20DTCG)

* Remove composition tokens \[#2800]\(# Remove composition tokens #2800)
* Change boxShadow values from x and y to offsetX and offsetY [#2052](https://github.com/tokens-studio/figma-plugin/issues/2052)
* Allow description in token groups [#1811](https://github.com/tokens-studio/figma-plugin/issues/1811)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
