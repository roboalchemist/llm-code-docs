# Source: https://docs.tokens.studio/figma/variables-overview.md

# Variables and Tokens Studio

## Manage Variables in Figma with Tokens Studio

If your team is working with Variables in Figma, you can use the Tokens Studio Plugin to attach Design Tokens to Variables (and styles). This allows you to manage your Tokens and Variables in the same place, and easily sync your design decisions to a code repository.

### Guides on working with Variables&#x20;

Select a card below to jump to a comprehensive guide on working with Variables, or scroll down to see the [answers to frequently asked questions ↓](#frequently-asked-questions).

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Export to Figma</strong> <br>Create Variables from Tokens using the Plugin.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFDa6fBDwo2XOXgLnjSXE%2Fcard-header-figma-export-overview.png?alt=media&#x26;token=d12beb6c-8659-4da5-ba77-9f3b6a132285">card-header-figma-export-overview.png</a></td><td><a href="export">export</a></td></tr><tr><td><strong>Skipped Variables</strong><br>Troubleshooting tips when creating new variables. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2t9OcuErpo05TtLrMZbH%2Fcard-header-figma-variables-skipped.png?alt=media&#x26;token=cd2efebc-f5f9-4aad-b95d-1e8252b065ad">card-header-figma-variables-skipped.png</a></td><td><a href="export/variables-skipped">variables-skipped</a></td></tr><tr><td><strong>Non-Local Variables (pro)</strong><br>Split variable collections across many Figma files.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FkPDmDsfoKXFgsIub4LjJ%2Fcard-header-figma-files.png?alt=media&#x26;token=a9f0dd2a-49b0-4816-8aec-1a32a8bbf2bd">card-header-figma-files.png</a></td><td><a href="non-local-files">non-local-files</a></td></tr><tr><td><strong>Import from Figma</strong><br>Create Tokens from Variables </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FySgL4m1UesD2QxbziFMV%2Fcard-header-figma-import-variables.png?alt=media&#x26;token=a0765adf-9ad3-4d5f-ab8a-a69649fbd3dc">card-header-figma-import-variables.png</a></td><td><a href="import/variables">variables</a></td></tr><tr><td><strong>Styles with Variable References</strong> </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FALB0ijN1FCGYOdgd71SF%2Fcard-header-figma-styles-var-references.png?alt=media&#x26;token=24756238-c207-4bb0-8775-e2b20b5d2236">card-header-figma-styles-var-references.png</a></td><td><a href="export/styles-variable-references">styles-variable-references</a></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>

***

### Frequently Asked Questions

Select a question to reveal the answer.&#x20;

<details>

<summary>Which Token types match the different Variable types?</summary>

Tokens Studio supports 23 unique Token Types and there is only 4 Variable Types. Head to the Export to Figma (overview) guide which shows the relationships.&#x20;

[#supported-token-types](https://docs.tokens.studio/export#supported-token-types "mention")

</details>

<details>

<summary>How do I make sure my Variables are hidden from publishing and scoped properly using Tokens Studio? </summary>

Tokens Studio is not yet able to control Figma's Scoping or Hide from Publishing features.

You can use the Figma native UI to adjust the desired Scoping and Publishing feature without adverse effects to the attached Tokens.&#x20;

</details>

<details>

<summary>Why isn't Theme switching in the Plugin working? </summary>

Once you Export to Figma as Variables using Themes, you will be required to use Figma's native Mode Switching feature.

The Theme Switcher in the Plugin will not work once those themes are attached to a Variable Collection

</details>

#### Manage Variables using Tokens Studio

<details>

<summary>Why didn't the Plugin create Variable Collections with Modes? I have duplicate Collections I wasn't expecting. </summary>

You need to export to Figma from Themes (pro) in order for the Plugin to be able to create a single collection with multiple modes.&#x20;

Head to the guide on Exporting to Figma from Themes for more details.&#x20;

[themes](https://docs.tokens.studio/figma/export/themes "mention")

</details>

<details>

<summary>My Variable Collection names aren't what I expected, how do I fix this?</summary>

When Exporting to Figma to create Variables, the Collection Name is created from the Theme Group when exporting from themes, and the Token Set name when exporting from Token Sets. \
\
Head to the guide on Exporting to Figma for more details.&#x20;

[export](https://docs.tokens.studio/figma/export "mention")

</details>

<details>

<summary>When creating Variables from Tokens using the Plugin, why are there less Variables then I have Tokens? </summary>

There are many reasons why the Plugin may have to skip creating a Variable. Head to the guides for Skipped Variables when Exporting to Figma for more details.&#x20;

[variables-skipped](https://docs.tokens.studio/figma/export/variables-skipped "mention")

</details>

#### Create Design Tokens in the Plugin from Variables

<details>

<summary>After importing my variables into the Plugin, I'm confused at how things are organized in Tokens Studio. </summary>

Congrats on getting this far! Head to the comprehensive guide on Importing Variables for some handy visuals and pro-tips.&#x20;

[variables](https://docs.tokens.studio/figma/import/variables "mention")

</details>

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
