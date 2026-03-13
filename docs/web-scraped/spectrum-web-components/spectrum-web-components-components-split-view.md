# Source: https://opensource.adobe.com/spectrum-web-components/components/split-view/

Title: Split View: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/split-view/

Markdown Content:
An `sp-split-view` element displays its first two direct child elements side by side (horizontal) or stacked (vertical with `vertical` attribute). The component automatically distributes the available space between the two panels. When the `resizable` attribute is added, users can drag the splitter or use keyboard controls to adjust the panel sizes.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/split-view?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/split-view?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/split-view
Import the side effectful registration of `<sp-split-view>` via:

import '@spectrum-web-components/split-view/sp-split-view.js';
When looking to leverage the `SplitView` base class as a type and/or for extension purposes, do so via:

import { SplitView } from '@spectrum-web-components/split-view';
Use the `collapsible` attribute to allow the user to collapse the split view. The `collapsible` attribute requires the `resizable` attribute to be set. When `collapsible` is set, primary and secondary min and max sizes are ignored.

Use the `resizable` attribute to allow the user to resize the split view. When `resizable` is set, it is recommended that you set preferred primary and secondary min and max sizes. If primary and/or secondary sizes, the `resize` behavior will resemble the `collapsible` behavior.

Use the `label` attribute to set the `aria-label` on the `splitter` element.

`primary-size` sets starting size of the primary pane. It can be a real pixel number|string, percentage or "auto". For example: "100", "120px", "75%" or "auto" are valid values

`primary-min` is the minimum size of the primary pane, while `primary-max` is the maximum size of the primary pane.

`secondary-min` is the minimum size of the secondary pane, while `secondary-max` is the maximum size of the secondary pane.

`splitter-pos` is the current splitter position of the split view.

Horizontal is the default orientation for the split view and does not require an attribute to be set.

Basic<sp-split-view>
  <div>Left panel</div>
  <div>Right panel</div>
</sp-split-view>Resizable<sp-split-view resizable primary-min="50" secondary-min="50" primary-size="100" label="Resize the horizontal panels">
  <div>
    <h1>Left panel</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    </p>
  </div>
  <div>
    <h2>Right panel</h2>
    <p>
      It is a long established fact that a reader will be distracted by the
      readable content of a page when looking at its layout.
    </p>
  </div>
</sp-split-view>Resizable & collapsible<sp-split-view resizable collapsible label="Resize the horizontal collapsible panels">
  <div>
    <h1>Left panel</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    </p>
  </div>
  <div>
    <h2>Right panel</h2>
    <p>
      It is a long established fact that a reader will be distracted by the
      readable content of a page when looking at its layout.
    </p>
  </div>
</sp-split-view>
Vertical split view requires the `vertical` attribute to be set.

Basic<sp-split-view vertical>
  <div>Top panel</div>
  <div>Bottom panel</div>
</sp-split-view>Resizable<sp-split-view vertical resizable primary-min="50" primary-max="150" secondary-min="50" label="Resize the vertical panels">
  <div>
    <h1>Top panel</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    </p>
  </div>
  <div>
    <h2>Bottom panel</h2>
    <p>
      It is a long established fact that a reader will be distracted by the
      readable content of a page when looking at its layout.
    </p>
  </div>
</sp-split-view>Resizable & collapsible<sp-split-view vertical resizable collapsible style="height: 300px;" label="Resize the vertical collapsible panels">
  <div>
    <h1>Top panel</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    </p>
  </div>
  <div>
    <h2>Bottom panel</h2>
    <p>
      It is a long established fact that a reader will be distracted by the
      readable content of a page when looking at its layout.
    </p>
  </div>
</sp-split-view><sp-split-view resizable primary-min="50" primary-max="200" secondary-min="50" style="height: 400px; width: 600px;">
  <div>
    <h1>First panel - Level 1</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
      Lorem Ipsum has been the industry's standard dummy text ever since the
      1500s, when an unknown printer took a galley of type and scrambled it to
      make a type specimen book.
    </p>
  </div>
  <div>
    <h2>Second panel - Level 1</h2>
    <sp-split-view vertical resizable primary-min="50" primary-size="100" secondary-min="50" style="height: 300px;" >
      <div>
        <h3>First panel - Level 2</h3>
        <p>
          Lorem Ipsum is simply dummy text of the printing and typesetting
          industry.
        </p>
      </div>
      <div>
        <h4>Second panel - Level 2</h4>
        <p>
          It is a long established fact that a reader will be distracted by the
          readable content of a page when looking at its layout.
        </p>
      </div>
    </sp-split-view>
  </div>
</sp-split-view>
The `label` attribute is used to set the `aria-label` on the `splitter` element. By default, the `splitter` element within an `<sp-split-view>` is given the label "Resize the panels". A label is required to surface the element and signal the interaction correctly to screen readers. You can customize or internationalize this by setting the `label` attribute.

The splitter element is given the role `separator` to indicate that it is a divider separating sections of content in the split view panels.

