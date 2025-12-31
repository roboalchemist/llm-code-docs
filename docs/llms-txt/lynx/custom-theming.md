# Source: https://lynxjs.org/guide/styling/custom-theming.md

# Theming

Lynx supports a wide range of [CSS properties](/api/css/properties.md), enabling seamless integration with [CSS selectors](/api/css/selectors.md), [CSS variables](/api/css/properties/css-variable.md), and opt-in CSS inheritance. By defining and managing different theme variables, developers can easily switch between various color schemes, font styles, and other visual elements, ensuring an optimal visual experience and interaction for users.

## Using CSS Descendant Selectors to Switch Themes

Similar to web development, using descendant selectors by toggling the class of a parent element can affect the styles of all its descendant nodes, thus enabling the switching of multiple theme styles.

### Defining CSS Themes

First, multiple theme CSS styles need to be defined, with different themes having different properties such as colors and backgrounds. For example, we can define both light and dark theme styles, with the light mode defined using `.theme-light .content` and the dark mode defined using `.theme-dark .content`.

```css
/* light theme */
.theme-light .content {
  color: black;
  background-color: white;
}

/* dark theme */
.theme-dark .content {
  color: white;
  background-color: black;
}
```

### Applying CSS Styles

In the page, set the class of the ancestor node (can be defined in the [`page`](/api/elements/built-in/page.md#using-page-element-explicitly)) to `theme-dark` or `theme-light`, and set the class of the descendant nodes to `content`. In this way, the descendant nodes can be styled with `.theme-light .content` or `.theme-dark .content` styles.

```tsx
function App() {
  return (
    <view className="theme-dark">
      <view>
        <text className="content">text</text>
      </view>
    </view>
  );
}
```

### Switching Theme Styles

When the theme changes, switch the class of the ancestor node to `theme-dark` or `theme-light`, which will update the styles of the descendant nodes. In the Lynx development scenario, the front-end themes can be notified by the native client. For example, the native client can notify the front-end of theme changes by updating [globalProps](/api/lynx-api/lynx/lynx-global-props.md).

The corresponding front-end implementation:

```tsx
import { useMemo } from '@lynx-js/react';
import './App.css';

export function App() {
  const themeClass = useMemo(
    () => `theme-${lynx.__globalProps.appTheme}`,
    [lynx.__globalProps.appTheme],
  );

  return (
    //themeClass's value is 'theme-dark' or 'theme-light'
    <view className={themeClass}>
      <view>
        ...
        <text className="content">Hello Theme</text>
        ...
      </view>
    </view>
  );
}
```

### Example

**This is an example below:  css**

**Entry:** `src/descendant_selectors_theme`
**Bundle:** `dist/descendant_selectors_theme.lynx.bundle` | Web: `dist/descendant_selectors_theme.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import { useState } from "react";
import "./index.scss";

export default function App() {
  const [isDark, setIsDark] = useState(false);
  const themeClass = isDark ? "theme-dark" : "theme-light";

  const toggleTheme = () => {
    setIsDark(prev => !prev);
  };

  return (
    <view className={themeClass}>
      <view className="container">
        <view className="theme-card" bindtap={toggleTheme}>
          <text className="theme-icon">
            {isDark ? "🌙" : "☀️"}
          </text>
          <text className="title">
            {isDark ? "Dark Mode" : "Light Mode"}
          </text>
          <text className="subtitle">
            Tap to switch theme
          </text>
        </view>
        <view className="content-cards">
          <view className="card">
            <text className="card-title">Card Sample 1</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 2</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 3</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 4</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
        </view>
      </view>
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Using CSS Variables to Switch Themes

When using descendant selectors for theme switching, we need to predefine selectors for different theme styles, which lacks flexibility when dealing with multiple themes.

Using [CSS Variable](/api/css/properties/css-variable.md) to define theme styles and achieve theme switching by directly modifying the variable values.

### Defining CSS Themes

Similarly, we define the theme style variables that need to change and assign different values to the same variables.

For example, under different themes, `color` and `background-color` need to change with the theme. Therefore, two CSS variables `--color` and `--bg` need to be defined.

The descendant nodes can obtain the values of these variables in the stylesheet using `var(--color)` and `var(--bg)`.

```css
.theme-light {
  --color: black;
  --bg: white;
}

.content {
  color: var(--color);
  background-color: var(--bg);
}
```

### Applying CSS Styles

Note that CSS variables need to be mounted on the ancestor node (can be defined in the [`page`](/api/elements/built-in/page.md#using-page-element-explicitly)) so that their descendant nodes can use these variables in their respective stylesheets.

The descendant nodes can apply the values of these variables in `.content` using the `var(--*)` syntax.

```tsx
function App() {
  return (
    <view id="root" className="theme-light">
      <view>
        <text className="content">text</text>
      </view>
    </view>
  );
}
```

### Switching Theme Styles

#### Directly Changing CSS Variable Values with JS

Use JS API ([`setProperty`](/api/css/properties/css-variable.md#modifying-css-variables-via-javascript-api)) to directly modify CSS variable values, allowing flexible batch updates of CSS variables.

```tsx
import './App.css';

export function App() {
  const handleClick = () => {
    lynx.getElementById('root').setProperty({
      '--color': 'white',
      '--bg': 'black',
    });
  };

  return (
    <view id="root" className="theme-light" bindtap={handleClick}>
      <text className="content">Hello Variable</text>
    </view>
  );
}
```

#### Indirectly Changing Variable Values by Switching Classes

Alternatively, you can indirectly modify variable values by switching classes on the ancestor node that define different [CSS variables](/api/css/properties/css-variable.md#modifying-the-selector-that-declares-css-variables), triggering style updates for all child nodes using these variables when theme switching is needed.

For example, use `.theme-light` and `.theme-dark` to define CSS variable values for different themes:

```css
.theme-light {
  --color: black;
  --bg: white;
}

.theme-dark {
  --color: white;
  --bg: black;
}

.content {
  color: var(--color);
  background-color: var(--bg);
}
```

Switching between `.theme-light` or `.theme-dark` on the ancestor node changes the values of `--color` and `--bg`, which updates the styles for corresponding `.content` elements.

```tsx
import { useMemo } from '@lynx-js/react';

import './App.css';

export function App() {
  const themeClass = useMemo(
    () => `theme-${lynx.__globalProps.appTheme}`,
    [lynx.__globalProps.appTheme],
  );

  return (
    //themeClass's value is 'theme-dark' or 'theme-light'
    <view className={themeClass}>
      <text id="test" className="content">
        Hello Variable
      </text>
    </view>
  );
}
```

### Example

**This is an example below:  css**

**Entry:** `src/css_variable_theme`
**Bundle:** `dist/css_variable_theme.lynx.bundle` | Web: `dist/css_variable_theme.web.bundle`

```tsx {23-43}
import { root } from "@lynx-js/react";
import { useState } from "react";
import "./index.scss";

export default function App() {
  const [isDark, setIsDark] = useState(false);
  const [useJS, setUseJS] = useState(false);
  const [showError, setShowError] = useState(false);
  const themeClass = isDark ? "theme-dark" : "theme-light";

  const toggleTheme = () => {
    if (useJS) {
      setShowError(true);
      setTimeout(() => setShowError(false), 3000);
      return;
    }

    setIsDark(prev => !prev);
  };

  const toggleThemeByJS = () => {
    setUseJS(true);
    const rootElement = lynx.getElementById("root");
    const newTheme = isDark ? "light" : "dark";

    if (rootElement) {
      if (isDark) {
        rootElement.setProperty({
          "--bg-primary": "#ffffff",
          "--bg-secondary": "#f5f5f5",
          "--text-primary": "#1a1a1a",
          "--text-secondary": "#666666",
          "--shadow": "rgba(0, 0, 0, 0.1)",
        });
      } else {
        rootElement.setProperty({
          "--bg-primary": "#2d2d2d",
          "--bg-secondary": "#1a1a1a",
          "--text-primary": "#ffffff",
          "--text-secondary": "#cccccc",
          "--shadow": "rgba(0, 0, 0, 0.3)",
        });
      }
      setIsDark(prev => !prev);
    }
  };

  return (
    <view id="root" className={themeClass}>
      <view className="container">
        <view className="theme-switchers">
          <view className="theme-card" bindtap={toggleTheme}>
            <text className="theme-icon">{isDark ? "🌙" : "☀️"}</text>
            <text className="title">{isDark ? "Dark Mode" : "Light Mode"}</text>
            <text className="subtitle">Tap to switch theme by className</text>
          </view>
          <view className="theme-card" bindtap={toggleThemeByJS}>
            <text className="theme-icon">{isDark ? "🌙" : "☀️"}</text>
            <text className="title">{isDark ? "Dark Mode" : "Light Mode"}</text>
            <text className="subtitle">Tap to switch theme through JS</text>
          </view>
        </view>
        <view className="content-cards">
          <view className="card">
            <text className="card-title">Card Sample 1</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 2</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 3</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
          <view className="card">
            <text className="card-title">Card Sample 4</text>
            <text className="card-text">This is a demo card showing theme switching effects.</text>
          </view>
        </view>
      </view>
      {showError && (
        <view className="error-message-container">
          <text className="error-message">
            Cannot change variables through the class after modifying them in JS!
          </text>
        </view>
      )}
    </view>
  );
}

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Leveraging CSS Inheritance As Needed

In pages with complex styles, using CSS inheritance can simplify development. However, implementing inheritance logic adds complexity to the style processing flow and can introduce some performance overhead. To optimize performance, Lynx does not enable inheritance for ordinary CSS properties by default, developers must enable it as needed. CSS custom properties (also known as CSS variables) are inherited by descendant nodes by default.

### Inheritance of CSS Custom Properties

[CSS Custom Properties](/api/css/properties/css-variable.md) (CSS variables, e.g., `--primary-color`) adhere to Web standards and are inherited by descendant nodes by default without additional configuration. Developers can define CSS custom properties in ancestor nodes to achieve dynamic style management.

### Inheritance of Regular (Non-Custom) Properties

To enable inheritance, configure[`enableCSSInheritance`](/api/rspeedy/react-rsbuild-plugin.pluginreactlynxoptions.enablecssinheritance.md).

#### Default-Inheritable Properties

After enabling `enableCSSInheritance`, these properties can be inherited:

[`direction`](/api/css/properties/direction.md),[`color`](/api/css/properties/color.md),[`font-family`](/api/css/properties/font-family.md),[`font-size`](/api/css/properties/font-size.md),[`font-style`](/api/css/properties/font-style.md),[`font-weight`](/api/css/properties/font-weight.md),[`letter-spacing`](/api/css/properties/letter-spacing.md),[`line-height`](/api/css/properties/line-height.md),[`text-align`](/api/css/properties/text-align.md),[`text-decoration`](/api/css/properties/text-decoration.md),[`text-shadow`](/api/css/properties/text-shadow.md)

Default inherited properties inherit behavior alignment with [🌐W3C definition](https://www.w3.org/TR/css-cascade-3/#inheriting)

#### Custom-Inheritable Properties

In addition to the default inheritable properties, you can configure the page with [`customCSSInheritanceList`](/api/rspeedy/react-rsbuild-plugin.pluginreactlynxoptions.customcssinheritancelist.md)to define custom inheritable CSS properties. When there are custom inheritance declarations, only the CSS properties listed in the `customCSSInheritanceList` will be inheritable.

Example:

```json
"customCSSInheritanceList":["font-size","flex-direction"]
```

#### Limitations of CSS Inheritance

1. Elements with `position: fixed` will always inherit properties only from the page.
2. The keyword "inherit" is not supported.
3. In addition to the default inheritable properties, only CSS properties with types enum or boolean support custom inheritance.
