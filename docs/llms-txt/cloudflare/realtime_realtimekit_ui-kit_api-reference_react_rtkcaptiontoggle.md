# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/index.md

---

title: RtkCaptionToggle · Cloudflare Realtime docs
description: API reference for RtkCaptionToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkCaptionToggle />;
}
```

### With Properties

```tsx
import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkCaptionToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
