# Source: https://developers.webflow.com/flowkit/foundation/spacing.mdx

***

title: Spacing
slug: foundation/spacing
description: >-
How spacing variables and gap utilities are structured in the Flowkit
Framework.
hidden: null
'og:title': Flowkit - Spacing
'og:description': >-
How spacing variables and gap utilities are structured in the Flowkit
Framework.
----------

Foundational predefined REM-based set of variables called <span class="sg-selector sg-var">Spacing</span> are used for margins, paddings, and gaps of components. This ensures consistent rhythm and layout behavior across the entire system.

***

### Size Variables

All the base spacing values are defined using a simple <span class="sg-selector sg-var">`value`x</span> naming convention. You can think of `x` as a multiplier of the base unit (1rem = 16px).

| Variable                                      | REM Value | Preview |
| --------------------------------------------- | --------- | ------- |
| <span class="sg-selector sg-var">0.25x</span> | 0.25rem   |         |
| <span class="sg-selector sg-var">0.5x</span>  | 0.5rem    |         |
| <span class="sg-selector sg-var">0.75x</span> | 0.75rem   |         |
| <span class="sg-selector sg-var">1x</span>    | 1rem      |         |
| <span class="sg-selector sg-var">1.25x</span> | 1.25rem   |         |
| <span class="sg-selector sg-var">1.5x</span>  | 1.5rem    |         |
| <span class="sg-selector sg-var">1.75x</span> | 1.75rem   |         |
| <span class="sg-selector sg-var">2x</span>    | 2rem      |         |
| <span class="sg-selector sg-var">3x</span>    | 3rem      |         |
| <span class="sg-selector sg-var">4x</span>    | 4rem      |         |
| <span class="sg-selector sg-var">5x</span>    | 5rem      |         |
| <span class="sg-selector sg-var">6x</span>    | 6rem      |         |
| <span class="sg-selector sg-var">7x</span>    | 7rem      |         |
| <span class="sg-selector sg-var">8x</span>    | 8rem      |         |

<Note title="Note">
  Variables can be remapped. For example, `0.25x` might be set to `0.5rem` based on your project's scale. To learn more about how `rem` works and why we use it, see the <a href="/flowkit/getting-started/units">Units page</a>.
</Note>

***

## Gap Variables

Used in flex and grid layouts. These use t-shirt sizing for consistent spacing across UI elements.

<ul>
  * <span class="sg-selector sg-var">
      gap-xsmall
    </span>
  * <span class="sg-selector sg-var">
      gap-small
    </span>
  * <span class="sg-selector sg-var">
      gap-medium
    </span>
  * <span class="sg-selector sg-var">
      gap-large
    </span>
  * <span class="sg-selector sg-var">
      gap-xlarge
    </span>
  * <span class="sg-selector sg-var">
      gap-xxlarge
    </span>
</ul>

***

## Utility Class Examples

Example of classes that apply spacing using the same variables as above for consistency:

* <span class="sg-selector sg-class">
    icon
  </span>
  <span class="sg-selector sg-class">
    is-small
  </span>
* <span class="sg-selector sg-class">
    flex_horizontal
  </span>
  <span class="sg-selector sg-class">
    gap-small
  </span>
* <span class="sg-selector sg-class">
    padding-bottom_small
  </span>
* <span class="sg-selector sg-class">
    margin-top_small
  </span>
