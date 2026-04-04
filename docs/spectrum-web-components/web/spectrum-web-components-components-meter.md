# Source: https://opensource.adobe.com/spectrum-web-components/components/meter/

Title: Meter: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/meter/

Markdown Content:
An `<sp-meter>` is a visual representation of a quantity or achievement. The meter's progress is determined by user actions, rather than system actions.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/meter?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/meter?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/meter
Import the side-effectful registration of `<sp-meter>` via:

import '@spectrum-web-components/meter/sp-meter.js';
When looking to leverage the `Meter` base class as a type and/or for extension purposes, do so via:

import { Meter } from '@spectrum-web-components/meter';
The meter consists of several key parts:

*   A label that describes what is being measured
*   A progress track showing the total possible range
*   A fill bar indicating the current progress
*   A percentage value showing the numeric progress

<sp-meter progress="71">Tasks Completed</sp-meter>
The label is the text that describes what is being measured. It can be provided either through the default slot or the `label` attribute.

<sp-meter progress="15">Course Progress</sp-meter>
<br />
<sp-meter progress="15" label="Course Progress"></sp-meter>Small<sp-meter size="s" progress="25">Tasks Completed</sp-meter>Medium<sp-meter size="m" progress="25">Tasks Completed</sp-meter>Large<sp-meter size="l" progress="25">Tasks Completed</sp-meter>Extra Large<sp-meter size="xl" progress="25">Tasks Completed</sp-meter>
The meter supports several variants to convey different semantic meanings:

Informative
By default, the informative variant can be used to represent a neutral or non-semantic value, such as the number of tutorials completed.

<sp-meter progress="50">Storage Space</sp-meter>Positive
The positive variant can be used to represent a positive semantic value, such as when there's a lot of space remaining. Use value `variant="positive"` to define a positive variant.

<sp-meter variant="positive" progress="50">Storage Space</sp-meter>Notice
The notice variant can be used to warn users about a situation that may need to be addressed soon, such as when space remaining is becoming limited. Use value `variant="notice"` to define a notice variant.

<sp-meter variant="notice" progress="73">Storage Space</sp-meter>Negative
The negative variant can be used to warn users about a critical situation that needs their urgent attention, such as when space remaining is becoming very limited. Use value `variant="negative"` to define a negative variant.

<sp-meter variant="negative" progress="92">Storage Space</sp-meter>
A meter can be delivered with its labeling displayed above its visual indicator or to either side. Use the boolean `side-label` attribute to define where this content should appear.

<sp-meter side-label progress="68">Side Label</sp-meter>
The `<sp-meter>` element is rendered with `role="meter progressbar"` to ensure proper semantics for assistive technologies. The current progress value is set as a percentager via the `progress` attribute and is exposed to assistive technology via `aria-valuenow`.

<sp-meter progress="71" label="Download Progress">Download Progress</sp-meter>
A meter is required to have either a visible text label or a `label` attribute.

The meter's variants provide semantic meaning through both color and ARIA attributes, ensuring that information is not conveyed through color alone. The progress track and fill maintain sufficient contrast for visibility.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/field-label@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/field-label@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`7af5e8f`, `b95e254`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/field-label@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/field-label@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies [`7d23140`, `72d807c`]: 
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/field-label@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`165a904`]: 
    *   @spectrum-web-components/field-label@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/field-label@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/field-label@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   **button:** adds pending button, fixes #3162 (#3163) (71254ec)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/meter

*   **meter:** add "variant" (coalescing various boolean attributes) and remove "over-background" attributes (#3514) (40e5f8a)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   **meter, progress-bar, progress-circle:** use innerText when label is not provided (#3483) (59358c7)
*   **meter:** added role meter progressbar in meter component (#3459) (d2eccef)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   **meter,progress-bar:** add i18n to progress delivery (c7e4020)

*   address a11y issues raised by updating our dependencies (4f06477)
*   **meter:** remove comment (27687ec)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update export patterns (b2da444)
*   update to latest spectrum-css packages (a5ca19f)
*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)

*   **action-button:** add action button pattern (03ac00a)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   include all Dev Mode files in side effects (f70817c)
*   **meter:** add meter pattern (fa092ba)
*   **meter:** update spectrum css input (683bb1a)
*   **progress-bar:** use core tokens (540552e)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use latest exports specification (a7ecf4b)
*   use SixedMixin to manage "size" property (8819821)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   **progress-bar:** use core tokens (540552e)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   use ObserveSlotText mixin to prevent white space from overriding label attribute (610fb4b)

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

**Note:** Version bump only for package @spectrum-web-components/meter

**Note:** Version bump only for package @spectrum-web-components/meter

*   address a11y issues raised by updating our dependencies (4f06477)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update export patterns (b2da444)
*   **meter:** remove comment (27687ec)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **meter:** add meter pattern (fa092ba)
*   **meter:** update spectrum css input (683bb1a)

*   stop merging selectors in a way that alters the cascade (369388f)
*   update export patterns (b2da444)
*   **meter:** remove comment (27687ec)

*   apply sizedMixin for t-shirt sizing (d7b63fb)
*   use SixedMixin to manage "size" property (8819821)
*   **action-button:** add action button pattern (03ac00a)
*   **meter:** add meter pattern (fa092ba)
*   **meter:** update spectrum css input (683bb1a)

Property  Attribute  Type  Default  Description `label``label``string``''``progress``progress``number``0``sideLabel``side-label``boolean``false``staticColor``static-color``'white' | undefined``variant``variant``MeterVariants` The variant applies specific styling when set to `negative`, `positive`, `notice` `variant` attribute is removed when not matching one of the above.

Name  Description `default slot` text labeling the Meter
