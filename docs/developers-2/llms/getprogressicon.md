# Source: https://developers.raycast.com/utilities/icons/getprogressicon.md

# getProgressIcon

Icon to represent the progress of a task, a project, *something*.

![Progress Icon example](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-8d31dd8b07fabd4eba1a4ab2d4f256bc50f0fb9c%2Futils-progress-icon.png?alt=media)

## Signature

```ts
function getProgressIcon(
  progress: number,
  color?: Color | string,
  options?: {
    background?: Color | string;
    backgroundOpacity?: number;
  },
): Image.Asset;
```

* `progress` is a number between 0 and 1 (0 meaning not started, 1 meaning finished).
* `color` is a Raycast `Color` or a hexadecimal representation of a color. By default it will be `Color.Red`.
* `options.background` is a Raycast `Color` or a hexadecimal representation of a color for the background of the progress icon. By default, it will be `white` if the Raycast's appearance is `dark`, and `black` if the appearance is `light`.
* `options.backgroundOpacity` is the opacity of the background of the progress icon. By default, it will be `0.1`.

Returns an [Image.Asset](https://developers.raycast.com/api-reference/user-interface/icons-and-images) that can be used where Raycast expects them.

## Example

```tsx
import { List } from "@raycast/api";
import { getProgressIcon } from "@raycast/utils";

export default function Command() {
  return (
    <List>
      <List.Item icon={getProgressIcon(0.1)} title="Project" />
    </List>
  );
}
```
