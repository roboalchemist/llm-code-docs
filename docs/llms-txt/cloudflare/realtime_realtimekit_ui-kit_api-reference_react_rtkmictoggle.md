# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/index.md

---

title: RtkMicToggle · Cloudflare Realtime docs
description: API reference for RtkMicToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/index.md
---

A button which toggles your microphone.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMicToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMicToggle />;
}
```

### With Properties

```tsx
import { RtkMicToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMicToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
