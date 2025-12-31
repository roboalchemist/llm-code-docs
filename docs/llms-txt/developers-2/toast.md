# Source: https://developers.raycast.com/api-reference/feedback/toast.md

# Toast

When an asynchronous operation is happening or when an error is thrown, it's usually a good idea to keep the user informed about it. Toasts are made for that.

Additionally, Toasts can have some actions associated to the action they are about. For example, you could provide a way to cancel an asynchronous operation, undo an action, or copy the stack trace of an error.

{% hint style="info" %}
The `showToast()` will fallback to [showHUD()](https://developers.raycast.com/api-reference/hud#showhud) if the Raycast window is closed.
{% endhint %}

![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-607b51d1dc3e47c6cdff37be217a0e4d42368a57%2Ftoast.webp?alt=media)

## API Reference

### showToast

Creates and shows a Toast with the given [options](#toast.options).

#### Signature

```typescript
async function showToast(options: Toast.Options): Promise<Toast>;
```

#### Example

```typescript
import { showToast, Toast } from "@raycast/api";

export default async function Command() {
  const success = false;

  if (success) {
    await showToast({ title: "Dinner is ready", message: "Pizza margherita" });
  } else {
    await showToast({
      style: Toast.Style.Failure,
      title: "Dinner isn't ready",
      message: "Pizza dropped on the floor",
    });
  }
}
```

When showing an animated Toast, you can later on update it:

```typescript
import { showToast, Toast } from "@raycast/api";
import { setTimeout } from "timers/promises";

export default async function Command() {
  const toast = await showToast({
    style: Toast.Style.Animated,
    title: "Uploading image",
  });

  try {
    // upload the image
    await setTimeout(1000);

    toast.style = Toast.Style.Success;
    toast.title = "Uploaded image";
  } catch (err) {
    toast.style = Toast.Style.Failure;
    toast.title = "Failed to upload image";
    if (err instanceof Error) {
      toast.message = err.message;
    }
  }
}
```

#### Parameters

| Name                                      | Description                         | Type                                                                                |
| ----------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- |
| options<mark style="color:red;">\*</mark> | The options to customize the Toast. | [`Alert.Options`](https://developers.raycast.com/api-reference/alert#alert.options) |

#### Return

A Promise that resolves with the shown Toast. The Toast can be used to change or hide it.

## Types

### Toast

A Toast with a certain style, title, and message.

Use [showToast](#showtoast) to create and show a Toast.

#### Properties

| Property                                          | Description                                                                                                        | Type                                                                                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| message<mark style="color:red;">\*</mark>         | An additional message for the Toast. Useful to show more information, e.g. an identifier of a newly created asset. | `string`                                                                                        |
| primaryAction<mark style="color:red;">\*</mark>   | The primary Action the user can take when hovering on the Toast.                                                   | [`Alert.ActionOptions`](https://developers.raycast.com/api-reference/alert#alert.actionoptions) |
| secondaryAction<mark style="color:red;">\*</mark> | The secondary Action the user can take when hovering on the Toast.                                                 | [`Alert.ActionOptions`](https://developers.raycast.com/api-reference/alert#alert.actionoptions) |
| style<mark style="color:red;">\*</mark>           | The style of a Toast.                                                                                              | [`Action.Style`](https://developers.raycast.com/user-interface/actions#action.style)            |
| title<mark style="color:red;">\*</mark>           | The title of a Toast. Displayed on the top.                                                                        | `string`                                                                                        |

#### Methods

| Name | Type                  | Description      |
| ---- | --------------------- | ---------------- |
| hide | `() => Promise<void>` | Hides the Toast. |
| show | `() => Promise<void>` | Shows the Toast. |

### Toast.Options

The options to create a [Toast](#toast).

#### Example

```typescript
import { showToast, Toast } from "@raycast/api";

export default async function Command() {
  const options: Toast.Options = {
    style: Toast.Style.Success,
    title: "Finished cooking",
    message: "Delicious pasta for lunch",
    primaryAction: {
      title: "Do something",
      onAction: (toast) => {
        console.log("The toast action has been triggered");
        toast.hide();
      },
    },
  };
  await showToast(options);
}
```

#### Properties

| Property                                | Description                                                                                                        | Type                                                                                            |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| title<mark style="color:red;">\*</mark> | The title of a Toast. Displayed on the top.                                                                        | `string`                                                                                        |
| message                                 | An additional message for the Toast. Useful to show more information, e.g. an identifier of a newly created asset. | `string`                                                                                        |
| primaryAction                           | The primary Action the user can take when hovering on the Toast.                                                   | [`Alert.ActionOptions`](https://developers.raycast.com/api-reference/alert#alert.actionoptions) |
| secondaryAction                         | The secondary Action the user can take when hovering on the Toast.                                                 | [`Alert.ActionOptions`](https://developers.raycast.com/api-reference/alert#alert.actionoptions) |
| style                                   | The style of a Toast.                                                                                              | [`Action.Style`](https://developers.raycast.com/user-interface/actions#action.style)            |

### Toast.Style

Defines the visual style of the Toast.

Use [Toast.Style.Success](#toast.style) for confirmations and [Toast.Style.Failure](#toast.style) for displaying errors.\
Use [Toast.Style.Animated](#toast.style) when your Toast should be shown until a process is completed.\
You can hide it later by using [Toast.hide](#toast) or update the properties of an existing Toast.

#### Enumeration members

| Name     | Value                                                                                                                                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animated | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-7e62989ba2fea14db0967e09bb5bfaf84706e12d%2Ftoast-animated.webp?alt=media) |
| Success  | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-dce0b170c3e47fa4c5525e1a0a74600350006445%2Ftoast-success.webp?alt=media)  |
| Failure  | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-96a3cfd7aaec6933c18481f6228bb647093217ff%2Ftoast-failure.webp?alt=media)  |

### Toast.ActionOptions

The options to create a [Toast](#toast) Action.

#### Properties

| Property                                   | Description                                     | Type                                                                             |
| ------------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------- |
| onAction<mark style="color:red;">\*</mark> | A callback called when the action is triggered. | `(toast:` [`Toast`](#toast)`) => void`                                           |
| title<mark style="color:red;">\*</mark>    | The title of the action.                        | `string`                                                                         |
| shortcut                                   | The keyboard shortcut for the action.           | [`Keyboard.Shortcut`](https://developers.raycast.com/keyboard#keyboard.shortcut) |
