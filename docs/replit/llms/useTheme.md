# Source: https://docs.replit.com/extensions/development/react/hooks/useTheme.md

# useTheme() Hook

> The `useTheme()` hook returns all metadata on the current theme including syntax highlighting, description, HSL, token values, and more.

## Usage

```ts  theme={null}
import { useTheme } from '@replit/extensions-react';

const Component = () => {
  const theme = useTheme();

  ...
}
```

## Signature

```ts  theme={null}
function useThemeValues(): ThemeVersion | null;
```

## Types

### [ThemeVersion](../../../api/themes.md#themeversion)

A specific theme version reflecting all colors and metadata on the current theme.
