# Source: https://img.ly/docs/cesdk/ios/animation/types-4e5f41/

---
title: "Supported Animation Types"
description: "Explore the types of animations supported by CE.SDK, including object, text, and transition effects."
platform: ios
url: "https://img.ly/docs/cesdk/ios/animation/types-4e5f41/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Animation](https://img.ly/docs/cesdk/ios/animation-ce900c/) > [Supported Animation Types](https://img.ly/docs/cesdk/ios/animation/types-4e5f41/)

---

## Animation Categories

There are three different categories of animations: *In*, *Out* and *Loop* animations.

### In Animations

*In* animations animate a block for a specified duration after the block first appears in the scene.
For example, if a block has a time offset of 4s in the scene and it has an *In* animation with a duration of 1s, then the appearance of the block will be animated between 4s and 5s with the *In* animation.

### Out Animations

*Out* animations animate a block for a specified duration before the block disappears from the scene.
For example, if a block has a time offset of 4s in the scene and a duration of 5s and it has an *Out* animation with a duration of 1s, then the appearance of the block will be animated between 8s and 9s with the *Out* animation.

### Loop Animations

*Loop* animations animate a block for the total duration that the block is visible in the scene. *Loop* animations also run simultaneously with *In* and *Out* animations, if those are present.

## Animation Presets

We currently support the following *In* and *Out* animation presets:

- `'//ly.img.ubq/animation/slide'`
- `'//ly.img.ubq/animation/pan'`
- `'//ly.img.ubq/animation/fade'`
- `'//ly.img.ubq/animation/blur'`
- `'//ly.img.ubq/animation/grow'`
- `'//ly.img.ubq/animation/zoom'`
- `'//ly.img.ubq/animation/pop'`
- `'//ly.img.ubq/animation/wipe'`
- `'//ly.img.ubq/animation/baseline'`
- `'//ly.img.ubq/animation/crop_zoom'`
- `'//ly.img.ubq/animation/spin'`
- `'//ly.img.ubq/animation/ken_burns'`
- `'//ly.img.ubq/animation/typewriter_text'` (text-only)
- `'//ly.img.ubq/animation/block_swipe_text'` (text-only)
- `'//ly.img.ubq/animation/merge_text'` (text-only)
- `'//ly.img.ubq/animation/spread_text'` (text-only)

and the following *Loop* animation types:

- `'//ly.img.ubq/animation/spin_loop'`
- `'//ly.img.ubq/animation/fade_loop'`
- `'//ly.img.ubq/animation/blur_loop'`
- `'//ly.img.ubq/animation/pulsating_loop'`
- `'//ly.img.ubq/animation/breathing_loop'`
- `'//ly.img.ubq/animation/jump_loop'`
- `'//ly.img.ubq/animation/squeeze_loop'`
- `'//ly.img.ubq/animation/sway_loop'`

## Animation Type Properties

## Baseline Type

A text animation that slides text in along its baseline.

This section describes the properties available for the **Baseline Type** (`//ly.img.ubq/animation/baseline`) block type.

| Property                       | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/baseline/direction` | `Enum`   | `"Up"`     | The direction of the wipe animation., Possible values: `"Up"`, `"Right"`, `"Down"`, `"Left"`                                                                                                                                                                                                                                                    |
| `animationEasing`              | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`            | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`         | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle`    | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Block Swipe Text Type

A text animation that reveals text with a colored block swiping across.

This section describes the properties available for the **Block Swipe Text Type** (`//ly.img.ubq/animation/block_swipe_text`) block type.

| Property                                  | Type     | Default                     | Description                                                                                                                         |
| ----------------------------------------- | -------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `animation/block_swipe_text/blockColor`   | `Color`  | `{"r":0,"g":0,"b":0,"a":1}` | The overlay block color.                                                                                                            |
| `animation/block_swipe_text/direction`    | `Enum`   | `"Right"`                   | The direction of the block swipe animation., Possible values: `"Up"`, `"Right"`, `"Down"`, `"Left"`                                 |
| `animation/block_swipe_text/useTextColor` | `Bool`   | `true`                      | Whether the overlay block should use the text color.                                                                                |
| `playback/duration`                       | `Double` | `1.2`                       | The duration in seconds for which this block should be visible.                                                                     |
| `textAnimationOverlap`                    | `Float`  | `0.35`                      | The overlap factor for text animations.                                                                                             |
| `textAnimationWritingStyle`               | `Enum`   | `"Line"`                    | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"` |

