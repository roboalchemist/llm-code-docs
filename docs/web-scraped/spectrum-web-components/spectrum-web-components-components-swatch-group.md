# Source: https://opensource.adobe.com/spectrum-web-components/components/swatch-group/

Title: Swatch Group: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/swatch-group/

Markdown Content:
An `<sp-swatch-group>` group is a grouping of `<sp-swatch>` elements that are related to each other.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/swatch?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/swatch?style=for-the-badge)

yarn add @spectrum-web-components/swatch
Import the side effectful registration of `<sp-swatch-group>` via:

import '@spectrum-web-components/swatch/sp-swatch-group.js';
When looking to leverage the `SwatchGroup` base class as a type and/or for extension purposes, do so via:

import { SwatchGroup } from '@spectrum-web-components/swatch';
Just like swatches, swatch groups come in four different sizes: extra-small, small, medium, and large. The medium size is the default option. This only affects the size of each individual swatch, not the spacing between them.

Extra Small<sp-swatch-group size="xs">
  <sp-swatch color="var(--spectrum-gray-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-red-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-orange-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-yellow-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-chartreuse-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-celery-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-green-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-seafoam-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Small<sp-swatch-group size="s">
  <sp-swatch color="var(--spectrum-gray-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-red-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-orange-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-yellow-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-chartreuse-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-celery-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-green-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-seafoam-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Medium<sp-swatch-group size="m">
  <sp-swatch color="var(--spectrum-gray-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-red-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-orange-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-yellow-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-chartreuse-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-celery-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-green-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-seafoam-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Large<sp-swatch-group size="l">
  <sp-swatch color="var(--spectrum-gray-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-red-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-orange-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-yellow-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-chartreuse-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-celery-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-green-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-seafoam-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>
Swatch groups come in 3 densities: regular (default), compact, and spacious. The `density` attribute/property is not required and when applied accepts the values of `compact` or `spacious`. When not applied or undefined, the density of the group is set to regular (default).

Regular<sp-swatch-group>
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Compact<sp-swatch-group density="compact">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>Spacious<sp-swatch-group density="spacious">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>
An `<sp-swatch-group>` element has two selection modes. The `selects` property can be set to either `single`, indicating a user can choose up to one swatch, or `multiple`, indicating a user can choose more than one swatch.

When the `selects` property is set to one of these values, the `selected` property of `<sp-swatch-group>` will surface an array the represents the string values that have been selected in the UI. This `selected` property can be populated in two ways: through user input, or directly from `<sp-swatch>` children.

When the value of `selected` is updated via user input, the `change` event will be dispatched on the `<sp-swatch-group>` element to announce that interaction. Calling `preventDefault()` on the `change` event will prevent both the `<sp-swatch-group>` and the `<sp-swatch>` that initiated the `change` interaction from updating their `selected` values.

The value of the `selected` property also can be provided directly from the `<sp-swatch>` children. Child `<sp-swatch>` elements with their own `selected` attribute will be gathered and merged with any other selection data on the `<sp-swatch-group>` parent to populate `selected`.

The `selected` property is always an array, so applications can programmatically set multiple selections regardless of the value of `selects`. However, user interactions will respect the `selects` property and enforce either single or multiple selection behavior accordingly.

Single<sp-swatch-group selects="single" onchange="this.nextElementSibling.textContent = `Selected: ${JSON.stringify(this.selected, null, ' ')}`">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)" selected></sp-swatch>
</sp-swatch-group>
<div>Selected: [ "var(--spectrum-magenta-500)" ]</div>Multiple
`<sp-swatch>` children of an `<sp-swatch-group selects="multiple">` parent will toggle their selection.

<sp-swatch-group selects="multiple" onchange="this.nextElementSibling.textContent = `Selected: ${JSON.stringify(this.selected, null, ' ')}`">
  <sp-swatch color="var(--spectrum-blue-500)" selected></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)" selected></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)"></sp-swatch>
</sp-swatch-group>
<div>
  Selected: [ "var(--spectrum-blue-500)", "var(--spectrum-purple-500)" ]
</div>
When available, the `selected` property will be populated with the `value` attributes/properties of the child `<sp-swatch>` elements. This is useful when you need the swatch data to correlate to a hash or identifier rather than the raw color string.

<sp-swatch-group selects="multiple" selected='["color-2"]' onchange="this.nextElementSibling.textContent = `Selected: ${JSON.stringify(this.selected, null, ' ')}`">
  <sp-swatch color="var(--spectrum-blue-500)" value="color-0"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)" value="color-1" selected ></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)" value="color-2"></sp-swatch>
  <sp-swatch color="var(--spectrum-fuchsia-500)" value="color-3" selected ></sp-swatch>
  <sp-swatch color="var(--spectrum-magenta-500)" value="color-4"></sp-swatch>
</sp-swatch-group>
<div>Selected: [ "color-2", "color-1", "color-3" ]</div>
An `<sp-swatch-group>` element can be modified by the following attributes/properties to customize its delivery as desired for your use case: `border`, `density`, `rounding`, `shape`, and `size`. Use these in concert with each other for a variety of final visual deliveries. Applying a value for one of these attributes/properties to an `<sp-swatch-group>` element will have it forward the value to all of the `<sp-swatch>` elements that are a direct child of the group, overriding any value that may be applied directly to those children.

Once applied to an `<sp-swatch-group>` element, the value of the `border`, `rounding`, `shape`, and `size` attributes/properties cannot be overridden on the children `<sp-swatch>` elements.

Shape<sp-swatch-group shape="rectangle">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
</sp-swatch-group>Rounding<sp-swatch-group rounding="full">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
</sp-swatch-group>No Rounding<sp-swatch-group rounding="none">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
</sp-swatch-group>Border<sp-swatch-group border="light">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
</sp-swatch-group>No Border<sp-swatch-group border="none">
  <sp-swatch color="var(--spectrum-blue-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-indigo-500)"></sp-swatch>
  <sp-swatch color="var(--spectrum-purple-500)"></sp-swatch>
</sp-swatch-group>
The swatch group implements several accessibility features:

*   `tabindex="0"` on the selected swatch and unselected swatches have `tabindex="-1"`
*   The swatch group role changes based on the `selects` property. When `selects="single"`, the group has `role="radiogroup"` and each swatch gets a `role="radio"`. When `selects="multiple"`, the group has `role="group"` and each swatch gets a `role="checkbox"`.

*   Ensure swatches have sufficient color contrast for visibility.
*   Verify that swatch groups are appropriately labeled for screen readers by adding `aria-label` or `aria-labelledby` attributes to describe the purpose of the group.

*   `Tab`: Move focus to the next focusable element
*   `Arrow keys`: Navigate between swatches in the group and move the focus indicator
*   `Enter` or `Space`: Select the focused swatch

Property  Attribute  Type  Default  Description `border``border``SwatchBorder``density``density``'compact' | 'spacious' | undefined``rounding``rounding``SwatchRounding``selected``selected``string[]``selects``selects``SwatchSelects``shape``shape``SwatchShape`

Name  Description `default slot` Swatch elements to manage as a group

Name  Type  Description `change``Event`
