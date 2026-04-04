# Source: https://lynxjs.org/api/lynx-api/main-thread/lynx-animate-api.md

# animate()

<APISummary />

## Introduction

Use `animate()` to set a [CSS Animation](/api/css/properties/animation.md) on UI elements.

## Syntax

```js
animate(keyframes, options);
```

### Parameter

#### keyframes

1. An **array** consisting of objects that contain properties and values of multiple keyframes.

```js
function controlAnimation(ele: MainThread.Element) {
  'main thread'
  ele.animate(
    [
      {
        // from
        opacity: 0,
        color: '#fff',
      },
      {
        // to
        opacity: 1,
        color: '#000',
      },
    ],
    2000,
  );
}
```

2. Assign a [timing-function](/api/css/properties/animation-timing-function.md) for each keyframe to control the animation's speed.

```js
function controlAnimation(ele: MainThread.Element) {
  'main thread'
  ele.animate(
    [
      {
        // from
        opacity: 0,
        color: '#fff',
        'animation-timing-function': 'linear',
      },
      {
        // to
        opacity: 1,
        color: '#000',
        'animation-timing-function': 'ease-in',
      },
    ],
    2000,
  );
}
```

#### options

An **object** that contains one or more properties:

| Key        | Value Type | Optional | Description                                                                                                                                                                                                                                                                        | Default Value          |
| ---------- | ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| duration   | Number     | optional | The length of time for the animation to run.                                                                                                                                                                                                                                       | 0                      |
| delay      | Number     | optional | The length of time to wait before starting the animation.                                                                                                                                                                                                                          | 0                      |
| iterations | Number     | optional | The number of times the animation should repeat. You can set this to `Infinity` to make the animation loop indefinitely.                                                                                                                                                           | 1                      |
| direction  | String     | optional | Whether the animation runs forwards (`normal`), backwards (`reverse`), switches direction after each iteration (`alternate`), or runs backwards and switches direction after each iteration (`alternate-reverse`). Defaults to `"normal"`.                                         | `"normal"`             |
| easing     | String     | optional | The rate of the animation's change over time. Accepts an [timing-function](/api/css/properties/animation-timing-function.md), such as `"linear"`, `"ease-in"`, or `"cubic-bezier(0.42, 0, 0.58, 1)"`. Defaults to "linear".                                                        | `"linear"`             |
| fill       | String     | optional | Dictates whether the animation's effects should be reflected by the element(s) prior to playing ("backwards"), retained after the animation has completed playing ("forwards"), or both. Defaults to "none".                                                                       | `"none"`               |
| name       | String     | optional | The name of the animation, which can be used to uniquely identify it. This name appears in the [animation events](/api/lynx-api/event/animation-event.md#animation) parameters and is typically used to determine if a particular animation event is the one you're interested in. | An internal unique ID. |
| play-state | String     | optional | Animation motion state, which defines whether an animation is running or paused, accepts an [animation-play-state](/api/css/properties/animation-play-state.md)                                                                                                                    | running                |

:::info Note:

If no `name` is specified, a unique id is generated incrementally.

:::

### Return Value

Returns an `Animation` object.
The `Animation` object has the following methods:

| Method Name          | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `Animation.cancel()` | Cancels the animation and triggers the `animation cancel` event. |
| `Animation.pause()`  | Pauses the animation.                                            |
| `Animation.play()`   | Resumes the animation.                                           |

## Example

```js
function controlAnimation(ele: MainThread.Element) {
  'main thread'
  let ani = ele.animate(
    [
      {
        'background-color': 'blue',
        transform: 'translateX(100px) translateY(300px) rotate(360deg)',
      },
      {
        'background-color': 'red',
        transform: 'translateX(0px) translateY(600px) rotate(0deg)',
      },
    ],
    {
      duration: 3000,
      delay: 1000,
      iterations: Infinity,
      direction: 'alternate',
      easing: 'ease-in-out',
      fill: 'both',
    },
  );

  ani.pause();
  ani.play();
  ani.cancel();
}

```

## Animation Event

The events for the `animate()` API are the same as the [animation events](/api/lynx-api/event/animation-event.md#animation) for CSS animations.

## See also

- [Introduction to CSS Animations](/guide/styling/animation.md)
- [Animate API in BTS](/api/lynx-api/lynx/lynx-animate-api.md)

## Compatibility

**Compatibility Table**
**Query:** `lynx-api.main-thread.ElementAnimate`

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 3.4 | - |
| iOS | 3.4 | - |
| Web | ❌ No | - |

**Description:** Create An Animation in MTS

