# Source: https://developers.webflow.com/designer/reference/style-properties.mdx

***

title: Style Properties
slug: designer/reference/style-properties
description: Reference guide for CSS style properties supported by the Webflow Designer API
hidden: false
'og:title': 'Webflow Designer API: Style Properties'
'og:description': Reference guide for CSS style properties supported by the Webflow Designer API
------------------------------------------------------------------------------------------------

Style properties define the visual appearance and layout of web page elements. Using the Webflow Designer API, you can programmatically set these CSS properties to control design aspects like colors, typography, spacing, and positioning.

## How to use style properties

The Designer API accepts style properties as a `PropertyMap` object. A `PropertyMap` is a key-value collection where keys are CSS property names and values are their corresponding settings.

```typescript title="PropertyMap Example"
{
    "color": "#ff5733",
    "font-size": "16px",
    "font-weight": "bold",
    "text-align": "center",
    "background-color": "#e0e0e0",
    "border-radius": "5px",
    "border-color": "#000000",
}
```

## Supported properties

The following properties are organized by functional category for reference. Each property accepts either a string value or, where noted, a Webflow variable reference.

### Layout & positioning

| Property          | Type                                        | Example        |
| ----------------- | ------------------------------------------- | -------------- |
| `display`         | string                                      | `flex`         |
| `position`        | string                                      | `absolute`     |
| `top`             | string, SizeVariable, or PercentageVariable | `100px`        |
| `right`           | string, SizeVariable, or PercentageVariable | `0px`          |
| `bottom`          | string, SizeVariable, or PercentageVariable | `0`            |
| `left`            | string, SizeVariable, or PercentageVariable | `50px`         |
| `inset`           | string                                      | `10px 20px`    |
| `width`           | string, SizeVariable, or PercentageVariable | `50%`          |
| `height`          | string, SizeVariable, or PercentageVariable | `100vh`        |
| `min-width`       | string, SizeVariable, or PercentageVariable | `60px`         |
| `max-width`       | string, SizeVariable, or PercentageVariable | `80%`          |
| `min-height`      | string, SizeVariable, or PercentageVariable | `100px`        |
| `max-height`      | string, SizeVariable, or PercentageVariable | `200px`        |
| `aspect-ratio`    | string                                      | `16 / 9`       |
| `box-sizing`      | string                                      | `border-box`   |
| `overflow`        | string                                      | `hidden`       |
| `overflow-x`      | string                                      | `auto`         |
| `overflow-y`      | string                                      | `scroll`       |
| `object-fit`      | string                                      | `cover`        |
| `object-position` | string                                      | `center top`   |
| `float`           | string                                      | `right`        |
| `clear`           | string                                      | `both`         |
| `visibility`      | string                                      | `hidden`       |
| `z-index`         | string or NumberVariable                    | `10`           |
| `contain`         | string                                      | `layout style` |
| `isolation`       | string                                      | `isolate`      |
| `zoom`            | string                                      | `1.5`          |

### Flex layout

| Property          | Type                                        | Example         |
| ----------------- | ------------------------------------------- | --------------- |
| `flex`            | string                                      | `1 1 auto`      |
| `flex-direction`  | string                                      | `row`           |
| `flex-wrap`       | string                                      | `wrap`          |
| `flex-flow`       | string                                      | `row wrap`      |
| `flex-basis`      | string, SizeVariable, or PercentageVariable | `auto`          |
| `flex-grow`       | string or NumberVariable                    | `1`             |
| `flex-shrink`     | string or NumberVariable                    | `1`             |
| `justify-content` | string                                      | `space-between` |
| `align-items`     | string                                      | `flex-start`    |
| `align-content`   | string                                      | `center`        |
| `align-self`      | string                                      | `stretch`       |
| `order`           | string                                      | `2`             |
| `gap`             | string                                      | `10px 20px`     |
| `place-content`   | string                                      | `center start`  |
| `place-items`     | string                                      | `center`        |
| `place-self`      | string                                      | `center`        |

### Grid

| Property                | Type                                        | Example               |
| ----------------------- | ------------------------------------------- | --------------------- |
| `grid`                  | string                                      | `auto / 1fr 1fr`      |
| `grid-template-columns` | string                                      | `50px 100px`          |
| `grid-template-rows`    | string                                      | `auto`                |
| `grid-template-areas`   | string                                      | `'header header'`     |
| `grid-template`         | string                                      | `auto / 1fr 1fr`      |
| `grid-column`           | string                                      | `1 / span 2`          |
| `grid-column-start`     | string                                      | `1`                   |
| `grid-column-end`       | string                                      | `span 2`              |
| `grid-row`              | string                                      | `1 / 3`               |
| `grid-row-start`        | string                                      | `1`                   |
| `grid-row-end`          | string                                      | `3`                   |
| `grid-area`             | string                                      | `header`              |
| `grid-auto-columns`     | string                                      | `minmax(100px, auto)` |
| `grid-auto-rows`        | string                                      | `auto`                |
| `grid-auto-flow`        | string                                      | `row dense`           |
| `gap`                   | string                                      | `10px 20px`           |
| `grid-gap`              | string                                      | `10px 20px`           |
| `grid-column-gap`       | string, SizeVariable, or PercentageVariable | `10px`                |
| `grid-row-gap`          | string, SizeVariable, or PercentageVariable | `20px`                |
| `row-gap`               | string or SizeVariable                      | `20px`                |
| `column-gap`            | string or SizeVariable                      | `20px`                |

### Typography

