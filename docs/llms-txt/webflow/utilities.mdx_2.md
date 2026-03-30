# Source: https://developers.webflow.com/flowkit/v1.0.0/reference/utilities.mdx

***

title: Utilitity Classes
slug: reference/utilities
description: >-
Utilities are a collection of classes fine-tune layouts and components that
render on a website.
hidden: null
'og:title': Flowkit - Utilities
'og:description': >-
Utilities are a collection of classes fine-tune layouts and components that
render on a website.
--------------------

Utilities are a collection of modifier classes that fine-tune layouts and components and keep consistency. You can add a utility classes as a combo class to adjust a behavior of the main class or apply it as a main class to define the functionality of an element. Fo instance, if you want to add a shadow to a card, you can add shadow utility class as a combo class for a card:

All utility classes are prefixed with `[Utility]`. The naming of the utility class describes exactly what it's doing.

## Margins and Padding

Margins and padding are applied to sections, containers, and other elements to define inner spacing or distance between elements.

### Margin

Margin defines the space **outside** of an element.

<div>
  <span>
    Margin
  </span>

  <div>
    <span>
      Padding
    </span>

    <div>
      Content
    </div>
  </div>
</div>

Utility classes use this structure:
<span class="sg-selector sg-class">\[Utility] Margin `Direction` `Value`</span>

**Margin Vertical**

* Direction: `Top`, `Bottom`
* Value: `0`, `0.5rem`, `1rem`, `2rem`, `3rem`, `4rem`, `5rem`, `6rem`, `7rem`, `8rem`, `Auto`

**Margin Horizontal**

* Direction: `Left`, `Right`, `All`
* Value: `0`, `0.5rem`, `1rem`, `2rem`, `Auto`

**Utility classes**

| Class                                                                    | Description                   |
| ------------------------------------------------------------------------ | ----------------------------- |
| <span class="sg-selector sg-class">\[Utility] Margin All 0</span>        | Remove all margin             |
| <span class="sg-selector sg-class">\[Utility] Margin All 0.5rem</span>   | Apply 0.5rem margin all sides |
| <span class="sg-selector sg-class">\[Utility] Tablet Margin Top 0</span> | Top margin 0 on Tablet        |
| <span class="sg-selector sg-class">\[Utility] Mobile Margin Top 0</span> | Top margin 0 on Mobile        |

### Padding

Padding defines the space **inside** of an element.

<div>
  <span>
    Margin
  </span>

  <div>
    <span>
      Padding
    </span>

    <div>
      Content
    </div>
  </div>
</div>

Utility classes use this structure:
<span class="sg-selector sg-class">\[Utility] Padding `Direction` `Value`</span>

**Padding Vertical**

* Direction: `Top`, `Bottom`
* Value: `0`, `0.5rem`, `1rem`, `2rem`, `3rem`, `4rem`, `5rem`, `6rem`, `7rem`, `8rem`

**Padding Horizontal**

* Direction: `Left`, `Right`
* Value: `1rem`, `2rem`

**Padding Around**

* Direction: `All`
* Value: `0`, `0.5rem`, `1rem`, `2rem`, `3rem`, `4rem`

**Padding Utilities**

| Class                                                                        | Description                  |
| ---------------------------------------------------------------------------- | ---------------------------- |
| <span class="sg-selector sg-class">\[Utility] Tablet Padding All 0</span>    | Remove all padding on Tablet |
| <span class="sg-selector sg-class">\[Utility] Tablet Padding All 1rem</span> | Padding 1rem on Tablet       |

### Responsive Spacing

On smaller screens (like **Mobile Landscape**), some margin and padding utility classes will use **smaller spacing variables** than their desktop counterparts.

For example:

<span class="sg-selector sg-class">
  \[Utility] Margin Top 6rem
</span>

* <span class="sg-selector sg-var">6x</span> on desktop,
* <span class="sg-selector sg-var">3x</span> on mobile devices.

This behavior ensures better vertical rhythm and balance on smaller screens without needing to apply breakpoint-specific classes manually.

***

## Display and Overflow

Utilities to control layout visibility and content flow.

