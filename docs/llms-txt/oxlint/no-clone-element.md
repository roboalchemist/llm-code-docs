# Source: https://oxc.rs/docs/guide/usage/linter/rules/react/no-clone-element.md

---
url: /docs/guide/usage/linter/rules/react/no-clone-element.md
---

### What it does

Prevents the usage of `React.cloneElement`, which is considered an anti-pattern in React.

### Why is this bad?

It is recommended not to use `React.cloneElement` because it can lead to code that is
harder to follow and understand. It is generally uncommon and fragile, and there are various
alternatives recommended by
[the React documentation](https://react.dev/reference/react/cloneElement#alternatives).

Note that this rule is based on [`@eslint-react/no-clone-element`](https://www.eslint-react.xyz/docs/rules/no-clone-element)
from `@eslint-react`, not a rule from `eslint-plugin-react`.

### Examples

Examples of **incorrect** code for this rule:

```jsx
import { cloneElement } from "react";

function List({ children }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  return (
    <div className="List">
      {Children.map(children, (child, index) =>
        cloneElement(child, {
          isHighlighted: index === selectedIndex,
        }),
      )}
    </div>
  );
}
```

Examples of **correct** code for this rule:

```jsx
// Using a map with a `renderItem` function prop instead.
function List({ items, renderItem }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  return (
    <div className="List">
      {items.map((item, index) => {
        const isHighlighted = index === selectedIndex;
        return renderItem(item, isHighlighted);
      })}
    </div>
  );
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["react"],
  "rules": {
    "react/no-clone-element": "error"
  }
}
```

```bash [CLI]
oxlint --deny react/no-clone-element --react-plugin
```

:::

## References

* Rule Source
