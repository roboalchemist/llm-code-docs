# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/index.md

---

title: RtkEmojiPickerButton · Cloudflare Realtime docs
description: API reference for RtkEmojiPickerButton component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipickerbutton/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isActive` | `boolean` | ✅ | - | Active state indicator |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkEmojiPickerButton />;
}
```

### With Properties

```tsx
import { RtkEmojiPickerButton } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkEmojiPickerButton
      isActive={true}
    />
  );
}
```
