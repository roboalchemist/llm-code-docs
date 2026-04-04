# Source: https://reactnative.dev/docs/share.md

# Share

## Example[​](#example "Direct link to Example")

* TypeScript
* JavaScript

# Reference

## Methods[​](#methods "Direct link to Methods")

### `share()`[​](#share "Direct link to share")

tsx

```
static share(content: ShareContent, options?: ShareOptions);
```

Open a dialog to share text content.

In iOS, returns a Promise which will be invoked with an object containing `action` and `activityType`. If the user dismissed the dialog, the Promise will still be resolved with action being `Share.dismissedAction` and all the other keys being undefined. Note that some share options will not appear or work on the iOS simulator.

In Android, returns a Promise which will always be resolved with action being `Share.sharedAction`.

**Properties:**

| Name            | Type   | Description                                                                                                                                                                                                        |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| contentRequired | object | `message` - a message to share<br />`url` - a URL to shareiOS<br />`title` - title of the messageAndroid***At least one of `url` and `message` is required.                                                        |
| options         | object | `dialogTitle`Android<br />`excludedActivityTypes`iOS<br />`subject` - a subject to share via emailiOS<br />`tintColor`iOS<br />`anchor` - the node to which the action sheet should be anchored (used for iPad)iOS |

***

## Properties[​](#properties "Direct link to Properties")

### `sharedAction`[​](#sharedaction "Direct link to sharedaction")

tsx

```
static sharedAction: 'sharedAction';
```

The content was successfully shared.

***

### `dismissedAction`iOS[​](#dismissedaction-ios "Direct link to dismissedaction-ios")

tsx

```
static dismissedAction: 'dismissedAction';
```

The dialog has been dismissed.
