# Source: https://docs.expo.dev/versions/latest/sdk/router

---
title: Router
description: A file-based routing library for React Native and web applications.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Router

A file-based routing library for React Native and web applications.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-router` is a routing library for React Native and web apps. It enables navigation management using a file-based routing system and provides native navigation components and is built on top of [React Navigation](https://reactnavigation.org/).

[Expo Router guides](/router/introduction) — Learn about Expo Router basics, navigation patterns, core concepts, and more.

## Installation

To use Expo Router in your project, you need to install. Follow the instructions from the Expo Router's installation guide:

[Install Expo Router](/router/installation) — Learn how to install Expo Router in your project.

## Configuration in app config

If you are using the [default](/more/create-expo#--template) template to create a new project, `expo-router`'s [config plugin](/config-plugins/introduction) is already configured in your app config.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": ["expo-router"]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `root` | `"app"` | Changes the routes directory from `app` to another value. Avoid using this property unless you have a specific need. |
| `origin` | `undefined` | Production origin URL where assets in the public folder are hosted. The fetch function is polyfilled to support relative requests from this origin in production. The development origin is inferred using the Expo CLI development server. |
| `headOrigin` | `undefined` | A more specific origin URL used in the `expo-router/head` module for iOS handoff. Defaults to `origin`. |
| `asyncRoutes` | `undefined` | Enable async routes (lazy loading). Can be a boolean, a string (`"development"` or `"production"`), or an object with platform-specific values (`{ android, ios, web, default }`). `production` is currently web-only and will be disabled on native. |
| `platformRoutes` | `true` | Enable or disable platform-specific routes (for example, **index.android.tsx** and **index.ios.tsx**). |
| `sitemap` | `true` | Enable or disable the automatically generated sitemap at **/_sitemap**. |
| `partialRouteTypes` | `true` | Enable partial typed routes generation. This allows TypeScript to provide type checking for routes without requiring all routes to be statically known. |
| `redirects` | `undefined` | An array of static redirect rules. Each rule should have `source`, `destination`, and optionally `permanent` (defaults to `false`) and `methods` (HTTP methods to redirect). |
| `rewrites` | `undefined` | An array of static rewrite rules. Each rule should have `source`, `destination`, and optionally `methods` (HTTP methods to rewrite). |
| `headers` | `undefined` | A list of headers that are set on every route response from the server. The value can be a string or an array of strings. |
| `disableSynchronousScreensUpdates` | `false` | Disable synchronous layout updates for native screens. This can help with performance in some cases. |
| `unstable_useServerMiddleware` | `false` | , Experimental. Enable server middleware support with a `+middleware.ts` file. Requires `web.output: "server"` to be set in app config. |
| `unstable_useServerDataLoaders` | `false` | , Experimental. Enable data loader support. This is only supported for `web.output: "static"` outputs at the moment. |
| `unstable_useServerRendering` | `false` | , Experimental. Enable server-side rendering. When enabled with `web.output: "server"`, HTML is rendered at request time instead of being pre-rendered at build time. |

## Usage

For information core concepts, notation patterns, navigation layouts, and common navigation patterns, start with Router 101 section:

[Router 101](/router/basics/core-concepts)

## API

```js
import { Stack, Tabs, Link } from 'expo-router';
```

## Components

### `Link`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LinkProps](#linkprops)\>

Component that renders a link using [`href`](#href) to another route. By default, it accepts children and wraps them in a `<Text>` component.

Uses an anchor tag (`<a>`) on web and performs a client-side navigation to preserve the state of the website and navigate faster. The web-only attributes such as `target`, `rel`, and `download` are supported and passed to the anchor tag on web. See [`WebAnchorProps`](#webanchorprops) for more details.

> **Note**: Client-side navigation works with both single-page apps, and [static-rendering](/router/reference/static-rendering).

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/about">About</Link>
  </View>
 );
}
```

LinkProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Used to customize the `Link` component. It will forward all props to the first child of the `Link`. Note that the child component must accept `onPress` or `onClick` props. The `href` and `role` are also passed to the child.

Example

```tsx
import { Link } from 'expo-router';
import { Pressable, Text } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/home" asChild>
     <Pressable>
      <Text>Home</Text>
     </Pressable>
   </Link>
  </View>
 );
}
```

### `className`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

On native, this can be used with CSS interop tools like Nativewind. On web, this sets the HTML `class` directly.

### `dangerouslySingular`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [SingularOptions](#singularoptions)

When navigating in a Stack, if the target is valid then screens in the history that matches the uniqueness constraint will be removed.

If used with `push`, the history will be filtered even if no navigation occurs.

### `dismissTo`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

While in a stack, this will dismiss screens until the provided `href` is reached. If the href is not found, it will instead replace the current screen with the provided `href`.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link dismissTo href="/feed">Close modal</Link>
  </View>
 );
}
```

### `href`

Supported platforms: Android, iOS, tvOS, Web.

Literal type: `union`

The path of the route to navigate to. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/about">About</Link>
   <Link
    href={{
      pathname: '/user/[id]',
      params: { id: 'bacon' }
    }}>
      View user
   </Link>
  </View>
 );
}
```

Acceptable values are: `string` | [HrefObject](#hrefobject)

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: (event: [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)<[HTMLAnchorElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement), [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)\> | GestureResponderEvent) => void

This function is called on press. Text intrinsically supports press handling with a default highlight state (which can be disabled with suppressHighlighting).

### `prefetch`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Prefetches the route when the component is rendered on a focused screen.

### `push`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Always pushes a new route, and never pops or replaces to existing route. You can push the current route multiple times or with new parameters.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link push href="/feed">Login</Link>
  </View>
 );
}
```

### `ref`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: Ref<[Text](https://reactnative.dev/docs/text)\>

### `relativeToDirectory`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.

> **See:** [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).

### `replace`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Removes the current route from the history and replace it with the specified URL. This is useful for [redirects](/router/reference/redirects).

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link replace href="/feed">Login</Link>
  </View>
 );
}
```

### `withAnchor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Replaces the initial screen with the current route.

#### Inherited Props

