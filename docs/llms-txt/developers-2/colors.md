# Source: https://developers.raycast.com/api-reference/user-interface/colors.md

# Colors

Anywhere you can pass a color in a component prop, you can pass either:

* A standard [Color](#color)
* A [Dynamic](#color.dynamic) Color
* A [Raw](#color.raw) Color

## API Reference

### Color

The standard colors. Use those colors for consistency.

The colors automatically adapt to the Raycast theme (light or dark).

#### Example

```typescript
import { Color, Icon, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="Blue" icon={{ source: Icon.Circle, tintColor: Color.Blue }} />
      <List.Item title="Green" icon={{ source: Icon.Circle, tintColor: Color.Green }} />
      <List.Item title="Magenta" icon={{ source: Icon.Circle, tintColor: Color.Magenta }} />
      <List.Item title="Orange" icon={{ source: Icon.Circle, tintColor: Color.Orange }} />
      <List.Item title="Purple" icon={{ source: Icon.Circle, tintColor: Color.Purple }} />
      <List.Item title="Red" icon={{ source: Icon.Circle, tintColor: Color.Red }} />
      <List.Item title="Yellow" icon={{ source: Icon.Circle, tintColor: Color.Yellow }} />
      <List.Item title="PrimaryText" icon={{ source: Icon.Circle, tintColor: Color.PrimaryText }} />
      <List.Item title="SecondaryText" icon={{ source: Icon.Circle, tintColor: Color.SecondaryText }} />
    </List>
  );
}
```

#### Enumeration members

| Name          | Dark Theme                                                                                                                                                                                                                | Light Theme                                                                                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blue          | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-bb792f0278bbeea127bab32134a0addabe1f471d%2Fcolor-dark-blue.webp?alt=media)           | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-b5fd11b78553af9231fec2bbd2065fa5b21daccd%2Fcolor-blue.webp?alt=media)           |
| Green         | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-1f26f61f56df07565cd4749355f553c998856c75%2Fcolor-dark-green.webp?alt=media)          | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-0ecfe804320264a9ea87283aaa994930f7cb4d7d%2Fcolor-green.webp?alt=media)          |
| Magenta       | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-460fbc6e16fa66a017a31462d181e1b7db1299f1%2Fcolor-dark-magenta.webp?alt=media)        | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-aab0de01b6ee3f98eedd291af31708cc27c1bceb%2Fcolor-magenta.webp?alt=media)        |
| Orange        | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-5c867edbcb01e9fb71ddbfd0351ec7e19cadbec2%2Fcolor-dark-orange.webp?alt=media)         | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-a80e366e832757469108afcaddff62f3aeb1d3a0%2Fcolor-orange.webp?alt=media)         |
| Purple        | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-6e5cba871d9c05aa374915445a220b40f3838aeb%2Fcolor-dark-purple.webp?alt=media)         | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-eb0b963fade8b81c5680524e646b95ebb223476e%2Fcolor-purple.webp?alt=media)         |
| Red           | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-ffb7f9534f418f2c52ff9983abbb886df9496f9f%2Fcolor-dark-red.webp?alt=media)            | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-73815c38fa3cbc20735f01160de3d9172a277cb1%2Fcolor-red.webp?alt=media)            |
| Yellow        | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-970d9768755133d23b1e27ff90b72b78e4753bad%2Fcolor-dark-yellow.webp?alt=media)         | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-656146171a1eb17d688bb5bc16eb442f955a6cf3%2Fcolor-yellow.webp?alt=media)         |
| PrimaryText   | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-46bb91f2a4e7d5a5ebe2b6e358560c6f5933ed47%2Fcolor-dark-primary-text.webp?alt=media)   | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-a2b368984466f481e372240d508588bb603f88bb%2Fcolor-primary-text.webp?alt=media)   |
| SecondaryText | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-eb8e7a97fd21d5853b9c40bc47634e4b8033585e%2Fcolor-dark-secondary-text.webp?alt=media) | ![](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-6302cb6111a94d075871bbc02b7d39b124eb70dd%2Fcolor-secondary-text.webp?alt=media) |

## Types

### Color.ColorLike

```typescript
ColorLike: Color | Color.Dynamic | Color.Raw;
```

Union type for the supported color types.

When using a [Raw Color](#color.raw), it will be adjusted to achieve high contrast with the Raycast user interface. To disable color adjustment, you need to switch to using a [Dynamic Color](#color.dynamic). However, we recommend leaving color adjustment on, unless your extension depends on exact color reproduction.

#### Example

```typescript
import { Color, Icon, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item title="Built-in color" icon={{ source: Icon.Circle, tintColor: Color.Red }} />
      <List.Item title="Raw color" icon={{ source: Icon.Circle, tintColor: "#FF0000" }} />
      <List.Item
        title="Dynamic color"
        icon={{
          source: Icon.Circle,
          tintColor: {
            light: "#FF01FF",
            dark: "#FFFF50",
            adjustContrast: true,
          },
        }}
      />
    </List>
  );
}
```

### Color.Dynamic

A dynamic color applies different colors depending on the active Raycast theme.

When using a [Dynamic Color](#color.dynamic), it will be adjusted to achieve high contrast with the Raycast user interface. To disable color adjustment, you can set the `adjustContrast` property to `false`. However, we recommend leaving color adjustment on, unless your extension depends on exact color reproduction.

#### Example

```typescript
import { Icon, List } from "@raycast/api";

export default function Command() {
  return (
    <List>
      <List.Item
        title="Dynamic Tint Color"
        icon={{
          source: Icon.Circle,
          tintColor: {
            light: "#FF01FF",
            dark: "#FFFF50",
            adjustContrast: false,
          },
        }}
      />
      <List.Item
        title="Dynamic Tint Color"
        icon={{
          source: Icon.Circle,
          tintColor: { light: "#FF01FF", dark: "#FFFF50" },
        }}
      />
    </List>
  );
}
```

#### Properties

| Property                                | Description                                                         | Type      |
| --------------------------------------- | ------------------------------------------------------------------- | --------- |
| dark<mark style="color:red;">\*</mark>  | The color which is used in dark theme.                              | `string`  |
| light<mark style="color:red;">\*</mark> | The color which is used in light theme.                             | `string`  |
| adjustContrast                          | Enables dynamic contrast adjustment for light and dark theme color. | `boolean` |

### Color.Raw

A color can also be a simple string. You can use any of the following color formats:

* HEX, e.g `#FF0000`
* Short HEX, e.g. `#F00`
* RGBA, e.g. `rgb(255, 0, 0)`
* RGBA Percentage, e.g. `rgb(255, 0, 0, 1.0)`
* HSL, e.g. `hsla(200, 20%, 33%, 0.2)`
* Keywords, e.g. `red`
