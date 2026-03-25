# Source: https://docs.tokens.studio/manage-tokens/token-types/typography.md

# Typography - Composite

## Typography - Token Type

Style text elements by composing many typography-related design decisions together into a single Typography Token.

Each of the nine design decisions (font size, letter spacing, etc.) that is part of the Composite Token is referred to as a **property** of the Typography Token in out guides.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fcif1BPrDV8eiXLk2Mt6Q%2Ftokens-typography-form-annotated-2-01.png?alt=media&#x26;token=770a3a70-4a78-47b5-8c47-b4131fdb6ce9" alt=""><figcaption><p>Creating a new Typography Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions&#x20;

Typography Tokens define a group of properties used to style text elements.

[In CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals), this is known as the `Text and Font Styling` properties, which are defined individually.

Typography Tokens can be applied to text layers to define all styling decisions in a single token.

Each property composed to style text elements can be defined as it's own Token and referenced within the Typography Composite Toke&#x6E;**:**

1. Font family
2. Font weight&#x20;
3. Font size&#x20;
4. Line height
5. Letter spacing&#x20;
6. Paragraph indent&#x20;
7. Paragraph spacing
8. Text decoration
9. Text case

<table data-card-size="large" data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><p></p><p>Typography Tokens can be attached to Text Styles in Figma. </p></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXpF0bqcTa55eT5303TKa%2Fcard-header-figma-styles.png?alt=media&#x26;token=60982acc-63e6-42d3-8f7c-5e7c67e961ef">card-header-figma-styles.png</a></td><td><a href="../../figma/export">export</a></td></tr></tbody></table>

***

### Possible values

Like all Composite Tokens, you define the value of each **property** individually. \
\
When you create the Typography Token in the plugin, you can reference each Token you've already created as a **property** or enter a hard-coded value.

{% hint style="info" %}
The best practice is to define all parts of a Composite Token, even with a `null/none` value, rather than to leave it empty.
{% endhint %}

#### Hard coded values

The dedicated Token Type of each **property** within the Typography Composite Token has unique specifications, described in detail in their own guides.

{% stepper %}
{% step %}

### Font Family

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F9nfWC3hWhNrAFEVdGEP5%2Fcard-header-token-type-font-family.png?alt=media&#x26;token=424130b5-4a7a-46d0-ba69-87f7aec7c8c2" alt="" data-size="original">

Font Family defines the typeface.&#x20;

* It must be written as a string value that exactly matches how Figma has it written in their UI.&#x20;
* It acts as a *'pair'* with Font Weight due to Figma's unique approach to text styling.&#x20;

[*→ Jump to the Font Family Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/font-family)

{% endstep %}

{% step %}

### Font Weight

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJCxYWRhGozrkJ8Nm1H6y%2Fcard-header-token-type-font-weight.png?alt=media&#x26;token=ebbb3a84-04e4-48d5-a933-ec9299318eab" alt="" data-size="original">

Font Weight defines the thickness and styling of the characters of a typeface.&#x20;

* It can be written as a unitless number, or a string value that exactly matches how Figma has written it their UI for the particular typeface.&#x20;
* It acts as a *'pair'* with Font Family due to Figma's unique approach to text styling.&#x20;

[*→ Jump to the Font Weight Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/font-weight)

{% endstep %}

{% step %}

### Font Size

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FAwn3zkzamS5c7N7xSyZ7%2Fcard-header-token-type-font-size.png?alt=media&#x26;token=d6798225-3708-4e1f-ad79-1fc16f9c9bd1" alt="" data-size="original">

Font Size defines the height of the glyphs/characters of a typeface.

* It should be written as a numeric value with a unit of measurement in either pixels or rem.&#x20;
* Font Size impacts the Line Height and Letter Spacing values.&#x20;

[*→ Jump to the Font Size Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/font-size)

{% endstep %}

{% step %}

### Line Height

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZmjpoAgqKEU1VJecyNPF%2Fcard-header-token-type-line-height.png?alt=media&#x26;token=6a163018-266b-4525-8aa0-e12154c449eb" alt="" data-size="original">

Line Height defines the vertical distance of each line of text related to its font size.&#x20;

* It should be written as a numeric value with a percentage to support responsive design in Figma.&#x20;
* Values without a percentage unit will be assumed as a fixed value in pixels.&#x20;

[*→ Jump to the Line Height Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/line-height)

{% endstep %}

{% step %}

### Letter Spacing

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FdzNQKeGfQt19oaD7qJRt%2Fcard-header-token-type-letter-spacing.png?alt=media&#x26;token=dea2907a-e016-4873-9095-4d7f65170124" alt="" data-size="original">

Letter Spacing defines the horizontal distance between each glyph/character related to its font size.&#x20;

* It should be written as a numeric value with a percentage to support responsive design in Figma.&#x20;
* Values without a percentage unit will be assumed as a fixed value in pixels.&#x20;

[*→ Jump to the Letter Spacing Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/letter-spacing)

{% endstep %}

{% step %}

