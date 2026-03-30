# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/index.md

---

title: RtkBreakoutRoomsToggle · Cloudflare Realtime docs
description: API reference for RtkBreakoutRoomsToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/index.md
---

A button which toggles visibility of breakout rooms. You need to pass the `meeting` object to it.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ✅ | - | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ✅ | - | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkBreakoutRoomsToggle />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkBreakoutRoomsToggle
      iconPack={defaultIconPack}
      meeting={meeting}
      size="md"
    />
  );
}
```
