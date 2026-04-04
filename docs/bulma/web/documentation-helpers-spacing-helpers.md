# Source: https://bulma.io/documentation/helpers/spacing-helpers/

Title: Spacing helpers

URL Source: https://bulma.io/documentation/helpers/spacing-helpers/

Markdown Content:
Bulma provides **margin**`m*` and **padding**`p*` helpers in all **directions**:

*   `*t` for **top**
*   `*r` for **right**
*   `*b` for **bottom**
*   `*l` for **left**
*   `*x` horizontally for both **left** and **right**
*   `*y` vertically for both **top** and **bottom**

You need to **combine** a margin/padding prefix with a direction suffix. For example:

*   for a `margin-top`, use `mt-*`
*   for a `padding-bottom`, use `pb-*`
*    for both `margin-left` and `margin-right`, use `mx-*`

Each of these `property-direction`**combinations** needs to be appended with one of **6 value suffixes**:

| Suffix | Value |
| --- | --- |
| `*-0` | `0` |
| `*-1` | `0.25rem` |
| `*-2` | `0.5rem` |
| `*-3` | `0.75rem` |
| `*-4` | `1rem` |
| `*-5` | `1.5rem` |
| `*-6` | `3rem` |

### List of all spacing helpers [#](https://bulma.io/documentation/helpers/spacing-helpers/#list-of-all-spacing-helpers)

There are **112 spacing helpers** to choose from:

| Property | Shortcut | Classes ↓ |
| --- | --- | --- |
| Values → | `0` | `0.25rem` | `0.5rem` | `0.75rem` | `1rem` | `1.5rem` | `3rem` | `auto` |
| `margin` | `m` | `m-0` | `m-1` | `m-2` | `m-3` | `m-4` | `m-5` | `m-6` | `m-auto` |
| `margin-top` | `mt` | `mt-0` | `mt-1` | `mt-2` | `mt-3` | `mt-4` | `mt-5` | `mt-6` | `mt-auto` |
| `margin-right` | `mr` | `mr-0` | `mr-1` | `mr-2` | `mr-3` | `mr-4` | `mr-5` | `mr-6` | `mr-auto` |
| `margin-bottom` | `mb` | `mb-0` | `mb-1` | `mb-2` | `mb-3` | `mb-4` | `mb-5` | `mb-6` | `mb-auto` |
| `margin-left` | `ml` | `ml-0` | `ml-1` | `ml-2` | `ml-3` | `ml-4` | `ml-5` | `ml-6` | `ml-auto` |
| `margin-left`and `margin-right` | `mx` | `mx-0` | `mx-1` | `mx-2` | `mx-3` | `mx-4` | `mx-5` | `mx-6` | `mx-auto` |
| `margin-top`and `margin-bottom` | `my` | `my-0` | `my-1` | `my-2` | `my-3` | `my-4` | `my-5` | `my-6` | `my-auto` |
| `padding` | `p` | `p-0` | `p-1` | `p-2` | `p-3` | `p-4` | `p-5` | `p-6` | `p-auto` |
| `padding-top` | `pt` | `pt-0` | `pt-1` | `pt-2` | `pt-3` | `pt-4` | `pt-5` | `pt-6` | `pt-auto` |
| `padding-right` | `pr` | `pr-0` | `pr-1` | `pr-2` | `pr-3` | `pr-4` | `pr-5` | `pr-6` | `pr-auto` |
| `padding-bottom` | `pb` | `pb-0` | `pb-1` | `pb-2` | `pb-3` | `pb-4` | `pb-5` | `pb-6` | `pb-auto` |
| `padding-left` | `pl` | `pl-0` | `pl-1` | `pl-2` | `pl-3` | `pl-4` | `pl-5` | `pl-6` | `pl-auto` |
| `padding-left`and `padding-right` | `px` | `px-0` | `px-1` | `px-2` | `px-3` | `px-4` | `px-5` | `px-6` | `px-auto` |
| `padding-top`and `padding-bottom` | `py` | `py-0` | `py-1` | `py-2` | `py-3` | `py-4` | `py-5` | `py-6` | `py-auto` |

To use these classes, simply append them to any HTML element:

```
<!-- Adds 1rem of margin at the bottom -->
<p class="mb-4">Margin bottom</p>

<!-- Adds 0.25rem of padding on the left and the right -->
<p class="px-1">Horizontal padding</p>

<!-- Removes the margin on the right and adds 0.75rem padding at the top -->
<p class="mr-0 pt-3">Both</p>
```

### Configuration [#](https://bulma.io/documentation/helpers/spacing-helpers/#configuration)

Because every developer has their own preferences, and to satisfy Bulma's customization features, it's possible to specify your own **class name shortcuts** as well as the **spacing values**.

For example, if you wanted:

*   **margin** to be abbreviated to `mg`
*   **padding** to be totally **excluded**
*   **horizontal** to be abbreviated to `h`
*   **vertical** to be excluded as well
*    and to only have 3 values: **"small"** at `10px`, **"medium"** at `30px`, and **"large"** at `60px`

You can simplify the CSS output by customizing these **SCSS variables**:

```
$spacing-shortcuts: ("margin": "mg"); $spacing-horizontal:
"h"; $spacing-vertical: null; $spacing-values: ("small": 10px, "medium": 30px,
"large": 60px);
```

| Property | Shortcut | Classes ↓ |
| --- | --- | --- |
| Values → | `10px` | `30px` | `60px` |
| `margin` | `mg` | `mg-small` | `mg-medium` | `mg-large` |
| `margin-top` | `mgt` | `mgt-small` | `mgt-medium` | `mgt-large` |
| `margin-right` | `mgr` | `mgr-small` | `mgr-medium` | `mgr-large` |
| `margin-bottom` | `mgb` | `mgb-small` | `mgb-medium` | `mgb-large` |
| `margin-left` | `mgl` | `mgl-small` | `mgl-medium` | `mgl-large` |
| `margin-left`and `margin-right` | `mgh` | `mgh-small` | `mgh-medium` | `mgh-large` |

By customizing the output, you've narrowed down the list of spacing helpers from 112 to only **18**.