### Paragraph Spacing

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FAcA3u6Ppl6lcUtT77kMI%2Fcard-header-token-type-paragraph-spacing.png?alt=media&#x26;token=613ff7c7-a5cb-416a-9558-b5452254f334" alt="" data-size="original">

Paragraph Spacing defines the vertical distance between 2 paragraphs of text&#x20;

* It should be written as a numeric value with a unit of measurement in either pixels or rem.&#x20;
* Values without a unit will be assumed as a fixed value in pixels.&#x20;

[*→ Jump to the Paragraph Spacing Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/paragraph-spacing)

{% endstep %}

{% step %}

### Paragraph Indent

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJHq6ez5odzGzG7yri6m1%2Fcard-header-token-type-paragraph-indent.png?alt=media&#x26;token=7deb17cd-af16-44cb-bfdb-d535e93ba88b" alt="" data-size="original">

Paragraph Indent defines an offset of the first word of every paragraph.

* It should be written as a numeric value with a unit of measurement in either pixels or rem.&#x20;
* Values without a unit will be assumed as a fixed value in pixels.&#x20;

[*→ Jump to the Paragraph Indent Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/paragraph-indent)

{% endstep %}

{% step %}

### Text Decoration

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FKsyM4AMOvVAMjl7xSorx%2Fcard-header-token-type-text-decoration.png?alt=media&#x26;token=be3108a3-959a-4d3a-b852-bc7b11ddec82" alt="" data-size="original">

Text Decoration defines the position of an optional line in a string of text.&#x20;

* It should be written as the string value that matches the intended property.&#x20;

[*→ Jump to the Text Decoration Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/text-decoration)

{% endstep %}

{% step %}

### Text Case

<img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDTfZReUns85bEwpARHhQ%2Fcard-header-token-type-text-case.png?alt=media&#x26;token=9d862020-f157-436f-aa93-11804f86c243" alt="" data-size="original">

Text Case defines a transformation to the capitalization of letters in a string of text.&#x20;

* It should be written as the string value that matches the intended property.&#x20;

