# Source: https://docs.tokens.studio/manage-tokens/token-types/dimension/spacing.md

# Spacing

## Spacing - Token Type

Spacing was one of the first Token Types we supported in the plugin.

Since then, a lot has changed.

The Design Tokens Community Group (DTCG) hosts a Token specification on the W3C community group pages for web standards. Although it's in draft form, the tools and technologies working with Design Tokens are trying to align with the W3C DTCG specification.

{% hint style="info" %}
The W3C DTCG specification does not recognize Spacing as an ['official token type'](https://tr.designtokens.org/format/#types) and instead has defined Dimension Tokens as the preferred token for space-related design decisions.&#x20;
{% endhint %}

If we want to fully align with the spec, it requires Tokens Studio to phase out the Spacing Token. However, we believe the choice should be yours!

If aligning with the W3C DTCG spec is important to your project, we suggest using Dimension Tokens instead.&#x20;

{% content-ref url="" %}
[](https://docs.tokens.studio/manage-tokens/token-types/dimension)
{% endcontent-ref %}

{% hint style="info" %}
There is no immediate plan to discontinue support of the Spacing Token Type.

Until we have a thoughtful solution to migrate between Token Types,  we've included a custom transformation for this Token Type in the sd-transforms npm package [detailed below↓](#transforming-tokens).&#x20;
{% endhint %}

If you love Spacing Tokens and want to make your voice heard, we've set up a forum in our feedback tool where you can leave your comments! Hopefully with enough support the DTCG may reconsider having Spacing as its own Token Type.&#x20;

→ [Conversation forum on Unofficial Token Types is here.](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FYOOlA3d9Ry2awFxWufH1%2Ftokens-spacing-form-empty-2-01.png?alt=media&#x26;token=a240377e-8ce6-4f10-8fdc-48954570f727" alt=""><figcaption><p>Creating a new Spacing Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Spacing defines the distance between design elements.&#x20;

<table data-card-size="large" data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><p></p><p>Spacing Tokens can be attached to Number Variables in Figma. </p></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FMqeS1ogOfJU7wHRyILYe%2Fcard-header-figma-variables.png?alt=media&#x26;token=62e99e18-cc17-45de-89ea-97da18143b02">card-header-figma-variables.png</a></td><td><a href="../../../figma/export">export</a></td></tr></tbody></table>

***

### Possible values

The Spacing Token supports numeric hard-coded values with or without a unit. You can also enter negative numeric values to achieve a 'stacked' appearance. You can also enter a string value of `AUTO` to support Figma's approach to `space-between`.

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
1rem
```

**Rem units (rem)**

To support responsive design, you can define your Spacing Token in `rem units`, and the plugin automatically converts the value to the pixel equivalent when applying the Token in Figma.

For example, a Spacing Token with a value of `0.5rem` will appear as a `8px` in Figma.

**Rem Units** act as a multiplier of the **base font size**, so when a user changes their preferences to a larger font size or uses a zoom feature in your product, elements defined in **rem units** will respond accordingly.

The value of `1rem` can be configured in the [plugin settings for Base Font Size](https://docs.tokens.studio/manage-settings/base-font-size).

#### Pixel units (px)

When you have design elements that should remain static even when users change their preferences, Spacing Tokens can be defined in pixel units.&#x20;

For example `4px`.

#### AUTO as a value

The plugin supports a string value of `AUTO` to match Figma's unique way of defining the CSS property of `justify-content: space-between` in their Auto Layout feature.

{% hint style="info" %}
It's important that you write this value in all caps `AUTO`&#x20;

Values in lowercase or titlecase will not work as expected.
{% endhint %}

### Values that reference another Token

When trying to **reference another Token as the Value** for a Spacing Token, you will see

* Tokens living in **Token Sets that are currently active**.
  * In the left menu on the plugin's **Tokens page**, a checkmark is visible next to the **Token Set name**.
* **Token Type** is compatible:
  * The same = `spacing`
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

You can define the value of a **Spacing Token** to mimic the way multi-value spacing properties are written in CSS.

When you **click to apply the Token Value** (without right-clicking), the plugin will apply spacing based on the number of values in your token.

Single value - For example, `10px`

* Applies the value to the `Gap` property.

Two values - For example, `8px 64px`

* The first value is applied as padding to the top and bottom.
* The second value is applied as padding to the right and left.

Three values - For example, `16px 8px 32px`

* The first value is applied as padding to the top.
* The second value is applied as padding to the right and left.
* The third value is applied as padding to the bottom.

Four values - For example, `2px 4px 8px 16px`

* The first value is applied as padding to the top.
* The second value is applied as padding to the right.
* The third value is applied as padding to the bottom.
* The fourth value is applied as padding to the left.

You can also write multiple value **Spacing Tokens** with references. For example, `{space.sm} {space.md}`.

{% hint style="danger" %}
Figma does not support Variables with multiple values!

If you export your Tokens to Variables in Figma, multiple value Tokens will be skipped, as Figma only supports single values.

[→ Read the guide on Skipped Variables for more details.](https://docs.tokens.studio/figma/export/variables-skipped)
{% endhint %}

***

### Apply Spacing Tokens&#x20;

A Spacing Token defines the distance between layers of an auto-layout frame in Figma when the Token is applied. &#x20;

You can apply a Spacing Token to all design properties at once, or each independently.&#x20;

Select one or more auto-layout elements in Figma, right-click on the Spacing Token Name in the Plugin to its options.&#x20;

Select your desired design property by clicking on it to apply the Tokens value instantly.&#x20;

{% hint style="info" %}
If you click to apply this Token to an element without accessing the right-click Token menu, the value will be applied to the **gap** (space between) property if your Spacing Token has a single value. \
\
If it has multiple values, it will apply the values to the independent properties defined in the Tokens Value. [More details above. ↑](#multiple-values)
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fa7qjfu0SfdK9a4VcOcch%2Ftokens-spacing-rightClick-all-V2-01.png?alt=media&#x26;token=ccead8c2-6d0d-4495-9a6b-06a548925bb6" alt=""><figcaption><p>The right-click menu of a Sizing Token is open to reveal the design properties it can be applied to in Figma.</p></figcaption></figure>

{% stepper %}
{% step %}

### Gap

Apply the Token value to the space between child elements within an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### All

Apply the Token value to padding on all sides of the parent container, and the space between child elements within an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Horizontal padding

Apply the Token value to the space between the border and child elements on the **left and right sides** an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Vertical padding

Apply the Token value to the space between the border and child elements on the **top and bottom sides** an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Row Gap

Apply the Token value to the space between rows of child elements in auto-layout frames set to wrap.&#x20;
{% endstep %}

{% step %}

### Top

Apply the Token value to padding on the highest side of an auto-layout frame on the X-axis only.
{% endstep %}

{% step %}

### Right

Apply the Token value to padding on the right side of an auto-layout frame on the y-axis only.
{% endstep %}

{% step %}

### Bottom

Apply the Token value to padding on the lowest side of an auto-layout frame on the X-axis only.
{% endstep %}

{% step %}

### Left

Apply the Token value to padding on the left side of an auto-layout frame on the y-axis only.
{% endstep %}
{% endstepper %}

For independent styling per side, you can repeat the steps above and apply different Spacing Tokens to each position of the same design element. Or, you can modify your [Spacing Tokens to have multiple values](#multiple-values).

{% hint style="info" %}
If you apply the Token to a frame ***before*** auto-layout is applied in Figma, you may have to remove and re-apply the Token after auto-layout has been enabled for the Token Value to apply as expected.

→ [Read Figma's doc on Autolayout here](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties)
{% endhint %}

Once a Token has been applied, it will remain attached until you manually remove it.&#x20;

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Spacing Tokens, there are some specific configurations to be aware of.

The preprocessor in the SD-Transforms package will automatically convert the Tokens Studio specific Token Type of `spacing` to align with the DTCG Format Token Type of `dimension`.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

**Token Values** entered as a number without a unit will be converted to a number with pixels as a unit.

→ [SD-Transforms Read-Me Doc, ts/size/px](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#tssizepx)

***

### Resources

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms)
* Style Dictionary - [Read Me](https://amzn.github.io/style-dictionary/#/)
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [8.0 Types](https://tr.designtokens.org/format/#types)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Spacing](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20spacing)

* AUTO Value is Created as '0' in Variables [#2916](https://github.com/tokens-studio/figma-plugin/issues/2916)
  * Exporting to variables when the Spacing Token value is `AUTO` creates a `0` value.

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* W3C DTCG Spec - Unofficial Token Types - [Conversation Forum](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
