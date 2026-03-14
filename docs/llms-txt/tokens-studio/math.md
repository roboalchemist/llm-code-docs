# Source: https://docs.tokens.studio/manage-tokens/token-values/math.md

# Using Math in Token Values

## Using Math in Token Values

Tokens Studio supports math equations to calculate the Value of a Token.

This is a popular approach to a create scales for typography, spacing, size, or dynamically calculate the radius of a focus ring (pictured above).

Combining math equations with referenced to another Token can create a flexible and powerful design system.&#x20;

### Token Types compatible with math

All Token Types that accept numeric values can use math equations to calculate their value in Tokens Studio.&#x20;

When you apply a Token with a math equation as its value, the Plugin applies the resolved value to the corresponding property in Figma.&#x20;

*Select a card to jump to its technical docs.*&#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Dimension</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FIjJYdDQWqHVNbjY6xI0E%2Fcard-header-token-type-dimension.png?alt=media&#x26;token=9d510dda-3952-4c17-a763-c55b2435924b">card-header-token-type-dimension.png</a></td><td><a href="../token-types/dimension">dimension</a></td></tr><tr><td>Number</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FivYNIP6dLorTCpKc1uQd%2Fcard-header-token-type-number.png?alt=media&#x26;token=a79d166e-4428-4d6c-bffc-2f95a32befb2">card-header-token-type-number.png</a></td><td><a href="../token-types/number">number</a></td></tr><tr><td>Spacing</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FCb25KpDXDE4qXMUY4VYR%2Fcard-header-token-type-spacing.png?alt=media&#x26;token=8973c7c4-0a23-4bc0-bc40-1d9e95a4f644">card-header-token-type-spacing.png</a></td><td><a href="../token-types/dimension/spacing">spacing</a></td></tr><tr><td>Sizing</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FD0OMEYi3qmQiCDTKFNDo%2Fcard-header-token-type-sizing.png?alt=media&#x26;token=84d3ab67-5879-4f54-b84e-a7cbfe97014c">card-header-token-type-sizing.png</a></td><td><a href="../token-types/dimension/sizing">sizing</a></td></tr><tr><td>Border Width</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FO2oBQjSparDF0oOo8OcC%2Fcard-header-token-type-borderwidth.png?alt=media&#x26;token=31b86d79-9bcf-4fbb-ad0d-fc2748b34537">card-header-token-type-borderwidth.png</a></td><td><a href="../token-types/dimension/border-width">border-width</a></td></tr><tr><td>Border Radius</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FjtjwZcOInBFKiru4hStl%2Fcard-header-token-type-border-radius.png?alt=media&#x26;token=4f6acf41-9778-4e8c-a98a-a1e0edadc862">card-header-token-type-border-radius.png</a></td><td><a href="../token-types/dimension/border-radius">border-radius</a></td></tr><tr><td>Font Size</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FAwn3zkzamS5c7N7xSyZ7%2Fcard-header-token-type-font-size.png?alt=media&#x26;token=d6798225-3708-4e1f-ad79-1fc16f9c9bd1">card-header-token-type-font-size.png</a></td><td><a href="../token-types/typography/font-size">font-size</a></td></tr><tr><td>Line Height</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZmjpoAgqKEU1VJecyNPF%2Fcard-header-token-type-line-height.png?alt=media&#x26;token=6a163018-266b-4525-8aa0-e12154c449eb">card-header-token-type-line-height.png</a></td><td><a href="../token-types/typography/line-height">line-height</a></td></tr><tr><td>Letter Spacing</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FdzNQKeGfQt19oaD7qJRt%2Fcard-header-token-type-letter-spacing.png?alt=media&#x26;token=dea2907a-e016-4873-9095-4d7f65170124">card-header-token-type-letter-spacing.png</a></td><td><a href="../token-types/typography/letter-spacing">letter-spacing</a></td></tr></tbody></table>

{% hint style="info" %}
Number variables in Figma doesn't support Math equations
{% endhint %}

This means when you export a Token with math in its value as a Variable in Figma:

* You won't see the references or equations.
* The plugin sends the resolved value of the equation to Figma as a Number Variable.

***

### Possible Values

Token Values written as equations can include hard-coded number values and references to other Tokens.&#x20;

For example, if you want `spacing.lg` to be twice as large as `spacing.md` you can write an equation to calculate its value:

```
{spacing.md} * 2
```

Or, you can replace the multipler with a reference to another Token named `scale.multiplier`&#x20;

```
{spacing.md} * {spacing.multipler}
```

#### Syntax

The syntax for writing a math equation varies based on the kind of equation you are writing.

Simple math equations can be written with or without brackets.&#x20;

For example, `8 * 8` and `(8 * 8)` will both resolve to `64`

Complex formulas require spaces between operators to ensure the Tokens can be transformed correctly using Style Dictionary.&#x20;

For example: `8 * 8` will transform as expected `8*8` will not.&#x20;

{% hint style="info" %}
Looking for more complex formulas supported in the Plugin?&#x20;

Here's the docs for [the math package used](https://www.npmjs.com/package/expr-eval?activeTab=readme) under the hood.
{% endhint %}

