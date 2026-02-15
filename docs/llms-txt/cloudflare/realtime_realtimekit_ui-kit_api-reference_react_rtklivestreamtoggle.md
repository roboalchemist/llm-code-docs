# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/index.md

---

title: RtkLivestreamToggle · Cloudflare Realtime docs
description: API reference for RtkLivestreamToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkLivestreamToggle />;
}
```

### With Properties

```tsx
import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkLivestreamToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
