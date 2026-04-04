# Source: https://bulma.io/documentation/helpers/typography-helpers/

Title: Typography helpers

URL Source: https://bulma.io/documentation/helpers/typography-helpers/

Markdown Content:
### Size [#](https://bulma.io/documentation/helpers/typography-helpers/#size)

There are **7 sizes** to choose from:

| Class | Font-size | Size |
| --- | --- | --- |
| `is-size-1` | `3rem` | Example |
| `is-size-2` | `2.5rem` | Example |
| `is-size-3` | `2rem` | Example |
| `is-size-4` | `1.5rem` | Example |
| `is-size-5` | `1.25rem` | Example |
| `is-size-6` | `1rem` | Example |
| `is-size-7` | `0.75rem` | Example |

### Responsive size [#](https://bulma.io/documentation/helpers/typography-helpers/#responsive-size)

You can choose a **specific** size for _each_ viewport width. You simply need to append the **viewport width** to the size modifier.

For example, here are the modifiers for `$size-1`:

| Class | Mobile Up to `768px` | Tablet Between `769px` and `1023px` | Desktop Between `1024px` and `1215px` | Widescreen Between `1216px` and `1407px` | FullHD `1408px` and above |
| --- | --- | --- | --- | --- | --- |
| `is-size-1-mobile` |  | unchanged | unchanged | unchanged | unchanged |
| `is-size-1-touch` |  |  | unchanged | unchanged | unchanged |
| `is-size-1-tablet` | unchanged |  |  |  |  |
| `is-size-1-desktop` | unchanged | unchanged |  |  |  |
| `is-size-1-widescreen` | unchanged | unchanged | unchanged |  |  |
| `is-size-1-fullhd` | unchanged | unchanged | unchanged | unchanged |  |

You can use the same logic for each of the **7 sizes**.

### Alignment [#](https://bulma.io/documentation/helpers/typography-helpers/#alignment)

You can align the text with the use of one of **4 alignment helpers**:

| Class | Alignment |
| --- | --- |
| `has-text-centered` | Makes the text **centered** |
| `has-text-justified` | Makes the text **justified** |
| `has-text-left` | Makes the text aligned to the **left** |
| `has-text-right` | Makes the text aligned to the **right** |

### Responsive Alignment [#](https://bulma.io/documentation/helpers/typography-helpers/#responsive-alignment)

You can **align text** differently for each **viewport width**. Simply append the **viewport width** to the alignment modifier.

For example, here are the modifiers for `has-text-left`:

| Class | Mobile Up to `768px` | Tablet Between `769px` and `1023px` | Desktop Between `1024px` and `1215px` | Widescreen Between `1216px` and `1407px` | FullHD `1408px` and above |
| --- | --- | --- | --- | --- | --- |
| `has-text-left-mobile` | left-aligned | unchanged | unchanged | unchanged | unchanged |
| `has-text-left-touch` | left-aligned | left-aligned | unchanged | unchanged | unchanged |
| `has-text-left-tablet-only` | unchanged | left-aligned | unchanged | unchanged | unchanged |
| `has-text-left-tablet` | unchanged | left-aligned | left-aligned | left-aligned | left-aligned |
| `has-text-left-desktop-only` | unchanged | unchanged | left-aligned | unchanged | unchanged |
| `has-text-left-desktop` | unchanged | unchanged | left-aligned | left-aligned | left-aligned |
| `has-text-left-widescreen-only` | unchanged | unchanged | unchanged | left-aligned | unchanged |
| `has-text-left-widescreen` | unchanged | unchanged | unchanged | left-aligned | left-aligned |
| `has-text-left-fullhd` | unchanged | unchanged | unchanged | unchanged | left-aligned |

You can use the same logic for each of the **4 alignments**.

### Text transformation [#](https://bulma.io/documentation/helpers/typography-helpers/#text-transformation)

You can transform the text with the use of one of **4 text transformation helpers**:

| Class | Transformation |
| --- | --- |
| `is-capitalized` | Transforms **the first character** of each word to **Uppercase** |
| `is-lowercase` | Transforms **all characters** to **lowercase** |
| `is-uppercase` | Transforms **all characters** to **UPPERCASE** |
| `is-italic` | Transforms **all characters** to **italic** |
| `is-underlined` | **Underlines** the text |

### Text weight [#](https://bulma.io/documentation/helpers/typography-helpers/#text-weight)

You can transform the text weight with the use of one of **6 text weight helpers**:

| Class | Weight |
| --- | --- |
| `has-text-weight-light` | Transforms text weight to light |
| `has-text-weight-normal` | Transforms text weight to normal |
| `has-text-weight-medium` | Transforms text weight to medium |
| `has-text-weight-semibold` | Transforms text weight to semibold |
| `has-text-weight-bold` | Transforms text weight to bold |
| `has-text-weight-extrabold` | Transforms text weight to extrabold |

### Font family [#](https://bulma.io/documentation/helpers/typography-helpers/#font-family)

You can change the font family with the use of one of **5 font family helpers**:

| Class | Family |
| --- | --- |
| `is-family-sans-serif` | Sets font family to `$family-sans-serif` |
| `is-family-monospace` | Sets font family to `$family-monospace` |
| `is-family-primary` | Sets font family to `$family-primary` |
| `is-family-secondary` | Sets font family to `$family-secondary` |
| `is-family-code` | Sets font family to `$family-code` |
