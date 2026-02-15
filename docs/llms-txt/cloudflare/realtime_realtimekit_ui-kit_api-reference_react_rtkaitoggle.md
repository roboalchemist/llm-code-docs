# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/index.md

---

title: RtkAiToggle · Cloudflare Realtime docs
description: API reference for RtkAiToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/index.md
---

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
import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkAiToggle />;
}
```

### With Properties

```tsx
import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkAiToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
