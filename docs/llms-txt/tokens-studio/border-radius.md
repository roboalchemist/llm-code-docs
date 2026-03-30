# Source: https://docs.tokens.studio/manage-tokens/token-types/dimension/border-radius.md

# Border Radius

## Border Radius - Token Type

Border Radius was one of the first Token Types we supported in the plugin.

Since then, a lot has changed.

The Design Tokens Community Group (DTCG) hosts a Token specification on the W3C community group pages for web standards. Although it's in draft form, the tools and technologies working with Design Tokens are trying to align with the W3C DTCG specification.

{% hint style="info" %}
The W3C DTCG specification does not recognize Border Radius as an ['official token type'](https://tr.designtokens.org/format/#types) and instead has defined Dimension as the preferred Type for radius-related design decisions.
{% endhint %}

If we want to fully align with the spec, it requires Tokens Studio to phase out the Border Radius Token. However, we believe the choice should be yours!

If aligning with the W3C DTCG spec is important to your project, we suggest using Dimension Tokens instead.&#x20;

{% content-ref url="" %}
[](https://docs.tokens.studio/manage-tokens/token-types/dimension)
{% endcontent-ref %}

{% hint style="info" %}
There is no immediate plan to discontinue support of the Border Radius Token Type.

Until we have a thoughtful solution to migrate between Token Types,  we've included a custom transformation for this Token Type in the sd-transforms npm package [detailed below↓](#transforming-tokens).&#x20;
{% endhint %}

If you love Border Radius Tokens and want to make your voice heard, we've set up a forum in our feedback tool where you can leave your comments! Hopefully with enough support the DTCG may reconsider having Border Radius as its own Token Type.&#x20;

→ [Conversation forum on Unofficial Token Types is here.](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fy38kkQLTrRozchhJV0rZ%2Ftokens-borderRadius-form-empty-2-01.png?alt=media&#x26;token=065e1f30-51dc-4b70-8618-5d48cb06a851" alt=""><figcaption><p>Creating a new Border Radius Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Border Radius defines the corner roundness of a design element, such as frames, groups, or polygonal shapes.

<table data-card-size="large" data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><p></p><p>Border Radius Tokens can be attached to Number Variables in Figma. </p></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FMqeS1ogOfJU7wHRyILYe%2Fcard-header-figma-variables.png?alt=media&#x26;token=62e99e18-cc17-45de-89ea-97da18143b02">card-header-figma-variables.png</a></td><td><a href="../../../figma/export">export</a></td></tr></tbody></table>

***

### Possible values

The Border Radius Token supports numeric values with or without a unit.&#x20;

All Token Types that accept numeric values can use math equations to calculate their value in Tokens Studio.

*Jump to the guide on Tokens with Math Values by selecting the card below to learn more.*

{% content-ref url="../../token-values/math" %}
[math](https://docs.tokens.studio/manage-tokens/token-values/math)
{% endcontent-ref %}

#### Hard-coded values

The syntax used to write values for Spacing Tokens is important.&#x20;

* Be sure to avoid any spaces between numbers and units of measurement.&#x20;
* Units are always written in lowercase.

For example:

```
6px
```

**Rem units (rem)**

To support responsive design, you can define your Border Radius Token in `rem units`, and the plugin automatically converts the value to the pixel equivalent when applying the Token in Figma.&#x20;

For example, a Border Radius Token with a value of `1rem` will appear as a `16px` corner radius in Figma.

**Rem Units** act as a multiplier of the **base font size**, so when a user changes their preferences to a larger font size or uses a zoom feature in your product, elements defined in **rem units** will respond accordingly.

The value of `1rem` can be configured in the [plugin settings for Base Font Size](https://docs.tokens.studio/manage-settings/base-font-size).

#### Pixel units (px)

When you have design elements that should remain static even when users change their preferences, Border Radius Tokens can be defined in pixel units.&#x20;

For example, `4px`.

### Values that reference another Token

When trying to reference another Token as the Value for a Border Radius Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name.**
* Token Type is compatible:
  * The same = `borderRadius`
  * `number`
  * `dimension`

However, like all Token Types, you can "force" a reference by manually entering the Token Name between curly brackets.&#x20;

For example `{token.name.here}`

{% hint style="info" %}
The value will show a broken reference until the originating Token Set is marked as enabled.
{% endhint %}

*Jump to the guide on Token Values with References by selecting the card below to learn more.*

{% content-ref url="../../token-values/references" %}
[references](https://docs.tokens.studio/manage-tokens/token-values/references)
{% endcontent-ref %}

### Multiple values

You can define the value of a **Border Radius Token** to mimic how multi-value Border Radius properties are written in CSS.

When you **click to apply the token value** (without right-clicking), the plugin will apply the border radius based on the number of values in your token.

Single value - For example, `10px`

* Applies the value to **all corners**.

Two values - For example, `8px 64px`

* The first value is applied to the radii on the top and bottom.
* The second value is applied to the radii on the right and left.

Three values - For example, `16px 8px 32px`

* The first value is applied to the radius on the top.
* The second value is applied to the radii on the right and left.
* The third value is applied to the radius on the bottom.

Four values - For example, `2px 4px 8px 16px`

* The first value is applied to the radius on the top.
* The second value is applied to the radius on the right.
* The third value is applied to the radius on the bottom.
* The fourth value is applied to the radius on the left.

You can also write multiple value **Border Radius Tokens** with references. For example, `{radius.sm} {radius.md}`.

{% hint style="danger" %}
Figma does not support Variables with multiple values!

If you export your Tokens to Variables in Figma, multiple value Tokens will be skipped, as Figma only supports single values.

[→ Read the guide on Skipped Variables for more details.](https://docs.tokens.studio/figma/export/variables-skipped)
{% endhint %}

***

### Apply Border Radius Tokens

A Border Radius Token defines the corner roundness of polygonal shape, frames, groups or graphic elements in Figma when the Token is applied. &#x20;

You can apply a Border Radius Token to all sides of the design element at once, or each side independently.&#x20;

With one or more elements selected in Figma, right-click on the Border Radius Token Name in the plugin to see the its options.&#x20;

Select your desired design property by clicking on it to apply the Tokens value instantly.

{% hint style="info" %}
If you click to apply a Border Radius Token to an element without accessing the right-click Token menu, the value will be applied to **all** sides if the Token has a single value.&#x20;

If it has multiple values, it will apply the values to the independent properties defined in the Tokens Value. [More details above ↑](#multiple-values)
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FJyLJPFVlkcjcr7HDwEvv%2Ftokens-borderRadius-rightClick-all-V2-01.png?alt=media&#x26;token=1ad3fb09-259c-4e85-9cf4-0dae1a0ad9f4" alt=""><figcaption><p>The right-click menu of a Border Radius Token is open to reveal the design properties it can be applied to in Figma.</p></figcaption></figure>

{% stepper %}
{% step %}

### All

Apply the Token value to the roundness of all corners of the selected design element.
{% endstep %}

{% step %}

### Top left

Apply the Token value to the roundness of the corner on the left highest side of the element on the X-axis only.
{% endstep %}

{% step %}

### Top right

Apply the Token value to the roundness of the corner on the right highest side of the element on the X-axis only.
{% endstep %}

{% step %}

### Bottom right

Apply the Token value to the roundness of the corner on the left lowest side of the element on the X-axis only.
{% endstep %}

{% step %}

### Bottom left

Apply the Token value to the roundness of the corner on the right lowest side of the element on the X-axis only.
{% endstep %}
{% endstepper %}

For independent corner styling, you can repeat the steps above and apply different Border Radius Tokens to each corner position of the same design element. Or, you can modify your Border Radius Tokens to have [multiple values](#multiple-values).&#x20;

Once a Token has been applied, it will remain attached until you manually remove it.&#x20;

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Border Radius Tokens, there are some specific configurations to be aware of.

The preprocessor in the SD-Transforms package will automatically convert the Tokens Studio specific Token Type of `borderRadius` to align with the DTCG Format Token Type of `dimension`.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

**Token Values** entered as a number without a unit will be converted to a number with pixels as a unit.

→ [SD-Transforms Read-Me Doc, ts/size/px](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#tssizepx)

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [8.0 Types](https://tr.designtokens.org/format/#types)

#### Figma resources:

* Design in Figma - [Adjust corner radius and smoothing](https://help.figma.com/hc/en-us/articles/360050986854-Adjust-corner-radius-and-smoothing)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Border Radius](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20border%20radius)

* Color modifiers break when borderRadius token is renamed [#2668](https://github.com/tokens-studio/figma-plugin/issues/2668)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* W3C DTCG Spec - Unofficial Token Types - [Conversation Forum](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