| Property                    | Type                                                        | Example                      |
| --------------------------- | ----------------------------------------------------------- | ---------------------------- |
| `font`                      | string                                                      | `italic bold 16px/1.5 Arial` |
| `font-family`               | string or FontFamilyVariable                                | `Arial, sans-serif`          |
| `font-size`                 | string, SizeVariable, or PercentageVariable                 | `16px`                       |
| `font-weight`               | string or NumberVariable                                    | `bold`                       |
| `font-style`                | string                                                      | `italic`                     |
| `font-variant`              | string                                                      | `small-caps`                 |
| `font-stretch`              | string                                                      | `condensed`                  |
| `font-feature-settings`     | string                                                      | `'liga' 1`                   |
| `font-variation-settings`   | string                                                      | `'wght' 400`                 |
| `line-height`               | string, SizeVariable, NumberVariable, or PercentageVariable | `1.5`                        |
| `text-align`                | string                                                      | `justify`                    |
| `text-transform`            | string                                                      | `uppercase`                  |
| `text-decoration`           | string                                                      | `underline`                  |
| `text-decoration-thickness` | string                                                      | `2px`                        |
| `text-underline-offset`     | string                                                      | `3px`                        |
| `text-wrap`                 | string                                                      | `balance`                    |
| `letter-spacing`            | string or SizeVariable                                      | `0.5em`                      |
| `word-spacing`              | string or SizeVariable                                      | `5px`                        |
| `white-space`               | string                                                      | `nowrap`                     |
| `word-break`                | string                                                      | `break-word`                 |
| `overflow-wrap`             | string                                                      | `break-word`                 |
| `hyphens`                   | string                                                      | `auto`                       |
| `color`                     | string or ColorVariable                                     | `#FF9800`                    |
| `tab-size`                  | string or SizeVariable                                      | `4`                          |
| `-webkit-line-clamp`        | string                                                      | `3`                          |

### Colors & backgrounds

| Property                | Type                    | Example                            |
| ----------------------- | ----------------------- | ---------------------------------- |
| `background`            | string                  | `#e0e0e0 url('img.jpg') no-repeat` |
| `background-color`      | string or ColorVariable | `#e0e0e0`                          |
| `background-image`      | string or ColorVariable | `url('image.jpg')`                 |
| `background-size`       | string                  | `cover`                            |
| `background-position`   | string                  | `top right`                        |
| `background-repeat`     | string                  | `repeat-x`                         |
| `background-attachment` | string                  | `fixed`                            |
| `background-clip`       | string                  | `border-box`                       |
| `background-origin`     | string                  | `padding-box`                      |
| `background-blend-mode` | string                  | `multiply`                         |
| `accent-color`          | string or ColorVariable | `#ff5733`                          |
| `caret-color`           | string or ColorVariable | `blue`                             |
| `color-scheme`          | string                  | `light dark`                       |

### Borders

| Property                     | Type                                        | Example           |
| ---------------------------- | ------------------------------------------- | ----------------- |
| `border`                     | string                                      | `1px solid black` |
| `border-width`               | string or SizeVariable                      | `2px`             |
| `border-style`               | string                                      | `solid`           |
| `border-color`               | string or ColorVariable                     | `#000000`         |
| `border-radius`              | string, SizeVariable, or PercentageVariable | `8px`             |
| `border-spacing`             | string                                      | `5px 10px`        |
| `border-top-width`           | string or SizeVariable                      | `2px`             |
| `border-top-style`           | string                                      | `ridge`           |
| `border-top-color`           | string or ColorVariable                     | `#3F51B5`         |
| `border-top-left-radius`     | string, SizeVariable, or PercentageVariable | `20px`            |
| `border-top-right-radius`    | string, SizeVariable, or PercentageVariable | `20px`            |
| `border-bottom-width`        | string or SizeVariable                      | `1px`             |
| `border-bottom-style`        | string                                      | `groove`          |
| `border-bottom-color`        | string or ColorVariable                     | `#f44336`         |
| `border-bottom-left-radius`  | string, SizeVariable, or PercentageVariable | `4px`             |
| `border-bottom-right-radius` | string, SizeVariable, or PercentageVariable | `4px`             |
| `border-left-width`          | string or SizeVariable                      | `2px`             |
| `border-left-style`          | string                                      | `dashed`          |
| `border-left-color`          | string or ColorVariable                     | `#9C27B0`         |
| `border-right-width`         | string or SizeVariable                      | `1px`             |
| `border-right-style`         | string                                      | `double`          |
| `border-right-color`         | string or ColorVariable                     | `#FFEB3B`         |

### Spacing

| Property         | Type                                        | Example     |
| ---------------- | ------------------------------------------- | ----------- |
| `margin`         | string                                      | `10px 20px` |
| `margin-top`     | string, SizeVariable, or PercentageVariable | `10px`      |
| `margin-right`   | string, SizeVariable, or PercentageVariable | `30px`      |
| `margin-bottom`  | string, SizeVariable, or PercentageVariable | `20px`      |
| `margin-left`    | string, SizeVariable, or PercentageVariable | `30px`      |
| `margin-block`   | string                                      | `10px`      |
| `margin-inline`  | string                                      | `10px`      |
| `padding`        | string                                      | `10px 20px` |
| `padding-top`    | string, SizeVariable, or PercentageVariable | `10px`      |
| `padding-right`  | string, SizeVariable, or PercentageVariable | `10px`      |
| `padding-bottom` | string, SizeVariable, or PercentageVariable | `15px`      |
| `padding-left`   | string, SizeVariable, or PercentageVariable | `10px`      |
| `padding-block`  | string                                      | `10px`      |
| `padding-inline` | string                                      | `10px`      |
| `gap`            | string                                      | `10px 20px` |
| `row-gap`        | string or SizeVariable                      | `20px`      |
| `column-gap`     | string or SizeVariable                      | `20px`      |

### Effects & transforms

| Property              | Type                                          | Example              |
| --------------------- | --------------------------------------------- | -------------------- |
| `box-shadow`          | string or SizeVariable                        | `10px 5px 5px black` |
| `text-shadow`         | string or SizeVariable                        | `2px 2px 5px grey`   |
| `filter`              | string or SizeVariable                        | `blur(2px)`          |
| `backdrop-filter`     | string or SizeVariable                        | `blur(5px)`          |
| `transform`           | string                                        | `rotate(45deg)`      |
| `transform-origin`    | string                                        | `top left`           |
| `transform-style`     | string                                        | `preserve-3d`        |
| `rotate`              | string                                        | `45deg`              |
| `scale`               | string                                        | `1.2`                |
| `translate`           | string or SizeVariable                        | `10px, 20px`         |
| `perspective`         | string or SizeVariable                        | `500px`              |
| `perspective-origin`  | string                                        | `50% 50%`            |
| `backface-visibility` | string                                        | `hidden`             |
| `opacity`             | string, NumberVariable, or PercentageVariable | `0.5`                |
| `mix-blend-mode`      | string                                        | `multiply`           |
| `clip-path`           | string                                        | `circle(50%)`        |
| `will-change`         | string                                        | `transform`          |