[*→ Jump to the Text Case Guide*](https://docs.tokens.studio/manage-tokens/token-types/typography/text-case)
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Any property defined within the Typography Token that accepts numeric values can use math to calculate their value in Tokens Studio.&#x20;

*There's an example in the image below for Line Height and Letter Spacing to convert a unitless number into a percentage to accommodate Figma's limitations on those properties.*&#x20;

[→ Jump to the guide on Tokens with Math Values for more details.](https://docs.tokens.studio/manage-tokens/token-values/math)
{% endhint %}

### Values that reference another Token

Like all Composite Tokens, you may reference an existing Token as the value for each individual property [as described above ↑](#hard-coded-values).

If you'd prefer to reference an existing Typography Composite Token as the value instead of defining each Property, select the Token's Reference mode button (2x2 circle icon).

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F8OPw2ZX2g0KdcSAqMFpz%2Ftokens-typography-form-references-both-2-01.png?alt=media&#x26;token=7cb95d92-d7d9-45d5-b49c-f00ade7f364d" alt=""><figcaption><p>Once the Typography Token form is open, you can select the icon button to reference a Typography composite Token as the value. </p></figcaption></figure>

When trying to reference another Token as the Value for a Typography Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently **active**.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name**.
* Token Type is compatible:
  * `typography`

However, like all Token Types, you can "force" a reference by manually entering the Token Name between curly brackets.&#x20;

For example `{token.name.here}`

{% hint style="info" %}
The value will show a broken reference until the originating Token Set is marked as enabled.
{% endhint %}

*Jump to the guide on Token Values with References by selecting the card below to learn more.*

{% content-ref url="../token-values/references" %}
[references](https://docs.tokens.studio/manage-tokens/token-values/references)
{% endcontent-ref %}

***

### Apply Typography Tokens

**Typography Tokens** define all 9 styling properties of text when the Token is applied.&#x20;

With one or more text layers selected in Figma, click on the name of a Typography Token in the Plugin to instantly apply its value.&#x20;

Keep in mind, Tokens can only be applied to the entire layer. In the case of Typography, you might want to apply a Token to a particular word within the text layer, but that is not possible today due to limitations of the Figma plugin API.

💌 Create a free account to upvote on the [feature request for this here](https://feedback.tokens.studio/p/multiple-token-per-layer) and we will notify you when we start working on it.&#x20;

Once a Token has been applied, it will remain attached until you manually remove it.&#x20;

***

### Text Styles in Figma

Typography Tokens can be [Exported to Figma as Text Styles](https://docs.tokens.studio/figma/export)**.** Tokens Studio also supports [Styles with Variable References](https://docs.tokens.studio/figma/export/styles-variable-references).

Here are some tips for creating Text Styles with Variable References using the Plugin.&#x20;

{% hint style="info" %}
Before you export your Typography Tokens to Figma as styles, ensure each property within the **Typography Tokens has a value referencing another Token**.
{% endhint %}

When you **Export to Figma**, select these **Options** from the menu:

* `Typography Styles` is selected.
* `Number` and `String Variables` are selected.
* `Create styles with variable references` is selected.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FsPjBKXvNGhcxTAzHvn1a%2Ftokens-typography-export-stylesvar-ref-2-01.png?alt=media&#x26;token=19f87901-b9b6-4d24-be07-3826543ce2ea" alt=""><figcaption><p>Select the Export Styles and Variables from the Tokens page to configure the Options. </p></figcaption></figure>

Ensure your Export to Figma as Themes or Sets configuration includes all necessary Tokens.

* Themes and token sets where the referenced Tokens are located are `active`.
* Themes and token sets where the variables are attached may need to be configured as `reference only`.

You'll notice these Variables are created on Export based on their Token Type:

* `fontFamily` (will create as string variable)
* `fontWeight` (will create either as string or number variable, depending on if they are a string or a number)
* `letterSpacing` (number variable)
* `lineHeight` (number variable)
* `paragraphSpacing` (number variable)
* `paragraphIndent` (number variable)

You'll notice the Text Style will be created on Export, with all possible values mapped to the appropriate Variables, based on the Token Type for each property.

{% hint style="info" %}
For Tokens using percentage units `%`, the plugin will not map this property to the variable created to preserve the responsive design decision in the token.
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FGYb4kY6rio3bUVS1MTl0%2FVariables-Skipped-percentage-typography-V2-1.png?alt=media&#x26;token=a4fd5543-8ece-477d-ac51-52953e058ce8" alt=""><figcaption><p>A Text Style created with Variable References from the Plugin will leave properties with percentage values attached to the Token value and not a variable. The remaining text properties will be attached to Variables. </p></figcaption></figure>

{% hint style="warning" %}
Known issue with Font Weight as Figma doesn't allow changing a Variable Type after its been created.&#x20;
{% endhint %}

If you are converting your [Font Weight Tokens](https://docs.tokens.studio/manage-tokens/token-types/font-weight#possible-values) between numeric and string values and you've already exported to Figma as a Style with Variable References, you may need to delete the Variable from the Figma collection.&#x20;

Figma doesn't allow the changing of a Variable type, so by deleting that single Variable in Figma, when you export the Typography Token as a Style with Variable References, the Plugin will create the variable with the new Token Type.&#x20;

*Jump to the guide on Exporting Tokens to Figma by selecting the card below to learn more.*

{% content-ref url="../../figma/export" %}
[export](https://docs.tokens.studio/figma/export)
{% endcontent-ref %}

***

### W3C DTCG Token Format

`typography` is an official token type in the W3C Design Token Community Group specifications.([9.7 Typography ](https://tr.designtokens.org/format/#typography))

However, Tokens Studio has approached Typography Tokens differently than how it is defined in the current spec draft. We support:

* Additional text properties not defined in the spec.
* Dedicated Token Types for each text property.

We've made these adjustments in the plugin to align with Figma's unique approach to Typography.

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Typography Tokens, which are a Composite Token with several adaptations to accommodate Figma's unique approach to Text Styling, there are specific configurations to be aware of.

**Composite Tokens** require the SD-Transforms option to `expand composite Tokens into multiple Tokens`.

Make sure you look at the generic SD-Transforms package to include this option, which allows you to further customize this transformation further using Style Dictionary.

→ [SD-Transforms Read-Me Doc, Using Expand](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-expand)

{% hint style="info" %}
"object, object" \
When you transform your Typography Tokens and they show `"object, object"`, it means your SD-Transforms configuration needs to be adjusted to include `"expand`".
{% endhint %}

If you are working in **Android Compose**, there is an optional transform to convert `typography objects` into Android Compose shorthand (platform option).

[→ SD-Transforms Read Me Doc, ts/typography/compose/shorthand](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#options)

Each property defined within the Typography Token has individual SD-Transform configurations to be aware of, which can all be found on the [Read Me page on Github.](https://github.com/tokens-studio/sd-transforms/blob/main/README.md)

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [9.7 Typography](ttps://tr.designTokens.org/format/#typography)

#### Figma resources:

* Design in Figma - [Explore Text Properties](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties)

#### CSS resources:

* MDN Web Docs - [Text Styling Fundamentals](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals)

#### Community resources:

* Nate Baldwin's Typography + Dimension scale tool - [Proportio.app](https://proportio.app/)
* Import Typography Styles from Figma into Tokens Studio - [Video Tutorial by Sam I am Designs](https://www.youtube.com/watch?v=Z8o3YDkB6c8)
* Marco Krenn's [Fluid Typescale Generator + Design Token Integration](https://fluid-tokenization.vercel.app/)
  * [Office hours demo of the tool and process (2023)](https://www.youtube.com/watch?v=EbykWCBeqBg)

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Typography Composite](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20typography)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* Enhanced Typography Support - [Feature Request](https://feedback.tokens.studio/p/enhanced-typography-support)
* Expand Token Types - [Feature Request](https://feedback.tokens.studio/p/expand-token-types)
* Support Multiple Token Types per Layer - [Feature Request](https://feedback.tokens.studio/p/multiple-token-per-layer)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