| Class                                                                           | Description                       |
| ------------------------------------------------------------------------------- | --------------------------------- |
| <span class="sg-selector sg-class">\[Utility] Display Block</span>              | Forces element to behave as block |
| <span class="sg-selector sg-class">\[Utility] Display Inline Block</span>       | Element behaves like inline-block |
| <span class="sg-selector sg-class">\[Utility] Display None</span>               | Hides element from layout         |
| <span class="sg-selector sg-class">\[Utility] Overflow Clip</span>              | Clips overflow without scroll     |
| <span class="sg-selector sg-class">\[Utility] Overflow Hidden</span>            | Hides overflow, no scroll         |
| <span class="sg-selector sg-class">\[Utility] Overflow Visible</span>           | Makes overflow content visible    |
| <span class="sg-selector sg-class">\[Utility] Overflow Auto</span>              | Scrollbars appear as needed       |
| <span class="sg-selector sg-class">\[Utility] Screen Reader Visible Only</span> | Visible to screen readers only    |

***

## Position

Controls element positioning behavior across breakpoints.

<svg data-wf-icon="DeviceLaptopStar24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18 11H19V8.366L21.2811 9.68301L21.7811 8.81699L19.5 7.49999L21.7811 6.18301L21.2811 5.31699L19 6.63399V4H18V6.63395L15.719 5.31699L15.219 6.18301L17.5 7.49999L15.2189 8.81699L15.7189 9.68301L18 8.36604V11Z" fill="currentColor" /><path d="M5.5 6H14V7H5.5C5.22386 7 5 7.22386 5 7.5V17H19V12H20V17L23 17.0273V18.0273H1V17.0273L4 17V7.5C4 6.67157 4.67157 6 5.5 6Z" fill="currentColor" /></svg> **Desktop**

{/* <!-- vale off --> */}

| Class                                                                                                                         | Description                          |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| <span class="sg-selector sg-class">\[Utility] Position Relative</span>                                                        | Offsets relative to normal position  |
| <span class="sg-selector sg-class">\[Utility] Position Absolute</span>                                                        | Removes from flow, absolute position |
| <span class="sg-selector sg-class">\[Utility] Position Fixed</span>                                                           | Fixed relative to viewport           |
| <span class="sg-selector sg-class">\[Utility] Position Fixed</span> <span class="sg-selector sg-class">Fixed Top</span>       | Fixed to top edge                    |
| <span class="sg-selector sg-class">\[Utility] Position Fixed</span> <span class="sg-selector sg-class">Fixed Left</span>      | Fixed to left edge                   |
| <span class="sg-selector sg-class">\[Utility] Position Fixed</span> <span class="sg-selector sg-class">Fixed Right</span>     | Fixed to right edge                  |
| <span class="sg-selector sg-class">\[Utility] Position Sticky</span>                                                          | Sticks to top on scroll              |
| <span class="sg-selector sg-class">\[Utility] Position Sticky</span> <span class="sg-selector sg-class">Top 120</span>        | Custom offset sticky                 |
| <span class="sg-selector sg-class">\[Utility] Position Sticky</span> <span class="sg-selector sg-class">Sticky Desktop</span> | Sticky only on desktop               |
| <span class="sg-selector sg-class">\[Utility] Position Static</span>                                                          | Default positioning                  |
| <span class="sg-selector sg-class">\[Utility] Z-Index 1</span>                                                                | Layer stacking with values 1–5       |

{/* <!-- vale on --> */}

<svg data-wf-icon="DeviceTabletPortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.99658 17L13.9966 17.0273L14.0034 16.0274L10.0034 16L9.99658 17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 5C6.67157 5 6 5.67157 6 6.5V17.5C6 18.3284 6.67157 19 7.5 19H16.5C17.3284 19 18 18.3284 18 17.5V6.5C18 5.67157 17.3284 5 16.5 5H7.5ZM7 6.5C7 6.22386 7.22386 6 7.5 6H16.5C16.7761 6 17 6.22386 17 6.5V17.5C17 17.7761 16.7761 18 16.5 18H7.5C7.22386 18 7 17.7761 7 17.5V6.5Z" fill="currentColor" /></svg> **Tablet**

