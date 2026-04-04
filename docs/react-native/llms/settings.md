# Source: https://reactnative.dev/docs/settings.md

# Settings

`Settings` serves as a wrapper for [`NSUserDefaults`](https://developer.apple.com/documentation/foundation/nsuserdefaults), a persistent key-value store available only on iOS.

## Example[​](#example "Direct link to Example")

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `clearWatch()`[​](#clearwatch "Direct link to clearwatch")

tsx

```
static clearWatch(watchId: number);
```

`watchId` is the number returned by `watchKeys()` when the subscription was originally configured.

***

### `get()`[​](#get "Direct link to get")

tsx

```
static get(key: string): any;
```

Get the current value for a given `key` in `NSUserDefaults`.

***

### `set()`[​](#set "Direct link to set")

tsx

```
static set(settings: Record<string, any>);
```

Set one or more values in `NSUserDefaults`.

***

### `watchKeys()`[​](#watchkeys "Direct link to watchkeys")

tsx

```
static watchKeys(keys: string | array<string>, callback: () => void): number;
```

Subscribe to be notified when the value for any of the keys specified by the `keys` parameter has been changed in `NSUserDefaults`. Returns a `watchId` number that may be used with `clearWatch()` to unsubscribe.

note

`watchKeys()` by design ignores internal `set()` calls and fires callback only on changes preformed outside of React Native code.
