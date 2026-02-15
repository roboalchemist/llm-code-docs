# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/index.md

---

title: RtkControlbar · Cloudflare Realtime docs
description: API reference for RtkControlbar component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/index.md
---

Controlbar component provides you with various designs as variants.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `disableRender` | `boolean` | ✅ | - | Whether to render the default UI |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'boxed'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkControlbar />;
}
```

### With Properties

```tsx
import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkControlbar
      disableRender={true}
      meeting={meeting}
      size="md"
    />
  );
}
```
