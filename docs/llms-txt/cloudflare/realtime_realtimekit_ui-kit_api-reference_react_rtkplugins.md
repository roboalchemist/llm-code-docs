# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/index.md

---

title: RtkPlugins · Cloudflare Realtime docs
description: API reference for RtkPlugins component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkplugins/index.md
---

A component which lists all available plugins from their preset, and ability to enable or disable plugins.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPlugins } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPlugins />;
}
```

### With Properties

```tsx
import { RtkPlugins } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPlugins
      meeting={meeting}
      size="md"
    />
  );
}
```
