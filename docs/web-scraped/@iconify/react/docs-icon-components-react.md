# Source: https://iconify.design/docs/icon-components/react/

Title: Iconify

URL Source: https://iconify.design/docs/icon-components/react/

Markdown Content:
## Iconify for React [​](https://iconify.design/docs/icon-components/react/#iconify-for-react)

Iconify offers native icon components for several popular UI frameworks.

Iconify for React is one of such components.

Yet another icon component? What are the advantages over other icon components?

*   One syntax for over 275,000 icons from 200+ icon sets.
*   Renders SVG. Many components simply render icon fonts, which look ugly. Iconify uses only pixel perfect SVG.
*   Loads icons on demand. No need to bundle icons, component will automatically load icon data for icons that you use from Iconify API.

## Installation [​](https://iconify.design/docs/icon-components/react/#installation)

If you are using NPM:

`npm install --save-dev @iconify/react`

If you are using Yarn:

`yarn add --dev @iconify/react`

### Version 4 [​](https://iconify.design/docs/icon-components/react/#version-4)

As of version 5, the component is a modern functional component that uses React hooks.

If you want to use the icon component with an older version of React, you can install version 4 using @legacy tag:

`npm install --save-dev @iconify/react@legacy`

## Usage [​](https://iconify.design/docs/icon-components/react/#usage)

Install @iconify/react and import Icon component from it:

js

`import { Icon } from "@iconify/react";`

Then use Icon component with icon name as icon parameter:

jsx

`<Icon icon="mdi-light:home" />`

Component will automatically retrieve data for mdi-light:home from Iconify API and render it. There are over 275,000 icons available on Iconify API from various free and open source icon sets, including all the most popular icon sets.

Availability of Iconify API is the biggest feature that makes Iconify components different from alternatives.

API sends data for icons on demand. Loading icons on demand has massive advantages over other methods:

*   There can be an unlimited number of icons, giving you more choices. Icons you do not use are not loaded.
*   No useless data. Icon sets usually have thousands of icons. Instead of bundling all icons, component retrieves only icons you use.

### Next.js [​](https://iconify.design/docs/icon-components/react/#ssr)

Component is compatible with the latest Next.js.

Unfortunately, Next.js currently does not support useState in components, making it impossible to use the same stateful components on server and client, so the icon component is a client-only component. SVG will not be rendered on server.

