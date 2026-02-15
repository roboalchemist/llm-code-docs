# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/index.md

---

title: RtkCameraToggle · Cloudflare Realtime docs
description: API reference for RtkCameraToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/index.md
---

A button which toggles your camera.

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
import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkCameraToggle />;
}
```

### With Properties

```tsx
import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkCameraToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
