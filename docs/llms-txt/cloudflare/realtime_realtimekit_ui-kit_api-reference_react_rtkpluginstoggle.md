# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/index.md

---

title: RtkPluginsToggle · Cloudflare Realtime docs
description: API reference for RtkPluginsToggle component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/index.md
---

A button which toggles visibility of plugins. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'plugins' }
```

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
import { RtkPluginsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPluginsToggle />;
}
```

### With Properties

```tsx
import { RtkPluginsToggle } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPluginsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
