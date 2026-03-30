# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/index.md

---

title: RtkChat · Cloudflare Realtime docs
description: API reference for RtkChat component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/index.md
---

Fully featured chat component with image & file upload, emoji picker and auto-scroll.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Overrides |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChat } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkChat />;
}
```

### With Properties

```tsx
import { RtkChat } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkChat
      meeting={meeting}
      size="md"
    />
  );
}
```
