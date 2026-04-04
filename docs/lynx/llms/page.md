# Source: https://lynxjs.org/api/elements/built-in/page.md

# `<page>`

`<page>` element is the root node, only one `<page>` element is allowed per page. You can omit the explicit `<page>` wrapper, as the frontend framework will generate the root node by default.

## Usage

### Omitting the `<page>` Element

By default, you don't need to manually add the `<page>` element as the frontend framework generates the root node automatically.

In this case, while direct `style` and `class` attributes cannot be set explicitly, you can still style the root node using [`page`](/api/css/selectors.md#using-page-to-select-the-root-node) and [`:root`](/api/css/selectors.md#root-selector) selectors, or select it via [`SelectorQuery:selectRoot()`](/api/lynx-api/selector-query/selector-query-select-root.md).

```css
/* use `page` selector */
page {
  background-color: white;
}

/* or you can use `:root` selector */
:root {
  background-color: white;
}
```

**This is an example below:  page**

**Entry:** `src/no_page_tag/`
**Bundle:** `dist/no_page_tag.lynx.bundle` | Web: `dist/no_page_tag.web.bundle`

```scss {1-3,5-8}
:root {
  background: linear-gradient(120deg, rgb(255, 53, 26), rgb(0, 235, 235));
}

page {
  border: 10px solid black;
  border-radius: 20px;
}

.title {
  font-size: 20px;
  font-weight: bold;
}

```



### Using `<page>` Element Explicitly

For more flexibility in styling the root node or binding events, you can add `<page>` as the outermost element. It works similarly to `<view>` and supports all its styles and attributes except for `width`, `height`, and `position`. See [No Direct Size Modification](#no-direct-size-modification) for details.

```jsx {3,7}
const App = () => {
  return (
    <page className="body" bindtap={handlePageClick}>
      <view style={{ width: '100%', height: '100%' }}>
        <text className="title">Page Example</text>
      </view>
    </page>
  );
};
```

Similar to `<view>`, you can add `style`, `class` and bind events to `<page>`. Note that you can only have one `<page>` element.

**This is an example below:  page**

**Entry:** `src/with_page_tag/`
**Bundle:** `dist/no_page_tag.lynx.bundle` | Web: `dist/no_page_tag.web.bundle`

```tsx {13,29}
import { root } from "@lynx-js/react";
import { useState } from "react";
import "./index.scss";

const App = () => {
  const [showPopup, setShowPopup] = useState(false);

  const handlePageClick = () => {
    setShowPopup(prev => !prev);
  };

  return (
    <page className="container" bindtap={handlePageClick}>
      <view
        style={{
          width: "100%",
          height: "100%",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <text className="title">Use Page Element Example, Click it</text>
      </view>
      {showPopup && (
        <view className="popup">
          <text className="popup-text">Click Response</text>
        </view>
      )}
    </page>
  );
};

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### No Direct Size Modification

The size constraints of `<page>` element are specified by its parent [native view](/guide/embed-lynx-to-native.md#Constraining-LynxView). You cannot directly modify its `width`, `height`, `left`, or `top` styles through `style` or `class`. This design allows Lynx pages to be embedded into native views, enabling better adaptation to the native app's layout flow.