| Class                                                                         | Description                     |
| ----------------------------------------------------------------------------- | ------------------------------- |
| <span class="sg-selector sg-class">\[Utility] Tablet Position Absolute</span> | Set position absolute on tablet |
| <span class="sg-selector sg-class">\[Utility] Tablet Position Relative</span> | Set position relative on tablet |
| <span class="sg-selector sg-class">\[Utility] Tablet Position Static</span>   | Set position static on tablet   |

<svg data-wf-icon="DeviceMobilePortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11 17H14V16H11V17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M17 6.5C17 5.67157 16.3284 5 15.5 5H9.5C8.67157 5 8 5.67157 8 6.5V17.5C8 18.3284 8.67157 19 9.5 19H15.5C16.3284 19 17 18.3284 17 17.5V6.5ZM15.5 6C15.7761 6 16 6.22386 16 6.5V17.5C16 17.7761 15.7761 18 15.5 18H9.5C9.22386 18 9 17.7761 9 17.5V6.5C9 6.22386 9.22386 6 9.5 6L15.5 6Z" fill="currentColor" /></svg> **Mobile**

{/* <!-- vale off --> */}

| Class                                                                                                                        | Description                |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| <span class="sg-selector sg-class">\[Utility] Position Sticky</span> <span class="sg-selector sg-class">Sticky Mobile</span> | Mobile-only sticky support |

{/* <!-- vale on --> */}

***

## Transform

Controls element translation and rotation.

| Class                                                              | Description                          |
| ------------------------------------------------------------------ | ------------------------------------ |
| <span class="sg-selector sg-class">\[Utility] Move Up 15%</span>   | Shifts element upward by 15%         |
| <span class="sg-selector sg-class">\[Utility] Move Up 50%</span>   | Shifts element upward by 50%         |
| <span class="sg-selector sg-class">\[Utility] Move Down 15%</span> | Shifts element downward by 15%       |
| <span class="sg-selector sg-class">\[Utility] Move Down 25%</span> | Shifts element downward by 25%       |
| <span class="sg-selector sg-class">\[Utility] Move Down 50%</span> | Shifts element downward by 50%       |
| <span class="sg-selector sg-class">\[Utility] Rotate -12</span>    | Rotates element left by 12 degrees   |
| <span class="sg-selector sg-class">\[Utility] Rotate -4.5</span>   | Rotates element left by 4.5 degrees  |
| <span class="sg-selector sg-class">\[Utility] Rotate 12</span>     | Rotates element right by 12 degrees  |
| <span class="sg-selector sg-class">\[Utility] Rotate 4.5</span>    | Rotates element right by 4.5 degrees |

***

## Width

Controls fixed, responsive, and percentage-based width settings.

<svg data-wf-icon="DeviceLaptopStar24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18 11H19V8.366L21.2811 9.68301L21.7811 8.81699L19.5 7.49999L21.7811 6.18301L21.2811 5.31699L19 6.63399V4H18V6.63395L15.719 5.31699L15.219 6.18301L17.5 7.49999L15.2189 8.81699L15.7189 9.68301L18 8.36604V11Z" fill="currentColor" /><path d="M5.5 6H14V7H5.5C5.22386 7 5 7.22386 5 7.5V17H19V12H20V17L23 17.0273V18.0273H1V17.0273L4 17V7.5C4 6.67157 4.67157 6 5.5 6Z" fill="currentColor" /></svg> **Desktop**

| Class                                                             | Description                 |
| ----------------------------------------------------------------- | --------------------------- |
| <span class="sg-selector sg-class">\[Utility] Max Width XS</span> | Restricts max width to XS   |
| <span class="sg-selector sg-class">\[Utility] Max Width SM</span> | Restricts max width to SM   |
| <span class="sg-selector sg-class">\[Utility] Max Width MD</span> | Restricts max width to MD   |
| <span class="sg-selector sg-class">\[Utility] Max Width LG</span> | Restricts max width to LG   |
| <span class="sg-selector sg-class">\[Utility] Width Auto</span>   | Width auto based on content |
| <span class="sg-selector sg-class">\[Utility] Width SM</span>     | Small fixed width           |
| <span class="sg-selector sg-class">\[Utility] Width MD</span>     | Medium fixed width          |
| <span class="sg-selector sg-class">\[Utility] Width 35%</span>    | Width set to 35%            |
| <span class="sg-selector sg-class">\[Utility] Width 40%</span>    | Width set to 40%            |
| <span class="sg-selector sg-class">\[Utility] Width 60%</span>    | Width set to 60%            |

