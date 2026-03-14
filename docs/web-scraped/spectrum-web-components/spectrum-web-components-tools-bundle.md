# Source: https://opensource.adobe.com/spectrum-web-components/tools/bundle/

Title: Bundle: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/tools/bundle/

Markdown Content:
`@spectrum-web-components/bundle` is a master dependency that allows a project to import any and all of the Spectrum Web Components. While it is a great approach to prototyping, the fact that it versions all of the Spectrum Web Components packages collectively means that depending on it can leave you with a lot of package updates to manage at any one version change. For a more predictable upgrade process we suggest that you depend upon individual packages directly, but hope you find this bundle productive when initially trying to get into the act of developing with Spectrum Web Components.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/bundle?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/bundle?style=for-the-badge)

yarn add @spectrum-web-components/bundle
Import the side effectful registrations of the bundled components:

import '@spectrum-web-components/bundle/elements.js';
When looking to leverage their base classes as a type and/or for extension purposes, do so via something like the following for the `ActionButton` base class:

import { ActionButton } from '@spectrum-web-components/bundle';
The bundle consists of several key parts:

*   All Spectrum Web Component elements registrations
*   Base classes for all components available for type checking and extension
*   Namespaced icon exports for UI and workflow icons (e.g., `UIIcons`, `WorkflowIcons`)

Import all component registrations at once for rapid prototyping:

import '@spectrum-web-components/bundle/elements.js';
This registers all available Spectrum Web Components for use in your application.

Import individual component classes for type checking and extension purposes:

import { ActionButton, Button, Tooltip } from '@spectrum-web-components/bundle';
While this bundle directly re-exports the majority of functionality as they would be exported from their own packages, icon packages that export template literals are handled differently. Due to the large number of exports that they feature, each of these packages is namespaced when included in the bundle.

`@spectrum-web-components/icons-ui` is renamed to `UIIcons` when leveraging the bundle. This means that you can use UI icons in your code by importing them from `@spectrum-web-components/bundle/icons.js`:

import { UIIcons } from '@spectrum-web-components/bundle/icons.js';

console.log(UIIcons.AsteriskIcon());

`@spectrum-web-components/icons-workflow` is namespaced to `WorkflowIcons` when leveraging the bundle. This means that you can use workflow icons in your code by importing them from `@spectrum-web-components/bundle/icons.js`:

import { WorkflowIcons } from '@spectrum-web-components/bundle/icons.js';

console.log(WorkflowIcons.CircleIcon());

The bundle versions all Spectrum Web Components packages collectively. This means:

*   A single version bump updates all components simultaneously
*   You may receive updates for components you're not actively using
*   For production applications, consider depending on individual packages for more granular control

All components included in the bundle follow WCAG accessibility guidelines. Each component maintains its own accessibility features as documented in their individual package documentation. Refer to the specific component documentation pages for detailed accessibility information.

*   Updated dependencies [`6f5419a`, `3783d87`]: 
    *   @spectrum-web-components/alert-banner@1.11.2
    *   @spectrum-web-components/picker@1.11.2
    *   @spectrum-web-components/asset@1.11.2
    *   @spectrum-web-components/badge@1.11.2
    *   @spectrum-web-components/divider@1.11.2
    *   @spectrum-web-components/progress-circle@1.11.2
    *   @spectrum-web-components/status-light@1.11.2
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/theme@1.11.2
    *   @spectrum-web-components/action-menu@1.11.2
    *   @spectrum-web-components/card@1.11.2
    *   @spectrum-web-components/coachmark@1.11.2
    *   @spectrum-web-components/dialog@1.11.2
    *   @spectrum-web-components/menu@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/combobox@1.11.2
    *   @spectrum-web-components/reactive-controllers@1.11.2
    *   @spectrum-web-components/accordion@1.11.2
    *   @spectrum-web-components/action-bar@1.11.2
    *   @spectrum-web-components/action-button@1.11.2
    *   @spectrum-web-components/action-group@1.11.2
    *   @spectrum-web-components/avatar@1.11.2
    *   @spectrum-web-components/breadcrumbs@1.11.2
    *   @spectrum-web-components/button-group@1.11.2
    *   @spectrum-web-components/checkbox@1.11.2
    *   @spectrum-web-components/clear-button@1.11.2
    *   @spectrum-web-components/close-button@1.11.2
    *   @spectrum-web-components/color-area@1.11.2
    *   @spectrum-web-components/color-field@1.11.2
    *   @spectrum-web-components/color-handle@1.11.2
    *   @spectrum-web-components/color-loupe@1.11.2
    *   @spectrum-web-components/color-slider@1.11.2
    *   @spectrum-web-components/color-wheel@1.11.2
    *   @spectrum-web-components/contextual-help@1.11.2
    *   @spectrum-web-components/dropzone@1.11.2
    *   @spectrum-web-components/field-group@1.11.2
    *   @spectrum-web-components/field-label@1.11.2
    *   @spectrum-web-components/help-text@1.11.2
    *   @spectrum-web-components/icon@1.11.2
    *   @spectrum-web-components/icons@1.11.2
    *   @spectrum-web-components/icons-ui@1.11.2
    *   @spectrum-web-components/icons-workflow@1.11.2
    *   @spectrum-web-components/iconset@1.11.2
    *   @spectrum-web-components/illustrated-message@1.11.2
    *   @spectrum-web-components/infield-button@1.11.2
    *   @spectrum-web-components/link@1.11.2
    *   @spectrum-web-components/meter@1.11.2
    *   @spectrum-web-components/modal@1.11.2
    *   @spectrum-web-components/number-field@1.11.2
    *   @spectrum-web-components/overlay@1.11.2
    *   @spectrum-web-components/picker-button@1.11.2
    *   @spectrum-web-components/popover@1.11.2
    *   @spectrum-web-components/progress-bar@1.11.2
    *   @spectrum-web-components/radio@1.11.2
    *   @spectrum-web-components/search@1.11.2
    *   @spectrum-web-components/sidenav@1.11.2
    *   @spectrum-web-components/slider@1.11.2
    *   @spectrum-web-components/split-view@1.11.2
    *   @spectrum-web-components/swatch@1.11.2
    *   @spectrum-web-components/switch@1.11.2
    *   @spectrum-web-components/table@1.11.2
    *   @spectrum-web-components/tabs@1.11.2
    *   @spectrum-web-components/tags@1.11.2
    *   @spectrum-web-components/textfield@1.11.2
    *   @spectrum-web-components/thumbnail@1.11.2
    *   @spectrum-web-components/toast@1.11.2
    *   @spectrum-web-components/tooltip@1.11.2
    *   @spectrum-web-components/top-nav@1.11.2
    *   @spectrum-web-components/tray@1.11.2
    *   @spectrum-web-components/underlay@1.11.2
    *   @spectrum-web-components/grid@1.11.2
    *   @spectrum-web-components/styles@1.11.2
    *   @spectrum-web-components/truncated@1.11.2

