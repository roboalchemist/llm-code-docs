# Source: https://opensource.adobe.com/spectrum-web-components/components/divider/

Title: Divider: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/divider/

Markdown Content:
`sp-divider` brings clarity to a layout by grouping and dividing content that exists in close proximity. It can also be used to establish rhythm and hierarchy.

View the design documentation for this component.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/divider?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/divider?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/divider
Import the side effectful registration of `<sp-divider>` via:

import '@spectrum-web-components/divider/sp-divider.js';
When looking to leverage the `Divider` base class as a type and/or for extension purposes, do so via:

import { Divider } from '@spectrum-web-components/divider';
Horizontal dividers are used to separate content stacked vertically.

Small<h2 class="spectrum-Heading spectrum-Heading--sizeXS">Small</h2>
<sp-divider size="s"></sp-divider>
<p class="spectrum-Body">
  The small divider is used to divide similar components such as table rows,
  action button groups, and components within a panel.
</p>Medium<h2 class="spectrum-Heading spectrum-Heading--sizeS">Medium</h2>
<sp-divider size="m"></sp-divider>
<p class="spectrum-Body">
  The medium divider is used to divide subsections on a page, or to separate
  different groups of components such as panels, rails, etc.
</p>Large<h2 class="spectrum-Heading spectrum-Heading--sizeM">Large</h2>
<sp-divider size="l"></sp-divider>
<p class="spectrum-Body">
  The large divider should be used only for page titles or section titles.
</p>
Vertical dividers are used to separate content horizontally.

When a vertical divider is used inside of a flex container, use `align-self: stretch; height: auto;` on the divider.

Small<div style="height: 32px; display: flex;">
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-divider size="s" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</div>Medium<div style="height: 32px; display: flex;">
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-divider size="m" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</div>Large<div style="height: 32px; display: flex;">
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
  <sp-divider size="l" style="align-self: stretch; height: auto;" vertical ></sp-divider>
  <sp-action-button quiet label="Zoom in">
    <sp-icon-magnify slot="icon"></sp-icon-magnify>
  </sp-action-button>
</div>
Use the static color option when a divider needs to be placed on top of a color background or visual. Static color dividers are available in black or white regardless of color theme.

Static black<div style="background-color: var(--spectrum-docs-static-black-background-color); color: var(--spectrum-black); padding: 20px">
  <h2 class="spectrum-Heading spectrum-Heading--sizeS">
    Static black on light background
  </h2>
  <sp-divider static-color="black" size="m"></sp-divider>
  <p class="spectrum-Body">
    Use static black on light color or image backgrounds.
  </p>
</div>Static white<div style="background-color: var(--spectrum-docs-static-white-background-color); color: var(--spectrum-white); padding: 20px;">
  <h2 class="spectrum-Heading spectrum-Heading--sizeS">
    Static white on dark background
  </h2>
  <sp-divider static-color="white" size="m"></sp-divider>
  <p class="spectrum-Body">
    Use static white on dark color or image backgrounds.
  </p>
</div>
The `<sp-divider>` element implements the following accessibility features:

*   **ARIA role**: Automatically sets `role="separator"` to ensure proper semantic meaning for assistive technologies
*   **Orientation support**: When `vertical` is true, automatically sets `aria-orientation="vertical"` to indicate the divider's orientation

*   Medium or large dividers can be used with header text to visually create a section or page title. Place the divider below the header for best results.
*   Ensure sufficient color contrast when using `static-color` variants on colored backgrounds.
*   Use dividers to create meaningful visual separation, not just decorative lines.
*   Use dividers sparingly; excessive use can diminish their visual impact.

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`283f0fe`, `1d76b70`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

*   #5629`826a2d5` Thanks @rise-erpelding! - **Added**: `staticColor` property to the Divider component, enabling programmatic control of the existing static color functionality.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   **divider:** update a11y semantics (46e6a12)
*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   update to latest spectrum-css packages (a5ca19f)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **divider:** create sp-divider from sp-rule (ec26d81)
*   **divider:** use core tokens (e30c969)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   **divider:** use core tokens (e30c969)

**Note:** Version bump only for package @spectrum-web-components/divider

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   **divider:** update a11y semantics (46e6a12)

**Note:** Version bump only for package @spectrum-web-components/divider

**Note:** Version bump only for package @spectrum-web-components/divider

*   use latest exports specification (a7ecf4b)

*   expand sized functionality to support no default and returning to default values (acf3cfb)
*   update to latest spectrum-css packages (a5ca19f)

*   **divider:** create sp-divider from sp-rule (ec26d81)

Property  Attribute  Type  Default  Description `staticColor``static-color``DividerStaticColor | undefined` The static color variant to use for the divider. `vertical``vertical``boolean``false` Whether the divider is vertical. If false, the divider is horizontal. The default is false.