The `aria-controls` attribute is set to the id of the controlled element. This is used to indicate that the splitter is controlling the size of the primary and secondary panes.

`aria-orientation` is set to `horizontal` or `vertical` to indicate the orientation of the split view.

`aria-valuenow` is used to indicate the current size of the primary pane as a percentage of the total size of the split view.

The splitter has an explicit `tabindex` of `0` when `resizable` is set. This allows the splitter to be focused and and navigable using the keyboard. The arrow keys can be used to move the splitter left and right or up and down depending on the orientation of the split view.

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.11.2
    *   @spectrum-web-components/shared@1.11.2

*   Updated dependencies [`95e1c25`]: 
    *   @spectrum-web-components/shared@1.11.1
    *   @spectrum-web-components/base@1.11.1

*   Updated dependencies [`f8bdeec`, `9cb816b`]: 
    *   @spectrum-web-components/shared@1.11.0
    *   @spectrum-web-components/base@1.11.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.10.0
    *   @spectrum-web-components/shared@1.10.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.1
    *   @spectrum-web-components/shared@1.9.1

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.9.0
    *   @spectrum-web-components/shared@1.9.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.8.0
    *   @spectrum-web-components/shared@1.8.0

*   #5428`94dd388` Thanks @Rajdeepc! - Added @spectrum-web-components/shared dependency in splitview since it uses ranDomId from the shared package

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.7.0
    *   @spectrum-web-components/shared@1.7.0

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

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   allowing split view to have a custom aria label (#4155) (d9abed7)

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   support generating random IDs outside of secure contexts (485a67c)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   **split-view:** expand accessible attribute usage and HCM delivery (cb7c71f)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   **base:** ensure streaming listener "streams" on the animation frame (1478db1)

**Note:** Version bump only for package @spectrum-web-components/split-view

*   adapt and improve css (649eeed)
*   adapt tests (88a2ff7)
*   add @slot description (03019d6)
*   cleaning up spectrum-config (0fde625)
*   correct @element jsDoc listing across library (c97a632)
*   correct calculation of height when using primary-size='auto' (0ff67c0)
*   correct viewSize calc and test (2befdd5)
*   improve css class handling, %-test and increase base dependency (2f2c28d)
*   improve css, simplify attributes & properties (6ddd47c)
*   polishing (d112875)
*   **split-view:** end drag on pointerleave (85e5258)
*   **split-view:** prevent touch-action on handle for delivery in mobile (b68c497)
*   **split-view:** redraw when primary-size change (665d238)

*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   include all Dev Mode files in side effects (f70817c)
*   setup SplitView component from rebase main (32f3272)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update lit-* dependencies, wip (377f3c8)
*   use latest exports specification (a7ecf4b)

*   version update (ab58bf9)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   **split-view:** prevent touch-action on handle for delivery in mobile (b68c497)

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   **split-view:** end drag on pointerleave (85e5258)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   update lit-* dependencies, wip (377f3c8)

**Note:** Version bump only for package @spectrum-web-components/split-view

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   correct @element jsDoc listing across library (c97a632)

*   **split-view:** redraw when primary-size change (665d238)

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

**Note:** Version bump only for package @spectrum-web-components/split-view

*   correct calculation of height when using primary-size='auto' (0ff67c0)

*   use latest exports specification (a7ecf4b)

*   version update (ab58bf9)

*   adapt and improve css (649eeed)
*   adapt tests (88a2ff7)
*   add @slot description (03019d6)
*   cleaning up spectrum-config (0fde625)
*   correct viewSize calc and test (2befdd5)
*   improve css class handling, %-test and increase base dependency (2f2c28d)
*   improve css, simplify attributes & properties (6ddd47c)
*   polishing (d112875)

*   setup SplitView component from rebase main (32f3272)

Property  Attribute  Type  Default  Description `collapsible``collapsible``boolean``false``label``label``string | undefined` Sets the `aria-label` on the splitter component `primaryMax``primary-max``DEFAULT_MAX_SIZE` The maximum size of the primary pane `primaryMin``primary-min``number``0` The minimum size of the primary pane `primarySize``primary-size``number | `${number}px` | `${number}%` | "auto"` The start size of the primary pane, can be a real pixel number|string, percentage or "auto" For example: "100", "120px", "75%" or "auto" are valid values `primarySize``primarySize``number | `${number}px` | `${number}%` | "auto"` The start size of the primary pane, can be a real pixel number|string, percentage or "auto" For example: "100", "120px", "75%" or "auto" are valid values `resizable``resizable``boolean``false``secondaryMax``secondary-max``DEFAULT_MAX_SIZE` The maximum size of the secondary pane `secondaryMin``secondary-min``number``0` The minimum size of the secondary pane `splitterPos``splitter-pos``number | undefined` The current splitter position of split-view `vertical``vertical``boolean``false`

Name  Description `Two` sibling elements to be sized by the element attritubes

Name  Type  Description `change``Event``Announces the new position of the splitter`