Additionally, to avoid hydration errors, component renders SVG only after it is mounted, which can sometimes cause a tiny delay. If you are using Next.js or similar framework, consider switching to [Iconify Icon web component](https://iconify.design/docs/iconify-icon/).

If you do want to render SVGs without a delay, provide [icon data](https://iconify.design/docs/types/iconify-icon.html) as parameter instead of icon name or use a different way to render icons, such as:

*   [Iconify Icon web component](https://iconify.design/docs/iconify-icon/)
*   [Unplugin Icons](https://iconify.design/docs/usage/svg/unplugin/)
*   [Tailwind CSS with Iconify plugin](https://iconify.design/docs/usage/css/tailwind/iconify/)
*   [UnoCSS with icons preset](https://iconify.design/docs/usage/css/unocss/)

## Properties [​](https://iconify.design/docs/icon-components/react/#properties)

You can pass any custom properties to Icon.

Required properties:

*   icon, [IconifyIcon](https://iconify.design/docs/types/iconify-icon.html "IconifyIcon documentation")|string icon name or icon data.

Optional properties:

*   inline, boolean changes vertical alignment.
*   width, string|number icon width.
*   height, string|number icon height.
*   hFlip, boolean flips icon horizontally.
*   vFlip, boolean flips icon vertically.
*   flip, string alternative to hFlip and vFlip.
*   rotate, number|string rotates icon.
*   color, string changes icon color.
*   onLoad, function is a callback that is called when icon data has been loaded. See below.

See below for more information on each optional property.

In addition to the properties mentioned above, the icon component accepts any other properties and events. All other properties and events will be passed to generated SVG element, so you can do stuff like assigning onClick event, setting the inline style, add title and so on.

## Icon [​](https://iconify.design/docs/icon-components/react/#icon)

Icon name is a string, which has 3 parts:

@api-provider:icon-prefix:icon-name
provider prefix name

*   provider points to API source. Starts with "@", can be empty (empty value is used for public Iconify API).
*   prefix is name of icon set.
*   name is name of icon.

Examples of valid icon names:

*   flat-color-icons:voice-presentation - icon is "voice-presentation" from [Flat Color Icons](https://icon-sets.iconify.design/flat-color-icons/) icon set, from public Iconify API.
*   mdi-light:home - icon is "home" from [Material Design Light](https://icon-sets.iconify.design/mdi-light/) icon set, from public Iconify API.

Exceptions:

*   If the API provider is empty, it can be skipped (like in examples above).
*   If prefix does not contain "-", prefix and icon name can be separated with hyphen. This is to support people migrating from icon fonts. For example, fa:arrow-left and fa-arrow-left are identical because "fa" does not contain hyphen.

There are over 275,000 icons available from 200+ icon sets. [Browse icons sets](https://icon-sets.iconify.design/) to see all available icons.

You can also add custom API providers for more icon choices. See [API providers documentation](https://iconify.design/docs/api/providers.html).

## Color [​](https://iconify.design/docs/icon-components/react/#color)

You can only change the color of monotone icons. Some icons, such as emoji, have a hardcoded palette that cannot be changed.

To add color to a monotone icon, simply change text color.

jsx

`<Icon icon="mdi:home" style={{ color: "red" }} />`

For various ways to set color, see [how to change icon color in Iconify for React](https://iconify.design/docs/icon-components/react/color.html).

## Dimensions [​](https://iconify.design/docs/icon-components/react/#dimensions)

By default, icon height is set to "1em", icon width is changed dynamically based on the icon's width/height ratio. This makes it easy to change icon size by changing font-size in the stylesheet, just like icon fonts.

There are several ways to change icon dimensions:

*   Setting font-size in style (or fontSize if you are using inline style).
*   Setting width and/or height property.

Values for width and height can be numbers or strings.

If you set only one dimension, another dimension will be calculated using the icon's width/height ratio. For example, if the icon size is 16 x 24, you set the height to 48, the width will be set to 32. Calculations work not only with numbers, but also with string values.

jsx

`<Icon icon="mdi:home" style={{ fontSize: "24px" }} />`

For various ways to change icon dimensions, see [how to change icon dimensions in Iconify for React](https://iconify.design/docs/icon-components/react/dimensions.html).

## Transformations [​](https://iconify.design/docs/icon-components/react/#transformations)

An icon can be rotated and flipped horizontally and/or vertically. All transformations are done relative to the center of the icon.

These are not CSS transformations, transformations are applied inside SVG.

For more details see [how to transform icon in Iconify for React](https://iconify.design/docs/icon-components/react/transform.html).

## onLoad [​](https://iconify.design/docs/icon-components/react/#onload)

onLoad property is an optional callback function. It is called when icon data has been loaded.

It is not an event, such as click event for links, it is a simple callback function.

When onLoad is called:

*   If value of icon property is an object, onLoad is not called.
*   If value of icon property is a string and icon data is available, onLoad is called on first render.
*   If value of icon property is a string and icon data is not available, onLoad is called on first re-render after icon data is retrieved from API.

What is the purpose of onLoad? To let you know when Icon component renders an icon and when it does not render anything. This allows you to do things like adding class name for the parent element, such as "container--with-icon" that modify layout if icon is being displayed.

## Functions [​](https://iconify.design/docs/icon-components/react/#functions)

Component exports various functions, which developers can use to control icons.

Functions are split in several groups (click function name to see more details and examples):

### Check available icons [​](https://iconify.design/docs/icon-components/react/#getting-icons)

There are several functions in this section:

*   [iconLoaded(name)](https://iconify.design/docs/icon-components/react/icon-exists.html "iconLoaded() documentation"). Checks if icon data is available, returns boolean.
*   [listIcons()](https://iconify.design/docs/icon-components/react/list-icons.html "listIcons() documentation"). Lists available icons, returns string[].
*   [getIcon(name)](https://iconify.design/docs/icon-components/react/get-icon.html "getIcon() documentation"). Returns icon data, returns [IconifyIcon](https://iconify.design/docs/types/iconify-icon.html "IconifyIcon documentation") object.

### Adding icons [​](https://iconify.design/docs/icon-components/react/#adding-icons)

Functions for adding icons to the component:

*   [addIcon()](https://iconify.design/docs/icon-components/react/add-icon.html "addIcon() documentation"). Adds one icon.
*   [addCollection()](https://iconify.design/docs/icon-components/react/add-collection.html "addCollection() documentation"). Adds an icon set.

Note: icons added to the component with these functions are not stored in the icon data cache. Component caches only icons retrieved from API.

### Custom loaders [​](https://iconify.design/docs/icon-components/react/#custom-loaders)

Custom loaders can be used to load icons from custom sources:

*   [setCustomIconLoader()](https://iconify.design/docs/icon-components/react/custom-loaders.html "setCustomIconLoader() documentation"). Loads one icon.
*   [setCustomIconsLoader()](https://iconify.design/docs/icon-components/react/custom-loaders.html "setCustomIconsLoader() documentation"). Loads icons in bulk.

Loaders are set per icon set prefix. Make sure to configure loader before displaying any icons.

It can also be used to customise icons: in custom loader you can load icon from API using [loadIcon](https://iconify.design/docs/icon-components/react/load-icon.html "loadIcon() documentation"), change its content (such as colors or stroke width) and return modified icon.

### Helper functions [​](https://iconify.design/docs/icon-components/react/#helper)

*   [replaceIDs(html)](https://iconify.design/docs/icon-components/react/replace-ids.html "replaceIDs() documentation"). Randomises IDs in generated string. This should be used when rendering icon based on data returned by [getIcon()](https://iconify.design/docs/icon-components/react/get-icon.html "getIcon() documentation") to make sure elements inside each icon have unique IDs.
*   calculateSize(). Calculates icon size. It is used to calculate width if only height is set and vice versa.
*   [buildIcon(icon, customisations?)](https://iconify.design/docs/icon-components/react/build-icon.html "buildIcon() documentation"). Generates data used by icon component. This can be used if you prefer to generate <svg> yourself. Data includes attributes for <svg> and inner HTML.

### API functions [​](https://iconify.design/docs/icon-components/react/#api)

*   [loadIcons(icons, callback?)](https://iconify.design/docs/icon-components/react/load-icons.html "loadIcons() documentation"). Loads icons from API, calls optional callback when either all or part of icons have been loaded.
*   [loadIcon(icon)](https://iconify.design/docs/icon-components/react/load-icon.html "loadIcon() documentation"). Loads one icon from API, returns Promise.
*   [addAPIProvider()](https://iconify.design/docs/icon-components/react/add-api-provider.html "addAPIProvider() documentation"). Adds custom API provider. See [API providers documentation](https://iconify.design/docs/api/providers.html).

### Internal API functions [​](https://iconify.design/docs/icon-components/react/#internal)

There are several internal API functions that are exposed. They are intended to be used by developers that need more control over the component. For example, it is used in Sketch and Figma plug-ins. Use them carefully.

All internal API functions are exposed as properties of _api object:

*   getAPI(). Returns internal API module.
*   getAPIConfig(). Returns API configuration.
*   setAPIModule(provider). Sets API module for provider. This is an experimental function intended for custom API providers that use custom module for retrieving data from API.
*   setFetch(fetch). Set custom Fetch API.
*   getFetch(). Returns used fetch() function, null if Fetch API is not available.
