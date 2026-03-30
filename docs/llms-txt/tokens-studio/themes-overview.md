# Source: https://docs.tokens.studio/manage-themes/themes-overview.md

# Themes (pro)

## Themes (pro)

In software and web development, a Theme defines the styling choices applied to the graphic elements of an interface, influencing the appearance and atmosphere of websites and software applications within a specific context, such as a brand, platform, or user preference.&#x20;

When you are working with Design Tokens, the concept of theming enables you to style the same components in different ways so you can do more without needing to manage more components.

For example, instead of having 2 button components, light-mode button and dark-mode button, you have a single button component that takes on the styling properties of the color mode theme that is currently active.&#x20;

The Themes feature in Tokens Studio allow you to define combinations of Token Sets that are intended to be applied together to style design elements. Under the hood, the Plugin creates a themes configuration file that can be shared with developers and used in code.&#x20;

Multiple Themes can be applied at the same time to create a matrix of possible concepts that a single design element can be styled with. This is also known as *multi-dimensional theming*.&#x20;

### Themes Guides&#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Themes that switch - a simple example. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPApW20hBDcajiUjWBjpw%2FcardHeader-themes-switch.png?alt=media&#x26;token=407f4a79-fe46-42a6-ae30-1f9ad8971012">cardHeader-themes-switch.png</a></td><td><a href="simple-switch-guide">simple-switch-guide</a></td></tr><tr><td>Export to Figma Styles and Variables using Themes. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FTPetIVSWuZKC9ykNmbkB%2Fcard-header-figma-export-themes.png?alt=media&#x26;token=93abe510-7106-4871-b977-e0a9d141d1fc">card-header-figma-export-themes.png</a></td><td><a href="../figma/export/themes">themes</a></td></tr></tbody></table>

We are working on several new guides to help you master working with Themes in the Tokens Studio Plugin for Figma - coming soon!&#x20;

* Creating, editing, and removing themes.&#x20;
* Multi-dimensional theming.&#x20;
* Detach styles and variables from Themes.&#x20;
* Attach local styles and variables to Themes.&#x20;

***

### Transforming Themes for use in Code

As soon as your Token project includes Themes, there are JSON files created by the plugin to save your configuration data so it can be shared with developers. Once developers have the new Themes files in your external storage provider, they can use that data in their transformation process to turn the themes file into usable code.&#x20;

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

SD-Transforms generic package includes a specific transforms to convert Tokens Studio themes into individual theme files for all possible permutations

→ [SD-Transforms Read-Me Doc, Theming](https://github.com/tokens-studio/sd-transforms?tab=readme-ov-file#theming)

#### Plugin Sync Settings

If this is the first time you are working with Themes in your project, theres a couple things you'll want to do in the Plugin Settings make the transformation process as simple as possible:&#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Sync to a remote storage provider, like GitHub, GitLab, Bitbucket or Azure DevOps.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FgRolgxxD0vV8UMp3dTxj%2FcardHeader-sync-remote-overview.png?alt=media&#x26;token=0f431460-e5f5-4e4d-82d3-1a04d222b4e6">cardHeader-sync-remote-overview.png</a></td><td><a href="../token-storage/remote">remote</a></td></tr><tr><td>Configure your sync settings to save to a folder in your repository with multiple files. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FGrj15Ab45viYXKNCUK9t%2FcardHeader-sync-remote-multi-file.png?alt=media&#x26;token=db7c14ac-ecd2-4c16-b91c-a26d3b3d3c74">cardHeader-sync-remote-multi-file.png</a></td><td><a href="../token-storage/remote-multi-file-sync">remote-multi-file-sync</a></td></tr></tbody></table>

***

### Resources

Mentioned in this Guide

* SD-Transforms Read-Me - [Theming](https://github.com/tokens-studio/sd-transforms?tab=readme-ov-file#theming)

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Themes](https://github.com/tokens-studio/figma-plugin/labels/themes)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
