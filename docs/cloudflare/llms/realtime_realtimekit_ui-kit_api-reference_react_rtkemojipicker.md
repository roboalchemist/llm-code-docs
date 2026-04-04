# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/index.md

---

title: RtkEmojiPicker · Cloudflare Realtime docs
description: API reference for RtkEmojiPicker component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkemojipicker/index.md
---

A very simple emoji picker component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkEmojiPicker />;
}
```

### With Properties

```tsx
import { RtkEmojiPicker } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkEmojiPicker
      focusWhenOpened={true}
    />
  );
}
```