### Transitions & animations

| Property                     | Type   | Example                     |
| ---------------------------- | ------ | --------------------------- |
| `transition`                 | string | `opacity 300ms ease-in-out` |
| `transition-property`        | string | `opacity`                   |
| `transition-duration`        | string | `300ms`                     |
| `transition-timing-function` | string | `ease-in-out`               |
| `transition-delay`           | string | `0.5s`                      |
| `transition-behavior`        | string | `allow-discrete`            |
| `animation`                  | string | `slidein 1s ease-in-out`    |
| `animation-name`             | string | `slidein`                   |
| `animation-duration`         | string | `1s`                        |
| `animation-timing-function`  | string | `ease-in-out`               |
| `animation-delay`            | string | `2s`                        |
| `animation-iteration-count`  | string | `infinite`                  |
| `animation-direction`        | string | `alternate`                 |
| `animation-fill-mode`        | string | `forwards`                  |
| `animation-play-state`       | string | `paused`                    |
| `animation-composition`      | string | `replace`                   |
| `animation-timeline`         | string | `auto`                      |

### Scroll snap

| Property                | Type   | Example       |
| ----------------------- | ------ | ------------- |
| `scroll-behavior`       | string | `smooth`      |
| `scroll-snap-type`      | string | `y mandatory` |
| `scroll-snap-align`     | string | `start`       |
| `scroll-snap-stop`      | string | `normal`      |
| `scroll-margin`         | string | `10px`        |
| `scroll-margin-top`     | string | `10px`        |
| `scroll-margin-bottom`  | string | `10px`        |
| `scroll-margin-left`    | string | `10px`        |
| `scroll-margin-right`   | string | `10px`        |
| `scroll-padding`        | string | `20px`        |
| `scroll-padding-top`    | string | `20px`        |
| `scroll-padding-bottom` | string | `20px`        |
| `scroll-padding-left`   | string | `20px`        |
| `scroll-padding-right`  | string | `20px`        |

### Scrollbar

| Property           | Type   | Example  |
| ------------------ | ------ | -------- |
| `scrollbar-color`  | string | `dark`   |
| `scrollbar-gutter` | string | `stable` |
| `scrollbar-width`  | string | `thin`   |

### Container queries

| Property                 | Type   | Example                 |
| ------------------------ | ------ | ----------------------- |
| `container`              | string | `sidebar / inline-size` |
| `container-name`         | string | `sidebar`               |
| `container-type`         | string | `inline-size`           |
| `contain`                | string | `layout style`          |
| `contain-intrinsic-size` | string | `200px 300px`           |
| `content-visibility`     | string | `auto`                  |

### Masking

| Property             | Type   | Example                     |
| -------------------- | ------ | --------------------------- |
| `mask`               | string | `url('mask.png') no-repeat` |
| `mask-image`         | string | `url('mask.png')`           |
| `mask-mode`          | string | `luminance`                 |
| `mask-position`      | string | `center`                    |
| `mask-repeat`        | string | `no-repeat`                 |
| `mask-size`          | string | `cover`                     |
| `mask-clip`          | string | `border-box`                |
| `mask-composite`     | string | `add`                       |
| `mask-origin`        | string | `border-box`                |
| `mask-type`          | string | `luminance`                 |
| `mask-border`        | string | `url('mask.png') 30`        |
| `mask-border-source` | string | `url('mask.png')`           |
| `mask-border-slice`  | string | `30%`                       |
| `mask-border-width`  | string | `10px`                      |
| `mask-border-outset` | string | `5px`                       |
| `mask-border-repeat` | string | `stretch`                   |
| `mask-border-mode`   | string | `luminance`                 |

### User interaction

| Property         | Type   | Example     |
| ---------------- | ------ | ----------- |
| `cursor`         | string | `pointer`   |
| `pointer-events` | string | `none`      |
| `touch-action`   | string | `pan-right` |
| `user-select`    | string | `none`      |
| `resize`         | string | `both`      |
| `appearance`     | string | `none`      |

### Complete property reference