-   [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<[TextProps](https://reactnative.dev/docs/text#props), 'href'\>
-   [WebAnchorProps](#webanchorprops)

### `Stack`

Supported platforms: Android, iOS, tvOS, Web.

Renders a native stack navigator.

### `Tabs`

Supported platforms: Android, iOS, tvOS, Web.

Renders a tabs navigator.

### `Badge`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BadgeProps](#badgeprops)\>

BadgeProps

#### Inherited Props

-   [NativeTabsTriggerBadgeProps](/versions/v55.0.0/sdk/router-native-tabs#nativetabstriggerbadgeprops)
-   [StackToolbarBadgeProps](#stacktoolbarbadgeprops)

### `ErrorBoundary`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ErrorBoundaryProps](#errorboundaryprops)\>

Props passed to a page's `ErrorBoundary` export.

ErrorBoundaryProps

### `error`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

The error that was thrown.

### `retry`

Supported platforms: Android, iOS, tvOS, Web.

Type: () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\>

A function that will re-render the route component by clearing the `error` state.

### `Icon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconProps](#iconprops)\>

IconProps

#### Inherited Props

-   [NativeTabsTriggerIconProps](/versions/v55.0.0/sdk/router-native-tabs#nativetabstriggericonprops)
-   [StackToolbarIconProps](#stacktoolbariconprops)

### `Label`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LabelProps](#labelprops)\>

LabelProps

#### Inherited Props

-   [NativeTabsTriggerLabelProps](/versions/v55.0.0/sdk/router-native-tabs#nativetabstriggerlabelprops)
-   [StackToolbarLabelProps](#stacktoolbarlabelprops)

### `Redirect`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RedirectProps](#redirectprops)\>

Redirects to the `href` as soon as the component is mounted.

Example

```tsx
import { View, Text } from 'react-native';
import { Redirect } from 'expo-router';

export default function Page() {
 const { user } = useAuth();

 if (!user) {
   return <Redirect href="/login" />;
 }

 return (
   <View>
     <Text>Welcome Back!</Text>
   </View>
 );
}
```

RedirectProps

### `href`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Href](/versions/v55.0.0/sdk/router#href-1)

The path of the route to navigate to. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

Example

```tsx
import { Redirect } from 'expo-router';

export default function RedirectToAbout() {
 return (
   <Redirect href="/about" />
 );
}
```

### `relativeToDirectory`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.

> **See:** [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).

### `withAnchor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Replaces the initial screen with the current route.

### `Slot`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<NavigatorProps<any\>, 'children'\>\>

Renders the currently selected content.

There are actually two different implementations of `<Slot/>`:

-   Used inside a `_layout` as the `Navigator`
-   Used inside a `Navigator` as the content

Since a custom `Navigator` will set the `NavigatorContext.contextKey` to the current `_layout`, you can use this to determine if you are inside a custom navigator or not.

### `VectorIcon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[VectorIconProps](/versions/v55.0.0/sdk/router#vectoriconprops)<NameT\>\>

Helper component for loading vector icons.

Prefer using the `md` and `sf` props on `Icon` rather than using this component directly. Only use this component when you need to load a specific icon from a vector icon family.

Example

```tsx
import { Icon, VectorIcon } from 'expo-router';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';

<Icon src={<VectorIcon family={MaterialCommunityIcons} name="home" />} />
```

VectorIconProps

### `family`

Supported platforms: Android, iOS, tvOS, Web.

Type: { getImageSource: (name: NameT, size: number, color: [ColorValue](https://reactnative.dev/docs/colors)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | null\> }

The family of the vector icon.

Example

```tsx
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
```

### `name`

Supported platforms: Android, iOS, tvOS, Web.

Type: `NameT`

The name of the vector icon.

### `Link.AppleZoom`

Supported platforms: iOS 18+.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LinkAppleZoomProps](#linkapplezoomprops)\>

When this component is used inside a Link, [zoom transition](https://developer.apple.com/documentation/uikit/enhancing-your-app-with-fluid-transitions?language=objc) will be used when navigating to the link's href.

LinkAppleZoomProps

### `alignmentRect`

Supported platforms: iOS 18+.

Optional • Type: `{ height: number, width: number, x: number, y: number }`

Defines the rectangle used for the zoom transition's alignment. This rectangle is specified in the zoomed screen's coordinate space.

#### Inherited Props

-   `PropsWithChildren`

### `Link.AppleZoomTarget`

Supported platforms: iOS 18+.

Type: React.Iterable<{ children: [ReactNode](https://reactnative.dev/docs/react-node) }\>

Defines the target for an Apple zoom transition.

Example

```tsx
import { Link } from 'expo-router';

export default function Screen() {
 return (
  <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
   <Link.AppleZoomTarget>
     <Image source={require('../assets/image.png')} style={{ width: 200, height: 200 }} />
   </Link.AppleZoomTarget>
  </View>
 );
}
```

### `Link.Menu`

Supported platforms: iOS.

Type: React.Element<[LinkMenuProps](#linkmenuprops)\>

Groups context menu actions for a link.

If multiple `Link.Menu` components are used within a single `Link`, only the first will be rendered. Only `Link.MenuAction` and `Link.Menu` components are allowed as children.

Example

```tsx
<Link.Menu>
  <Link.MenuAction title="Action 1" onPress={() => {}} />
  <Link.MenuAction title="Action 2" onPress={() => {}} />
</Link.Menu>
```

LinkMenuProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `destructive`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/destructive) for more information.

> **Deprecated:** Use `palette` prop instead.

### `displayAsPalette`

Supported platforms: iOS.

Optional • Type: `boolean`

> **Deprecated:** Use `inline` prop instead.

### `displayInline`

Supported platforms: iOS.

Optional • Type: `boolean`

### `elementSize`

Supported platforms: iOS 16.0+.

Optional • Literal type: `string`

The preferred size of the menu elements. `elementSize` property is ignored when `palette` is used.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize) for more information.

Acceptable values are: `'small'` | `'auto'` | `'medium'` | `'large'`

### `icon`

Supported platforms: iOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

Optional SF Symbol displayed alongside the menu item.

### `image`

Supported platforms: iOS.

Optional • Literal type: `union`

Custom image loaded using `useImage()` hook from `expo-image`. Takes priority over `icon` (SF Symbol) when both are provided.

Example

```tsx
import { useImage } from 'expo-image';
import { Link } from 'expo-router';

const customIcon = useImage('https://simpleicons.org/icons/expo.svg', {
  maxWidth: 24,
  maxHeight: 24,
});

<Link.Menu image={customIcon} title="Menu">
  <Link.MenuAction title="Action" onPress={() => {}} />
</Link.Menu>
```

Acceptable values are: `ImageRef` | `null`

### `inline`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be displayed inline. This means that the menu will not be collapsed

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayinline) for more information.

### `palette`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be displayed as a palette. This means that the menu will be displayed as one row. The `elementSize` property is ignored when palette is used, all items will be `elementSize="small"`. Use `elementSize="medium"` instead of `palette` to display actions with titles horizontally.

> **Note**: Palette menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayaspalette) for more information.

### `subtitle`

Supported platforms: iOS.

Optional • Type: `string`

An optional subtitle for the submenu. Does not appear on `inline` menus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

### `title`

Supported platforms: iOS.

Optional • Type: `string`

The title of the menu item

### `Link.MenuAction`

Supported platforms: iOS.

Type: React.Element<[LinkMenuActionProps](#linkmenuactionprops)\>

This component renders a context menu action for a link. It should only be used as a child of `Link.Menu` or `LinkMenu`.

LinkMenuActionProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The title of the menu item.

### `destructive`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be disabled and not selectable.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/disabled) for more information.

### `discoverabilityLabel`

Supported platforms: iOS.

Optional • Type: `string`

An elaborated title that explains the purpose of the action.

### `hidden`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

Whether the menu element should be hidden.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/hidden) for more information.

### `icon`

Supported platforms: iOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

SF Symbol displayed alongside the menu item.

### `image`

Supported platforms: iOS.

Optional • Literal type: `union`

Custom image loaded using `useImage()` hook from `expo-image`. Takes priority over `icon` (SF Symbol) when both are provided.

Example

```tsx
import { useImage } from 'expo-image';
import { Link } from 'expo-router';

const customIcon = useImage('https://simpleicons.org/icons/expo.svg', {
  maxWidth: 24,
  maxHeight: 24,
});

<Link.Menu title="Menu">
  <Link.MenuAction image={customIcon} title="Action" onPress={() => {}} />
</Link.Menu>
```

Acceptable values are: `ImageRef` | `null`

### `imageRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `isOn`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as selected.

### `onPress`

Supported platforms: iOS.

Optional • Type: `() => void`

### `subtitle`

Supported platforms: iOS.

Optional • Type: `string`

An optional subtitle for the menu item.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

> **Deprecated:** Use `children` prop instead.

### `title`

Supported platforms: iOS.

Optional • Type: `string`

The title of the menu item.

### `unstable_keepPresented`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be kept presented after the action is selected.

This is marked as unstable, because when action is selected it will recreate the menu, which will close all opened submenus and reset the scroll position.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented) for more information.

### `Link.Preview`

Supported platforms: iOS.

Type: React.Element<[LinkPreviewProps](#linkpreviewprops)\>

A component used to render and customize the link preview.

If `Link.Preview` is used without any props, it will render a preview of the `href` passed to the `Link`.

If multiple `Link.Preview` components are used within a single `Link`, only the first one will be rendered.

To customize the preview, you can pass custom content as children.

Example

```tsx
<Link href="/about">
  <Link.Preview>
    <Text>Custom Preview Content</Text>
  </Link.Preview>
</Link>
```

Example

```tsx
<Link href="/about">
  <Link.Preview />
</Link>
```

LinkPreviewProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `style`

Supported platforms: iOS.

Optional • Type: `LinkPreviewStyle`

Custom styles for the preview container.

Note that some styles may not work, as they are limited or reset by the native view

### `Link.Trigger`

Supported platforms: iOS.

Type: React.Iterable<[LinkTriggerProps](#linktriggerprops)\>

Serves as the trigger for a link. The content inside this component will be rendered as part of the base link.

If multiple `Link.Trigger` components are used within a single `Link`, only the first will be rendered.

Example

```tsx
<Link href="/about">
  <Link.Trigger>
    Trigger
  </Link.Trigger>
</Link>
```

LinkTriggerProps

### `withAppleZoom`

Supported platforms: iOS 18+.

Optional • Type: `boolean`

A shorthand for enabling the Apple Zoom Transition on this link trigger.

When set to `true`, the trigger will be wrapped with `Link.AppleZoom`. If another `Link.AppleZoom` is already used inside `Link.Trigger`, an error will be thrown.

#### Inherited Props

-   `PropsWithChildren`

### `Stack.Header`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackHeaderProps](#stackheaderprops)\>

The component used to configure header styling for a stack screen.

Use this component to set header appearance properties like blur effect, background color, and shadow visibility.

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Header
        blurEffect="systemMaterial"
        style={{ backgroundColor: '#fff' }}
      />
      <ScreenContent />
    </>
  );
}
```

Example

When used inside a layout with Stack.Screen:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Header blurEffect="systemMaterial" />
      </Stack.Screen>
    </Stack>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackHeaderProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom header component, replacing the default header entirely. Use this to implement fully custom header layouts.

### `blurEffect`

Supported platforms: iOS.

Optional • Type: `BlurEffectTypes`

The blur effect to apply to the header background on iOS. Common values include 'regular', 'prominent', 'systemMaterial', etc.

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements for custom header when `asChild` is true.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to hide the header completely. When set to `true`, the header will not be rendered.

### `largeStyle`

Supported platforms: iOS.

Optional • Type: StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent' }\>

Style properties for the large title header (iOS).

-   `backgroundColor`: Background color of the large title header
-   `shadowColor`: Set to 'transparent' to hide the large title shadow/border

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), color: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent' }\>

Style properties for the standard-sized header.

-   `color`: Tint color for header elements (similar to tintColor in React Navigation)
-   `backgroundColor`: Background color of the header
-   `shadowColor`: Set to 'transparent' to hide the header shadow/border

### `transparent`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the header should be transparent. When `true`, the header is absolutely positioned and content scrolls underneath.

Auto-enabled when:

-   `style.backgroundColor` is 'transparent'
-   `blurEffect` is set (required for blur to work)

### `Stack.Screen`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenProps](#stackscreenprops)\>

StackScreenProps

### `dangerouslySingular`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [SingularOptions](#singularoptions)

When enabled, the navigator will reuse an existing screen instead of pushing a new one.

Only supported when used inside a Layout component.

> **Deprecated:** Use `dangerouslySingular` instead.
> 
> Only supported when used inside a Layout component.

### `getId`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `(__namedParameters: { params: Record<string, any> }) => string | undefined`

Function to determine a unique ID for the screen.

### `initialParams`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `Record<string, any>`

Initial params to pass to the route.

Only supported when used inside a Layout component.

### `listeners`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Listeners for navigation events.

Only supported when used inside a Layout component.

Acceptable values are: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<undefined\> | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<TState, TEventMap\>

### `name`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

Name is required when used inside a Layout component.

### `options`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Options to configure the screen.

Accepts an object or a function returning an object. The function form `options={({ route }) => ({})}` is only supported when used inside a Layout component. When used inside a page component, pass an options object directly.

Acceptable values are: [NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options) | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => [NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options)

### `redirect`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render.

Only supported when used inside a Layout component.

#### Inherited Props

-   `PropsWithChildren`

### `Stack.SearchBar`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackSearchBarProps](#stacksearchbarprops)\>

A search bar component that integrates with the native stack header.

> **Note:** Using `Stack.SearchBar` will automatically make the header visible (`headerShown: true`), as the search bar is rendered as part of the native header.

To display the search bar in the bottom toolbar on iOS 26+, use `Stack.Toolbar.SearchBarSlot` inside `Stack.Toolbar`.

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.SearchBar
        placeholder="Search..."
        onChangeText={(text) => console.log(text)}
      />
     <ScreenContent />
    </>
  );
}
```

StackSearchBarProps

#### Inherited Props

-   `SearchBarProps`

### `Stack.Toolbar`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackToolbarProps](#stacktoolbarprops)\>

The component used to configure the stack toolbar.

-   Use `placement="left"` to customize the left side of the header.
-   Use `placement="right"` to customize the right side of the header.
-   Use `placement="bottom"` (default) to show a bottom toolbar (iOS only).

If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

> **Note:** Using `Stack.Toolbar` with `placement="left"` or `placement="right"` will automatically make the header visible (`headerShown: true`), as the toolbar is rendered as part of the native header.

> **Note:** `Stack.Toolbar` with `placement="bottom"` can only be used inside **page** components, not in layout components.

Example

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Toolbar placement="left">
          <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
        </Stack.Toolbar>
        <Stack.Toolbar placement="right">
          <Stack.Toolbar.Button icon="ellipsis.circle" onPress={() => alert('Right button pressed!')} />
        </Stack.Toolbar>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
      </Stack.Toolbar>
      <Stack.Toolbar>
        <Stack.Toolbar.Spacer />
        <Stack.Toolbar.Button icon="magnifyingglass" onPress={() => {}} />
        <Stack.Toolbar.Spacer />
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

StackToolbarProps

### `asChild`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom only) components.

### `placement`

Supported platforms: iOS.

Optional • Type: `ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

-   `'left'`: Renders items in the left area of the header.
-   `'right'`: Renders items in the right area of the header.
-   `'bottom'`: Renders items in the bottom toolbar (iOS only).

### `Tabs.Screen`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ScreenProps](#screenprops)<[TabsProps](/versions/v55.0.0/sdk/router-ui#tabsprops), [TabNavigationState](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase\>, BottomTabNavigationEventMap\>\>

### `Stack.Screen.BackButton`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenBackButtonProps](#stackscreenbackbuttonprops)\>

Component to configure the back button.

Can be used inside Stack.Screen in a layout or directly inside a screen component.

Example

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="detail">
        <Stack.Screen.BackButton displayMode="minimal">Back</Stack.Screen.BackButton>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Screen.BackButton hidden />
      <ScreenContent />
    </>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackScreenBackButtonProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The title to display for the back button.

### `displayMode`

Supported platforms: iOS.

Optional • Type: `BackButtonDisplayMode`

The display mode for the back button.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Whether to hide the back button.

### `src`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)

Custom image source for the back button.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `StyleProp<undefined>`

Style for the back button title.

### `withMenu`

Supported platforms: iOS.

Optional • Type: `boolean`

Whether to show a context menu when long pressing the back button.

### `Stack.Screen.Title`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenTitleProps](#stackscreentitleprops)\>

Component to set the screen title.

Can be used inside Stack.Screen in a layout or directly inside a screen component.

Example

String title in a layout:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Screen.Title large>Home</Stack.Screen.Title>
      </Stack.Screen>
    </Stack>
  );
}
```

Example

String title inside a screen:

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Screen.Title>My Page</Stack.Screen.Title>
      <ScreenContent />
    </>
  );
}
```

Example

Custom component as the title using `asChild`:

```tsx
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Screen.Title asChild>
          <MyCustomTitle />
        </Stack.Screen.Title>
      </Stack.Screen>
    </Stack>
  );
}
```

> **Note:** If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackScreenTitleProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Use this to render a custom component as the header title.

Example

```tsx
<Stack.Screen.Title asChild>
  <MyCustomTitle />
</Stack.Screen.Title>
```

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `React.ReactNode`

The title content. Pass a string for a plain text title, or a custom component when `asChild` is enabled.

### `large`

Supported platforms: iOS.

Optional • Type: `boolean`

Enables large title mode.

### `largeStyle`

Supported platforms: iOS.

Optional • Type: StyleProp<{ color: string, fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number\> }\>

Style properties for the large title header.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<{ color: string, fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number\>, textAlign: 'left' | 'center' }\>

### `Stack.Toolbar.Badge`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarBadgeProps](#stacktoolbarbadgeprops)\>\>

StackToolbarBadgeProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the badge

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[TextStyle](https://reactnative.dev/docs/text-style-props), 'fontFamily' | 'fontSize' | 'fontWeight' | 'backgroundColor' | 'color'\>\>

### `Stack.Toolbar.Button`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarButtonProps](#stacktoolbarbuttonprops)\>\>

StackToolbarButtonProps

### `accessibilityHint`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `accessibilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

There are two ways to specify the content of the button:

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="star.fill">As text passed as children</Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

Example

```tsx
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button>
          <Stack.Toolbar.Icon sf="star.fill" />
          <Stack.Toolbar.Label>As components</Stack.Toolbar.Label>
          <Stack.Toolbar.Badge>3</Stack.Toolbar.Badge>
        </Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}
```

> **Note**: When icon is used, the label will not be shown and will be used for accessibility purposes only. Badge is only supported in left/right placements, not in bottom (iOS toolbar limitation).

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the button should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Icon to display in the button.

Can be a string representing an SFSymbol or an image source.

> **Note**: When used in `placement="bottom"`, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display in the button.

> **Note**: This prop is only supported in toolbar with `placement="bottom"`.

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `() => void`

### `selected`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Whether the button is in a selected state

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/isselected) for more information

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: StyleProp<[TextStyle](https://reactnative.dev/docs/text-style-props)\>

Style for the label of the header item.

### `tintColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color to apply to the button item

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

### `variant`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `string` • Default: `'plain'`

Acceptable values are: `'done'` | `'prominent'` | `'plain'`

### `Stack.Toolbar.Icon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarIconProps](#stacktoolbariconprops)\>\>

StackToolbarIconProps

### `renderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how the image icon is rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors

Defaults based on parent component's `tintColor`:

-   With `tintColor`: defaults to `'template'`
-   Without `tintColor`: defaults to `'original'`

Acceptable values are: `'template'` | `'original'`

### `src`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)

### `sf`

Supported platforms: Android, iOS, tvOS, Web.

Type: [SFSymbol](https://github.com/nandorojo/sf-symbols-typescript)

### `xcasset`

Supported platforms: iOS.

Type: `string`

Name of an image in your Xcode asset catalog (`.xcassets`).

### `Stack.Toolbar.Label`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarLabelProps](#stacktoolbarlabelprops)\>\>

StackToolbarLabelProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

The text to display as the label for the tab.

### `Stack.Toolbar.Menu`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuProps](#stacktoolbarmenuprops)\>\>

StackToolbarMenuProps

### `accessibilityHint`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `accessibilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Menu content - can include icons, labels, badges and menu actions.

Example

```tsx
<Stack.Toolbar.Menu>
  <Stack.Toolbar.Icon sfSymbol="ellipsis.circle" />
  <Stack.Toolbar.Label>Options</Stack.Toolbar.Label>
  <Stack.Toolbar.MenuAction onPress={() => {}}>Action 1</Stack.Toolbar.MenuAction>
</Stack.Toolbar.Menu>
```

### `destructive`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `elementSize`

Supported platforms: iOS 16.0+.

Optional • Literal type: `string`

The preferred size of the menu elements.

> **Note**: This prop is only supported in `Stack.Toolbar.Bottom`.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize) for more information.

Acceptable values are: `'small'` | `'auto'` | `'medium'` | `'large'`

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the menu should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

> **See:** [Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Icon for the menu item.

Can be an SF Symbol name or an image source.

> **Note**: When used in `placement="bottom"`, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon (useful for monochrome icons)
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display for the menu item.

> **Note**: This prop is only supported in toolbar with `placement="bottom"`.

### `inline`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be displayed inline. This means that the menu will not be collapsed

> **Note**: Inline menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayinline) for more information.

### `palette`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be displayed as a palette. This means that the menu will be displayed as one row

> **Note**: Palette menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayaspalette) for more information.

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `StyleProp<BasicTextStyle>`

Style for the label of the header item.

### `tintColor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The tint color to apply to the button item

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

### `title`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

Optional title to show on top of the menu.

### `variant`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `string` • Default: `'plain'`

Acceptable values are: `'done'` | `'prominent'` | `'plain'`

### `Stack.Toolbar.MenuAction`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuActionProps](#stacktoolbarmenuactionprops)\>\>

StackToolbarMenuActionProps

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Can be an Icon, Label or string title.

### `destructive`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be disabled and not selectable.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/disabled) for more information.

### `discoverabilityLabel`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

An elaborated title that explains the purpose of the action.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

### `icon`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Literal type: `union`

Acceptable values are: [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

### `iconRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon (useful for monochrome icons)
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

**Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `image`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ImageRef`

Image to display for the menu action.

> **Note**: This prop is only supported in `Stack.Toolbar.Bottom`.

### `isOn`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as selected.

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `() => void`

### `subtitle`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

An optional subtitle for the menu item.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

### `unstable_keepPresented`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

If `true`, the menu will be kept presented after the action is selected.

This is marked as unstable, because when action is selected it will recreate the menu, which will close all opened submenus and reset the scroll position.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented) for more information.

### `Stack.Toolbar.SearchBarSlot`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSearchBarSlotProps](#stacktoolbarsearchbarslotprops)\>\>

StackToolbarSearchBarSlotProps

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the search bar slot should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

### `separateBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether this search bar slot has a separate background from adjacent items. When this prop is `true`, the search bar will always render as `integratedButton`.

In order to render the search bar with a separate background, ensure that adjacent toolbar items have `separateBackground` set to `true` or use `Stack.Toolbar.Spacer` to create spacing.

Example

```tsx
<Stack.SearchBar onChangeText={()=>{}} />
<Stack.Toolbar placement="bottom">
  <Stack.Toolbar.SearchBarSlot />
  <Stack.Toolbar.Spacer />
  <Stack.Toolbar.Button icon="square.and.pencil" />
</Stack.Toolbar>
```

### `Stack.Toolbar.Spacer`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSpacerProps](#stacktoolbarspacerprops)\>\>

StackToolbarSpacerProps

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the spacer should be hidden.

### `sharesBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether this spacer shares background with adjacent items.

Only available in bottom placement.

### `width`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `number`

The width of the spacing element.

In Left/Right placements, width is required. In Bottom placement, if width is not provided, the spacer will be flexible and expand to fill available space.

### `Stack.Toolbar.View`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarViewProps](#stacktoolbarviewprops)\>\>

StackToolbarViewProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom only) components.

### `placement`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

-   `'left'`: Renders items in the left area of the header.
-   `'right'`: Renders items in the right area of the header.
-   `'bottom'`: Renders items in the bottom toolbar (iOS only).

### `children`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `ReactElement<unknown, string | JSXElementConstructor<any>>`

Can be any React node.

### `hidden`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether the view should be hidden.

### `hidesSharedBackground`

Supported platforms: iOS 26+.

Optional • Type: `boolean`

Whether to hide the shared background.

> **See:** [Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `separateBackground`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean` • Default: `false`

Whether to separate the background of this item from other items.

Only available in bottom placement.

## Constants

### `Color`

Supported platforms: Android, iOS.

Type: [ColorType](#colortype)

Color utility to access platform-specific colors easily.

On **Android**, it provides access to:

-   System colors, as a type-safe wrapper over `PlatformColor`. For example, `Color.android.background`.
-   Attribute colors, as a type-safe wrapper over `PlatformColor`. For example, `Color.android.attr.colorPrimary`.
-   [Material Design 3 static colors](https://m3.material.io/styles/color/static/baseline). For example, `Color.android.material.primary`.
-   [Material Design 3 dynamic colors](https://m3.material.io/styles/color/dynamic/user-generated-source). For example, `Color.android.dynamic.primary`.

On **iOS**, it is a type-safe wrapper over `PlatformColor`, providing access to system colors. For example, `Color.ios.label`.

> **Note**: To ensure the colors align with the system theme on Android, make sure they are used within a component that responds to theme changes, such as by using the `useColorScheme` hook from React Native. This is especially important when using React Compiler, which can memoize components.

Example

```tsx
import { Color } from 'expo-router';

Color.ios.label; // Access iOS system color
Color.android.background; // Access Android system color
Color.android.attr.colorPrimary; // Access Android attribute color
Color.android.material.primary; // Access Android Material Design 3 static color
Color.android.dynamic.primary; // Access Android Material Design 3 dynamic color
```

Example

```tsx
import { Color } from 'expo-router';
import { View, Text, useColorScheme } from 'react-native';

export default function MyComponent() {
  useColorScheme(); // Ensure the app responds to system theme changes
  return (
    <View style={{ flex: 1, backgroundColor: Color.android.dynamic.primary }}>
      <Text style={{ color: Color.android.dynamic.onPrimary }}>
        Hello, World!
      </Text>
    </View>
  );
}
```

### `unstable_navigationEvents`

Supported platforms: Android, iOS, tvOS, Web.

Type: `{ addListener: (eventType: EventType, callback: (event: Payload<EventType>) => void) => () => void, emit: (type: EventType, event: Payload<EventType>) => void, enable: () => void, isEnabled: () => boolean, saveCurrentPathname: () => void, }`

## Hooks

### `useFocusEffect(effect, do_not_pass_a_second_prop)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `effect` | [EffectCallback](#effectcallback) | Memoized callback containing the effect, should optionally return a cleanup function. |
| `do_not_pass_a_second_prop`(optional) | `undefined` | - |

  

Hook to run an effect whenever a route is **focused**. Similar to [`React.useEffect`](https://react.dev/reference/react/useEffect).

This can be used to perform side-effects such as fetching data or subscribing to events. The passed callback should be wrapped in [`React.useCallback`](https://react.dev/reference/react/useCallback) to avoid running the effect too often.

Returns: `void`

Example

```tsx
import { useFocusEffect } from 'expo-router';
import { useCallback } from 'react';

export default function Route() {
  useFocusEffect(
    // Callback should be wrapped in `React.useCallback` to avoid running the effect too often.
    useCallback(() => {
      // Invoked whenever the route is focused.
      console.log("Hello, I'm focused!");

      // Return function is invoked whenever the route gets out of focus.
      return () => {
        console.log('This route is now unfocused.');
      };
    }, []),
   );

 return </>;
}
```

### `useGlobalSearchParams()`

Supported platforms: Android, iOS, tvOS, Web.

Returns URL parameters for globally selected route, including dynamic path segments. This function updates even when the route is not focused. Useful for analytics or other background operations that don't draw to the screen.

Route URL example: `acme://profile/baconbrix?extra=info`.

When querying search params in a stack, opt-towards using [`useLocalSearchParams`](#uselocalsearchparams) because it will only update when the route is focused.

> **Note:** For usage information, see [Local versus global search parameters](/router/reference/url-parameters#local-versus-global-url-parameters).

Returns: `RouteParams<troute> & TParams</troute>`

Example

```tsx
import { Text } from 'react-native';
import { useGlobalSearchParams } from 'expo-router';

export default function Route() {
  // user=baconbrix & extra=info
  const { user, extra } = useGlobalSearchParams();

  return <Text>User: {user}</Text>;
}
```

### `useIsPreview()`

Supported platforms: Android, iOS, tvOS, Web.

Hook to determine if the current route is rendered inside a preview.

Returns: `boolean`

-   True if the current route is rendered inside a preview, false otherwise.

### `useLoaderData()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the result of the `loader` function for the calling route.

Returns: `LoaderFunctionResult<t>`

Example

```tsx
import { Text } from 'react-native';
import { useLoaderData } from 'expo-router';

export function loader() {
  return Promise.resolve({ foo: 'bar' }};
}

export default function Route() {
 const data = useLoaderData<typeof loader>(); // { foo: 'bar' }

 return <Text>Data: {JSON.stringify(data)}</Text>;
}
```

### `useLocalSearchParams()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the URL parameters for the contextually focused route. Useful for stacks where you may push a new screen that changes the query parameters. For dynamic routes, both the route parameters and the search parameters are returned.

Route URL example: `acme://profile/baconbrix?extra=info`.

To observe updates even when the invoking route is not focused, use [`useGlobalSearchParams`](#useglobalsearchparams).

> **Note:** For usage information, see [Local versus global search parameters](/router/reference/url-parameters#local-versus-global-url-parameters).

Returns: `RouteParams<troute> & TParams</troute>`

Example

```tsx
import { Text } from 'react-native';
import { useLocalSearchParams } from 'expo-router';

export default function Route() {
 // user=baconbrix & extra=info
 const { user, extra } = useLocalSearchParams();

 return <Text>User: {user}</Text>;
}
```

### `useNavigation(parent)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `parent`(optional) | string | [HrefObject](#hrefobject) | Provide an absolute path such as `/(root)` to the parent route or a relative path like `. /. /` to the parent route. |

  

Returns the underlying React Navigation [`navigation` object](https://reactnavigation.org/docs/navigation-object) to imperatively access layout-specific functionality like `navigation.openDrawer()` in a [Drawer](/router/advanced/drawer) layout.

Returns: `T`

The navigation object for the current route.

> **See:** React Navigation documentation on [navigation dependent functions](https://reactnavigation.org/docs/navigation-object/#navigator-dependent-functions) for more information.

Example

```tsx
import { useNavigation } from 'expo-router';

export default function Route() {
  // Access the current navigation object for the current route.
  const navigation = useNavigation();

  return (
    <View>
      <Text onPress={() => {
        // Open the drawer view.
        navigation.openDrawer();
      }}>
        Open Drawer
      </Text>
    </View>
  );
}
```

When using nested layouts, you can access higher-order layouts by passing a secondary argument denoting the layout route. For example, `/menu/_layout.tsx` is nested inside `/app/orders/`, you can use `useNavigation('/orders/menu/')`.

Example

```tsx
import { useNavigation } from 'expo-router';

export default function MenuRoute() {
  const rootLayout = useNavigation('/');
  const ordersLayout = useNavigation('/orders');

  // Same as the default results of `useNavigation()` when invoked in this route.
  const parentLayout = useNavigation('/orders/menu');
}
```

If you attempt to access a layout that doesn't exist, an error such as `Could not find parent navigation with route "/non-existent"` is thrown.

### `useNavigationContainerRef()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `NavigationContainerRefWithCurrent<rootparamlist>`

The root `<NavigationContainer />` ref for the app. The `ref.current` may be `null` if the `<NavigationContainer />` hasn't mounted yet.

### `usePathname()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the currently selected route location without search parameters. For example, `/acme?foo=bar` returns `/acme`. Segments will be normalized. For example, `/[id]?id=normal` becomes `/normal`.

Returns: `string`

Example

```tsx
import { Text } from 'react-native';
import { usePathname } from 'expo-router';

export default function Route() {
  // pathname = "/profile/baconbrix"
  const pathname = usePathname();

  return <Text>Pathname: {pathname}</Text>;
}
```

### `usePreventZoomTransitionDismissal(_options)`

Supported platforms: iOS.

| Parameter | Type |
| --- | --- |
| `_options`(optional) | [UsePreventZoomTransitionDismissalOptions](#usepreventzoomtransitiondismissaloptions) |

  

Limits the screen area where interactive dismissal gestures are allowed for zoom transitions.

This hook must be called from the destination screen of a zoom transition (the screen you navigate to, not the source). It restricts where app users can start swipe gestures to dismiss the screen and return to the previous screen.

When a dismissal gesture starts inside the bounds, the screen can be dismissed. When a dismissal gesture starts outside the bounds, dismissal is blocked completely. Undefined coordinates place no restriction on that dimension.

> **Note**: Only one instance of this hook should be used per screen. If multiple instances exist, the last one to render will take effect.

Returns: `void`

Example

```tsx
// In your destination screen (e.g., app/image.tsx)
import { usePreventZoomTransitionDismissal } from 'expo-router';
import { useWindowDimensions } from 'react-native';
import { Image } from 'expo-image';

export default function ImageScreen() {
  const dimensions = useWindowDimensions();
  // Only allow dismissal from the bottom 200px of the screen
  usePreventZoomTransitionDismissal({
    unstable_dismissalBoundsRect: {
      minY: dimensions.height - 200
    }
  });

  return <Image source={...} style={{ flex: 1 }} />;
}
```

> **Deprecated:** Use [`useNavigationContainerRef`](#usenavigationcontainerref) instead, which returns a React `ref`.

### `useRootNavigation()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `NavigationContainerRef<rootparamlist> | null</rootparamlist>`

### `useRootNavigationState()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the [navigation state](https://reactnavigation.org/docs/navigation-state/) of the navigator which contains the current screen.

Returns: `Readonly<undefined>`

Example

```tsx
import { useRootNavigationState } from 'expo-router';

export default function Route() {
 const { routes } = useRootNavigationState();

 return <Text>{routes[0].name}</Text>;
}
```

### `useRouter()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the [Router](#router) object for imperative navigation.

Returns: `Router`

Example

```tsx
import { useRouter } from 'expo-router';
import { Text } from 'react-native';

export default function Route() {
 const router = useRouter();

 return (
  <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}
```

### `useSegments()`

Supported platforms: Android, iOS, tvOS, Web.

Returns a list of selected file segments for the currently selected route. Segments are not normalized, so they will be the same as the file path. For example, `/[id]?id=normal` becomes `["[id]"]`.

Returns: `RouteSegments<tsegments>`

Example

```tsx
import { Text } from 'react-native';
import { useSegments } from 'expo-router';

export default function Route() {
  // segments = ["profile", "[user]"]
  const segments = useSegments();

  return <Text>Hello</Text>;
}
```

`useSegments` can be typed using an abstract. Consider the following file structure:

```md
- app
  - [user]
    - index.tsx
    - followers.tsx
  - settings.tsx
```

This can be strictly typed using the following abstract with `useSegments` hook:

```tsx
const [first, second] = useSegments<['settings'] | ['[user]'] | ['[user]', 'followers']>()
```

### `useSitemap()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `SitemapType | null`

## Methods

### `Sitemap()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `Element`

### `withLayoutContext(Nav, processor, useOnlyUserDefinedScreens)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `Nav` | `T` | The navigator component to wrap. |
| `processor`(optional) | (options: [ScreenProps[]](#screenprops)) => [ScreenProps[]](#screenprops) | A function that processes the screens before passing them to the navigator. |
| `useOnlyUserDefinedScreens`(optional) | `boolean` | If true, all screens not specified as navigator's children will be ignored. Default: `false` |

  

Returns a navigator that automatically injects matched routes and renders nothing when there are no children. Return type with `children` prop optional.

Enables use of other built-in React Navigation navigators and other navigators built with the React Navigation custom navigator API.

Returns: `Component<propswithoutref>> & { Protected: FunctionComponent, Screen: (props: ScreenProps) => null }</propswithoutref`

Example

```tsx
import { ParamListBase, TabNavigationState } from "@react-navigation/native";
import {
  createMaterialTopTabNavigator,
  MaterialTopTabNavigationOptions,
  MaterialTopTabNavigationEventMap,
} from "@react-navigation/material-top-tabs";
import { withLayoutContext } from "expo-router";

const MaterialTopTabs = createMaterialTopTabNavigator();

const ExpoRouterMaterialTopTabs = withLayoutContext<
  MaterialTopTabNavigationOptions,
  typeof MaterialTopTabs.Navigator,
  TabNavigationState<ParamListBase>,
  MaterialTopTabNavigationEventMap
>(MaterialTopTabs.Navigator);

export default function TabLayout() {
  return <ExpoRouterMaterialTopTabs />;
}
```

## Interfaces

### `AndroidBaseColorSDK1`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/background_dark") |
| background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/background_light") |
| black | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/black") |
| darker_gray | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/darker_gray") |
| tab_indicator_text | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/tab_indicator_text") |
| transparent | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/transparent") |
| white | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/white") |
| widget_edittext_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/widget_edittext_dark") |

### `AndroidBaseColorSDK14`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| holo_blue_bright | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_bright") |
| holo_blue_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_dark") |
| holo_blue_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_light") |
| holo_green_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_green_dark") |
| holo_green_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_green_light") |
| holo_orange_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_orange_dark") |
| holo_orange_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_orange_light") |
| holo_purple | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_purple") |
| holo_red_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_red_dark") |
| holo_red_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_red_light") |

### `AndroidBaseColorSDK31`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| system_accent1_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_0") |
| system_accent1_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_10") |
| system_accent1_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_100") |
| system_accent1_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_1000") |
| system_accent1_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_200") |
| system_accent1_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_300") |
| system_accent1_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_400") |
| system_accent1_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_50") |
| system_accent1_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_500") |
| system_accent1_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_600") |
| system_accent1_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_700") |
| system_accent1_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_800") |
| system_accent1_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_900") |
| system_accent2_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_0") |
| system_accent2_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_10") |
| system_accent2_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_100") |
| system_accent2_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_1000") |
| system_accent2_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_200") |
| system_accent2_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_300") |
| system_accent2_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_400") |
| system_accent2_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_50") |
| system_accent2_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_500") |
| system_accent2_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_600") |
| system_accent2_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_700") |
| system_accent2_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_800") |
| system_accent2_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_900") |
| system_accent3_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_0") |
| system_accent3_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_10") |
| system_accent3_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_100") |
| system_accent3_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_1000") |
| system_accent3_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_200") |
| system_accent3_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_300") |
| system_accent3_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_400") |
| system_accent3_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_50") |
| system_accent3_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_500") |
| system_accent3_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_600") |
| system_accent3_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_700") |
| system_accent3_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_800") |
| system_accent3_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_900") |
| system_neutral1_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_0") |
| system_neutral1_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_10") |
| system_neutral1_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_100") |
| system_neutral1_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_1000") |
| system_neutral1_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_200") |
| system_neutral1_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_300") |
| system_neutral1_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_400") |
| system_neutral1_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_50") |
| system_neutral1_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_500") |
| system_neutral1_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_600") |
| system_neutral1_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_700") |
| system_neutral1_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_800") |
| system_neutral1_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_900") |
| system_neutral2_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_0") |
| system_neutral2_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_10") |
| system_neutral2_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_100") |
| system_neutral2_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_1000") |
| system_neutral2_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_200") |
| system_neutral2_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_300") |
| system_neutral2_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_400") |
| system_neutral2_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_50") |
| system_neutral2_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_500") |
| system_neutral2_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_600") |
| system_neutral2_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_700") |
| system_neutral2_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_800") |
| system_neutral2_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_900") |

### `AndroidBaseColorSDK34`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| system_background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_background_dark") |
| system_background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_background_light") |
| system_control_activated_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_activated_dark") |
| system_control_activated_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_activated_light") |
| system_control_highlight_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_highlight_dark") |
| system_control_highlight_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_highlight_light") |
| system_control_normal_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_normal_dark") |
| system_control_normal_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_normal_light") |
| system_error_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_container_dark") |
| system_error_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_container_light") |
| system_error_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_dark") |
| system_error_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_light") |
| system_on_background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_background_dark") |
| system_on_background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_background_light") |
| system_on_error_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_container_dark") |
| system_on_error_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_container_light") |
| system_on_error_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_dark") |
| system_on_error_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_light") |
| system_on_primary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_container_dark") |
| system_on_primary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_container_light") |
| system_on_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_dark") |
| system_on_primary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_fixed") |
| system_on_primary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_fixed_variant") |
| system_on_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_light") |
| system_on_secondary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_container_dark") |
| system_on_secondary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_container_light") |
| system_on_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_dark") |
| system_on_secondary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_fixed") |
| system_on_secondary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_fixed_variant") |
| system_on_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_light") |
| system_on_surface_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_dark") |
| system_on_surface_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_light") |
| system_on_surface_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_variant_dark") |
| system_on_surface_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_variant_light") |
| system_on_tertiary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_container_dark") |
| system_on_tertiary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_container_light") |
| system_on_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_dark") |
| system_on_tertiary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_fixed") |
| system_on_tertiary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_fixed_variant") |
| system_on_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_light") |
| system_outline_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_dark") |
| system_outline_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_light") |
| system_outline_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_variant_dark") |
| system_outline_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_variant_light") |
| system_palette_key_color_neutral_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_dark") |
| system_palette_key_color_neutral_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_light") |
| system_palette_key_color_neutral_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_variant_dark") |
| system_palette_key_color_neutral_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_variant_light") |
| system_palette_key_color_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_primary_dark") |
| system_palette_key_color_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_primary_light") |
| system_palette_key_color_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_secondary_dark") |
| system_palette_key_color_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_secondary_light") |
| system_palette_key_color_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_tertiary_dark") |
| system_palette_key_color_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_tertiary_light") |
| system_primary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_container_dark") |
| system_primary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_container_light") |
| system_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_dark") |
| system_primary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_fixed") |
| system_primary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_fixed_dim") |
| system_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_light") |
| system_secondary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_container_dark") |
| system_secondary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_container_light") |
| system_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_dark") |
| system_secondary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_fixed") |
| system_secondary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_fixed_dim") |
| system_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_light") |
| system_surface_bright_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_bright_dark") |
| system_surface_bright_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_bright_light") |
| system_surface_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_dark") |
| system_surface_container_high_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_high_dark") |
| system_surface_container_high_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_high_light") |
| system_surface_container_highest_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_highest_dark") |
| system_surface_container_highest_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_highest_light") |
| system_surface_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_light") |
| system_surface_container_low_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_low_dark") |
| system_surface_container_low_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_low_light") |
| system_surface_container_lowest_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_lowest_dark") |
| system_surface_container_lowest_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_lowest_light") |
| system_surface_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dark") |
| system_surface_dim_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dim_dark") |
| system_surface_dim_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dim_light") |
| system_surface_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_light") |
| system_surface_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_variant_dark") |
| system_surface_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_variant_light") |
| system_tertiary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_container_dark") |
| system_tertiary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_container_light") |
| system_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_dark") |
| system_tertiary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_fixed") |
| system_tertiary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_fixed_dim") |
| system_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_light") |
| system_text_hint_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_hint_inverse_dark") |
| system_text_hint_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_hint_inverse_light") |
| system_text_primary_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_dark") |
| system_text_primary_inverse_disable_only_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_disable_only_dark") |
| system_text_primary_inverse_disable_only_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_disable_only_light") |
| system_text_primary_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_light") |
| system_text_secondary_and_tertiary_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_dark") |
| system_text_secondary_and_tertiary_inverse_disabled_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_disabled_dark") |
| system_text_secondary_and_tertiary_inverse_disabled_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_disabled_light") |
| system_text_secondary_and_tertiary_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_light") |

### `AndroidBaseColorSDK35`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| system_error_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_0") |
| system_error_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_10") |
| system_error_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_100") |
| system_error_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_1000") |
| system_error_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_200") |
| system_error_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_300") |
| system_error_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_400") |
| system_error_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_50") |
| system_error_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_500") |
| system_error_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_600") |
| system_error_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_700") |
| system_error_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_800") |
| system_error_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_900") |
| system_on_surface_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_disabled") |
| system_outline_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_disabled") |
| system_surface_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_disabled") |

### `AndroidColorAttrSDK1`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackground") |
| colorForeground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorForeground") |
| colorForegroundInverse | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorForegroundInverse") |

### `AndroidColorAttrSDK14`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorActivatedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorActivatedHighlight") |
| colorFocusedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorFocusedHighlight") |
| colorLongPressedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorLongPressedHighlight") |
| colorMultiSelectHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorMultiSelectHighlight") |
| colorPressedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPressedHighlight") |

### `AndroidColorAttrSDK21`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorAccent | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorAccent") |
| colorButtonNormal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorButtonNormal") |
| colorControlActivated | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlActivated") |
| colorControlHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlHighlight") |
| colorControlNormal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlNormal") |
| colorEdgeEffect | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorEdgeEffect") |
| colorPrimary | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPrimary") |
| colorPrimaryDark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPrimaryDark") |

### `AndroidColorAttrSDK23`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorBackgroundFloating | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackgroundFloating") |

### `AndroidColorAttrSDK25`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorSecondary | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorSecondary") |

### `AndroidColorAttrSDK26`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorError | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorError") |
| colorMode | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorMode") |

### `AndroidColorAttrSDK5`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| colorBackgroundCacheHint | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackgroundCacheHint") |

### `AndroidDeprecatedColor`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| primary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_dark") |
| primary_text_dark_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_dark_nodisable") |
| primary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_light") |
| primary_text_light_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_light_nodisable") |
| secondary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_dark") |
| secondary_text_dark_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_dark_nodisable") |
| secondary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_light") |
| secondary_text_light_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_light_nodisable") |
| tertiary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/tertiary_text_dark") |
| tertiary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/tertiary_text_light") |

### `AndroidDynamicMaterialColorType`

Supported platforms: Android, iOS, tvOS, Web.

[Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source)

You can find out more about color roles in [official Material Design 3 documentation](https://m3.material.io/styles/color/roles).

You can read about the difference between dynamic and static colors in [official Material Design 3 documentation](https://m3.material.io/styles/color/choosing-a-scheme).

For a detailed definition of each color role, see [material components color documentation](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md).

| Property | Type | Description |
| --- | --- | --- |
| background | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. |
| error | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| errorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onBackground | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. |
| onError | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onErrorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onPrimary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onSecondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSurface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onSurfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| onSurfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onTertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| outline | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| outlineVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| primary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| secondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| surface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceBright | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHigh | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHighest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLow | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLowest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| surfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| tertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |

### `AndroidStaticMaterialColorType`

Supported platforms: Android, iOS, tvOS, Web.

[Android Static Material Colors](https://m3.material.io/styles/color/static/baseline)

You can find out more about color roles in [official Material Design 3 documentation](https://m3.material.io/styles/color/roles).

You can read about the difference between dynamic and static colors in [official Material Design 3 documentation](https://m3.material.io/styles/color/choosing-a-scheme).

For a detailed definition of each color role, see [material components color documentation](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md).

| Property | Type | Description |
| --- | --- | --- |
| background | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) |
| error | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| errorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onBackground | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) |
| onError | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onErrorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onPrimary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onSecondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSurface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onSurfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| onSurfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onTertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| outline | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| outlineVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| primary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| secondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| surface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceBright | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHigh | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHighest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLow | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLowest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| surfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| tertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |

### `ColorType`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| android | [AndroidBaseColorSDK1](#androidbasecolorsdk1) & [AndroidBaseColorSDK14](#androidbasecolorsdk14) & [AndroidBaseColorSDK31](#androidbasecolorsdk31) & [AndroidBaseColorSDK34](#androidbasecolorsdk34) & [AndroidBaseColorSDK35](#androidbasecolorsdk35) & [AndroidDeprecatedColor](#androiddeprecatedcolor) & undefined & { attr: [AndroidBaseColorAttr](#androidbasecolorattr), dynamic: [AndroidDynamicMaterialColor](#androiddynamicmaterialcolor), material: [AndroidMaterialColor](#androidmaterialcolor) } | - |
| ios | [IOSBaseColor](#iosbasecolor) & undefined | - |

### `DismissalBoundsRect`

Supported platforms: iOS.

Defines the screen bounds where interactive dismissal gestures are allowed for zoom transitions.

| Property | Type | Description |
| --- | --- | --- |
| maxX(optional) | `number` | Maximum X coordinate (right edge) where dismissal gestures are allowed. |
| maxY(optional) | `number` | Maximum Y coordinate (bottom edge) where dismissal gestures are allowed. |
| minX(optional) | `number` | Minimum X coordinate (left edge) where dismissal gestures are allowed. |
| minY(optional) | `number` | Minimum Y coordinate (top edge) where dismissal gestures are allowed. |

### `IOSBaseColor`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| darkText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("darkText") |
| label | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("label") |
| lightText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("lightText") |
| link | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("link") |
| opaqueSeparator | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("opaqueSeparator") |
| placeholderText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("placeholderText") |
| quaternaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("quaternaryLabel") |
| quaternarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("quaternarySystemFill") |
| secondaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondaryLabel") |
| secondarySystemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemBackground") |
| secondarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemFill") |
| secondarySystemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemGroupedBackground") |
| separator | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("separator") |
| systemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBackground") |
| systemBlue | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBlue") |
| systemBrown | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBrown") |
| systemCyan | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemCyan") |
| systemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemFill") |
| systemGray | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray") |
| systemGray2 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray2") |
| systemGray3 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray3") |
| systemGray4 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray4") |
| systemGray5 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray5") |
| systemGray6 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray6") |
| systemGreen | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGreen") |
| systemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGroupedBackground") |
| systemIndigo | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemIndigo") |
| systemMint | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemMint") |
| systemOrange | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemOrange") |
| systemPink | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemPink") |
| systemPurple | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemPurple") |
| systemRed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemRed") |
| systemTeal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemTeal") |
| systemYellow | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemYellow") |
| tertiaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiaryLabel") |
| tertiarySystemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemBackground") |
| tertiarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemFill") |
| tertiarySystemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemGroupedBackground") |

### `StackHeaderItemSharedProps`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| accessibilityHint(optional) | `string` | - |
| accessibilityLabel(optional) | `string` | - |
| children(optional) | [ReactNode](https://reactnative.dev/docs/react-node) | - |
| disabled(optional) | `boolean` | - |
| hidesSharedBackground(optional) | `boolean` | - |
| icon(optional) | [ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript) | - |
| iconRenderingMode(optional) | `'template' | 'original'` | Supported platforms: iOS. Controls how image-based icons are rendered on iOS.
-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors (useful for multi-color icons)

. **Default behavior:**

-   If `tintColor` is specified, defaults to `'template'`
-   If no `tintColor`, defaults to `'original'`

. This prop only affects image-based icons (not SF Symbols).See: Apple documentation for more information. |
| separateBackground(optional) | `boolean` | - |
| style(optional) | `StyleProp<BasicTextStyle>` | - |
| tintColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| variant(optional) | `'done' | 'prominent' | 'plain'` | Default: `'plain'` |

### `UsePreventZoomTransitionDismissalOptions`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| unstable_dismissalBoundsRect(optional) | [DismissalBoundsRect](#dismissalboundsrect) | Defines the screen bounds where interactive dismissal gestures are allowed. Each coordinate is optional. Undefined coordinates place no restriction on that dimension. For example, if only `minY` and `maxY` are defined, horizontal gestures are unrestricted while vertical gestures must stay within the Y bounds.See: Apple documentation for more information. |

## Types

### `AndroidBaseColor`

Supported platforms: Android, iOS, tvOS, Web.

Type: [AndroidBaseColorSDK1](#androidbasecolorsdk1) [AndroidBaseColorSDK14](#androidbasecolorsdk14) [AndroidBaseColorSDK31](#androidbasecolorsdk31) [AndroidBaseColorSDK34](#androidbasecolorsdk34) [AndroidBaseColorSDK35](#androidbasecolorsdk35) [AndroidDeprecatedColor](#androiddeprecatedcolor) extended by:

| Property | Type | Description |
| --- | --- | --- |

### `AndroidBaseColorAttr`

Supported platforms: Android, iOS, tvOS, Web.

Type: [AndroidColorAttrSDK1](#androidcolorattrsdk1) [AndroidColorAttrSDK5](#androidcolorattrsdk5) [AndroidColorAttrSDK14](#androidcolorattrsdk14) [AndroidColorAttrSDK21](#androidcolorattrsdk21) [AndroidColorAttrSDK23](#androidcolorattrsdk23) [AndroidColorAttrSDK25](#androidcolorattrsdk25) [AndroidColorAttrSDK26](#androidcolorattrsdk26) extended by:

| Property | Type | Description |
| --- | --- | --- |

### `AndroidDynamicMaterialColor`

Supported platforms: Android, iOS, tvOS, Web.

Type: [AndroidDynamicMaterialColorType](#androiddynamicmaterialcolortype) extended by:

| Property | Type | Description |
| --- | --- | --- |

### `AndroidMaterialColor`

Supported platforms: Android, iOS, tvOS, Web.

Type: [AndroidStaticMaterialColorType](#androidstaticmaterialcolortype) extended by:

| Property | Type | Description |
| --- | --- | --- |

### `EffectCallback()`

Supported platforms: Android, iOS, tvOS, Web.

Memoized callback containing the effect, should optionally return a cleanup function.

Returns:

`undefined | void | () => void`

### `ExternalPathString`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `{string}:{string}` | `//{string}`

### `Href<T>`

Supported platforms: Android, iOS, tvOS, Web.

The main routing type for Expo Router. It includes all available routes with strongly typed parameters. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

An Href can either be a string or an object.

Generic: `T`

Type: T ? T[href] : string | [HrefObject](#hrefobject)

### `HrefObject`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| params(optional) | `UnknownInputParams` | Optional parameters for the route. |
| pathname | `string` | The path of the route. |

### `NativeIntent`

Supported platforms: Android, iOS, tvOS, Web.

Created by using a special file called `+native-intent.tsx` at the top-level of your project's **app** directory. It exports `redirectSystemPath` or `legacy_subscribe` functions, both methods designed to handle URL/path processing.

Useful for re-writing URLs to correctly target a route when unique/referred URLs are incoming from third-party providers or stale URLs from previous versions.

> **See:** For more information on how to use `NativeIntent`, see [Customizing links](/router/advanced/native-intent).

| Property | Type | Description |
| --- | --- | --- |
| legacy_subscribe(optional) | `(listener: (url: string) => void) => undefined | void | () => void` | Useful as an alternative API when a third-party provider doesn't support Expo Router but has support for React Navigation via `Linking.subscribe()` for existing projects. Using this API is not recommended for newer projects or integrations since it is incompatible with Server Side Routing and [Static Rendering](/router/reference/static-rendering), and can become challenging to manage while offline or in a low network environment. |
| redirectSystemPath(optional) | (event: { initial: boolean, path: string }) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string | null\> | string | null | A special method used to process URLs in native apps. When invoked, it receives an `options` object with the following properties:
-   **path**: represents the URL or path undergoing processing.
-   **initial**: a boolean indicating whether the path is the app's initial URL.

. Its return value should be a `string`, a `Promise<string | null>`, or `null`. When a falsy value is returned (for example, `null`), no redirection occurs and the app stays on the current path. Note that throwing errors within this method may result in app crashes. It's recommended to wrap your code inside a `try/catch` block and utilize `.catch()` when appropriate.See: For usage information, see Redirecting system paths. |

### `PickPartial`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

The list of input keys will become optional, everything else will remain the same.

Acceptable values are: [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<T, K\> | [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<T, K\>\>

### `RedirectConfig`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| destination | `string` | - |
| destinationContextKey | `string` | - |
| external(optional) | `boolean` | - |
| methods(optional) | `string[]` | - |
| permanent(optional) | `boolean` | - |
| source | `string` | - |

### `RelativePathString`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `./{string}` | `../{string}` | `'..'`

### `ResultState`

Supported platforms: Android, iOS, tvOS, Web.

Type: PartialState<[NavigationState](https://reactnavigation.org/docs/navigation-state)\> extended by:

| Property | Type | Description |
| --- | --- | --- |
| state(optional) | [ResultState](#resultstate) | - |

### `Route`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<Extract[pathname], [RelativePathString](#relativepathstring) | [ExternalPathString](#externalpathstring)\>

### `Router`

Supported platforms: Android, iOS, tvOS, Web.

Returns `router` object for imperative navigation API.

Example

```tsx
import { router } from 'expo-router';
import { Text } from 'react-native';

export default function Route() {

 return (
  <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}
```

| Property | Type | Description |
| --- | --- | --- |
| back | `() => void` | Goes back in the navigation history. |
| canDismiss | `() => boolean` | Checks if it is possible to dismiss the current screen. Returns `true` if the router is within the stack with more than one screen in stack's history. |
| canGoBack | `() => boolean` | Navigates to a route in the navigator's history if it supports invoking the `back` function. |
| dismiss | `(count: number) => void` | Navigates to the a stack lower than the current screen using the provided count if possible, otherwise 1. If the current screen is the only route, it will dismiss the entire stack. |
| dismissAll | `() => void` | Returns to the first screen in the closest stack. This is similar to [`popToTop`](https://reactnavigation.org/docs/stack-actions/#poptotop) stack action. |
| dismissTo | (href: [Href](/versions/v55.0.0/sdk/router#href-1), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Dismisses screens until the provided href is reached. If the href is not found, it will instead replace the current screen with the provided `href`. |
| navigate | (href: [Href](/versions/v55.0.0/sdk/router#href-1), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to the provided [`href`](#href). |
| prefetch | (name: [Href](/versions/v55.0.0/sdk/router#href-1)) => void | Prefetch a screen in the background before navigating to it |
| push | (href: [Href](/versions/v55.0.0/sdk/router#href-1), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to the provided [`href`](#href) using a push operation if possible. |
| replace | (href: [Href](/versions/v55.0.0/sdk/router#href-1), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to route without appending to the history. Can be used with [`useFocusEffect`](#usefocuseffecteffect-do_not_pass_a_second_prop) to redirect imperatively to a new screen.See: Using useRouter() hook to redirect. |
| setParams | (params: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<RouteInputParams<T\>\>) => void | Updates the current route's query params. |

### `ScreenProps`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| dangerouslySingular(optional) | [SingularOptions](#singularoptions) | - |
| getId(optional) | `({ params }: { params: Record<string, any> }) => string | undefined` | - |
| initialParams(optional) | `Record<string, any>` | - |
| listeners(optional) | ScreenListeners<TState, TEventMap\> | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<TState, TEventMap\> | - |
| name(optional) | `string` | Name is required when used inside a Layout component. |
| options(optional) | TOptions | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => TOptions | - |
| redirect(optional) | `boolean` | Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render. |

### `SearchOrHash`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `?{string}` | `#{string}`

### `SingularOptions`

Supported platforms: Android, iOS, tvOS, Web.

Type: `boolean` or `object` shaped as below:

#### `` (name, params) => `string | undefined` ``

| Parameter | Type | Description |
| --- | --- | --- |
| name[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | `string` | - |
| params[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | `UnknownOutputParams` | - |

### `SitemapType`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| children | [SitemapType[]](#sitemaptype) | - |
| contextKey | `string` | - |
| filename | `string` | - |
| href | string | [Href](/versions/v55.0.0/sdk/router#href-1) | - |
| isGenerated | `boolean` | - |
| isInitial | `boolean` | - |
| isInternal | `boolean` | - |

### `WebAnchorProps`

Supported platforms: Web.

| Property | Type | Description |
| --- | --- | --- |
| download(optional) | `string` | Specifies that the [`href`](#href) should be downloaded when the user clicks on the link, instead of navigating to it. It is typically used for links that point to files that the user should download, such as PDFs, images, documents, and more. The value of the `download` property, which represents the filename for the downloaded file. This property is passed to the underlying anchor (`<a>`) tag. . Example
```jsx
<Link href="/image.jpg" download="my-image.jpg">Download image</Link>
```

 |
| rel(optional) | `string` | Specifies the relationship between the [`href`](#href) and the current route. Common values:

-   **nofollow**: Indicates to search engines that they should not follow the `href`. This is often used for user-generated content or links that should not influence search engine rankings.
-   **noopener**: Suggests that the `href` should not have access to the opening window's `window.opener` object, which is a security measure to prevent potentially harmful behavior in cases of links that open new tabs or windows.
-   **noreferrer**: Requests that the browser does not send the `Referer` HTTP header when navigating to the `href`. This can enhance user privacy.

. The `rel` property is primarily used for informational and instructive purposes, helping browsers and web crawlers make better decisions about how to handle and interpret the links on a web page. It is important to use appropriate `rel` values to ensure that links behave as intended and adhere to best practices for web development and SEO (Search Engine Optimization). This property is passed to the underlying anchor (`<a>`) tag. . Example

```jsx
<Link href="https://expo.dev" rel="nofollow">Go to Expo</Link>
```

 |
| target(optional) | `'_self' | '_blank' | '_parent' | '_top' | string & object` | Specifies where to open the [`href`](#href).

-   **_self**: the current tab.
-   **_blank**: opens in a new tab or window.
-   **_parent**: opens in the parent browsing context. If no parent, defaults to **_self**.
-   **_top**: opens in the highest browsing context ancestor. If no ancestors, defaults to **_self**.

. This property is passed to the underlying anchor (`<a>`) tag. Default: `'_self'`. Example

```jsx
<Link href="https://expo.dev" target="_blank">Go to Expo in new tab</Link>
```

 |
