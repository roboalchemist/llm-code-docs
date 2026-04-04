# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/index.md

---

title: RtkDebuggerToggle · Cloudflare Realtime docs
description: API reference for RtkDebuggerToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/index.md
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
import { RtkDebuggerToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkDebuggerToggle />;
}
```

### With Properties

```tsx
import { RtkDebuggerToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkDebuggerToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
