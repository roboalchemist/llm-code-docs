# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/index.md

---

title: RtkStageToggle · Cloudflare Realtime docs
description: API reference for RtkStageToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkStageToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkStageToggle />;
}
```

### With Properties

```tsx
import { RtkStageToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkStageToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
