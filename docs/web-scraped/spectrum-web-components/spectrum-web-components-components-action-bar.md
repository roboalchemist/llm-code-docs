# Source: https://opensource.adobe.com/spectrum-web-components/components/action-bar/

Title: Action Bar: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/action-bar/

Markdown Content:
A `<sp-action-bar>` delivers a floating action bar that is a convenient way to deliver stateful actions in cases like selection mode. `<sp-action-bar>` can be deployed in two variants beyond the default: `[varient="fixed"]` to position the element in relation to the page, and `[variant=sticky]` to position the content in relation to content that may scroll.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/action-bar?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/action-bar?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/action-bar

Import the side effectful registration of `<sp-action-bar>` via:

import '@spectrum-web-components/action-bar/sp-action-bar.js';

When looking to leverage the `ActionBar` base class as a type and/or for extension purposes, do so via:

import { ActionBar } from '@spectrum-web-components/action-bar';
<sp-action-bar open>
  2 selected
  <sp-action-button slot="buttons" label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button slot="buttons" label="More">
    <sp-icon-more slot="icon"></sp-icon-more>
  </sp-action-button>
</sp-action-bar>
Use the `emphasized` attribute to add priority to the information that is delivered within your `<sp-action-bar>` element:

<sp-action-bar emphasized open>
  2 selected
  <sp-action-button slot="buttons" label="Edit">
    <sp-icon-edit slot="icon"></sp-icon-edit>
  </sp-action-button>
  <sp-action-button slot="buttons" label="More">
    <sp-icon-more slot="icon"></sp-icon-more>
  </sp-action-button>
</sp-action-bar>
When using `[variant="fixed"]`, the `<sp-action-bar>` will display by default at the bottom left of the window and can be customized via CSS from the outside.

<h4>Look down and to the left when toggling.</h4>
<sp-button onclick="javascript:this.nextElementSibling.open = !this.nextElementSibling.open;">
  Toggle fixed action bar
</sp-button>
<sp-action-bar variant="fixed">2 selected</sp-action-bar>
When using `[variant="sticky"]`, be sure you've spent some time touching up on how `sticky` really works to ensure the most successful delivery of your content.

<section style="position: relative; max-height: 6em; overflow: auto;">
  <h4>Scroll down for toggle button</h4>
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </p>
  <sp-button onclick="javascript:this.nextElementSibling.open = !this.nextElementSibling.open;" >
    Toggle sticky action bar
  </sp-button>
  <sp-action-bar variant="sticky" style="inset-block: 0px">
    2 selected
    <sp-action-button slot="buttons" label="Edit">
      <sp-icon-edit slot="icon"></sp-icon-edit>
    </sp-action-button>
    <sp-action-button slot="buttons" label="More">
      <sp-icon-more slot="icon"></sp-icon-more>
    </sp-action-button>
  </sp-action-bar>
</section>

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2
    *   @spectrum-web-components/button@1.11.2
    *   @spectrum-web-components/action-group@1.11.2
    *   @spectrum-web-components/field-label@1.11.2
    *   @spectrum-web-components/popover@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1
    *   @spectrum-web-components/button@1.11.1
    *   @spectrum-web-components/field-label@1.11.1
    *   @spectrum-web-components/action-group@1.11.1
    *   @spectrum-web-components/popover@1.11.1

*   #5900`283f0fe` Thanks @TarunAdobe! - Added missing dependencies to the package.json files of several components to align with their usage in source code.

*   Updated dependencies [`7af5e8f`, `f8bdeec`, `9cb816b`]:

    *   @spectrum-web-components/field-label@1.11.0
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0
    *   @spectrum-web-components/action-group@1.11.0
    *   @spectrum-web-components/button@1.11.0
    *   @spectrum-web-components/popover@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/action-group@1.10.0
    *   @spectrum-web-components/button@1.10.0
    *   @spectrum-web-components/field-label@1.10.0
    *   @spectrum-web-components/popover@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/popover@1.9.1
    *   @spectrum-web-components/action-group@1.9.1
    *   @spectrum-web-components/button@1.9.1
    *   @spectrum-web-components/field-label@1.9.1
    *   @spectrum-web-components/base@1.9.1

