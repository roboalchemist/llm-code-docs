# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/index.md

---

title: RtkScreenShareToggle · Cloudflare Realtime docs
description: API reference for RtkScreenShareToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/index.md
---

A button which toggles your screenshare.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkScreenShareToggle />;
}
```

### With Properties

```tsx
import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkScreenShareToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