<svg data-wf-icon="DeviceTabletPortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.99658 17L13.9966 17.0273L14.0034 16.0274L10.0034 16L9.99658 17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 5C6.67157 5 6 5.67157 6 6.5V17.5C6 18.3284 6.67157 19 7.5 19H16.5C17.3284 19 18 18.3284 18 17.5V6.5C18 5.67157 17.3284 5 16.5 5H7.5ZM7 6.5C7 6.22386 7.22386 6 7.5 6H16.5C16.7761 6 17 6.22386 17 6.5V17.5C17 17.7761 16.7761 18 16.5 18H7.5C7.22386 18 7 17.7761 7 17.5V6.5Z" fill="currentColor" /></svg> **Tablet**

| Class                                                                  | Description                   |
| ---------------------------------------------------------------------- | ----------------------------- |
| <span class="sg-selector sg-class">\[Utility] Tablet Width 50%</span>  | Sets width to 50% on tablets  |
| <span class="sg-selector sg-class">\[Utility] Tablet Width 60%</span>  | Sets width to 60% on tablets  |
| <span class="sg-selector sg-class">\[Utility] Tablet Width 100%</span> | Sets width to 100% on tablets |

<svg data-wf-icon="DeviceMobilePortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11 17H14V16H11V17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M17 6.5C17 5.67157 16.3284 5 15.5 5H9.5C8.67157 5 8 5.67157 8 6.5V17.5C8 18.3284 8.67157 19 9.5 19H15.5C16.3284 19 17 18.3284 17 17.5V6.5ZM15.5 6C15.7761 6 16 6.22386 16 6.5V17.5C16 17.7761 15.7761 18 15.5 18H9.5C9.22386 18 9 17.7761 9 17.5V6.5C9 6.22386 9.22386 6 9.5 6L15.5 6Z" fill="currentColor" /></svg> **Mobile Landscape**

| Class                                                                            | Description        |
| -------------------------------------------------------------------------------- | ------------------ |
| <span class="sg-selector sg-class">\[Utility] Mobile Landscape Width 70%</span>  | Sets width to 70%  |
| <span class="sg-selector sg-class">\[Utility] Mobile Landscape Width 80%</span>  | Sets width to 80%  |
| <span class="sg-selector sg-class">\[Utility] Mobile Landscape Width 100%</span> | Sets width to 100% |

<svg data-wf-icon="DeviceMobilePortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11 17H14V16H11V17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M17 6.5C17 5.67157 16.3284 5 15.5 5H9.5C8.67157 5 8 5.67157 8 6.5V17.5C8 18.3284 8.67157 19 9.5 19H15.5C16.3284 19 17 18.3284 17 17.5V6.5ZM15.5 6C15.7761 6 16 6.22386 16 6.5V17.5C16 17.7761 15.7761 18 15.5 18H9.5C9.22386 18 9 17.7761 9 17.5V6.5C9 6.22386 9.22386 6 9.5 6L15.5 6Z" fill="currentColor" /></svg> **Mobile Portrait**

| Class                                                                           | Description        |
| ------------------------------------------------------------------------------- | ------------------ |
| <span class="sg-selector sg-class">\[Utility] Mobile Portrait Width 100%</span> | Sets width to 100% |

***

## Height

Controls element height and minimum height behavior across breakpoints.