***

### Known limitations

Working with math in the plugin can be a powerful workflow enhancement, but there are some limitations to be aware of.

#### Multi-value Tokens won't resolve

The plugin supports Tokens with more than one value. When these Tokens are referenced in a math equation, the plugin can not resolve the equation because it doesn't know how to interpret the value.

For example, a [Spacing Token](https://docs.tokens.studio/token-types/dimension/spacing#multiple-values) with `2,4` as its value represents spacing on top/bottom and right/left.

#### Units in equations

Referencing Tokens in our math equations that have values that contain units can lead to unexpected results.

This is because the math package we use can resolve equations with units, as long as the units aren't mixed.

For example:

* A Token named `size-2` with a value of `1.5rem`
* A Token named `density-default` with a value of `2px`

When both Tokens are included in a math equation written as:

```
{size-2} + {density-default}
```

The equation can't be resolved because the Tokens referenced contain a mix of `rem` and `pixel` units. If both Tokens have the same units, or are unitless, the equation would resolve as expected.

**Workarounds**

One method is to create your math equations using the [Other](https://docs.tokens.studio/manage-tokens/token-types/other) or [Number Token](https://docs.tokens.studio/manage-tokens/token-types/number) Types which don't require a unit, and add them in later.

For example, you could create a sizing scale using then add the required unit when it is referenced in a [Typography Token](https://docs.tokens.studio/manage-tokens/token-types/typography).

* lineHeights = `{lineHeights-calc-body-default}%`
* fontSize = `{scale-rem-md}rem`

***

### Equations to try

Here are some math equations used by our team.

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Round to the nearest whole number

When using multipliers that aren't a whole number, you can use a rounding function to calculate values that don't include decimals, because a spacing value of `12.11px` might not be ideal.

To round to the nearest whole number, you can put our equation inside the `roundTo` function.

For example, if `sizing.sm` has a value of `2`

```
roundTo({sizing.sm} * 1.33, 0)
```

`2 * 1.33 = 2.66`

Will calculate a resolved value of  `3`

#### Create a percentage from a unitless number

In Figma, the only option for a [responsive line-height value is in percentage](https://docs.tokens.studio/manage-tokens/token-types/typography/line-height), but your engineers might prefer the Token defined as a unitless number.

In this case, you can create a unitless Number Token with the preferred value, and write an equation in the [Typography Composite Token](https://docs.tokens.studio/token-types/typography#possible-values) to convert it to a percentage so it works well with Figma.&#x20;

For example, the Number Token called `lineHeights-unitless.heading.relaxed` with a value of `1.5` would be written in a Line Height Token as:

```
{lineHeights-unitless.heading.relaxed} * 100%
```

Which calculates a resolved value of `150%`

#### Convert unitless numbers to rem

This equation requires having a Token which defines the value of 1 rem, and adjusting the Tokens Studio plugin settings to reference this Token as the value for "base font size".

[*→ Jump to the guide on Base Font Size Settings*](https://docs.tokens.studio/manage-settings/base-font-size)

In this example, there is a&#x20;

* Number Token called `unitless-Token` with a value of `48`
* Number Token called `rem-base` with a value of `16`

A new Dimension Token is created with the value as an equation:

```
{unitless-Token} / {rem-base} * 1rem
```

Which calculates a resolved value of `3rem`

***

### W3C DTCG Token Format

At the time of writing this doc, Math as a Token value is not mentioned in [the most recent Design Tokens Community Group W3C specifications](https://tr.designtokens.org/format/) for Design Tokens.

Tokens Studio has included this feature in the plugin to help design system maintainers work more efficiently.

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Tokens with Math in their Values, there are specific configurations to be aware of.

Token Values entered with math equations need to be checked and resolved.

→ [SD-Transforms Read-Me Doc, ts/resolveMath](https://github.com/tokens-studio/sd-transforms/?tab=readme-ov-file#tssizepx)

Token Values entered as a number without a unit converted to a number with pixels as a unit.

→ [SD-Transforms Read-Me Doc, ts/size/px](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#tssizepx)

{% hint style="info" %}
Having trouble with Math equations not resolving properly? Check your syntax! \
[↑ Spaces are required between operators as described above. ](#syntax)
{% endhint %}

***

### Resources

Tokens Studio uses the JavaScript Expression Evaluator for the implementation of math in token values.

* nmp - [JavaScript Expression Evaluator](https://www.npmjs.com/package/expr-eval?activeTab=readme)

Mentioned in this doc:

* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms)
* Style Dictionary - [Read Me](https://amzn.github.io/style-dictionary/#/)
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)

#### Community resources:

* Sam I am Designs has a written guide and Figma community file featuring many of the math equations mentioned above.
  * [Sam's Fancy Math Equations in Tokens Studio](https://samiamdesigns.substack.com/p/sams-fancy-math-equations-in-tokens)

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Values Math](https://github.com/tokens-studio/figma-plugin/labels/token%20value%20-%20math%20functions)

* None yet

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* Math in token value enhancements - [Feature Request](https://feedback.tokens.studio/p/math-in-value-enhancements)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
