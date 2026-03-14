# Source: https://opensource.adobe.com/spectrum-web-components/components/progress-bar/

Title: Progress Bar: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/progress-bar/

Markdown Content:
An `<sp-progress-bar>` is used to visually show the progression of a system operation such as downloading, uploading, processing, etc. By default, progress bars have a blue fill that shows the progress.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/progress-bar?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/progress-bar?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/progress-bar
Import the side effectful registration of `<sp-progress-bar>` via:

import '@spectrum-web-components/progress-bar/sp-progress-bar.js';
When looking to leverage the `ProgressBar` base class as a type and/or for extension purposes, do so via:

import { ProgressBar } from '@spectrum-web-components/progress-bar';
Progress bars have the following parts:

*   **Label:** Progress bars should have a label that gives context about the operation being performed. Use an ellipsis at the end of the label text to communicate that the process is in progress.
*   **Value label:** Progress bars can have a value label that gives detailed information about the progress. This value label works alongside the label and should not be displayed if the label itself is not displayed. The value label is always placed above the track. Use the `progress` attribute to set the value label.

<sp-progress-bar label="Generating images..." progress="58"></sp-progress-bar>Small<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar size="s" label="Loaded a little" progress="22" ></sp-progress-bar>
</div>Medium<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar size="m" label="Loaded a little" progress="22" ></sp-progress-bar>
</div>Large<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar size="l" label="Loaded a little" progress="22" ></sp-progress-bar>
</div>Extra Large<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar size="xl" label="Loaded a little" progress="22" ></sp-progress-bar>
</div>Static white
When a progress bar needs to be placed on top of a colored background, use the static white progress bar as signified by `[static-color="white"]`. This progress bar uses a white opaque color no matter the background. Make sure the background offers enough contrast for the loader to be legible.

<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around; background-color: var(--spectrum-seafoam-900);">
  <sp-progress-bar label="Loaded a large amount" progress="77" static-color="white" ></sp-progress-bar>
</div>Indeterminate
A progress bar can be either determinate or indeterminate as signified by `[indeterminate]`. By default, loaders are determinate. Use a determinate loader when progress can be calculated against a specific goal (e.g., downloading a file of a known size). Use an indeterminate loader when progress is happening but the time or effort to completion can’t be determined (e.g., attempting to reconnect to a server).

<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar aria-label="Loaded an unclear amount" indeterminate ></sp-progress-bar>
</div>
The above `sp-progress-bar` also leverages the `aria-label` attribute in place of the `label` attribute in ensure that the element is labelled correctly without that label appearing visibly in the UI.

Side label
A progress bar can be delivered with its labeling displayed above its visual indicator or to either side. Use the boolean `[side-label]` attribute to define where this content should appear.

<div style="width: 240px; height: 160px; display: flex; flex-direction: column; align-items: center; justify-content: space-around;">
  <sp-progress-bar side-label label="Label Beside" progress="23" ></sp-progress-bar>
</div>
An `sp-progress-bar` element will register itself as a `role="progressbar"` element in the accessibility tree. Any value applied to the `label` attribute will be used both to visibly label the element and to set the `aria-label` attribute on the host.

Progress bars should have a label that gives context about the operation being performed. Use an ellipsis at the end of the label text to communicate that the process is in progress.

In rare cases where a visible label is not desired, context is sufficient and an accessibility expert has reviewed the design, be sure to include an `aria-label` attribute or an `aria-labelledby` attribute to manually to ensure that the `sp-progress-bar` correctly fulfills its responsibilities to visitors of your site of all abilities.

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

*   #5553`a292dc7` Thanks @cdransf! - **Added**: Deprecation warning for the over-background attribute.

*   #5535`d5f2909` Thanks @marissahuysentruyt! - Smooths the transition animation of indeterminate progress bar by overriding the incoming CSS, and positioning the animating fill element completely off of the progress bar track in both LTR and RTL languages. Before, the fill element was automatically starting on the track which led to a jarring animation loop.

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

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   remove deprecated 'static' references (#4818)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **progress-bar:** removed duplicate label (#4494) (39b6622)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **progress-bar:** remove aria-label only if set by label and label is empty; add tests (d351451)
*   **styles, theme:** surface exports that omit Spectrum Vars proactively (#4142) (5b524c1)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **meter:** add "variant" (coalescing various boolean attributes) and remove "over-background" attributes (#3514) (40e5f8a)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **meter, progress-bar, progress-circle:** use innerText when label is not provided (#3483) (59358c7)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **meter,progress-bar:** add i18n to progress delivery (c7e4020)

*   update to latest spectrum-css packages (a5ca19f)

*   add t-shirt sizing to the Radio pattern (fc49343)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   delivery dev mode messages in various packages (62370a1)
*   include all Dev Mode files in side effects (f70817c)
*   **progress-bar:** replace bar-loader with progress-bar (182935c)
*   **progress-bar:** use core tokens (540552e)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   **tabs:** add sp-tab-panel element (b17d276)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **progress-bar:** use core tokens (540552e)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   add t-shirt sizing to the Radio pattern (fc49343)

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

**Note:** Version bump only for package @spectrum-web-components/progress-bar

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   **progress-bar:** replace bar-loader with progress-bar (182935c)

Property  Attribute  Type  Default  Description `indeterminate``indeterminate``boolean``false``label``label``string``''``overBackground``over-background``boolean``progress``progress``number``0``sideLabel``side-label``boolean``false``staticColor``static-color``'white' | undefined`
