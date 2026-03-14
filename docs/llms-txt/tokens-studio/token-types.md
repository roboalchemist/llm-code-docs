# Source: https://docs.tokens.studio/figma/import/variables/token-types.md

# Source: https://docs.tokens.studio/manage-tokens/token-types.md

# Token Types

## Token Types in Tokens Studio

The `type` is the anatomic part of a Design Token that defines the category of design property the decision belongs to, or ***when*** it can be applied. &#x20;

You might recall from our [Intro to Design Tokens Guide](https://docs.tokens.studio/fundamentals/design-tokens) that the `type` determines what Values are acceptable.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FmObosUuw4StzoO7T9rZE%2Fcode-tokenAnat-type.png?alt=media&#x26;token=2e245ed2-fa7c-4f80-aa8a-15a0d3177cb6" alt=""><figcaption><p>In this infographic, the Token examples on the right side highlight the Type. Both code blocks have <code>color</code>as the Token Type.</p></figcaption></figure>

Tokens Studio (TS) supports 24 unique **Token Types.**&#x20;

Before you jump into the technical docs for each Token Type, you may want to review the [common terms and concepts below](#common-language) that will help strengthen your knowledge.&#x20;

*Select the Token Type card below to jump to its guide.*

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Color</td><td>Layer fill and stroke.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fp0NbEiubmi7VBL4Y16x6%2Fcard-header-token-type-color.png?alt=media&#x26;token=4c6458b7-f299-4c5f-99db-22fee98d6030">card-header-token-type-color.png</a></td><td><a href="token-types/color">color</a></td></tr><tr><td>Opacity</td><td>Defines layer transparency.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FuybB3jf4mZdu6FEpYC5D%2Fcard-header-token-type-opacity.png?alt=media&#x26;token=a5fb7c5e-850c-433a-8e54-720ced0c7749">card-header-token-type-opacity.png</a></td><td><a href="token-types/opacity">opacity</a></td></tr><tr><td>Box Shadow - Composite</td><td>X, Y, Blur, Spread, and Color.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFkPoaYKarI6eMCUR2cSG%2Fcard-header-token-type-box-shadow.png?alt=media&#x26;token=13d6cfae-e043-4e6e-8040-48e2e12ad581">card-header-token-type-box-shadow.png</a></td><td><a href="token-types/box-shadow">box-shadow</a></td></tr><tr><td>Border - Composite</td><td>Stroke color, width and style.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FQHti7A7qoHPWxeDATqEr%2Fcard-header-token-type-border.png?alt=media&#x26;token=64a1bfe0-507a-4868-bed2-3fcc5950734f">card-header-token-type-border.png</a></td><td><a href="token-types/border">border</a></td></tr><tr><td>Asset</td><td>URL hosted images and assets.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2ucrIdhmmrCaHheH9kRC%2Fcard-header-token-type-asset.png?alt=media&#x26;token=12bb21fb-9627-4ad2-9f24-1d7cbed0ee5c">card-header-token-type-asset.png</a></td><td><a href="token-types/asset">asset</a></td></tr><tr><td>Boolean</td><td>Controls layer visibility.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FINDO3H70VEZqXRRQ2rDk%2Fcard-header-token-type-boolean.png?alt=media&#x26;token=c27de8a1-97bf-4142-978e-9e70031187f3">card-header-token-type-boolean.png</a></td><td><a href="token-types/boolean">boolean</a></td></tr></tbody></table>

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td>Number</td><td>Unitless numeric value.</td><td><a href="token-types/number">number</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FivYNIP6dLorTCpKc1uQd%2Fcard-header-token-type-number.png?alt=media&#x26;token=a79d166e-4428-4d6c-bffc-2f95a32befb2">card-header-token-type-number.png</a></td></tr><tr><td>Dimension</td><td>Numeric value with pixel or rem units.</td><td><a href="token-types/dimension">dimension</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FIjJYdDQWqHVNbjY6xI0E%2Fcard-header-token-type-dimension.png?alt=media&#x26;token=9d510dda-3952-4c17-a763-c55b2435924b">card-header-token-type-dimension.png</a></td></tr><tr><td>Border Radius</td><td>Unofficial Token converted to a Dimension Token. </td><td><a href="token-types/dimension/border-radius">border-radius</a></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FjtjwZcOInBFKiru4hStl%2Fcard-header-token-type-border-radius.png?alt=media&#x26;token=4f6acf41-9778-4e8c-a98a-a1e0edadc862">card-header-token-type-border-radius.png</a></td></tr><tr><td>Border Width</td><td>Unofficial Token converted to a Dimension Token. </td><td></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FO2oBQjSparDF0oOo8OcC%2Fcard-header-token-type-borderwidth.png?alt=media&#x26;token=31b86d79-9bcf-4fbb-ad0d-fc2748b34537">card-header-token-type-borderwidth.png</a></td></tr><tr><td>Sizing</td><td>Unofficial Token converted to a Dimension Token. </td><td></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FD0OMEYi3qmQiCDTKFNDo%2Fcard-header-token-type-sizing.png?alt=media&#x26;token=84d3ab67-5879-4f54-b84e-a7cbfe97014c">card-header-token-type-sizing.png</a></td></tr><tr><td>Spacing</td><td>Unofficial Token converted to a Dimension Token. </td><td></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FCb25KpDXDE4qXMUY4VYR%2Fcard-header-token-type-spacing.png?alt=media&#x26;token=8973c7c4-0a23-4bc0-bc40-1d9e95a4f644">card-header-token-type-spacing.png</a></td></tr></tbody></table>

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Text (string)</td><td>Strings of text for copy and content.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJwbLGvVcpOI3oiRdhPI8%2Fcard-header-token-type-text.png?alt=media&#x26;token=7c3c9ca8-6534-477a-bf1c-f784aa724a66">card-header-token-type-text.png</a></td><td><a href="token-types/text">text</a></td></tr><tr><td>Typography (composite)</td><td>All text and font styling properties combined.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FP2GZO2Zry7c5atV4C07K%2Fcard-header-token-type-typography.png?alt=media&#x26;token=3d04dee1-4e98-41bd-a0c0-ce37246d9458">card-header-token-type-typography.png</a></td><td><a href="token-types/typography">typography</a></td></tr><tr><td>Font Size</td><td>Define in pixel or rem values for responsive design.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FAwn3zkzamS5c7N7xSyZ7%2Fcard-header-token-type-font-size.png?alt=media&#x26;token=d6798225-3708-4e1f-ad79-1fc16f9c9bd1">card-header-token-type-font-size.png</a></td><td><a href="token-types/typography/font-size">font-size</a></td></tr><tr><td>Font Family</td><td>Works with Font Weight as a pair in Figma. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F9nfWC3hWhNrAFEVdGEP5%2Fcard-header-token-type-font-family.png?alt=media&#x26;token=424130b5-4a7a-46d0-ba69-87f7aec7c8c2">card-header-token-type-font-family.png</a></td><td><a href="token-types/typography/font-family">font-family</a></td></tr><tr><td>Font Weight</td><td>Works with Font Family as a pair in Figma. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJCxYWRhGozrkJ8Nm1H6y%2Fcard-header-token-type-font-weight.png?alt=media&#x26;token=ebbb3a84-04e4-48d5-a933-ec9299318eab">card-header-token-type-font-weight.png</a></td><td><a href="token-types/typography/font-weight">font-weight</a></td></tr><tr><td>Line Height</td><td>Define in percentage for responsive design in Figma. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZmjpoAgqKEU1VJecyNPF%2Fcard-header-token-type-line-height.png?alt=media&#x26;token=6a163018-266b-4525-8aa0-e12154c449eb">card-header-token-type-line-height.png</a></td><td><a href="token-types/typography/line-height">line-height</a></td></tr><tr><td>Letter Spacing</td><td>Define in percentage for responsive design in Figma. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FdzNQKeGfQt19oaD7qJRt%2Fcard-header-token-type-letter-spacing.png?alt=media&#x26;token=dea2907a-e016-4873-9095-4d7f65170124">card-header-token-type-letter-spacing.png</a></td><td><a href="token-types/typography/letter-spacing">letter-spacing</a></td></tr><tr><td>Paragraph Spacing</td><td>Matches Figma's text property.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FAcA3u6Ppl6lcUtT77kMI%2Fcard-header-token-type-paragraph-spacing.png?alt=media&#x26;token=613ff7c7-a5cb-416a-9558-b5452254f334">card-header-token-type-paragraph-spacing.png</a></td><td><a href="token-types/typography/paragraph-spacing">paragraph-spacing</a></td></tr><tr><td>Paragraph Indent</td><td>Defined as a Dimension Token.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJHq6ez5odzGzG7yri6m1%2Fcard-header-token-type-paragraph-indent.png?alt=media&#x26;token=7deb17cd-af16-44cb-bfdb-d535e93ba88b">card-header-token-type-paragraph-indent.png</a></td><td><a href="token-types/typography/paragraph-indent">paragraph-indent</a></td></tr><tr><td>Text Decoration</td><td>Define underline or strike for additional emphasis.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FKsyM4AMOvVAMjl7xSorx%2Fcard-header-token-type-text-decoration.png?alt=media&#x26;token=be3108a3-959a-4d3a-b852-bc7b11ddec82">card-header-token-type-text-decoration.png</a></td><td><a href="token-types/typography/text-decoration">text-decoration</a></td></tr><tr><td>Text Case</td><td>Define caps or title case to change text.</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDTfZReUns85bEwpARHhQ%2Fcard-header-token-type-text-case.png?alt=media&#x26;token=9d862020-f157-436f-aa93-11804f86c243">card-header-token-type-text-case.png</a></td><td><a href="token-types/typography/text-case">text-case</a></td></tr></tbody></table>

***

### Common Terms

These terms are not the only way to describe Token Types; they are the labels the Tokens Studio team uses for simplicity across our documentation.&#x20;

If your team uses different descriptive terms, that's totally okay!

**Official**

***Official*** Token Types are listed in the [W3C Design Tokens Community Group (DTCG) Specifications for Design Tokens](https://tr.designtokens.org/format/#types)

For example, **Dimension Token** is an official type.

**Unofficial**

***Unofficial*** Token Types were created by Tokens Studio before the W3C DTCG Specs defined an alternate Token Type.

For example, **Border Width Token** is an unofficial type defined by the spec as a **Dimension Token**.

Tokens Studio will continue to support unofficial Token Types for now. We've already built a conversion into our SD-transforms script; [more details are below ↓](#transforming-tokens).

{% hint style="info" %}
Any Token Types we are planning to deprecate will be listed as `legacy`.
{% endhint %}

**Composite**

When elements are styled by composing many related design decisions together, they are combined into a ***Composite*** Token Type.

For example, a **Typography Token** is composed of 9 independent text-related properties.

**Property**

Each design decision that is a part of the **Composite Token** is referred to as a ***property*** of their respective Composite Token in our guides.

For example, `fontFamily` and `fontWeight`are *unofficial* Tokens we created to independently define the ***properties*** that Compose a `typography` Token.&#x20;

They may be included in the DTCG Specifications in the future, in which case they would be **official property** Tokens.

**Compatible**

A Token Type with properties that is ***compatible*** with another Token Type.&#x20;

For example, the `dimension` Token Type is compatible with `fontSize` when referenced within a `typography` Composite Token.

Compatible Token Types are visible by default when defining Token Values which reference another Token in the plugin. This becomes important when creating and maintaining Tokens in the plugin.

→ Read the Token Values with References guide for more details&#x20;

{% content-ref url="token-values/references" %}
[references](https://docs.tokens.studio/manage-tokens/token-values/references)
{% endcontent-ref %}

***

### Working with Token Types

In the Plugin, you select which Type of Token you'd like to create using a no-code interface. Under the hood, Tokens Studio will write the Token as properly formatted JSON files so they can be used in code. &#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FLj7rtQPMk1pAMcHMpiEa%2FtokenType-overview-all.png?alt=media&#x26;token=5f06f3aa-f7d8-4691-98d5-4dd0e789022a" alt=""><figcaption><p>The Tokens page of the Tokens Studio Plugin shows all Token Types supported. The list is quite long, so the page is scrolled and shown side-by-side to capture them all. </p></figcaption></figure>

You might recall that Design Tokens are platform agnostic, written in a common language so they can shared across different tools and technologies.&#x20;

This means that engineers working with Design Tokens have to ***transform*** them from JSON files into whatever specific programming needs they have before they can work with them.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fae7JX4axDJYJLy97vX25%2Finfographic-transform-sd.png?alt=media&#x26;token=32fbdf4c-3c51-456c-b8a8-71d6b9685d85" alt=""><figcaption><p>The Geko in this infographic represents Style Dictionary.</p></figcaption></figure>

### Transforming Tokens&#x20;

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

Some Tokens we create in Tokens Studio (TS) have subtle differences in how the Token `type` is written compared to the DTCG specifications. In the case of **unofficial** Token Types, which don't exist in the DTCG spec, we have to transform the **TS Type** into something Style Dictionary is prepared to work with.

The SD-Transforms package's preprocessor will transform the **TS Token Type** to the **Style Dictionary Type**, as described in the table below.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

***

### Available Token Types

Each Token Type has unique properties and specifications, which are documented in detail. Select the common name of the Token Type in the table below to access its docs.

<table data-full-width="true"><thead><tr><th width="141">Common Name</th><th width="130">W3C DTCG Official</th><th>Composite</th><th>TS JSON Type</th><th>SD Type</th><th>DTCG Type</th></tr></thead><tbody><tr><td><a href="token-types/color">Color Token</a></td><td>✓</td><td>Can be a Property of <code>border</code>, <code>shadow</code></td><td><code>color</code></td><td><code>color</code></td><td><code>color</code></td></tr><tr><td><a href="token-types/typography">Typography Token</a></td><td>✓</td><td>Composite</td><td><code>typography</code></td><td><code>typography</code></td><td><code>typography</code></td></tr><tr><td><a href="token-types/typography/font-family">Font Family Token</a></td><td>✓</td><td>Property of <code>typography</code></td><td><code>fontFamilies</code> and <code>fontFamily</code></td><td><code>fontFamily</code></td><td><code>fontFamily</code></td></tr><tr><td><a href="token-types/typography/font-weight">Font Weight Token</a></td><td>✓</td><td>Property of <code>typography</code></td><td><code>fontWeights</code> and <code>fontWeight</code></td><td><code>fontWeight</code></td><td><code>fontWeight</code></td></tr><tr><td><a href="token-types/typography/font-size">Font Size Token</a></td><td>✓</td><td>Property of <code>typography</code></td><td><code>fontSizes</code> and <code>fontSize</code></td><td><code>fontSize</code></td><td><code>fontSize</code></td></tr><tr><td><a href="token-types/typography/line-height">Line Height Token</a></td><td>✓</td><td>Property of <code>typography</code></td><td><code>lineHeights</code> and <code>lineHeight</code></td><td><code>lineHeight</code></td><td>NA</td></tr><tr><td><a href="token-types/typography/letter-spacing">Letter Spacing Token</a></td><td>✓</td><td>Property of <code>typography</code></td><td><code>letterSpacing</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/typography/paragraph-spacing">Paragraph Spacing Token</a></td><td>X</td><td>Property of <code>typography</code> (in TS, not DTCG)</td><td><code>paragraphSpacing</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/typography/text-case">Text Case Token</a></td><td>X</td><td>Property of <code>typography</code> (in TS, not DTCG)</td><td><code>textCase</code></td><td><code>textCase</code></td><td>NA</td></tr><tr><td><a href="token-types/typography/text-decoration">Text Decoration Token</a></td><td>X</td><td>Property of <code>typography</code> (in TS, not DTCG)</td><td><code>textDecoration</code></td><td><code>textDecoration</code></td><td>NA</td></tr><tr><td><a href="token-types/dimension">Dimension Token</a></td><td>✓</td><td>Can be a Property of <code>border</code>, <code>shadow</code>, <code>typography</code></td><td><code>dimension</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/number">Number Token</a></td><td>✓</td><td></td><td><code>number</code></td><td><code>number</code></td><td><code>number</code></td></tr><tr><td><a href="token-types/border">Border Token</a></td><td>✓</td><td>Composite</td><td><code>border</code></td><td><code>border</code></td><td><code>border</code></td></tr><tr><td><a href="token-types/box-shadow">Box Shadow Token</a></td><td>✓</td><td>Composite</td><td><code>boxShadow</code></td><td><code>shadow</code></td><td><code>shadow</code></td></tr><tr><td><a href="token-types/dimension/border-radius">Border Radius Token</a></td><td>X</td><td></td><td><code>borderRadius</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/dimension/border-width">Border Width Token</a></td><td>X</td><td></td><td><code>borderWidth</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/dimension/spacing">Spacing Token</a></td><td>X</td><td></td><td><code>spacing</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/dimension/sizing">Sizing Token</a></td><td>X</td><td></td><td><code>sizing</code></td><td><code>dimension</code></td><td><code>dimension</code></td></tr><tr><td><a href="token-types/asset">Asset Token</a></td><td>X</td><td></td><td><code>asset</code></td><td><code>asset</code></td><td>NA</td></tr><tr><td><a href="token-types/boolean">Boolean Token</a></td><td>X</td><td></td><td><code>boolean</code></td><td><code>boolean</code></td><td>NA</td></tr><tr><td><a href="token-types/text">Text Token</a></td><td>X</td><td></td><td><code>text</code></td><td><code>content</code></td><td>NA</td></tr><tr><td><a href="token-types/other">Other Token</a></td><td>X</td><td></td><td><code>other</code></td><td><code>other</code></td><td>NA</td></tr><tr><td><a href="token-types/opacity">Opacity Token</a></td><td>X</td><td></td><td><code>opacity</code></td><td><code>opacity</code></td><td>NA</td></tr><tr><td><a href="token-types/composition">Composition Token</a></td><td>X</td><td></td><td><code>composition</code></td><td>each type in the composition is added individually</td><td>NA</td></tr></tbody></table>

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [8.0 Token Types](https://tr.designtokens.org/format/#types)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Transforming Token Types](https://github.com/tokens-studio/figma-plugin/labels/transform%20tokens)

Tokens Studio Plugin GitHub - [Open issues for Token Type Support](https://github.com/tokens-studio/figma-plugin/labels/token%20types)

* Remove composition tokens [#2800](https://github.com/tokens-studio/figma-plugin/issues/2800)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* Expand Token Types - [Feature request](https://feedback.tokens.studio/p/expand-token-types)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