For a comprehensive list of all supported properties, see the [W3Schools CSS Properties reference](https://www.w3schools.com/cssref/index.php).

{/* <!-- vale off --> */}

| Style Property                | Value                                                       | Example                            |
| ----------------------------- | ----------------------------------------------------------- | ---------------------------------- |
| accent-color                  | string or ColorVariable                                     | `#ff5733`                          |
| align-content                 | string                                                      | `center`                           |
| align-items                   | string                                                      | `flex-start`                       |
| align-self                    | string                                                      | `stretch`                          |
| align-tracks                  | string                                                      | `normal`                           |
| all                           | string                                                      | `unset`                            |
| anchor-name                   | string                                                      | `--my-anchor`                      |
| anchor-scope                  | string                                                      | `--my-anchor`                      |
| animation                     | string                                                      | `slidein 1s ease-in-out`           |
| animation-composition         | string                                                      | `replace`                          |
| animation-delay               | string                                                      | `2s`                               |
| animation-direction           | string                                                      | `alternate`                        |
| animation-duration            | string                                                      | `1s`                               |
| animation-fill-mode           | string                                                      | `forwards`                         |
| animation-iteration-count     | string                                                      | `infinite`                         |
| animation-name                | string                                                      | `slidein`                          |
| animation-play-state          | string                                                      | `paused`                           |
| animation-range               | string                                                      | `normal`                           |
| animation-range-end           | string                                                      | `normal`                           |
| animation-range-start         | string                                                      | `normal`                           |
| animation-timeline            | string                                                      | `auto`                             |
| animation-timing-function     | string                                                      | `ease-in-out`                      |
| appearance                    | string                                                      | `none`                             |
| aspect-ratio                  | string                                                      | `16 / 9`                           |
| azimuth                       | string                                                      | `center`                           |
| backdrop-filter               | string or SizeVariable                                      | `blur(5px)`                        |
| backface-visibility           | string                                                      | `hidden`                           |
| background                    | string                                                      | `#e0e0e0 url('img.jpg') no-repeat` |
| background-attachment         | string                                                      | `fixed`                            |
| background-blend-mode         | string                                                      | `multiply`                         |
| background-clip               | string                                                      | `border-box`                       |
| background-color              | string or ColorVariable                                     | `#e0e0e0`                          |
| background-image              | string or ColorVariable                                     | `url('image.jpg')`                 |
| background-origin             | string                                                      | `padding-box`                      |
| background-position           | string                                                      | `top right`                        |
| background-position-x         | string or SizeVariable                                      | `50%`                              |
| background-position-y         | string or SizeVariable                                      | `50%`                              |
| background-repeat             | string                                                      | `repeat-x`                         |
| background-size               | string                                                      | `cover`                            |
| block-size                    | string or SizeVariable                                      | `100px`                            |
| border                        | string                                                      | `1px solid black`                  |
| border-block                  | string                                                      | `1px solid black`                  |
| border-block-color            | string                                                      | `#000000`                          |
| border-block-end              | string                                                      | `1px solid black`                  |
| border-block-end-color        | string or ColorVariable                                     | `#000000`                          |
| border-block-end-style        | string                                                      | `dotted`                           |
| border-block-end-width        | string or SizeVariable                                      | `3px`                              |
| border-block-start            | string                                                      | `1px solid black`                  |
| border-block-start-color      | string or ColorVariable                                     | `#333333`                          |
| border-block-start-style      | string                                                      | `solid`                            |
| border-block-start-width      | string or SizeVariable                                      | `2px`                              |
| border-block-style            | string                                                      | `solid`                            |
| border-block-width            | string                                                      | `1px`                              |
| border-bottom                 | string                                                      | `1px solid black`                  |
| border-bottom-color           | string or ColorVariable                                     | `#f44336`                          |
| border-bottom-left-radius     | string, SizeVariable, or PercentageVariable                 | `4px`                              |
| border-bottom-right-radius    | string, SizeVariable, or PercentageVariable                 | `4px`                              |
| border-bottom-style           | string                                                      | `groove`                           |
| border-bottom-width           | string or SizeVariable                                      | `1px`                              |
| border-collapse               | string                                                      | `collapse`                         |
| border-color                  | string or ColorVariable                                     | `#000000`                          |
| border-end-end-radius         | string or SizeVariable                                      | `10px`                             |
| border-end-start-radius       | string or SizeVariable                                      | `10px`                             |
| border-image                  | string                                                      | `url('border.png') 30 stretch`     |
| border-image-outset           | string or SizeVariable                                      | `5px`                              |
| border-image-repeat           | string                                                      | `stretch`                          |
| border-image-slice            | string                                                      | `30%`                              |
| border-image-source           | string                                                      | `url('border.png')`                |
| border-image-width            | string or SizeVariable                                      | `10px`                             |
| border-inline                 | string                                                      | `1px solid black`                  |
| border-inline-color           | string                                                      | `#000000`                          |
| border-inline-end             | string                                                      | `1px solid black`                  |
| border-inline-end-color       | string or ColorVariable                                     | `#4CAF50`                          |
| border-inline-end-style       | string                                                      | `inset`                            |
| border-inline-end-width       | string or SizeVariable                                      | `4px`                              |
| border-inline-start           | string                                                      | `1px solid black`                  |
| border-inline-start-color     | string or ColorVariable                                     | `#2196F3`                          |
| border-inline-start-style     | string                                                      | `outset`                           |
| border-inline-start-width     | string or SizeVariable                                      | `3px`                              |
| border-inline-style           | string                                                      | `solid`                            |
| border-inline-width           | string                                                      | `1px`                              |
| border-left                   | string                                                      | `1px solid black`                  |
| border-left-color             | string or ColorVariable                                     | `#9C27B0`                          |
| border-left-style             | string                                                      | `dashed`                           |
| border-left-width             | string or SizeVariable                                      | `2px`                              |
| border-radius                 | string, SizeVariable, or PercentageVariable                 | `8px`                              |
| border-right                  | string                                                      | `1px solid black`                  |
| border-right-color            | string or ColorVariable                                     | `#FFEB3B`                          |
| border-right-style            | string                                                      | `double`                           |
| border-right-width            | string or SizeVariable                                      | `1px`                              |
| border-spacing                | string                                                      | `5px 10px`                         |
| border-start-end-radius       | string or SizeVariable                                      | `5px`                              |
| border-start-start-radius     | string or SizeVariable                                      | `5px`                              |
| border-style                  | string                                                      | `solid`                            |
| border-top                    | string                                                      | `1px solid black`                  |
| border-top-color              | string or ColorVariable                                     | `#3F51B5`                          |
| border-top-left-radius        | string, SizeVariable, or PercentageVariable                 | `20px`                             |
| border-top-right-radius       | string, SizeVariable, or PercentageVariable                 | `20px`                             |
| border-top-style              | string                                                      | `ridge`                            |
| border-top-width              | string or SizeVariable                                      | `2px`                              |
| border-width                  | string or SizeVariable                                      | `2px`                              |
| bottom                        | string, SizeVariable, or PercentageVariable                 | `0`                                |
| box-align                     | string                                                      | `center`                           |
| box-decoration-break          | string                                                      | `clone`                            |
| box-direction                 | string                                                      | `normal`                           |
| box-flex                      | string                                                      | `1`                                |
| box-flex-group                | string                                                      | `1`                                |
| box-lines                     | string                                                      | `single`                           |
| box-ordinal-group             | string                                                      | `1`                                |
| box-orient                    | string                                                      | `horizontal`                       |
| box-pack                      | string                                                      | `center`                           |
| box-shadow                    | string or SizeVariable                                      | `10px 5px 5px black`               |
| box-sizing                    | string                                                      | `border-box`                       |
| break-after                   | string                                                      | `auto`                             |
| break-before                  | string                                                      | `always`                           |
| break-inside                  | string                                                      | `avoid`                            |
| caption-side                  | string                                                      | `bottom`                           |
| caret                         | string                                                      | `auto`                             |
| caret-color                   | string or ColorVariable                                     | `blue`                             |
| caret-shape                   | string                                                      | `bar`                              |
| clear                         | string                                                      | `both`                             |
| clip                          | string                                                      | `rect(0,0,0,0)`                    |
| clip-path                     | string                                                      | `circle(50%)`                      |
| clip-rule                     | string                                                      | `evenodd`                          |
| color                         | string or ColorVariable                                     | `#FF9800`                          |
| color-interpolation           | string                                                      | `sRGB`                             |
| color-interpolation-filters   | string                                                      | `linearRGB`                        |
| color-scheme                  | string                                                      | `light dark`                       |
| column-count                  | string                                                      | `3`                                |
| column-fill                   | string                                                      | `auto`                             |
| column-gap                    | string or SizeVariable                                      | `20px`                             |
| column-rule                   | string                                                      | `1px solid #ccc`                   |
| column-rule-color             | string or ColorVariable                                     | `#607D8B`                          |
| column-rule-style             | string                                                      | `solid`                            |
| column-rule-width             | string or SizeVariable                                      | `1px`                              |
| column-span                   | string                                                      | `all`                              |
| column-width                  | string or SizeVariable                                      | `200px`                            |
| columns                       | string                                                      | `3 200px`                          |
| contain                       | string                                                      | `layout style`                     |
| contain-intrinsic-block-size  | string                                                      | `300px`                            |
| contain-intrinsic-height      | string                                                      | `300px`                            |
| contain-intrinsic-inline-size | string                                                      | `200px`                            |
| contain-intrinsic-size        | string                                                      | `200px 300px`                      |
| contain-intrinsic-width       | string                                                      | `200px`                            |
| container                     | string                                                      | `sidebar / inline-size`            |
| container-name                | string                                                      | `sidebar`                          |
| container-type                | string                                                      | `inline-size`                      |
| content                       | string                                                      | `'Hello'`                          |
| content-visibility            | string                                                      | `auto`                             |
| counter-increment             | string                                                      | `section`                          |
| counter-reset                 | string                                                      | `section`                          |
| counter-set                   | string                                                      | `section 5`                        |
| cursor                        | string                                                      | `pointer`                          |
| cx                            | string                                                      | `50`                               |
| cy                            | string                                                      | `50`                               |
| d                             | string                                                      | `path('M10 10')`                   |
| direction                     | string                                                      | `ltr`                              |
| display                       | string                                                      | `flex`                             |
| dominant-baseline             | string                                                      | `alphabetic`                       |
| empty-cells                   | string                                                      | `show`                             |
| field-sizing                  | string                                                      | `content`                          |
| fill                          | string                                                      | `#f00`                             |
| fill-opacity                  | string                                                      | `0.5`                              |
| fill-rule                     | string                                                      | `nonzero`                          |
| filter                        | string or SizeVariable                                      | `blur(2px)`                        |
| flex                          | string                                                      | `1 1 auto`                         |
| flex-basis                    | string, SizeVariable, or PercentageVariable                 | `auto`                             |
| flex-direction                | string                                                      | `row`                              |
| flex-flow                     | string                                                      | `row wrap`                         |
| flex-grow                     | string or NumberVariable                                    | `1`                                |
| flex-shrink                   | string or NumberVariable                                    | `1`                                |
| flex-wrap                     | string                                                      | `wrap`                             |
| float                         | string                                                      | `right`                            |
| flood-color                   | string or ColorVariable                                     | `#00BCD4`                          |
| flood-opacity                 | string                                                      | `0.7`                              |
| font                          | string                                                      | `italic bold 16px/1.5 Arial`       |
| font-family                   | string or FontFamilyVariable                                | `Arial, sans-serif`                |
| font-feature-settings         | string                                                      | `'liga' 1`                         |
| font-kerning                  | string                                                      | `normal`                           |
| font-language-override        | string                                                      | `normal`                           |
| font-optical-sizing           | string                                                      | `auto`                             |
| font-palette                  | string                                                      | `--custom`                         |
| font-size                     | string, SizeVariable, or PercentageVariable                 | `16px`                             |
| font-size-adjust              | string                                                      | `0.5`                              |
| font-smooth                   | string                                                      | `auto`                             |
| font-stretch                  | string                                                      | `condensed`                        |
| font-style                    | string                                                      | `italic`                           |
| font-synthesis                | string                                                      | `weight style`                     |
| font-synthesis-position       | string                                                      | `auto`                             |
| font-synthesis-small-caps     | string                                                      | `auto`                             |
| font-synthesis-style          | string                                                      | `auto`                             |
| font-synthesis-weight         | string                                                      | `auto`                             |
| font-variant                  | string                                                      | `small-caps`                       |
| font-variant-alternates       | string                                                      | `normal`                           |
| font-variant-caps             | string                                                      | `small-caps`                       |
| font-variant-east-asian       | string                                                      | `normal`                           |
| font-variant-ligatures        | string                                                      | `none`                             |
| font-variant-numeric          | string                                                      | `ordinal`                          |
| font-variant-position         | string                                                      | `sub`                              |
| font-variation-settings       | string                                                      | `'wght' 400`                       |
| font-weight                   | string or NumberVariable                                    | `bold`                             |
| forced-color-adjust           | string                                                      | `none`                             |
| gap                           | string                                                      | `10px 20px`                        |
| grid                          | string                                                      | `auto / 1fr 1fr`                   |
| grid-area                     | string                                                      | `header`                           |
| grid-auto-columns             | string                                                      | `minmax(100px, auto)`              |
| grid-auto-flow                | string                                                      | `row dense`                        |
| grid-auto-rows                | string                                                      | `auto`                             |
| grid-column                   | string                                                      | `1 / span 2`                       |
| grid-column-end               | string                                                      | `span 2`                           |
| grid-column-gap               | string, SizeVariable, or PercentageVariable                 | `10px`                             |
| grid-column-start             | string                                                      | `1`                                |
| grid-gap                      | string                                                      | `10px 20px`                        |
| grid-row                      | string                                                      | `1 / 3`                            |
| grid-row-end                  | string                                                      | `3`                                |
| grid-row-gap                  | string, SizeVariable, or PercentageVariable                 | `20px`                             |
| grid-row-start                | string                                                      | `1`                                |
| grid-template                 | string                                                      | `auto / 1fr 1fr`                   |
| grid-template-areas           | string                                                      | `'header header'`                  |
| grid-template-columns         | string                                                      | `50px 100px`                       |
| grid-template-rows            | string                                                      | `auto`                             |
| hanging-punctuation           | string                                                      | `first`                            |
| height                        | string, SizeVariable, or PercentageVariable                 | `100vh`                            |
| hyphenate-character           | string                                                      | `auto`                             |
| hyphenate-limit-chars         | string                                                      | `auto`                             |
| hyphens                       | string                                                      | `auto`                             |
| image-orientation             | string                                                      | `90deg`                            |
| image-rendering               | string                                                      | `auto`                             |
| image-resolution              | string                                                      | `300dpi`                           |
| ime-mode                      | string                                                      | `auto`                             |
| initial-letter                | string                                                      | `3`                                |
| initial-letter-align          | string                                                      | `auto`                             |
| inline-size                   | string or SizeVariable                                      | `200px`                            |
| input-security                | string                                                      | `auto`                             |
| inset                         | string                                                      | `10px 20px`                        |
| inset-block                   | string                                                      | `10px`                             |
| inset-block-end               | string or SizeVariable                                      | `20px`                             |
| inset-block-start             | string or SizeVariable                                      | `5px`                              |
| inset-inline                  | string                                                      | `10px`                             |
| inset-inline-end              | string or SizeVariable                                      | `10px`                             |
| inset-inline-start            | string or SizeVariable                                      | `10px`                             |
| interpolate-size              | string                                                      | `allow-keywords`                   |
| isolation                     | string                                                      | `isolate`                          |
| justify-content               | string                                                      | `space-between`                    |
| justify-items                 | string                                                      | `stretch`                          |
| justify-self                  | string                                                      | `center`                           |
| justify-tracks                | string                                                      | `normal`                           |
| left                          | string, SizeVariable, or PercentageVariable                 | `50px`                             |
| letter-spacing                | string or SizeVariable                                      | `0.5em`                            |
| lighting-color                | string or ColorVariable                                     | `white`                            |
| line-break                    | string                                                      | `strict`                           |
| line-height                   | string, SizeVariable, NumberVariable, or PercentageVariable | `1.5`                              |
| line-height-step              | string                                                      | `20px`                             |
| list-style                    | string                                                      | `disc inside`                      |
| list-style-image              | string                                                      | `url('star.png')`                  |
| list-style-position           | string                                                      | `inside`                           |
| list-style-type               | string                                                      | `disc`                             |
| margin                        | string                                                      | `10px 20px`                        |
| margin-block                  | string                                                      | `10px`                             |
| margin-block-end              | string or SizeVariable                                      | `15px`                             |
| margin-block-start            | string or SizeVariable                                      | `15px`                             |
| margin-bottom                 | string, SizeVariable, or PercentageVariable                 | `20px`                             |
| margin-inline                 | string                                                      | `10px`                             |
| margin-inline-end             | string or SizeVariable                                      | `10px`                             |
| margin-inline-start           | string or SizeVariable                                      | `10px`                             |
| margin-left                   | string, SizeVariable, or PercentageVariable                 | `30px`                             |
| margin-right                  | string, SizeVariable, or PercentageVariable                 | `30px`                             |
| margin-top                    | string, SizeVariable, or PercentageVariable                 | `10px`                             |
| margin-trim                   | string                                                      | `block-end`                        |
| marker                        | string                                                      | `url('marker.svg')`                |
| marker-end                    | string                                                      | `url('arrowhead.svg')`             |
| marker-mid                    | string                                                      | `url('dot.svg')`                   |
| marker-start                  | string                                                      | `url('circle.svg')`                |
| mask                          | string                                                      | `url('mask.png') no-repeat`        |
| mask-border                   | string                                                      | `url('mask.png') 30`               |
| mask-border-mode              | string                                                      | `luminance`                        |
| mask-border-outset            | string                                                      | `5px`                              |
| mask-border-repeat            | string                                                      | `stretch`                          |
| mask-border-slice             | string                                                      | `30%`                              |
| mask-border-source            | string                                                      | `url('mask.png')`                  |
| mask-border-width             | string                                                      | `10px`                             |
| mask-clip                     | string                                                      | `border-box`                       |
| mask-composite                | string                                                      | `add`                              |
| mask-image                    | string                                                      | `url('mask.png')`                  |
| mask-mode                     | string                                                      | `luminance`                        |
| mask-origin                   | string                                                      | `border-box`                       |
| mask-position                 | string                                                      | `center`                           |
| mask-repeat                   | string                                                      | `no-repeat`                        |
| mask-size                     | string                                                      | `cover`                            |
| mask-type                     | string                                                      | `luminance`                        |
| masonry-auto-flow             | string                                                      | `pack`                             |
| math-depth                    | string                                                      | `0`                                |
| math-shift                    | string                                                      | `normal`                           |
| math-style                    | string                                                      | `normal`                           |
| max-block-size                | string or SizeVariable                                      | `100px`                            |
| max-height                    | string, SizeVariable, or PercentageVariable                 | `200px`                            |
| max-inline-size               | string or SizeVariable                                      | `300px`                            |
| max-lines                     | string                                                      | `3`                                |
| max-width                     | string, SizeVariable, or PercentageVariable                 | `80%`                              |
| min-block-size                | string or SizeVariable                                      | `50px`                             |
| min-height                    | string, SizeVariable, or PercentageVariable                 | `100px`                            |
| min-inline-size               | string or SizeVariable                                      | `150px`                            |
| min-width                     | string, SizeVariable, or PercentageVariable                 | `60px`                             |
| mix-blend-mode                | string                                                      | `multiply`                         |
| object-fit                    | string                                                      | `cover`                            |
| object-position               | string                                                      | `center top`                       |
| offset                        | string                                                      | `path('M10 80') 50px`              |
| offset-anchor                 | string                                                      | `auto`                             |
| offset-distance               | string or SizeVariable                                      | `10px`                             |
| offset-path                   | string                                                      | `path('M10 80 Q 95 10 180 80')`    |
| offset-position               | string                                                      | `auto`                             |
| offset-rotate                 | string                                                      | `auto`                             |
| opacity                       | string, NumberVariable, or PercentageVariable               | `0.5`                              |
| order                         | string                                                      | `2`                                |
| orphans                       | string                                                      | `2`                                |
| outline                       | string                                                      | `2px solid red`                    |
| outline-color                 | string or ColorVariable                                     | `#FF5722`                          |
| outline-offset                | string or SizeVariable                                      | `2px`                              |
| outline-style                 | string                                                      | `dashed`                           |
| outline-width                 | string or SizeVariable                                      | `3px`                              |
| overflow                      | string                                                      | `hidden`                           |
| overflow-anchor               | string                                                      | `auto`                             |
| overflow-block                | string                                                      | `auto`                             |
| overflow-clip-box             | string                                                      | `padding-box`                      |
| overflow-clip-margin          | string                                                      | `5px`                              |
| overflow-inline               | string                                                      | `auto`                             |
| overflow-wrap                 | string                                                      | `break-word`                       |
| overflow-x                    | string                                                      | `auto`                             |
| overflow-y                    | string                                                      | `scroll`                           |
| overlay                       | string                                                      | `auto`                             |
| overscroll-behavior           | string                                                      | `contain`                          |
| overscroll-behavior-block     | string                                                      | `contain`                          |
| overscroll-behavior-inline    | string                                                      | `none`                             |
| overscroll-behavior-x         | string                                                      | `contain`                          |
| overscroll-behavior-y         | string                                                      | `none`                             |
| padding                       | string                                                      | `10px 20px`                        |
| padding-block                 | string                                                      | `10px`                             |
| padding-block-end             | string or SizeVariable                                      | `25px`                             |
| padding-block-start           | string or SizeVariable                                      | `25px`                             |
| padding-bottom                | string, SizeVariable, or PercentageVariable                 | `15px`                             |
| padding-inline                | string                                                      | `10px`                             |
| padding-inline-end            | string or SizeVariable                                      | `20px`                             |
| padding-inline-start          | string or SizeVariable                                      | `20px`                             |
| padding-left                  | string, SizeVariable, or PercentageVariable                 | `10px`                             |
| padding-right                 | string, SizeVariable, or PercentageVariable                 | `10px`                             |
| padding-top                   | string, SizeVariable, or PercentageVariable                 | `10px`                             |
| page                          | string                                                      | `auto`                             |
| page-break-after              | string                                                      | `always`                           |
| page-break-before             | string                                                      | `always`                           |
| page-break-inside             | string                                                      | `avoid`                            |
| paint-order                   | string                                                      | `fill stroke markers`              |
| perspective                   | string or SizeVariable                                      | `500px`                            |
| perspective-origin            | string                                                      | `50% 50%`                          |
| place-content                 | string                                                      | `center start`                     |
| place-items                   | string                                                      | `center`                           |
| place-self                    | string                                                      | `center`                           |
| pointer-events                | string                                                      | `none`                             |
| position                      | string                                                      | `absolute`                         |
| position-anchor               | string                                                      | `--my-anchor`                      |
| position-area                 | string                                                      | `top center`                       |
| position-try                  | string                                                      | `--my-fallback`                    |
| position-try-fallbacks        | string                                                      | `flip-block`                       |
| position-try-order            | string                                                      | `most-height`                      |
| position-visibility           | string                                                      | `anchors-visible`                  |
| print-color-adjust            | string                                                      | `exact`                            |
| quotes                        | string                                                      | `'"' '"'`                          |
| r                             | string or SizeVariable                                      | `50px`                             |
| resize                        | string                                                      | `both`                             |
| right                         | string, SizeVariable, or PercentageVariable                 | `0px`                              |
| rotate                        | string                                                      | `45deg`                            |
| row-gap                       | string or SizeVariable                                      | `20px`                             |
| ruby-align                    | string                                                      | `center`                           |
| ruby-merge                    | string                                                      | `auto`                             |
| ruby-position                 | string                                                      | `over`                             |
| rx                            | string or SizeVariable                                      | `10px`                             |
| ry                            | string or SizeVariable                                      | `10px`                             |
| scale                         | string                                                      | `1.2`                              |
| scroll-behavior               | string                                                      | `smooth`                           |
| scroll-margin                 | string                                                      | `10px`                             |
| scroll-margin-block           | string                                                      | `10px`                             |
| scroll-margin-block-end       | string or SizeVariable                                      | `10px`                             |
| scroll-margin-block-start     | string or SizeVariable                                      | `10px`                             |
| scroll-margin-bottom          | string                                                      | `10px`                             |
| scroll-margin-inline          | string                                                      | `10px`                             |
| scroll-margin-inline-end      | string or SizeVariable                                      | `10px`                             |
| scroll-margin-inline-start    | string or SizeVariable                                      | `10px`                             |
| scroll-margin-left            | string                                                      | `10px`                             |
| scroll-margin-right           | string                                                      | `10px`                             |
| scroll-margin-top             | string                                                      | `10px`                             |
| scroll-padding                | string                                                      | `20px`                             |
| scroll-padding-block          | string                                                      | `20px`                             |
| scroll-padding-block-end      | string or SizeVariable                                      | `20px`                             |
| scroll-padding-block-start    | string or SizeVariable                                      | `20px`                             |
| scroll-padding-bottom         | string                                                      | `20px`                             |
| scroll-padding-inline         | string                                                      | `20px`                             |
| scroll-padding-inline-end     | string or SizeVariable                                      | `20px`                             |
| scroll-padding-inline-start   | string or SizeVariable                                      | `20px`                             |
| scroll-padding-left           | string                                                      | `20px`                             |
| scroll-padding-right          | string                                                      | `20px`                             |
| scroll-padding-top            | string                                                      | `20px`                             |
| scroll-snap-align             | string                                                      | `start`                            |
| scroll-snap-coordinate        | string                                                      | `50% 50%`                          |
| scroll-snap-destination       | string                                                      | `50% 50%`                          |
| scroll-snap-points-x          | string                                                      | `repeat(100px)`                    |
| scroll-snap-points-y          | string                                                      | `repeat(100px)`                    |
| scroll-snap-stop              | string                                                      | `normal`                           |
| scroll-snap-type              | string                                                      | `y mandatory`                      |
| scroll-snap-type-x            | string                                                      | `mandatory`                        |
| scroll-snap-type-y            | string                                                      | `mandatory`                        |
| scroll-timeline               | string                                                      | `--my-scroller block`              |
| scroll-timeline-axis          | string                                                      | `block`                            |
| scroll-timeline-name          | string                                                      | `--my-scroller`                    |
| scrollbar-color               | string                                                      | `dark`                             |
| scrollbar-gutter              | string                                                      | `stable`                           |
| scrollbar-width               | string                                                      | `thin`                             |
| shape-image-threshold         | string                                                      | `0.3`                              |
| shape-margin                  | string or SizeVariable                                      | `15px`                             |
| shape-outside                 | string                                                      | `circle(50%)`                      |
| shape-rendering               | string                                                      | `auto`                             |
| stop-color                    | string or ColorVariable                                     | `#0D47A1`                          |
| stop-opacity                  | string                                                      | `0.8`                              |
| stroke                        | string or ColorVariable                                     | `black`                            |
| stroke-dasharray              | string                                                      | `5, 10`                            |
| stroke-dashoffset             | string or SizeVariable                                      | `5px`                              |
| stroke-linecap                | string                                                      | `round`                            |
| stroke-linejoin               | string                                                      | `bevel`                            |
| stroke-miterlimit             | string                                                      | `10`                               |
| stroke-opacity                | string                                                      | `1`                                |
| stroke-width                  | string or SizeVariable                                      | `3px`                              |
| tab-size                      | string or SizeVariable                                      | `4`                                |
| table-layout                  | string                                                      | `fixed`                            |
| text-align                    | string                                                      | `justify`                          |
| text-align-last               | string                                                      | `center`                           |
| text-anchor                   | string                                                      | `start`                            |
| text-combine-upright          | string                                                      | `all`                              |
| text-decoration               | string                                                      | `underline`                        |
| text-decoration-color         | string or ColorVariable                                     | `red`                              |
| text-decoration-line          | string                                                      | `overline`                         |
| text-decoration-skip          | string                                                      | `spaces`                           |
| text-decoration-skip-ink      | string                                                      | `auto`                             |
| text-decoration-style         | string                                                      | `dotted`                           |
| text-decoration-thickness     | string                                                      | `2px`                              |
| text-emphasis                 | string                                                      | `filled circle red`                |
| text-emphasis-color           | string or ColorVariable                                     | `green`                            |
| text-emphasis-position        | string                                                      | `under right`                      |
| text-emphasis-style           | string                                                      | `filled circle`                    |
| text-indent                   | string, SizeVariable, or PercentageVariable                 | `20px`                             |
| text-justify                  | string                                                      | `inter-word`                       |
| text-orientation              | string                                                      | `mixed`                            |
| text-overflow                 | string                                                      | `ellipsis`                         |
| text-rendering                | string                                                      | `optimizeLegibility`               |
| text-shadow                   | string or SizeVariable                                      | `2px 2px 5px grey`                 |
| text-size-adjust              | string                                                      | `100%`                             |
| text-spacing-trim             | string                                                      | `normal`                           |
| text-transform                | string                                                      | `uppercase`                        |
| text-underline-offset         | string                                                      | `3px`                              |
| text-underline-position       | string                                                      | `under`                            |
| text-wrap                     | string                                                      | `balance`                          |
| text-wrap-mode                | string                                                      | `wrap`                             |
| text-wrap-style               | string                                                      | `balance`                          |
| timeline-scope                | string                                                      | `--my-timeline`                    |
| top                           | string, SizeVariable, or PercentageVariable                 | `100px`                            |
| touch-action                  | string                                                      | `pan-right`                        |
| transform                     | string                                                      | `rotate(45deg)`                    |
| transform-box                 | string                                                      | `view-box`                         |
| transform-origin              | string                                                      | `top left`                         |
| transform-style               | string                                                      | `preserve-3d`                      |
| transition                    | string                                                      | `opacity 300ms ease-in-out`        |
| transition-behavior           | string                                                      | `allow-discrete`                   |
| transition-delay              | string                                                      | `0.5s`                             |
| transition-duration           | string                                                      | `300ms`                            |
| transition-property           | string                                                      | `opacity`                          |
| transition-timing-function    | string                                                      | `ease-in-out`                      |
| translate                     | string or SizeVariable                                      | `10px, 20px`                       |
| unicode-bidi                  | string                                                      | `bidi-override`                    |
| user-select                   | string                                                      | `none`                             |
| vector-effect                 | string                                                      | `non-scaling-stroke`               |
| vertical-align                | string                                                      | `middle`                           |
| view-timeline                 | string                                                      | `--my-view block`                  |
| view-timeline-axis            | string                                                      | `block`                            |
| view-timeline-inset           | string                                                      | `auto`                             |
| view-timeline-name            | string                                                      | `--my-view`                        |
| view-transition-name          | string                                                      | `my-transition`                    |
| visibility                    | string                                                      | `hidden`                           |
| white-space                   | string                                                      | `nowrap`                           |
| white-space-collapse          | string                                                      | `collapse`                         |
| widows                        | string                                                      | `2`                                |
| width                         | string, SizeVariable, or PercentageVariable                 | `50%`                              |
| will-change                   | string                                                      | `transform`                        |
| word-break                    | string                                                      | `break-word`                       |
| word-spacing                  | string or SizeVariable                                      | `5px`                              |
| word-wrap                     | string                                                      | `break-word`                       |
| writing-mode                  | string                                                      | `vertical-rl`                      |
| x                             | string or SizeVariable                                      | `5px`                              |
| y                             | string or SizeVariable                                      | `10px`                             |
| z-index                       | string or NumberVariable                                    | `10`                               |
| zoom                          | string                                                      | `1.5`                              |
| -webkit-line-clamp            | string                                                      | `3`                                |
| -webkit-text-fill-color       | string or ColorVariable                                     | `#FF5722`                          |
| -webkit-text-stroke-color     | string or ColorVariable                                     | `#4CAF50`                          |
| -webkit-text-stroke-width     | string or SizeVariable                                      | `1px`                              |

{/* <!-- vale on --> */}
