# Source: https://flatfile.com/docs/guides/theme-your-space.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Theming

> Learn how to customize the look and feel of Flatfile to match your brand

Flatfile supports modifying most UI elements including colors, fonts, borders, padding, and more via the [Space](/core-concepts/spaces) endpoint.

1. Start by simply updating `theme.root.primaryColor` and `theme.sidebar.logo` when calling `spaces.update()`.
2. If needed, you can customize the theme further with additional css variables.

## Building a theme

Learn how to create a Space with a theme, and update a theme from an Event listener.

```javascript  theme={null}
import api from "@flatfile/api";

export default function flatfileEventListener(listener) {
  //listen for space:configure job and build out space
  listener.filter({ job: "space:configure" }, (configure) => {});

  //theme during creation or update your space after it is created
  listener.on("space:created", async ({ context: { spaceId } }) => {
    const updateSpace = await api.spaces.update(spaceId, {
      metadata: {
        theme: {
          root: {
            primaryColor: "red",
          },
          sidebar: {
            logo: "https://image.png",
          },
          // See reference for all possible variables
        },
      },
    });
  });
}
```

See full code example in our [flatfile-docs-kitchen-sink Github repo](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main)

## Theme reference

### theme.root

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=3859fb8948836b90bb82ba9098366304" alt="Theme root configuration example" data-og-width="6640" width="6640" data-og-height="2092" height="2092" data-path="guides/assets/theme-root.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=751f0a219707a5871ff5a6f474cf7eae 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=307ad8892e73ec763cb0dc6fc6c44d1e 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=dfb25e84e64e854ef1bd2ee856e50544 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=14d095fc07c41fda99910478c0a9d2f6 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=68a20c42f012da93c6283fe52be804bb 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-root.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c94fd60cab80ea34d6ee9cea1355540c 2500w" />

<Tip>
  The sidebar, table and document will automatically inherit theming from your
  root variables!
</Tip>

#### Font

**fontFamily** `string`\
The font family used throughout the application. Only system fonts are supported at the moment

#### Colors

**primaryColor** `string`\
The primary color used throughout the application.

**dangerColor** `string`\
The color used for error messages.

**warningColor** `string`\
The color used for warning messages.

**borderColor** `string`\
The color used for borders throughout the application.

### theme.sidebar

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=38fa7b23ae2cb2f5c41f44e0a785291d" alt="Theme sidebar configuration example" data-og-width="6640" width="6640" data-og-height="2092" height="2092" data-path="guides/assets/theme-sidebar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c416d01df5f224739641f9402c2e72af 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f7bd00959195c916f1bfcac7ca6d2a4a 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e459dbb7f79022bcefb18e9b7a443f75 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=d689c41e71a186ba1c969b58fac80473 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a44ca680f141eefe702fde367b8da330 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-sidebar.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=03eef9c9db0420dce758abb68a888843 2500w" />

<Info>
  You can override the default colors of the sidebar below. If these are not set
  they will inherit from your root colors.
</Info>

**logo** `string`\
The img path for the logo displayed in the sidebar.

**textColor** `string`\
The color of the text in the sidebar.

**titleColor** `string`\
The color of the title in the sidebar.

**focusBgColor** `string`\
The background color of the active navigation link. The hover state will use the same color with 30% opacity applied.

**focusTextColor** `string`\
The text color of the active/focused navigation link.

**backgroundColor** `string`\
The background color of the sidebar.

### theme.table

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=135ba01937fe06ff3902e93a9330877b" alt="Theme table configuration example" data-og-width="1660" width="1660" data-og-height="523" height="523" data-path="guides/assets/theme-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=9428e2f93eefbf9a933a10b106e66af2 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=0425021aa31c07f453829757f96123cc 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=56a38e74e8d7fc914e75034f35a7cd83 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=bf1ceda1e5b49ec2d21e17332561b69f 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f8b9b1957cac22a48905b2934745dfab 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=89bd9a13bce898412a1b92049f2d02cc 2500w" />

<Info>
  You can override the default colors and values for different elements in the
  table below. If these are not set they will inherit from your root values.
</Info>

#### Font

**fontFamily** `string`\
The font family used throughout the table. Only system fonts are supported at the moment

#### Active cell

**cell.active.borderWidth** `string`\
The width of the border around the active cell.

**cell.active.borderShadow** `string`\
The box shadow around the active cell.

**cell.number.fontFamily** `string`\
The font family for number cells.

#### Column header

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=cefbbb05feb8cfbd7322029526c2fc8f" alt="Theme table column configuration" data-og-width="6640" width="6640" data-og-height="1396" height="1396" data-path="guides/assets/theme-table-column.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=9b908e59a402d684b4633131b084c3e7 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=fdb975660e974a6accfcc879e50d28de 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=42b9b992ae06da216a3d4a4a64df6f81 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=baa000382d0d92c15264d2c0ebc29860 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e6c5ebd5e12a48cb28df6580ff3219e6 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-column.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=075769db0674594bc6317fd06ce9e24b 2500w" />

