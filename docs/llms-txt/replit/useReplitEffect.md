# Source: https://docs.replit.com/extensions/development/react/hooks/useReplitEffect.md

# useReplitEffect() Hook

> The `useReplitEffect()` hook fires a callback with the `replit` API wrapper upon the first component render and when its dependency array changes. It is similar in functionality to the `useEffect` React hook.

## Usage

```ts  theme={null}
import { useReplitEffect } from '@replit/extensions-react';

const Component = () => {
  useReplitEffect(async (replit) => {
    ...
  }, [...dependencies]);

  ...
}
```

## Signature

```ts  theme={null}
function useReplitEffect(
  callback: (typeof replit) => Promise<void>;
  dependencies: Array<any>
): null;
```
