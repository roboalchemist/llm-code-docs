# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/index.md

---

title: RtkPluginMain · Cloudflare Realtime docs
description: API reference for RtkPluginMain component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginmain/index.md
---

A component which loads a plugin.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `plugin` | `RTKPlugin` | ✅ | - | Plugin |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPluginMain />;
}
```

### With Properties

```tsx
import { RtkPluginMain } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPluginMain
      meeting={meeting}
      plugin={rtkplugin}
    />
  );
}
```