*   Updated dependencies [`95e1c25`, `cdf6a24`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/table@1.11.1
    *   @spectrum-web-components/alert-banner@1.11.1
    *   @spectrum-web-components/asset@1.11.1
    *   @spectrum-web-components/badge@1.11.1
    *   @spectrum-web-components/divider@1.11.1
    *   @spectrum-web-components/progress-circle@1.11.1
    *   @spectrum-web-components/status-light@1.11.1
    *   @spectrum-web-components/theme@1.11.1
    *   @spectrum-web-components/accordion@1.11.1
    *   @spectrum-web-components/action-bar@1.11.1
    *   @spectrum-web-components/action-button@1.11.1
    *   @spectrum-web-components/action-menu@1.11.1
    *   @spectrum-web-components/avatar@1.11.1
    *   @spectrum-web-components/breadcrumbs@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/card@1.11.1
    *   @spectrum-web-components/checkbox@1.11.1
    *   @spectrum-web-components/coachmark@1.11.1
    *   @spectrum-web-components/color-area@1.11.1
    *   @spectrum-web-components/color-slider@1.11.1
    *   @spectrum-web-components/color-wheel@1.11.1
    *   @spectrum-web-components/dialog@1.11.1
    *   @spectrum-web-components/field-label@1.11.1
    *   @spectrum-web-components/help-text@1.11.1
    *   @spectrum-web-components/link@1.11.1
    *   @spectrum-web-components/menu@1.11.1
    *   @spectrum-web-components/meter@1.11.1
    *   @spectrum-web-components/number-field@1.11.1
    *   @spectrum-web-components/overlay@1.11.1
    *   @spectrum-web-components/picker@1.11.1
    *   @spectrum-web-components/picker-button@1.11.1
    *   @spectrum-web-components/progress-bar@1.11.1
    *   @spectrum-web-components/radio@1.11.1
    *   @spectrum-web-components/sidenav@1.11.1
    *   @spectrum-web-components/slider@1.11.1
    *   @spectrum-web-components/split-view@1.11.1
    *   @spectrum-web-components/swatch@1.11.1
    *   @spectrum-web-components/tabs@1.11.1
    *   @spectrum-web-components/tags@1.11.1
    *   @spectrum-web-components/textfield@1.11.1
    *   @spectrum-web-components/toast@1.11.1
    *   @spectrum-web-components/tooltip@1.11.1
    *   @spectrum-web-components/top-nav@1.11.1
    *   @spectrum-web-components/tray@1.11.1
    *   @spectrum-web-components/action-group@1.11.1
    *   @spectrum-web-components/button-group@1.11.1
    *   @spectrum-web-components/clear-button@1.11.1
    *   @spectrum-web-components/close-button@1.11.1
    *   @spectrum-web-components/color-field@1.11.1
    *   @spectrum-web-components/color-handle@1.11.1
    *   @spectrum-web-components/color-loupe@1.11.1
    *   @spectrum-web-components/combobox@1.11.1
    *   @spectrum-web-components/contextual-help@1.11.1
    *   @spectrum-web-components/dropzone@1.11.1
    *   @spectrum-web-components/field-group@1.11.1
    *   @spectrum-web-components/icon@1.11.1
    *   @spectrum-web-components/icons@1.11.1
    *   @spectrum-web-components/icons-ui@1.11.1
    *   @spectrum-web-components/icons-workflow@1.11.1
    *   @spectrum-web-components/iconset@1.11.1
    *   @spectrum-web-components/illustrated-message@1.11.1
    *   @spectrum-web-components/infield-button@1.11.1
    *   @spectrum-web-components/modal@1.11.1
    *   @spectrum-web-components/popover@1.11.1
    *   @spectrum-web-components/search@1.11.1
    *   @spectrum-web-components/switch@1.11.1
    *   @spectrum-web-components/thumbnail@1.11.1
    *   @spectrum-web-components/underlay@1.11.1
    *   @spectrum-web-components/grid@1.11.1
    *   @spectrum-web-components/styles@1.11.1
    *   @spectrum-web-components/truncated@1.11.1
    *   @spectrum-web-components/reactive-controllers@1.11.1

*   Updated dependencies [`0c43e2e`, `7af5e8f`, `ae61361`, `eac97a2`, `b95e254`, `02b2d7d`, `b95e254`, `6b887f2`, `283f0fe`, `f07344f`, `2732aad`, `1d76b70`, `f8bdeec`, `b95e254`, `cadc39e`, `50ad026`, `e780f82`, `b95e254`, `4cb0b7b`, `9cb816b`, `e66cdb2`, `7c26e3a`]: 
    *   @spectrum-web-components/avatar@1.11.0
    *   @spectrum-web-components/field-label@1.11.0
    *   @spectrum-web-components/help-text@1.11.0
    *   @spectrum-web-components/picker@1.11.0
    *   @spectrum-web-components/menu@1.11.0
    *   @spectrum-web-components/reactive-controllers@1.11.0
    *   @spectrum-web-components/overlay@1.11.0
    *   @spectrum-web-components/tray@1.11.0
    *   @spectrum-web-components/action-menu@1.11.0
    *   @spectrum-web-components/breadcrumbs@1.11.0
    *   @spectrum-web-components/action-bar@1.11.0
    *   @spectrum-web-components/coachmark@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/close-button@1.11.0
    *   @spectrum-web-components/tooltip@1.11.0
    *   @spectrum-web-components/slider@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/contextual-help@1.11.0
    *   @spectrum-web-components/styles@1.11.0
    *   @spectrum-web-components/meter@1.11.0
    *   @spectrum-web-components/progress-bar@1.11.0
    *   @spectrum-web-components/field-group@1.11.0
    *   @spectrum-web-components/radio@1.11.0
    *   @spectrum-web-components/textfield@1.11.0
    *   @spectrum-web-components/combobox@1.11.0
    *   @spectrum-web-components/accordion@1.11.0
    *   @spectrum-web-components/action-group@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/color-area@1.11.0
    *   @spectrum-web-components/color-slider@1.11.0
    *   @spectrum-web-components/color-wheel@1.11.0
    *   @spectrum-web-components/icon@1.11.0
    *   @spectrum-web-components/number-field@1.11.0
    *   @spectrum-web-components/sidenav@1.11.0
    *   @spectrum-web-components/swatch@1.11.0
    *   @spectrum-web-components/tabs@1.11.0
    *   @spectrum-web-components/tags@1.11.0
    *   @spectrum-web-components/grid@1.11.0
    *   @spectrum-web-components/popover@1.11.0
    *   @spectrum-web-components/truncated@1.11.0
    *   @spectrum-web-components/alert-banner@1.11.0
    *   @spectrum-web-components/asset@1.11.0
    *   @spectrum-web-components/badge@1.11.0
    *   @spectrum-web-components/divider@1.11.0
    *   @spectrum-web-components/progress-circle@1.11.0
    *   @spectrum-web-components/status-light@1.11.0
    *   @spectrum-web-components/theme@1.11.0
    *   @spectrum-web-components/action-button@1.11.0
    *   @spectrum-web-components/card@1.11.0
    *   @spectrum-web-components/checkbox@1.11.0
    *   @spectrum-web-components/dialog@1.11.0
    *   @spectrum-web-components/link@1.11.0
    *   @spectrum-web-components/picker-button@1.11.0
    *   @spectrum-web-components/split-view@1.11.0
    *   @spectrum-web-components/toast@1.11.0
    *   @spectrum-web-components/top-nav@1.11.0
    *   @spectrum-web-components/button-group@1.11.0
    *   @spectrum-web-components/clear-button@1.11.0
    *   @spectrum-web-components/color-field@1.11.0
    *   @spectrum-web-components/color-handle@1.11.0
    *   @spectrum-web-components/color-loupe@1.11.0
    *   @spectrum-web-components/dropzone@1.11.0
    *   @spectrum-web-components/icons@1.11.0
    *   @spectrum-web-components/icons-ui@1.11.0
    *   @spectrum-web-components/icons-workflow@1.11.0
    *   @spectrum-web-components/iconset@1.11.0
    *   @spectrum-web-components/illustrated-message@1.11.0
    *   @spectrum-web-components/infield-button@1.11.0
    *   @spectrum-web-components/modal@1.11.0
    *   @spectrum-web-components/search@1.11.0
    *   @spectrum-web-components/switch@1.11.0
    *   @spectrum-web-components/table@1.11.0
    *   @spectrum-web-components/thumbnail@1.11.0
    *   @spectrum-web-components/underlay@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/accordion@1.10.0
    *   @spectrum-web-components/action-bar@1.10.0
    *   @spectrum-web-components/action-button@1.10.0
    *   @spectrum-web-components/action-group@1.10.0
    *   @spectrum-web-components/action-menu@1.10.0
    *   @spectrum-web-components/alert-banner@1.10.0
    *   @spectrum-web-components/asset@1.10.0
    *   @spectrum-web-components/avatar@1.10.0
    *   @spectrum-web-components/badge@1.10.0
    *   @spectrum-web-components/breadcrumbs@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/button-group@1.10.0
    *   @spectrum-web-components/card@1.10.0
    *   @spectrum-web-components/checkbox@1.10.0
    *   @spectrum-web-components/clear-button@1.10.0
    *   @spectrum-web-components/close-button@1.10.0
    *   @spectrum-web-components/coachmark@1.10.0
    *   @spectrum-web-components/color-area@1.10.0
    *   @spectrum-web-components/color-field@1.10.0
    *   @spectrum-web-components/color-handle@1.10.0
    *   @spectrum-web-components/color-loupe@1.10.0
    *   @spectrum-web-components/color-slider@1.10.0
    *   @spectrum-web-components/color-wheel@1.10.0
    *   @spectrum-web-components/combobox@1.10.0
    *   @spectrum-web-components/contextual-help@1.10.0
    *   @spectrum-web-components/dialog@1.10.0
    *   @spectrum-web-components/divider@1.10.0
    *   @spectrum-web-components/dropzone@1.10.0
    *   @spectrum-web-components/field-group@1.10.0
    *   @spectrum-web-components/field-label@1.10.0
    *   @spectrum-web-components/help-text@1.10.0
    *   @spectrum-web-components/icon@1.10.0
    *   @spectrum-web-components/icons@1.10.0
    *   @spectrum-web-components/icons-ui@1.10.0
    *   @spectrum-web-components/icons-workflow@1.10.0
    *   @spectrum-web-components/iconset@1.10.0
    *   @spectrum-web-components/illustrated-message@1.10.0
    *   @spectrum-web-components/infield-button@1.10.0
    *   @spectrum-web-components/link@1.10.0
    *   @spectrum-web-components/menu@1.10.0
    *   @spectrum-web-components/meter@1.10.0
    *   @spectrum-web-components/modal@1.10.0
    *   @spectrum-web-components/number-field@1.10.0
    *   @spectrum-web-components/overlay@1.10.0
    *   @spectrum-web-components/picker@1.10.0
    *   @spectrum-web-components/picker-button@1.10.0
    *   @spectrum-web-components/popover@1.10.0
    *   @spectrum-web-components/progress-bar@1.10.0
    *   @spectrum-web-components/progress-circle@1.10.0
    *   @spectrum-web-components/radio@1.10.0
    *   @spectrum-web-components/search@1.10.0
    *   @spectrum-web-components/sidenav@1.10.0
    *   @spectrum-web-components/slider@1.10.0
    *   @spectrum-web-components/split-view@1.10.0
    *   @spectrum-web-components/status-light@1.10.0
    *   @spectrum-web-components/swatch@1.10.0
    *   @spectrum-web-components/switch@1.10.0
    *   @spectrum-web-components/table@1.10.0
    *   @spectrum-web-components/tabs@1.10.0
    *   @spectrum-web-components/tags@1.10.0
    *   @spectrum-web-components/textfield@1.10.0
    *   @spectrum-web-components/thumbnail@1.10.0
    *   @spectrum-web-components/toast@1.10.0
    *   @spectrum-web-components/tooltip@1.10.0
    *   @spectrum-web-components/top-nav@1.10.0
    *   @spectrum-web-components/tray@1.10.0
    *   @spectrum-web-components/underlay@1.10.0
    *   @spectrum-web-components/grid@1.10.0
    *   @spectrum-web-components/shared@1.10.0
    *   @spectrum-web-components/styles@1.10.0
    *   @spectrum-web-components/theme@1.10.0
    *   @spectrum-web-components/truncated@1.10.0
    *   @spectrum-web-components/reactive-controllers@1.10.0

*   Updated dependencies [`2811b9e`, `a19cbe3`]: 
    *   @spectrum-web-components/status-light@1.9.1
    *   @spectrum-web-components/overlay@1.9.1
    *   @spectrum-web-components/combobox@1.9.1
    *   @spectrum-web-components/contextual-help@1.9.1
    *   @spectrum-web-components/menu@1.9.1
    *   @spectrum-web-components/picker@1.9.1
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/tooltip@1.9.1
    *   @spectrum-web-components/truncated@1.9.1
    *   @spectrum-web-components/breadcrumbs@1.9.1
    *   @spectrum-web-components/action-menu@1.9.1
    *   @spectrum-web-components/action-bar@1.9.1
    *   @spectrum-web-components/card@1.9.1
    *   @spectrum-web-components/accordion@1.9.1
    *   @spectrum-web-components/action-button@1.9.1
    *   @spectrum-web-components/action-group@1.9.1
    *   @spectrum-web-components/alert-banner@1.9.1
    *   @spectrum-web-components/asset@1.9.1
    *   @spectrum-web-components/avatar@1.9.1
    *   @spectrum-web-components/badge@1.9.1
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/button-group@1.9.1
    *   @spectrum-web-components/checkbox@1.9.1
    *   @spectrum-web-components/clear-button@1.9.1
    *   @spectrum-web-components/close-button@1.9.1
    *   @spectrum-web-components/coachmark@1.9.1
    *   @spectrum-web-components/color-area@1.9.1
    *   @spectrum-web-components/color-field@1.9.1
    *   @spectrum-web-components/color-handle@1.9.1
    *   @spectrum-web-components/color-loupe@1.9.1
    *   @spectrum-web-components/color-slider@1.9.1
    *   @spectrum-web-components/color-wheel@1.9.1
    *   @spectrum-web-components/dialog@1.9.1
    *   @spectrum-web-components/divider@1.9.1
    *   @spectrum-web-components/dropzone@1.9.1
    *   @spectrum-web-components/field-group@1.9.1
    *   @spectrum-web-components/field-label@1.9.1
    *   @spectrum-web-components/help-text@1.9.1
    *   @spectrum-web-components/icon@1.9.1
    *   @spectrum-web-components/icons@1.9.1
    *   @spectrum-web-components/icons-ui@1.9.1
    *   @spectrum-web-components/icons-workflow@1.9.1
    *   @spectrum-web-components/iconset@1.9.1
    *   @spectrum-web-components/illustrated-message@1.9.1
    *   @spectrum-web-components/infield-button@1.9.1
    *   @spectrum-web-components/link@1.9.1
    *   @spectrum-web-components/meter@1.9.1
    *   @spectrum-web-components/modal@1.9.1
    *   @spectrum-web-components/number-field@1.9.1
    *   @spectrum-web-components/picker-button@1.9.1
    *   @spectrum-web-components/progress-bar@1.9.1
    *   @spectrum-web-components/progress-circle@1.9.1
    *   @spectrum-web-components/radio@1.9.1
    *   @spectrum-web-components/search@1.9.1
    *   @spectrum-web-components/sidenav@1.9.1
    *   @spectrum-web-components/slider@1.9.1
    *   @spectrum-web-components/split-view@1.9.1
    *   @spectrum-web-components/swatch@1.9.1
    *   @spectrum-web-components/switch@1.9.1
    *   @spectrum-web-components/table@1.9.1
    *   @spectrum-web-components/tabs@1.9.1
    *   @spectrum-web-components/tags@1.9.1
    *   @spectrum-web-components/textfield@1.9.1
    *   @spectrum-web-components/thumbnail@1.9.1
    *   @spectrum-web-components/toast@1.9.1
    *   @spectrum-web-components/top-nav@1.9.1
    *   @spectrum-web-components/tray@1.9.1
    *   @spectrum-web-components/underlay@1.9.1
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/grid@1.9.1
    *   @spectrum-web-components/reactive-controllers@1.9.1
    *   @spectrum-web-components/shared@1.9.1
    *   @spectrum-web-components/styles@1.9.1
    *   @spectrum-web-components/theme@1.9.1

*   Updated dependencies [`7d23140`, `7d23140`, `4880da4`, `bdf54c1`, `dbba861`, `72d807c`, `14ebeb9`, `7d23140`, `7d23140`, `7d23140`, `72d807c`, `72d807c`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/combobox@1.9.0
    *   @spectrum-web-components/menu@1.9.0
    *   @spectrum-web-components/icons-workflow@1.9.0
    *   @spectrum-web-components/picker@1.9.0
    *   @spectrum-web-components/textfield@1.9.0
    *   @spectrum-web-components/progress-circle@1.9.0
    *   @spectrum-web-components/reactive-controllers@1.9.0
    *   @spectrum-web-components/help-text@1.9.0
    *   @spectrum-web-components/field-label@1.9.0
    *   @spectrum-web-components/action-bar@1.9.0
    *   @spectrum-web-components/action-button@1.9.0
    *   @spectrum-web-components/alert-banner@1.9.0
    *   @spectrum-web-components/button-group@1.9.0
    *   @spectrum-web-components/coachmark@1.9.0
    *   @spectrum-web-components/dialog@1.9.0
    *   @spectrum-web-components/infield-button@1.9.0
    *   @spectrum-web-components/picker-button@1.9.0
    *   @spectrum-web-components/search@1.9.0
    *   @spectrum-web-components/tags@1.9.0
    *   @spectrum-web-components/toast@1.9.0
    *   @spectrum-web-components/breadcrumbs@1.9.0
    *   @spectrum-web-components/action-group@1.9.0
    *   @spectrum-web-components/action-menu@1.9.0
    *   @spectrum-web-components/card@1.9.0
    *   @spectrum-web-components/contextual-help@1.9.0
    *   @spectrum-web-components/color-field@1.9.0
    *   @spectrum-web-components/number-field@1.9.0
    *   @spectrum-web-components/accordion@1.9.0
    *   @spectrum-web-components/color-area@1.9.0
    *   @spectrum-web-components/color-slider@1.9.0
    *   @spectrum-web-components/color-wheel@1.9.0
    *   @spectrum-web-components/icon@1.9.0
    *   @spectrum-web-components/meter@1.9.0
    *   @spectrum-web-components/overlay@1.9.0
    *   @spectrum-web-components/progress-bar@1.9.0
    *   @spectrum-web-components/radio@1.9.0
    *   @spectrum-web-components/sidenav@1.9.0
    *   @spectrum-web-components/slider@1.9.0
    *   @spectrum-web-components/swatch@1.9.0
    *   @spectrum-web-components/tabs@1.9.0
    *   @spectrum-web-components/tooltip@1.9.0
    *   @spectrum-web-components/tray@1.9.0
    *   @spectrum-web-components/grid@1.9.0
    *   @spectrum-web-components/field-group@1.9.0
    *   @spectrum-web-components/checkbox@1.9.0
    *   @spectrum-web-components/icons-ui@1.9.0
    *   @spectrum-web-components/table@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/truncated@1.9.0
    *   @spectrum-web-components/top-nav@1.9.0
    *   @spectrum-web-components/switch@1.9.0
    *   @spectrum-web-components/asset@1.9.0
    *   @spectrum-web-components/avatar@1.9.0
    *   @spectrum-web-components/badge@1.9.0
    *   @spectrum-web-components/clear-button@1.9.0
    *   @spectrum-web-components/close-button@1.9.0
    *   @spectrum-web-components/color-handle@1.9.0
    *   @spectrum-web-components/color-loupe@1.9.0
    *   @spectrum-web-components/divider@1.9.0
    *   @spectrum-web-components/dropzone@1.9.0
    *   @spectrum-web-components/icons@1.9.0
    *   @spectrum-web-components/iconset@1.9.0
    *   @spectrum-web-components/illustrated-message@1.9.0
    *   @spectrum-web-components/link@1.9.0
    *   @spectrum-web-components/modal@1.9.0
    *   @spectrum-web-components/split-view@1.9.0
    *   @spectrum-web-components/status-light@1.9.0
    *   @spectrum-web-components/thumbnail@1.9.0
    *   @spectrum-web-components/underlay@1.9.0
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0
    *   @spectrum-web-components/styles@1.9.0
    *   @spectrum-web-components/theme@1.9.0

*   Updated dependencies [`a292dc7`, `cc6e91e`, `77bdef6`, `c3d5558`, `6c2acaf`, `14486d6`, `f27ab09`, `ee1bae6`, `dcd2cd3`, `15be17d`, `f8da034`, `99ab45e`, `b0570bc`, `aa411d0`, `d5f2909`, `14486d6`, `eae4332`, `826a2d5`]: 
    *   @spectrum-web-components/progress-bar@1.8.0
    *   @spectrum-web-components/combobox@1.8.0
    *   @spectrum-web-components/styles@1.8.0
    *   @spectrum-web-components/color-wheel@1.8.0
    *   @spectrum-web-components/picker@1.8.0
    *   @spectrum-web-components/overlay@1.8.0
    *   @spectrum-web-components/menu@1.8.0
    *   @spectrum-web-components/switch@1.8.0
    *   @spectrum-web-components/clear-button@1.8.0
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/card@1.8.0
    *   @spectrum-web-components/contextual-help@1.8.0
    *   @spectrum-web-components/slider@1.8.0
    *   @spectrum-web-components/link@1.8.0
    *   @spectrum-web-components/grid@1.8.0
    *   @spectrum-web-components/divider@1.8.0
    *   @spectrum-web-components/illustrated-message@1.8.0
    *   @spectrum-web-components/theme@1.8.0
    *   @spectrum-web-components/truncated@1.8.0
    *   @spectrum-web-components/action-menu@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/tooltip@1.8.0
    *   @spectrum-web-components/breadcrumbs@1.8.0
    *   @spectrum-web-components/action-bar@1.8.0
    *   @spectrum-web-components/action-button@1.8.0
    *   @spectrum-web-components/alert-banner@1.8.0
    *   @spectrum-web-components/button-group@1.8.0
    *   @spectrum-web-components/coachmark@1.8.0
    *   @spectrum-web-components/dialog@1.8.0
    *   @spectrum-web-components/infield-button@1.8.0
    *   @spectrum-web-components/picker-button@1.8.0
    *   @spectrum-web-components/search@1.8.0
    *   @spectrum-web-components/tags@1.8.0
    *   @spectrum-web-components/toast@1.8.0
    *   @spectrum-web-components/action-group@1.8.0
    *   @spectrum-web-components/tabs@1.8.0
    *   @spectrum-web-components/number-field@1.8.0
    *   @spectrum-web-components/top-nav@1.8.0
    *   @spectrum-web-components/accordion@1.8.0
    *   @spectrum-web-components/asset@1.8.0
    *   @spectrum-web-components/avatar@1.8.0
    *   @spectrum-web-components/badge@1.8.0
    *   @spectrum-web-components/checkbox@1.8.0
    *   @spectrum-web-components/close-button@1.8.0
    *   @spectrum-web-components/color-area@1.8.0
    *   @spectrum-web-components/color-field@1.8.0
    *   @spectrum-web-components/color-handle@1.8.0
    *   @spectrum-web-components/color-loupe@1.8.0
    *   @spectrum-web-components/color-slider@1.8.0
    *   @spectrum-web-components/dropzone@1.8.0
    *   @spectrum-web-components/field-group@1.8.0
    *   @spectrum-web-components/field-label@1.8.0
    *   @spectrum-web-components/help-text@1.8.0
    *   @spectrum-web-components/icon@1.8.0
    *   @spectrum-web-components/icons@1.8.0
    *   @spectrum-web-components/icons-ui@1.8.0
    *   @spectrum-web-components/icons-workflow@1.8.0
    *   @spectrum-web-components/iconset@1.8.0
    *   @spectrum-web-components/meter@1.8.0
    *   @spectrum-web-components/modal@1.8.0
    *   @spectrum-web-components/progress-circle@1.8.0
    *   @spectrum-web-components/radio@1.8.0
    *   @spectrum-web-components/sidenav@1.8.0
    *   @spectrum-web-components/split-view@1.8.0
    *   @spectrum-web-components/status-light@1.8.0
    *   @spectrum-web-components/swatch@1.8.0
    *   @spectrum-web-components/table@1.8.0
    *   @spectrum-web-components/textfield@1.8.0
    *   @spectrum-web-components/thumbnail@1.8.0
    *   @spectrum-web-components/tray@1.8.0
    *   @spectrum-web-components/underlay@1.8.0
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/reactive-controllers@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   Updated dependencies [`1126cf2`, `ae9dcf8`, `3aeafdd`, `a646ae8`, `56f2ff4`, `c1669d2`, `8da375b`, `94dd388`, `cde976d`]: 
    *   @spectrum-web-components/styles@1.7.0
    *   @spectrum-web-components/card@1.7.0
    *   @spectrum-web-components/menu@1.7.0
    *   @spectrum-web-components/overlay@1.7.0
    *   @spectrum-web-components/action-button@1.7.0
    *   @spectrum-web-components/tabs@1.7.0
    *   @spectrum-web-components/split-view@1.7.0
    *   @spectrum-web-components/textfield@1.7.0
    *   @spectrum-web-components/sidenav@1.7.0
    *   @spectrum-web-components/tooltip@1.7.0
    *   @spectrum-web-components/illustrated-message@1.7.0
    *   @spectrum-web-components/theme@1.7.0
    *   @spectrum-web-components/truncated@1.7.0
    *   @spectrum-web-components/breadcrumbs@1.7.0
    *   @spectrum-web-components/combobox@1.7.0
    *   @spectrum-web-components/picker@1.7.0
    *   @spectrum-web-components/contextual-help@1.7.0
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/action-group@1.7.0
    *   @spectrum-web-components/action-menu@1.7.0
    *   @spectrum-web-components/top-nav@1.7.0
    *   @spectrum-web-components/color-field@1.7.0
    *   @spectrum-web-components/number-field@1.7.0
    *   @spectrum-web-components/search@1.7.0
    *   @spectrum-web-components/slider@1.7.0
    *   @spectrum-web-components/action-bar@1.7.0
    *   @spectrum-web-components/accordion@1.7.0
    *   @spectrum-web-components/alert-banner@1.7.0
    *   @spectrum-web-components/asset@1.7.0
    *   @spectrum-web-components/avatar@1.7.0
    *   @spectrum-web-components/badge@1.7.0
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/button-group@1.7.0
    *   @spectrum-web-components/checkbox@1.7.0
    *   @spectrum-web-components/clear-button@1.7.0
    *   @spectrum-web-components/close-button@1.7.0
    *   @spectrum-web-components/coachmark@1.7.0
    *   @spectrum-web-components/color-area@1.7.0
    *   @spectrum-web-components/color-handle@1.7.0
    *   @spectrum-web-components/color-loupe@1.7.0
    *   @spectrum-web-components/color-slider@1.7.0
    *   @spectrum-web-components/color-wheel@1.7.0
    *   @spectrum-web-components/dialog@1.7.0
    *   @spectrum-web-components/divider@1.7.0
    *   @spectrum-web-components/dropzone@1.7.0
    *   @spectrum-web-components/field-group@1.7.0
    *   @spectrum-web-components/field-label@1.7.0
    *   @spectrum-web-components/help-text@1.7.0
    *   @spectrum-web-components/icon@1.7.0
    *   @spectrum-web-components/icons@1.7.0
    *   @spectrum-web-components/icons-ui@1.7.0
    *   @spectrum-web-components/icons-workflow@1.7.0
    *   @spectrum-web-components/iconset@1.7.0
    *   @spectrum-web-components/infield-button@1.7.0
    *   @spectrum-web-components/link@1.7.0
    *   @spectrum-web-components/meter@1.7.0
    *   @spectrum-web-components/modal@1.7.0
    *   @spectrum-web-components/picker-button@1.7.0
    *   @spectrum-web-components/progress-bar@1.7.0
    *   @spectrum-web-components/progress-circle@1.7.0
    *   @spectrum-web-components/radio@1.7.0
    *   @spectrum-web-components/status-light@1.7.0
    *   @spectrum-web-components/swatch@1.7.0
    *   @spectrum-web-components/switch@1.7.0
    *   @spectrum-web-components/table@1.7.0
    *   @spectrum-web-components/tags@1.7.0
    *   @spectrum-web-components/thumbnail@1.7.0
    *   @spectrum-web-components/toast@1.7.0
    *   @spectrum-web-components/tray@1.7.0
    *   @spectrum-web-components/underlay@1.7.0
    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/grid@1.7.0
    *   @spectrum-web-components/reactive-controllers@1.7.0
    *   @spectrum-web-components/shared@1.7.0

*   Updated dependencies [`02af616`, `03a4439`, `f6cebbd`, `3c3bc2b`, `00eb0a8`, `74386e8`, `700489f`, `9e15a66`, `a9727d2`, `53f3769`]: 
    *   @spectrum-web-components/slider@1.6.0
    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/icons-workflow@1.6.0
    *   @spectrum-web-components/picker@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/number-field@1.6.0
    *   @spectrum-web-components/tooltip@1.6.0
    *   @spectrum-web-components/infield-button@1.6.0
    *   @spectrum-web-components/textfield@1.6.0
    *   @spectrum-web-components/search@1.6.0
    *   @spectrum-web-components/styles@1.6.0
    *   @spectrum-web-components/close-button@1.6.0
    *   @spectrum-web-components/dropzone@1.6.0
    *   @spectrum-web-components/illustrated-message@1.6.0
    *   @spectrum-web-components/menu@1.6.0
    *   @spectrum-web-components/status-light@1.6.0
    *   @spectrum-web-components/switch@1.6.0
    *   @spectrum-web-components/table@1.6.0
    *   @spectrum-web-components/tabs@1.6.0
    *   @spectrum-web-components/toast@1.6.0
    *   @spectrum-web-components/overlay@1.6.0
    *   @spectrum-web-components/action-bar@1.6.0
    *   @spectrum-web-components/combobox@1.6.0
    *   @spectrum-web-components/contextual-help@1.6.0
    *   @spectrum-web-components/action-group@1.6.0
    *   @spectrum-web-components/action-menu@1.6.0
    *   @spectrum-web-components/alert-banner@1.6.0
    *   @spectrum-web-components/breadcrumbs@1.6.0
    *   @spectrum-web-components/card@1.6.0
    *   @spectrum-web-components/dialog@1.6.0
    *   @spectrum-web-components/help-text@1.6.0
    *   @spectrum-web-components/action-button@1.6.0
    *   @spectrum-web-components/button-group@1.6.0
    *   @spectrum-web-components/coachmark@1.6.0
    *   @spectrum-web-components/picker-button@1.6.0
    *   @spectrum-web-components/tags@1.6.0
    *   @spectrum-web-components/truncated@1.6.0
    *   @spectrum-web-components/color-field@1.6.0
    *   @spectrum-web-components/theme@1.6.0
    *   @spectrum-web-components/top-nav@1.6.0
    *   @spectrum-web-components/field-group@1.6.0
    *   @spectrum-web-components/radio@1.6.0
    *   @spectrum-web-components/accordion@1.6.0
    *   @spectrum-web-components/asset@1.6.0
    *   @spectrum-web-components/avatar@1.6.0
    *   @spectrum-web-components/badge@1.6.0
    *   @spectrum-web-components/checkbox@1.6.0
    *   @spectrum-web-components/clear-button@1.6.0
    *   @spectrum-web-components/color-area@1.6.0
    *   @spectrum-web-components/color-handle@1.6.0
    *   @spectrum-web-components/color-loupe@1.6.0
    *   @spectrum-web-components/color-slider@1.6.0
    *   @spectrum-web-components/color-wheel@1.6.0
    *   @spectrum-web-components/divider@1.6.0
    *   @spectrum-web-components/field-label@1.6.0
    *   @spectrum-web-components/icon@1.6.0
    *   @spectrum-web-components/icons@1.6.0
    *   @spectrum-web-components/icons-ui@1.6.0
    *   @spectrum-web-components/iconset@1.6.0
    *   @spectrum-web-components/link@1.6.0
    *   @spectrum-web-components/meter@1.6.0
    *   @spectrum-web-components/modal@1.6.0
    *   @spectrum-web-components/progress-bar@1.6.0
    *   @spectrum-web-components/progress-circle@1.6.0
    *   @spectrum-web-components/sidenav@1.6.0
    *   @spectrum-web-components/split-view@1.6.0
    *   @spectrum-web-components/swatch@1.6.0
    *   @spectrum-web-components/thumbnail@1.6.0
    *   @spectrum-web-components/tray@1.6.0
    *   @spectrum-web-components/underlay@1.6.0
    *   @spectrum-web-components/base@1.6.0
    *   @spectrum-web-components/grid@1.6.0
    *   @spectrum-web-components/reactive-controllers@1.6.0
    *   @spectrum-web-components/shared@1.6.0

*   Updated dependencies [`86bcd12`, `165a904`, `a4de4c7`, `4e06533`, `fa4be70`, `daeb11f`, `8f8735c`, `e19e55f`, `6c58f50`, `fa4be70`, `4c2f908`, `a69accb`, `c7efe31`, `5a3bc6d`]: 
    *   @spectrum-web-components/menu@1.5.0
    *   @spectrum-web-components/accordion@1.5.0
    *   @spectrum-web-components/action-bar@1.5.0
    *   @spectrum-web-components/alert-banner@1.5.0
    *   @spectrum-web-components/asset@1.5.0
    *   @spectrum-web-components/avatar@1.5.0
    *   @spectrum-web-components/badge@1.5.0
    *   @spectrum-web-components/button-group@1.5.0
    *   @spectrum-web-components/card@1.5.0
    *   @spectrum-web-components/color-area@1.5.0
    *   @spectrum-web-components/color-handle@1.5.0
    *   @spectrum-web-components/color-loupe@1.5.0
    *   @spectrum-web-components/color-slider@1.5.0
    *   @spectrum-web-components/color-wheel@1.5.0
    *   @spectrum-web-components/divider@1.5.0
    *   @spectrum-web-components/field-label@1.5.0
    *   @spectrum-web-components/help-text@1.5.0
    *   @spectrum-web-components/illustrated-message@1.5.0
    *   @spectrum-web-components/link@1.5.0
    *   @spectrum-web-components/modal@1.5.0
    *   @spectrum-web-components/sidenav@1.5.0
    *   @spectrum-web-components/split-view@1.5.0
    *   @spectrum-web-components/styles@1.5.0
    *   @spectrum-web-components/tags@1.5.0
    *   @spectrum-web-components/tray@1.5.0
    *   @spectrum-web-components/underlay@1.5.0
    *   @spectrum-web-components/checkbox@1.5.0
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/picker-button@1.5.0
    *   @spectrum-web-components/breadcrumbs@1.5.0
    *   @spectrum-web-components/overlay@1.5.0
    *   @spectrum-web-components/color-field@1.5.0
    *   @spectrum-web-components/action-button@1.5.0
    *   @spectrum-web-components/combobox@1.5.0
    *   @spectrum-web-components/tabs@1.5.0
    *   @spectrum-web-components/number-field@1.5.0
    *   @spectrum-web-components/picker@1.5.0
    *   @spectrum-web-components/dialog@1.5.0
    *   @spectrum-web-components/coachmark@1.5.0
    *   @spectrum-web-components/meter@1.5.0
    *   @spectrum-web-components/progress-bar@1.5.0
    *   @spectrum-web-components/slider@1.5.0
    *   @spectrum-web-components/field-group@1.5.0
    *   @spectrum-web-components/radio@1.5.0
    *   @spectrum-web-components/textfield@1.5.0
    *   @spectrum-web-components/theme@1.5.0
    *   @spectrum-web-components/truncated@1.5.0
    *   @spectrum-web-components/switch@1.5.0
    *   @spectrum-web-components/table@1.5.0
    *   @spectrum-web-components/infield-button@1.5.0
    *   @spectrum-web-components/search@1.5.0
    *   @spectrum-web-components/toast@1.5.0
    *   @spectrum-web-components/contextual-help@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/tooltip@1.5.0
    *   @spectrum-web-components/action-group@1.5.0
    *   @spectrum-web-components/action-menu@1.5.0
    *   @spectrum-web-components/top-nav@1.5.0
    *   @spectrum-web-components/clear-button@1.5.0
    *   @spectrum-web-components/close-button@1.5.0
    *   @spectrum-web-components/dropzone@1.5.0
    *   @spectrum-web-components/icon@1.5.0
    *   @spectrum-web-components/icons@1.5.0
    *   @spectrum-web-components/icons-ui@1.5.0
    *   @spectrum-web-components/icons-workflow@1.5.0
    *   @spectrum-web-components/iconset@1.5.0
    *   @spectrum-web-components/progress-circle@1.5.0
    *   @spectrum-web-components/status-light@1.5.0
    *   @spectrum-web-components/swatch@1.5.0
    *   @spectrum-web-components/thumbnail@1.5.0
    *   @spectrum-web-components/base@1.5.0
    *   @spectrum-web-components/grid@1.5.0
    *   @spectrum-web-components/reactive-controllers@1.5.0
    *   @spectrum-web-components/shared@1.5.0

*   Updated dependencies [`2a0422e`, `3cca7ea`, `72dbe62`, `46cd782`, `e247de9`, `6618422`, `1fc141c`, `70f5f6f`, `82212f4`]: 
    *   @spectrum-web-components/picker@1.4.0
    *   @spectrum-web-components/menu@1.4.0
    *   @spectrum-web-components/contextual-help@1.4.0
    *   @spectrum-web-components/styles@1.4.0
    *   @spectrum-web-components/action-button@1.4.0
    *   @spectrum-web-components/overlay@1.4.0
    *   @spectrum-web-components/color-field@1.4.0
    *   @spectrum-web-components/action-menu@1.4.0
    *   @spectrum-web-components/breadcrumbs@1.4.0
    *   @spectrum-web-components/combobox@1.4.0
    *   @spectrum-web-components/card@1.4.0
    *   @spectrum-web-components/illustrated-message@1.4.0
    *   @spectrum-web-components/theme@1.4.0
    *   @spectrum-web-components/truncated@1.4.0
    *   @spectrum-web-components/action-group@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/tooltip@1.4.0
    *   @spectrum-web-components/slider@1.4.0
    *   @spectrum-web-components/action-bar@1.4.0
    *   @spectrum-web-components/accordion@1.4.0
    *   @spectrum-web-components/alert-banner@1.4.0
    *   @spectrum-web-components/asset@1.4.0
    *   @spectrum-web-components/avatar@1.4.0
    *   @spectrum-web-components/badge@1.4.0
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/button-group@1.4.0
    *   @spectrum-web-components/checkbox@1.4.0
    *   @spectrum-web-components/clear-button@1.4.0
    *   @spectrum-web-components/close-button@1.4.0
    *   @spectrum-web-components/coachmark@1.4.0
    *   @spectrum-web-components/color-area@1.4.0
    *   @spectrum-web-components/color-handle@1.4.0
    *   @spectrum-web-components/color-loupe@1.4.0
    *   @spectrum-web-components/color-slider@1.4.0
    *   @spectrum-web-components/color-wheel@1.4.0
    *   @spectrum-web-components/dialog@1.4.0
    *   @spectrum-web-components/divider@1.4.0
    *   @spectrum-web-components/dropzone@1.4.0
    *   @spectrum-web-components/field-group@1.4.0
    *   @spectrum-web-components/field-label@1.4.0
    *   @spectrum-web-components/help-text@1.4.0
    *   @spectrum-web-components/icon@1.4.0
    *   @spectrum-web-components/icons@1.4.0
    *   @spectrum-web-components/icons-ui@1.4.0
    *   @spectrum-web-components/icons-workflow@1.4.0
    *   @spectrum-web-components/iconset@1.4.0
    *   @spectrum-web-components/infield-button@1.4.0
    *   @spectrum-web-components/link@1.4.0
    *   @spectrum-web-components/meter@1.4.0
    *   @spectrum-web-components/modal@1.4.0
    *   @spectrum-web-components/number-field@1.4.0
    *   @spectrum-web-components/picker-button@1.4.0
    *   @spectrum-web-components/progress-bar@1.4.0
    *   @spectrum-web-components/progress-circle@1.4.0
    *   @spectrum-web-components/radio@1.4.0
    *   @spectrum-web-components/search@1.4.0
    *   @spectrum-web-components/sidenav@1.4.0
    *   @spectrum-web-components/split-view@1.4.0
    *   @spectrum-web-components/status-light@1.4.0
    *   @spectrum-web-components/swatch@1.4.0
    *   @spectrum-web-components/switch@1.4.0
    *   @spectrum-web-components/table@1.4.0
    *   @spectrum-web-components/tabs@1.4.0
    *   @spectrum-web-components/tags@1.4.0
    *   @spectrum-web-components/textfield@1.4.0
    *   @spectrum-web-components/thumbnail@1.4.0
    *   @spectrum-web-components/toast@1.4.0
    *   @spectrum-web-components/top-nav@1.4.0
    *   @spectrum-web-components/tray@1.4.0
    *   @spectrum-web-components/underlay@1.4.0
    *   @spectrum-web-components/base@1.4.0
    *   @spectrum-web-components/grid@1.4.0
    *   @spectrum-web-components/reactive-controllers@1.4.0
    *   @spectrum-web-components/shared@1.4.0

*   Updated dependencies [`ea38ef0`, `468314f`]: 
    *   @spectrum-web-components/reactive-controllers@1.3.0
    *   @spectrum-web-components/action-menu@1.3.0
    *   @spectrum-web-components/picker@1.3.0
    *   @spectrum-web-components/menu@1.3.0
    *   @spectrum-web-components/checkbox@1.3.0
    *   @spectrum-web-components/dialog@1.3.0
    *   @spectrum-web-components/overlay@1.3.0
    *   @spectrum-web-components/accordion@1.3.0
    *   @spectrum-web-components/action-group@1.3.0
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/coachmark@1.3.0
    *   @spectrum-web-components/color-area@1.3.0
    *   @spectrum-web-components/color-slider@1.3.0
    *   @spectrum-web-components/color-wheel@1.3.0
    *   @spectrum-web-components/field-label@1.3.0
    *   @spectrum-web-components/meter@1.3.0
    *   @spectrum-web-components/number-field@1.3.0
    *   @spectrum-web-components/progress-bar@1.3.0
    *   @spectrum-web-components/radio@1.3.0
    *   @spectrum-web-components/sidenav@1.3.0
    *   @spectrum-web-components/slider@1.3.0
    *   @spectrum-web-components/swatch@1.3.0
    *   @spectrum-web-components/tabs@1.3.0
    *   @spectrum-web-components/tags@1.3.0
    *   @spectrum-web-components/tooltip@1.3.0
    *   @spectrum-web-components/tray@1.3.0
    *   @spectrum-web-components/grid@1.3.0
    *   @spectrum-web-components/breadcrumbs@1.3.0
    *   @spectrum-web-components/combobox@1.3.0
    *   @spectrum-web-components/card@1.3.0
    *   @spectrum-web-components/switch@1.3.0
    *   @spectrum-web-components/table@1.3.0
    *   @spectrum-web-components/contextual-help@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/truncated@1.3.0
    *   @spectrum-web-components/action-bar@1.3.0
    *   @spectrum-web-components/action-button@1.3.0
    *   @spectrum-web-components/alert-banner@1.3.0
    *   @spectrum-web-components/button-group@1.3.0
    *   @spectrum-web-components/infield-button@1.3.0
    *   @spectrum-web-components/picker-button@1.3.0
    *   @spectrum-web-components/search@1.3.0
    *   @spectrum-web-components/toast@1.3.0
    *   @spectrum-web-components/top-nav@1.3.0
    *   @spectrum-web-components/asset@1.3.0
    *   @spectrum-web-components/avatar@1.3.0
    *   @spectrum-web-components/badge@1.3.0
    *   @spectrum-web-components/clear-button@1.3.0
    *   @spectrum-web-components/close-button@1.3.0
    *   @spectrum-web-components/color-field@1.3.0
    *   @spectrum-web-components/color-handle@1.3.0
    *   @spectrum-web-components/color-loupe@1.3.0
    *   @spectrum-web-components/divider@1.3.0
    *   @spectrum-web-components/dropzone@1.3.0
    *   @spectrum-web-components/field-group@1.3.0
    *   @spectrum-web-components/help-text@1.3.0
    *   @spectrum-web-components/icon@1.3.0
    *   @spectrum-web-components/icons@1.3.0
    *   @spectrum-web-components/icons-ui@1.3.0
    *   @spectrum-web-components/icons-workflow@1.3.0
    *   @spectrum-web-components/iconset@1.3.0
    *   @spectrum-web-components/illustrated-message@1.3.0
    *   @spectrum-web-components/link@1.3.0
    *   @spectrum-web-components/modal@1.3.0
    *   @spectrum-web-components/progress-circle@1.3.0
    *   @spectrum-web-components/split-view@1.3.0
    *   @spectrum-web-components/status-light@1.3.0
    *   @spectrum-web-components/textfield@1.3.0
    *   @spectrum-web-components/thumbnail@1.3.0
    *   @spectrum-web-components/underlay@1.3.0
    *   @spectrum-web-components/base@1.3.0
    *   @spectrum-web-components/shared@1.3.0
    *   @spectrum-web-components/styles@1.3.0
    *   @spectrum-web-components/theme@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **breadcrumbs:** add Breadcrumbs component (#4578) (acd4b5e)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **alert-banner:** add alert banner component (#4266) (10d456e)
*   **contextual-help:** add contextual help pattern (#4285) (a259aa3)

*   **contextual-help:** add contextual help pattern (#4285) (a259aa3)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **color-field:** added missing dependencies (#4141) (b3bb23a)
*   **truncated:** add truncated package (#4163) (4ba0480)

*   Revert "Truncated element (#4125)" (#4160) (da88bbe), closes #4125#4160

*   **color-field:** add color-field package (#3870) (5081634)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **coachmark:** rename "sp-coachmark" to "sp-coachmark-indicator", add "sp-coachmark" (#3639) (a94389c)

*   **combobox:** add combobox pattern (#3894) (47d7d71), closes #3887

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **infield-button:** add infield-button package (057b885)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **alert-dialog:** add Alert Dialog package (#3501) (1062847)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **overlay:** ship Overlay API v2 (67b5d1b)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **tabs:** update bundle setup and readme (0249b94)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **tabs:** update bundle setup and readme (0249b94)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   add Picker Button pattern (31337b8)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   add docs and address PR comments (568062a)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   add swatch pattern (0cdc04b)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   add badge component (cabfdfe)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   add Help Text pattern (fdbb812)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   allow "updateComplete" to resolve to a boolean like the LitElement default (6127946)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   multi-handle slider implementation (8d5a743), closes #1385

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **tray:** add tray pattern (0915fa5)

*   **number-field:** add number field pattern (384ab34)
*   **tabs:** add sp-tab-panel element (b17d276)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   split icons into their own export (98dac4c)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **bundle:** bundle does not export its own custom-elements.json (a362886)

*   **thumbnail:** add the thumbnail package (56935d5)
*   use latest exports specification (a7ecf4b)

*   correct dependency graph (69165eb)

*   setup SplitView component from rebase main (32f3272)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   include the "types" entry in package.json files (b432f59)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **field-label:** add field label pattern (2fa7c7e)
*   **meter:** add meter pattern (fa092ba)

*   include the "types" entry in package.json files (b432f59)

*   **action-button:** add action button pattern (03ac00a)
*   **field-group:** add field-group pattern (f8d265c)
*   **field-label:** add field label pattern (2fa7c7e)
*   **meter:** add meter pattern (fa092ba)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   include default export in the "exports" fields (f32407d)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **accordion:** add accordion pattern (97529d8)
*   **action-group:** add action-group pattern (d2de766)
*   **quick-actions:** add quick-actions pattern (3664b51)
*   **split-button:** add split-button pattern (4833a59)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **asset:** add the asset pattern (a7c00bb)

*   include element is bundle side effects (ce320f8)

*   **bar-loader:** add bar-loader pattern (eff18e7)
*   leverage "exports" field in package.json (321abd7)

*   **button-group:** add ButtonGroup pattern (c4d85b5)

*   add dialog, dialog-wrapped, and underlay elements (3df9050)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **tags:** add tags pattern (ae91865)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **rule:** add Spectrum rule pattern and apply to docs (f4c52ae)

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **coachmark:** add coachmark pattern (f53ae70)
*   **icons-workflow:** add workflow icons package (6b09287)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   factor theme to use a single DOM node (7641228), closes #154

*   join overlay-root and overlay-trigger as overlay (dcde42c)

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **toast:** add "sp-toast" pattern (d0a5f00)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   **circleloader:** add circleloader component (ebab180)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **status-light:** review comments for status-light (80caa08)
*   **status-light:** update version in bundle pjson (a8eabdb)

*   **status-light:** add status-light component (e3a5b3d)

*   **avatar:** add avatar component (a6882b4)

**Note:** Version bump only for package @spectrum-web-components/bundle

**Note:** Version bump only for package @spectrum-web-components/bundle

*   **bundle:** add search (0e00123)
*   **bundle:** include sp-actionbar (af4b09f)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/bundle
