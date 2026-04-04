# Source: https://docs.replit.com/extensions/api/messages.md

# messages API

> Display custom toast notifications in the Replit workspace using the messages API to show confirmations, errors, warnings, and notices.

The messages API allows you to send custom notices in the Replit workspace.

## Usage

```ts  theme={null}
import { messages } from '@replit/extensions';
```

## Methods

### `messages.showConfirm`

Shows a confirmation toast message within the Replit workspace for `length` milliseconds. Returns the ID of the message as a UUID

```ts  theme={null}
showConfirm(str: string, length: number): Promise<string>
```

### `messages.showError`

Shows an error toast message within the Replit workspace for `length` milliseconds. Returns the ID of the message as a UUID

```ts  theme={null}
showError(str: string, length: number): Promise<string>
```

### `messages.showNotice`

Shows a notice toast message within the Replit workspace for `length` milliseconds. Returns the ID of the message as a UUID

```ts  theme={null}
showNotice(str: string, length: number): Promise<string>
```

### `messages.showWarning`

Shows a warning toast message within the Replit workspace for `length` milliseconds. Returns the ID of the message as a UUID

```ts  theme={null}
showWarning(str: string, length: number): Promise<string>
```

### `messages.hideMessage`

Hides a message by its IDs

```ts  theme={null}
hideMessage(id: string): Promise<void>
```

### `messages.hideAllMessages`

Hides all toast messages visible on the screens

```ts  theme={null}
hideAllMessages(): Promise<void>
```
