# Source: https://developers.raycast.com/api-reference/feedback/hud.md

# HUD

When the user takes an action that has the side effect of closing Raycast (for example when copying something in the [Clipboard](https://developers.raycast.com/api-reference/clipboard)), you can use a HUD to confirm that the action worked properly.

![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-690446648e9c7bb76403f9d177ecfc8a3851ee8a%2Fhud.webp?alt=media)

## API Reference

### showHUD

A HUD will automatically hide the main window and show a compact message at the bottom of the screen.

#### Signature

```typescript
async function showHUD(
  title: string,
  options?: { clearRootSearch?: boolean; popToRootType?: PopToRootType }
): Promise<void>;
```

#### Example

```typescript
import { showHUD } from "@raycast/api";

export default async function Command() {
  await showHUD("Hey there 👋");
}
```

`showHUD` closes the main window when called, so you can use the same options as `closeMainWindow`:

```typescript
import { PopToRootType, showHUD } from "@raycast/api";

export default async function Command() {
  await showHUD("Hey there 👋", { clearRootSearch: true, popToRootType: PopToRootType.Immediate });
}
```

#### Parameters

| Name                                    | Description                                                                                                                          | Type                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| title<mark style="color:red;">\*</mark> | The title that will be displayed in the HUD.                                                                                         | `string`                                                                              |
| options                                 | Can be used to control the behaviour after closing the main window.                                                                  | `Object`                                                                              |
| options.clearRootSearch                 | Clears the text in the root search bar and scrolls to the top                                                                        | `boolean`                                                                             |
| options.popToRootType                   | Defines the pop to root behavior (PopToRootType); the default is to to respect the user's "Pop to Root Search" preference in Raycast | [`PopToRootType`](https://developers.raycast.com/window-and-search-bar#poptoroottype) |

#### Return

A Promise that resolves when the HUD is shown.
