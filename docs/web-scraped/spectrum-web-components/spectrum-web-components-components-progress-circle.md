# Source: https://opensource.adobe.com/spectrum-web-components/components/progress-circle/

Title: Progress Circle: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/progress-circle/

Markdown Content:
An `<sp-progress-circle>` shows the progression of a system operation such as downloading, uploading, processing, etc. in a visual way. It can represent both determinate and indeterminate progress, helping users understand the status of ongoing operations.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/progress-circle?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/progress-circle?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/progress-circle

Import the side effectful registration of `<sp-progress-circle>` via:

import '@spectrum-web-components/progress-circle/sp-progress-circle.js';

When looking to leverage the `ProgressCircle` base class as a type and/or for extension purposes, do so via:

import { ProgressCircle } from '@spectrum-web-components/progress-circle';

A progress circle consists of several key parts:

*   A label (via `slot="label"`)
*   A progress value (via `progress` attribute)
*   An optional indeterminate state (via `indeterminate` attribute)

<sp-progress-circle label="Download progress" progress="75"></sp-progress-circle>
Progress circles come in three sizes to fit various contexts:

Small<sp-progress-circle size="s" label="Small progress indicator" progress="42"></sp-progress-circle>Medium<sp-progress-circle label="Medium progress indicator" progress="67"></sp-progress-circle>Large<sp-progress-circle size="l" label="Large progress indicator" progress="89"></sp-progress-circle>
When displaying over images or colored backgrounds, use the `static-color` attribute for better contrast:

<div style="background-color: rgb(15, 15, 15); padding: 20px;">
  <sp-progress-circle label="Progress on dark background" progress="50" static-color="white" ></sp-progress-circle>
</div>
Use indeterminate progress when the duration cannot be calculated:

<sp-progress-circle label="Loading content" indeterminate></sp-progress-circle>
The `<sp-progress-circle>` element implements several accessibility features:

1.   **ARIA Role**: Automatically sets `role="progressbar"` for proper semantic meaning
2.   **Labeling**: 
    *   Uses the `label` attribute value as `aria-label`
    *   When determinate, adds `aria-valuenow` with the current progress
    *   Includes `aria-valuemin="0"` and `aria-valuemax="100"` for the progress range

3.   **Status Communication**: 
    *   Screen readers announce progress updates
    *   Indeterminate state is properly conveyed to assistive technologies

*   Always provide a descriptive `label` that explains what the progress represents
*   Use determinate progress when possible to give users a clear sense of completion
*   For determinate progress, ensure the `progress` value accurately reflects the actual progress
*   Consider using size="l" for primary loading states to improve visibility
*   Ensure sufficient color contrast when using `static-color="white"`

<sp-progress-circle label="Downloading report.pdf - 24 MB of 50 MB" progress="48"></sp-progress-circle>

<sp-progress-circle label="Connecting to server" indeterminate></sp-progress-circle>

*   Updated dependencies [`6f5419a`]: 
    *   @spectrum-web-components/core@0.0.4
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/core@0.0.3
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`283f0fe`, `1d76b70`, `f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/core@0.0.2
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   #5730`7d23140` Thanks @caseyisonit! - - **Fixed**: Accessibility warning logic in `<sp-progress-circle>` component.

    *   **Fixed**: Updated accessibility warning logic to only apply when `role="progressbar"` is explicitly set
    *   **Fixed**: Improved label validation for better accessibility compliance

These changes ensure accessibility warnings are only shown when appropriate and improve overall accessibility compliance.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   remove progress-circle overBackground property (#4750)

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   **progress-circle:** remove aria-label only when set by label and changed label is empty (cdd181a)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   **progress-circle:** ensure size can be applied to non-"size" attribute bearing elements (2bc1065)

*   **icon:** use core tokens (a11ef6b)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   **progress-circle,toast,tooltip:** ensure complete dependency graph (#3701) (a5dfada)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   **meter, progress-bar, progress-circle:** use innerText when label is not provided (#3483) (59358c7)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   update to latest spectrum-css packages (a5ca19f)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   delivery dev mode messages in various packages (62370a1)
*   include all Dev Mode files in side effects (f70817c)
*   **progress-circle:** replace circle-loader with progress-circle (a852140)
*   **progress-circle:** use core tokens (587ac63)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   **progress-circle:** use core tokens (587ac63)

*   include all Dev Mode files in side effects (f70817c)

*   delivery dev mode messages in various packages (62370a1)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

**Note:** Version bump only for package @spectrum-web-components/progress-circle

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   **progress-circle:** replace circle-loader with progress-circle (a852140)

 Property  Attribute  Type  Default  Description `indeterminate``indeterminate``boolean``false` Whether the progress circle shows indeterminate progress (loading state). 
When true, displays an animated loading indicator instead of a specific progress value.

`label``label``string``''` Accessible label for the progress circle. 
Used to provide context about what is loading or progressing.

`progress``progress``number``0` Progress value from 0 to 100. 
Only relevant when indeterminate is false.

`staticColor``static-color``ProgressCircleStaticColorS1 | undefined` Static color variant for use on different backgrounds. 
When set to 'white', the component uses white styling for images with a dark tinted background.

Name  Description `default slot` Accessible label for the progress circle. Used to provide context about what is loading or progressing.
