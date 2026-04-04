# Source: https://reactnative.dev/docs/systrace.md

# Systrace

`Systrace` is a standard Android marker-based profiling tool (and is installed when you install the Android platform-tools package). Profiled code blocks are surrounded by start/end markers which are then visualized in a colorful chart format. Both the Android SDK and React Native framework provide standard markers that you can visualize.

## Example[​](#example "Direct link to Example")

`Systrace` allows you to mark JavaScript (JS) events with a tag and an integer value. Capture the non-Timed JS events in EasyProfiler.

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `isEnabled()`[​](#isenabled "Direct link to isenabled")

tsx

```
static isEnabled(): boolean;
```

***

### `beginEvent()`[​](#beginevent "Direct link to beginevent")

tsx

```
static beginEvent(eventName: string | (() => string), args?: EventArgs);
```

beginEvent/endEvent for starting and then ending a profile within the same call stack frame.

***

### `endEvent()`[​](#endevent "Direct link to endevent")

tsx

```
static endEvent(args?: EventArgs);
```

***

### `beginAsyncEvent()`[​](#beginasyncevent "Direct link to beginasyncevent")

tsx

```
static beginAsyncEvent(
  eventName: string | (() => string),
  args?: EventArgs,
): number;
```

beginAsyncEvent/endAsyncEvent for starting and then ending a profile where the end can either occur on another thread or out of the current stack frame, eg await the returned cookie variable should be used as input into the endAsyncEvent call to end the profile.

***

### `endAsyncEvent()`[​](#endasyncevent "Direct link to endasyncevent")

tsx

```
static endAsyncEvent(
  eventName: EventName,
  cookie: number,
  args?: EventArgs,
);
```

***

### `counterEvent()`[​](#counterevent "Direct link to counterevent")

tsx

```
static counterEvent(eventName: string | (() => string), value: number);
```

Register the value to the profileName on the systrace timeline.
