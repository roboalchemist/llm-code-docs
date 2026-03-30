# Source: https://docs.tokens.studio/debug/inspect-tokens.md

# Inspect Tokens

## Inspect Tokens in the Plugin

The **Inspect page** of the Plugin is where you can see which Tokens have been applied to a selected design element in Figma and modify the Tokens as needed.&#x20;

{% hint style="info" %}
The way this page appears changes based on the elements you have currently selected on the Figma canvas.&#x20;

→ [Read Figma's guide on selecting layers and objects for more details.](https://help.figma.com/hc/en-us/articles/360040449873-Select-layers-and-objects)
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fw4cgvuYhWkjGh1PNrSp0%2Finspect-layers-selected-V2-3-4.png?alt=media&#x26;token=457878ac-fca7-47d1-8bcb-a1559ca90803" alt=""><figcaption><p>The left side example shows how the Inspect page looks before selecting a Figma design element compared with the right side example, showing many Tokens applied to a selected layer in Figma. </p></figcaption></figure>

There are three main sections on the Inspect Page visible when a design element is selected in Figma:

1. [Inspect Controls](#id-1.-inspect-controls)
2. [Token Actions](#id-2.-token-actions)
3. [Token List](#id-3.-token-list)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FFAZ2yyXYRaNhzvipIle3%2Finspect-sections-annotated-V2-3-4.png?alt=media&#x26;token=d2a2f6e0-760d-43be-b793-f1ca29db192f" alt=""><figcaption><p>The Inspect page of the Plugin is shown with its controls annotated with numbers that match the sections mentioned above. </p></figcaption></figure>

### 1. Inspect Controls

The actions at the top of the Inspect Page control how the Plugin displays the Tokens being inspected below it:

A. [Token Name Search](#a.-token-name-search)

B. [Deep Inspect](#b.-deep-inspect)

C. [Inspect Options](#c.-inspect-options)

D. [Token View Toggle](#d.-token-view-toggle)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FvVP6msTmhxoiFJlZm0nd%2Finspect-controls-annotated-V2-3-3.png?alt=media&#x26;token=d9b01dee-9331-4df7-8ab4-de978805ce56" alt=""><figcaption><p>The Inspect page of the Plugin is shown with its controls annotated with letters that match their detailed descriptions below. </p></figcaption></figure>

#### A. Token Name Search&#x20;

When you type in the search input, only the Design Tokens with names that match will appear in the Token list below.&#x20;

{% hint style="info" %}
Like the search feature on the Tokens Page, the results are limited to Token Name. The Token Type and names references in values are not included in the search.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FK6DZarjDKggQCJUvP3wy%2FinspectControls-search-V2-3-4.png?alt=media&#x26;token=52609ec4-5662-4a4e-9709-ba25b77a1767" alt=""><figcaption><p>The left example of the Inspect page of the Plugin shows a list of Tokens. The example on the right shows how entering in the search term "col" filters the Tokens listed below it to only those with that exact string in the Token Name. </p></figcaption></figure>

If you select another design element in Figma before clearing the search input, the Plugin will only display Token names that match your search. This can help speed up workflows where you are looking for specific Tokens across designs in your Figma file.&#x20;

#### B. Deep Inspect

The Deep Inspect feature controls how many layers of your selected Figma element are being looked at by the Plugin.&#x20;

* Deep Inspect Off - empty checkbox&#x20;
  * Currently selected layer is being inspected.
  * Only Tokens applied directly to the current layer appear in the Token list below.&#x20;

Deep Inspect On- checkmark visible

* Current layer and all children layers below are being inspected.&#x20;
* All Tokens applied to the current layer and children layers appear in the Token list below.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fx3x5jISioN2zbgxokbLE%2FinspectControls-deepInspect-V2-3-4.png?alt=media&#x26;token=bd41e3d5-48e0-496b-ab4c-7d53bb31d85c" alt=""><figcaption><p>The example on the left shows the Inspect page of the plugin with the Deep Inspect feature disabled (no checkmark) and a single Token listed below. The example on the right shows the Deep Inspect feature enabled (checkmark visible) and 4 Tokens listed below. </p></figcaption></figure>

The Deep Inspect feature in the Plugin is the only way to see all Tokens applied to a design element at once. Figma's native features in Dev Mode or their Inspect views only shows the current selected layer and ignore all children layers.&#x20;

{% hint style="info" %}
Icons tend to be tricky with layers!&#x20;

Color Tokens applied to style the vector path are always applied to the children layers, and when selecting the parent container without deep inspect enabled you might miss them! This is a common complaint in Dev Mode in Figma as well to be aware of!&#x20;
{% endhint %}

#### C. Inspect Options

The Inspect Options menu contains some handy filters if you are working with design elements in Figma with lots of Tokens applied to them:

1. Show broken references&#x20;
   * Controls visibility of Tokens applied that have an issue blocking the Plugin from resolving the value of the Token correctly.&#x20;
   * Most often there is an issue with the Token Name not being found in the plugin, or the value of the Token has an error.
2. Show resolved references
   * Controls visibility of Tokens applied with no issues detected by the Plugin. &#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FdRL7zVLIEpdSJbW7sIJ4%2FinspectControls-options-showResolved-V2-3-4.png?alt=media&#x26;token=dd374eed-7ded-4d3e-a289-f952b6d81128" alt=""><figcaption><p>The example on the left shows the Inspect page of the plugin with a list of Tokens below, which includes a broken Token. The example on the right shows the Inspect Options menu open with the "show broken references" disabled (no checkmark), and the list of Tokens below does not include any broken Tokens. </p></figcaption></figure>

For example you are only checking for Broken Tokens, you could deselect the `show resolved references`option so the checkmark is not visible. That way any layers you are inspecting in the Plugin will only show Tokens with broken references in the list below so you can find what you are looking for faster.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2g6wWt43WdI0hKASgC1N%2FinspectControls-options-showBroken-V2-3-4.png?alt=media&#x26;token=a5d13837-0cd3-4df7-a313-cdf25f90180a" alt=""><figcaption><p>The example on the left shows the Inspect page of the plugin with a list of Tokens below, which includes a broken Token. The example on the right shows the Inspect Options menu open with the "show resolved references" disabled (no checkmark), and the list of Tokens below only shows the broken Token. </p></figcaption></figure>

#### D. Token View Toggle

Much like on the Tokens page of the Plugin, the Tokens View toggle allows you to switch between the no-code (list) and code (debug) views.&#x20;

By default, the Inspect page is on the List view. You can select the `i`icon button to toggle to the debug view.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F4giGCUfQgjkHcpDoIIV8%2Finspect-debug-toggle-V2-3-3.png?alt=media&#x26;token=c14f3418-9efe-4d46-a6e4-8c842d1134d8" alt=""><figcaption><p>With a card element selected in the Figma canvas in the middle, the Plugin screenshot on the left shows the Inspect page as the List view. The screenshot on the right shows the Inspect page in debug view. The controls to toggle between views are annotated. </p></figcaption></figure>

#### Debug and Annotate

When you are inspecting a selected layer in the Plugin from the Debug View, you will see all Tokens applied to the layer written in code.&#x20;

You can also select one of the arrows to create a static annotation element next to the selected layer in the Figma file. The annotation element will include the names of all Tokens applied to the selected layer and an arrow indicating which layer the annotation belongs to.&#x20;

For example, selecting the arrow pointing down will place the annotation element underneath the design element on the Figma canvas.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FDsU53k2BgiboN6qQ3G1F%2Finspect-debug-annotation-down-V2-3-3.png?alt=media&#x26;token=fabb86a5-19b6-4e13-860c-bf6f8b205c41" alt=""><figcaption><p>With a card element selected in the Figma canvas on the lift, the Plugin screenshot on the right shows the Inspect page in the debug view. The controls to Add as an annotation on the bottom are highlighted to show the output from the plugin for the selected card element. </p></figcaption></figure>

{% hint style="info" %}
The annotations generated are static, acting like a snapshot in time. You can manually apply a Documentation Token if you want the annotations to change if the Token Names change in the future. \
\
→[ Jump to the guide on Documentation Tokens for more details. ](https://docs.tokens.studio/manage-tokens/apply/documentation-tokens)
{% endhint %}

***

### 2. Token Actions

These actions allow you to interact with the Tokens listed below them:

A. [Select All ](#a.-select-all)

B. [Bulk Remap](#b.-bulk-remap)&#x20;

C. [Set to None](#c.-set-to-none)

D. [Remove Selected ](#d.-remove-selected)

{% hint style="info" %}
You can perform bulk actions on more than on design element in Figma! Simply select everything in your design that you want the Plugin to inspect at the same time.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FItzhILo44l3yvMxvwtiH%2Finspect-tokenActions-annotated-V2-3-4.png?alt=media&#x26;token=ed408bf9-4ecb-481f-b784-f2679f2077b1" alt=""><figcaption><p>The Inspect page of the Plugin is shown with the Token Actions annotated with letters that match their detailed descriptions below. </p></figcaption></figure>

#### A. Select All&#x20;

The Select All feature controls the Tokens listed below it:

* Select All Off - empty checkbox&#x20;
  * Individual Tokens below it can be selected as required.&#x20;

Select All On- checkmark visible

* All Tokens below it will be selected with their checkmarks visible.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FrDgYerZQGQrlXPMDFCJO%2FinspectActions-selectAll-V2-3-3.png?alt=media&#x26;token=c7abe74c-290a-44ff-86e4-ad10540b5f71" alt=""><figcaption><p>The left screenshot of the Inspect page of the plugin shows the Select all control as disabled (no checkmark), and one of the Tokens listed below has a checkmark visible. The example on the right shows how enabling the Select All control will change all Tokens listed below to have a checkmark visible next to their name. </p></figcaption></figure>

#### B. Bulk Remap

Selecting the Bulk Remap button allows you to use a match and replace feature to update the names of multiple Tokens applied to design elements in your Figma file. This is helpful in fixing broken Tokens that were not [remapped to after editing a Token's name](https://docs.tokens.studio/manage-tokens/token-names/edit#id-2.-configure-your-remap-options).&#x20;

The Bulk Remap modal allows you to match and replace strings of Token Names using the inputs:

1. Match - the string you'd like the Plugin to find.&#x20;
2. Replace - the new string that will replace all instances the Plugin finds that match.&#x20;
3. Remap across document (slow) - tells the Plugin to expand the action across the entire Figma file instead of limiting it to the currently selected design elements.&#x20;

Once you've filled out the inputs with your desired strings, be sure to select the Remap button to save your changes.&#x20;

Once you are finished Remapping all desired Tokens, you'll need to navigate back to the Tokens Page and select the Apply Token Data button to push the new values to Figma to complete the process.&#x20;

→ [Jump to the Remap Tokens guide for more details. ](https://docs.tokens.studio/debug/remap-tokens)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXlJdlNWtUsBtuoky7PB9%2Finspect-bulkRemap-annotated-V2-3-4.png?alt=media&#x26;token=e4f78cb0-a1b9-4559-84f6-8c30b3966a94" alt=""><figcaption><p>Selecting the Bulk Remap button on the Inspect page of the Plugin will open the Bulk Remap modal, pictured on the right, with numeric annotations to match the inputs described above. </p></figcaption></figure>

#### C. Set to None

Selecting the Set to None feature was developed for working with instances of components in Figma.&#x20;

You can not remove a Token from an instance of a component due to the way that components work in Figma. If you apply another Token, Style or Variable to the same property as an over-ride, when the Plugin runs the value of the Token applied to the main component will be applied, effectively erasing your styling over ride. \
\
So to get around this limitation, you can use the Set to None feature which tells the plugin to change the value of the Token to `none` without removing it. When the value is `none` , you can style that property with another Token, Style or Variable in Figma. When the Plugin runs in the future, your over-ride will persist.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2OjZd0PIMMc4nh495vW7%2FtokenName-setNone-annotated-V2-3-2.png?alt=media&#x26;token=069ef2fe-dc98-4a3d-8555-0750d5cbde27" alt=""><figcaption><p>Selecting the Set to none button on the Inspect page of the Plugin will change the value of the selected Token to "none" as pictured on the right. </p></figcaption></figure>

#### D. Remove Selected

The Remove Selected button allows you to remove Tokens that are listed below with the checkmark visible from your chosen design elements on the Figma canvas.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FEMPpkHCei667LBRPaEjw%2Finspect-removeSelected-flow-V2-4-1.png?alt=media&#x26;token=4e5fe88b-a17d-4fa7-9c9d-975b7177d265" alt=""><figcaption><p>Selecting the Remove selected button on the Inspect page of the Plugin will remove the Tokens with a checkmark next to them. </p></figcaption></figure>

#### Limitations of removing Tokens

The Plugin can not remove Tokens from instances of components. You'll need to use the Set to None feature instead ([↑ described above](#c.-set-to-none)).

The Plugin can not remove Variables or Styles applied to design elements with Figma's native features.&#x20;

There are also some nuances of removing Tokens from the Inspect or Tokens Page of the Plugin to be aware of, which are described in detail in the Remove Tokens guide.&#x20;

{% content-ref url="../figma/remove-tokens" %}
[remove-tokens](https://docs.tokens.studio/figma/remove-tokens)
{% endcontent-ref %}

***

### 3. Token List

Once you've selected a design element in Figma, the Tokens applied are listed in the Plugin. Each Token Type will appear in the list with slight differences, but all Tokens in the list share the same anatomy:&#x20;

A. [Design Property](#id-3.-token-list)

B. [Select Token Control](#b.-select-token)

C. [Value Preview](#c.-value-preview)

D. [Token Application Symbol ](#d.-token-application-symbol)

E. [Token Name ](#e.-token-name)

F. [Figma Layer Actions](#f.-figma-layer-actions)

{% hint style="info" %}
It's important to remember that the controls and actions above the Token List influence which Tokens you will see for the currently selected design element on the Figma canvas.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FHW7R792OZAvotAggmohj%2Finspect-tokenList-annotated-V2-3-4.png?alt=media&#x26;token=d5dbfe10-fbb6-48ec-850f-64f569aa5d9b" alt=""><figcaption><p>The Inspect page of the Plugin is shown with the Token List features annotated with letters that match their detailed descriptions below. </p></figcaption></figure>

#### A. Design Property&#x20;

The Tokens in the list are organized by the design property they have been applied to for the selected elements on the Figma canvas.

The design property appears as the heading of the Tokens listed below it.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FQWf7ExJurya8NpPWvHTc%2Finspect-tokenListProperty-annotated-V2-3-4.png?alt=media&#x26;token=dd3b9277-a521-41dd-a5a5-46584af95728" alt=""><figcaption><p>An example of the Inspect page of the Plugin shows a long list of Tokens with the design properties they were applied to highlighted. </p></figcaption></figure>

The names of the design properties displayed on the inspect page don't always match the design properties displayed when you right click on a Token to apply it to a design element. \
\
Here's a list of the design properties you'll see on inspect page and the corresponding Token Type. You can select the Token Type to jump to its guide.&#x20;

<table><thead><tr><th width="259.296875">Design Property</th><th>Common Name</th><th>Token Types</th></tr></thead><tbody><tr><td><code>asset</code></td><td>Assets/images</td><td><a href="../manage-tokens/token-types/asset">Asset</a></td></tr><tr><td><code>backgroundBlur</code></td><td>Background blur</td><td><a href="../../manage-tokens/token-types/dimension#id-5.-background-blur">Dimension</a></td></tr><tr><td><code>border</code></td><td>Border all sides</td><td><a href="../../manage-tokens/token-types/border#apply-border-tokens">Border</a></td></tr><tr><td><code>borderBottom</code></td><td>Bottom border only</td><td><a href="../../manage-tokens/token-types/border#apply-border-tokens">Border</a></td></tr><tr><td><code>borderColor</code></td><td>Border/stroke color</td><td><a href="../../manage-tokens/token-types/color#apply-color-tokens">Color</a></td></tr><tr><td><code>borderLeft</code></td><td>Left border properties</td><td><a href="../../manage-tokens/token-types/border#apply-border-tokens">Border</a></td></tr><tr><td><code>borderRadius</code></td><td>Border radius (all corners)</td><td><a href="../../manage-tokens/token-types/dimension#id-3.-border-radius">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-radius#apply-border-radius-tokens">Border Radius</a></td></tr><tr><td><code>borderRadiusBottomLeft</code></td><td>Bottom-left border radius</td><td><a href="../../manage-tokens/token-types/dimension#id-3.-border-radius">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-radius#apply-border-radius-tokens">Border Radius</a></td></tr><tr><td><code>borderRadiusBottomRight</code></td><td>Bottom-right border radius</td><td><a href="../../manage-tokens/token-types/dimension#id-3.-border-radius">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-radius#apply-border-radius-tokens">Border Radius</a></td></tr><tr><td><code>borderRadiusTopLeft</code></td><td>Top-left border radius</td><td><a href="../../manage-tokens/token-types/dimension#id-3.-border-radius">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-radius#apply-border-radius-tokens">Border Radius</a></td></tr><tr><td><code>borderRadiusTopRight</code></td><td>Top-right border radius</td><td><a href="../../manage-tokens/token-types/dimension#id-3.-border-radius">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-radius#apply-border-radius-tokens">Border Radius</a></td></tr><tr><td><code>borderRight</code></td><td>Right border properties</td><td><a href="../../manage-tokens/token-types/border#apply-border-tokens">Border</a></td></tr><tr><td><code>borderTop</code></td><td>Top border properties</td><td><a href="../../manage-tokens/token-types/border#apply-border-tokens">Border</a></td></tr><tr><td><code>borderWidth</code></td><td>Border width</td><td><a href="../../manage-tokens/token-types/dimension#id-4.-border-width">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-width#apply-border-width-tokens">Border Width</a></td></tr><tr><td><code>borderWidthBottom</code></td><td>Bottom border width</td><td><a href="../../manage-tokens/token-types/dimension#id-4.-border-width">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-width#apply-border-width-tokens">Border Width</a></td></tr><tr><td><code>borderWidthLeft</code></td><td>Left border width</td><td><a href="../../manage-tokens/token-types/dimension#id-4.-border-width">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-width#apply-border-width-tokens">Border Width</a></td></tr><tr><td><code>borderWidthRight</code></td><td>Right border width</td><td><a href="../../manage-tokens/token-types/dimension#id-4.-border-width">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-width#apply-border-width-tokens">Border Width</a></td></tr><tr><td><code>borderWidthTop</code></td><td>Top border width</td><td><a href="../../manage-tokens/token-types/dimension#id-4.-border-width">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/border-width#apply-border-width-tokens">Border Width</a></td></tr><tr><td><code>boxShadow</code></td><td>Box shadow</td><td><a href="../manage-tokens/token-types/box-shadow">BoxShadow</a></td></tr><tr><td><code>composition</code></td><td>Composition (legacy)</td><td><a href="../manage-tokens/token-types/composition">Composition</a></td></tr><tr><td><code>counterAxisSpacing</code></td><td>Row gap</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>description</code></td><td>Token description</td><td><a href="../../manage-tokens/apply/documentation-tokens#description">Documentation Tokens</a></td></tr><tr><td><code>dimension</code></td><td>Dimension without property specified</td><td><a href="../../manage-tokens/token-types/dimension#apply-dimension-tokens">Dimension</a></td></tr><tr><td><code>fill</code></td><td>Fill color</td><td><a href="../../manage-tokens/token-types/color#apply-color-tokens">Color</a></td></tr><tr><td><code>height</code></td><td>Height</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>horizontalPadding</code></td><td>Horizontal padding</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>itemSpacing</code></td><td>Spacing between items</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>maxHeight</code></td><td>Maximum height</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>maxWidth</code></td><td>Maximum width</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>minHeight</code></td><td>Minimum height</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>minWidth</code></td><td>Minimum width</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>number</code></td><td>Number without property specified</td><td><a href="../../manage-tokens/token-types/number#apply-number-tokens">Number</a></td></tr><tr><td><code>opacity</code></td><td>Opacity/transparency</td><td><a href="../../manage-tokens/token-types/opacity#apply-opacity-tokens">Opacity</a></td></tr><tr><td><code>paddingBottom</code></td><td>Bottom padding</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>paddingLeft</code></td><td>Left padding</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>paddingRight</code></td><td>Right padding</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>paddingTop</code></td><td>Top padding</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>rotation</code></td><td>Rotation</td><td><a href="../../manage-tokens/token-types/number#id-7.-rotation">Number</a></td></tr><tr><td><code>sizing</code></td><td>Size (width and height)</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>spacing</code></td><td>General spacing</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>text</code></td><td>String text content</td><td><a href="../manage-tokens/token-types/text">Text</a></td></tr><tr><td><code>textDecoration</code></td><td>Text decoration</td><td><a href="../manage-tokens/token-types/typography/text-decoration">Text Decoration</a></td></tr><tr><td><code>tokenName</code></td><td>Token name</td><td><a href="../../manage-tokens/apply/documentation-tokens#description">Documentation Token</a></td></tr><tr><td><code>tokenValue</code></td><td>Token raw value</td><td><a href="../../manage-tokens/apply/documentation-tokens#token-value-raw">Documentation Token</a></td></tr><tr><td><code>typography</code></td><td>Typography Composite </td><td><a href="../manage-tokens/token-types/typography">Typography</a></td></tr><tr><td><code>verticalPadding</code></td><td>Vertical padding</td><td><a href="../../manage-tokens/token-types/dimension#id-1.-spacing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/spacing#apply-spacing-tokens">Spacing</a>, <a href="../../manage-tokens/token-types/number#id-1.-spacing">Number</a></td></tr><tr><td><code>value</code></td><td>Token resolved value </td><td><a href="../../manage-tokens/apply/documentation-tokens#value-resolved">Documentation Token</a></td></tr><tr><td><code>visibility</code></td><td>Visibility state</td><td><a href="../../manage-tokens/token-types/boolean#apply-boolean-tokens">Boolean</a></td></tr><tr><td><code>width</code></td><td>Width</td><td><a href="../../manage-tokens/token-types/dimension#id-2.-sizing">Dimension</a>, <a href="../../manage-tokens/token-types/dimension/sizing#apply-sizing-tokens">Sizing</a>, <a href="../../manage-tokens/token-types/number#id-2.-sizing">Number</a></td></tr><tr><td><code>x</code></td><td>X position</td><td><a href="../../manage-tokens/token-types/dimension#id-6.-x-and-y-position">Dimension</a>, <a href="../../manage-tokens/token-types/number#id-6.-x-and-y-position">Number</a></td></tr><tr><td><code>y</code></td><td>Y position</td><td><a href="../../manage-tokens/token-types/dimension#id-6.-x-and-y-position">Dimension</a>, <a href="../../manage-tokens/token-types/number#id-6.-x-and-y-position">Number</a></td></tr></tbody></table>

#### B. Select Token&#x20;

The Select Token control allows the bulk actions above the list to be applied to the Token:

* Empty checkbox&#x20;
  * This Token will be skipped from bulk actions.
* Checkmark visible
  * Bulk actions will be applied to this Token.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FHZ5aiwNnPFICsMkLwhct%2Finspect-tokenListSelect-annotated-V2-3-4.png?alt=media&#x26;token=a31e7881-32da-4bd4-8ffc-e33d3dcadf86" alt=""><figcaption><p>An example of the Inspect page of the Plugin highlights the Bulk Actions after a Token in the list below has been enabled (checkmark visible). </p></figcaption></figure>

#### C. Value Preview

Each Token Type will preview the [Resolved Value](https://docs.tokens.studio/manage-tokens/token-values#resolved-value) of the Token in a slightly different way. For example, Color Tokens display a swatch of the color, where as a Dimension Token shows the numeric value.&#x20;

* When a Token is "broken" and it's value can not be resolved, the value will be replaced with an icon of a broken link (↓ more details below).&#x20;
* When the Value has been Set to None using the bulk action, the value will be replaced with an icon of a circle with a line through it ([↑ more details above](#c.-set-to-none)).&#x20;

{% hint style="info" %}
Known Issue \
When values are long, sometimes the UI preview will appear visually broken or cut off.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FR7eOt84A3e3hktg3FRzb%2Finspect-tokenListValue-annotated-V2-3-4.png?alt=media&#x26;token=82e732ed-301b-45d7-b901-ca778216328a" alt=""><figcaption><p>An example of the Inspect page of the Plugin highlights the Token Values for several different Token Types described above.</p></figcaption></figure>

#### D. Token Application Symbol

The Plugin will display a symbol next to the Token Name to indicate how it was applied to the design element.&#x20;

1. Applied with Tokens Studio - no symbol
2. Applied as a Figma Style - 2 x 2 dots
3. Applied as a Figma Variable - Hexagon&#x20;
4. Broken Token - Chain link with line through it.&#x20;
5. Value Set to None - Circle with a line through it.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPG0sYm56V2ecSDh0ldv5%2Finspect-tokenListApplication-annotated-V2-3-4.png?alt=media&#x26;token=de3c8ef3-a009-4ab9-b0dd-7616a8feb3a4" alt=""><figcaption><p>An example of the Inspect page of the Plugin highlights the symbols for how Tokens were applied to the selected design element as described above.</p></figcaption></figure>

#### E. Token Name

The Token Name that Figma is using as the ID of the design decision will show in the list. If the Token was applied using the Plugin directly, you can select the chevron to the right of the name to access the Remap feature.&#x20;

If you use the remap feature it will only apply the changes to the design elements on the Figma Canvas that are currently selected. You can use the actions to the right of the Token Name to check which layers are selected ([described below ↓](#f.-figma-layer-actions)).&#x20;

→ [Jump to the Remap Tokens guide for more details. ](https://docs.tokens.studio/debug/remap-tokens)

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F2jFcnyRuFBYSlAJPt7Jf%2Finspect-tokenListName-remapFlow-V2-3-4.png?alt=media&#x26;token=cd529da5-b067-4c72-96b3-bb3970072066" alt=""><figcaption><p>An example of the Inspect page of the Plugin shows how to open the remap feature by selecting the chevron next to the Name of a Token in the list. </p></figcaption></figure>

#### F.  Figma Layer Actions

The actions on the right side of the Token list interact with the layers within your selected design elements in Figma. These actions allow for fine-grained control of selecting the correct layers when debugging Tokens that are broken or require remapping:

1. Layer count - the number of layers the Token is applied to&#x20;
   1. Selecting the layer count will open a list of the layer names.&#x20;
2. Layer navigation - will change the Plugin's current selected layers to the layers listed in the count to the left.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F05y17UX90Los1DOaG0R2%2Finspect-tokenListLayers-Annotated-V2-3-4.png?alt=media&#x26;token=7ee66614-a362-4e51-bd5b-6e3ac01a1f27" alt=""><figcaption><p>An example of the Inspect page of the Plugin shows the Figma Layer features. On the left, the layer selected feature is highlighted. On the right, the layer count is highlighted with an example showing a specific Figma layer name when the count is selected. </p></figcaption></figure>

***

### Resources

Mentioned in this doc:

* Figma Learn - [Select layers and objects](https://help.figma.com/hc/en-us/articles/360040449873-Select-layers-and-objects)

#### Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Inspect](https://github.com/tokens-studio/figma-plugin/labels/Inspect%20tab)

Tokens Studio Plugin GitHub - [Open issues for Deep Inspect](https://github.com/tokens-studio/figma-plugin/labels/Inspect%20deep)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* None yet.&#x20;

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
