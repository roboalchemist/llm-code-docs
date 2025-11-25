# Source: https://docs.replit.com/extensions/development/react/hooks/useThemeValues.md

# useThemeValues() Hook

> The `useThemeValues()` hook provides you with the global token color values of the current user's theme.

## Usage

```ts  theme={null}
import { useThemeValues } from '@replit/extensions-react';

const Component = () => {
  const themeValues = useThemeValues();

  ...
}
```

## Signature

```ts  theme={null}
function useThemeValues(): ThemeValuesGlobal | null;
```

## Types

### [ThemeValuesGlobal](../../../api/themes.md#themevaluesglobal)

Replit's global theme token values for UI, excluding syntax highlighting.
