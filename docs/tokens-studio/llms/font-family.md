# Source: https://docs.tokens.studio/manage-tokens/token-types/typography/font-family.md

# Font Family

## Font Family - Token Type

Font Family Tokens define typeface as an individual property to be composed within a [Typography Token](https://docs.tokens.studio/manage-tokens/token-types/typography). It is **not** intended to be applied to text elements directly.&#x20;

{% hint style="info" %}
Font Family and Font Weight Tokens work as a pair in Figma.

Figma's unique approach to combining Font Weight and Style as a single property written as a string value requires an exact match to the Font Family it is paired with.&#x20;

This means you must apply both Font Family and Font Weight Tokens at the same time to interact with Figma's text properties and see a visual change.
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F7n4IHcqM9GdzdqwlbdO2%2Ftokens-fontFamily-form-empty-2-01.png?alt=media&#x26;token=7a26abf3-5d28-4973-b514-58df2d0cb365" alt=""><figcaption><p>Creating a new Font Family Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Font Family defines a group of related fonts that vary in weight, style or width but maintain a consistent visual appearance and share the same design characteristics.

In [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) this property is called `font-family`.

Font Family design decisions ensure that text elements are easy to read in a particular context while representing the visual style of the brand/product/service.

A design system will typically define which Font Family is to be used when text within a visual design calls for:

* serif font
* sans-serif font
* mono-spaced font
* decorative font

<table data-card-size="large" data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><p></p><p>Font Family Tokens can be attached to String Variables in Figma. </p></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FMqeS1ogOfJU7wHRyILYe%2Fcard-header-figma-variables.png?alt=media&#x26;token=62e99e18-cc17-45de-89ea-97da18143b02">card-header-figma-variables.png</a></td><td><a href="../../../figma/export">export</a></td></tr></tbody></table>

***

### Possible values

The Value of a Font Family Token must be identical to the text string value for the Font Family in the Figma design panel due to limitations from Figma (plugin API).

When writing the string value of a Font Family Token, pay close attention to:

* Spelling
* Spacing
* Punctuation
* Use of capital letters

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F7OXdBIcvnMJYB23KlPZE%2FtokenType-fontFamily-values-string-ref-2-01.png?alt=media&#x26;token=fc4402f4-95dc-4d3c-9c58-75cbb1d8a2e5" alt=""><figcaption><p>Once the Font Family Token form is open, select the value dropdown to open the menu. The Token tab shows compatible Font Family Tokens available to reference as the value. </p></figcaption></figure>

#### Hard-coded values

To ensure your Font Family Token values are an exact match to what Figma has, you can:

* Carefully type it out, paying attention to the syntax in Figma.
* Save your Font Family and Font Weight pairs as text styles in Figma, then import them into the plugin to see how they appear.
* Select the value from the Tokens Studio menu, pictured below.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FlTVpfQ3sB1NzKZ2jy4Dd%2FtokenType-typography-form-fontFam-references-suggest-2-01.png?alt=media&#x26;token=6f771351-09da-4e0d-a105-9935122dbcb6" alt=""><figcaption><p>Once the Font Family Token form is open, select the value dropdown to open the menu. The Fonts tab shows available Font Families from Figma to set as the hard-coded value. </p></figcaption></figure>

### Values that reference another Token

When trying to reference another Token as the Value for a Font Family Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name**.
* Token Type is compatible:
  * The same = `fontFamilies`

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F81ReTNm21FyxKfhwHcop%2Ftokens-typography-form-references-fontFamily2-01.png?alt=media&#x26;token=b589a4d1-3135-41b8-982b-e884f976fb52" alt=""><figcaption><p>The Typography Composite Token form is open, with each property referencing another Token. The Font Family property is highlighted. </p></figcaption></figure>

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

**Font Family is an official Token Type** in the in the W3C Design Token Community Group specifications.( [8.3 Font Family](https://tr.designtokens.org/format/#font-family))

It is mentioned as a required part of a [typography token](https://tr.designtokens.org/format/#typography)

> "The typography's font. The value of this property *MUST* be a valid font family value or a reference to a font family token." - 9.7. Typography

#### Token Type syntax

In Tokens Studio, the Font Family Token has a unique syntax in code which identifies if the token is:

* An independent property Token
* Part of a Typography Composite Token

Looking at the JSON format, the `"type"` is written in plural `"fontFamilies`" when the Font Size Token is defined as an independent property Token.

This example shows a Font Family property Token named `font-family-sans` with a value of Satoshi Variable (see line 4).

{% code lineNumbers="true" %}

```json
{
  "font-family-sans": {
      "value": "Satoshi Variable",
      "type": "fontFamilies"
    }
  }
```

{% endcode %}

This is in contrast to the Typography Composite Token, which has the property Token `"type"` written in the singular `"fontFamily"`.

This example shows a Typography composite token with the Font Family Token named `font-family-sans` referenced as the value (see line 4).&#x20;

{% code lineNumbers="true" %}

```json
{
  "paragraph-3": {
    "value": {
      "fontFamily": "{font-family-sans}",
      "fontWeight": "{font-weight-default}",
      "lineHeight": "{line-height-classic}",
      "fontSize": "{font-size-small}",
      "letterSpacing": "{letter-spacing-tight}",
      "paragraphSpacing": "{paragraphSpacing.none}"
      "paragraphIndent": "{paragraphIndent.none}"
      "textCase": "{textCase.none}",
      "textDecoration": "{textDecoration.none}"
    },
    "type": "typography"
  }
}
```

{% endcode %}

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Font Family Tokens, there are specific configurations to be aware of.

The preprocessor in the SD-Transforms package will automatically convert the Tokens Studio specific Token Type of `fontFamilies` to align with the DTCG Format Token Type of `fontFamily`.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

Font Family, as a part of Typography Composite Tokens, require the SD-Transforms option to `expand composite Tokens into multiple Tokens`.

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
* Style Dictionary -[ https://styledictionary.com/](https://styledictionary.com/)
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [8.3 Font Family](https://tr.designtokens.org/format/#font-family)
* Design Tokens Community Group - [9.7 Typography](ttps://tr.designTokens.org/format/#typography)

#### Figma resources:

* Design in Figma - [Explore Text Properties, Font Family](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties#font-family)
* Figma Learn - \[Add a font in Figma]\(# Add a font to Figma design)

#### CSS resources:

* MDN Web Docs - [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)

#### Community resources:

* Font Weight + Font Family Pairs explained by [Sam I am Designs](https://bento.me/samiam)
  * [It took me 2 years to figure out that Typography in Figma is not how text properties work in code.](https://samiamdesigns.substack.com/p/it-took-me-2-years-to-figure-out)
  * Import Typography Styles from Figma into Tokens Studio - [Video Tutorial by Sam I am Designs](https://www.youtube.com/watch?v=Z8o3YDkB6c8)

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Font Family](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20font%20family)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
