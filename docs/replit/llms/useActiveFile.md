# Source: https://docs.replit.com/extensions/development/react/hooks/useActiveFile.md

# useActiveFile() Hook

> The useActiveFile() hook returns the file actively focused on by the current user.

## Usage

```tsx  theme={null}
import { useActiveFile } from "@replit/extensions-react";

const Component = () => {
  const activeFile = useActiveFile();

  return (
    <>
      <span>Active File: {activeFile}</span>
    </>
  );
};
```

## Signature

```ts  theme={null}
function useActiveFile(): string | null;
```
