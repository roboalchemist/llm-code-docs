# Source: https://developers.webflow.com/flowkit/v1.0.0/structure/grid.mdx

***

title: Grid layout
slug: structure/grid
description: Grid layout system in Webflow CSS Framework using responsive combo classes.
hidden: null
'og:title': Flowkit - Grid
'og:description': Grid layout system in Webflow CSS Framework using responsive combo classes.
---------------------------------------------------------------------------------------------

The base class <span class="sg-selector sg-class">Grid Layout</span> defines the element as a grid. By default, it creates a 2-column grid layout with no spacing.

<span class="sg-selector sg-class">Grid Layout</span> can be extended with various combo class modifiers that adjust the layout's spacing, column count, alignment, and responsiveness. You can combine these modifiers to configure the grid layout to your needs.

Style selector structure:

<span class="sg-selector sg-class">
  Grid Layout
</span>

<span class="sg-selector">
  (Optional) Responsive Column Modifier
</span>

<span class="sg-selector">
  (Optional) Spacing Modifier
</span>

<span class="sg-selector">
  (Optional) Alignment Modifier
</span>

Check examples how to mix combo-classes:

<span class="sg-selector sg-class">
  Grid Layout
</span>

<span class="sg-selector sg-class">
  Desktop 9 Column
</span>

<span class="sg-selector sg-class">
  Tablet 3 Column
</span>

<span class="sg-selector sg-class">
  Mobile Landscape 1 Column
</span>

<span class="sg-selector sg-class">
  Grid Gap MD
</span>

<span class="sg-selector sg-class">
  X Center
</span>

<img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/d4043d660edf0b92accb25f3ddf13e789f5f9b4ff148c45b6c0d7c6091eba8df/products/flowkit/pages/v1/grid/flowkit_grids.webp" alt="Grid" />

***

## Spacing Modifiers

Spacing is following t-shirt size coding with 2-letter abbreviations (e.g. `SM`, `MD`, `XL`).

Style selector structure:
<span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">Grid Gap `Size`</span>

Options: `XXS`, `XS`, `SM`, `MD`, `LG`, `XL`, `XXL`

Example: <span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">Grid Gap MD</span>

***

## Alignment Modifiers

These modifiers set alignment for all child elements inside the grid.

Style selector structure:
<span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">`X or Y` `Position`</span>

Options: `X Left`, `X Center`, `X Right`, `Y Top`, `Y Center`, `Y Bottom`

Example: <span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">X Center</span> <span class="sg-selector sg-class">Y Bottom</span>

***

## Responsive Column Modifiers

You can define unique behavior for every breakpoint by adding the combo class for the breakpoint you want to target.

Style selector structure:
<span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">`Breakpoint` `Count` Column Grid</span>

Options:

| Breakpoint         | Count      |
| ------------------ | ---------- |
| `Desktop`          | `1` – `12` |
| `Tablet`           | `1` – `6`  |
| `Mobile Landscape` | `1` – `4`  |
| `Mobile Portrait`  | `1` – `4`  |

Example: <span class="sg-selector sg-class">Grid Layout</span> <span class="sg-selector sg-class">Tablet 3 Column Grid</span>
