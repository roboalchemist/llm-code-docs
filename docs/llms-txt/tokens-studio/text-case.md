# Source: https://docs.tokens.studio/manage-tokens/token-types/typography/text-case.md

# Text Case

## Text Case - Token Type

Text Case Tokens define a transformation to the capitalization of letters as an individual property to be composed within a [Typography Token](https://docs.tokens.studio/manage-tokens/token-types/typography). It is **not** intended to be applied to text elements directly.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fvsx7zrwhqftVIkuUancz%2Ftokens-textCase-form-empty-2-01.png?alt=media&#x26;token=b401225a-6ff6-4c73-aa2a-1ba4c61cf298" alt=""><figcaption><p>Creating a new Text Case Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Text Case defines that the system should transform the capitalization of letters in a text element regardless of how they are typed.

In [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform), this property is called `text-transform`.

Text Case design decisions are typically used to:

* communicate the visual emphasis of text or
* standardize data inputs and data display to ensure consistency

Occasionally, they are used for creative styling decisions, for example, a personal blog where the author wants:

* HEADINGS to have all letters capitalized.
* contact details to appear in lowercase.

When we apply a **Typography Composite Token** to a text layer in Figma, these **Text Case** values will change the letter casing:

* All letters appear as typed - `null`
  * By default, the system will not transform the capitalization of letters
* All letters capitalized - `uppercase`
  * Examples:
    * button labels
    * list of countries presented as abbreviations
* No letters are capitalized - `lowercase`
  * Examples:
    * email address listed in a contact section
    * username entered in a sign-up form
* The first letter of each word is capitalized - `capitalize`
  * Examples:
    * full name entered in a sign-up form
    * list of city names

***

### Possible Values

The syntax used to write string values for Design Tokens is important, so be sure to write your Text Case Token value with **all lowercase letters and ensure there are no spaces**.&#x20;

#### Hard-coded Values

The Text Case Token has a few specific string Values depending on your needs.

**null**

Most of the time, text will appear as typed; the Text Case Token Value will be:

```
null
```

**uppercase**

When all letters should be capitalized, set the Text Case Token Value to:

```
uppercase
```

**lowercase**

When none of the letters should be capitalized, set the Text Case Token Value to:

```
lowercase
```

**capitalize**

When the first letter of each word should be capitalized, set the Text Case Token Value to:

```
capitalize
```

Many people confuse Figma's "capitalize" with "title case," but they are different.

* Title case has some words capitalized while others remain lowercase.&#x20;
  * For example `Hyma for Tokens Studio`
* Capitalize transforms all words.&#x20;
  * For example `Hyma For Tokens Studio`

**Not supported by Figma**

Additional text-transform properties commonly used in CSS are not supported in Figma, such as `Full Width`.

You can still create Text Case Tokens with these Values using the Tokens Studio plugin.

When you apply them to design elements in Figma, the Token will be present and visible to engineers inspecting the design element in Figma, but the Token won't interact with the Letter Case property in Figma's UI.

### Values that reference another Token

When trying to reference another Token as the Value for a Text Case Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name.**
* Token Type is compatible:
  * The same = `textCase`

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FzOjvrFocrFgRWJTQ09dV%2Ftokens-typography-form-references-textCase-2-01.png?alt=media&#x26;token=07e0131a-27ab-4913-9917-c15026fdc9bf" alt=""><figcaption><p>The Typography Composite Token form is open, with each property referencing another Token. The Text Case property is highlighted. </p></figcaption></figure>

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

Text Case is not yet an official Token type in the W3C Design Token Community Group specifications.

Tokens Studio has added Text Case as an unofficial Token Type in anticipation of its inclusion in the W3C specs in the near future.

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Test Case tokens, there are no specific transforms to be aware of.

Running the SD-Transforms pre-processor as part of the generic package will prep your Text Case Tokens for Style Dictionary.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

However, Text Case, as part of Typography Composite Tokens, requires the SD-Transforms option to `expand composite Tokens into multiple Tokens`.

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

* Design in Figma - [Explore Text Properties, Letter Case](https://help.figma.com/hc/en-us/articles/360039956634-Explore-text-properties#letter-case)

#### CSS resources:

* MDN Web Docs - [Letter Case](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Text Case](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20text%20case)

* None yet

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
