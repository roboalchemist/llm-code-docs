# Source: https://docs.tokens.studio/manage-tokens/token-types/typography/paragraph-spacing.md

# Paragraph Spacing

## Paragraph Spacing - Token Type

Paragraph Spacing Tokens define the vertical distance between 2 paragraphs of text as an individual property to be composed within a [Typography Token](https://docs.tokens.studio/manage-tokens/token-types/typography). It is **not** intended to be applied to text elements directly.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FScnkCZVAPocIMN9jT4K9%2Ftokens-paragraphSpacing-form-empty-2-01.png?alt=media&#x26;token=ce138014-dd9c-4144-8c8b-70e5cee303df" alt=""><figcaption><p>Creating a new Paragraph Spacing Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Tokens Studio added support for Paragraph Spacing to accommodate Figma's unique way of handling text styles. They use this property to define the vertical distance between 2 paragraphs of text.

This isn't a typical CSS property; you could define it by adding a [margin to your paragraphs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p#accessibility_concerns).&#x20;

{% hint style="info" %}
This property does not appear in Figma's Dev Mode&#x20;

While you can apply the Token using the plugin to change Figma's Paragraph Spacing property, this value does not have a CSS equivalent property so it does not show up in Dev Mode when inspecting CSS.

The Token applied will show up when inspecting Tokens Studio in Dev Mode.

→ Read the Dev Mode guide here.
{% endhint %}

When we apply a **Typography Composite Token** to a text layer in Figma, these **Paragraph Spacing** values will change the text layer:

* Preferred value - `0`
  * No additional space between paragraphs.
  * A line break would be added to create the space needed instead.
  * This most closely matches how spacing between paragraphs would be done in code.
* Relative to **Font Size** - `value in rem units`
  * Example: **Paragraph Spacing** at `0.5rem` with **Font Size** at `1rem`
  * A person who has increased the font size of a mobile phone will see the space between paragraphs half the size of the text.
* Fixed - `value in pixels`
  * Example `8px`
  * The space between paragraphs will remain the same as a user zooms into a webpage.

Paragraph Spacing Tokens can be attached to Number Variables in Figma.

*Jump to the guide on Exporting Tokens to Figma by selecting the card below to learn more.*

{% content-ref url="../../../figma/export" %}
[export](https://docs.tokens.studio/figma/export)
{% endcontent-ref %}

***

### Possible values

Like all Tokens defining a dimension design decision, the value of a **Paragraph Spacing Token** must include a numeric value and, ideally, a unit of measure.

Tokens without a unit specified are applied as the pixel equivalent in Figma.

### Hard-coded values

When writing the hard-coded values for a **Paragraph Spacing Token**, you'll want to:

* Avoid spaces
* Include a number and unit of measure.
  * Values without a unit will be translated to pixels in Figma.
  * The value should always be greater than 0.
* Or use the specified string (below) for the `normal` value.

**rem units (rem)**

To support responsive design, you can define your Paragraph Spacing Token in **rem units**, and the plugin automatically converts the value to the pixel equivalent when the Typography Composite Token is applied to the text element in Figma.&#x20;

For example, a Paragraph Spacing Token with a value of `1rem`, when applied as a Typography Composite Token, will appear as `16px` in Figma.

**Rem Units** act as a multiplier of the **base font size**, so when a user changes their preferences to a larger font size or uses a zoom feature in your product, elements defined in **rem units** will respond accordingly.

The value of `1rem` can be configured in the [plugin settings for Base Font Size](https://docs.tokens.studio/manage-settings/base-font-size).

**Pixel units (px)**

While its not common, should you require the space between every paragraph to remain static even when users change their preferences, the Paragraph Spacing value can be defined in pixel units. For example:

```
16px
```

### Values that reference another Token

When trying to reference another Token as the Value for a Paragraph Spacing Token,  you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name.**
* Token Type is compatible:
  * The same = `paragraphSpacing`
  * `dimension`
  * `number`

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FBUXmJS0XqE2HiXxE303p%2Ftokens-typography-form-references-paragraphSpacing-2-01.png?alt=media&#x26;token=1a555961-7ad5-45cb-b708-17024fcce49e" alt=""><figcaption><p>The Typography Composite Token form is open, with each property referencing another Token. The Paragraph Spacing property is highlighted. </p></figcaption></figure>

However, like all Token Types, you can "force" a reference by manually entering the Token Name between curly brackets.&#x20;

For example `{token.name.here}`

{% hint style="info" %}
The value will show a broken reference until the originating Token Set is marked as enabled.
{% endhint %}

*Jump to the guide on Token Values with References by selecting the card below to learn more.*

{% content-ref url="../../token-values/references" %}
[references](https://docs.tokens.studio/manage-tokens/token-values/references)
{% endcontent-ref %}

***

### W3C DTCG Token Format

Paragraph Spacing is not an official token type in the W3C Design Token Community Group specifications.

Tokens Studio has added Paragraph Spacing as an unofficial Token Type to support Figma's unique approach to this text property.

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Paragraph Spacing Tokens, there are specific configurations to be aware of.

The preprocessor in the SD-Transforms package will automatically convert the Tokens Studio specific Token Type of `paragraphSpacing` to align with the DTCG Format Token Type of `dimension`.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

Paragraph Spacing, as part of Typography Composite Tokens, requires the SD-Transforms option to `expand composite Tokens into multiple Tokens`.

Make sure you look at the generic SD-Transforms package to include this option, which allows you to further customize this transformation further using Style Dictionary.

→ [SD-Transforms Read-Me Doc, Using Expand](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-expand)

{% hint style="info" %}
"object, object" \
When you transform your Typography Tokens and they show `"object, object"`, it means your SD-Transforms configuration needs to be adjusted to include `"expand`".
{% endhint %}

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [9.7 Typography](ttps://tr.designTokens.org/format/#typography)

#### Figma resources:

* Design in Figma - Explore Text Properties, [Paragraph Spacing](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties#paragraph-spacing)

#### CSS resources:

* MDN Web Docs - [The paragraph element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p#accessibility_concerns)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Paragraph Spacing](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20paragraph%20spacing)

* None yet

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
