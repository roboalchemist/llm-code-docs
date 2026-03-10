# Source: https://developers.webflow.com/flowkit/getting-started/units.mdx

***

title: Units
slug: getting-started/units
description: >-
Units are a collection of values that determine the size of a website and its
parts.
hidden: null
'og:title': Flowkit - Units
'og:description': >-
Units are a collection of values that determine the size of a website and its
parts.
------

## Overview

The primary unit of the framework is `REM`. It's used for sizing, spacing, and typography to ensure flexibility and accessibility. Other units are also used based on the use-case. Here is the list of all the units used:

| Category       | Unit      | Primary Uses                                                    | Description                                                                                                                          |
| -------------- | --------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Responsive** | `REM`     | <ul><li>Typography</li><li>Spacing</li><li>Components</li></ul> | Scales with root font size (default: 16px)                                                                                           |
|                | `EM`      | <ul><li>Button padding</li><li>Icon sizes</li></ul>             | Scales with parent element's font size                                                                                               |
| **Layout**     | `%`       | <ul><li>Container widths</li><li>Max-widths</li></ul>           | Relative to parent element's size                                                                                                    |
|                | `FR`      | <ul><li>Grid columns</li><li>Grid layouts</li></ul>             | Distributes available space in CSS Grid                                                                                              |
| **Viewport**   | `VH`/`VW` | <ul><li>Hero sections</li><li>Full-height layouts</li></ul>     | Relative to viewport dimensions                                                                                                      |
|                | `DVH`     | <ul><li>Mobile layouts</li><li>Dynamic heights</li></ul>        | Adjusts for mobile browser chrome                                                                                                    |
| **Special**    | `PX`      | <ul><li>Borders</li><li>Shadows</li></ul>                       | Fixed-size elements (use sparingly)                                                                                                  |
|                | `CQW`     | Fluid typography                                                | Character-width-based unit for responsive typography. Requires <span class="sg-selector sg-class">heading-responsive\_wrapper</span> |

***

## Why do we use REM?

`REM` (short for "root em") is the foundation of our unit system.

* It scales based on the root `<html>` font size (by default `16px`)
* It makes spacing and typography fluid-responsive and consistent
* It improves accessibility and user control

If `1rem = 16px`, then:

| REM      | Pixels |
| -------- | ------ |
| `0.5rem` | 8px    |
| `1rem`   | 16px   |
| `2rem`   | 32px   |

You can override the base by embedding a rule in your Webflow project custom code:

```html
<style>
  html { font-size: 20px; } /* 1rem now equals 20px */
</style>
```

<Note title="Pro Tip">
  To see the font size change reflected in the Webflow Designer, it's best to place this code inside a [Code embed element](https://help.webflow.com/hc/en-us/articles/33961332238611-Custom-code-embed) within a reusable Component. This ensures the override is included on every page of your project.
</Note>

***

## REM in Webflow

Webflow supports REM-based math directly in input fields. You can type formulas like 64/16 hit `↵` and get a result of 4. In Webflow `PX` is the default unit, you can switch to REM by clicking on units indicator and select REM, or simply add 64/16REM, hit `↵` and get `4 REM`.

<img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/bedb118254d8d8b2403c519113ea0c1937913b6e4390652ae9b6562c10be8f7e/products/flowkit/pages/v2/units/flowkit-calc.gif" alt="Style Guide" />