<svg data-wf-icon="DeviceLaptopStar24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M18 11H19V8.366L21.2811 9.68301L21.7811 8.81699L19.5 7.49999L21.7811 6.18301L21.2811 5.31699L19 6.63399V4H18V6.63395L15.719 5.31699L15.219 6.18301L17.5 7.49999L15.2189 8.81699L15.7189 9.68301L18 8.36604V11Z" fill="currentColor" /><path d="M5.5 6H14V7H5.5C5.22386 7 5 7.22386 5 7.5V17H19V12H20V17L23 17.0273V18.0273H1V17.0273L4 17V7.5C4 6.67157 4.67157 6 5.5 6Z" fill="currentColor" /></svg> **Desktop**

| Class                                                                    | Description             |
| ------------------------------------------------------------------------ | ----------------------- |
| <span class="sg-selector sg-class">\[Utility] Height 100%</span>         | Full height of parent   |
| <span class="sg-selector sg-class">\[Utility] Min Height 100%</span>     | Minimum height 100%     |
| <span class="sg-selector sg-class">\[Utility] Viewport Height 50</span>  | 50% of viewport height  |
| <span class="sg-selector sg-class">\[Utility] Viewport Height 100</span> | 100% of viewport height |

<svg data-wf-icon="DeviceTabletPortrait24Icon" width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.99658 17L13.9966 17.0273L14.0034 16.0274L10.0034 16L9.99658 17Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M7.5 5C6.67157 5 6 5.67157 6 6.5V17.5C6 18.3284 6.67157 19 7.5 19H16.5C17.3284 19 18 18.3284 18 17.5V6.5C18 5.67157 17.3284 5 16.5 5H7.5ZM7 6.5C7 6.22386 7.22386 6 7.5 6H16.5C16.7761 6 17 6.22386 17 6.5V17.5C17 17.7761 16.7761 18 16.5 18H7.5C7.22386 18 7 17.7761 7 17.5V6.5Z" fill="currentColor" /></svg> **Tablet**

| Class                                                                       | Description                     |
| --------------------------------------------------------------------------- | ------------------------------- |
| <span class="sg-selector sg-class">\[Utility] Tablet Height Auto</span>     | Sets height auto on tablets     |
| <span class="sg-selector sg-class">\[Utility] Tablet Min Height Auto</span> | Sets min-height auto on tablets |

***

## Border Radius

Controls element corner roundness using utility classes.

### Component Specific

These are helpful when you need to customize or reset corners without affecting the base component class.

* <span class="sg-selector sg-class">
    \[Utility] Radius Card
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Radius Button
  </span>

### Size Specific

Use the <span class="sg-selector sg-class">\[Utility] Radius `Size`</span> format to control element corner roundness.
The `Size` follows t-shirt sizing convention: `SM`, `MD`, `LG`, `XL`, `Round`

Example: <span class="sg-selector sg-class">\[Utility] Radius LG</span>

### Side-specific

These utilities give you full control when working with overlapping sections, containers with flush corners, or when selectively removing roundness.

* <span class="sg-selector sg-class">
    \[Utility] Radius All 0
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Radius Top 0
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Radius Right 0
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Radius Bottom 0
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Radius Left 0
  </span>

***

## Mask

Use utility mask classes <span class="sg-selector sg-class">\[Utility] Mask (Direction)</span> to apply directional fades to images or elements.
These are commonly paired with <span class="sg-selector sg-class">Overlay</span> and <span class="sg-selector sg-class">Image</span>

Apply one of the following as a combo class:

* <span class="sg-selector sg-class">
    \[Utility] Mask Top
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Mask Bottom
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Mask Left
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Mask Right
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Mask Horizontal Fade
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Mask Vertical Fade
  </span>

Example:

<span class="sg-selector sg-class">
  Image
</span>

<span class="sg-selector sg-class">
  \[Utility] Mask Bottom
</span>

