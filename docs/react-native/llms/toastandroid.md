# Source: https://reactnative.dev/docs/toastandroid.md

# ToastAndroid

React Native's ToastAndroid API exposes the Android platform's ToastAndroid module as a JS module. It provides the method `show(message, duration)` which takes the following parameters:

* *message* A string with the text to toast
* *duration* The duration of the toast—either `ToastAndroid.SHORT` or `ToastAndroid.LONG`

You can alternatively use `showWithGravity(message, duration, gravity)` to specify where the toast appears in the screen's layout. May be `ToastAndroid.TOP`, `ToastAndroid.BOTTOM` or `ToastAndroid.CENTER`.

The `showWithGravityAndOffset(message, duration, gravity, xOffset, yOffset)` method adds the ability to specify an offset with in pixels.

note

Starting with Android 11 (API level 30), setting the gravity has no effect on text toasts. Read about the changes [here](https://developer.android.com/about/versions/11/behavior-changes-11#text-toast-api-changes).

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `show()`[​](#show "Direct link to show")

tsx

```
static show(message: string, duration: number);
```

***

### `showWithGravity()`[​](#showwithgravity "Direct link to showwithgravity")

This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.

tsx

```
static showWithGravity(message: string, duration: number, gravity: number);
```

***

### `showWithGravityAndOffset()`[​](#showwithgravityandoffset "Direct link to showwithgravityandoffset")

This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.

tsx

```
static showWithGravityAndOffset(
  message: string,
  duration: number,
  gravity: number,
  xOffset: number,
  yOffset: number,
);
```

## Properties[​](#properties "Direct link to Properties")

### `SHORT`[​](#short "Direct link to short")

Indicates the duration on the screen.

tsx

```
static SHORT: number;
```

***

### `LONG`[​](#long "Direct link to long")

Indicates the duration on the screen.

tsx

```
static LONG: number;
```

***

### `TOP`[​](#top "Direct link to top")

Indicates the position on the screen.

tsx

```
static TOP: number;
```

***

### `BOTTOM`[​](#bottom "Direct link to bottom")

Indicates the position on the screen.

tsx

```
static BOTTOM: number;
```

***

### `CENTER`[​](#center "Direct link to center")

Indicates the position on the screen.

tsx

```
static CENTER: number;
```