**column.header.backgroundColor** `string`\
The background color of the column headers in the table.

**column.header.color** `string`\
The text color of the column headers in the table.

#### Index column

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=1a316e8340ab89380d30a3b9b374c2be" alt="Theme table index column configuration" data-og-width="6640" width="6640" data-og-height="2092" height="2092" data-path="guides/assets/theme-table-index-column.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=af84f28d42e4eaeb1f3c98e91ee97b81 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e63304a579c9e47c523c711c04b88516 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=da66c8579b67d2115a23368a692f8843 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a3aae207846154afeabbbab42843e81d 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=db524d9f1427d61dca5073e32cbdde8e 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-index-column.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a4664bd49a68d6677b06176f02bda004 2500w" />

**indexColumn.backgroundColor** `string`\
The background color of the first column in the table.

**indexColumn.color** `string`\
The text color of the first column in the table.

**indexColumn.selected.backgroundColor** `string`\
The background color of the first column in the table when selected.

#### Checkboxes

<img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=5a1111d7f33e1500c813bbab3a70b8fb" alt="Theme table inputs configuration" data-og-width="1660" width="1660" data-og-height="523" height="523" data-path="guides/assets/theme-table-inputs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=9e98100f33ae5dbd4623ffa24b157d09 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ec9c14ef45d58e3903f89482ba5e5015 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=eea66ba7a8a7a1ea8f096d18bb503106 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ccacde00fcff768f3e3e6eae8e0ef65a 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ab336638296af83ea1d3083eb1e30ca2 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/theme-table-inputs.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=d7e7412d309304dcb5b0b9864d95534a 2500w" />

**inputs.checkbox.color** `string`\
The color of the checkboxes in the table.

**inputs.checkbox.borderColor** `string`\
The color of the border for the checkboxes in the table.

#### Filters

**filters.outerBorderRadius** `string`\
The border radius of the table filters

**filters.innerBorderRadius** `string`\
The border radius for the individual filters

**filters.outerBorder** `string`\
The border of the table filters. By default there is no border.

> When nested objects share the same border radius, small gaps may appear. To resolve this, adjust the inner and outer border radius on the filters to seamlessly fill any gaps.

#### Buttons

**buttons.iconColor** `string`\
The color of the icon buttons in the toolbar and table

**buttons.pill.color** `string`\
The color of the pill buttons in the toolbar

### theme.email

You can theme the guest invite emails as well as guest email verification emails via the properties below. These are sent to a guest when they are invited to a Space via the guest management page in your Space.

> Email theming is only available on the pro and enterprise plans.

**logo** `string`\
The URL of the image displayed at the top of the email

**textColor** `string`\
The color of the text in the email

**titleColor** `string`\
The color of the title in the email

**buttonBgColor** `string`\
The background color of the button

**buttonTextColor** `string`\
The text color of the button

**footerTextColor** `string`\
The text color of the footer text

**backgroundColor** `string`\
The background color of the email

#### theme.email.dark

If your default email theme (as set above) is light, we suggest adding a dark mode email theme. Different email providers handle dark and light mode differently. While Apple Mail and some other clients will respect dark mode variables, some email providers do not support dark mode and will display your default theme. We suggest you test your themes across various email clients before going to production to ensure consistent appearance.

**logo** `string`\
The URL of the image displayed at the top of the email in dark mode

**textColor** `string`\
The color of the text in the email in dark mode

**titleColor** `string`\
The color of the title in the email in dark mode

**buttonBgColor** `string`\
The background color of the button in dark mode

**buttonTextColor** `string`\
The text color of the button in dark mode

**footerTextColor** `string`\
The text color of the footer text in dark mode

**backgroundColor** `string`\
The background color of the email in dark mode

## Deprecation Notice

Flatfile's new design system released in Q1 2025 supports a more streamlined experience when configuring theme. The new system accepts a more limited set of properties, but ensures those supplied properties are cohesively applied across the application.

As a result, many of the original `theme.root` properties which applied to specific UI elements have been deprecated. We have taken steps to ensure some level of backwards compatibility for these properties in the new system - however we recommend any usage of these properties be updated to the new system as soon as possible.

## Example Project

Find the theming example in the Flatfile GitHub repository.

* [Clone the theming example in Typescript](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/typescript/theming/index.ts)
* [Clone the theming example in Javascript](https://github.com/FlatFilers/flatfile-docs-kitchen-sink/blob/main/javascript/theming/index.js)