<div>
  <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 1280 800" fill="none">
    <rect width="1280" height="800" fill="#F0F0F0" />

    <path fill-rule="evenodd" clip-rule="evenodd" d="M529.954 336.456C529.954 326.991 537.627 319.318 547.092 319.318C556.557 319.318 564.23 326.991 564.23 336.456C564.23 345.92 556.557 353.593 547.092 353.593C537.627 353.593 529.954 345.92 529.954 336.456ZM547.092 313.46C534.392 313.46 524.096 323.755 524.096 336.456C524.096 349.156 534.392 359.451 547.092 359.451C559.792 359.451 570.087 349.156 570.087 336.456C570.087 323.755 559.792 313.46 547.092 313.46ZM611.751 366.971C612.653 366.971 613.504 367.386 614.059 368.097L659.813 426.672L685.27 394.827C685.826 394.131 686.668 393.727 687.558 393.727C688.448 393.727 689.29 394.131 689.846 394.827L759.359 481.782C760.062 482.662 760.198 483.866 759.711 484.88C759.223 485.895 758.197 486.54 757.071 486.54H700.936C700.875 486.54 700.814 486.538 700.754 486.534C700.694 486.538 700.634 486.54 700.573 486.54H522.929C521.809 486.54 520.787 485.902 520.297 484.895C519.806 483.889 519.931 482.691 520.621 481.808L609.443 368.097C609.998 367.386 610.849 366.971 611.751 366.971ZM702.002 480.682L663.52 431.417L687.558 401.346L750.98 480.682H702.002ZM611.751 374.658L528.933 480.682H694.569L611.751 374.658Z" fill="#ABABAB" />
  </svg>
</div>

***

## Overlay

Overlay classes are used to create translucent layers above content.
They are commonly used to improve readability on background images or to emphasize text.

| Class                                                     | Description                              |
| --------------------------------------------------------- | ---------------------------------------- |
| <span class="sg-selector sg-class">Overlay</span>         | Adds a dark semi-transparent background  |
| <span class="sg-selector sg-class">Inverse Overlay</span> | Adds a light semi-transparent background |

**Link Overlay**

| Class                                                             | Description                                                                  |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| <span class="sg-selector sg-class">\[Utility] Link Overlay</span> | Expands a link to cover its entire container (use inside position: relative) |

**Overlay with Mask**

Combine <span class="sg-selector sg-class">Overlay</span> with directional mask utility classes to create faded on a side images or faded overlays.

Example:

* <span class="sg-selector sg-class">
    Overlay
  </span>
  <span class="sg-selector sg-class">
    \[Utility] Mask Top
  </span>
* <span class="sg-selector sg-class">
    Overlay
  </span>
  <span class="sg-selector sg-class">
    \[Utility] Mask Left
  </span>

***

## Drop Shadow

Add subtle or strong depth to elements using drop shadow utility classes.

* <span class="sg-selector sg-class">
    \[Utility] Shadow XXS
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow XS
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow SM
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow MD
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow LG
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow XL
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Shadow XXL
  </span>

***

## Typography

These utility classes allow you to control alignment and color of text elements globally or responsively.

### Text Color

These utility classes are used to apply specific text colors to an element.

* <span class="sg-selector sg-class">
    \[Utility] Text Primary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Secondary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Inverse
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Inverse Secondary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Accent Primary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Accent Secondary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Accent Tertiary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Accent On Inverse
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Accent On Primary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text On Accent Primary
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text On Accent Secondary
  </span>

### Text Alignment

Text alignment utilities let you override the default left-aligned behavior.

* <span class="sg-selector sg-class">
    \[Utility] Text Align Left
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Align Center
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Align Right
  </span>

Responsive modifiers:

* <span class="sg-selector sg-class">
    \[Utility] Text Align Center Tablet
  </span>
* <span class="sg-selector sg-class">
    \[Utility] Text Align Right Mobile
  </span>

***

## Misc

Other utility helpers for visual effects and behaviors.

| Class                                                                     | Description                          |
| ------------------------------------------------------------------------- | ------------------------------------ |
| <span class="sg-selector sg-class">\[Utility] Filter Invert</span>        | Inverts colors (dark/light mode)     |
| <span class="sg-selector sg-class">\[Utility] Text Decoration None</span> | Removes underline from links or text |
| <span class="sg-selector sg-class">\[Utility] Backdrop Filter Blur</span> | Applies backdrop blur filter         |
| <span class="sg-selector sg-class">\[Utility] Link Content Block</span>   | Expands link to fill container       |
