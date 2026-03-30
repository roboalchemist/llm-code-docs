# Source: https://docs.tokens.studio/manage-tokens/token-types/dimension/sizing.md

# Sizing

## Sizing - Token Type

Sizing was one of the first Token Types we supported in the plugin.

Since then, a lot has changed.

The Design Tokens Community Group (DTCG) hosts a Token specification on the W3C community group pages for web standards. Although it's in draft form, the tools and technologies working with Design Tokens are trying to align with the W3C DTCG specification.

{% hint style="info" %}
The W3C DTCG specification does not recognize Sizing as an ['official token type'](https://tr.designtokens.org/format/#types) and instead has defined Dimension Token as the preferred token for size-related design decisions.&#x20;
{% endhint %}

If we want to fully align with the spec, it requires Tokens Studio to phase out the Sizing Token. However, we believe the choice should be yours!

If aligning with the W3C DTCG spec is important to your project, we suggest using Dimension Tokens instead.&#x20;

{% content-ref url="" %}
[](https://docs.tokens.studio/manage-tokens/token-types/dimension)
{% endcontent-ref %}

{% hint style="info" %}
There is no immediate plan to discontinue support of the Sizing Token Type.

Until we have a thoughtful solution to migrate between Token Types,  we've included a custom transformation for this Token Type in the sd-transforms npm package[ detailed below↓](#transforming-tokens).&#x20;
{% endhint %}

If you love Sizing Tokens and want to make your voice heard, we've set up a forum in our feedback tool where you can leave your comments! Hopefully with enough support the DTCG may reconsider having Border Width as its own Token Type.&#x20;

→ [Conversation forum on Unofficial Token Types is here.](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXJY8UoBnyYqD9T6zSIiU%2Ftokens-sizing-form-empty-2-01.png?alt=media&#x26;token=a46f71a1-7671-46e6-94f2-f6792e3443d8" alt=""><figcaption><p>Creating a new Sizing Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Sizing defines the height or width of a design element.

<table data-card-size="large" data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><p></p><p>Sizing Tokens can be attached to Number Variables in Figma. </p></td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FMqeS1ogOfJU7wHRyILYe%2Fcard-header-figma-variables.png?alt=media&#x26;token=62e99e18-cc17-45de-89ea-97da18143b02">card-header-figma-variables.png</a></td><td><a href="../../../figma/export">export</a></td></tr></tbody></table>

***

### Possible values

The Sizing Token supports numeric values, with or without a unit.&#x20;

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

To support responsive design, you can define your Sizing Token in `rem units`, and the plugin automatically converts the value to the pixel equivalent when applying the Token in Figma.&#x20;

For example, a Sizing Token with a value of `2rem` will appear as a `32px` in Figma.

**Rem Units** act as a multiplier of the **base font size**, so when a user changes their preferences to a larger font size or uses a zoom feature in your product, elements defined in **rem units** will respond accordingly.

The value of `1rem` can be configured in the [plugin settings for Base Font Size](https://docs.tokens.studio/manage-settings/base-font-size).

#### Pixel units (px)

When you have design elements that should remain static even when users change their preferences, Sizing Tokens can be defined in pixel units.&#x20;

For example `4px`.

### Values that reference another Token

When trying to reference another Token as the Value for a Sizing Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name.**
* Token Type is compatible:
  * The same = `sizing`
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

***

### Apply Sizing Tokens

A Sizing Token defines the width or height of polygonal shape, frames, groups or graphic elements in Figma when the Token is applied. &#x20;

You can apply a Sizing Token to all sides of the design element at once, or each side independently.&#x20;

With one or more elements selected in Figma, right-click on the Sizing Token Name in the Plugin to its options.&#x20;

Select your desired design property by clicking on it to apply the Tokens value instantly.&#x20;

{% hint style="info" %}
If you click to apply this Token to an element without accessing the right-click Token menu, the value will be applied as **all.**&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FWjLbKKjOLdr60SU695Ff%2Ftokens-sizing-rightClick-all-V2-01.png?alt=media&#x26;token=ea6c5d2b-3243-46c6-a59a-555920585afb" alt=""><figcaption><p>The right-click menu of a Sizing Token is open to reveal the design properties it can be applied to in Figma.</p></figcaption></figure>

{% stepper %}
{% step %}

### All

Apply the Token value to the horizontal and vertical size of the design element.
{% endstep %}

{% step %}

### Width

Apply the Token value to the horizontal size of the design element only.&#x20;
{% endstep %}

{% step %}

### Height

Apply the Token value to the vertical size of the design element only.&#x20;
{% endstep %}

{% step %}

### Min Width

Apply the Token value to set the smallest allowed horizontal size of an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Max Width

Apply the Token value to set the largest allowed horizontal size of an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Min Height&#x20;

Apply the Token value to set the smallest allowed vertical size of an auto-layout frame.&#x20;
{% endstep %}

{% step %}

### Max Height

Apply the Token value to set the largest allowed vertical size of an auto-layout frame.&#x20;
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you apply the Token to a frame ***before*** auto-layout is applied in Figma, you may have to remove and re-apply the Token after auto-layout has been enabled for the Token Value to apply as expected.

→ [Read Figma's doc on Autolayout here](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties)
{% endhint %}

Once a Token has been applied, it will remain attached until you manually remove it.&#x20;

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming Sizing Tokens, there are some specific configurations to be aware of.

The preprocessor in the SD-Transforms package will automatically convert the Tokens Studio specific Token Type of `sizing` to align with the DTCG Format Token Type of `dimension`.

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

Tokens Studio Plugin GitHub - [Open issues for Token Type Sizing](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20sizing)

* Deselecting The "All" Property In Spacing Tokens Removes Other Spacing Tokens [#2377](https://github.com/tokens-studio/figma-plugin/issues/2377)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* W3C DTCG Spec - Unofficial Token Types - [Conversation Forum](https://feedback.tokens.studio/p/dtcg-unofficial-token-type)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
