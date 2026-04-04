# Source: https://developers.webflow.com/flowkit/structure/grid.mdx

***

title: Grid layout
slug: structure/grid
description: Grid layout system in Webflow CSS Framework using responsive combo classes.
hidden: null
'og:title': Flowkit - Grid
'og:description': Grid layout system in Webflow CSS Framework using responsive combo classes.
---------------------------------------------------------------------------------------------

## Grid system

The grid system provides a flexible layout foundation using CSS Grid. Basic grid classes come with built-in responsive behavior that automatically adjusts the layout based on screen size.

### Basic grid classes

Basic grid classes with base column configurations:

<ul>
  * <span class="sg-selector sg-class">
      grid_1-col
    </span>
  * <span class="sg-selector sg-class">
      grid_2-col
    </span>
  * <span class="sg-selector sg-class">
      grid_3-col
    </span>
  * <span class="sg-selector sg-class">
      grid_4-col
    </span>
  * <span class="sg-selector sg-class">
      grid_5-col
    </span>
  * <span class="sg-selector sg-class">
      grid_6-col
    </span>
  * <span class="sg-selector sg-class">
      grid_9-col
    </span>
  * <span class="sg-selector sg-class">
      grid_12-col
    </span>
</ul>

### Responsive behavior

These responsive behaviors are built into the grid classes and automatically adjust the layout based on screen size without requiring additional responsive modifiers.

| Grid Class                                             | Desktop    | Tablet    | Mobile-L  | Mobile   |
| ------------------------------------------------------ | ---------- | --------- | --------- | -------- |
| <span class="sg-selector sg-class">grid\_1-col</span>  | 1 column   | 1 column  | 1 column  | 1 column |
| <span class="sg-selector sg-class">grid\_2-col</span>  | 2 columns  | 2 columns | 1 column  | 1 column |
| <span class="sg-selector sg-class">grid\_3-col</span>  | 3 columns  | 3 columns | 2 columns | 1 column |
| <span class="sg-selector sg-class">grid\_4-col</span>  | 4 columns  | 2 columns | 1 column  | 1 column |
| <span class="sg-selector sg-class">grid\_5-col</span>  | 5 columns  | 3 columns | 2 columns | 1 column |
| <span class="sg-selector sg-class">grid\_6-col</span>  | 6 columns  | 3 columns | 2 columns | 1 column |
| <span class="sg-selector sg-class">grid\_9-col</span>  | 9 columns  | 3 columns | 2 columns | 1 column |
| <span class="sg-selector sg-class">grid\_12-col</span> | 12 columns | 3 columns | 2 columns | 1 column |

Default behavior can be adjusted using responsive combo classes:

<span class="sg-selector sg-class">
  grid_3-col
</span>

<span class="sg-selector sg-class">
  tablet-1-col
</span>

***

## Spacing modifiers

Class structure:
<span class="sg-selector sg-class">grid\_`columns`-col</span> <span class="sg-selector sg-class">gap-`size`</span>

Size options: `xsmall`, `small`, `medium`, `large`, `xlarge`, `xxlarge`

Example: <span class="sg-selector sg-class">grid\_3-col</span> <span class="sg-selector sg-class">gap-medium</span>

***

## Alignment modifiers

These modifiers set alignment for all child elements inside the grid.

Class structure:
<span class="sg-selector sg-class">grid\_`columns`-col</span> <span class="sg-selector sg-class">is-`X or Y`-`position`</span>

Available combo classes:

* <span class="sg-selector sg-class">
    is-x-left
  </span>
* <span class="sg-selector sg-class">
    is-x-center
  </span>
* <span class="sg-selector sg-class">
    is-x-right
  </span>
* <span class="sg-selector sg-class">
    is-y-top
  </span>
* <span class="sg-selector sg-class">
    is-y-center
  </span>
* <span class="sg-selector sg-class">
    is-y-bottom
  </span>

Example: <span class="sg-selector sg-class">grid\_3-col</span> <span class="sg-selector sg-class">is-x-center</span> <span class="sg-selector sg-class">is-y-bottom</span>
