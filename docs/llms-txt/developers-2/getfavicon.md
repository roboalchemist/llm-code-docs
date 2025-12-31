# Source: https://developers.raycast.com/utilities/icons/getfavicon.md

# getFavicon

Icon showing the favicon of a website.

A favicon (favorite icon) is a tiny icon included along with a website, which is displayed in places like the browser's address bar, page tabs, and bookmarks menu.

![Favicon example](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-8383499b76a723de43e610079031cd2543c52a66%2Futils-favicon.png?alt=media)

## Signature

```ts
function getFavicon(
  url: string | URL,
  options?: {
    fallback?: Image.Fallback;
    size?: boolean;
    mask?: Image.Mask;
  },
): Image.ImageLike;
```

* `name` is a string of the subject's name.
* `options.fallback` is a [Image.Fallback](https://developers.raycast.com/api-reference/user-interface/icons-and-images#image.fallback) icon in case the Favicon is not found. By default, the fallback will be `Icon.Link`.
* `options.size` is the size of the returned favicon. By default, it is 64 pixels.
* `options.mask` is the size of the [Image.Mask](https://developers.raycast.com/api-reference/user-interface/icons-and-images#image.mask) to apply to the favicon.

Returns an [Image.ImageLike](https://developers.raycast.com/api-reference/user-interface/icons-and-images) that can be used where Raycast expects them.

## Example

```tsx
import { List } from "@raycast/api";
import { getFavicon } from "@raycast/utils";

export default function Command() {
  return (
    <List>
      <List.Item icon={getFavicon("https://raycast.com")} title="Raycast Website" />
    </List>
  );
}
```
