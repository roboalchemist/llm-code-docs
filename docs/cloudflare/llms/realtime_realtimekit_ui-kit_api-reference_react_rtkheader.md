# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/index.md

---

title: RtkHeader · Cloudflare Realtime docs
description: API reference for RtkHeader component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkheader/index.md
---

A component that houses all the header components.

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
import { RtkHeader } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkHeader />;
}
```

### With Properties

```tsx
import { RtkHeader } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkHeader
      disableRender={true}
      meeting={meeting}
      size="md"
    />
  );
}
```
