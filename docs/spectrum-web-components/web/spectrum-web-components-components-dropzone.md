# Source: https://opensource.adobe.com/spectrum-web-components/components/dropzone/

Title: Dropzone: Spectrum Web Components - Spectrum Web Components

URL Source: https://opensource.adobe.com/spectrum-web-components/components/dropzone/

Markdown Content:
A `<sp-dropzone>` is an area on the screen into which an object can be dragged and dropped to accomplish a task. For example, a drop zone might be used in an upload workflow to enable the user to drop a file from their operating system into the drop zone, which is a more efficient and intuitive action than utilizing the standard "Choose File" dialog.

Drop zones should be used with an illustrated message component as a child if the drop zone is empty, otherwise the existing content should be passed as a child.

![Image 1: See it on NPM!](https://img.shields.io/npm/v/@spectrum-web-components/dropzone?style=for-the-badge)![Image 2: How big is this package in your project?](https://img.shields.io/bundlephobia/minzip/@spectrum-web-components/dropzone?style=for-the-badge)![Image 3: Try it on Stackblitz](https://img.shields.io/badge/Try%20it%20on-Stackblitz-blue?style=for-the-badge)

yarn add @spectrum-web-components/dropzone
Import the side effectful registration of `<sp-dropzone>` via:

import '@spectrum-web-components/dropzone/sp-dropzone.js';
When looking to leverage the `Dropzone` base class as a type and/or for extension purposes, do so via:

import { Dropzone } from '@spectrum-web-components/dropzone';
The `<sp-dropzone>` element consists of several key parts:

*   An illustrated message child component that includes a heading, illustration and an optional body area.
*   An optional action area that can be used to provide additional context to the heading, including a single button or links to prompt the user to take action.

Call to action with links<sp-dropzone id="dropzone-1" style="width: 400px;">
  <sp-illustrated-message heading="Drag and drop your file">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 103" width="150" height="103" >
      <path d="M133.7,8.5h-118c-1.9,0-3.5,1.6-3.5,3.5v27c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V23.5h119V92c0,0.3-0.2,0.5-0.5,0.5h-118c-0.3,0-0.5-0.2-0.5-0.5V69c0-0.8-0.7-1.5-1.5-1.5s-1.5,0.7-1.5,1.5v23c0,1.9,1.6,3.5,3.5,3.5h118c1.9,0,3.5-1.6,3.5-3.5V12C137.2,10.1,135.6,8.5,133.7,8.5z M15.2,21.5V12c0-0.3,0.2-0.5,0.5-0.5h118c0.3,0,0.5,0.2,0.5,0.5v9.5H15.2z M32.6,16.5c0,0.6-0.4,1-1,1h-10c-0.6,0-1-0.4-1-1s0.4-1,1-1h10C32.2,15.5,32.6,15.9,32.6,16.5z M13.6,56.1l-8.6,8.5C4.8,65,4.4,65.1,4,65.1c-0.4,0-0.8-0.1-1.1-0.4c-0.6-0.6-0.6-1.5,0-2.1l8.6-8.5l-8.6-8.5c-0.6-0.6-0.6-1.5,0-2.1c0.6-0.6,1.5-0.6,2.1,0l8.6,8.5l8.6-8.5c0.6-0.6,1.5-0.6,2.1,0c0.6,0.6,0.6,1.5,0,2.1L15.8,54l8.6,8.5c0.6,0.6,0.6,1.5,0,2.1c-0.3,0.3-0.7,0.4-1.1,0.4c-0.4,0-0.8-0.1-1.1-0.4L13.6,56.1z" ></path>
    </svg>
  </sp-illustrated-message>

  <div>
    <label for="file-input">
      <sp-link href="javascript:;" onclick="this.parentElement.nextElementSibling.click()" >
        Select a File
      </sp-link>
      from your computer
    </label>
    <input type="file" id="file-input" style="display: none" />
  </div>
  <div>
    or
    <sp-link href="http://stock.adobe.com" target="blank">
      Search Adobe Stock
    </sp-link>
  </div>
</sp-dropzone>Call to action with button<sp-dropzone id="dropzone-1" style="width: 400px;">
  <sp-illustrated-message heading="Drag and drop your file" description="Or browse files on your computer" >
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 103" width="150" height="103" >
      <path d="M133.7,8.5h-118c-1.9,0-3.5,1.6-3.5,3.5v27c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V23.5h119V92c0,0.3-0.2,0.5-0.5,0.5h-118c-0.3,0-0.5-0.2-0.5-0.5V69c0-0.8-0.7-1.5-1.5-1.5s-1.5,0.7-1.5,1.5v23c0,1.9,1.6,3.5,3.5,3.5h118c1.9,0,3.5-1.6,3.5-3.5V12C137.2,10.1,135.6,8.5,133.7,8.5z M15.2,21.5V12c0-0.3,0.2-0.5,0.5-0.5h118c0.3,0,0.5,0.2,0.5,0.5v9.5H15.2z M32.6,16.5c0,0.6-0.4,1-1,1h-10c-0.6,0-1-0.4-1-1s0.4-1,1-1h10C32.2,15.5,32.6,15.9,32.6,16.5z M13.6,56.1l-8.6,8.5C4.8,65,4.4,65.1,4,65.1c-0.4,0-0.8-0.1-1.1-0.4c-0.6-0.6-0.6-1.5,0-2.1l8.6-8.5l-8.6-8.5c-0.6-0.6-0.6-1.5,0-2.1c0.6-0.6,1.5-0.6,2.1,0l8.6,8.5l8.6-8.5c0.6-0.6,1.5-0.6,2.1,0c0.6,0.6,0.6,1.5,0,2.1L15.8,54l8.6,8.5c0.6,0.6,0.6,1.5,0,2.1c-0.3,0.3-0.7,0.4-1.1,0.4c-0.4,0-0.8-0.1-1.1-0.4L13.6,56.1z" ></path>
    </svg>
  </sp-illustrated-message>

  <sp-button variant="accent">Browse files</sp-button>
</sp-dropzone>Dragged
When a file is dragged over the `<sp-dropzone>` element, it will display with the `dragged` attribute, as follows:

<sp-dropzone id="dropzone" dragged style="width: 400px;">
  <sp-illustrated-message heading="Drag and drop your file">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 103" width="150" height="103" >
      <path d="M133.7,8.5h-118c-1.9,0-3.5,1.6-3.5,3.5v27c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V23.5h119V92c0,0.3-0.2,0.5-0.5,0.5h-118c-0.3,0-0.5-0.2-0.5-0.5V69c0-0.8-0.7-1.5-1.5-1.5s-1.5,0.7-1.5,1.5v23c0,1.9,1.6,3.5,3.5,3.5h118c1.9,0,3.5-1.6,3.5-3.5V12C137.2,10.1,135.6,8.5,133.7,8.5z M15.2,21.5V12c0-0.3,0.2-0.5,0.5-0.5h118c0.3,0,0.5,0.2,0.5,0.5v9.5H15.2z M32.6,16.5c0,0.6-0.4,1-1,1h-10c-0.6,0-1-0.4-1-1s0.4-1,1-1h10C32.2,15.5,32.6,15.9,32.6,16.5z M13.6,56.1l-8.6,8.5C4.8,65,4.4,65.1,4,65.1c-0.4,0-0.8-0.1-1.1-0.4c-0.6-0.6-0.6-1.5,0-2.1l8.6-8.5l-8.6-8.5c-0.6-0.6-0.6-1.5,0-2.1c0.6-0.6,1.5-0.6,2.1,0l8.6,8.5l8.6-8.5c0.6-0.6,1.5-0.6,2.1,0c0.6,0.6,0.6,1.5,0,2.1L15.8,54l8.6,8.5c0.6,0.6,0.6,1.5,0,2.1c-0.3,0.3-0.7,0.4-1.1,0.4c-0.4,0-0.8-0.1-1.1-0.4L13.6,56.1z" ></path>
    </svg>
  </sp-illustrated-message>

  <div>
    <label for="file-input">
      <sp-link href="javascript:;" onclick="this.parentElement.nextElementSibling.click()" >
        Select a File
      </sp-link>
      from your computer
    </label>
    <input type="file" id="file-input" style="display: none" />
  </div>
  <div>
    or
    <sp-link href="http://stock.adobe.com" target="blank">
      Search Adobe Stock
    </sp-link>
  </div>
</sp-dropzone>Filled
When the `<sp-dropzone>` is in a filled state, set the `filled` attribute, as follows:

<sp-action-button draggable="true" style="margin-block-end: 16px;">
    Drag me
</sp-action-button>
<sp-dropzone tabindex="0" id="dropzone" drop-effect="copy">
    <sp-illustrated-message style="--mod-illustrated-message-display: flex;" heading="Drag and drop your file" id="message">
     <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 103" width="150" height="103" >
            <path d="M133.7,8.5h-118c-1.9,0-3.5,1.6-3.5,3.5v27c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V23.5h119V92c0,0.3-0.2,0.5-0.5,0.5h-118c-0.3,0-0.5-0.2-0.5-0.5V69c0-0.8-0.7-1.5-1.5-1.5s-1.5,0.7-1.5,1.5v23c0,1.9,1.6,3.5,3.5,3.5h118c1.9,0,3.5-1.6,3.5-3.5V12C137.2,10.1,135.6,8.5,133.7,8.5z M15.2,21.5V12c0-0.3,0.2-0.5,0.5-0.5h118c0.3,0,0.5,0.2,0.5,0.5v9.5H15.2z M32.6,16.5c0,0.6-0.4,1-1,1h-10c-0.6,0-1-0.4-1-1s0.4-1,1-1h10C32.2,15.5,32.6,15.9,32.6,16.5z M13.6,56.1l-8.6,8.5C4.8,65,4.4,65.1,4,65.1c-0.4,0-0.8-0.1-1.1-0.4c-0.6-0.6-0.6-1.5,0-2.1l8.6-8.5l-8.6-8.5c-0.6-0.6-0.6-1.5,0-2.1c0.6-0.6,1.5-0.6,2.1,0l8.6,8.5l8.6-8.5c0.6-0.6,1.5-0.6,2.1,0c0.6,0.6,0.6,1.5,0,2.1L15.8,54l8.6,8.5c0.6,0.6,0.6,1.5,0,2.1c-0.3,0.3-0.7,0.4-1.1,0.4c-0.4,0-0.8-0.1-1.1-0.4L13.6,56.1z" ></path>
        </svg>
    </sp-illustrated-message>
    <div>
        <label for="file-input">
            <sp-link href="javascript:;" onclick="this.parentElement.nextElementSibling.click()" >
                Select a File
            </sp-link>
            from your computer
        </label>
        <input type="file" id="file-input" style="display: none" />
    </div>
    <div>
        or
        <sp-link href="http://stock.adobe.com" target="blank">
            Search Adobe Stock
        </sp-link>
    </div>
</sp-dropzone>

<script type="module"> customElements.whenDefined('sp-dropzone').then(() => { const dropzone = document.getElementById('dropzone'); const message = document.getElementById('message'); const fileInput = document.getElementById('file-input'); let input; let beingDraggedOver = false; const updateMessage = () => { message.heading = input !== undefined ? (beingDraggedOver ? 'Drop here to replace!' : 'You dropped something!') : 'Drag and drop your file'; }; const handleDropOrChange = () => { input = 'mock-file'; dropzone.setAttribute("filled", true); beingDraggedOver = false; updateMessage(); }; dropzone.addEventListener('dragover', (event) => { event.preventDefault(); beingDraggedOver = true; updateMessage(); }); dropzone.addEventListener('dragleave', () => { beingDraggedOver = false; updateMessage(); }); dropzone.addEventListener('drop', (event) => { event.preventDefault(); handleDropOrChange(); }); fileInput.addEventListener('change', handleDropOrChange); });</script>

When actions, e.g. copy/paste, can be enacted directly on the `<sp-dropzone>` element itself, be sure to supply a `tabindex` so that keyboard users can find this interaction in the tab order. For screen readers, be sure to announce what the actions are, how to complete them, and when they are completed by supplying the appropriate `role` and `aria-label` attributes.

A button is required to have either a visible text label or a `label` attribute on either the `<sp-button>` itself or on an `<sp-icon*>` element child.

*   `Tab`: Moves focus into the dropzone only when button or link is present.
*   `Enter` or `Space`: Activates the button or link.

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

*   #5349`a9727d2` Thanks @renovate! - Remove unnecessary system theme references to reduce complexity for components that don't need the additional mapping layer.

*   Updated dependencies []:

    *   @spectrum-web-components/base@1.6.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.5.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.4.0

*   Updated dependencies []: 
    *   @spectrum-web-components/base@1.3.0

All notable changes to this project will be documented in this file. See Conventional Commits for commit guidelines.

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   lock prerelease versions for Spectrum CSS (#5014) (8aa7734)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   add filled state to dropzone component (#4617) (f6b7144)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   **asset:** use core tokens (99e76f4)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   **dropzone:** use core tokens (11f7560)

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   correct @element jsDoc listing across library (c97a632)
*   **dropzone:** show dragged color in new illustratedmessage version (0591acf)
*   ensure browser understandable extensions (f4e59f7)
*   include "type" in package.json, generate custom-elements.json (1a8d716)
*   include default export in the "exports" fields (f32407d)
*   include the "types" entry in package.json files (b432f59)
*   move hover/focus hoisting into conditioning (15ac2f7)
*   normalize "event" and "error" argument names (8d382cd)
*   remove ":" based namespacing of events (d77a843)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   update side effect listings (8160d3a)
*   update to latest spectrum-css packages (a5ca19f)
*   use latest @spectrum-css/* versions (c35eb86)

*   **action-group:** add action-group pattern (d2de766)
*   adopt DNA@7 base Spectrum CSS (e08cafd)
*   **dropzone:** update spectrum css input (0f5a667)
*   include all Dev Mode files in side effects (f70817c)
*   leverage "exports" field in package.json (321abd7)
*   shared pkg versions, devmode define warning, registry-conflicts docs (6e49565)
*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)
*   use latest exports specification (a7ecf4b)

*   use "sideEffects" listing in package.json (7271614)
*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

*   Revert "chore: release new versions" (a6d655d)

*   **dropzone:** show dragged color in new illustratedmessage version (0591acf)

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   move hover/focus hoisting into conditioning (15ac2f7)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   include all Dev Mode files in side effects (f70817c)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   adopt DNA@7 base Spectrum CSS (e08cafd)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   correct @element jsDoc listing across library (c97a632)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   use latest exports specification (a7ecf4b)

*   update to latest spectrum-css packages (a5ca19f)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **dropzone:** update spectrum css input (0f5a667)

*   include the "types" entry in package.json files (b432f59)
*   stop merging selectors in a way that alters the cascade (369388f)
*   update latest Spectrum CSS beta releases (d8d3acc)
*   use latest @spectrum-css/* versions (c35eb86)

*   **dropzone:** update spectrum css input (0f5a667)

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   include default export in the "exports" fields (f32407d)

*   update side effect listings (8160d3a)

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   update to Spectrum CSS v3.0.0 (e8b3d8f)
*   **action-group:** add action-group pattern (d2de766)

*   ensure browser understandable extensions (f4e59f7)

*   leverage "exports" field in package.json (321abd7)

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   use "sideEffects" listing in package.json (7271614)

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

**Note:** Version bump only for package @spectrum-web-components/dropzone

*   normalize "event" and "error" argument names (8d382cd)

*   include "type" in package.json, generate custom-elements.json (1a8d716)

*   use :focus-visable (via polyfill) instead of :focus (11c6fc7)
*   use @adobe/spectrum-css@2.15.1 (3918888)

*   remove ":" based namespacing of events (d77a843)

*   use imported TypeScript helpers instead of inlining them (cc2bd0a)

**Note:** Version bump only for package @spectrum-web-components/dropzone

Property  Attribute  Type  Default  Description `isDragged``dragged``boolean``false` Indicates that files are currently being dragged over the dropzone. `dropEffect``dropEffect``'copy' | 'move' | 'link' | 'none'` Controls the feedback (typically visual) the user is given during a drag and drop operation `isFilled``filled``boolean``false` Set this property to indicate that the component is in a filled state.

Name  Description `default slot` The default slot on an `sp-dropzone` is a great place to place upload instructions built with an `sp-illustrated-message` or other information, possibly even built from data provided by the upload, to support users successfully interacting with the drag and drop based features of your application

Name  Type  Description `sp-dropzone-dragleave``Event``Announces when dragged files have been moved out of the UI without having been dropped.``sp-dropzone-dragover``Event``Announces when files have been dragged over the UI, but not yet dropped.``sp-dropzone-drop``Event``Announces when dragged files have been dropped on the UI.``sp-dropzone-should-accept``Event``A cancellable event that confirms whether or not a file dropped on the UI should be accepted.`
