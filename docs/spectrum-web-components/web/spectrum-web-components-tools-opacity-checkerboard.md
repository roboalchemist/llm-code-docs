# Source: https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/

Title: Opacity Checkerboard: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/tools/opacity-checkerboard/

Markdown Content:
The `opacity-checkerboard` class provides a CSS utility that displays a checkerboard pattern background, commonly used to highlight transparent or semi-transparent areas in UI components. This visual indicator helps users distinguish between transparent and opaque regions, making it an essential tool for color pickers, image editors, and other components that work with opacity.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/opacity-checkerboard?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/opacity-checkerboard?style=for-the-badge)

yarn add @spectrum-web-components/opacity-checkerboard
Import the opacity checkerboard styles from:

import opacityCheckerBoardStyles from '@spectrum-web-components/opacity-checkerboard/src/opacity-checkerboard.css.js';
To integrate the opacity checkerboard styles into your component, add them to your component's styles array. The order of inclusion is important, as selectors within opacity checkerboard may have the same specificity as those within your component:

public static override get styles(): CSSResultArray {
    return [opacityCheckerBoardStyles, styles];
}
Apply the `opacity-checkerboard` class to any element that needs to display the checkerboard pattern:

<div class="opacity-checkerboard" style="inline-size: 100px; block-size: 100px;" aria-hidden="true"></div>
The opacity checkerboard works well as a background for elements with partial transparency:

<div class="opacity-checkerboard" style="inline-size: 200px; block-size: 200px; position: relative;" aria-hidden="true">
    <div style=" position: absolute; inset: 0; background-color: rgba(255, 0, 0, 0.5); " ></div>
</div>
When implementing the opacity checkerboard pattern, ensure proper accessibility by:

*   **Hiding from screen readers**: Use `aria-hidden="true"` on the checkerboard element since it's purely visual
*   **Providing semantic information**: Use separate text nodes or live regions to convey opacity information
*   **Using live regions**: Implement `aria-live` regions to announce opacity changes dynamically
*   **Descriptive context**: Provide meaningful descriptions of the actual color and opacity values, not the visual pattern

The opacity checkerboard is a purely visual indicator and should remain hidden from screen readers. Instead, provide semantic information through separate text nodes or live regions that update as opacity changes:

<div class="color-container">
    <div class="opacity-checkerboard" style="inline-size: 100px; block-size: 100px;" aria-hidden="true" ></div>
    <div class="visually-hidden" aria-live="polite" id="opacity-status">
        Current opacity: 75%
    </div>
</div>
For components that change opacity dynamically, use a live region to announce changes:

<div class="dynamic-opacity-example">
    <div class="opacity-checkerboard" style="inline-size: 100px; block-size: 100px; position: relative;" aria-hidden="true" >
        <div style=" position: absolute; inset: 0; background-color: rgba(255, 0, 0, 0.6); " ></div>
    </div>
    <div aria-live="assertive" class="visually-hidden">
        Opacity changed to 60%
    </div>
</div>
When the opacity checkerboard is part of an interactive component, ensure it doesn't interfere with keyboard navigation:

<button class="color-button" aria-label="Select red color with 50% opacity" aria-describedby="opacity-description">
    <span class="opacity-checkerboard" style="inline-size: 40px; block-size: 40px; display: block;" aria-hidden="true" ></span>
    <span id="opacity-description" class="visually-hidden">
        Red color with 50% transparency
    </span>
</button>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`9cb816b`]: 
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

*   **opacity-checkerboard:** bump CSS version (#5040) (e3bf6d3)

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

*   **opacity-checkerboard:** bump CSS version (#5040) (e3bf6d3)

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

*   update deps graph, fix imports (f633005)

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

*   **color-handle,color-loupe,swatch,thumbnail:** use the Opacity Checkerboard package (47e1fc4)
*   opacity checkerboard inclusion order (#3651) (4f417dc)

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

**Note:** Version bump only for package @spectrum-web-components/opacity-checkerboard

*   **opacity-checkerboard:** add component (#3416) (90202f9)
