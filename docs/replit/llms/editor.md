# Source: https://docs.replit.com/extensions/api/editor.md

# editor API

> Access and manage editor preferences in Replit Apps using the editor API module. Get settings like font size, indentation, and code intelligence.

The `editor` api module allows you to get the current user's editor preferences.

## Usage

```ts  theme={null}
import { experimental } from '@replit/extensions';
const { editor } = experimental;
```

## Methods

### `editor.getPreferences`

Returns the current user's editor preferences.

```ts  theme={null}
getPreferences(): Promise<EditorPreferences>
```

## Types

### EditorPreferences

Editor Preferences

| Property               | Type      |
| ---------------------- | --------- |
| \_\_typename           | `string`  |
| codeIntelligence       | `boolean` |
| codeSuggestion         | `boolean` |
| fontSize               | `number`  |
| indentIsSpaces         | `boolean` |
| indentSize             | `number`  |
| keyboardHandler        | `string`  |
| minimapDisplay         | `string`  |
| multiselectModifierKey | `string`  |
| wrapping               | `boolean` |