## Blur Type

An animation that applies a blur effect over time.

This section describes the properties available for the **Blur Type** (`//ly.img.ubq/animation/blur`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/blur/fade`       | `Bool`   | `true`     | Whether an opacity fade animation should be applied during the blur animation.                                                                                                                                                                                                                                                                  |
| `animation/blur/intensity`  | `Float`  | `1`        | The maximum intensity of the blur.                                                                                                                                                                                                                                                                                                              |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Blur Loop Type

A looping animation that continuously applies a blur effect.

This section describes the properties available for the **Blur Loop Type** (`//ly.img.ubq/animation/blur_loop`) block type.

| Property                        | Type     | Default | Description                                                     |
| ------------------------------- | -------- | ------- | --------------------------------------------------------------- |
| `animation/blur_loop/intensity` | `Float`  | `1`     | The maximum blur intensity of this effect.                      |
| `playback/duration`             | `Double` | `1.2`   | The duration in seconds for which this block should be visible. |

## Breathing Loop Type

A looping animation with a slow, breathing-like scale effect.

This section describes the properties available for the **Breathing Loop Type** (`//ly.img.ubq/animation/breathing_loop`) block type.

| Property                             | Type     | Default | Description                                                                                                                             |
| ------------------------------------ | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/breathing_loop/intensity` | `Float`  | `0`     | Controls the intensity of the scaling. A value of 0 results in a maximum scale of 1.25. A value of 1 results in a maximum scale of 2.5. |
| `playback/duration`                  | `Double` | `1.2`   | The duration in seconds for which this block should be visible.                                                                         |

## Crop Zoom Type

An animation that zooms the content within the block's frame.

This section describes the properties available for the **Crop Zoom Type** (`//ly.img.ubq/animation/crop_zoom`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/crop_zoom/fade`  | `Bool`   | `true`     | Whether an opacity fade animation should be applied during the crop zoom animation.                                                                                                                                                                                                                                                             |
| `animation/crop_zoom/scale` | `Float`  | `1.25`     | The maximum crop scale value.                                                                                                                                                                                                                                                                                                                   |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `1.2`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |

## Fade Type

An animation that fades the block in or out.

This section describes the properties available for the **Fade Type** (`//ly.img.ubq/animation/fade`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Fade Loop Type

A looping animation that continuously fades the block in and out.

This section describes the properties available for the **Fade Loop Type** (`//ly.img.ubq/animation/fade_loop`) block type.

| Property            | Type     | Default | Description                                                     |
| ------------------- | -------- | ------- | --------------------------------------------------------------- |
| `playback/duration` | `Double` | `1.2`   | The duration in seconds for which this block should be visible. |

## Grow Type

An animation that scales the block up from a point.

This section describes the properties available for the **Grow Type** (`//ly.img.ubq/animation/grow`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/grow/direction`  | `Enum`   | `"All"`    | The direction from which the grow animation originates. Can be horizontal only, vertical only, from the center (all), or from any of the four corners (top-left, top-right, bottom-left, bottom-right)., Possible values: `"Horizontal"`, `"Vertical"`, `"All"`                                                                                 |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Jump Loop Type

A looping animation with a jumping motion.

This section describes the properties available for the **Jump Loop Type** (`//ly.img.ubq/animation/jump_loop`) block type.

| Property                        | Type     | Default | Description                                                                                  |
| ------------------------------- | -------- | ------- | -------------------------------------------------------------------------------------------- |
| `animation/jump_loop/direction` | `Enum`   | `"Up"`  | The direction of the jump animation., Possible values: `"Up"`, `"Right"`, `"Down"`, `"Left"` |
| `animation/jump_loop/intensity` | `Float`  | `0.5`   | Controls how far the block should move as a percentage of its width or height.               |
| `playback/duration`             | `Double` | `1.2`   | The duration in seconds for which this block should be visible.                              |

## Ken Burns Type

An animation that simulates the Ken Burns effect by panning and zooming on content.

This section describes the properties available for the **Ken Burns Type** (`//ly.img.ubq/animation/ken_burns`) block type.

| Property                                  | Type     | Default          | Description                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------- | -------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/ken_burns/direction`           | `Enum`   | `"Right"`        | The direction of the pan travel., Possible values: `"Up"`, `"Right"`, `"Down"`, `"Left"`                                                                                                                                                                                                                                                        |
| `animation/ken_burns/fade`                | `Bool`   | `false`          | Whether an opacity fade animation should be applied during the animation.                                                                                                                                                                                                                                                                       |
| `animation/ken_burns/travelDistanceRatio` | `Float`  | `1`              | The movement distance relative to the length of the crop.                                                                                                                                                                                                                                                                                       |
| `animation/ken_burns/zoomIntensity`       | `Float`  | `0.5`            | The factor by which to zoom in or out.                                                                                                                                                                                                                                                                                                          |
| `animationEasing`                         | `Enum`   | `"EaseOutQuint"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`                       | `Double` | `2.4`            | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |

## Merge Text Type

A text animation where lines of text merge from opposite directions.

This section describes the properties available for the **Merge Text Type** (`//ly.img.ubq/animation/merge_text`) block type.

| Property                         | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/merge_text/direction` | `Enum`   | `"Left"`   | The in-animation direction of the first line of text., Possible values: `"Right"`, `"Left"`                                                                                                                                                                                                                                                     |
| `animation/merge_text/intensity` | `Float`  | `0.5`      | The intensity of the pan.                                                                                                                                                                                                                                                                                                                       |
| `animationEasing`                | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`              | `Double` | `1.2`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |

## Pan Type

An animation that pans the block across the view.

This section describes the properties available for the **Pan Type** (`//ly.img.ubq/animation/pan`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/pan/direction`   | `Float`  | `0`        | The movement direction of the animation in radians.                                                                                                                                                                                                                                                                                             |
| `animation/pan/distance`    | `Float`  | `0.1`      | The movement distance relative to the longer side of the page.                                                                                                                                                                                                                                                                                  |
| `animation/pan/fade`        | `Bool`   | `true`     | Whether an opacity fade animation should be applied during the pan animation.                                                                                                                                                                                                                                                                   |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Pop Type

An animation that quickly scales the block up and down.

This section describes the properties available for the **Pop Type** (`//ly.img.ubq/animation/pop`) block type.

| Property                    | Type     | Default  | Description                                                                                                                         |
| --------------------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `playback/duration`         | `Double` | `0.6`    | The duration in seconds for which this block should be visible.                                                                     |
| `textAnimationOverlap`      | `Float`  | `0.35`   | The overlap factor for text animations.                                                                                             |
| `textAnimationWritingStyle` | `Enum`   | `"Line"` | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"` |

## Pulsating Loop Type

A looping animation with a pulsating scale effect.

This section describes the properties available for the **Pulsating Loop Type** (`//ly.img.ubq/animation/pulsating_loop`) block type.

| Property                             | Type     | Default | Description                                                                                                                                      |
| ------------------------------------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `animation/pulsating_loop/intensity` | `Float`  | `0`     | Controls the intensity of the pulsating effect. A value of 0 results in a maximum scale of 1.25. A value of 1 results in a maximum scale of 2.5. |
| `playback/duration`                  | `Double` | `0.6`   | The duration in seconds for which this block should be visible.                                                                                  |

## Slide Type

An animation that slides the block into or out of view.

This section describes the properties available for the **Slide Type** (`//ly.img.ubq/animation/slide`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/slide/direction` | `Float`  | `0`        | The movement direction angle of the slide animation in radians.                                                                                                                                                                                                                                                                                 |
| `animation/slide/fade`      | `Bool`   | `false`    | Whether an opacity fade animation should be applied during the slide animation.                                                                                                                                                                                                                                                                 |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Spin Type

An animation that rotates the block.

This section describes the properties available for the **Spin Type** (`//ly.img.ubq/animation/spin`) block type.

| Property                    | Type     | Default       | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/spin/direction`  | `Enum`   | `"Clockwise"` | The direction of the spin animation., Possible values: `"Clockwise"`, `"CounterClockwise"`                                                                                                                                                                                                                                                      |
| `animation/spin/fade`       | `Bool`   | `true`        | Whether an opacity fade animation should be applied during the spin animation.                                                                                                                                                                                                                                                                  |
| `animation/spin/intensity`  | `Float`  | `1`           | How far the animation should spin the block. 1.0 is a full rotation (360°).                                                                                                                                                                                                                                                                     |
| `animationEasing`           | `Enum`   | `"Linear"`    | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`         | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`        | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`      | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Spin Loop Type

A looping animation that continuously rotates the block.

This section describes the properties available for the **Spin Loop Type** (`//ly.img.ubq/animation/spin_loop`) block type.

| Property                        | Type     | Default       | Description                                                                                |
| ------------------------------- | -------- | ------------- | ------------------------------------------------------------------------------------------ |
| `animation/spin_loop/direction` | `Enum`   | `"Clockwise"` | The direction of the spin animation., Possible values: `"Clockwise"`, `"CounterClockwise"` |
| `playback/duration`             | `Double` | `1.2`         | The duration in seconds for which this block should be visible.                            |

## Spread Text Type

A text animation where letters spread apart or come together.

This section describes the properties available for the **Spread Text Type** (`//ly.img.ubq/animation/spread_text`) block type.

| Property                          | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/spread_text/fade`      | `Bool`   | `true`     | Whether the text should fade in / out during the spread animation.                                                                                                                                                                                                                                                                              |
| `animation/spread_text/intensity` | `Float`  | `0.5`      | The intensity of the spread.                                                                                                                                                                                                                                                                                                                    |
| `animationEasing`                 | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`               | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |

## Squeeze Loop Type

A looping animation with a squeezing effect.

This section describes the properties available for the **Squeeze Loop Type** (`//ly.img.ubq/animation/squeeze_loop`) block type.

| Property            | Type     | Default | Description                                                     |
| ------------------- | -------- | ------- | --------------------------------------------------------------- |
| `playback/duration` | `Double` | `1.2`   | The duration in seconds for which this block should be visible. |

## Sway Loop Type

A looping animation with a swaying rotational motion.

This section describes the properties available for the **Sway Loop Type** (`//ly.img.ubq/animation/sway_loop`) block type.

| Property                        | Type     | Default | Description                                                                         |
| ------------------------------- | -------- | ------- | ----------------------------------------------------------------------------------- |
| `animation/sway_loop/intensity` | `Float`  | `1`     | The intensity of the animation. Defines the maximum sway angle between 15° and 45°. |
| `playback/duration`             | `Double` | `1.2`   | The duration in seconds for which this block should be visible.                     |

## Typewriter Text Type

A text animation that reveals text as if it's being typed.

This section describes the properties available for the **Typewriter Text Type** (`//ly.img.ubq/animation/typewriter_text`) block type.

| Property                                 | Type     | Default       | Description                                                                                                   |
| ---------------------------------------- | -------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| `animation/typewriter_text/writingStyle` | `Enum`   | `"Character"` | Whether the text should appear one character or one word at a time., Possible values: `"Character"`, `"Word"` |
| `playback/duration`                      | `Double` | `0.6`         | The duration in seconds for which this block should be visible.                                               |

## Wipe Type

An animation that reveals or hides the block with a wipe transition.

This section describes the properties available for the **Wipe Type** (`//ly.img.ubq/animation/wipe`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/wipe/direction`  | `Enum`   | `"Right"`  | The direction of the wipe animation., Possible values: `"Up"`, `"Right"`, `"Down"`, `"Left"`                                                                                                                                                                                                                                                    |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |

## Zoom Type

An animation that scales the entire block.

This section describes the properties available for the **Zoom Type** (`//ly.img.ubq/animation/zoom`) block type.

| Property                    | Type     | Default    | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | -------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `animation/zoom/fade`       | `Bool`   | `true`     | Whether an opacity fade animation should be applied during the zoom animation.                                                                                                                                                                                                                                                                  |
| `animationEasing`           | `Enum`   | `"Linear"` | The easing function to apply to the animation., Possible values: `"Linear"`, `"EaseIn"`, `"EaseOut"`, `"EaseInOut"`, `"EaseInQuart"`, `"EaseOutQuart"`, `"EaseInOutQuart"`, `"EaseInQuint"`, `"EaseOutQuint"`, `"EaseInOutQuint"`, `"EaseInBack"`, `"EaseOutBack"`, `"EaseInOutBack"`, `"EaseInSpring"`, `"EaseOutSpring"`, `"EaseInOutSpring"` |
| `playback/duration`         | `Double` | `0.6`      | The duration in seconds for which this block should be visible.                                                                                                                                                                                                                                                                                 |
| `textAnimationOverlap`      | `Float`  | `0.35`     | The overlap factor for text animations.                                                                                                                                                                                                                                                                                                         |
| `textAnimationWritingStyle` | `Enum`   | `"Line"`   | The writing style for text animations (e.g., by character, by word)., Possible values: `"Block"`, `"Line"`, `"Character"`, `"Word"`                                                                                                                                                                                                             |




---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