*   Updated dependencies [`7d23140`, `72d807c`]: 
    *   @spectrum-web-components/button@1.9.0
    *   @spectrum-web-components/field-label@1.9.0
    *   @spectrum-web-components/action-group@1.9.0
    *   @spectrum-web-components/popover@1.9.0
    *   @spectrum-web-components/base@1.9.0

*   Updated dependencies [`15be17d`]: 
    *   @spectrum-web-components/button@1.8.0
    *   @spectrum-web-components/popover@1.8.0
    *   @spectrum-web-components/action-group@1.8.0
    *   @spectrum-web-components/field-label@1.8.0
    *   @spectrum-web-components/base@1.8.0

*   Updated dependencies []: 
    *   @spectrum-web-components/popover@1.7.0
    *   @spectrum-web-components/action-group@1.7.0
    *   @spectrum-web-components/button@1.7.0
    *   @spectrum-web-components/field-label@1.7.0
    *   @spectrum-web-components/base@1.7.0

*   Updated dependencies [`03a4439`, `00eb0a8`]: 
    *   @spectrum-web-components/popover@1.6.0
    *   @spectrum-web-components/button@1.6.0
    *   @spectrum-web-components/action-group@1.6.0
    *   @spectrum-web-components/field-label@1.6.0
    *   @spectrum-web-components/base@1.6.0

*   #5271`165a904` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies [`165a904`, `4e06533`]:

    *   @spectrum-web-components/field-label@1.5.0
    *   @spectrum-web-components/button@1.5.0
    *   @spectrum-web-components/popover@1.5.0
    *   @spectrum-web-components/action-group@1.5.0
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-group@1.4.0
    *   @spectrum-web-components/popover@1.4.0
    *   @spectrum-web-components/button@1.4.0
    *   @spectrum-web-components/field-label@1.4.0
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/action-group@1.3.0
    *   @spectrum-web-components/button@1.3.0
    *   @spectrum-web-components/field-label@1.3.0
    *   @spectrum-web-components/popover@1.3.0
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   add `static-color` to replace `static` (#4808) (43cf086)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **action-bar:** support for action-menus (#3780) (4aff599)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **action-bar:** include focus-visible polyfilling (#4273) (fd71ca1)
*   **styles,theme:** add S2 tokens and theme (#4241) (a29e4a2), closes #4232#4228

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **action-bar:** allow "close" event to be cancelled (17cf55e)

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   update deps graph, update link docs (#3709) (2deb284)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **action-bar:** use core tokens (4e21edf)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   correct @element jsDoc listing across library (c97a632)
*   **menu:** add support for submenu interactions (68399af)
*   propogate open to child sp-popover (ae97677)
*   update to latest spectrum-css packages (a5ca19f)

*   **action-bar:** create sp-action-bar component to replace sp-actionbar (38004b4)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   use latest exports specification (a7ecf4b)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   **menu:** add support for submenu interactions (68399af)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   correct @element jsDoc listing across library (c97a632)
*   propogate open to child sp-popover (ae97677)

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

**Note:** Version bump only for package @spectrum-web-components/action-bar

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   **action-bar:** create sp-action-bar component to replace sp-actionbar (38004b4)

Property  Attribute  Type  Default  Description `emphasized``emphasized``boolean``false` Deliver the Action Bar with additional visual emphasis. `flexible``flexible``boolean``false` When `flexible` the action bar sizes itself to its content rather than a specific width. `open``open``boolean``false``variant``variant``string` The variant applies specific styling when set to `sticky` or `fixed`. `variant` attribute is removed when not matching one of the above.

Name  Description `default slot` Content to display with the Action Bar

Name  Type  Description `close``Event`
