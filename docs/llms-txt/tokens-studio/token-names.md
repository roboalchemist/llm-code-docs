# Source: https://docs.tokens.studio/manage-tokens/token-names.md

# Token Names

## Token Names in Tokens Studio

The `name` of a Design Token tells us ***who***, or which parts of our system, this design decision is intended for.&#x20;

You might recall from our [Intro to Design Tokens Guide](https://docs.tokens.studio/fundamentals/design-tokens/anatomy-name) that the Token Name acts as the unique identifier for each design decision in the system and are the most customizable part of a Token's anatomy.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FF8PGN6mxVenZF9TXe3Ro%2Fcode-annotated-card-name.png?alt=media&#x26;token=8f933683-7b65-4cd2-9580-f4640409db6e" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Name. The top code block shows a Token Name with groups. The bottom code block shows a flat Token Name.</p></figcaption></figure>

Each Design Token has a location of where it lives in our system files. In code, Design Tokens live in JSON files. In Tokens Studio, they live in [Token Sets](https://docs.tokens.studio/manage-tokens/token-sets) which are the no-code representation of a JSON file.&#x20;

Each Design Token has to have a unique Name per location. However, Design Tokens in different locations may have identical names, and this provides the basis of Theming!&#x20;

→ J[ump to the guide on Theming.](https://docs.tokens.studio/manage-themes/themes-overview)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFyZ47azn5qGZYJHqiOhJ%2FtokenColor-lightVsDark-Sets-V2-3.png?alt=media&#x26;token=76200cc8-5eaa-4e1a-b4cd-71ea1183970c" alt=""><figcaption><p>Two Token Sets in the same project are shown side by side. Both examples contain Tokens with identical names which is allowed because they are located in different Token Sets. The example on the left shows a Token set named <code>theme/light-mode</code>which has the Token called <code>theme-color.background.default</code>with a light color as its value, compared to the example on the right in the <code>theme/dark-mode</code> Token Set which has the value as a dark color. </p></figcaption></figure>

{% hint style="info" %}
Before you get started [Naming your Tokens](https://docs.tokens.studio/manage-tokens/token-names/technical-specs), you'll want to get familiar with the Common Terms related to Naming and how to work with them in the Plugin for Figma.&#x20;
{% endhint %}

***

### Common Terms

We have seen many different ways to talk about Naming Tokens over the years and it can be really hard to keep them straight! So here's the common terms we will use across our technical docs that you should be aware of.&#x20;

These terms are not the only way to describe Token Names; they are the labels the Tokens Studio team uses for simplicity across our documentation.&#x20;

If your team uses different descriptive terms, that's totally okay!&#x20;

#### Token Name

The Token Name is the ID of the design decision captured in the Design Token. Each Token within a Token Set must have a unique name.  Token Names are used in code by engineers, so there are some specific nuances to be aware of [covered in its own guide. ](https://docs.tokens.studio/manage-tokens/token-names/technical-specs) The Name is also how the Plugin attaches a Token to a design element, style or variable in Figma. &#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FCumHHN0NiZCzBev3aFsH%2Ftokens-button-figma-properties.png?alt=media&#x26;token=4695fad6-067c-44f3-9e19-3caa3f8da74a" alt=""><figcaption><p>The infographic shows the name of a Token called <code>button-label-color,</code> which could be applied directly to the button design element and represented as a hex code, color style, or variable in Figma. </p></figcaption></figure>

#### Token Groups

The period (.) character is used in a Token Name to create relationships between Tokens that should be grouped together.

Token Groups helps to organize your Tokens into a tree structure in the Tokens Studio plugin and their code files. [In the guide for Token Groups](#token-groups), you'll learn about the powerful workflow features we've added to the Plugin which allows you to take bulk actions on Tokens in the same Group!&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fo9lAcPi0vP2tFxHE7aAY%2FtokenColor-flatVsGroups-V2-3.png?alt=media&#x26;token=930e667e-5ff3-4ab0-900a-dab0ae8eb43b" alt=""><figcaption><p>Two examples of Token names are shown. On the left, the Token names are considered "flat" because they do not contain any groups. On the right, the Token names have groups which create a tree structure which can be collapsed and expanded as needed. </p></figcaption></figure>

Here are some additional terms related to Token Names with Groups that might be helpful:

<details>

<summary>Flat Name</summary>

A Token `name` which is flat does not contain any groups.&#x20;

For example:\
`colors-green-500`

</details>

<details>

<summary>Folder Name or Tree Name</summary>

A Token `name` which contains groups are sometimes referred to as a folder or tree name because the groups organize the Tokens in a tree structure that behaves like a series of sub-folders.&#x20;

</details>

<details>

<summary>Token Path</summary>

The Token Path is the full `name`of the Token including any Groups. \
\
For example:\
`colors-green-500 or` `colors.green.500`

</details>

#### Alias Tokens&#x20;

When a new Token is created, its [Value can reference another Token](https://docs.tokens.studio/manage-tokens/token-values/references). The new Token created is sometimes referred to as an Alias Token, because it's purpose is to provide an alias, or a new name, or an existing design decision with some context about how the design decision is intended to be used in the system.&#x20;

This new name, or alias, is also referred to as its semantic name in the community.&#x20;

For example, a new Token named `success-default`with a value referencing `{colors.green.500}` could be referred to as an Alias Token.&#x20;

The name `success-default` may also be referred to as a semantic Token, as it provides some meaningful context about how the `colors.green.500` Token is intended to be used in the system.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXCQycYs1Aj9L4uhD7BNx%2Ftoken-intro-example-value-references.png?alt=media&#x26;token=ef194b8f-d5fa-461c-adf2-2510f3682f14" alt=""><figcaption><p>An example of a button is shown with a label annotated to show a series of Tokens with values referencing each other to arrive at the final color of the label text. </p></figcaption></figure>

Here are some additional terms related to Alias Tokens that might be helpful:

<details>

<summary>Component Tokens or Component Specific Tokens</summary>

Although Component Token may sound like a type of Token, its industry jargon to describe the name of a Token that is specific to a component.

They are also referred to as Component Specific Tokens for this reason.&#x20;

For example, a Color Token named `action.button.success.hover.background-color`has a Grouped Name specific to a Button component. The different groups within the name help communicate that the Token is intended to be used for success actions when they are interacted with on hover and applied to the background container.&#x20;

You can see by this example that a component specific name can also be considered an alias or semantic name which can be confusing!

</details>

<details>

<summary>Semantic Tokens</summary>

A Semantic Token is another way to say "Alias Token".  While this term might sound like a type of Token, its really just industry jargon to describe the name of a Token with a new name (or alias) for an existing Token in our system that has meaninful context about how it is intended to be used.&#x20;

For example, a new Token named `success-default`with a value referencing `{colors.green.500}` could be referred to as a semantic Token, as it provides some meaningful context about how the `colors.green.500` Token is intended to be used in the system.&#x20;

</details>

<details>

<summary>Primitive Tokens</summary>

Although a Primitive Token sounds like a type of Token, its industry jargon to describe the name of a Token that does not contain any context about how it is intended to be used.&#x20;

For example `colors.green.500` could be referred to as a Primitive Token.&#x20;

</details>

<details>

<summary>Token Taxonomy</summary>

Token Taxonomy is a technical way to describe how a Token is named based on some agreed upon logic. Or in other words, a really fancy way to say "Token Name Template".&#x20;

For example, for the Tokens in your system that have hard-coded values representing the options you have to choose from, you may decide on a Token Taxonomy that is `attribute.category.identifier` which looks like `colors.green.500`when naming a Color Token belonging to a green scale located at the 5th position on the scale.&#x20;

Your team may decide to have different Token Naming templates for different parts of your Token Structure. A good example of this is the component specific Token Name above `action.button.success.hover.background-color` which follows a template that more closely resembles CSS.&#x20;

</details>

***

### Working with Token Names

The Token Name appears anywhere in the Plugin you are creating, viewing or editing a Token.&#x20;

From the Tokens Page of the Tokens Studio Plugin for Figma, there are three places to see the Name of a Token.&#x20;

1. Token data on hover
2. Token form
3. JSON file

When [Inspecting Design Elements](https://docs.tokens.studio/debug/inspect-tokens) or using [Dev Mode in Figma](https://docs.tokens.studio/figma/dev-mode), the Token Name will also appear to identify which Tokens are mapped to the specific layer you have selected.&#x20;

#### 1. Token Data on Hover

Hover on an existing Token to view its data. The `name` appears as the first piece of data in the list.&#x20;

{% hint style="info" %}
Each Token will have different data to view on Hover depending on its `type` and `value`, however the position the data remains the same.&#x20;
{% endhint %}

If the Token has a flat name, you will see the full name on hover. If the Token has a name with Groups, you will only see the final part of the Token Path in the preview on hover.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FU1EbkqsPRmn7MXxasCsf%2FtokenColor-hoverData-flatVsGroups-V2-3.png?alt=media&#x26;token=f0ddea2b-3046-4365-b80f-8682614e3713" alt=""><figcaption><p>Two examples of Token Sets being viewed from the Tokens page of the Plugin. The left example shows flat Token Names, the right shows Token Names with groups. When the Token Name is hovered on, it appears differently if the Name is flat or grouped. </p></figcaption></figure>

#### 2. Token Form

Right click on a Token Name and select Edit to view its properties as a form. The first input displays the  Name.&#x20;

{% hint style="info" %}
The Token Form for each Token Type is unique, but the Name always appears as the first input.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FpToLr3XG68JNECXb3qGp%2FtokenForm-names-colorVsTypography-V2-3.png?alt=media&#x26;token=2b6dbaa4-8735-4883-b2a0-cfcf3cde1399" alt=""><figcaption><p>Two Token forms are pictured with its <code>name</code>input annotated. On the left side, the form is for a <code>color</code>Token Type. On the right, the form is for a <code>typography Token Type.</code> </p></figcaption></figure>

The Token Name also appears when it is being [Referenced in the Value of another Token](https://docs.tokens.studio/manage-tokens/token-values/references) in the Value input.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FRJKT7Xg2SGBZGYIefags%2Fvalues-references-createNew-typing-v2-2.png?alt=media&#x26;token=74929900-2f41-4b96-b2f4-f773d63d2794" alt=""><figcaption><p>The image on the right shows a <code>color</code>Token form with its <code>value</code> input open, showing available Token Names that can be referenced as the value. Once a Token Name is selected from the list, it appears wrapped in curly brackets as the <code>value</code>in the Token Form. </p></figcaption></figure>

#### 3. JSON File

Use the Token View Toggle see your Tokens written in JSON code files.  The Name will appear as the first part of data about the Token.&#x20;

If the Token has a flat name, you will see the full name before the rest of the properties. If the Token has a name with Groups, the JSON file will organize the data by groups.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FzkkGBfQmqpPin1l12oJk%2FtokenColor-JSON-flatVsGroups-V2-3.png?alt=media&#x26;token=843b3316-baca-48f3-b61f-2fbcc6affa90" alt=""><figcaption><p>Two examples of Token Sets being viewed as their JSON file from within the Plugin. The left example shows flat Token Names, the right shows Token Names with groups. </p></figcaption></figure>

If you are comfortable working in code (and have edit permissions), you can edit Token Names in the JSON view.  However, making changes to Token Names in the JSON files which have already been applied to design elements in Figma require a few extra steps to be aware of.&#x20;

→ [Jump to the guide on Editing Token Names for more details. ](https://docs.tokens.studio/manage-tokens/token-names/edit)

{% hint style="info" %}
The JSON view functions similar to Visual Studio Code thanks to an amazing open-source contribution from a Tokens Studio community member. 🫶
{% endhint %}

{% content-ref url="token-sets/json-view" %}
[json-view](https://docs.tokens.studio/manage-tokens/token-sets/json-view)
{% endcontent-ref %}

***

### In Figma

When you apply a Token to a design element in Figma, the `name` of the Token can appear in a few placed in the Figma UI, depending on your project:

* Styles and Variables - if the Token applied is attached to Style or Variable the matching name will appear in the design panel for the appropriate property when possible.&#x20;
  * Unless you've set the Plugin to Apply all Tokens as Resolved Values.
* Dev Mode - if you've configured Tokens Studio as a plugin in Dev Mode and selected it as your language.&#x20;

If you want to learn more about how your Token names appear in Figma, check out these detailed guides:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td>Export to Figma as Styles or Variables</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFDa6fBDwo2XOXgLnjSXE%2Fcard-header-figma-export-overview.png?alt=media&#x26;token=d12beb6c-8659-4da5-ba77-9f3b6a132285">card-header-figma-export-overview.png</a></td></tr><tr><td>Apply Token Actions + Settings</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FQwpM9vFJZNQwj4F3gKFf%2Fcard-header-figma-apply-token.png?alt=media&#x26;token=ead556b2-6ccf-41ae-b741-f7088198b089">card-header-figma-apply-token.png</a></td></tr><tr><td>Dev Mode + Tokens Studio</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FdWNQGqL6pVwyoZ7vYPel%2Fcard-header-figma-ts-devMode.png?alt=media&#x26;token=bd89345f-42b4-495c-849d-cbab8bbc79eb">card-header-figma-ts-devMode.png</a></td></tr></tbody></table>

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

During the transformation process, they often modify the Token names to match their preferred workflow.

Most common Token name modifications:

* Change casing and punctuation.
* Flatten them to remove groups.
* Add or remove front matter/prefixes.
* Remove designer-specific words.

It's important to consider how a Token Name may be modified during the transformation process to avoid unintentional naming collisions.&#x20;

→ [Jump to the Token Name Technical Specs for more details on naming transformations and collisions](https://docs.tokens.studio/manage-tokens/token-names/technical-specs).

***

### Naming Token Guides&#x20;

Now that you've got the basics covered, check out these guides related to Naming Tokens in the Plugin:

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td>Technical Specs for Token Names</td><td>The do's and don'ts of writing great Token Names. </td><td><a href="token-names/technical-specs">technical-specs</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FK3kroA8VxsOQ7Xnmoj6y%2Fcard-header-anatomy-tokenName-technicalSpec.png?alt=media&#x26;token=ae946289-640c-4c51-8c87-8ba834913724">card-header-anatomy-tokenName-technicalSpec.png</a></td></tr><tr><td>Token Groups</td><td>A deep dive into how to take advantage of powerful workflows using Token Groups in the plugin.</td><td><a href="token-names/groups">groups</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fr9b8mfThIUvwkIzpn1bu%2Fcard-header-anatomy-tokenName-group.png?alt=media&#x26;token=2940daf6-d1c9-419c-a645-ab1777a0fbfb">card-header-anatomy-tokenName-group.png</a></td></tr><tr><td>Edit Token Names</td><td>Changing Token Names can be tricky! Here's what you need to know to be successful.</td><td><a href="token-names/edit">edit</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FSe63C36vYqN3e8kosZbA%2Fcard-header-anatomy-tokenName-remap.png?alt=media&#x26;token=fe691630-8578-48de-b390-b359ba59a57e">card-header-anatomy-tokenName-remap.png</a></td></tr></tbody></table>

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary -[ https://styledictionary.com/](https://styledictionary.com/)
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [W3C Draft, 5.1 Name and Value](https://tr.designtokens.org/format/#name-and-value)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Names](https://github.com/tokens-studio/figma-plugin/labels/token%20name)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None yet.&#x20;

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
